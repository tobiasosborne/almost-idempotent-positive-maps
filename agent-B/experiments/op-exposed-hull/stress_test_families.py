#!/usr/bin/env python3
"""Stress tests for the op-exposed-hull classical route.

This is Agent B sandbox code.  It numerically evaluates finite row polytopes
coming from exact signed affine retractions where possible, and records why
nearby tempting families fail the exact-idempotent constraint.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.linalg import block_diag
from scipy.optimize import linprog


TOL = 1e-8


def neg_mass(row: np.ndarray) -> float:
    return float(np.maximum(-row, 0.0).sum())


def inf_row_norm(matrix: np.ndarray) -> float:
    return float(np.abs(matrix).sum(axis=1).max())


def hume_matrix(s: float) -> np.ndarray:
    v = np.array([1.0, -1.0 + s, -s])
    u = np.array([1.0 - s + s * s, -s, 0.0])
    return np.eye(3) - np.outer(u, v)


def kron_power(matrix: np.ndarray, power: int) -> np.ndarray:
    out = np.array([[1.0]])
    for _ in range(power):
        out = np.kron(out, matrix)
    return out


def block_hume(s: float, copies: int) -> np.ndarray:
    return block_diag(*[hume_matrix(s) for _ in range(copies)])


def polygon_projection(m: int) -> np.ndarray:
    idx = np.arange(m)
    theta = 2.0 * math.pi / m
    rows = []
    for i in idx:
        rows.append((1.0 + 2.0 * np.cos(theta * (i - idx))) / m)
    return np.array(rows)


def polygon_local_stencil(m: int) -> np.ndarray:
    theta = 2.0 * math.pi / m
    a = 1.0 / (2.0 * math.cos(theta))
    center_weight = 1.0 - 1.0 / math.cos(theta)
    p = np.full((m, m), center_weight / m)
    for i in range(m):
        p[i, (i - 1) % m] += a
        p[i, (i + 1) % m] += a
    return p


def hypercube_affine_projection(dim: int) -> np.ndarray:
    verts = np.array(
        [
            [1.0 if (mask >> j) & 1 else -1.0 for j in range(dim)]
            for mask in range(2**dim)
        ]
    )
    rows = []
    for t in verts:
        rows.append((1.0 + verts @ t) / (2**dim))
    return np.array(rows)


def stochastic_idempotent_from_classes(
    n: int, classes: list[list[int]], rng: np.random.Generator
) -> np.ndarray:
    recurrent = []
    for cls in classes:
        row = np.zeros(n)
        row[cls] = 1.0 / len(cls)
        recurrent.append(row)

    p = np.zeros((n, n))
    class_by_index = {i: a for a, cls in enumerate(classes) for i in cls}
    for i in range(n):
        if i in class_by_index:
            p[i] = recurrent[class_by_index[i]]
        else:
            weights = rng.dirichlet(np.ones(len(classes)))
            p[i] = sum(weights[a] * recurrent[a] for a in range(len(classes)))
    return p


def random_similarity_projection(n: int, rank: int, eps: float, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    class_size = 2
    classes = [
        list(range(a * class_size, min((a + 1) * class_size, n)))
        for a in range(rank)
    ]
    used = {i for cls in classes for i in cls}
    classes = [cls for cls in classes if cls]
    e = stochastic_idempotent_from_classes(n, classes, rng)

    a = rng.normal(size=(n, n))
    a = a - a.sum(axis=1, keepdims=True) / n
    s = np.eye(n) + eps * a
    # Retry deterministically with smaller eps if the random perturbation is
    # poorly conditioned.
    while np.linalg.cond(s) > 1e4:
        eps *= 0.5
        s = np.eye(n) + eps * a
    p = np.linalg.solve(s, e @ s)
    assert len(used) <= n
    return p


def solve_feasible(a_eq: np.ndarray, b_eq: np.ndarray, nvar: int) -> bool:
    res = linprog(
        np.zeros(nvar),
        A_eq=a_eq,
        b_eq=b_eq,
        bounds=[(0.0, None)] * nvar,
        method="highs",
    )
    return bool(res.success)


def vertex_indices(points: np.ndarray) -> list[int]:
    n, d = points.shape
    vertices: list[int] = []
    for i in range(n):
        others = [j for j in range(n) if j != i]
        if not others:
            vertices.append(i)
            continue
        a_eq = np.vstack([points[others].T, np.ones(len(others))])
        b_eq = np.concatenate([points[i], [1.0]])
        if not solve_feasible(a_eq, b_eq, len(others)):
            vertices.append(i)
    return vertices


def exposedness(points: np.ndarray, vertex: int, rho: float) -> float:
    n, d = points.shape
    v = points[vertex]
    outside = [i for i in range(n) if np.linalg.norm(points[i] - v, ord=1) >= rho - 1e-10]
    if not outside:
        return 1.0

    # Variables are a_0,...,a_{d-1}, b, t.  h(x)=a.x+b.
    nvar = d + 2
    b_index = d
    t_index = d + 1
    c = np.zeros(nvar)
    c[t_index] = -1.0
    a_ub = []
    b_ub = []

    for x in points:
        row = np.zeros(nvar)
        row[:d] = x
        row[b_index] = 1.0
        a_ub.append(row)
        b_ub.append(1.0)

        row = np.zeros(nvar)
        row[:d] = -x
        row[b_index] = -1.0
        a_ub.append(row)
        b_ub.append(0.0)

    for i in outside:
        row = np.zeros(nvar)
        row[:d] = -points[i]
        row[b_index] = -1.0
        row[t_index] = 1.0
        a_ub.append(row)
        b_ub.append(0.0)

    a_eq = np.zeros((1, nvar))
    a_eq[0, :d] = v
    a_eq[0, b_index] = 1.0
    b_eq = np.array([0.0])

    bounds = [(None, None)] * d + [(None, None), (0.0, 1.0)]
    res = linprog(
        c,
        A_ub=np.array(a_ub),
        b_ub=np.array(b_ub),
        A_eq=a_eq,
        b_eq=b_eq,
        bounds=bounds,
        method="highs",
    )
    if not res.success:
        return float("nan")
    return float(max(0.0, min(1.0, res.x[t_index])))


def l1_dist_to_hull(point: np.ndarray, hull_points: np.ndarray) -> float:
    if len(hull_points) == 0:
        return float("inf")
    m, d = hull_points.shape
    # Variables lambda_0..lambda_{m-1}, z_0..z_{d-1}.
    nvar = m + d
    c = np.concatenate([np.zeros(m), np.ones(d)])
    a_ub = []
    b_ub = []
    for coord in range(d):
        row = np.zeros(nvar)
        row[:m] = -hull_points[:, coord]
        row[m + coord] = -1.0
        a_ub.append(row)
        b_ub.append(-point[coord])

        row = np.zeros(nvar)
        row[:m] = hull_points[:, coord]
        row[m + coord] = -1.0
        a_ub.append(row)
        b_ub.append(point[coord])

    a_eq = np.zeros((1, nvar))
    a_eq[0, :m] = 1.0
    b_eq = np.array([1.0])
    bounds = [(0.0, None)] * nvar
    res = linprog(
        c,
        A_ub=np.array(a_ub),
        b_ub=np.array(b_ub),
        A_eq=a_eq,
        b_eq=b_eq,
        bounds=bounds,
        method="highs",
    )
    if not res.success:
        return float("nan")
    return float(res.fun)


@dataclass
class FamilyCase:
    name: str
    matrix: np.ndarray
    exact_retraction: bool
    comment: str


def summarize_case(case: FamilyCase, rho_factor: float, kappa_factor: float) -> dict:
    p = case.matrix
    delta = max(neg_mass(row) for row in p)
    tau = math.sqrt(max(delta, 0.0))
    rho = rho_factor * tau
    kappa = kappa_factor * tau
    vertices = vertex_indices(p)
    e_values = {i: exposedness(p, i, rho) for i in vertices}
    well = [i for i, e in e_values.items() if e >= kappa - 1e-9]
    hull = p[well]
    distances = [l1_dist_to_hull(row, hull) for row in p]
    finite_distances = [x for x in distances if math.isfinite(x)]
    max_dist = max(finite_distances) if finite_distances else float("inf")
    return {
        "name": case.name,
        "n": int(p.shape[0]),
        "exact_retraction_declared": case.exact_retraction,
        "row_sum_error": float(np.max(np.abs(p.sum(axis=1) - 1.0))),
        "idempotency_error_inf_row": inf_row_norm(p @ p - p),
        "delta": delta,
        "tau": tau,
        "rho_factor": rho_factor,
        "kappa_factor": kappa_factor,
        "rho": rho,
        "kappa": kappa,
        "num_vertices": len(vertices),
        "num_well_exposed_vertices": len(well),
        "min_e_over_vertices": min(e_values.values()) if e_values else None,
        "median_e_over_vertices": float(np.median(list(e_values.values()))) if e_values else None,
        "max_dist_to_well_hull": max_dist,
        "max_dist_over_tau": max_dist / tau if tau > 0 and math.isfinite(max_dist) else None,
        "min_e_over_tau": min(e_values.values()) / tau if tau > 0 and e_values else None,
        "well_vertex_indices": well[:20],
        "comment": case.comment,
    }


def main() -> None:
    root = Path(__file__).resolve().parent
    script_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

    cases: list[FamilyCase] = []
    for s in [0.02, 0.05, 0.1]:
        cases.append(
            FamilyCase(
                f"hume_s={s}",
                hume_matrix(s),
                True,
                "Hume sharp rank-one family; expected sqrt-scale only.",
            )
        )
    for power, s in [(2, 0.02), (2, 0.05), (3, 0.02)]:
        cases.append(
            FamilyCase(
                f"hume_tensor_power={power}_s={s}",
                kron_power(hume_matrix(s), power),
                True,
                "Kronecker product of exact Hume retractions.",
            )
        )
    for copies, s in [(3, 0.05), (6, 0.05)]:
        cases.append(
            FamilyCase(
                f"hume_direct_sum_copies={copies}_s={s}",
                block_hume(s, copies),
                True,
                "Block direct sum of independent Hume escapes.",
            )
        )
    for m in [7, 11, 21, 41]:
        cases.append(
            FamilyCase(
                f"regular_polygon_exact_projection_m={m}",
                polygon_projection(m),
                True,
                "Exact affine projection onto constants and first Fourier modes.",
            )
        )
    for m in [11, 21, 41]:
        cases.append(
            FamilyCase(
                f"regular_polygon_local_stencil_m={m}",
                polygon_local_stencil(m),
                False,
                "Small-negative local neighbor stencil; reconstructs polygon vertices but is not idempotent.",
            )
        )
    for dim in [2, 3, 4, 5]:
        cases.append(
            FamilyCase(
                f"hypercube_affine_projection_dim={dim}",
                hypercube_affine_projection(dim),
                True,
                "Exact affine projection for cube vertices using first-order Fourier coordinates.",
            )
        )
    for n, rank, eps, first_seed, count in [
        (8, 3, 0.005, 200, 5),
        (8, 3, 0.02, 210, 5),
        (12, 4, 0.02, 220, 5),
        (12, 4, 0.05, 230, 5),
    ]:
        for seed in range(first_seed, first_seed + count):
            cases.append(
                FamilyCase(
                    f"random_similarity_n={n}_rank={rank}_eps={eps}_seed={seed}",
                    random_similarity_projection(n, rank, eps, seed),
                    True,
                    "Exact similarity of a stochastic idempotent by S1=1; signed but already near a stochastic idempotent.",
                )
            )

    rows: list[dict] = []
    for rho_factor, kappa_factor in [(2.0, 0.25), (4.0, 0.10), (8.0, 0.05)]:
        for case in cases:
            rows.append(summarize_case(case, rho_factor, kappa_factor))

    json_path = root / "stress_test_families.json"
    csv_path = root / "stress_test_families.csv"
    payload = {
        "script": str(Path(__file__).relative_to(root.parents[2])),
        "script_sha256": script_hash,
        "rho_kappa_grid": [
            {"rho_factor": 2.0, "kappa_factor": 0.25},
            {"rho_factor": 4.0, "kappa_factor": 0.10},
            {"rho_factor": 8.0, "kappa_factor": 0.05},
        ],
        "rows": rows,
    }
    json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")

    fieldnames = list(rows[0].keys())
    with csv_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {json_path}")
    print(f"wrote {csv_path}")
    print(f"script_sha256 {script_hash}")
    for row in rows:
        if row["rho_factor"] == 4.0 and row["kappa_factor"] == 0.10:
            print(
                row["name"],
                "delta=",
                f"{row['delta']:.6g}",
                "tau=",
                f"{row['tau']:.6g}",
                "verts=",
                row["num_vertices"],
                "well=",
                row["num_well_exposed_vertices"],
                "maxdist/tau=",
                row["max_dist_over_tau"],
                "idem_err=",
                f"{row['idempotency_error_inf_row']:.6g}",
            )


if __name__ == "__main__":
    main()
