#!/usr/bin/env python3
"""Explicit second-order rigidity jet at the n=3,k=2 pure-transient base."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.linalg import expm


def delta(P: np.ndarray) -> float:
    return float(np.max(np.sum(np.maximum(-P, 0.0), axis=1)))


def main() -> None:
    P0 = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 0.0, 0.0]])
    rows = []
    for a in [0.1, 0.5, 1.0, 2.0]:
        # Block C0 promotes pure transient state 2 at rate 1.  The pure
        # transient row simultaneously tries to move toward block C1 at rate a.
        A = np.array([[-1.0, 0.0, 1.0], [0.0, 0.0, 0.0], [-1.0 - a, a, 1.0]])
        I = np.eye(3)
        C = P0 @ A @ (I - P0)
        D = (I - P0) @ A @ P0
        Y = D - C
        B = 0.5 * (Y @ Y @ P0 + P0 @ Y @ Y - 2.0 * Y @ P0 @ Y)
        samples = []
        for t in [1e-2, 1e-3, 1e-4, 1e-5]:
            P = expm(t * Y) @ P0 @ expm(-t * Y)
            samples.append(
                {
                    "t": t,
                    "delta": delta(P),
                    "delta_over_t2": delta(P) / (t * t),
                    "row0_col1": float(P[0, 1]),
                    "idempotence_err": float(np.max(np.abs(P @ P - P))),
                    "row_sum_err": float(np.max(np.abs(P.sum(axis=1) - 1.0))),
                }
            )
        rows.append(
            {
                "a": a,
                "tangent_residual": float(np.max(np.abs(P0 @ A + A @ P0 - A))),
                "active_zero_min_A": float(np.min(A[P0 == 0.0])),
                "B_row0_col1": float(B[0, 1]),
                "expected_quadratic_delta_coeff": a,
                "samples": samples,
            }
        )

    summary = {
        "base": P0.tolist(),
        "description": "zero first-order active cost; second-order negative entry P[0,1] = -a t^2 + O(t^3)",
        "records": rows,
    }
    Path("second_order_rigidity_results.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    lines = [
        "w23_loj explicit second-order rigidity demo",
        json.dumps(summary, indent=2),
    ]
    Path("second_order_rigidity_summary.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
