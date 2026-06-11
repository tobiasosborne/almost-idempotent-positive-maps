#!/usr/bin/env python3
"""
w16_nlopt_search.py

End-to-end nonlinear search over exact signed idempotents

    P = Lambda R,   R Lambda = I_k,
    Lambda = [I_k; X],   R = [I_k - Q X | Q],

with each row of X summing to one.  This is the requested P = L B,
B L = I parametrization, written in a gauge where the first k rows of L
are the identity.  Row-stochasticity follows from X 1 = 1.

The script reuses the w15 verifier, then adds:
  * direct nonlinear scale/polish around the best w15 (X,Q) warm start,
  * perturbation/random starts in the same exact factorization,
  * LP primal/dual exposedness certificate dumps for the final candidate.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from pathlib import Path
from typing import Any

import numpy as np
from scipy.optimize import basinhopping, brentq, linprog, minimize, minimize_scalar

import w15_verifier_reuse as verifier


np.set_printoptions(precision=10, suppress=True, linewidth=220)

DEFAULT_W15_DIR = Path(
    "/home/tobias/Projects/almost-idempotent-positive-maps/"
    "agent-A/explorations/classical-portfolio/experiments/out/w15_refuter"
)


def as_float_list(x: Any) -> Any:
    if isinstance(x, np.ndarray):
        return as_float_list(x.tolist())
    if isinstance(x, (list, tuple)):
        return [as_float_list(v) for v in x]
    if isinstance(x, (np.floating, float)):
        v = float(x)
        return v if math.isfinite(v) else None
    if isinstance(x, (np.integer, int)):
        return int(x)
    if isinstance(x, dict):
        return {str(k): as_float_list(v) for k, v in x.items()}
    return x


def load_w15_warm_start(w15_dir: Path) -> tuple[np.ndarray, np.ndarray, dict[str, Any]]:
    summary = json.loads((w15_dir / "w15_summary.json").read_text())
    rec = summary["best_record"]
    params = rec["params"]
    X = np.array(params["L"], dtype=float)
    Q = np.array(params["Q"], dtype=float)
    return X, Q, rec


def build_projection(X: np.ndarray, Q: np.ndarray) -> np.ndarray:
    """Build exact row-stochastic idempotent from the Lambda/R gauge."""
    k = Q.shape[0]
    Lambda = np.vstack([np.eye(k), X])
    R = np.c_[np.eye(k) - Q @ X, Q]
    return Lambda @ R


def pack(X: np.ndarray, Q: np.ndarray) -> np.ndarray:
    return np.r_[X[:, :-1].ravel(), Q.ravel()]


def unpack(z: np.ndarray, m: int, k: int) -> tuple[np.ndarray, np.ndarray]:
    x_free = z[: m * (k - 1)].reshape(m, k - 1)
    X = np.c_[x_free, 1.0 - x_free.sum(axis=1)]
    Q = z[m * (k - 1) :].reshape(k, m)
    return X, Q


def verify_from_factors(X: np.ndarray, Q: np.ndarray, label: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    P = build_projection(X, Q)
    rec = verifier.verify_instance(P, label, params=params or {})
    sig = rec.get("sigma_tilde")
    if rec.get("gate") == "PASS" and sig and sig > 0:
        rec["delta_over_sigma2"] = float(rec["delta"] / (sig * sig))
        rec["barrier_crossed"] = bool(rec["delta"] <= 0.25 and rec["sigma_tilde_over_tau"] > 1.0)
    else:
        rec["delta_over_sigma2"] = None
        rec["barrier_crossed"] = False
    return rec


def target_hidden(rec: dict[str, Any], target: int) -> bool:
    return (
        rec.get("gate") == "PASS"
        and rec.get("delta", math.inf) <= 0.25
        and rec.get("v") == target
        and target not in set(rec.get("W", []))
        and (rec.get("sigma_tilde") or 0.0) > 0.0
    )


def rec_score(rec: dict[str, Any]) -> float:
    """Higher is better for frontier tracking."""
    if rec.get("gate") != "PASS" or rec.get("delta", math.inf) > 0.25:
        return -1e100
    sig_ratio = rec.get("sigma_tilde_over_tau") or 0.0
    h_ratio = rec.get("H_over_tau") or 0.0
    ratio = rec.get("delta_over_sigma2")
    ratio_term = 0.0 if ratio is None else -math.log(max(ratio, 1e-300))
    return 10.0 * sig_ratio + h_ratio + ratio_term


def one_dim_scale_scan(X0: np.ndarray, Q0: np.ndarray, target: int, samples: int) -> dict[str, Any]:
    """Scan/polish the strongest warm-start scale family Q = s Q0."""
    records: list[dict[str, Any]] = []
    best: dict[str, Any] | None = None

    def eval_s(s: float, label: str = "scale") -> dict[str, Any]:
        rec = verify_from_factors(X0, s * Q0, label, {"scale": float(s), "family": "w15_Q_scale"})
        rec["scale"] = float(s)
        return rec

    # Coarse-to-fine scan.  The upper range intentionally passes the hiddenness
    # loss point, so the active transition is visible in the output.
    for s in np.linspace(0.2, 5.3, samples):
        rec = eval_s(float(s))
        records.append(rec)
        if target_hidden(rec, target) and (best is None or (rec["delta_over_sigma2"] or math.inf) < (best["delta_over_sigma2"] or math.inf)):
            best = rec

    # Find the observed hiddenness transition: target was hidden and then enters W.
    transitions: list[dict[str, Any]] = []
    for a, b in zip(records, records[1:]):
        if target_hidden(a, target) and not target_hidden(b, target):
            transitions.append({"left": a["scale"], "right": b["scale"]})

    def P_at(s: float) -> np.ndarray:
        return build_projection(X0, s * Q0)

    roots: list[dict[str, Any]] = []
    for tr in transitions:
        lo = float(tr["left"])
        hi = float(tr["right"])
        # The transition in this warm start is caused by a far row crossing the
        # rho threshold in the target's exposedness LP.  Detect every such root.
        for row in range(P_at(lo).shape[0]):
            if row == target:
                continue

            def gap(s: float, row: int = row) -> float:
                P = P_at(s)
                _, delta = verifier.neg_mass(P)
                return float(np.abs(P[row] - P[target]).sum() - 4.0 * math.sqrt(delta))

            try:
                glo, ghi = gap(lo), gap(hi)
                if glo == 0 or glo * ghi < 0:
                    root = float(brentq(lambda ss: gap(ss), lo, hi, xtol=1e-12, rtol=1e-12))
                    roots.append({"transition": tr, "row": row, "scale": root})
            except Exception:
                pass

    # Add robust just-left candidates near any far-row threshold.
    for root in roots:
        for eps in (1e-3, 5e-4, 1e-4):
            s = root["scale"] - eps
            if s > 0:
                rec = eval_s(s, "scale_threshold_left")
                rec["active_threshold"] = root
                records.append(rec)
                if target_hidden(rec, target) and (best is None or (rec["delta_over_sigma2"] or math.inf) < (best["delta_over_sigma2"] or math.inf)):
                    best = rec

    # SciPy nonlinear polish over the same one-dimensional exact factorization.
    def objective_scalar(s: float) -> float:
        if s <= 0:
            return 1e9
        rec = eval_s(float(s), "scale_minimize_scalar")
        if not target_hidden(rec, target):
            return 1e6 + abs(float(s))
        return float(rec["delta_over_sigma2"])

    opt = minimize_scalar(objective_scalar, bounds=(0.2, 5.3), method="bounded", options={"xatol": 1e-5, "maxiter": 80})
    rec = eval_s(float(opt.x), "scale_minimize_scalar_result")
    rec["optimizer"] = {"method": "minimize_scalar_bounded", "success": bool(opt.success), "fun": float(opt.fun), "nit": int(opt.nit)}
    records.append(rec)
    if target_hidden(rec, target) and (best is None or (rec["delta_over_sigma2"] or math.inf) < (best["delta_over_sigma2"] or math.inf)):
        best = rec

    # Basinhopping is run with the exact verifier-gated objective; this usually
    # returns to the same active threshold.
    try:
        bh = basinhopping(
            lambda z: objective_scalar(float(z[0])),
            np.array([best["scale"] if best else 1.0]),
            niter=12,
            stepsize=0.08,
            minimizer_kwargs={"method": "Nelder-Mead", "options": {"maxiter": 80, "xatol": 1e-5, "fatol": 1e-5}},
            seed=1616,
            disp=False,
        )
        rec = eval_s(float(bh.x[0]), "scale_basinhopping_result")
        rec["optimizer"] = {"method": "basinhopping_Nelder-Mead", "fun": float(bh.fun), "scale": float(bh.x[0])}
        records.append(rec)
        if target_hidden(rec, target) and (best is None or (rec["delta_over_sigma2"] or math.inf) < (best["delta_over_sigma2"] or math.inf)):
            best = rec
    except Exception as exc:
        records.append({"label": "scale_basinhopping_error", "error": repr(exc)})

    return {"records": records, "best": best, "transitions": transitions, "threshold_roots": roots}


def smoothplus(x: np.ndarray | float, beta: float = 80.0) -> np.ndarray | float:
    arr = np.asarray(x, dtype=float)
    y = beta * arr
    out = np.where(y > 30.0, arr, np.log1p(np.exp(np.clip(y, -700.0, 30.0))) / beta)
    if np.isscalar(x):
        return float(out)
    return out


def slsqp_polish(X0: np.ndarray, Q0: np.ndarray, start_scale: float, target: int, maxiter: int) -> dict[str, Any]:
    """A short smooth W-aware local polish in full (X,Q) variables."""
    m, k = X0.shape
    z0 = pack(X0, start_scale * Q0)
    bounds = [(-0.2, 1.2)] * (m * (k - 1)) + [(-3.0, 3.0)] * (k * m)
    eval_records: list[dict[str, Any]] = []

    def objective(z: np.ndarray) -> float:
        X, Q = unpack(z, m, k)
        P = build_projection(X, Q)
        neg = smoothplus(-P, beta=70.0).sum(axis=1)
        mx = float(np.max(neg))
        delta = mx + math.log(float(np.exp(35.0 * (neg - mx)).sum())) / 35.0
        B = X @ Q
        h = target - k
        sig = float(smoothplus(B[h], beta=70.0).sum())
        pen = 0.0
        pen += 2000.0 * float(smoothplus(delta - 0.25, beta=50.0)) ** 2
        # W-aware hiddenness surrogate: use the exact target exposedness LP value
        # but only for target row, so SLSQP gets pressure before final verification.
        try:
            tau = math.sqrt(max(delta, 1e-16))
            ok, margin, _ = verifier.exposed_margin(P, target, 4.0 * tau, 0.25 * tau)
            if margin is not None and math.isfinite(margin):
                pen += 0.25 * float(smoothplus(margin - 0.25 * tau, beta=40.0)) ** 2 / (tau * tau + 1e-12)
            if ok:
                pen += 0.2
        except Exception:
            pen += 1.0
        pen += 1e-5 * float(np.sum(Q * Q) + np.sum(X * X))
        return float(delta / max(sig * sig, 1e-18) + pen)

    res = minimize(objective, z0, method="SLSQP", bounds=bounds, options={"maxiter": maxiter, "ftol": 1e-7, "disp": False})
    for label, z in (("slsqp_start", z0), ("slsqp_result", res.x)):
        X, Q = unpack(z, m, k)
        rec = verify_from_factors(X, Q, label, {"optimizer": "SLSQP"})
        eval_records.append(rec)
    return {
        "optimizer": {"method": "SLSQP", "success": bool(res.success), "status": int(res.status), "message": res.message, "fun": float(res.fun), "nit": int(res.nit)},
        "records": eval_records,
        "best": max(eval_records, key=rec_score),
    }


def perturbation_search(X0: np.ndarray, Q0: np.ndarray, scale: float, target: int, rng: np.random.Generator, trials: int) -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    best: dict[str, Any] | None = None
    best_factors: dict[str, Any] | None = None
    for t in range(trials):
        amp_x = 10 ** rng.uniform(-5.0, -1.7)
        amp_q = 10 ** rng.uniform(-5.0, -1.2)
        X = X0.copy()
        X[:, :-1] += amp_x * rng.normal(size=X[:, :-1].shape)
        X[:, -1] = 1.0 - X[:, :-1].sum(axis=1)
        Q = scale * Q0 + amp_q * rng.normal(size=Q0.shape)
        rec = verify_from_factors(X, Q, "perturb_w15_scale", {"trial": t, "amp_x": amp_x, "amp_q": amp_q, "base_scale": scale})
        records.append(rec)
        if target_hidden(rec, target) and (best is None or (rec["delta_over_sigma2"] or math.inf) < (best["delta_over_sigma2"] or math.inf)):
            best = rec
            best_factors = {"X": X.copy(), "Q": Q.copy()}
    return {"records": records, "best": best, "best_factors": best_factors}


def random_direct_search(rng: np.random.Generator, shapes: list[tuple[int, int]], trials_per_shape: int) -> dict[str, Any]:
    by_shape: dict[str, Any] = {}
    for n, k in shapes:
        m = n - k
        shape_key = f"n{n}_k{k}"
        best: dict[str, Any] | None = None
        best_factors: dict[str, Any] | None = None
        counts: dict[str, int] = {}
        records: list[dict[str, Any]] = []
        for t in range(trials_per_shape):
            # Seed one outside-simplex hidden row, then add nearby hidden rows.
            X = rng.dirichlet(np.ones(k), size=m)
            h = int(rng.integers(0, m))
            neg_coord = int(rng.integers(0, k))
            eps = 10 ** rng.uniform(-3.5, -1.0)
            X[h, neg_coord] -= eps
            X[h] += eps / (k - 1)
            X[h, neg_coord] -= eps / (k - 1)
            X[h] /= X[h].sum()
            for r in range(m):
                if r != h and rng.random() < 0.45:
                    X[r] = X[h] + 10 ** rng.uniform(-4.5, -2.0) * rng.normal(size=k)
                    X[r] += (1.0 - X[r].sum()) / k

            Q = 10 ** rng.uniform(-3.5, -0.1) * rng.normal(size=(k, m))
            # Positive self-mass/return-flow bias, the w15 loophole.
            Q[:, h] += rng.normal(scale=0.02, size=k)
            target = k + h
            rec = verify_from_factors(X, Q, "random_direct_LB", {"trial": t, "target": target, "shape": [n, k]})
            counts[rec.get("gate", "UNKNOWN")] = counts.get(rec.get("gate", "UNKNOWN"), 0) + 1
            records.append({key: rec.get(key) for key in ("label", "gate", "n", "delta", "tau", "W", "v", "H_over_tau", "sigma_tilde_over_tau", "delta_over_sigma2", "barrier_crossed")})
            if rec_score(rec) > rec_score(best or {}):
                best = rec
                best_factors = {"X": X.copy(), "Q": Q.copy()}
        by_shape[shape_key] = {"counts": counts, "best": best, "best_factors": best_factors, "sample_records": records[:20]}
    return by_shape


def exposedness_lp_certificate(P: np.ndarray, i: int, rho: float, kappa: float) -> dict[str, Any]:
    rows = np.asarray(P, dtype=float)
    n, d = rows.shape
    di = np.abs(rows - rows[i]).sum(axis=1)
    far = [k for k in range(n) if k != i and di[k] >= rho - 1e-12]
    nv = d + 2
    c = np.zeros(nv)
    c[-1] = -1.0
    A_ub: list[np.ndarray] = []
    b_ub: list[float] = []
    names: list[str] = []

    def hvec(krow: int) -> np.ndarray:
        v = np.zeros(nv)
        v[:d] = rows[krow]
        v[d] = 1.0
        return v

    for krow in range(n):
        hk = hvec(krow)
        A_ub.append(hk.copy())
        b_ub.append(1.0)
        names.append(f"h(row {krow}) <= 1")
        A_ub.append(-hk.copy())
        b_ub.append(0.0)
        names.append(f"h(row {krow}) >= 0")
    for krow in far:
        hk = hvec(krow)
        row = -hk
        row[-1] = 1.0
        A_ub.append(row)
        b_ub.append(0.0)
        names.append(f"t <= h(row {krow})")

    A_eq = np.array([hvec(i)])
    b_eq = np.array([0.0])
    bounds = [(None, None)] * d + [(None, None), (None, 1.0)]
    attempts = []
    result = None
    for method, presolve in (("highs-ipm", False), ("highs", False), ("highs-ds", False), ("highs-ipm", True)):
        res = linprog(
            c,
            A_ub=np.array(A_ub),
            b_ub=np.array(b_ub),
            A_eq=A_eq,
            b_eq=b_eq,
            bounds=bounds,
            method=method,
            options={"presolve": presolve},
        )
        attempts.append({"method": method, "presolve": presolve, "success": bool(res.success), "status": int(res.status), "message": res.message})
        if res.success and result is None:
            result = res

    if result is None:
        return {"success": False, "attempts": attempts, "far": far}

    x = result.x
    h_values = rows @ x[:d] + x[d]
    tstar = -float(result.fun)
    active = []
    slacks = np.array(result.slack)
    for idx, slack in enumerate(slacks):
        if abs(float(slack)) <= 1e-7:
            active.append({"constraint": names[idx], "slack": float(slack), "dual_marginal": float(result.ineqlin.marginals[idx])})
    return {
        "success": True,
        "attempts": attempts,
        "target": int(i),
        "rho": float(rho),
        "kappa": float(kappa),
        "tstar": tstar,
        "tstar_over_kappa": float(tstar / kappa) if kappa > 0 else None,
        "hidden_by_margin": bool(tstar < kappa - 1e-9),
        "far": [int(x) for x in far],
        "distances_from_target": [float(x) for x in di],
        "objective_fun": float(result.fun),
        "affine_w": [float(x) for x in x[:d]],
        "affine_b": float(x[d]),
        "t_variable": float(x[-1]),
        "h_values": [float(x) for x in h_values],
        "eqlin_residual": [float(x) for x in result.eqlin.residual],
        "eqlin_marginals": [float(x) for x in result.eqlin.marginals],
        "ineqlin_active": active,
        "lower_marginals": [float(x) for x in result.lower.marginals],
        "upper_marginals": [float(x) for x in result.upper.marginals],
        "status": int(result.status),
        "message": result.message,
    }


def save_certificate(outdir: Path, X: np.ndarray, Q: np.ndarray, tag: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    P = build_projection(X, Q)
    rec = verifier.verify_instance(P, f"w16_verified_crossing_{tag}", params or {})
    sig = rec["sigma_tilde"]
    rec["delta_over_sigma2"] = float(rec["delta"] / (sig * sig))
    cert = exposedness_lp_certificate(P, int(rec["v"]), float(rec["rho"]), float(rec["kappa"]))
    matrix_payload = {
        "P": as_float_list(P),
        "Lambda": as_float_list(np.vstack([np.eye(Q.shape[0]), X])),
        "B_or_R": as_float_list(np.c_[np.eye(Q.shape[0]) - Q @ X, Q]),
        "X_hidden_rows": as_float_list(X),
        "Q": as_float_list(Q),
        "rank_k": int(Q.shape[0]),
        "n": int(P.shape[0]),
    }
    certificate = {
        "verdict": "BARRIER_CROSSED",
        "record": as_float_list(rec),
        "hiddenness_lp_certificate": as_float_list(cert),
        "matrix_payload_files": {
            "matrix_json": f"w16_{tag}_matrix.json",
            "matrix_txt": f"w16_{tag}_matrix.txt",
            "factorization_json": f"w16_{tag}_factorization.json",
        },
    }
    (outdir / f"w16_{tag}_matrix.json").write_text(json.dumps(as_float_list(P), indent=2))
    np.savetxt(outdir / f"w16_{tag}_matrix.txt", P, fmt="%.17g")
    (outdir / f"w16_{tag}_factorization.json").write_text(json.dumps(matrix_payload, indent=2))
    (outdir / f"w16_{tag}_certificate.json").write_text(json.dumps(certificate, indent=2))
    return certificate


def compact_record(rec: dict[str, Any] | None) -> dict[str, Any] | None:
    if not rec:
        return None
    keys = [
        "label",
        "gate",
        "n",
        "delta",
        "tau",
        "rho",
        "kappa",
        "W",
        "v",
        "H",
        "H_over_tau",
        "sigma_tilde",
        "sigma_tilde_over_tau",
        "delta_over_sigma2",
        "P_vv",
        "nu_v",
        "best_component",
        "barrier_crossed",
        "scale",
    ]
    return {k: rec.get(k) for k in keys if k in rec}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default=".")
    ap.add_argument("--w15-dir", default=str(DEFAULT_W15_DIR))
    ap.add_argument("--seed", type=int, default=1616)
    ap.add_argument("--scale-samples", type=int, default=700)
    ap.add_argument("--perturb-trials", type=int, default=80)
    ap.add_argument("--random-trials-per-shape", type=int, default=20)
    ap.add_argument("--slsqp-maxiter", type=int, default=25)
    args = ap.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(args.seed)
    t0 = time.time()

    X0, Q0, warm_rec = load_w15_warm_start(Path(args.w15_dir))
    k = Q0.shape[0]
    target = k

    scale_result = one_dim_scale_scan(X0, Q0, target, args.scale_samples)
    best_scale = scale_result["best"]
    if best_scale is None:
        raise RuntimeError("warm-start scale scan did not retain a hidden target candidate")

    slsqp_result = slsqp_polish(X0, Q0, float(best_scale["scale"]), target, args.slsqp_maxiter)
    perturb_result = perturbation_search(X0, Q0, float(best_scale["scale"]), target, rng, args.perturb_trials)
    random_result = random_direct_search(rng, [(6, 3), (7, 4), (8, 4), (10, 4), (12, 4)], args.random_trials_per_shape)

    all_best = [best_scale, slsqp_result.get("best"), perturb_result.get("best")]
    for item in random_result.values():
        all_best.append(item.get("best"))
    all_best = [x for x in all_best if x]
    best_overall = max(all_best, key=rec_score)

    scale_certificate = None
    best_certificate = None
    if best_scale.get("barrier_crossed"):
        scale_certificate = save_certificate(
            outdir,
            X0.copy(),
            float(best_scale["scale"]) * Q0,
            "scale",
            {"scale": float(best_scale["scale"]), "family": "w15_Q_scale"},
        )

    if best_overall.get("barrier_crossed"):
        if best_overall is perturb_result.get("best") and perturb_result.get("best_factors"):
            bf = perturb_result["best_factors"]
            best_certificate = save_certificate(outdir, bf["X"], bf["Q"], "best", {"family": "w15_scale_perturbation"})
        else:
            best_certificate = scale_certificate

    summary = {
        "created": time.strftime("%Y-%m-%d %H:%M:%S"),
        "elapsed_seconds": time.time() - t0,
        "seed": args.seed,
        "warm_start": compact_record(warm_rec),
        "scale_search": {
            "best": compact_record(scale_result["best"]),
            "transitions": scale_result["transitions"],
            "threshold_roots": scale_result["threshold_roots"],
            "num_records": len(scale_result["records"]),
        },
        "slsqp": {"optimizer": slsqp_result["optimizer"], "best": compact_record(slsqp_result["best"])},
        "perturbations": {"trials": args.perturb_trials, "best": compact_record(perturb_result["best"])},
        "random_by_shape": {shape: {"counts": data["counts"], "best": compact_record(data["best"])} for shape, data in random_result.items()},
        "best_overall": compact_record(best_overall),
        "scale_certificate": compact_record(scale_certificate["record"]) if scale_certificate else None,
        "decision_certificate": compact_record(best_certificate["record"]) if best_certificate else None,
    }
    (outdir / "w16_results.json").write_text(json.dumps(as_float_list(summary), indent=2))

    # Keep a fuller but still bounded frontier dump for audit.
    frontier = {
        "scale_records": [compact_record(r) for r in scale_result["records"] if isinstance(r, dict) and r.get("gate") == "PASS"],
        "slsqp_records": [compact_record(r) for r in slsqp_result["records"]],
        "perturbation_best": compact_record(perturb_result["best"]),
    }
    (outdir / "w16_frontier.json").write_text(json.dumps(as_float_list(frontier), indent=2))

    print("=== W16 NLOPT SUMMARY ===")
    print(json.dumps(as_float_list(summary), indent=2))
    if best_certificate:
        print("=== CERTIFICATE ===")
        print(json.dumps(as_float_list(compact_record(best_certificate["record"])), indent=2))
        print("hiddenness tstar/kappa =", best_certificate["hiddenness_lp_certificate"].get("tstar_over_kappa"))


if __name__ == "__main__":
    main()
