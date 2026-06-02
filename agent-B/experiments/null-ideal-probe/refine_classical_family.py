#!/usr/bin/env python3
"""Refine one classical family selected from classical_probe.py output."""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from classical_probe import (  # noqa: E402
    exact_absorbing_projection,
    linf_op_norm,
    maximize_defect,
    spectral_projection_near_one,
)


@dataclass
class ScalingRecord:
    a: float
    eta: float
    defect: float
    ratio_sqrt: float
    ratio_linear: float
    rank: int
    eig_cond: float
    r: list[float]
    s: list[float]
    p_matrix: list[list[float]]


def load_family(path: Path, index: int) -> tuple[np.ndarray, np.ndarray]:
    records = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(records, dict) and "w" in records and "S" in records:
        w = float(records["w"])
        return np.array([[w, 1.0 - w]], dtype=float), np.array(records["S"], dtype=float)
    if isinstance(records, dict) and "records" in records:
        return np.array(records["weights"], dtype=float), np.array(records["stochastic_s"], dtype=float)
    records = sorted(records, key=lambda r: r["ratio_linear"], reverse=True)
    rec = records[index]
    weights = np.array(rec["p0_weights"], dtype=float)
    s_mat = np.array(rec["stochastic_s"], dtype=float)
    return weights, s_mat


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--family-json", type=Path, required=True)
    parser.add_argument("--family-index", type=int, default=0)
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--samples", type=int, default=1000)
    parser.add_argument("--de-iters", type=int, default=80)
    parser.add_argument(
        "--a-values",
        type=lambda s: [float(x) for x in s.split(",")],
        default=[1e-1, 3e-2, 1e-2, 3e-3, 1e-3, 3e-4, 1e-4],
    )
    parser.add_argument("--out-dir", type=Path, default=SCRIPT_DIR / "refined-family")
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    weights, s_mat = load_family(args.family_json, args.family_index)
    n = s_mat.shape[0]
    k = weights.shape[1]
    p0, _ = exact_absorbing_projection(rng, n, k, weights=weights)

    rows: list[ScalingRecord] = []
    for a in args.a_values:
        t = (1.0 - a) * p0 + a * s_mat
        eta = linf_op_norm(t @ t - t)
        p, rank, cond = spectral_projection_near_one(t)
        defect, r, s_vec = maximize_defect(
            p, rng, samples=args.samples, de_iters=args.de_iters
        )
        rows.append(
            ScalingRecord(
                a=float(a),
                eta=float(eta),
                defect=float(defect),
                ratio_sqrt=float(defect / math.sqrt(eta)),
                ratio_linear=float(defect / eta),
                rank=rank,
                eig_cond=cond,
                r=np.round(r, 12).tolist(),
                s=np.round(s_vec, 12).tolist(),
                p_matrix=np.round(p, 12).tolist(),
            )
        )

    args.out_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.out_dir / "scaling.json"
    csv_path = args.out_dir / "scaling.csv"
    with json_path.open("w", encoding="utf-8") as f:
        json.dump(
            {
                "source": str(args.family_json),
                "family_index_by_ratio_linear": args.family_index,
                "weights": np.round(weights, 12).tolist(),
                "stochastic_s": np.round(s_mat, 12).tolist(),
                "records": [asdict(r) for r in rows],
            },
            f,
            indent=2,
        )
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "a",
                "eta",
                "defect",
                "ratio_sqrt",
                "ratio_linear",
                "rank",
                "eig_cond",
            ],
        )
        writer.writeheader()
        for r in rows:
            rr = asdict(r)
            writer.writerow({key: rr[key] for key in writer.fieldnames})

    print(f"json: {json_path}")
    print(f"csv: {csv_path}")
    print("weights:", np.round(weights, 12).tolist())
    print("S:", np.round(s_mat, 12).tolist())
    for r in rows:
        print(
            f"a={r.a:g} eta={r.eta:.9g} defect={r.defect:.9g} "
            f"def/eta={r.ratio_linear:.9g} def/sqrt(eta)={r.ratio_sqrt:.9g}"
        )


if __name__ == "__main__":
    main()
