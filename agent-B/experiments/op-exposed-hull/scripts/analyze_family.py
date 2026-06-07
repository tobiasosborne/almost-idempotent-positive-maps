#!/usr/bin/env python3
"""Analyze fixed exact signed retraction families for exposed-hull metrics."""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from exposed_hull import scan_grid  # noqa: E402
from families import hume, hume_product, random_similarity_retraction, regular_polygon_projection  # noqa: E402


def floats(text: str) -> list[float]:
    return [float(part) for part in text.split(",") if part.strip()]


def safe_float(value: float) -> str:
    if math.isinf(value):
        return "inf"
    if math.isnan(value):
        return "nan"
    return f"{value:.12g}"


def build_matrix(args: argparse.Namespace):
    if args.family == "hume":
        return hume(args.s)
    if args.family == "hume-product":
        return hume_product(args.s, args.power)
    if args.family == "random-similarity":
        return random_similarity_retraction(args.n, args.rank, args.amp, args.seed)
    if args.family == "regular-polygon":
        return regular_polygon_projection(args.n)
    raise ValueError(args.family)


def write_csv(path: Path, metadata: dict, reports: list[dict]) -> None:
    fields = [
        "family",
        "n",
        "rank",
        "seed",
        "s",
        "power",
        "amp",
        "delta",
        "tau",
        "rho_mult",
        "kappa_mult",
        "vertices",
        "W",
        "max_distance",
        "ratio",
        "idempotence_linf_l1",
        "row_sum_linf",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for report in reports:
            row = {
                "family": metadata.get("family"),
                "n": report["n"],
                "rank": metadata.get("rank", ""),
                "seed": metadata.get("seed", ""),
                "s": metadata.get("s", ""),
                "power": metadata.get("power", ""),
                "amp": metadata.get("amp", ""),
                "delta": safe_float(report["delta"]),
                "tau": safe_float(report["tau"]),
                "rho_mult": safe_float(report["rho_mult"]),
                "kappa_mult": safe_float(report["kappa_mult"]),
                "vertices": len(report["vertices"]),
                "W": len(report["W_indices"]),
                "max_distance": safe_float(report["max_distance_to_conv_W"]),
                "ratio": safe_float(report["max_distance_ratio"]),
                "idempotence_linf_l1": safe_float(report["errors"]["idempotence_linf_l1"]),
                "row_sum_linf": safe_float(report["errors"]["row_sum_linf"]),
            }
            writer.writerow(row)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--family",
        choices=["hume", "hume-product", "random-similarity", "regular-polygon"],
        required=True,
    )
    parser.add_argument("--s", type=float, default=0.05)
    parser.add_argument("--power", type=int, default=2)
    parser.add_argument("--n", type=int, default=6)
    parser.add_argument("--rank", type=int, default=3)
    parser.add_argument("--amp", type=float, default=0.05)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--rho-mults", default="0.5,1,2,4,8")
    parser.add_argument("--kappa-mults", default="0.1,0.25,0.5,1")
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-csv", type=Path, required=True)
    args = parser.parse_args()

    generated = build_matrix(args)
    reports = scan_grid(generated.matrix, floats(args.rho_mults), floats(args.kappa_mults))
    payload = {
        "command": " ".join(sys.argv),
        "metadata": generated.metadata,
        "matrix": generated.matrix.tolist(),
        "reports": reports,
    }
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_csv(args.out_csv, generated.metadata, reports)
    print(args.out_json)
    print(args.out_csv)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
