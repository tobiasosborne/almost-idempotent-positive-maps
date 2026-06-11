#!/usr/bin/env python3
"""Second-order dangerous-cone numerics for w21_second.

This script samples H-M strata, constructs tangent directions with
dot_delta(A)=0, integrates exact idempotent arcs through the chart
P(t)=exp(tY)P0 exp(-tY), and estimates the second-order race H/delta.

It deliberately imports the audited w19 implementation for the base H-M
strata, height, delta, and first-order tangent LP conventions.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.linalg import null_space
from scipy.optimize import linprog


AUDIT_PATH = Path(
    "/home/tobias/Projects/almost-idempotent-positive-maps/"
    "agent-A/explorations/classical-portfolio/experiments/out/"
    "w19_tangent_audit/tangent_audit.py"
)


def load_audit_module():
    spec = importlib.util.spec_from_file_location("tangent_audit", AUDIT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {AUDIT_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def min_positive_recurrent_mass(st) -> float:
    vals: list[float] = []
    for pi in st.pis:
        vals.extend(float(x) for x in pi if x > 0)
    return min(vals) if vals else 1.0


def min_positive_entry(P: np.ndarray) -> float:
    vals = P[P > 1e-14]
    return float(vals.min()) if vals.size else 1.0


def flatten(A: np.ndarray) -> np.ndarray:
    return np.asarray(A, dtype=float).reshape(-1)


def unflatten(x: np.ndarray, n: int) -> np.ndarray:
    return np.asarray(x, dtype=float).reshape((n, n))


def active_pairs(P0: np.ndarray, tol: float = 1e-12) -> list[tuple[int, int]]:
    n = P0.shape[0]
    return [(i, j) for i in range(n) for j in range(n) if P0[i, j] <= tol]


def tangent_matrix_equalities(audit, P0: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    return audit.tangent_equalities(P0, P0.size)


def dangerous_equalities(audit, st) -> tuple[np.ndarray, np.ndarray, list[tuple[int, int]]]:
    """Linear equalities for tangent directions with A_ij=0 on active zeros.

    This is a linear slice of the dangerous cone. General dot_delta=0 permits
    A_ij>0 on active zeros; those one-sided directions are sampled separately
    by LP vertices. The equality slice is where genuine second-order delta can
    first appear without a linear positive buffer.
    """
    P0 = audit.build_p0(st)
    n = st.n
    Aeq, beq = tangent_matrix_equalities(audit, P0)
    rows = [row.copy() for row in Aeq]
    rhs = [float(v) for v in beq]
    pairs = active_pairs(P0)
    for i, j in pairs:
        row = np.zeros(n * n)
        row[i * n + j] = 1.0
        rows.append(row)
        rhs.append(0.0)
    return np.array(rows), np.array(rhs), pairs


def dot_delta(audit, st, A: np.ndarray) -> float:
    return float(audit.dot_delta(st, A))


def frozen_D(audit, st, A: np.ndarray) -> float:
    return float(audit.frozen_D(st, A))


def height_visible_clustered(audit, P: np.ndarray, cluster_tol: float) -> dict:
    """Stable visible-height computation with a tunable near-duplicate row tolerance."""
    rows, rep_indices = audit.unique_rows(P, tol=cluster_tol)
    delta = max(float(np.maximum(-row, 0.0).sum()) for row in P)
    tau = math.sqrt(max(delta, 0.0))
    rho = 4.0 * tau
    kappa = tau / 4.0
    vertex_flags: list[bool] = []
    visible_flags: list[bool] = []
    margins: list[float | None] = []
    for idx, row in enumerate(rows):
        others = np.array([r for j, r in enumerate(rows) if j != idx])
        dist = math.inf if len(others) == 0 else audit.l1_distance_to_conv(row, others)
        is_vertex = len(others) == 0 or dist > max(1e-11, cluster_tol / 10.0)
        vertex_flags.append(is_vertex)
        if not is_vertex:
            visible_flags.append(False)
            margins.append(None)
            continue
        if delta <= 1e-16:
            margin = math.inf
        else:
            margin = audit.exposed_margin(row, rows, rho)
        margins.append(margin)
        visible_flags.append(math.isinf(margin) or margin + 1e-9 >= kappa)
    visible_points = np.array([row for row, flag in zip(rows, visible_flags) if flag])
    heights = [audit.l1_distance_to_conv(row, visible_points) for row in P] if len(visible_points) else [math.inf]
    return {
        "delta": delta,
        "tau": tau,
        "rho": rho,
        "kappa": kappa,
        "unique_rows": len(rows),
        "representatives": rep_indices,
        "vertices": int(sum(vertex_flags)),
        "visible": int(sum(visible_flags)),
        "margins": [None if m is None else ("inf" if math.isinf(m) else m) for m in margins],
        "H": max(heights),
        "row_heights": heights,
    }


def exact_arc(audit, P0: np.ndarray, A: np.ndarray, t: float) -> np.ndarray:
    return audit.exact_arc(P0, A, t)


def exact_second_derivative(audit, P0: np.ndarray, A: np.ndarray) -> np.ndarray:
    """Return B where P(t)=P0+tA+t^2 B+O(t^3) for the exact arc."""
    n = P0.shape[0]
    I = np.eye(n)
    C = P0 @ A @ (I - P0)
    D = (I - P0) @ A @ P0
    Y = D - C
    return 0.5 * (Y @ Y @ P0 + P0 @ Y @ Y - 2.0 * Y @ P0 @ Y)


def second_delta_from_B(P0: np.ndarray, A: np.ndarray, B: np.ndarray) -> float:
    vals = []
    for i in range(P0.shape[0]):
        row_cost = 0.0
        for j in range(P0.shape[1]):
            if P0[i, j] <= 1e-12 and abs(A[i, j]) <= 1e-9:
                row_cost += max(-float(B[i, j]), 0.0)
        vals.append(row_cost)
    return max(vals) if vals else 0.0


def normalize_A(A: np.ndarray) -> np.ndarray:
    m = float(np.max(np.abs(A)))
    if m <= 0:
        return A
    return A / m


@dataclass
class Direction:
    source: str
    A: np.ndarray
    meta: dict


def equality_slice_directions(audit, st, rng: np.random.Generator, samples: int) -> list[Direction]:
    P0 = audit.build_p0(st)
    n = st.n
    Aeq, _beq, _pairs = dangerous_equalities(audit, st)
    ns = null_space(Aeq)
    out: list[Direction] = []
    if ns.size == 0:
        return out
    dim = ns.shape[1]
    for idx in range(samples):
        coeff = rng.normal(size=dim)
        vec = ns @ coeff
        A = normalize_A(unflatten(vec, n))
        if np.max(np.abs(A)) <= 1e-10:
            continue
        out.append(Direction("zero-active-nullspace", A, {"null_dim": int(dim), "sample": idx}))
    # Include coordinate-ish nullspace columns for repeatable edge probes.
    for idx in range(min(dim, samples)):
        A = normalize_A(unflatten(ns[:, idx], n))
        if np.max(np.abs(A)) > 1e-10:
            out.append(Direction("zero-active-basis", A, {"null_dim": int(dim), "basis": idx}))
    return out


def lp_extreme_directions(audit, st, rng: np.random.Generator, samples: int) -> list[Direction]:
    """Sample LP extreme points in the full one-sided dangerous cone."""
    P0 = audit.build_p0(st)
    n = st.n
    base_vars = n * n
    Aeq, beq = tangent_matrix_equalities(audit, P0)
    pairs = active_pairs(P0)
    Aub: list[np.ndarray] = []
    bub: list[float] = []
    # dot_delta=0 is A_ij >= 0 on active zeros.
    for i, j in pairs:
        row = np.zeros(base_vars)
        row[i * n + j] = -1.0
        Aub.append(row)
        bub.append(0.0)
    bounds = [(-1.0, 1.0)] * base_vars
    out: list[Direction] = []
    objectives: list[np.ndarray] = []
    for _ in range(samples):
        objectives.append(rng.normal(size=base_vars))
    # Bias objectives toward active-zero coordinates and gamma-normal coordinates.
    for i, j in pairs[: min(len(pairs), samples)]:
        c = np.zeros(base_vars)
        c[i * n + j] = -1.0
        objectives.append(c)
    for idx, c in enumerate(objectives):
        res = linprog(
            c,
            A_ub=np.array(Aub) if Aub else None,
            b_ub=np.array(bub) if bub else None,
            A_eq=Aeq,
            b_eq=beq,
            bounds=bounds,
            method="highs",
        )
        if not res.success:
            continue
        A = normalize_A(unflatten(res.x, n))
        if np.max(np.abs(A)) <= 1e-10:
            continue
        out.append(Direction("one-sided-lp-extreme", A, {"objective": idx}))
    return out


def recurrent_singleton_endpoint_directions(audit) -> list[tuple[object, Direction]]:
    """Hand targets around n=3 endpoint strata."""
    rng = np.random.default_rng(1234)
    out: list[tuple[object, Direction]] = []
    for st in audit.deterministic_strata(rng):
        if st.name == "n3_k2_endpoint_sweep_1":
            A = np.zeros((3, 3))
            # A row 2 moves toward column 1 positively at the active zero,
            # with row-sum correction in column 0. This is dot_delta=0.
            A[2] = np.array([-1.0, 1.0, 0.0])
            out.append((st, Direction("target-n3-endpoint-positive-face", A, {})))
        if st.name == "n3_k2_endpoint_sweep_0":
            A = np.zeros((3, 3))
            A[2] = np.array([1.0, -1.0, 0.0])
            out.append((st, Direction("target-n3-endpoint-positive-face", A, {})))
    return out


def evaluate_direction(audit, st, direction: Direction, ts: list[float], cluster_factor: float) -> dict:
    P0 = audit.build_p0(st)
    A = direction.A
    B = exact_second_derivative(audit, P0, A)
    q_delta_B = second_delta_from_B(P0, A, B)
    samples = []
    for t in ts:
        P = exact_arc(audit, P0, A, t)
        cluster_tol = max(1e-12, cluster_factor * t * t)
        hv = height_visible_clustered(audit, P, cluster_tol=cluster_tol)
        delta = float(hv["delta"])
        H = float(hv["H"])
        ratio = math.inf if delta <= 0 and H > 0 else (0.0 if delta <= 0 else H / delta)
        samples.append(
            {
                "t": t,
                "delta": delta,
                "H": H,
                "delta_over_t": delta / t,
                "H_over_t": H / t if math.isfinite(H) else math.inf,
                "delta_over_t2": delta / (t * t),
                "H_over_t2": H / (t * t) if math.isfinite(H) else math.inf,
                "H_over_delta": ratio,
                "visible": int(hv["visible"]),
                "vertices": int(hv["vertices"]),
                "unique_rows": int(hv["unique_rows"]),
                "idempotence_residual": float(np.max(np.abs(P @ P - P))),
                "row_sum_residual": float(np.max(np.abs(P @ np.ones(P.shape[0]) - 1.0))),
            }
        )
    finite_tail = [s for s in samples[-3:] if math.isfinite(s["H_over_delta"])]
    tail_ratio = max((s["H_over_delta"] for s in finite_tail), default=math.inf)
    tail_delta_t2 = [s["delta_over_t2"] for s in samples[-3:]]
    tail_H_t2 = [s["H_over_t2"] for s in samples[-3:] if math.isfinite(s["H_over_t2"])]
    max_active_negative_A = 0.0
    min_active_A = math.inf
    for i, j in active_pairs(P0):
        max_active_negative_A = max(max_active_negative_A, max(-float(A[i, j]), 0.0))
        min_active_A = min(min_active_A, float(A[i, j]))
    return {
        "stratum": st.name,
        "n": st.n,
        "k": st.k,
        "transients": len(st.transients),
        "block_sizes": [len(b) for b in st.blocks],
        "mu": min_positive_recurrent_mass(st),
        "min_positive_entry": min_positive_entry(P0),
        "source": direction.source,
        "meta": direction.meta,
        "dot_delta": dot_delta(audit, st, A),
        "frozen_D": frozen_D(audit, st, A),
        "max_abs_A": float(np.max(np.abs(A))),
        "min_active_A": min_active_A,
        "max_active_negative_A": max_active_negative_A,
        "q_delta_B": q_delta_B,
        "tail_ratio_max": tail_ratio,
        "tail_delta_over_t2": tail_delta_t2,
        "tail_H_over_t2": tail_H_t2,
        "A": A.tolist(),
        "B": B.tolist(),
        "samples": samples,
    }


def build_strata(audit, rng: np.random.Generator, random_count: int) -> list:
    return audit.deterministic_strata(rng) + audit.random_strata(random_count, rng)


def run(args: argparse.Namespace) -> dict:
    audit = load_audit_module()
    rng = np.random.default_rng(args.seed)
    strata = build_strata(audit, rng, args.random_strata)
    records: list[dict] = []
    generated = 0
    for st in strata:
        dirs: list[Direction] = []
        dirs.extend(equality_slice_directions(audit, st, rng, args.nullspace_samples))
        dirs.extend(lp_extreme_directions(audit, st, rng, args.lp_samples))
        # Deduplicate lightly by rounded flattened coordinates.
        seen: set[tuple[float, ...]] = set()
        unique_dirs: list[Direction] = []
        for d in dirs:
            key = tuple(np.round(flatten(d.A), 8).tolist())
            if key in seen:
                continue
            seen.add(key)
            unique_dirs.append(d)
        for direction in unique_dirs[: args.max_dirs_per_stratum]:
            rec = evaluate_direction(audit, st, direction, args.ts, args.cluster_factor)
            records.append(rec)
            generated += 1
    for st, direction in recurrent_singleton_endpoint_directions(audit):
        records.append(evaluate_direction(audit, st, direction, args.ts, args.cluster_factor))

    finite = [r for r in records if math.isfinite(r["tail_ratio_max"])]
    worst = max(finite, key=lambda r: r["tail_ratio_max"], default=None)
    zero_qdelta_positive_H = [
        r
        for r in records
        if max(r["tail_delta_over_t2"] or [0.0]) <= args.zero_tol
        and max(r["tail_H_over_t2"] or [0.0]) > args.zero_tol
    ]
    suspicious = [
        r
        for r in records
        if math.isfinite(r["tail_ratio_max"]) and r["tail_ratio_max"] > args.suspicious_ratio
    ]
    summary = {
        "seed": args.seed,
        "random_strata": args.random_strata,
        "strata_total": len(strata),
        "directions_total": len(records),
        "audit_module": str(AUDIT_PATH),
        "ts": args.ts,
        "max_tail_ratio": None if worst is None else worst["tail_ratio_max"],
        "worst_stratum": None if worst is None else worst["stratum"],
        "worst_source": None if worst is None else worst["source"],
        "worst_mu": None if worst is None else worst["mu"],
        "counterseed_count": len(zero_qdelta_positive_H),
        "suspicious_count": len(suspicious),
        "dot_delta_max": max((r["dot_delta"] for r in records), default=math.nan),
        "frozen_D_max": max((r["frozen_D"] for r in records), default=math.nan),
    }
    top = sorted(finite, key=lambda r: r["tail_ratio_max"], reverse=True)[: args.top]
    return {
        "summary": summary,
        "top": top,
        "counterseeds": zero_qdelta_positive_H[: args.top],
        "suspicious": suspicious[: args.top],
        "records": [] if args.no_full_records else records,
    }


def write_text(result: dict, path: Path) -> None:
    s = result["summary"]
    lines = ["w21_second dangerous-cone second-order decider"]
    for key in [
        "seed",
        "random_strata",
        "strata_total",
        "directions_total",
        "audit_module",
        "ts",
        "max_tail_ratio",
        "worst_stratum",
        "worst_source",
        "worst_mu",
        "counterseed_count",
        "suspicious_count",
        "dot_delta_max",
        "frozen_D_max",
    ]:
        lines.append(f"{key}: {s[key]}")
    lines.append("")
    lines.append("top limiting-ratio samples")
    for idx, rec in enumerate(result["top"]):
        last = rec["samples"][-1]
        lines.append(
            "#{idx} stratum={stratum} source={source} n={n} k={k} mu={mu:.3g} "
            "dot_delta={dot_delta:.3g} frozen_D={frozen_D:.3g} q_delta_B={q_delta_B:.12g} "
            "tail_ratio={tail_ratio_max:.12g} last_t={t:.3g} "
            "last_delta/t2={delta_over_t2:.12g} last_H/t2={H_over_t2:.12g} "
            "visible={visible} vertices={vertices}".format(idx=idx, **rec, **last)
        )
        lines.append(f"  meta={rec['meta']}")
    if result["counterseeds"]:
        lines.append("")
        lines.append("q_delta=0 with positive q_H candidates")
        for rec in result["counterseeds"]:
            lines.append(
                "stratum={stratum} source={source} tail_H/t2={h} tail_delta/t2={d}".format(
                    stratum=rec["stratum"],
                    source=rec["source"],
                    h=rec["tail_H_over_t2"],
                    d=rec["tail_delta_over_t2"],
                )
            )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=21021)
    parser.add_argument("--random-strata", type=int, default=40)
    parser.add_argument("--nullspace-samples", type=int, default=8)
    parser.add_argument("--lp-samples", type=int, default=12)
    parser.add_argument("--max-dirs-per-stratum", type=int, default=18)
    parser.add_argument("--cluster-factor", type=float, default=1e-3)
    parser.add_argument("--zero-tol", type=float, default=1e-8)
    parser.add_argument("--suspicious-ratio", type=float, default=2.0001)
    parser.add_argument("--top", type=int, default=12)
    parser.add_argument("--out-json", type=Path, default=Path("second_order_results.json"))
    parser.add_argument("--out-txt", type=Path, default=Path("second_order_summary.txt"))
    parser.add_argument("--no-full-records", action="store_true")
    parser.add_argument(
        "--ts",
        type=float,
        nargs="*",
        default=[1e-2, 3e-3, 1e-3, 3e-4, 1e-4, 3e-5, 1e-5],
    )
    args = parser.parse_args()
    result = run(args)
    args.out_json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_text(result, args.out_txt)
    print(args.out_txt.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
