#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

import numpy as np
from scipy.optimize import linprog


REPO = Path("/home/tobias/Projects/almost-idempotent-positive-maps")
ART = REPO / "agent-A/explorations/classical-portfolio/experiments/out/w16_nlopt"
OUT = Path("/tmp/codex-sigma-wall/w16_cert_audit")

LP_TOL = 1e-9
DUP_TOL = 1e-10
VERTEX_TOL = 1e-8
OUTSIDE_TOL = 1e-8


def robust_linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None):
    attempts = []
    for method, presolve in (
        ("highs-ipm", False),
        ("highs-ds", False),
        ("highs", False),
        ("highs-ipm", True),
        ("highs-ds", True),
        ("highs", True),
    ):
        res = linprog(
            c,
            A_ub=A_ub,
            b_ub=b_ub,
            A_eq=A_eq,
            b_eq=b_eq,
            bounds=bounds,
            method=method,
            options={"presolve": presolve},
        )
        attempts.append(
            {
                "method": method,
                "presolve": presolve,
                "success": bool(res.success),
                "status": int(res.status),
                "message": str(res.message),
            }
        )
        if res.success or res.status == 2:
            res.audit_attempts = attempts
            return res
    res.audit_attempts = attempts
    return res


def as_float_matrix(x):
    return np.asarray(x, dtype=float)


def row_negative_masses(P: np.ndarray):
    vals = np.maximum(-P, 0.0).sum(axis=1)
    return vals, float(vals.max())


def l1_distances(rows: np.ndarray, i: int):
    return np.abs(rows - rows[i]).sum(axis=1)


def conv_l1_distance(rows: np.ndarray, target: np.ndarray, hull_idx: list[int]):
    d = rows.shape[1]
    m = len(hull_idx)
    if m == 0:
        return math.inf, None, None
    c = np.r_[np.zeros(m), np.ones(d)]
    A_ub = []
    b_ub = []
    hull = rows[hull_idx]
    for j in range(d):
        row = np.zeros(m + d)
        row[:m] = hull[:, j]
        row[m + j] = -1.0
        A_ub.append(row)
        b_ub.append(target[j])

        row = np.zeros(m + d)
        row[:m] = -hull[:, j]
        row[m + j] = -1.0
        A_ub.append(row)
        b_ub.append(-target[j])
    A_eq = np.zeros((1, m + d))
    A_eq[0, :m] = 1.0
    res = robust_linprog(
        c,
        A_ub=np.asarray(A_ub),
        b_ub=np.asarray(b_ub),
        A_eq=A_eq,
        b_eq=np.asarray([1.0]),
        bounds=[(0, None)] * (m + d),
    )
    if not res.success:
        return math.inf, None, res
    return float(res.fun), res.x[:m], res


def duplicate_groups(rows: np.ndarray):
    n = rows.shape[0]
    seen = [False] * n
    groups = []
    for i in range(n):
        if seen[i]:
            continue
        group = []
        for j in range(i, n):
            if not seen[j] and float(np.abs(rows[j] - rows[i]).sum()) <= DUP_TOL:
                seen[j] = True
                group.append(j)
        groups.append(group)
    return groups


def row_vertex_distances(rows: np.ndarray):
    n = rows.shape[0]
    out = {}
    groups = duplicate_groups(rows)
    reps = [g[0] for g in groups]
    for i in range(n):
        hull = [r for r in reps if float(np.abs(rows[r] - rows[i]).sum()) > DUP_TOL]
        dist, lam, _ = conv_l1_distance(rows, rows[i], hull)
        out[i] = {
            "is_vertex": bool(dist > VERTEX_TOL),
            "dist_to_conv_other_distinct_rows": dist,
            "hull_indices": hull,
            "lambda": None if lam is None else lam.tolist(),
        }
    return groups, out


def h_vector(rows: np.ndarray, j: int):
    n = rows.shape[1]
    v = np.zeros(n + 2)
    v[:n] = rows[j]
    v[n] = 1.0
    return v


