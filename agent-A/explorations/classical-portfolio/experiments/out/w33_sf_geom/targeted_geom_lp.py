#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from fixed_support_geom_lp import (
    all_transverse_pairs,
    cycle_support,
    max_abs_minor,
    signed_pair_support,
    solve_support_margin,
)


def main() -> None:
    cases = []
    for a in [0.02, 0.05, 0.1, 0.2, 0.35, 0.5]:
        cases.append((f"pair_k3_a{a:g}", signed_pair_support(3, a)))
    for a in [0.05, 0.2, 0.35, 0.5]:
        cases.append((f"cycle_k4_a{a:g}", cycle_support(4, a)))
        cases.append((f"allpairs_k4_a{a:g}", all_transverse_pairs(4, a)))

    records = []
    for name, L in cases:
        k = L.shape[1]
        n = L.shape[0]
        minor, arg = max_abs_minor(L, k)
        if minor > 1.0 + 1e-8 or n > 10:
            records.append(
                {
                    "name": name,
                    "k": k,
                    "n": n,
                    "max_abs_minor": minor,
                    "skipped": True,
                    "reason": "minor bound or n limit",
                }
            )
            continue
        checks = []
        for C in [1.0, 1.25, 1.5, 2.0, 2.5, 3.0, 4.0]:
            rec = solve_support_margin(L, 0, C, keep_solution=(C in [1.0, 2.0]))
            checks.append(rec)
        records.append(
            {
                "name": name,
                "k": k,
                "n": n,
                "L": L.tolist(),
                "max_abs_minor": minor,
                "max_minor_rows": list(arg) if arg is not None else None,
                "checks": checks,
            }
        )

    Path("targeted_geom_lp_results.json").write_text(json.dumps(records, indent=2, sort_keys=True))
    lines = []
    for rec in records:
        if rec.get("skipped"):
            lines.append(f"SKIP {rec['name']}: {rec['reason']} n={rec['n']} minor={rec['max_abs_minor']:.6g}")
            continue
        parts = []
        for check in rec["checks"]:
            best = check["best"]
            margin = best.get("margin")
            ratio = best.get("ratio")
            parts.append(
                f"C={check['C']:g}:margin={margin:.4g},ratio={ratio if ratio is not None else 'na'}"
            )
        lines.append(
            f"{rec['name']} k={rec['k']} n={rec['n']} minor={rec['max_abs_minor']:.6g} | "
            + "; ".join(parts)
        )
    summary = "\n".join(lines) + "\n"
    Path("targeted_geom_lp_summary.txt").write_text(summary)
    print(summary, end="")


if __name__ == "__main__":
    main()
