#!/usr/bin/env python3
"""Independent probes for the w23_loj audit.

The script avoids the claimant's w23 code.  It has two jobs:

1. Stress the smallest exact support-promotion/face-opening model at the
   n=3,k=2 pure-transient H-M corner.  This is the place where a missed local
   H-M branch would immediately make J1' false.
2. Recompute the report's visible-height quantity on the saved w16/w17
   certified matrices, to keep the local-law numerics separated from the
   claimant's assembly summary.
"""

from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
from scipy.optimize import linprog, minimize_scalar


ROOT = Path("/home/tobias/Projects/almost-idempotent-positive-maps")
W16 = ROOT / "agent-A/explorations/classical-portfolio/experiments/out/w16_cert_audit/w16_best_rational_instance.json"
W17_MAIN = ROOT / "agent-A/explorations/classical-portfolio/experiments/out/w17_cert_audit/main_rational_instance.json"
W17_ROBUST = ROOT / "agent-A/explorations/classical-portfolio/experiments/out/w17_cert_audit/robust_rational_instance.json"
W20 = Path("/tmp/codex-sigma-wall/w20_t1_audit/independent_visibility_results.json")
W21 = Path("/tmp/codex-sigma-wall/w21_second/second_order_full_records.json")


def delta(P: np.ndarray) -> float:
    return float(np.max(np.sum(np.maximum(-P, 0.0), axis=1)))


def idem_err(P: np.ndarray) -> float:
    return float(np.max(np.abs(P @ P - P)))


def row_err(P: np.ndarray) -> float:
    return float(np.max(np.abs(P.sum(axis=1) - 1.0)))


def rank2_pure_corner(b: float, g: float) -> np.ndarray:
    """Exact row-stochastic rank-2 idempotent near [[1,0,0],[0,1,0],[1,0,0]].

    b opens the pure transient state 2 as recurrent support in block 0.
    g opens the same state's transient coefficient toward block 1.
    The two moves are individually H-M; together they force P[0,1] = -b*g.
    """
    den = 1.0 + b
    return np.array(
        [
            [(1.0 + b * g) / den, -b * g, b * (1.0 + b * g) / den],
            [0.0, 1.0, 0.0],
            [(1.0 - g) / den, g, b * (1.0 - g) / den],
        ],
        dtype=float,
    )


def hm_base_branch(c: float) -> np.ndarray:
    return np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0 - c, c, 0.0]])


def hm_promote_branch(c: float) -> np.ndarray:
    return np.array([[1.0 - c, 0.0, c], [0.0, 1.0, 0.0], [1.0 - c, 0.0, c]])


def dist2_to_n3_local_hm(P: np.ndarray) -> tuple[float, str, float]:
    """Frobenius-square distance to the two exact local H-M branches.

    This is not the claimant's chart norm; at this fixed base it is equivalent
    to it and is enough to detect exponent failures.
    """

    def fit(branch):
        res = minimize_scalar(
            lambda x: float(np.sum((P - branch(x)) ** 2)),
            bounds=(0.0, 0.25),
            method="bounded",
            options={"xatol": 1e-14},
        )
        return float(res.fun), float(res.x)

    d_base, c_base = fit(hm_base_branch)
    d_prom, c_prom = fit(hm_promote_branch)
    if d_base <= d_prom:
        return d_base, "face-open", c_base
    return d_prom, "promote", c_prom


def robust_linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None):
    return linprog(
        np.asarray(c, dtype=float),
        A_ub=None if A_ub is None else np.asarray(A_ub, dtype=float),
        b_ub=None if b_ub is None else np.asarray(b_ub, dtype=float),
        A_eq=None if A_eq is None else np.asarray(A_eq, dtype=float),
        b_eq=None if b_eq is None else np.asarray(b_eq, dtype=float),
        bounds=bounds,
        method="highs",
    )


def unique_rows(P: np.ndarray, tol: float = 1e-8) -> tuple[np.ndarray, list[int]]:
    rows: list[np.ndarray] = []
    reps: list[int] = []
    for i, row in enumerate(P):
        if not any(np.max(np.abs(row - old)) <= tol for old in rows):
            rows.append(row.copy())
            reps.append(i)
    return np.array(rows), reps


def l1_distance_to_conv(x: np.ndarray, points: np.ndarray) -> float:
    if len(points) == 0:
        return math.inf
    m, n = points.shape
    c = np.r_[np.zeros(m), np.ones(n)]
    A_ub = []
    b_ub = []
    for j in range(n):
        row = np.zeros(m + n)
        row[:m] = points[:, j]
        row[m + j] = -1.0
        A_ub.append(row)
        b_ub.append(x[j])
        row = np.zeros(m + n)
        row[:m] = -points[:, j]
        row[m + j] = -1.0
        A_ub.append(row)
        b_ub.append(-x[j])
    A_eq = [np.r_[np.ones(m), np.zeros(n)]]
    res = robust_linprog(
        c,
        A_ub=A_ub,
        b_ub=b_ub,
        A_eq=A_eq,
        b_eq=[1.0],
        bounds=[(0.0, None)] * (m + n),
    )
    if not res.success:
        return math.inf
    return float(res.fun)


