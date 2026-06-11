#!/usr/bin/env python3
"""Filter second-order decider output into fixed-base and boundary windows."""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("results", type=Path)
    parser.add_argument("--factor", type=float, default=0.1)
    parser.add_argument("--out", type=Path, default=Path("second_order_filtered_summary.txt"))
    parser.add_argument("--top", type=int, default=12)
    args = parser.parse_args()

    data = json.loads(args.results.read_text(encoding="utf-8"))
    records = data.get("records", [])
    local = []
    transition = []
    for rec in records:
        min_entry = float(rec["min_positive_entry"])
        cutoff = args.factor * min_entry
        local_samples = [
            s for s in rec["samples"]
            if s["t"] < cutoff and math.isfinite(s["H_over_delta"])
        ]
        transition_samples = [
            s for s in rec["samples"]
            if s["t"] >= cutoff and math.isfinite(s["H_over_delta"])
        ]
        if local_samples:
            best = max(local_samples, key=lambda s: s["H_over_delta"])
            local.append((best["H_over_delta"], rec, best, len(local_samples)))
        if transition_samples:
            best = max(transition_samples, key=lambda s: s["H_over_delta"])
            transition.append((best["H_over_delta"], rec, best, len(transition_samples)))

    local.sort(key=lambda x: x[0], reverse=True)
    transition.sort(key=lambda x: x[0], reverse=True)

    lines: list[str] = []
    lines.append(
        f"filtered local asymptotic samples: t < {args.factor:g} * min_positive_entry(P0)"
    )
    lines.append(f"records: {len(records)}")
    lines.append(f"with_local_samples: {len(local)}")
    if local:
        lines.append(f"max_local_ratio: {local[0][0]:.12g}")
        for ratio, rec, sample, count in local[: args.top]:
            lines.append(
                "local ratio={:.12g} stratum={} source={} t={} min_entry={:.3g} "
                "delta/t2={:.12g} H/t2={:.12g} q_delta_B={:.3g} "
                "dot_delta={:.3g} frozen_D={:.3g} local_count={}".format(
                    ratio,
                    rec["stratum"],
                    rec["source"],
                    sample["t"],
                    rec["min_positive_entry"],
                    sample["delta_over_t2"],
                    sample["H_over_t2"],
                    rec["q_delta_B"],
                    rec["dot_delta"],
                    rec["frozen_D"],
                    count,
                )
            )

    lines.append("")
    lines.append(
        f"finite-scale samples: t >= {args.factor:g} * min_positive_entry(P0)"
    )
    lines.append(f"with_transition_samples: {len(transition)}")
    if transition:
        lines.append(f"max_transition_ratio: {transition[0][0]:.12g}")
        for ratio, rec, sample, count in transition[: args.top]:
            lines.append(
                "transition ratio={:.12g} stratum={} source={} t={} min_entry={:.3g} "
                "delta/t={:.12g} H/t2={:.12g} visible={} vertices={} "
                "transition_count={}".format(
                    ratio,
                    rec["stratum"],
                    rec["source"],
                    sample["t"],
                    rec["min_positive_entry"],
                    sample["delta_over_t"],
                    sample["H_over_t2"],
                    sample["visible"],
                    sample["vertices"],
                    count,
                )
            )

    args.out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(args.out.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