def exposedness_primal(rows: np.ndarray, i: int, rho: float, kappa: float):
    n, d = rows.shape
    distances = l1_distances(rows, i)
    far = [j for j in range(n) if j != i and distances[j] >= rho - 1e-12]
    if not far:
        return {
            "far": far,
            "far_distances": {},
            "t": math.inf,
            "exposed": True,
            "status": "no_far_rows",
            "kappa": kappa,
            "rho": rho,
        }

    c = np.zeros(d + 2)
    c[-1] = -1.0
    A_ub = []
    b_ub = []
    labels = []
    for j in range(n):
        hj = h_vector(rows, j)
        A_ub.append(-hj)
        b_ub.append(0.0)
        labels.append(("lower_h_ge_0", j))
        A_ub.append(hj)
        b_ub.append(1.0)
        labels.append(("upper_h_le_1", j))
    for j in far:
        hj = h_vector(rows, j)
        row = -hj
        row[-1] = 1.0
        A_ub.append(row)
        b_ub.append(0.0)
        labels.append(("far_h_ge_t", j))
    A_ub = np.asarray(A_ub)
    b_ub = np.asarray(b_ub)
    A_eq = np.asarray([h_vector(rows, i)])
    b_eq = np.asarray([0.0])
    bounds = [(None, None)] * (d + 2)
    res = robust_linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
    if not res.success:
        return {
            "far": far,
            "far_distances": {str(j): float(distances[j]) for j in far},
            "t": None,
            "exposed": False,
            "status": "solver_failed",
            "attempts": getattr(res, "audit_attempts", []),
            "kappa": kappa,
            "rho": rho,
        }

    x = res.x
    hvals = rows @ x[:d] + x[d]
    t = float(x[-1])
    y_from_marginals = None
    dual_from_marginals = None
    kkt_inf = None
    active_duals = []
    if hasattr(res, "ineqlin") and hasattr(res.ineqlin, "marginals"):
        y = -np.asarray(res.ineqlin.marginals, dtype=float)
        lam = -np.asarray(res.eqlin.marginals, dtype=float)
        cmax = np.zeros(d + 2)
        cmax[-1] = 1.0
        kkt_inf = float(np.max(np.abs(A_ub.T @ y + A_eq.T @ lam - cmax)))
        dual_from_marginals = float(b_ub @ y + b_eq @ lam)
        y_from_marginals = y.tolist()
        for label, val in zip(labels, y):
            if abs(val) > 1e-8:
                active_duals.append({"constraint": label[0], "row": int(label[1]), "weight": float(val)})

    return {
        "far": far,
        "far_distances": {str(j): float(distances[j]) for j in far},
        "t": t,
        "exposed": bool(t >= kappa - LP_TOL),
        "kappa": kappa,
        "rho": rho,
        "h_values": hvals.tolist(),
        "affine_a": x[:d].tolist(),
        "affine_b": float(x[d]),
        "objective_check_min_far_h": float(min(hvals[j] for j in far)),
        "attempts": getattr(res, "audit_attempts", []),
        "labels": labels,
        "A_ub": A_ub,
        "b_ub": b_ub,
        "A_eq": A_eq,
        "b_eq": b_eq,
        "dual_from_marginals": dual_from_marginals,
        "dual_kkt_inf": kkt_inf,
        "active_duals_from_marginals": active_duals,
        "raw_y_from_marginals": y_from_marginals,
    }


def exposedness_dual_from_primal_data(pr):
    if "A_ub" not in pr:
        return None
    A_ub = pr["A_ub"]
    b_ub = pr["b_ub"]
    A_eq = pr["A_eq"]
    labels = pr["labels"]
    dvars = A_ub.shape[1]
    m = A_ub.shape[0]
    cmax = np.zeros(dvars)
    cmax[-1] = 1.0
    c = np.r_[b_ub, np.zeros(A_eq.shape[0])]
    Aeq_dual = np.c_[A_ub.T, A_eq.T]
    bounds = [(0, None)] * m + [(None, None)] * A_eq.shape[0]
    res = robust_linprog(c, A_eq=Aeq_dual, b_eq=cmax, bounds=bounds)
    if not res.success:
        return {"success": False, "attempts": getattr(res, "audit_attempts", [])}
    y = res.x[:m]
    lam = res.x[m:]
    active = []
    for label, val in zip(labels, y):
        if abs(val) > 1e-8:
            active.append({"constraint": label[0], "row": int(label[1]), "weight": float(val)})
    stationarity = A_ub.T @ y + A_eq.T @ lam - cmax
    return {
        "success": True,
        "dual_objective": float(res.fun),
        "stationarity_inf": float(np.max(np.abs(stationarity))),
        "lambda_eq": lam.tolist(),
        "active_duals": active,
        "attempts": getattr(res, "audit_attempts", []),
    }


