#!/usr/bin/env python3
"""Leading-order optimizer for the R^3 absorbing/transient model.

P0 has two absorbing states and one transient row [w, 1-w, 0].
For T_a = P0 + a K with K = S - P0 and S row-stochastic,

  eta = a ||P0 K + K P0 - K||_{inf->inf} + O(a^2).

For range vectors with sup norm <= 1, the leading null-ideal defect is

  a * 16 w^2(1-w)^2 * ||P'_0 e_3||_inf + O(a^2),

where P'_0 is the derivative of the spectral projection. In this model
P'_0 e_3 = P0 S e_3 = (S_13, S_23, w S_13 + (1-w) S_23).

This script maximizes the ratio of these two leading coefficients over
row-stochastic S and w in (0,1).
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
from scipy import optimize


def p0_matrix(w: float) -> np.ndarray:
    return np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [w, 1.0 - w, 0.0]])


def rows_from_unit_cube(x: np.ndarray) -> np.ndarray:
    rows = []
    for i in range(0, 6, 2):
        first = x[i]
        second_frac = x[i + 1]
        rows.append([first, (1.0 - first) * second_frac, (1.0 - first) * (1.0 - second_frac)])
    return np.array(rows, dtype=float)


def leading_ratio(w: float, s_mat: np.ndarray) -> tuple[float, float, float]:
    p0 = p0_matrix(w)
    k_mat = s_mat - p0
    d_mat = p0 @ k_mat + k_mat @ p0 - k_mat
    eta_coeff = float(np.max(np.sum(np.abs(d_mat), axis=1)))
    q_col = np.array(
        [s_mat[0, 2], s_mat[1, 2], w * s_mat[0, 2] + (1.0 - w) * s_mat[1, 2]]
    )
    defect_coeff = 16.0 * w * w * (1.0 - w) * (1.0 - w) * float(np.max(np.abs(q_col)))
    if eta_coeff <= 1e-14:
        return 0.0, defect_coeff, eta_coeff
    return defect_coeff / eta_coeff, defect_coeff, eta_coeff


def objective(z: np.ndarray) -> float:
    w = z[0]
    s_mat = rows_from_unit_cube(z[1:])
    ratio, _, _ = leading_ratio(w, s_mat)
    return -ratio


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20260604)
    parser.add_argument("--random-samples", type=int, default=200000)
    parser.add_argument("--de-iters", type=int, default=600)
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parent / "leading_r3_opt.json")
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    best_z = None
    best_ratio = -1.0
    for _ in range(args.random_samples):
        z = rng.random(7)
        z[0] = 0.001 + 0.998 * z[0]
        ratio = -objective(z)
        if ratio > best_ratio:
            best_ratio = ratio
            best_z = z

    result = optimize.differential_evolution(
        objective,
        bounds=[(1e-5, 1.0 - 1e-5)] + [(0.0, 1.0)] * 6,
        maxiter=args.de_iters,
        popsize=20,
        polish=True,
        tol=1e-10,
        seed=args.seed,
        updating="immediate",
        workers=1,
        x0=best_z,
    )
    z = np.array(result.x, dtype=float)
    w = float(z[0])
    s_mat = rows_from_unit_cube(z[1:])
    ratio, defect_coeff, eta_coeff = leading_ratio(w, s_mat)
    payload = {
        "seed": args.seed,
        "random_samples": args.random_samples,
        "de_iters": args.de_iters,
        "w": w,
        "S": np.round(s_mat, 15).tolist(),
        "leading_ratio": ratio,
        "defect_coeff": defect_coeff,
        "eta_coeff": eta_coeff,
        "optimizer_fun": float(result.fun),
        "optimizer_success": bool(result.success),
        "optimizer_message": str(result.message),
    }
    args.out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"out: {args.out}")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
