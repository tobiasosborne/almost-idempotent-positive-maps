#!/usr/bin/env python3
"""LP metrics for the op-exposed-hull exploration.

Given a row-unital signed idempotent P, compute:

* row negative masses;
* row vertices of K=conv{p_i};
* exposedness modulus e_v(rho);
* W_{rho,kappa};
* row distances to conv W.

This script is exploratory evidence only.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np
from numpy.typing import NDArray
from scipy.optimize import linprog


Array = NDArray[np.float64]


@dataclass
class RowMetric:
    index: int
    is_vertex: bool
    exposedness: float | None
    in_w: bool
    distance_to_w: float | None


@dataclass
class Report:
    name: str
    n: int
    delta: float
    tau: float
    rho: float
    kappa: float
    idempotence_error: float
    unital_error: float
    vertex_indices: list[int]
    w_indices: list[int]
    max_distance_to_w: float | None
    rows: list[RowMetric]


def row_l1_norm(a: Array) -> float:
    return float(np.max(np.sum(np.abs(a), axis=1)))


def neg_mass(p: Array) -> float:
    return float(np.max(np.sum(np.maximum(-p, 0.0), axis=1)))


def hume_family(s: float) -> Array:
    v = np.array([1.0, -1.0 + s, -s])
    u = np.array([1.0 - s + s * s, -s, 0.0])
    return np.eye(3) - np.outer(u, v)


def random_unital_projection(n: int, rank: int, rng: np.random.Generator) -> Array:
    """Sample an idempotent P with P1=1.

    The range is spanned by 1 and rank-1 random vectors.  A random complement
    gives a projection onto that range.  This is not biased toward small
    negative mass, so callers should filter.
    """

    if not (1 <= rank <= n):
        raise ValueError("rank must be between 1 and n")
    basis = [np.ones(n)]
    while len(basis) < rank:
        x = rng.normal(size=n)
        for b in basis:
            x = x - (x @ b) / (b @ b) * b
        if np.linalg.norm(x) > 1e-8:
            basis.append(x)
    range_basis = np.column_stack(basis)

    comp_cols: list[Array] = []
    while len(comp_cols) < n - rank:
        x = rng.normal(size=n)
        for b in basis + comp_cols:
            x = x - (x @ b) / (b @ b) * b
        if np.linalg.norm(x) > 1e-8:
            comp_cols.append(x)

    if comp_cols:
        full = np.column_stack([range_basis, np.column_stack(comp_cols)])
    else:
        full = range_basis
    diag = np.diag([1.0] * rank + [0.0] * (n - rank))
    return full @ diag @ np.linalg.inv(full)


def distance_to_hull(point: Array, hull_points: Array) -> float:
    if len(hull_points) == 0:
        return math.inf
    m, n = hull_points.shape
    # variables: lambda_0..lambda_{m-1}, u_0..u_{n-1}
    c = np.concatenate([np.zeros(m), np.ones(n)])
    a_eq = [np.concatenate([np.ones(m), np.zeros(n)])]
    b_eq = [1.0]
    a_ub = []
    b_ub = []
    for k in range(n):
        coeff = hull_points[:, k]
        row = np.zeros(m + n)
        # point_k - coeff.lambda <= u_k
        row[:m] = -coeff
        row[m + k] = -1.0
        a_ub.append(row)
        b_ub.append(-point[k])

        row = np.zeros(m + n)
        # coeff.lambda - point_k <= u_k
        row[:m] = coeff
        row[m + k] = -1.0
        a_ub.append(row)
        b_ub.append(point[k])

    bounds = [(0.0, None)] * m + [(0.0, None)] * n
    res = linprog(
        c,
        A_ub=np.array(a_ub),
        b_ub=np.array(b_ub),
        A_eq=np.array(a_eq),
        b_eq=np.array(b_eq),
        bounds=bounds,
        method="highs",
    )
    if not res.success:
        return math.inf
    return float(res.fun)


def row_vertices(rows: Array, tol: float = 1e-9) -> list[int]:
    vertices: list[int] = []
    for i, p in enumerate(rows):
        others = np.delete(rows, i, axis=0)
        if len(others) == 0 or distance_to_hull(p, others) > tol:
            vertices.append(i)
    return vertices


def exposedness_modulus(rows: Array, vertex: int, rho: float) -> float:
    """Return e_v(rho).

    Variables are affine h(x)=a.x+b and t.  Since h is affine, constraints
    0<=h<=1 on row points imply 0<=h<=1 on K.
    """

    n = rows.shape[1]
    v = rows[vertex]
    outside = [
        i for i, p in enumerate(rows)
        if float(np.sum(np.abs(p - v))) >= rho and i != vertex
    ]
    if not outside:
        return 1.0

    # variables: a_0..a_{n-1}, b, t
    c = np.zeros(n + 2)
    c[-1] = -1.0

    a_eq = [np.concatenate([v, [1.0, 0.0]])]
    b_eq = [0.0]

    a_ub = []
    b_ub = []
    for p in rows:
        # h(p) <= 1
        a_ub.append(np.concatenate([p, [1.0, 0.0]]))
        b_ub.append(1.0)
        # -h(p) <= 0
        a_ub.append(np.concatenate([-p, [-1.0, 0.0]]))
        b_ub.append(0.0)
    for i in outside:
        # t <= h(p_i)
        p = rows[i]
        a_ub.append(np.concatenate([-p, [-1.0, 1.0]]))
        b_ub.append(0.0)

    bounds = [(None, None)] * (n + 1) + [(0.0, 1.0)]
    res = linprog(
        c,
        A_ub=np.array(a_ub),
        b_ub=np.array(b_ub),
        A_eq=np.array(a_eq),
        b_eq=np.array(b_eq),
        bounds=bounds,
        method="highs",
    )
    if not res.success:
        return float("nan")
    return float(-res.fun)


def evaluate(name: str, p: Array, rho_factor: float, kappa_factor: float) -> Report:
    delta = neg_mass(p)
    tau = math.sqrt(max(delta, 0.0))
    rho = rho_factor * tau
    kappa = kappa_factor * tau
    vertices = row_vertices(p)
    exposed: dict[int, float] = {}
    w_indices: list[int] = []
    for i in vertices:
        e = exposedness_modulus(p, i, rho)
        exposed[i] = e
        if e >= kappa:
            w_indices.append(i)

    w_rows = p[w_indices] if w_indices else np.empty((0, p.shape[1]))
    row_reports: list[RowMetric] = []
    distances: list[float] = []
    for i, row in enumerate(p):
        dist = distance_to_hull(row, w_rows) if w_indices else math.inf
        distances.append(dist)
        row_reports.append(RowMetric(
            index=i,
            is_vertex=i in vertices,
            exposedness=exposed.get(i),
            in_w=i in w_indices,
            distance_to_w=dist,
        ))

    max_dist = max(distances) if distances else None
    return Report(
        name=name,
        n=int(p.shape[0]),
        delta=delta,
        tau=tau,
        rho=rho,
        kappa=kappa,
        idempotence_error=row_l1_norm(p @ p - p),
        unital_error=float(np.max(np.abs(p @ np.ones(p.shape[0]) - 1.0))),
        vertex_indices=vertices,
        w_indices=w_indices,
        max_distance_to_w=max_dist,
        rows=row_reports,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--family", choices=["hume", "random"], default="hume")
    parser.add_argument("--s", type=float, default=0.05)
    parser.add_argument("--n", type=int, default=5)
    parser.add_argument("--rank", type=int, default=2)
    parser.add_argument("--samples", type=int, default=100)
    parser.add_argument("--seed", type=int, default=20260607)
    parser.add_argument("--max-delta", type=float, default=0.05)
    parser.add_argument("--rho-factor", type=float, default=8.0)
    parser.add_argument("--kappa-factor", type=float, default=0.125)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    if args.family == "hume":
        p = hume_family(args.s)
        name = f"hume_s={args.s:g}"
        report = evaluate(name, p, args.rho_factor, args.kappa_factor)
        payload = asdict(report)
    else:
        rng = np.random.default_rng(args.seed)
        reports: list[Report] = []
        for sample in range(args.samples):
            p = random_unital_projection(args.n, args.rank, rng)
            delta = neg_mass(p)
            if delta <= args.max_delta:
                reports.append(evaluate(
                    f"random_n={args.n}_r={args.rank}_sample={sample}",
                    p,
                    args.rho_factor,
                    args.kappa_factor,
                ))
        reports.sort(
            key=lambda r: -1.0 if r.max_distance_to_w is None or r.tau == 0 else r.max_distance_to_w / r.tau,
            reverse=True,
        )
        payload = {
            "family": "random",
            "n": args.n,
            "rank": args.rank,
            "samples": args.samples,
            "accepted": len(reports),
            "rho_factor": args.rho_factor,
            "kappa_factor": args.kappa_factor,
            "reports": [asdict(r) for r in reports[:20]],
        }

    text = json.dumps(payload, indent=2)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n", encoding="utf-8")
        print(f"wrote {args.out}")
    print(text)


if __name__ == "__main__":
    main()
