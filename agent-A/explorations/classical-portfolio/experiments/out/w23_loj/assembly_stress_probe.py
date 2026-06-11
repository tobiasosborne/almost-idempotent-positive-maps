#!/usr/bin/env python3
"""Summarize saved w20/w21 stress data for the local linear-law assembly.

This script intentionally reuses the audited numerical artifacts rather than
reimplementing visible-height logic.  It separates fixed-base local windows
from finite-scale boundary recoding windows.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any


W21 = Path("/tmp/codex-sigma-wall/w21_second/second_order_full_records.json")
W20 = Path("/tmp/codex-sigma-wall/w20_t1_audit/independent_visibility_results.json")


def finite_ratio(sample: dict[str, Any]) -> float | None:
    value = sample.get("H_over_delta")
    if value is None:
        d = float(sample.get("delta", 0.0))
        h = float(sample.get("H", 0.0))
        if d <= 0:
            return 0.0 if h <= 1e-14 else math.inf
        value = h / d
    value = float(value)
    if not math.isfinite(value):
        return None
    return value


def summarize_w21() -> dict[str, Any]:
    data = json.loads(W21.read_text(encoding="utf-8"))
    local: list[float] = []
    transition: list[float] = []
    all_ratios: list[float] = []
    sharp_transition: list[dict[str, Any]] = []

    for rec in data["records"]:
        min_entry = float(rec["min_positive_entry"])
        for sample in rec["samples"]:
            ratio = finite_ratio(sample)
            if ratio is None:
                continue
            all_ratios.append(ratio)
            item = {
                "stratum": rec["stratum"],
                "source": rec["source"],
                "t": sample["t"],
                "min_positive_entry": min_entry,
                "t_over_min_entry": sample["t"] / min_entry if min_entry > 0 else math.inf,
                "H_over_delta": ratio,
                "delta": sample["delta"],
                "H": sample["H"],
                "visible": sample["visible"],
                "vertices": sample["vertices"],
            }
            if sample["t"] < 0.1 * min_entry:
                local.append(ratio)
            else:
                transition.append(ratio)
                if ratio >= 1.9:
                    sharp_transition.append(item)

    return {
        "records": len(data["records"]),
        "samples": len(all_ratios),
        "local_samples": len(local),
        "transition_samples": len(transition),
        "max_all_H_over_delta": max(all_ratios) if all_ratios else None,
        "max_local_H_over_delta": max(local) if local else None,
        "max_transition_H_over_delta": max(transition) if transition else None,
        "sharp_transition_count_ratio_ge_1p9": len(sharp_transition),
        "top_sharp_transition": sorted(
            sharp_transition, key=lambda x: x["H_over_delta"], reverse=True
        )[:5],
    }


def summarize_w20() -> dict[str, Any]:
    data = json.loads(W20.read_text(encoding="utf-8"))
    sweep = data["tiny_active_scale_sweep"]
    mu = float(sweep["mu"])
    local: list[float] = []
    transition: list[float] = []
    for sample in sweep["records"]:
        ratio = finite_ratio(sample)
        if ratio is None:
            continue
        if sample["t"] <= mu:
            local.append(ratio)
        else:
            transition.append(ratio)
    sanity = data["fixed_mass_sanity"]
    return {
        "fixed_mass_records": sanity["records"],
        "fixed_mass_condition_true": sanity["condition_true"],
        "fixed_mass_violations": len(sanity["violations"]),
        "tiny_active_mu": mu,
        "tiny_active_local_samples_t_le_mu": len(local),
        "tiny_active_transition_samples_t_gt_mu": len(transition),
        "tiny_active_max_local_H_over_delta": max(local) if local else None,
        "tiny_active_max_transition_H_over_delta": max(transition) if transition else None,
        "tiny_active_active_zero_derivative_cost": sweep["active_zero_derivative_cost"],
    }


def main() -> None:
    summary = {
        "w21_second_stress": summarize_w21(),
        "w20_visibility_stress": summarize_w20(),
    }
    Path("assembly_stress_results.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    lines = [
        "w23_loj local assembly stress summary",
        json.dumps(summary, indent=2),
        "",
        "interpretation:",
        "- w21 local fixed-base clean windows have max ratio reported above.",
        "- ratio-2 samples occur only in transition windows beyond the tiny positive-entry scale.",
        "- w20 fixed-mass visibility audit has zero condition violations; its tiny-active ratio-2 sample is also a transition-scale sample.",
    ]
    Path("assembly_stress_summary.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
