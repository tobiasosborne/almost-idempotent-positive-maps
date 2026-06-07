#!/usr/bin/env python3
"""Search exact affine retractions from the direct P=A B parameterization."""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from direct_ab import (  # noqa: E402
    anchor_barycentric_retraction,
    free_left_inverse_retraction,
)
from exposed_hull import scan_grid  # noqa: E402


def floats(text: str) -> list[float]:
    return [float(part) for part in text.split(",") if part.strip()]


def pairs(text: str) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for part in text.split(","):
        if not part.strip():
            continue
        n_text, rank_text = part.split(":", 1)
        out.append((int(n_text), int(rank_text)))
    return out


def families(text: str) -> list[str]:
    items = [part.strip() for part in text.split(",") if part.strip()]
    bad = [item for item in items if item not in {"anchor", "free"}]
    if bad:
        raise ValueError(f"unknown families: {bad}")
    return items


def report_score(report: dict) -> float | None:
    if not report["W_indices"]:
        return None
    value = float(report["max_distance_ratio"])
    if math.isfinite(value):
        return value
    return None


def summarize_reports(reports: list[dict]) -> dict:
    finite: list[tuple[float, dict]] = []
    empty_w = 0
    for report in reports:
        if not report["W_indices"]:
            empty_w += 1
        score = report_score(report)
        if score is not None:
            finite.append((score, report))
    finite.sort(key=lambda item: item[0], reverse=True)
    best = finite[0][1] if finite else None
    return {
        "score": float(finite[0][0]) if finite else -math.inf,
        "empty_w_count": int(empty_w),
        "finite_report_count": int(len(finite)),
        "best_constants": None
        if best is None
        else {
            "rho_mult": float(best["rho_mult"]),
            "kappa_mult": float(best["kappa_mult"]),
            "vertices": int(len(best["vertices"])),
            "W": int(len(best["W_indices"])),
            "max_distance": float(best["max_distance_to_conv_W"]),
            "ratio": float(best["max_distance_ratio"]),
        },
    }


def matrix_payload(entry) -> dict:
    return {
        "matrix": entry.matrix.tolist(),
        "A": entry.a_matrix.tolist(),
        "B": entry.b_matrix.tolist(),
    }


def evaluate(entry, rho_mults: list[float], kappa_mults: list[float]) -> dict:
    reports = scan_grid(entry.matrix, rho_mults, kappa_mults)
    summary = summarize_reports(reports)
    return {
        "metadata": entry.metadata,
        "summary": summary,
        "reports": reports,
        **matrix_payload(entry),
    }


def build_candidate(
    family: str,
    n: int,
    rank: int,
    target_delta: float,
    seed: int,
    args: argparse.Namespace,
):
    if family == "anchor":
        return anchor_barycentric_retraction(
            n,
            rank,
            target_delta,
            seed,
            outside_probability=args.outside_probability,
        )
    noise_choices = floats(args.feature_noises)
    noise = noise_choices[seed % len(noise_choices)]
    return free_left_inverse_retraction(
        n,
        rank,
        target_delta,
        seed,
        feature_noise=noise,
        max_amp=args.max_amp,
        amp_grid=args.amp_grid,
    )


