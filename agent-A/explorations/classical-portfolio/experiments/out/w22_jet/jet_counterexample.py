#!/usr/bin/env python3
"""Exact boundary H-M support-addition checks for w22_jet.

The rank-one family is the exact w18 chart at
P0 = [[1, 0], [1, 0]].  The chart coordinate is C=c, D=0, and
P(c) has both rows equal to (1-c, c).
"""

from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass

import numpy as np


def delta(P: np.ndarray) -> float:
    """Max row negative mass."""

    return float(np.max(np.sum(np.maximum(-P, 0.0), axis=1)))


def row_stoch_err(P: np.ndarray) -> float:
    return float(np.max(np.abs(P.sum(axis=1) - 1.0)))


def idem_err(P: np.ndarray) -> float:
    return float(np.max(np.abs(P @ P - P)))


def rank1_chart(c: float) -> np.ndarray:
    row = np.array([1.0 - c, c], dtype=float)
    return np.vstack([row, row])


def rank2_support_addition(eps: float) -> np.ndarray:
    return np.array(
        [
            [1.0 - eps, 0.0, eps],
            [0.0, 1.0, 0.0],
            [1.0 - eps, 0.0, eps],
        ],
        dtype=float,
    )


@dataclass
class Record:
    family: str
    parameter: float
    delta: float
    normal_norm_sq: float
    ratio: str
    idempotence_err: float
    row_stoch_err: float
    H_reference: float
    H_over_delta: str


def ratio_string(num: float, den: float) -> str:
    if den == 0.0:
        if num == 0.0:
            return "0/0"
        return "inf"
    return f"{num / den:.17g}"


def rank1_records() -> list[Record]:
    records: list[Record] = []
    for c in [
        -1e-1,
        -3e-2,
        -1e-2,
        -1e-3,
        -1e-4,
        0.0,
        1e-8,
        1e-6,
        1e-4,
        1e-3,
        1e-2,
    ]:
        P = rank1_chart(c)
        d = delta(P)
        normal_sq = c * c
        # All rows coincide, so the row set has zero height against its own
        # visible/reference hull.  For c >= 0 this is also a nonnegative H-M
        # point, hence the genuine H-M height is zero.
        H = 0.0
        records.append(
            Record(
                family="rank1_exact_chart",
                parameter=c,
                delta=d,
                normal_norm_sq=normal_sq,
                ratio=ratio_string(normal_sq, d),
                idempotence_err=idem_err(P),
                row_stoch_err=row_stoch_err(P),
                H_reference=H,
                H_over_delta=ratio_string(H, d),
            )
        )
    return records


def rank2_records() -> list[Record]:
    records: list[Record] = []
    for eps in [1e-8, 1e-6, 1e-4, 1e-3, 1e-2]:
        P = rank2_support_addition(eps)
        d = delta(P)
        # Relative to the fixed boundary profile
        # C1={1}, C2={2}, T={3}, alpha_3=e_1, the stratum is stationary in
        # the recurrent column 3 direction.  The displayed family has first
        # variation in rows 1 and 3, columns 1 and 3, with Frobenius square
        # 4 eps^2; any chart norm gives an equivalent positive normal square.
        normal_sq = 4.0 * eps * eps
        H = 0.0
        records.append(
            Record(
                family="rank2_support_addition",
                parameter=eps,
                delta=d,
                normal_norm_sq=normal_sq,
                ratio=ratio_string(normal_sq, d),
                idempotence_err=idem_err(P),
                row_stoch_err=row_stoch_err(P),
                H_reference=H,
                H_over_delta=ratio_string(H, d),
            )
        )
    return records


def main() -> None:
    records = rank1_records() + rank2_records()
    finite = [
        float(r.ratio)
        for r in records
        if r.ratio not in {"inf", "0/0"} and math.isfinite(float(r.ratio))
    ]
    inf_records = [r for r in records if r.ratio == "inf"]
    summary = {
        "records": len(records),
        "infinite_J1_ratios": len(inf_records),
        "max_finite_normal_sq_over_delta": max(finite) if finite else None,
        "max_idempotence_err": max(r.idempotence_err for r in records),
        "max_row_stoch_err": max(r.row_stoch_err for r in records),
        "max_H_over_delta_finite": 0.0,
    }

    with open("jet_counterexample_results.json", "w", encoding="utf-8") as f:
        json.dump(
            {"summary": summary, "records": [asdict(r) for r in records]},
            f,
            indent=2,
        )

    lines = [
        "w22_jet exact-chart/support-addition numerics",
        json.dumps(summary, indent=2),
        "",
        "family parameter delta normal_norm_sq normal_sq/delta H/delta idem_err",
    ]
    for r in records:
        lines.append(
            f"{r.family} {r.parameter:.17g} {r.delta:.17g} "
            f"{r.normal_norm_sq:.17g} {r.ratio} {r.H_over_delta} "
            f"{r.idempotence_err:.3g}"
        )
    with open("numerics_summary.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
