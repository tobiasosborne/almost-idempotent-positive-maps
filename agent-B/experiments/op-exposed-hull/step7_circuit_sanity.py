#!/usr/bin/env python3
"""Sanity checks for Step 7 circuit lower-bound formulations.

Agent B sandbox evidence only.  This script records small exact examples that
separate false "any affine circuit" statements from the vertex/minor versions
needed in the op-exposed-hull hard block.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parent


def max_negative_mass(rows: np.ndarray) -> float:
    return float(np.maximum(-rows, 0.0).sum(axis=1).max())


def l1(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.abs(a - b).sum())


def retraction_errors(p: np.ndarray) -> dict[str, float]:
    one = np.ones(p.shape[0])
    return {
        "row_sum_error": float(np.abs(p @ one - one).max()),
        "idempotence_error_linf": float(np.abs(p @ p - p).sum(axis=1).max()),
    }


def transient_segment_counterexample() -> dict:
    """A stochastic idempotent with a non-vertex separated affine circuit."""

    p = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.5, 0.5, 0.0],
        ]
    )
    circuit_residual = p[2] - 0.5 * p[0] - 0.5 * p[1]
    return {
        "name": "stochastic_segment_transient_row",
        "purpose": "Shows the raw affine-circuit lower bound is false unless the support is restricted to bad vertices or a Step-6 one-sided witness circuit.",
        "matrix": p.tolist(),
        "max_negative_mass": max_negative_mass(p),
        "errors": retraction_errors(p),
        "affine_circuit": "p_2 = 1/2 p_0 + 1/2 p_1",
        "circuit_residual_l1": float(np.abs(circuit_residual).sum()),
        "pairwise_distances": {
            "d01": l1(p[0], p[1]),
            "d02": l1(p[0], p[2]),
            "d12": l1(p[1], p[2]),
        },
        "nonvertex_warning": "p_2 is not a row vertex; in the real exposed-hull proof it is already in conv{p_0,p_1}.",
    }


def n4_hume_shape(t: float) -> dict:
    """The exact n=4 corank-one family from the small-case note."""

    v = np.array([1.0 - t * t, t * t, -1.0 + t * t, -t * t])
    u = np.array([1.0, 0.0, -(t * t) / (1.0 - t * t), 0.0])
    p = np.eye(4) - np.outer(u, v)
    residual = (1 - t * t) * p[0] + t * t * p[1] - (1 - t * t) * p[2] - t * t * p[3]
    dists = {
        f"d{i}{j}": l1(p[i], p[j])
        for i in range(4)
        for j in range(i + 1, 4)
    }
    return {
        "name": f"n4_corank_one_hume_shape_t_{t:g}",
        "purpose": "Shows how small circuit coefficients are accompanied by collapse of a vertex pair at the sqrt(delta) scale.",
        "max_negative_mass": max_negative_mass(p),
        "tau": t,
        "coefficients": {
            "a": 1.0 - t * t,
            "b": t * t,
            "c": 1.0 - t * t,
            "d": t * t,
        },
        "errors": retraction_errors(p),
        "circuit_residual_l1": float(np.abs(residual).sum()),
        "pairwise_distances": dists,
        "minimum_pairwise_distance_over_tau": min(dists.values()) / t,
    }


def script_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def main() -> None:
    payload = {
        "status": "Agent B sandbox; Step 7 sanity checks, not canonical.",
        "command": "python3 agent-B/experiments/op-exposed-hull/step7_circuit_sanity.py",
        "script_sha256": script_sha256(),
        "examples": [
            transient_segment_counterexample(),
            n4_hume_shape(0.1),
            n4_hume_shape(0.02),
        ],
    }
    out = ROOT / "step7_circuit_sanity.json"
    out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"wrote {out}")
    for example in payload["examples"]:
        print(f"{example['name']}: neg={example['max_negative_mass']:.6g}")


if __name__ == "__main__":
    main()