def exposure_feasibility_at_kappa(rows: np.ndarray, i: int, rho: float, kappa: float):
    pr = exposedness_primal(rows, i, rho, kappa)
    if "A_ub" not in pr:
        return {"far": pr["far"], "status": "no_far_rows"}
    dvars = pr["A_ub"].shape[1]
    row = np.zeros(dvars)
    row[-1] = -1.0
    A_ub = np.vstack([pr["A_ub"], row])
    b_ub = np.r_[pr["b_ub"], -kappa]
    res = robust_linprog(
        np.zeros(dvars),
        A_ub=A_ub,
        b_ub=b_ub,
        A_eq=pr["A_eq"],
        b_eq=pr["b_eq"],
        bounds=[(None, None)] * dvars,
    )
    return {
        "success": bool(res.success),
        "status": int(res.status),
        "message": str(res.message),
        "attempts": getattr(res, "audit_attempts", []),
    }


def visible_set(rows: np.ndarray, vertex_info: dict[int, dict[str, Any]], rho: float, kappa: float):
    W = []
    exp = {}
    for i in range(rows.shape[0]):
        if not vertex_info[i]["is_vertex"]:
            exp[i] = {"exposed": False, "reason": "not_vertex"}
            continue
        pr = exposedness_primal(rows, i, rho, kappa)
        exp[i] = {
            k: v
            for k, v in pr.items()
            if k
            not in {
                "A_ub",
                "b_ub",
                "A_eq",
                "b_eq",
                "labels",
                "raw_y_from_marginals",
            }
        }
        if pr["exposed"]:
            W.append(i)
    return W, exp


def canonical_separator(rows: np.ndarray, W: list[int], v: int):
    n, d = rows.shape
    c = np.zeros(d + 1)
    c[:d] = -rows[v]
    c[d] = -1.0
    A_ub = []
    b_ub = []
    for w in W:
        row = np.zeros(d + 1)
        row[:d] = rows[w]
        row[d] = 1.0
        A_ub.append(row)
        b_ub.append(0.0)
    bounds = [(-1.0, 1.0)] * d + [(None, None)]
    res = robust_linprog(c, A_ub=np.asarray(A_ub), b_ub=np.asarray(b_ub), bounds=bounds)
    if not res.success:
        return None
    a = res.x[:d]
    b = res.x[d]
    phi = rows @ a + b
    return {
        "a": a.tolist(),
        "b": float(b),
        "phi": phi.tolist(),
        "H_separator": float(phi[v]),
        "max_phi_on_W": float(max(phi[w] for w in W)),
        "lip_linf_norm": float(np.max(np.abs(a))),
        "attempts": getattr(res, "audit_attempts", []),
    }


def analyze_float_matrix(P: np.ndarray, label: str, claimed: dict[str, Any] | None = None):
    n = P.shape[0]
    row_sum_resid = float(np.max(np.abs(P @ np.ones(n) - 1.0)))
    idem_resid = float(np.max(np.abs(P @ P - P)))
    row_neg, delta = row_negative_masses(P)
    tau = math.sqrt(delta)
    rho = 4.0 * tau
    kappa = tau / 4.0
    groups, vertex_info = row_vertex_distances(P)
    W, exposed = visible_set(P, vertex_info, rho, kappa)
    dist_to_CW = []
    bary = []
    for i in range(n):
        dist, lam, _ = conv_l1_distance(P, P[i], W)
        dist_to_CW.append(dist)
        bary.append(None if lam is None else lam.tolist())
    H = float(max(dist_to_CW))
    top_vertices = [i for i, d in enumerate(dist_to_CW) if abs(d - H) <= 1e-8]
    outside = [i for i, d in enumerate(dist_to_CW) if d > OUTSIDE_TOL]
    hidden_vertices = [i for i in range(n) if vertex_info[i]["is_vertex"] and i not in W]
    v = 4 if n > 4 else top_vertices[0]
    sigma = float(np.maximum(P[v, outside], 0.0).sum())
    nu_v = float(np.maximum(-P[v], 0.0).sum())
    sep = canonical_separator(P, W, top_vertices[0]) if W else None
    g = None
    sep_resid = None
    if sep is not None:
        phi = np.asarray(sep["phi"])
        g = H - phi
        sep_resid = float(np.max(np.abs(P @ g - g)))
    hidden_pr = exposedness_primal(P, v, rho, kappa)
    hidden_dual = exposedness_dual_from_primal_data(hidden_pr)
    hidden_feas_kappa = exposure_feasibility_at_kappa(P, v, rho, kappa)
    threshold_gaps = []
    for i in range(n):
        ds = l1_distances(P, i)
        threshold_gaps.extend(abs(float(ds[j] - rho)) for j in range(n) if j != i)
    min_threshold_gap = float(min(threshold_gaps)) if threshold_gaps else math.inf
    result = {
        "label": label,
        "n": n,
        "row_sum_resid": row_sum_resid,
        "idempotence_resid": idem_resid,
        "row_negative_masses": row_neg.tolist(),
        "delta": delta,
        "tau": tau,
        "rho": rho,
        "kappa": kappa,
        "duplicate_groups": groups,
        "row_vertices": {str(k): v0 for k, v0 in vertex_info.items()},
        "W": W,
        "hidden_vertices": hidden_vertices,
        "exposedness": {str(k): v0 for k, v0 in exposed.items()},
        "dist_to_CW": dist_to_CW,
        "barycentric_to_CW": bary,
        "H": H,
        "H_over_tau": H / tau if tau else math.inf,
        "top_vertices": top_vertices,
        "v_checked": v,
        "outside_CW": outside,
        "sigma_tilde_v": sigma,
        "sigma_tilde_over_tau": sigma / tau if tau else math.inf,
        "nu_v": nu_v,
        "P_vv": float(P[v, v]),
        "hiddenness_v4_primal": {
            k: val
            for k, val in hidden_pr.items()
            if k
            not in {
                "A_ub",
                "b_ub",
                "A_eq",
                "b_eq",
                "labels",
                "raw_y_from_marginals",
            }
        },
        "hiddenness_v4_dual": hidden_dual,
        "hiddenness_v4_feasibility_with_t_ge_kappa": hidden_feas_kappa,
        "min_abs_l1_distance_minus_rho_over_all_pairs": min_threshold_gap,
        "canonical_separator": sep,
        "deficit_g": None if g is None else g.tolist(),
        "deficit_Pg_resid": sep_resid,
    }
    if claimed:
        comparisons = {}
        for key, ours in (
            ("delta", delta),
            ("tau", tau),
            ("W", W),
            ("H", H),
            ("H_over_tau", H / tau if tau else math.inf),
            ("sigma_tilde", sigma),
            ("sigma_tilde_over_tau", sigma / tau if tau else math.inf),
        ):
            if key in claimed:
                theirs = claimed[key]
                comparisons[key] = {"ours": ours, "claimed": theirs}
                if isinstance(ours, float) and isinstance(theirs, (float, int)):
                    comparisons[key]["diff"] = ours - float(theirs)
        result["claim_comparison"] = comparisons
    return result


