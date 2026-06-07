#!/usr/bin/env python3
"""Small coordinate-negativity probes for the op-exposed-hull route.

This is sandbox evidence only.  It enumerates simplex representatives in
low-dimensional point clouds and computes the maximum negative mass of the
resulting barycentric coordinate vector on all points.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np
from numpy.typing import NDArray


Array = NDArray[np.float64]


@dataclass
class ProbeResult:
    name: str
    size: int
    best_reps: list[int]
    max_negative_mass: float
    worst_index: int
    worst_coeffs: list[float]


@dataclass
class Output:
    command: str
    script_sha256: str
    results: list[ProbeResult]


def barycentric_coeffs(point: Array, reps: Array) -> Array | None:
    dim = reps.shape[1]
    if reps.shape[0] != dim + 1:
        raise ValueError("need dim+1 representatives")
    matrix = np.vstack([reps.T, np.ones(dim + 1)])
    rhs = np.append(point, 1.0)
    try:
        return np.linalg.solve(matrix, rhs)
    except np.linalg.LinAlgError:
        return None


def negative_mass(coeffs: Array) -> float:
    return float(np.maximum(-coeffs, 0.0).sum())


def best_simplex_coordinate_negativity(points: Array) -> ProbeResult:
    points = intrinsic_affine_coordinates(points)
    n, dim = points.shape
    best: tuple[float, tuple[int, ...], int, Array] | None = None
    for reps_idx in itertools.combinations(range(n), dim + 1):
        reps = points[list(reps_idx)]
        worst = -1.0
        worst_index = -1
        worst_coeffs: Array | None = None
        feasible = True
        for i, point in enumerate(points):
            coeffs = barycentric_coeffs(point, reps)
            if coeffs is None:
                feasible = False
                break
            neg = negative_mass(coeffs)
            if neg > worst:
                worst = neg
                worst_index = i
                worst_coeffs = coeffs
        if not feasible or worst_coeffs is None:
            continue
        if best is None or worst < best[0]:
            best = (worst, reps_idx, worst_index, worst_coeffs)
    if best is None:
        raise RuntimeError("no nondegenerate simplex representatives")
    worst, reps_idx, worst_index, worst_coeffs = best
    return ProbeResult(
        name="",
        size=n,
        best_reps=list(reps_idx),
        max_negative_mass=worst,
        worst_index=worst_index,
        worst_coeffs=np.round(worst_coeffs, 12).tolist(),
    )


def intrinsic_affine_coordinates(points: Array, tol: float = 1e-10) -> Array:
    """Represent points in their affine hull using SVD coordinates."""

    base = points[0]
    centered = points - base
    _, singular_values, vh = np.linalg.svd(centered, full_matrices=False)
    rank = int(np.sum(singular_values > tol))
    if rank == 0:
        return np.zeros((points.shape[0], 0), dtype=float)
    basis = vh[:rank].T
    return centered @ basis


def regular_polygon(m: int) -> Array:
    theta = 2.0 * np.pi * np.arange(m) / m
    return np.column_stack([np.cos(theta), np.sin(theta)])


def thin_rectangle(eps: float) -> Array:
    return np.array(
        [
            [0.0, 0.0],
            [1.0, 0.0],
            [1.0, eps],
            [0.0, eps],
        ],
        dtype=float,
    )


def hume_rows(s: float) -> Array:
    v = np.array([1.0, -1.0 + s, -s])
    u = np.array([1.0 - s + s * s, -s, 0.0])
    return np.eye(3) - np.outer(u, v)


def script_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--out",
        type=Path,
        default=Path(__file__).with_name("robust_coordinate_probe.json"),
    )
    args = parser.parse_args()

    cases: list[tuple[str, Array]] = []
    for m in [5, 6, 8, 12, 24, 48]:
        cases.append((f"regular_polygon_{m}", regular_polygon(m)))
    for eps in [1.0, 0.1, 0.01, 0.001]:
        cases.append((f"thin_rectangle_eps_{eps:g}", thin_rectangle(eps)))
    for s in [0.2, 0.05, 0.01]:
        cases.append((f"hume_s_{s:g}", hume_rows(s)))

    results: list[ProbeResult] = []
    for name, points in cases:
        result = best_simplex_coordinate_negativity(points)
        result.name = name
        results.append(result)

    output = Output(
        command="python3 agent-B/experiments/op-exposed-hull/robust_coordinate_probe.py",
        script_sha256=script_hash(Path(__file__)),
        results=results,
    )
    args.out.write_text(json.dumps(asdict(output), indent=2), encoding="utf-8")
    print(f"wrote {args.out}")
    for result in results:
        print(
            f"{result.name}: max_neg={result.max_negative_mass:.12g} "
            f"best_reps={result.best_reps} worst={result.worst_index}"
        )


if __name__ == "__main__":
    main()
