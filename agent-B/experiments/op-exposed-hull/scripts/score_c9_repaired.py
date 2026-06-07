#!/usr/bin/env python3
"""C9 repaired-kernel scorer for direct op-exposed-hull samples.

This is Agent B sandbox evidence only.  It searches for samples where the
repaired positive-coordinate chain has a long-lived bad class but the shadow
witnesses do not stay in the high slice, which would threaten the C9 interface.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from pathlib import Path
from typing import Iterable

import numpy as np
from scipy.optimize import linprog

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from direct_ab import (  # noqa: E402
    anchor_barycentric_retraction,
    free_left_inverse_retraction,
)
from exposed_hull import (  # noqa: E402
    exposed_hull_report,
    l1_distance_to_conv,
    max_negative_mass,
    retraction_errors,
)


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


def repaired_kernel(rows: np.ndarray) -> np.ndarray:
    positive = np.maximum(rows, 0.0)
    denom = positive.sum(axis=1)
    if np.any(denom <= 0.0):
        raise ValueError("row has zero positive mass")
    return positive / denom[:, None]


def separator_to_hull(point: np.ndarray, hull_points: np.ndarray) -> tuple[np.ndarray, float]:
    """Return l_infty-bounded separator maximizing phi(point)-max_H phi."""
    point = np.asarray(point, dtype=float)
    hull_points = np.asarray(hull_points, dtype=float)
    d = point.shape[0]
    if hull_points.size == 0:
        raise ValueError("empty hull")
    if hull_points.ndim == 1:
        hull_points = hull_points.reshape(1, -1)

    # Variables are phi in R^d and m=max_H phi.  Minimize m-phi(point).
    c = np.r_[-point, 1.0]
    a_ub = []
    b_ub = []
    for row in hull_points:
        constraint = np.r_[row, -1.0]
        a_ub.append(constraint)
        b_ub.append(0.0)
    bounds = [(-1.0, 1.0)] * d + [(None, None)]
    res = linprog(c, A_ub=np.asarray(a_ub), b_ub=np.asarray(b_ub), bounds=bounds, method="highs")
    if not res.success:
        raise RuntimeError(res.message)
    phi = np.asarray(res.x[:d], dtype=float)
    gap = float(point @ phi - res.x[d])
    return phi, gap


def lifetime_from_subkernel(t: np.ndarray) -> float:
    if t.size == 0:
        return 0.0
    eye = np.eye(t.shape[0])
    try:
        life = np.linalg.solve(eye - t, np.ones(t.shape[0]))
    except np.linalg.LinAlgError:
        return math.inf
    if np.any(life < -1e-7):
        return math.inf
    return float(np.max(life))


def stat_block(values: Iterable[float]) -> dict:
    vals = [float(v) for v in values if math.isfinite(float(v))]
    if not vals:
        return {"count": 0, "max": math.nan, "mean": math.nan}
    return {"count": len(vals), "max": max(vals), "mean": float(sum(vals) / len(vals))}


def min_shadow_leakage(
    rows: np.ndarray,
    phi_values: np.ndarray,
    outside: list[int],
    high_slice: set[int],
    threshold: float,
) -> float | None:
    if not outside:
        return None
    c = np.array([0.0 if idx in high_slice else 1.0 for idx in outside], dtype=float)
    a_ub = -phi_values[outside].reshape(1, -1)
    b_ub = np.array([-threshold])
    a_eq = np.ones((1, len(outside)))
    b_eq = np.array([1.0])
    res = linprog(
        c,
        A_ub=a_ub,
        b_ub=b_ub,
        A_eq=a_eq,
        b_eq=b_eq,
        bounds=[(0.0, None)] * len(outside),
        method="highs",
    )
    if not res.success:
        return None
    return float(res.fun)


def shadow_stats(rows: np.ndarray, vertices: list[int], phi: np.ndarray, h1: set[int], rho: float, kappa: float) -> dict:
    delta = max_negative_mass(rows)
    phi_values = rows @ phi
    step3_drop = float((2.0 + 4.0 * delta) * kappa)
    records = []
    for idx in vertices:
        outside = [j for j, row in enumerate(rows) if np.linalg.norm(row - rows[idx], ord=1) >= rho]
        if not outside:
            continue
        best = max(outside, key=lambda j: phi_values[j])
        threshold = float(phi_values[idx] - step3_drop)
        records.append(
            {
                "vertex": int(idx),
                "best_outside": int(best),
                "drop": float(phi_values[idx] - phi_values[best]),
                "step3_drop_bound": step3_drop,
                "best_outside_in_H1": bool(best in h1),
                "min_leakage_for_step3_average": min_shadow_leakage(rows, phi_values, outside, h1, threshold),
            }
        )
    leakages = [
        rec["min_leakage_for_step3_average"]
        for rec in records
        if rec["min_leakage_for_step3_average"] is not None
    ]
    return {
        "records": records[:12],
        "record_count": len(records),
        "max_min_leakage": max(leakages) if leakages else math.nan,
        "best_row_leak_count": sum(0 if rec["best_outside_in_H1"] else 1 for rec in records),
    }


def distances_to_hull(rows: np.ndarray, w_indices: list[int]) -> list[float]:
    if not w_indices:
        return [math.inf] * rows.shape[0]
    hull = rows[w_indices]
    return [float(l1_distance_to_conv(row, hull).value) for row in rows]


def score_matrix(
    rows: np.ndarray,
    metadata: dict,
    rho_mult: float,
    kappa_mult: float,
    bad_distance_mult: float,
    h0_delta_mult: float,
    h1_tau_mult: float,
) -> dict:
    rows = np.asarray(rows, dtype=float)
    delta = max_negative_mass(rows)
    tau = math.sqrt(max(delta, 0.0))
    report = exposed_hull_report(rows, rho_mult, kappa_mult)
    w_indices = list(report["W_indices"])
    distances = distances_to_hull(rows, w_indices)
    finite_distances = [d for d in distances if math.isfinite(d)]
    max_distance = max(finite_distances) if finite_distances else math.inf
    focus = int(max(range(rows.shape[0]), key=lambda idx: distances[idx] if math.isfinite(distances[idx]) else -1.0))

    q = repaired_kernel(rows)
    repair_errors = np.sum(np.abs(rows - q @ rows), axis=1)
    bad_threshold = bad_distance_mult * tau
    bad = [idx for idx, dist in enumerate(distances) if math.isfinite(dist) and dist > bad_threshold]
    t = q[np.ix_(bad, bad)] if bad else np.empty((0, 0))
    lifetime = lifetime_from_subkernel(t)
    bad_exit = [] if not bad else list(1.0 - t.sum(axis=1))

    c9 = {
        "bad_distance_threshold": float(bad_threshold),
        "bad_indices": [int(idx) for idx in bad],
        "bad_count": len(bad),
        "bad_lifetime": lifetime,
        "tau_times_bad_lifetime": float(tau * lifetime) if math.isfinite(lifetime) else math.inf,
        "bad_exit": stat_block(bad_exit),
        "repair_error": stat_block(repair_errors),
        "repair_error_over_delta_max": float(max(repair_errors) / delta) if delta > 0.0 else math.nan,
    }

    sep_info = None
    if w_indices and math.isfinite(max_distance) and max_distance > 1e-10:
        phi, sep_gap = separator_to_hull(rows[focus], rows[w_indices])
        phi_values = rows @ phi
        height = np.max(phi_values) - phi_values
        h0_limit = h0_delta_mult * delta
        h1_limit = h1_tau_mult * tau
        h0 = {idx for idx, value in enumerate(height) if value <= h0_limit + 1e-12}
        h1 = {idx for idx, value in enumerate(height) if value <= h1_limit + 1e-12}
        q_exit_h1 = [1.0 - q[idx, list(h1)].sum() for idx in h0] if h1 else [1.0 for _ in h0]
        q_exit_h1_from_h1 = [1.0 - q[idx, list(h1)].sum() for idx in h1] if h1 else []
        phi_repair = phi_values - q @ phi_values
        sep_info = {
            "focus_row": focus,
            "separator_gap": sep_gap,
            "focus_distance_to_conv_W": float(distances[focus]),
            "max_phi": float(np.max(phi_values)),
            "focus_height": float(height[focus]),
            "H0_limit": float(h0_limit),
            "H1_limit": float(h1_limit),
            "H0": sorted(int(idx) for idx in h0),
            "H1": sorted(int(idx) for idx in h1),
            "q_exit_H0_to_H1c": stat_block(q_exit_h1),
            "q_exit_H1_to_H1c": stat_block(q_exit_h1_from_h1),
            "phi_repair_error": stat_block(np.abs(phi_repair)),
            "phi_repair_error_over_delta_max": float(max(abs(phi_repair)) / delta) if delta > 0.0 else math.nan,
            "shadow": shadow_stats(rows, list(report["vertices"]), phi, h1, report["rho"], report["kappa"]),
        }

    threat_tuple = [
        1 if bad else 0,
        c9["tau_times_bad_lifetime"] if math.isfinite(c9["tau_times_bad_lifetime"]) else 1e100,
        float(max_distance / tau) if tau > 0.0 and math.isfinite(max_distance) else 0.0,
        0.0
        if sep_info is None or math.isnan(sep_info["shadow"]["max_min_leakage"])
        else float(sep_info["shadow"]["max_min_leakage"]),
    ]
    return {
        "metadata": metadata,
        "constants": {
            "rho_mult": float(rho_mult),
            "kappa_mult": float(kappa_mult),
            "rho": float(report["rho"]),
            "kappa": float(report["kappa"]),
        },
        "delta": float(delta),
        "tau": float(tau),
        "errors": retraction_errors(rows),
        "vertices": [int(idx) for idx in report["vertices"]],
        "W_indices": [int(idx) for idx in w_indices],
        "max_distance_to_conv_W": float(max_distance),
        "max_distance_ratio": float(max_distance / tau) if tau > 0.0 and math.isfinite(max_distance) else math.inf,
        "row_distances_to_conv_W": distances,
        "c9": c9,
        "separator": sep_info,
        "threat_tuple": threat_tuple,
        "matrix": rows.tolist(),
    }


def build_candidate(family: str, n: int, rank: int, target_delta: float, seed: int, args: argparse.Namespace):
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


def load_existing(paths: list[Path]) -> list[tuple[np.ndarray, dict]]:
    samples = []
    for path in paths:
        payload = json.loads(path.read_text(encoding="utf-8"))
        for item in payload.get("top", []):
            meta = dict(item.get("metadata", {}))
            meta["source_json"] = str(path)
            samples.append((np.asarray(item["matrix"], dtype=float), meta))
    return samples


def write_csv(path: Path, rows: list[dict]) -> None:
    fields = [
        "family",
        "source_json",
        "n",
        "rank",
        "target_delta",
        "delta",
        "tau",
        "seed",
        "rho_mult",
        "kappa_mult",
        "vertices",
        "W",
        "max_distance_ratio",
        "bad_count",
        "tau_times_bad_lifetime",
        "bad_exit_max",
        "H0_size",
        "H1_size",
        "q_exit_H0_to_H1c_max",
        "max_shadow_min_leakage",
        "repair_error_over_delta_max",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for item in rows:
            meta = item["metadata"]
            sep = item["separator"] or {}
            shadow = sep.get("shadow", {})
            writer.writerow(
                {
                    "family": meta.get("family"),
                    "source_json": meta.get("source_json", ""),
                    "n": meta.get("n"),
                    "rank": meta.get("rank"),
                    "target_delta": meta.get("target_delta"),
                    "delta": item["delta"],
                    "tau": item["tau"],
                    "seed": meta.get("seed"),
                    "rho_mult": item["constants"]["rho_mult"],
                    "kappa_mult": item["constants"]["kappa_mult"],
                    "vertices": len(item["vertices"]),
                    "W": len(item["W_indices"]),
                    "max_distance_ratio": item["max_distance_ratio"],
                    "bad_count": item["c9"]["bad_count"],
                    "tau_times_bad_lifetime": item["c9"]["tau_times_bad_lifetime"],
                    "bad_exit_max": item["c9"]["bad_exit"]["max"],
                    "H0_size": len(sep.get("H0", [])),
                    "H1_size": len(sep.get("H1", [])),
                    "q_exit_H0_to_H1c_max": sep.get("q_exit_H0_to_H1c", {}).get("max", ""),
                    "max_shadow_min_leakage": shadow.get("max_min_leakage", ""),
                    "repair_error_over_delta_max": item["c9"]["repair_error_over_delta_max"],
                }
            )


def jsonable(value):
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-json", action="append", type=Path, default=[])
    parser.add_argument("--families", default="anchor,free")
    parser.add_argument("--n-ranks", default="5:2,5:3,6:3,7:3,8:4")
    parser.add_argument("--target-deltas", default="0.0001,0.001,0.01")
    parser.add_argument("--rho-mults", default="1,2,4")
    parser.add_argument("--kappa-mults", default="0.05,0.1,0.25")
    parser.add_argument("--samples", type=int, default=12)
    parser.add_argument("--seed", type=int, default=2026060711)
    parser.add_argument("--keep", type=int, default=20)
    parser.add_argument("--bad-distance-mult", type=float, default=0.05)
    parser.add_argument("--h0-delta-mult", type=float, default=16.0)
    parser.add_argument("--h1-tau-mult", type=float, default=4.0)
    parser.add_argument("--outside-probability", type=float, default=0.65)
    parser.add_argument("--feature-noises", default="0,0.001,0.005,0.02")
    parser.add_argument("--max-amp", type=float, default=0.25)
    parser.add_argument("--amp-grid", type=int, default=24)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--out-csv", type=Path)
    args = parser.parse_args()

    rho_mults = floats(args.rho_mults)
    kappa_mults = floats(args.kappa_mults)
    candidates = load_existing(args.input_json)
    aggregate = {
        "loaded_existing": len(candidates),
        "attempted_generated": 0,
        "accepted_generated": 0,
        "skipped_above_target_delta": 0,
        "errors": 0,
        "scored_constants": 0,
        "nonempty_bad_reports": 0,
    }
    errors = []

    for fam_index, fam in enumerate(families(args.families)):
        for delta_index, target_delta in enumerate(floats(args.target_deltas)):
            for pair_index, (n, rank) in enumerate(pairs(args.n_ranks)):
                for sample in range(args.samples):
                    seed = args.seed + 1_000_000 * fam_index + 100_000 * delta_index + 1_000 * pair_index + sample
                    aggregate["attempted_generated"] += 1
                    try:
                        candidate = build_candidate(fam, n, rank, target_delta, seed, args)
                        if candidate.metadata["delta"] > target_delta + 1e-10:
                            aggregate["skipped_above_target_delta"] += 1
                            continue
                        candidates.append((candidate.matrix, candidate.metadata))
                        aggregate["accepted_generated"] += 1
                    except Exception as exc:  # pragma: no cover - exploratory runner
                        aggregate["errors"] += 1
                        errors.append({"family": fam, "n": n, "rank": rank, "seed": seed, "error": repr(exc)})

    top = []
    for matrix, metadata in candidates:
        for rho_mult in rho_mults:
            for kappa_mult in kappa_mults:
                try:
                    item = score_matrix(
                        matrix,
                        metadata,
                        rho_mult,
                        kappa_mult,
                        args.bad_distance_mult,
                        args.h0_delta_mult,
                        args.h1_tau_mult,
                    )
                except Exception as exc:  # pragma: no cover - exploratory runner
                    aggregate["errors"] += 1
                    errors.append({"metadata": metadata, "rho_mult": rho_mult, "kappa_mult": kappa_mult, "error": repr(exc)})
                    continue
                aggregate["scored_constants"] += 1
                if item["c9"]["bad_count"]:
                    aggregate["nonempty_bad_reports"] += 1
                top.append(item)
                top.sort(key=lambda row: tuple(row["threat_tuple"]), reverse=True)
                top = top[: args.keep]

    payload = {
        "status": "Agent B sandbox numerical evidence only; not a proof.",
        "command": " ".join(sys.argv),
        "objective": "rank repaired-coordinate C9 threats by bad lifetime, bad distance, and shadow leakage",
        "parameters": jsonable(vars(args)),
        "aggregate": aggregate,
        "errors": errors[:30],
        "top": top,
    }
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(args.out_json)
    if args.out_csv:
        write_csv(args.out_csv, top)
        print(args.out_csv)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