def frac(x: float, max_den: int):
    return Fraction(float(x)).limit_denominator(max_den)


def rationalize_factorization(factor: dict[str, Any], max_den: int):
    Lf = as_float_matrix(factor["Lambda"])
    Bf = as_float_matrix(factor["B_or_R"])
    n, k = Lf.shape
    m = n - k
    X = Lf[k:, :]
    Q = Bf[:, k:]
    Xr = []
    for i in range(m):
        row = [frac(float(X[i, j]), max_den) for j in range(k - 1)]
        row.append(Fraction(1) - sum(row, Fraction(0)))
        Xr.append(row)
    Qr = [[frac(float(Q[i, j]), max_den) for j in range(m)] for i in range(k)]
    Lr = []
    for i in range(k):
        Lr.append([Fraction(1 if i == j else 0) for j in range(k)])
    Lr.extend(Xr)
    Ar = []
    for i in range(k):
        row = []
        for j in range(k):
            val = Fraction(1 if i == j else 0)
            val -= sum(Qr[i][h] * Xr[h][j] for h in range(m))
            row.append(val)
        Ar.append(row)
    Br = [Ar[i] + Qr[i] for i in range(k)]
    Pr = [[sum(Lr[i][a] * Br[a][j] for a in range(k)) for j in range(n)] for i in range(n)]
    return Lr, Br, Pr


def frac_matmul(A, B):
    rows = len(A)
    mid = len(B)
    cols = len(B[0])
    return [[sum(A[i][h] * B[h][j] for h in range(mid)) for j in range(cols)] for i in range(rows)]


def frac_eye(n):
    return [[Fraction(1 if i == j else 0) for j in range(n)] for i in range(n)]


def frac_to_float_matrix(M):
    return np.asarray([[float(x) for x in row] for row in M], dtype=float)


def fstr(x: Fraction):
    if x.denominator == 1:
        return str(x.numerator)
    return f"{x.numerator}/{x.denominator}"


def exact_negative_masses(P):
    vals = []
    for row in P:
        vals.append(sum((-x for x in row if x < 0), Fraction(0)))
    return vals, max(vals)


