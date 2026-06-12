#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from fixed_support_geom_lp import excess_values, max_abs_minor, solve_support_margin


def dense_pair(k: int, a: float) -> np.ndarray:
    s = 0
    foreign = list(range(1, k))
    if len(foreign) % 2:
        raise ValueError("dense_pair uses an even number of foreign coordinates")
    half = len(foreign) // 2
    v = np.zeros(k)
    for t in foreign[:half]:
        v[t] = 1.0
    for t in foreign[half:]:
        v[t] = -1.0
    rows = [np.eye(k)[i] for i in range(k)]
    rows.append(np.eye(k)[s] + a * v)
    rows.append(np.eye(k)[s] - a * v)
    return np.array(rows, dtype=float)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ks", type=int, nargs="+", default=[5, 7, 9])
    parser.add_argument("--amplitudes", type=float, nargs="+", default=[0.02, 0.05, 0.1, 0.2, 0.25])
    parser.add_argument("--C", type=float, default=0.0, help="constant for max target - C delta; C=0 maximizes target")
    parser.add_argument("--keep-solutions", action="store_true")
    parser.add_argument("--out-json", default="dense_pair_probe_results.json")
    parser.add_argument("--out-summary", default="dense_pair_probe_summary.txt")
    args = parser.parse_args()

    records = []
    for k in args.ks:
        for a in args.amplitudes:
            L = dense_pair(k, a)
            minor, arg = max_abs_minor(L, k)
            rec = {
                "k": k,
                "a": a,
                "n": int(len(L)),
                "max_abs_minor": minor,
                "max_minor_rows": list(arg) if arg is not None else None,
                "E_extra": excess_values(L, 0)[-2:].tolist(),
                "L": L.tolist(),
            }
            if minor <= 1.0 + 1e-8:
                lp = solve_support_margin(L, 0, args.C, keep_solution=args.keep_solutions)
                rec["lp"] = lp
            else:
                rec["skipped"] = "max-volume minor violation"
            records.append(rec)

    Path(args.out_json).write_text(json.dumps(records, indent=2, sort_keys=True))
    lines = []
    for rec in records:
        if "lp" not in rec:
            lines.append(
                f"SKIP dense k={rec['k']} a={rec['a']}: minor={rec['max_abs_minor']:.6g}"
            )
            continue
        best = rec["lp"]["best"]
        lines.append(
            f"dense k={rec['k']} a={rec['a']}: n={rec['n']} minor={rec['max_abs_minor']:.6g} "
            f"E={rec['E_extra']} target={best.get('target')} delta={best.get('delta')} "
            f"ratio={best.get('ratio')} margin_C{args.C:g}={best.get('margin')}"
        )
    summary = "\n".join(lines) + "\n"
    Path(args.out_summary).write_text(summary)
    print(summary, end="")


if __name__ == "__main__":
    main()