def exposed_margin(row: np.ndarray, rows: np.ndarray, rho: float) -> float:
    far = [i for i, r in enumerate(rows) if np.sum(np.abs(r - row)) >= rho - 1e-10]
    if not far:
        return math.inf
    n = rows.shape[1]
    t_idx = n + 1
    c = np.zeros(n + 2)
    c[t_idx] = -1.0
    A_ub = []
    b_ub = []
    for r in rows:
        h = np.r_[r, 1.0, 0.0]
        A_ub.append(h)
        b_ub.append(1.0)
        A_ub.append(-h)
        b_ub.append(0.0)
    for i in far:
        coeff = np.r_[-rows[i], -1.0, 1.0]
        A_ub.append(coeff)
        b_ub.append(0.0)
    A_eq = [np.r_[row, 1.0, 0.0]]
    res = robust_linprog(
        c,
        A_ub=A_ub,
        b_ub=b_ub,
        A_eq=A_eq,
        b_eq=[0.0],
        bounds=[(None, None)] * (n + 2),
    )
    if not res.success:
        return -math.inf
    return float(res.x[t_idx])


def visible_height(P: np.ndarray, cluster_tol: float = 1e-8) -> dict:
    rows, reps = unique_rows(P, tol=cluster_tol)
    d = delta(P)
    tau = math.sqrt(max(d, 0.0))
    rho = 4.0 * tau
    kappa = tau / 4.0
    vertices = []
    visible = []
    margins = []
    for i, row in enumerate(rows):
        others = np.array([r for j, r in enumerate(rows) if j != i])
        vdist = math.inf if len(others) == 0 else l1_distance_to_conv(row, others)
        is_vertex = vdist > max(1e-11, cluster_tol / 10.0)
        vertices.append(is_vertex)
        if not is_vertex:
            visible.append(False)
            margins.append(None)
            continue
        margin = math.inf if d <= 1e-14 else exposed_margin(row, rows, rho)
        margins.append(margin)
        visible.append(math.isinf(margin) or margin >= kappa - 1e-8)
    W = np.array([row for row, flag in zip(rows, visible) if flag])
    heights = [l1_distance_to_conv(row, W) for row in P] if len(W) else [math.inf]
    H = float(max(heights))
    return {
        "delta": d,
        "tau": tau,
        "rho": rho,
        "kappa": kappa,
        "unique_rows": int(len(rows)),
        "vertices": int(sum(vertices)),
        "visible": int(sum(visible)),
        "H": H,
        "H_over_delta": (math.inf if d <= 0.0 and H > 1e-12 else (0.0 if d <= 0.0 else H / d)),
        "reps": reps,
        "margins": ["inf" if m is not None and math.isinf(m) else m for m in margins],
    }


@dataclass
class N3Record:
    label: str
    t: float
    b: float
    g: float
    delta: float
    dist2: float
    dist2_over_delta: float
    branch: str
    branch_param: float
    H: float
    H_over_delta: float
    product_bg: float
    eps_inf_l1_to_branch: float
    branch_mu: float
    eps_over_mu_over_8: float | None
    eps_over_tau_over_64: float | None
    idem_err: float
    row_err: float


def n3_records() -> list[N3Record]:
    recipes = [
        ("balanced", lambda t: (t, t)),
        ("promotion-first_face-second", lambda t: (t, t * t)),
        ("face-first_promotion-second", lambda t: (t * t, t)),
        ("both-second", lambda t: (t * t, t * t)),
        ("third-order-face-mix", lambda t: (t, t**3)),
        ("third-order-promotion-mix", lambda t: (t**3, t)),
    ]
    out: list[N3Record] = []
    for label, fn in recipes:
        for t in [1e-1, 3e-2, 1e-2, 3e-3, 1e-3, 3e-4]:
            b, g = fn(t)
            P = rank2_pure_corner(b, g)
            d2, branch, param = dist2_to_n3_local_hm(P)
            Q = hm_promote_branch(param) if branch == "promote" else hm_base_branch(param)
            eps = float(np.max(np.sum(np.abs(P - Q), axis=1)))
            branch_mu = min(param, 1.0 - param) if branch == "promote" else 1.0
            d = delta(P)
            hv = visible_height(P)
            out.append(
                N3Record(
                    label=label,
                    t=t,
                    b=b,
                    g=g,
                    delta=d,
                    dist2=d2,
                    dist2_over_delta=(d2 / d if d > 0 else 0.0),
                    branch=branch,
                    branch_param=param,
                    H=hv["H"],
                    H_over_delta=float(hv["H_over_delta"]),
                    product_bg=b * g,
                    eps_inf_l1_to_branch=eps,
                    branch_mu=branch_mu,
                    eps_over_mu_over_8=(eps / (branch_mu / 8.0) if branch_mu > 0 else None),
                    eps_over_tau_over_64=(eps / (math.sqrt(d) / 64.0) if d > 0 else None),
                    idem_err=idem_err(P),
                    row_err=row_err(P),
                )
            )
    return out