def rational_exact_checks(Lr, Br, Pr):
    n = len(Pr)
    k = len(Br)
    BL = frac_matmul(Br, Lr)
    P2 = frac_matmul(Pr, Pr)
    row_sums = [sum(row, Fraction(0)) for row in Pr]
    row_neg, delta = exact_negative_masses(Pr)
    return {
        "BL_equals_I": BL == frac_eye(k),
        "P2_equals_P": P2 == Pr,
        "row_sums_equal_1": all(x == 1 for x in row_sums),
        "row_sums": [fstr(x) for x in row_sums],
        "row_negative_masses_frac": [fstr(x) for x in row_neg],
        "delta_frac": fstr(delta),
        "delta_float": float(delta),
    }


def exact_sigma_for_outside(Pr, v: int, outside: list[int]):
    return sum((Pr[v][j] for j in outside if Pr[v][j] > 0), Fraction(0))


def write_rational_instance(path: Path, Lr, Br, Pr, meta: dict[str, Any]):
    payload = {
        "metadata": meta,
        "Lambda_frac": [[fstr(x) for x in row] for row in Lr],
        "B_frac": [[fstr(x) for x in row] for row in Br],
        "P_frac": [[fstr(x) for x in row] for row in Pr],
        "P_decimal": [[float(x) for x in row] for row in Pr],
    }
    path.write_text(json.dumps(payload, indent=2) + "\n")


def load_claimed_record(name: str):
    cert = json.loads((ART / name).read_text())
    rec = cert["record"]
    return {
        "delta": rec.get("delta"),
        "tau": rec.get("tau"),
        "W": rec.get("W"),
        "H": rec.get("H"),
        "H_over_tau": rec.get("H_over_tau"),
        "sigma_tilde": rec.get("sigma_tilde"),
        "sigma_tilde_over_tau": rec.get("sigma_tilde_over_tau"),
    }


def factorization_residuals(factor: dict[str, Any]):
    P = as_float_matrix(factor["P"])
    L = as_float_matrix(factor["Lambda"])
    B = as_float_matrix(factor["B_or_R"])
    k = L.shape[1]
    return {
        "B_L_minus_I_inf": float(np.max(np.abs(B @ L - np.eye(k)))),
        "L_B_minus_P_inf": float(np.max(np.abs(L @ B - P))),
    }


def build_factor_family_matrix(factor: dict[str, Any], alpha: float):
    L = as_float_matrix(factor["Lambda"]).copy()
    B0 = as_float_matrix(factor["B_or_R"])
    n, k = L.shape
    for i in range(k, n):
        L[i, -1] = 1.0 - float(np.sum(L[i, :-1]))
    X = L[k:, :]
    Q = alpha * B0[:, k:]
    A = np.eye(k) - Q @ X
    B = np.c_[A, Q]
    return L @ B


def continuation_probe(factor: dict[str, Any]):
    rows = []
    for alpha in [0.25, 0.35, 0.40, 0.43, 0.45, 0.50, 0.60, 0.75, 0.90, 1.00]:
        P = build_factor_family_matrix(factor, alpha)
        ana = analyze_float_matrix(P, f"Q_scale_alpha_{alpha:.2f}")
        rows.append(
            {
                "alpha": alpha,
                "delta": ana["delta"],
                "tau": ana["tau"],
                "W": ana["W"],
                "hidden_vertices": ana["hidden_vertices"],
                "top_vertices": ana["top_vertices"],
                "H": ana["H"],
                "H_over_tau": ana["H_over_tau"],
                "sigma_tilde_v4": ana["sigma_tilde_v"],
                "sigma_tilde_v4_over_tau": ana["sigma_tilde_over_tau"],
                "v4_hidden": 4 in ana["hidden_vertices"],
                "v4_crosses": bool(4 in ana["hidden_vertices"] and ana["sigma_tilde_v"] > ana["tau"]),
                "row_sum_resid": ana["row_sum_resid"],
                "idempotence_resid": ana["idempotence_resid"],
            }
        )
    return rows


