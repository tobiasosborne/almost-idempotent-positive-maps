"""LP utilities for Agent B's op-exposed-hull experiments.

All routines treat numerical output as evidence only.  The LPs are finite row
set computations for the definition in `definitions/def-exposed.md`.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable

import numpy as np
from scipy.optimize import linprog


LP_TOL = 1e-8


@dataclass
class LPValue:
    value: float
    success: bool
    status: int
    message: str


def negative_mass(row: np.ndarray) -> float:
    return float(np.maximum(-np.asarray(row, dtype=float), 0.0).sum())


def max_negative_mass(rows: np.ndarray) -> float:
    rows = np.asarray(rows, dtype=float)
    return float(max(negative_mass(row) for row in rows))


def retraction_errors(p: np.ndarray) -> dict[str, float]:
    p = np.asarray(p, dtype=float)
    idem = np.max(np.sum(np.abs(p @ p - p), axis=1))
    row_sum = np.max(np.abs(p.sum(axis=1) - 1.0))
    return {"idempotence_linf_l1": float(idem), "row_sum_linf": float(row_sum)}


def unique_row_indices(rows: np.ndarray, tol: float = 1e-9) -> list[int]:
    rows = np.asarray(rows, dtype=float)
    keep: list[int] = []
    for idx, row in enumerate(rows):
        if not any(np.linalg.norm(row - rows[j], ord=1) <= tol for j in keep):
            keep.append(idx)
    return keep


def l1_distance_to_conv(point: np.ndarray, hull_points: np.ndarray) -> LPValue:
    point = np.asarray(point, dtype=float)
    hull_points = np.asarray(hull_points, dtype=float)
    if hull_points.size == 0:
        return LPValue(math.inf, False, -1, "empty hull")
    if hull_points.ndim == 1:
        hull_points = hull_points.reshape(1, -1)

    m, d = hull_points.shape
    c = np.r_[np.zeros(m), np.ones(d)]

    a_eq = np.zeros((1, m + d))
    a_eq[0, :m] = 1.0
    b_eq = np.array([1.0])

    a_ub = []
    b_ub = []
    for k in range(d):
        row = np.zeros(m + d)
        row[:m] = hull_points[:, k]
        row[m + k] = -1.0
        a_ub.append(row)
        b_ub.append(point[k])

        row = np.zeros(m + d)
        row[:m] = -hull_points[:, k]
        row[m + k] = -1.0
        a_ub.append(row)
        b_ub.append(-point[k])

    bounds = [(0.0, None)] * m + [(0.0, None)] * d
    res = linprog(
        c,
        A_ub=np.asarray(a_ub),
        b_ub=np.asarray(b_ub),
        A_eq=a_eq,
        b_eq=b_eq,
        bounds=bounds,
        method="highs",
    )
    value = float(res.fun) if res.success else math.inf
    return LPValue(value, bool(res.success), int(res.status), str(res.message))


def vertex_indices(rows: np.ndarray, tol: float = LP_TOL) -> list[int]:
    rows = np.asarray(rows, dtype=float)
    unique = unique_row_indices(rows, tol=tol)
    if len(unique) <= 1:
        return unique
    vertices: list[int] = []
    for idx in unique:
        others = rows[[j for j in unique if j != idx]]
        dist = l1_distance_to_conv(rows[idx], others)
        if (not dist.success) or dist.value > tol:
            vertices.append(idx)
    return vertices


def exposedness_modulus(rows: np.ndarray, vertex_idx: int, rho: float) -> LPValue:
    rows = np.asarray(rows, dtype=float)
    v = rows[vertex_idx]
    outside = [i for i, row in enumerate(rows) if np.linalg.norm(row - v, ord=1) >= rho]
    if not outside:
        return LPValue(1.0, True, 0, "outside row set empty")

    n_rows, d = rows.shape
    # Variables are affine coefficients a in R^d, offset b, and gap t.
    c = np.r_[np.zeros(d + 1), -1.0]

    a_eq = np.zeros((1, d + 2))
    a_eq[0, :d] = v
    a_eq[0, d] = 1.0
    b_eq = np.array([0.0])

    a_ub = []
    b_ub = []
    for row_point in rows:
        upper = np.zeros(d + 2)
        upper[:d] = row_point
        upper[d] = 1.0
        a_ub.append(upper)
        b_ub.append(1.0)

        lower = np.zeros(d + 2)
        lower[:d] = -row_point
        lower[d] = -1.0
        a_ub.append(lower)
        b_ub.append(0.0)

    for idx in outside:
        sep = np.zeros(d + 2)
        sep[:d] = -rows[idx]
        sep[d] = -1.0
        sep[d + 1] = 1.0
        a_ub.append(sep)
        b_ub.append(0.0)

    bounds = [(None, None)] * (d + 1) + [(0.0, 1.0)]
    res = linprog(
        c,
        A_ub=np.asarray(a_ub),
        b_ub=np.asarray(b_ub),
        A_eq=a_eq,
        b_eq=b_eq,
        bounds=bounds,
        method="highs",
    )
    value = float(-res.fun) if res.success else math.nan
    return LPValue(value, bool(res.success), int(res.status), str(res.message))


def exposed_hull_report(
    rows: np.ndarray,
    rho_mult: float,
    kappa_mult: float,
    vertex_tol: float = LP_TOL,
) -> dict:
    rows = np.asarray(rows, dtype=float)
    delta = max_negative_mass(rows)
    tau = math.sqrt(max(delta, 0.0))
    rho = float(rho_mult * tau)
    kappa = float(kappa_mult * tau)
    verts = vertex_indices(rows, tol=vertex_tol)

    exposed = {}
    w_indices: list[int] = []
    for idx in verts:
        val = exposedness_modulus(rows, idx, rho)
        exposed[str(idx)] = {
            "value": val.value,
            "success": val.success,
            "status": val.status,
            "message": val.message,
        }
        if val.success and val.value + 1e-9 >= kappa:
            w_indices.append(idx)

    hull = rows[w_indices] if w_indices else np.empty((0, rows.shape[1]))
    distances = []
    for row in rows:
        dist = l1_distance_to_conv(row, hull)
        distances.append(
            {
                "value": dist.value,
                "success": dist.success,
                "status": dist.status,
                "message": dist.message,
            }
        )

    finite_distances = [d["value"] for d in distances if math.isfinite(d["value"])]
    max_dist = max(finite_distances) if finite_distances else math.inf
    ratio = max_dist / tau if tau > 0.0 and math.isfinite(max_dist) else math.inf
    if tau == 0.0 and math.isfinite(max_dist):
        ratio = 0.0 if max_dist <= vertex_tol else math.inf

    return {
        "n": int(rows.shape[0]),
        "dimension": int(rows.shape[1]),
        "delta": delta,
        "tau": tau,
        "rho_mult": float(rho_mult),
        "kappa_mult": float(kappa_mult),
        "rho": rho,
        "kappa": kappa,
        "vertices": verts,
        "exposedness": exposed,
        "W_indices": w_indices,
        "row_distances_to_conv_W": distances,
        "max_distance_to_conv_W": max_dist,
        "max_distance_ratio": ratio,
        "errors": retraction_errors(rows),
    }


def scan_grid(
    rows: np.ndarray,
    rho_mults: Iterable[float],
    kappa_mults: Iterable[float],
) -> list[dict]:
    return [
        exposed_hull_report(rows, rho_mult, kappa_mult)
        for rho_mult in rho_mults
        for kappa_mult in kappa_mults
    ]
