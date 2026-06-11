#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path("/home/tobias/Projects/almost-idempotent-positive-maps")
PORT = ROOT / "agent-A/explorations/classical-portfolio"
W17 = PORT / "experiments/out/w17_antecedent/w17_decider.py"
TARGET = PORT / "experiments/out/w17_antecedent/targeted_best/fine_best_factorization.json"
OUTDIR = Path("/tmp/codex-sigma-wall/w19_boundary")

EDGE_TOL = 1e-12


def load_w17():
    spec = importlib.util.spec_from_file_location("w17_decider", W17)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {W17}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def finite(x: Any) -> Any:
    if isinstance(x, np.ndarray):
        return finite(x.tolist())
    if isinstance(x, dict):
        return {str(k): finite(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [finite(v) for v in x]
    if isinstance(x, (np.integer, int)):
        return int(x)
    if isinstance(x, (np.floating, float)):
        y = float(x)
        return y if math.isfinite(y) else None
    return x


def max_row_l1(M: np.ndarray) -> float:
    if M.size == 0:
        return 0.0
    return float(np.abs(M).sum(axis=1).max())


def matrix_masses(M: np.ndarray) -> dict[str, float]:
    if M.size == 0:
        return {
            "sum": 0.0,
            "l1_total": 0.0,
            "pos_total": 0.0,
            "neg_total": 0.0,
            "max_row_l1": 0.0,
            "max_row_pos": 0.0,
            "trace": 0.0,
        }
    return {
        "sum": float(M.sum()),
        "l1_total": float(np.abs(M).sum()),
        "pos_total": float(np.maximum(M, 0.0).sum()),
        "neg_total": float(np.maximum(-M, 0.0).sum()),
        "max_row_l1": max_row_l1(M),
        "max_row_pos": float(np.maximum(M, 0.0).sum(axis=1).max()),
        "trace": float(np.trace(M)) if M.shape[0] == M.shape[1] else 0.0,
    }


def sccs(vertices: list[int], adj: dict[int, list[int]]) -> list[list[int]]:
    index = 0
    stack: list[int] = []
    on_stack: set[int] = set()
    indices: dict[int, int] = {}
    low: dict[int, int] = {}
    comps: list[list[int]] = []

    def visit(v: int) -> None:
        nonlocal index
        indices[v] = index
        low[v] = index
        index += 1
        stack.append(v)
        on_stack.add(v)
        for w in adj.get(v, []):
            if w not in indices:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in on_stack:
                low[v] = min(low[v], indices[w])
        if low[v] == indices[v]:
            comp = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                comp.append(w)
                if w == v:
                    break
            comps.append(sorted(comp))

    for v in vertices:
        if v not in indices:
            visit(v)
    return comps


def component_path_product(M: np.ndarray, comp: list[int]) -> tuple[float, int]:
    comp = list(comp)
    m = len(comp)
    if m <= 1:
        return 1.0, 0
    idx = {v: a for a, v in enumerate(comp)}
    best = np.zeros((m, m))
    dist = np.full((m, m), np.inf)
    for a in range(m):
        best[a, a] = 1.0
        dist[a, a] = 0
    for i in comp:
        a = idx[i]
        for j in comp:
            p = float(M[i, j])
            if p > EDGE_TOL:
                b = idx[j]
                best[a, b] = max(best[a, b], p)
                dist[a, b] = min(dist[a, b], 1)
    for k in range(m):
        for i in range(m):
            for j in range(m):
                if dist[i, k] + dist[k, j] < dist[i, j]:
                    dist[i, j] = dist[i, k] + dist[k, j]
    finite_dist = dist[np.isfinite(dist)]
    diameter = int(np.max(finite_dist)) if finite_dist.size else 0
    cur = best.copy()
    out = best.copy()
    for _ in range(2, m + 1):
        nxt = np.zeros((m, m))
        for i in range(m):
            for k in range(m):
                if cur[i, k] <= 0:
                    continue
                nxt[i, :] = np.maximum(nxt[i, :], cur[i, k] * best[k, :])
        out = np.maximum(out, nxt)
        cur = nxt
    off = [out[i, j] for i in range(m) for j in range(m) if i != j]
    return (float(min(off)) if off else 1.0), diameter


def build_projection(X: np.ndarray, Q: np.ndarray) -> np.ndarray:
    k = Q.shape[0]
    lam = np.vstack([np.eye(k), X])
    r = np.c_[np.eye(k) - Q @ X, Q]
    return lam @ r


def random_hm_projection(n: int, k: int, rng: np.random.Generator) -> np.ndarray:
    x = rng.dirichlet(np.ones(k), size=n - k)
    q = np.zeros((k, n - k))
    return build_projection(x, q)


def row_sum_similarity(P: np.ndarray, rng: np.random.Generator, eps: float) -> np.ndarray | None:
    n = P.shape[0]
    K = rng.normal(size=(n, n))
    K -= K.mean(axis=1, keepdims=True)
    A = np.eye(n) + eps * K
    try:
        Ainv = np.linalg.inv(A)
    except np.linalg.LinAlgError:
        return None
    return A @ P @ Ainv


def quotient_from_record(w17, P: np.ndarray) -> tuple[np.ndarray, list[list[int]], list[int]]:
    classes, cls_of = w17.row_classes(P)
    return w17.quotient_matrix(P, classes, cls_of), classes, cls_of


def band_diagnostics(
    w17,
    P: np.ndarray,
    rec: dict[str, Any],
    threshold_factor: float,
    label: str,
) -> dict[str, Any]:
    Q, classes, cls_of = quotient_from_record(w17, P)
    g = np.array(rec["g"], dtype=float)
    gq = np.array([g[c[0]] for c in classes], dtype=float)
    delta = float(rec["delta"])
    tau = float(rec["tau"])
    kappa = float(rec["kappa"])
    Omega = float(rec["Omega"])
    t = threshold_factor * kappa * Omega
    S = [i for i, gi in enumerate(gq) if gi < t + 1e-12]
    T = [i for i in range(len(gq)) if i not in S]
    s_pos = {c: i for i, c in enumerate(S)}
    vq = cls_of[int(rec["v"])]
    Wq = sorted({cls_of[int(w)] for w in rec["W"]})

    B = Q[np.ix_(S, S)]
    E = Q[np.ix_(S, T)]
    C = Q[np.ix_(T, S)]
    D = Q[np.ix_(T, T)]
    EC = E @ C
    identity_resid = float(np.abs(B @ B - B + EC).max()) if B.size else 0.0

    zeta = max_row_l1(B @ B - B)
    eps_finisher = zeta + 6.0 * delta + 4.0 * delta * delta
    rstar = 0.85 * tau
    theta_required = (
        2.0 * (1.0 + delta) * eps_finisher / (rstar - 4.0 * delta)
        if rstar > 4.0 * delta
        else math.inf
    )

    boundary_by_m: list[dict[str, Any]] = []
    Bpow = np.eye(len(S))
    Rsum = np.zeros_like(B)
    for m in range(2, 9):
        Rsum = Rsum + Bpow @ EC
        Bpow = Bpow @ B
        exact = B - Bpow
        row_v = None
        if vq in s_pos:
            rv = Rsum[s_pos[vq], :]
            row_v = matrix_masses(rv.reshape(1, -1))
            row_v["over_tau_max_row_l1"] = row_v["max_row_l1"] / tau if tau > 0 else None
            row_v["over_tau_pos_total"] = row_v["pos_total"] / tau if tau > 0 else None
        mm = matrix_masses(Rsum)
        boundary_by_m.append(
            {
                "m": m,
                "resid_B_minus_Bm": float(np.abs(Rsum - exact).max()) if B.size else 0.0,
                **mm,
                "over_tau_max_row_l1": mm["max_row_l1"] / tau if tau > 0 else None,
                "over_tau_pos_total": mm["pos_total"] / tau if tau > 0 else None,
                "row_v": row_v,
            }
        )

    adj = {i: [j for j in S if Q[i, j] > EDGE_TOL] for i in S}
    comps = []
    for comp in sccs(S, adj):
        mass_from_v = float(sum(max(Q[vq, j], 0.0) for j in comp))
        Pi, L = component_path_product(Q, comp)
        internal_pos = []
        leak_pos = []
        leak_deep = []
        leak_shallow = []
        for i in comp:
            internal_pos.append(sum(max(Q[i, j], 0.0) for j in comp))
            leak_deep.append(sum(max(Q[i, j], 0.0) for j in T))
            leak_shallow.append(sum(max(Q[i, j], 0.0) for j in S if j not in comp))
            leak_pos.append(leak_deep[-1] + leak_shallow[-1])
        closed_w12 = bool(max(leak_pos, default=0.0) <= 1e-10 and min(internal_pos, default=0.0) >= 1.0 - 1e-10)
        R_with_theta_pi = (
            4.0 * delta + 2.0 * (1.0 + delta) * eps_finisher / Pi if Pi > 0.0 else math.inf
        )
        comps.append(
            {
                "component": [int(x) for x in comp],
                "size": len(comp),
                "contains_v": bool(vq in comp),
                "contains_W": sorted(set(comp).intersection(Wq)),
                "mass_from_v": mass_from_v,
                "Pi": Pi,
                "Pi_over_tau": Pi / tau if tau > 0 else None,
                "L": L,
                "min_internal_pos": float(min(internal_pos, default=0.0)),
                "max_pos_leak_total": float(max(leak_pos, default=0.0)),
                "max_pos_leak_deep": float(max(leak_deep, default=0.0)),
                "max_pos_leak_shallow": float(max(leak_shallow, default=0.0)),
                "closed_w12": closed_w12,
                "theta_required_for_finisher": theta_required,
                "optimistic_pi_minus_theta_required": Pi - theta_required if math.isfinite(theta_required) else -math.inf,
                "optimistic_R_using_pi": R_with_theta_pi,
                "optimistic_finisher_with_pi": bool(closed_w12 and R_with_theta_pi < rstar),
            }
        )
    comps.sort(key=lambda r: (not r["optimistic_finisher_with_pi"], -r["mass_from_v"], r["Pi"]))

    Epos = np.maximum(E, 0.0)
    Eneg = np.maximum(-E, 0.0)
    Cpos = np.maximum(C, 0.0)
    Cneg = np.maximum(-C, 0.0)
    gS = gq[S]
    gT = gq[T]
    gap = gT[:, None] - gS[None, :] if len(T) and len(S) else np.zeros((len(T), len(S)))
    triple_pp = Epos @ Cpos if len(S) and len(T) else np.zeros_like(B)
    triple_nn = Eneg @ Cneg if len(S) and len(T) else np.zeros_like(B)
    triple_pn = Epos @ Cneg if len(S) and len(T) else np.zeros_like(B)
    triple_np = Eneg @ Cpos if len(S) and len(T) else np.zeros_like(B)
    descent_pp = float((Epos[:, :, None] * Cpos[None, :, :] * gap[None, :, :]).sum()) if len(S) and len(T) else 0.0
    descent_signed = float((E[:, :, None] * C[None, :, :] * gap[None, :, :]).sum()) if len(S) and len(T) else 0.0
    deep_visible = [a for a in T if a in Wq]
    deep_nonvisible = [a for a in T if a not in Wq]
    t_index = {a: i for i, a in enumerate(T)}
    band_v_row = s_pos.get(vq)

    def E_pos_to(cols: list[int]) -> float:
        if not cols:
            return 0.0
        return float(Epos[:, [t_index[c] for c in cols]].sum())

    charge = {
        "E_pos_total": float(Epos.sum()),
        "E_neg_total": float(Eneg.sum()),
        "C_pos_total": float(Cpos.sum()),
        "C_neg_total": float(Cneg.sum()),
        "E_pos_to_deep_visible": E_pos_to(deep_visible),
        "E_pos_to_deep_nonvisible": E_pos_to(deep_nonvisible),
        "triple_pp": matrix_masses(triple_pp),
        "triple_nn": matrix_masses(triple_nn),
        "triple_pn": matrix_masses(triple_pn),
        "triple_np": matrix_masses(triple_np),
        "descent_pp": descent_pp,
        "descent_pp_over_tau": descent_pp / tau if tau > 0 else None,
        "descent_signed": descent_signed,
        "descent_signed_over_tau": descent_signed / tau if tau > 0 else None,
    }
    if band_v_row is not None:
        charge["v_E_pos_total"] = float(Epos[band_v_row, :].sum())
        charge["v_E_neg_total"] = float(Eneg[band_v_row, :].sum())
        charge["v_E_pos_over_tau"] = float(Epos[band_v_row, :].sum() / tau) if tau > 0 else None
        charge["v_E_neg_over_delta"] = float(Eneg[band_v_row, :].sum() / delta) if delta > 0 else None
        charge["v_E_pos_gT"] = float(Epos[band_v_row, :] @ gT) if len(T) else 0.0
        charge["v_E_pos_gT_over_deltaOmega"] = (
            float((Epos[band_v_row, :] @ gT) / (delta * Omega)) if delta > 0 and Omega > 0 and len(T) else None
        )

    return {
        "label": label,
        "threshold_factor": threshold_factor,
        "t": float(t),
        "t_over_kappaOmega": threshold_factor,
        "num_classes": len(classes),
        "S": [int(x) for x in S],
        "T": [int(x) for x in T],
        "v_class": int(vq),
        "W_classes": [int(x) for x in Wq],
        "identity_resid_m2": identity_resid,
        "zeta": zeta,
        "epsilon_finisher": eps_finisher,
        "rstar": rstar,
        "theta_required_for_finisher": theta_required,
        "EC": {
            **matrix_masses(EC),
            "over_tau_max_row_l1": max_row_l1(EC) / tau if tau > 0 else None,
            "over_tau_pos_total": float(np.maximum(EC, 0.0).sum() / tau) if tau > 0 else None,
        },
        "trace_tax": float(np.trace(EC)) if EC.shape[0] == EC.shape[1] else 0.0,
        "boundary_by_m": boundary_by_m,
        "components": comps,
        "best_component": comps[0] if comps else None,
        "charge": charge,
    }


def evaluate_instance(w17, P: np.ndarray, label: str) -> dict[str, Any]:
    rec = w17.verify_instance(P, label)
    out: dict[str, Any] = {
        "label": label,
        "gate": rec.get("gate"),
        "n": rec.get("n"),
        "delta": rec.get("delta"),
        "tau": rec.get("tau"),
        "H": rec.get("H"),
        "H_over_tau": rec.get("H_over_tau"),
        "sigma_tilde": rec.get("sigma_tilde"),
        "sigma_tilde_over_tau": rec.get("sigma_tilde_over_tau"),
        "v": rec.get("v"),
        "W": rec.get("W"),
    }
    if rec.get("gate") == "PASS":
        out["bands"] = [band_diagnostics(w17, P, rec, f, label) for f in (0.5, 0.75, 1.0)]
        out["min_boundary_m2_maxrow_over_tau"] = min(b["EC"]["over_tau_max_row_l1"] for b in out["bands"])
        out["max_boundary_m2_maxrow_over_tau"] = max(b["EC"]["over_tau_max_row_l1"] for b in out["bands"])
        out["max_boundary_m2_pos_over_tau"] = max(b["EC"]["over_tau_pos_total"] for b in out["bands"])
        out["any_optimistic_finisher"] = any(
            c.get("optimistic_finisher_with_pi")
            for b in out["bands"]
            for c in b.get("components", [])
        )
    return out


def random_probe(w17, rng: np.random.Generator, samples: int) -> dict[str, Any]:
    records = []
    best_small_boundary = None
    best_antecedent = None
    shapes = [(7, 3), (8, 4), (10, 5), (12, 5)]
    eps_grid = np.geomspace(2e-4, 0.14, 18)
    for s in range(samples):
        n, k = shapes[s % len(shapes)]
        P0 = random_hm_projection(n, k, rng)
        eps = float(eps_grid[s % len(eps_grid)] * math.exp(rng.normal(0.0, 0.35)))
        P = row_sum_similarity(P0, rng, eps)
        if P is None:
            continue
        rec = evaluate_instance(w17, P, f"hm_similarity_{s:04d}")
        if rec.get("gate") != "PASS" or rec.get("delta") is None or rec["delta"] <= 1e-12 or rec["delta"] > 0.25:
            continue
        compact = {
            "label": rec["label"],
            "n": rec["n"],
            "delta": rec["delta"],
            "tau": rec["tau"],
            "H_over_tau": rec.get("H_over_tau"),
            "sigma_tilde_over_tau": rec.get("sigma_tilde_over_tau"),
            "min_boundary_m2_maxrow_over_tau": rec.get("min_boundary_m2_maxrow_over_tau"),
            "max_boundary_m2_pos_over_tau": rec.get("max_boundary_m2_pos_over_tau"),
            "any_optimistic_finisher": rec.get("any_optimistic_finisher"),
            "eps": eps,
        }
        records.append(compact)
        key = compact["min_boundary_m2_maxrow_over_tau"]
        if key is not None and not compact["any_optimistic_finisher"]:
            if best_small_boundary is None or key < best_small_boundary[0]:
                best_small_boundary = (key, compact, rec, P)
        sig = rec.get("sigma_tilde_over_tau") or 0.0
        h = rec.get("H_over_tau") or 0.0
        if sig > 1.0:
            score = h + 0.02 * sig
            if best_antecedent is None or score > best_antecedent[0]:
                best_antecedent = (score, compact, rec, P)

    out: dict[str, Any] = {
        "num_pass": len(records),
        "records": records[:200],
        "best_small_boundary": best_small_boundary[1] if best_small_boundary else None,
        "best_antecedent_like": best_antecedent[1] if best_antecedent else None,
    }
    if best_small_boundary is not None:
        np.savetxt(OUTDIR / "both_horns_fail_candidate_matrix.txt", best_small_boundary[3])
        (OUTDIR / "both_horns_fail_candidate.json").write_text(json.dumps(finite(best_small_boundary[2]), indent=2))
        out["saved_both_horns_fail_candidate"] = {
            "matrix": str(OUTDIR / "both_horns_fail_candidate_matrix.txt"),
            "json": str(OUTDIR / "both_horns_fail_candidate.json"),
        }
    if best_antecedent is not None:
        np.savetxt(OUTDIR / "random_antecedent_like_matrix.txt", best_antecedent[3])
        (OUTDIR / "random_antecedent_like.json").write_text(json.dumps(finite(best_antecedent[2]), indent=2))
        out["saved_antecedent_like"] = {
            "matrix": str(OUTDIR / "random_antecedent_like_matrix.txt"),
            "json": str(OUTDIR / "random_antecedent_like.json"),
        }
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--samples", type=int, default=120)
    ap.add_argument("--seed", type=int, default=19019)
    args = ap.parse_args()

    w17 = load_w17()
    payload = json.loads(TARGET.read_text())
    P = np.array(payload["P"], dtype=float)
    targeted = evaluate_instance(w17, P, "w17_targeted_best")
    rng = np.random.default_rng(args.seed)
    random = random_probe(w17, rng, args.samples)
    summary = {"targeted_best": targeted, "random_hm_perturbed": random}
    (OUTDIR / "boundary_measurements.json").write_text(json.dumps(finite(summary), indent=2))

    lines = []
    lines.append("boundary dichotomy measurements")
    lines.append(
        "targeted_best: "
        f"delta={targeted.get('delta'):.12g} "
        f"H/tau={targeted.get('H_over_tau'):.12g} "
        f"sigma/tau={targeted.get('sigma_tilde_over_tau'):.12g} "
        f"m2 maxrow/tau=[{targeted.get('min_boundary_m2_maxrow_over_tau'):.6g}, "
        f"{targeted.get('max_boundary_m2_maxrow_over_tau'):.6g}] "
        f"m2 pos/tau max={targeted.get('max_boundary_m2_pos_over_tau'):.6g} "
        f"optimistic_finisher={targeted.get('any_optimistic_finisher')}"
    )
    lines.append(
        "random_hm: "
        f"pass={random.get('num_pass')} "
        f"best_small_boundary={random.get('best_small_boundary')} "
        f"best_antecedent_like={random.get('best_antecedent_like')}"
    )
    (OUTDIR / "boundary_summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