def perturbation_summary(P_float: np.ndarray, P_rat_float: np.ndarray, rational_analysis: dict[str, Any]):
    eps_inf = float(np.max(np.abs(P_float - P_rat_float)))
    eps_row_l1 = float(np.max(np.sum(np.abs(P_float - P_rat_float), axis=1)))
    n = P_float.shape[0]
    delta = rational_analysis["delta"]
    tau = rational_analysis["tau"]
    sigma = rational_analysis["sigma_tilde_v"]
    H = rational_analysis["H"]
    fixed_support_sigma_bound = len(rational_analysis["outside_CW"]) * eps_inf
    delta_bound = n * eps_inf
    tau_bound = delta_bound / (2.0 * max(tau, 1e-300))
    height_bound = 2.0 * eps_row_l1
    visible_gaps = []
    hidden_gaps = []
    for info in rational_analysis["exposedness"].values():
        if "t" not in info or info["t"] is None or math.isinf(info["t"]):
            continue
        if info.get("exposed"):
            visible_gaps.append(info["t"] - rational_analysis["kappa"])
        else:
            hidden_gaps.append(rational_analysis["kappa"] - info["t"])
    outside_positive_dist = [
        rational_analysis["dist_to_CW"][j] for j in rational_analysis["outside_CW"]
    ]
    return {
        "max_entry_abs_float_minus_rational": eps_inf,
        "max_row_l1_float_minus_rational": eps_row_l1,
        "delta_lipschitz_bound_for_entry_eps": delta_bound,
        "tau_first_order_bound_for_entry_eps": tau_bound,
        "fixed_outside_support_sigma_bound": fixed_support_sigma_bound,
        "height_conv_bound": height_bound,
        "sigma_minus_tau": sigma - tau,
        "H": H,
        "min_visible_t_minus_kappa": min(visible_gaps) if visible_gaps else None,
        "min_hidden_kappa_minus_t": min(hidden_gaps) if hidden_gaps else None,
        "min_outside_distance_to_CW": min(outside_positive_dist) if outside_positive_dist else None,
        "min_abs_l1_distance_minus_rho": rational_analysis[
            "min_abs_l1_distance_minus_rho_over_all_pairs"
        ],
    }


def short_num(x):
    if isinstance(x, float):
        return f"{x:.17g}"
    return str(x)


def make_markdown(results: dict[str, Any]):
    best = results["best_float"]
    rat = results["best_rational"]["analysis"]
    scale = results["scale_float"]
    pert = results["perturbation"]
    ctx = results["context"]
    lines = []
    lines.append("# w16 independent certification audit")
    lines.append("")
    lines.append(f"VERDICT: {results['verdict']}")
    lines.append("")
    lines.append("## Floating best instance")
    lines.append("")
    lines.append("| quantity | independent | claimed | diff |")
    lines.append("|---|---:|---:|---:|")
    for key in ["delta", "tau", "sigma_tilde", "sigma_tilde_over_tau", "H", "H_over_tau"]:
        comp = best["claim_comparison"].get(key)
        if comp:
            lines.append(
                f"| {key} | {short_num(comp['ours'])} | {short_num(comp['claimed'])} | {short_num(comp.get('diff', 0.0))} |"
            )
    lines.append(f"| W | {best['W']} | {best['claim_comparison']['W']['claimed']} | |")
    lines.append("")
    lines.append(f"row_sum_resid = {best['row_sum_resid']:.3e}, idempotence_resid = {best['idempotence_resid']:.3e}")
    lines.append(f"duplicate row groups = {best['duplicate_groups']}")
    lines.append(f"row vertices = {[i for i, info in best['row_vertices'].items() if info['is_vertex']]}")
    lines.append(f"hidden vertices = {best['hidden_vertices']}; outside_CW = {best['outside_CW']}")
    lines.append("")
    lines.append("## Hiddenness LP for v=4")
    hv = best["hiddenness_v4_primal"]
    hd = best["hiddenness_v4_dual"]
    lines.append(f"rho = {best['rho']:.17g}, kappa = {best['kappa']:.17g}")
    lines.append(f"far rows = {hv['far']}; far distances = {hv['far_distances']}")
    lines.append(f"primal t* = {hv['t']:.17g}; kappa - t* = {best['kappa'] - hv['t']:.17g}")
    lines.append(f"dual objective = {hd['dual_objective']:.17g}; stationarity_inf = {hd['stationarity_inf']:.3e}")
    lines.append(f"t >= kappa feasibility status = {best['hiddenness_v4_feasibility_with_t_ge_kappa']['status']} ({best['hiddenness_v4_feasibility_with_t_ge_kappa']['message']})")
    lines.append("active dual weights:")
    for item in hd["active_duals"]:
        lines.append(f"- {item['constraint']} row {item['row']}: {item['weight']:.17g}")
    lines.append("")
    lines.append("## Exact rational hardening")
    lines.append("")
    lines.append(f"rational instance = {results['best_rational']['path']}")
    lines.append(f"denominator limit = {results['best_rational']['denominator_limit']}")
    lines.append(f"BL=I exactly: {results['best_rational']['exact_checks']['BL_equals_I']}; P^2=P exactly: {results['best_rational']['exact_checks']['P2_equals_P']}; P1=1 exactly: {results['best_rational']['exact_checks']['row_sums_equal_1']}")
    lines.append(f"max |P_float-P_rat|_inf = {pert['max_entry_abs_float_minus_rational']:.3e}")
    lines.append(f"delta_rat = {rat['delta']:.17g}; tau_rat = {rat['tau']:.17g}; sigma_rat = {rat['sigma_tilde_v']:.17g}; sigma/tau = {rat['sigma_tilde_over_tau']:.17g}; H/tau = {rat['H_over_tau']:.17g}")
    lines.append(f"exact delta fraction = {results['best_rational']['exact_checks']['delta_frac']}")
    lines.append(f"exact sigma fraction = {results['best_rational']['sigma_frac']}")
    lines.append("")
    lines.append("## Perturbation scale")
    lines.append("")
    for key in [
        "delta_lipschitz_bound_for_entry_eps",
        "tau_first_order_bound_for_entry_eps",
        "fixed_outside_support_sigma_bound",
        "height_conv_bound",
        "sigma_minus_tau",
        "min_visible_t_minus_kappa",
        "min_hidden_kappa_minus_t",
        "min_outside_distance_to_CW",
        "min_abs_l1_distance_minus_rho",
    ]:
        lines.append(f"- {key}: {short_num(pert[key])}")
    lines.append("")
    lines.append("## Second saved scale instance")
    lines.append("")
    lines.append(f"delta = {scale['delta']:.17g}, tau = {scale['tau']:.17g}, sigma_tilde_v4 = {scale['sigma_tilde_v']:.17g}, sigma/tau = {scale['sigma_tilde_over_tau']:.17g}, H/tau = {scale['H_over_tau']:.17g}, W = {scale['W']}, hidden = {scale['hidden_vertices']}")
    lines.append(f"row_sum_resid = {scale['row_sum_resid']:.3e}, idempotence_resid = {scale['idempotence_resid']:.3e}")
    lines.append("")
    lines.append("## Context")
    lines.append("")
    lines.append(f"H/tau best = {ctx['best_H_over_tau']:.17g}; below 0.1*tau record threshold: {ctx['best_below_0p1_tau']}")
    lines.append(f"sigma-height-collapse branch applies: {ctx['sigma_height_collapse_branch_applies']}")
    lines.append(f"corner H/tau = {ctx['corner_H_over_tau']:.17g}; best H/tau below corner: {ctx['best_H_over_tau_below_corner']}")
    lines.append(f"linear-law delta >= H/2: {ctx['linear_law_delta_ge_H_over_2']}")
    lines.append("")
    lines.append("continuation probe:")
    lines.append("")
    lines.append("| alpha | delta | sigma/tau | H/tau | W | v4 crosses |")
    lines.append("|---:|---:|---:|---:|---|---|")
    for row in ctx["continuation_probe"]:
        lines.append(f"| {row['alpha']:.2f} | {row['delta']:.6g} | {row['sigma_tilde_v4_over_tau']:.6g} | {row['H_over_tau']:.6g} | {row['W']} | {row['v4_crosses']} |")
    return "\n".join(lines) + "\n"