def n3_grid_summary() -> dict:
    worst = None
    records = []
    for b in np.geomspace(1e-6, 5e-2, 34):
        for g in np.geomspace(1e-6, 5e-2, 34):
            P = rank2_pure_corner(float(b), float(g))
            d2, branch, param = dist2_to_n3_local_hm(P)
            d = delta(P)
            ratio = d2 / d if d > 0 else 0.0
            rec = {
                "b": float(b),
                "g": float(g),
                "delta": d,
                "dist2": d2,
                "ratio": ratio,
                "branch": branch,
                "branch_param": param,
            }
            records.append(rec)
            if worst is None or ratio > worst["ratio"]:
                worst = rec
    assert worst is not None
    return {
        "grid_records": len(records),
        "max_dist2_over_delta": worst["ratio"],
        "worst": worst,
        "median_dist2_over_delta": float(np.median([r["ratio"] for r in records])),
    }


def load_matrix(path: Path) -> np.ndarray:
    data = json.loads(path.read_text(encoding="utf-8"))
    key = "P_decimal" if "P_decimal" in data else "P"
    return np.array(data[key], dtype=float)


def certified_summaries() -> list[dict]:
    out = []
    for name, path in [("w16_rational", W16), ("w17_main", W17_MAIN), ("w17_robust", W17_ROBUST)]:
        P = load_matrix(path)
        hv = visible_height(P)
        out.append(
            {
                "name": name,
                "path": str(path),
                "n": int(P.shape[0]),
                "delta": hv["delta"],
                "tau": hv["tau"],
                "H": hv["H"],
                "H_over_delta": hv["H_over_delta"],
                "H_over_tau": hv["H"] / hv["tau"] if hv["tau"] > 0 else 0.0,
                "visible": hv["visible"],
                "vertices": hv["vertices"],
                "idem_err": idem_err(P),
                "row_err": row_err(P),
            }
        )
    return out


def audited_stress_scalar_summary() -> dict:
    w20 = json.loads(W20.read_text(encoding="utf-8"))
    tiny = w20["tiny_active_scale_sweep"]
    local = [r for r in tiny["records"] if r["t"] <= tiny["mu"]]
    transition = [r for r in tiny["records"] if r["t"] > tiny["mu"]]

    w21 = json.loads(W21.read_text(encoding="utf-8"))
    local21 = []
    transition21 = []
    for rec in w21["records"]:
        min_entry = float(rec["min_positive_entry"])
        for sample in rec["samples"]:
            item = sample | {"min_positive_entry": min_entry, "stratum": rec["stratum"]}
            if sample["t"] < 0.1 * min_entry:
                local21.append(item)
            else:
                transition21.append(item)

    def max_ratio(items: Iterable[dict]) -> float | None:
        vals = [float(x["H_over_delta"]) for x in items if math.isfinite(float(x["H_over_delta"]))]
        return max(vals) if vals else None

    return {
        "source_note": "scalar reuse of previously audited w20/w21 artifacts; not counted as new matrix recomputation",
        "w20_tiny_mu": tiny["mu"],
        "w20_local_samples": len(local),
        "w20_local_max_H_over_delta": max_ratio(local),
        "w20_transition_samples": len(transition),
        "w20_transition_max_H_over_delta": max_ratio(transition),
        "w21_local_samples": len(local21),
        "w21_local_max_H_over_delta": max_ratio(local21),
        "w21_transition_samples": len(transition21),
        "w21_transition_max_H_over_delta": max_ratio(transition21),
    }


def main() -> None:
    n3 = n3_records()
    result = {
        "n3_exact_product_family": [asdict(r) for r in n3],
        "n3_grid_summary": n3_grid_summary(),
        "certified_matrix_recomputations": certified_summaries(),
        "audited_stress_scalar_summary": audited_stress_scalar_summary(),
    }
    Path("audit_probe_results.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    lines = [
        "w23_loj_audit independent probe",
        "",
        "n=3,k=2 exact product-family summary:",
        json.dumps(result["n3_grid_summary"], indent=2),
        "",
        "selected exact mixed jets:",
    ]
    for r in n3:
        if r.t in {0.01, 0.001, 0.0003}:
            lines.append(
                f"{r.label} t={r.t:.1e} b={r.b:.3e} g={r.g:.3e} "
                f"delta={r.delta:.3e} dist2={r.dist2:.3e} "
                f"dist2/delta={r.dist2_over_delta:.6g} H/delta={r.H_over_delta:.6g} "
                f"eps/(mu/8)={r.eps_over_mu_over_8:.6g} "
                f"eps/(tau/64)={r.eps_over_tau_over_64:.6g} branch={r.branch}"
            )
    lines.extend(
        [
            "",
            "certified matrix recomputations:",
            json.dumps(result["certified_matrix_recomputations"], indent=2),
            "",
            "w20/w21 audited scalar stress windows:",
            json.dumps(result["audited_stress_scalar_summary"], indent=2),
        ]
    )
    Path("audit_probe_summary.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