def write_csv(path: Path, top: list[dict]) -> None:
    fields = [
        "family",
        "n",
        "rank",
        "target_delta",
        "delta",
        "seed",
        "score",
        "empty_w_count",
        "rho_mult",
        "kappa_mult",
        "vertices",
        "W",
        "max_distance",
        "ratio",
        "idempotence_linf_l1",
        "row_sum_linf",
        "BA_error_linf",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for item in top:
            meta = item["metadata"]
            best = item["summary"]["best_constants"] or {}
            writer.writerow(
                {
                    "family": meta.get("family"),
                    "n": meta.get("n"),
                    "rank": meta.get("rank"),
                    "target_delta": meta.get("target_delta"),
                    "delta": meta.get("delta"),
                    "seed": meta.get("seed"),
                    "score": item["summary"]["score"],
                    "empty_w_count": item["summary"]["empty_w_count"],
                    "rho_mult": best.get("rho_mult", ""),
                    "kappa_mult": best.get("kappa_mult", ""),
                    "vertices": best.get("vertices", ""),
                    "W": best.get("W", ""),
                    "max_distance": best.get("max_distance", ""),
                    "ratio": best.get("ratio", ""),
                    "idempotence_linf_l1": meta["errors"]["idempotence_linf_l1"],
                    "row_sum_linf": meta["errors"]["row_sum_linf"],
                    "BA_error_linf": meta["BA_error_linf"],
                }
            )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--families", default="anchor,free")
    parser.add_argument("--n-ranks", default="5:2,5:3,6:3,7:3,8:4")
    parser.add_argument("--target-deltas", default="0.0001,0.001,0.01")
    parser.add_argument("--rho-mults", default="0.5,1,2,4")
    parser.add_argument("--kappa-mults", default="0.1,0.25,0.5")
    parser.add_argument("--samples", type=int, default=20)
    parser.add_argument("--seed", type=int, default=20260607)
    parser.add_argument("--keep", type=int, default=12)
    parser.add_argument("--outside-probability", type=float, default=0.65)
    parser.add_argument("--feature-noises", default="0,0.005,0.02,0.05")
    parser.add_argument("--max-amp", type=float, default=0.1)
    parser.add_argument("--amp-grid", type=int, default=24)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-csv", type=Path)
    args = parser.parse_args()

    fams = families(args.families)
    n_rank_pairs = pairs(args.n_ranks)
    target_deltas = floats(args.target_deltas)
    rho_mults = floats(args.rho_mults)
    kappa_mults = floats(args.kappa_mults)
    top: list[dict] = []
    aggregate = {
        "attempted": 0,
        "accepted": 0,
        "skipped_above_target_delta": 0,
        "errors": 0,
        "empty_w_reports": 0,
    }
    errors: list[dict] = []

    for fam_index, fam in enumerate(fams):
        for delta_index, target_delta in enumerate(target_deltas):
            for pair_index, (n, rank) in enumerate(n_rank_pairs):
                if rank > n:
                    continue
                for sample in range(args.samples):
                    seed = (
                        args.seed
                        + 1_000_000 * fam_index
                        + 100_000 * delta_index
                        + 1_000 * pair_index
                        + sample
                    )
                    aggregate["attempted"] += 1
                    try:
                        candidate = build_candidate(fam, n, rank, target_delta, seed, args)
                        if candidate.metadata["delta"] > target_delta + 1e-10:
                            aggregate["skipped_above_target_delta"] += 1
                            continue
                        item = evaluate(candidate, rho_mults, kappa_mults)
                    except Exception as exc:  # pragma: no cover - exploratory runner
                        aggregate["errors"] += 1
                        errors.append(
                            {
                                "family": fam,
                                "n": n,
                                "rank": rank,
                                "target_delta": target_delta,
                                "seed": seed,
                                "error": repr(exc),
                            }
                        )
                        continue
                    aggregate["accepted"] += 1
                    aggregate["empty_w_reports"] += item["summary"]["empty_w_count"]
                    top.append(item)
                    top.sort(
                        key=lambda row: (
                            row["summary"]["score"],
                            -row["summary"]["empty_w_count"],
                        ),
                        reverse=True,
                    )
                    top = top[: args.keep]

    parameters = {
        key: str(value) if isinstance(value, Path) else value
        for key, value in vars(args).items()
    }
    payload = {
        "status": "Agent B sandbox numerical evidence only; not a proof.",
        "command": " ".join(sys.argv),
        "objective": "maximize finite dist(row,conv W)/sqrt(delta); empty W reports are counted separately",
        "parameters": parameters,
        "aggregate": aggregate,
        "errors": errors[:20],
        "top": top,
    }
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(args.out_json)
    if args.out_csv:
        args.out_csv.parent.mkdir(parents=True, exist_ok=True)
        write_csv(args.out_csv, top)
        print(args.out_csv)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