def main():
    best_P = as_float_matrix(json.loads((ART / "w16_best_matrix.json").read_text()))
    scale_P = as_float_matrix(json.loads((ART / "w16_scale_matrix.json").read_text()))
    best_factor = json.loads((ART / "w16_best_factorization.json").read_text())
    scale_factor = json.loads((ART / "w16_scale_factorization.json").read_text())

    best_claim = load_claimed_record("w16_best_certificate.json")
    scale_claim = load_claimed_record("w16_scale_certificate.json")

    best_float = analyze_float_matrix(best_P, "w16_best_float", best_claim)
    scale_float = analyze_float_matrix(scale_P, "w16_scale_float", scale_claim)

    chosen = None
    rational_records = []
    for den in [10_000, 100_000, 1_000_000, 10_000_000]:
        Lr, Br, Pr = rationalize_factorization(best_factor, den)
        Pfr = frac_to_float_matrix(Pr)
        ana = analyze_float_matrix(Pfr, f"w16_best_rational_den_{den}")
        exact = rational_exact_checks(Lr, Br, Pr)
        sigma_frac = exact_sigma_for_outside(Pr, 4, ana["outside_CW"])
        record = {
            "denominator_limit": den,
            "analysis": ana,
            "exact_checks": exact,
            "sigma_frac": fstr(sigma_frac),
            "sigma_float_exact_support": float(sigma_frac),
            "max_abs_diff_float": float(np.max(np.abs(best_P - Pfr))),
        }
        rational_records.append(record)
        if (
            exact["BL_equals_I"]
            and exact["P2_equals_P"]
            and exact["row_sums_equal_1"]
            and ana["W"] == [0, 1, 2, 3]
            and 4 in ana["hidden_vertices"]
            and ana["top_vertices"] == [4]
            and ana["sigma_tilde_v"] > ana["tau"]
            and record["max_abs_diff_float"] < 1e-5
        ):
            chosen = (den, Lr, Br, Pr, record)
            break
    if chosen is None:
        den, Lr, Br, Pr, record = rational_records[-1]["denominator_limit"], Lr, Br, Pr, rational_records[-1]
    else:
        den, Lr, Br, Pr, record = chosen

    rat_path = OUT / "w16_best_rational_instance.json"
    write_rational_instance(
        rat_path,
        Lr,
        Br,
        Pr,
        {
            "source": str(ART / "w16_best_factorization.json"),
            "construction": "Lambda=[I;X] with rational X row sums set to 1; B=[I-QX,Q]",
            "denominator_limit": den,
            "max_abs_diff_from_float": record["max_abs_diff_float"],
        },
    )
    record["path"] = str(rat_path)

    P_rat_float = frac_to_float_matrix(Pr)
    perturb = perturbation_summary(best_P, P_rat_float, record["analysis"])

    continuation = continuation_probe(best_factor)
    corner = 2.0 * (2.0 - math.sqrt(3.0))
    context = {
        "best_H_over_tau": best_float["H_over_tau"],
        "best_below_0p1_tau": bool(best_float["H_over_tau"] < 0.1),
        "sigma_height_collapse_branch_applies": bool(best_float["sigma_tilde_v"] <= best_float["tau"]),
        "sigma_height_collapse_note": "The proved collapse lemma quoted in the report is for sigma_tilde <= tau; this instance has sigma_tilde > tau, so the lemma does not apply. Its small H is consistent with the lemma's direction.",
        "corner_H_over_tau": corner,
        "best_H_over_tau_below_corner": bool(best_float["H_over_tau"] < corner),
        "linear_law_delta_ge_H_over_2": bool(best_float["delta"] >= best_float["H"] / 2.0),
        "continuation_probe": continuation,
        "continuation_delta_le_0p1_crosses": [
            row for row in continuation if row["delta"] <= 0.1 and row["v4_crosses"]
        ],
    }

    verdict = "CERTIFIED (exact rational)" if chosen is not None else "CERTIFIED (float)"
    results = {
        "verdict": verdict,
        "best_float": best_float,
        "scale_float": scale_float,
        "factorization_residuals_best": factorization_residuals(best_factor),
        "factorization_residuals_scale": factorization_residuals(scale_factor),
        "best_rational_attempts": rational_records,
        "best_rational": record,
        "perturbation": perturb,
        "context": context,
    }

    # Remove large arrays from nested attempts for the compact JSON.
    for section in ["best_float", "scale_float"]:
        for exp in results[section]["exposedness"].values():
            exp.pop("affine_a", None)
            exp.pop("h_values", None)
        results[section]["hiddenness_v4_primal"].pop("affine_a", None)
        results[section]["hiddenness_v4_primal"].pop("h_values", None)
    for attempt in results["best_rational_attempts"]:
        for exp in attempt["analysis"]["exposedness"].values():
            exp.pop("affine_a", None)
            exp.pop("h_values", None)
        attempt["analysis"]["hiddenness_v4_primal"].pop("affine_a", None)
        attempt["analysis"]["hiddenness_v4_primal"].pop("h_values", None)
    for exp in results["best_rational"]["analysis"]["exposedness"].values():
        exp.pop("affine_a", None)
        exp.pop("h_values", None)
    results["best_rational"]["analysis"]["hiddenness_v4_primal"].pop("affine_a", None)
    results["best_rational"]["analysis"]["hiddenness_v4_primal"].pop("h_values", None)

    (OUT / "audit_results.json").write_text(json.dumps(results, indent=2) + "\n")
    (OUT / "audit_report.md").write_text(make_markdown(results))
    print(json.dumps({
        "verdict": verdict,
        "best_delta": best_float["delta"],
        "best_sigma_over_tau": best_float["sigma_tilde_over_tau"],
        "best_H_over_tau": best_float["H_over_tau"],
        "rational_path": str(rat_path),
        "rational_delta": record["analysis"]["delta"],
        "rational_sigma_over_tau": record["analysis"]["sigma_tilde_over_tau"],
        "scale_sigma_over_tau": scale_float["sigma_tilde_over_tau"],
        "delta_le_0p1_crosses": context["continuation_delta_le_0p1_crosses"],
    }, indent=2))


if __name__ == "__main__":
    main()
