#!/usr/bin/env python3
"""n=4 corank-one 2|2 circuit certificates for op-exposed-hull.

Agent B sandbox evidence only.  The script records the exact coefficient
certificates used in `subagent-op-exposed-hull-n4-circuit.md`.
"""

from __future__ import annotations

import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def exposure_values(a: Fraction, b: Fraction, c: Fraction, d: Fraction) -> dict[str, list[str]]:
    """Affine values on vertices 0,1,2,3 certifying exposedness.

    The normalized circuit is

        a x0 + b x1 = c x2 + d x3,       a+b=c+d=1.

    A value vector is affine iff it satisfies the same scalar relation.
    """
    return {
        "vertex_0": ["0", "1", fstr(b), fstr(b)],
        "vertex_1": ["1", "0", fstr(a), fstr(a)],
        "vertex_2": [fstr(d), fstr(d), "0", "1"],
        "vertex_3": [fstr(c), fstr(c), "1", "0"],
    }


def exposure_lower_bounds(a: Fraction, b: Fraction, c: Fraction, d: Fraction) -> dict[str, str]:
    return {
        "vertex_0": fstr(b),
        "vertex_1": fstr(a),
        "vertex_2": fstr(d),
        "vertex_3": fstr(c),
    }


def collapse_bounds(
    a: Fraction, b: Fraction, c: Fraction, d: Fraction, diameter_bound: Fraction
) -> dict[str, str]:
    """Bounds for distance of a low-exposed vertex to the opposite edge."""
    return {
        "vertex_0_to_conv_23_if_b_small": fstr(diameter_bound * b / a),
        "vertex_1_to_conv_23_if_a_small": fstr(diameter_bound * a / b),
        "vertex_2_to_conv_01_if_d_small": fstr(diameter_bound * d / c),
        "vertex_3_to_conv_01_if_c_small": fstr(diameter_bound * c / d),
    }


def classify(
    name: str,
    coeffs: tuple[Fraction, Fraction, Fraction, Fraction],
    delta: Fraction,
    kappa_multiplier: Fraction = Fraction(1, 8),
) -> dict:
    a, b, c, d = coeffs
    if a + b != 1 or c + d != 1:
        raise ValueError("coefficients must be normalized")
    tau = math.sqrt(float(delta))
    kappa = float(kappa_multiplier) * tau
    diameter_bound = Fraction(2) + 4 * delta
    lower = {
        key: float(value)
        for key, value in {
            "vertex_0": b,
            "vertex_1": a,
            "vertex_2": d,
            "vertex_3": c,
        }.items()
    }
    exposed = {key: value >= kappa for key, value in lower.items()}
    verdict = "all_four_exposed" if all(exposed.values()) else "collapse_branch"
    return {
        "name": name,
        "coefficients": {"a": fstr(a), "b": fstr(b), "c": fstr(c), "d": fstr(d)},
        "delta": fstr(delta),
        "tau_float": tau,
        "kappa_multiplier": fstr(kappa_multiplier),
        "kappa_float": kappa,
        "diameter_bound": fstr(diameter_bound),
        "exposure_values": exposure_values(a, b, c, d),
        "exposure_lower_bounds": exposure_lower_bounds(a, b, c, d),
        "exposed_at_kappa": exposed,
        "collapse_bounds": collapse_bounds(a, b, c, d, diameter_bound),
        "verdict": verdict,
    }


def script_sha256() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def main() -> None:
    cases = [
        classify(
            "balanced_all_exposed_delta_1e-4",
            (Fraction(2, 5), Fraction(3, 5), Fraction(1, 3), Fraction(2, 3)),
            Fraction(1, 10000),
        ),
        classify(
            "small_mate_coefficient_hume_shape_t_1_10",
            (
                Fraction(99, 100),
                Fraction(1, 100),
                Fraction(99, 100),
                Fraction(1, 100),
            ),
            Fraction(1, 100),
        ),
        classify(
            "two_small_cross_coefficients_delta_1e-4",
            (
                Fraction(999, 1000),
                Fraction(1, 1000),
                Fraction(1, 1000),
                Fraction(999, 1000),
            ),
            Fraction(1, 10000),
        ),
    ]
    payload = {
        "status": "Agent B sandbox; coefficient-level proof aid, not canonical.",
        "command": "python3 agent-B/experiments/op-exposed-hull/n4_circuit_analysis.py",
        "script_sha256": script_sha256(),
        "normalization": "a,b,c,d>0, a+b=c+d=1, a x0+b x1=c x2+d x3",
        "cases": cases,
    }
    out = ROOT / "n4_circuit_analysis.json"
    out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"wrote {out}")
    for case in cases:
        print(f"{case['name']}: {case['verdict']}")


if __name__ == "__main__":
    main()
