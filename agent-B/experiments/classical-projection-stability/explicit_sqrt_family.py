#!/usr/bin/env python3
"""Explicit 3x3 family with distance comparable to sqrt(delta).

Let 0 < s < 1 and set

    v_s = (1, -1+s, -s),
    u_s = (1-s+s^2, -s, 0),
    P_s = I - u_s v_s^T.

Then v_s^T 1 = 0 and v_s^T u_s = 1, so P_s is a row-unital idempotent.
The only negative entry is (P_s)_{1,2} = -s^2, hence delta=s^2.

As s -> 0, P_s tends to the stochastic idempotent with rows
e_1, e_1, e_2.  For s>0, rows 0 and 1 are separated by l1 distance
2s + O(s^2), while both remain near the same edge.  Any stochastic
idempotent close to this boundary point must either keep row 1 near e_1
and then misses row 0 by order s, or identify rows 0 and 1 and move one
of them by at least half their separation.  The numerical distance
enumeration for n=3 confirms distance/sqrt(delta) -> 1.
"""

from __future__ import annotations

import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np
from numpy.typing import NDArray

from n3_rank2_search import best_distance_to_stochastic_idempotent, neg_mass, row_l1_norm


Array = NDArray[np.float64]


@dataclass
class Record:
    s: float
    delta: float
    distance: float
    ratio_linear: float
    ratio_sqrt: float
    nearest_type: str
    row01_l1: float
    idem_error: float
    p: list[list[float]]


def family(s: float) -> Array:
    v = np.array([1.0, -1.0 + s, -s])
    u = np.array([1.0 - s + s * s, -s, 0.0])
    return np.eye(3) - np.outer(u, v)


def main() -> None:
    out_dir = Path(__file__).resolve().parent
    s_values = [0.3, 0.2, 0.1, 0.07, 0.05, 0.03, 0.02, 0.01, 0.007, 0.005, 0.003, 0.001]
    records: list[Record] = []
    for s in s_values:
        p = family(s)
        delta = neg_mass(p)
        distance, typ = best_distance_to_stochastic_idempotent(p)
        rec = Record(
            s=s,
            delta=delta,
            distance=distance,
            ratio_linear=distance / delta,
            ratio_sqrt=distance / np.sqrt(delta),
            nearest_type=typ,
            row01_l1=float(np.sum(np.abs(p[0] - p[1]))),
            idem_error=row_l1_norm(p @ p - p),
            p=np.round(p, 14).tolist(),
        )
        records.append(rec)

    json_path = out_dir / "explicit_sqrt_family.json"
    csv_path = out_dir / "explicit_sqrt_family.csv"
    json_path.write_text(json.dumps([asdict(r) for r in records], indent=2), encoding="utf-8")
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "s",
                "delta",
                "distance",
                "ratio_linear",
                "ratio_sqrt",
                "nearest_type",
                "row01_l1",
                "idem_error",
            ],
        )
        writer.writeheader()
        for rec in records:
            writer.writerow({
                "s": rec.s,
                "delta": rec.delta,
                "distance": rec.distance,
                "ratio_linear": rec.ratio_linear,
                "ratio_sqrt": rec.ratio_sqrt,
                "nearest_type": rec.nearest_type,
                "row01_l1": rec.row01_l1,
                "idem_error": rec.idem_error,
            })

    print(f"wrote {json_path}")
    for rec in records:
        print(
            f"s={rec.s:.4g} delta={rec.delta:.4g} dist={rec.distance:.8g} "
            f"dist/sqrt(delta)={rec.ratio_sqrt:.8g} type={rec.nearest_type}"
        )


if __name__ == "__main__":
    main()
