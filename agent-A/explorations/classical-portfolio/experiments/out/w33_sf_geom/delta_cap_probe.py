#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from dense_pair_probe import dense_pair
from fixed_support_geom_lp import solve_support_margin


def main() -> None:
    records = []
    for cap in [0.02, 0.05, 0.1, 0.2, 0.25, 0.35]:
        for k in [5, 7, 9]:
            for a in [0.02, 0.05, 0.1, 0.2, 0.25]:
                L = dense_pair(k, a)
                rec = solve_support_margin(L, 0, 0.0, keep_solution=False, delta_cap=cap)
                best = rec["best"]
                records.append(
                    {
                        "family": "dense_pair",
                        "delta_cap": cap,
                        "k": k,
                        "a": a,
                        "target": best.get("target"),
                        "delta": best.get("delta"),
                        "ratio": best.get("ratio"),
                        "margin": best.get("margin"),
                    }
                )

    Path("delta_cap_probe_results.json").write_text(json.dumps(records, indent=2, sort_keys=True))
    lines = []
    for cap in sorted({r["delta_cap"] for r in records}):
        subset = [r for r in records if r["delta_cap"] == cap and r["target"] is not None]
        best = max(subset, key=lambda r: -1 if r["ratio"] is None else r["ratio"])
        lines.append(
            f"cap={cap}: best k={best['k']} a={best['a']} target={best['target']} "
            f"delta={best['delta']} ratio={best['ratio']}"
        )
    summary = "\n".join(lines) + "\n"
    Path("delta_cap_probe_summary.txt").write_text(summary)
    print(summary, end="")


if __name__ == "__main__":
    main()
