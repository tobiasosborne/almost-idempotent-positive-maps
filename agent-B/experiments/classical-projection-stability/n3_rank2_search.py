#!/usr/bin/env python3
"""Search rank-2 signed idempotents on l_infty^3 near the stochastic ones.

Every rank-2 row-unital idempotent on R^3 can be written

    P = I - u v^T,       v^T 1 = 0,       v^T u = 1.

For n=3 the row-stochastic idempotents are explicit:
  * I;
  * rank-one matrices with all rows equal to a probability vector;
  * one transient state and two absorbing singleton states;
  * one two-state recurrent class and one absorbing singleton state.

The script samples the rank-2 signed family and computes the exact
max-row-l1 distance to this enumerated stochastic-idempotent union up to
one-dimensional/global numerical optimization.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np
from numpy.typing import NDArray
from scipy import optimize


Array = NDArray[np.float64]


@dataclass
class Record:
    delta: float
    distance: float
    ratio_linear: float
    ratio_sqrt: float
    nearest_type: str
    p: list[list[float]]
    u: list[float]
    v: list[float]


def row_l1_norm(a: Array) -> float:
    return float(np.max(np.sum(np.abs(a), axis=1)))


def neg_mass(p: Array) -> float:
    return float(np.max(np.sum(np.maximum(-p, 0.0), axis=1)))


def dist_to_matrix(p: Array, e: Array) -> float:
    return row_l1_norm(p - e)


def rank_one_matrix(mu: Array) -> Array:
    return np.tile(mu.reshape(1, 3), (3, 1))


def transient_matrix(t: int, a: int, b: int, lam: float) -> Array:
    e = np.eye(3)
    out = np.zeros((3, 3))
    out[a] = e[a]
    out[b] = e[b]
    out[t, a] = lam
    out[t, b] = 1.0 - lam
    return out


def class_pair_matrix(a: int, b: int, c: int, lam: float) -> Array:
    e = np.eye(3)
    pi = np.zeros(3)
    pi[a] = lam
    pi[b] = 1.0 - lam
    out = np.zeros((3, 3))
    out[a] = pi
    out[b] = pi
    out[c] = e[c]
    return out


def best_distance_to_stochastic_idempotent(p: Array) -> tuple[float, str]:
    best = (dist_to_matrix(p, np.eye(3)), "identity")

    def update(value: float, name: str) -> None:
        nonlocal best
        if value < best[0]:
            best = (value, name)

    def simplex_obj(x: Array) -> float:
        a, b = x
        if a < 0 or b < 0 or a + b > 1:
            return 10.0 + abs(min(a, b, 1 - a - b))
        mu = np.array([a, b, 1.0 - a - b])
        return dist_to_matrix(p, rank_one_matrix(mu))

    result = optimize.differential_evolution(
        simplex_obj,
        bounds=[(0.0, 1.0), (0.0, 1.0)],
        constraints=(),
        tol=1e-10,
        polish=True,
        seed=12345,
        workers=1,
    )
    update(float(result.fun), "rank_one")

    for t in range(3):
        a, b = [i for i in range(3) if i != t]

        res = optimize.minimize_scalar(
            lambda lam: dist_to_matrix(p, transient_matrix(t, a, b, lam)),
            bounds=(0.0, 1.0),
            method="bounded",
            options={"xatol": 1e-12},
        )
        update(float(res.fun), f"transient_{t}")

        res = optimize.minimize_scalar(
            lambda lam: dist_to_matrix(p, class_pair_matrix(a, b, t, lam)),
            bounds=(0.0, 1.0),
            method="bounded",
            options={"xatol": 1e-12},
        )
        update(float(res.fun), f"class_pair_{a}{b}")

    return best


def sample_projection(rng: np.random.Generator) -> tuple[Array, Array, Array] | None:
    v = rng.normal(size=3)
    v = v - np.mean(v)
    if np.linalg.norm(v) < 1e-12:
        return None

    u0 = rng.normal(size=3)
    denom = float(v @ u0)
    if abs(denom) < 1e-8:
        return None
    u = u0 / denom
    p = np.eye(3) - np.outer(u, v)
    return p, u, v


def run(args: argparse.Namespace) -> list[Record]:
    rng = np.random.default_rng(args.seed)
    records: list[Record] = []
    best_by_bin: dict[int, Record] = {}

    for _ in range(args.samples):
        item = sample_projection(rng)
        if item is None:
            continue
        p, u, v = item
        err_idem = row_l1_norm(p @ p - p)
        err_unital = float(np.max(np.abs(p @ np.ones(3) - 1.0)))
        if err_idem > 1e-8 or err_unital > 1e-8:
            continue
        delta = neg_mass(p)
        if not (args.min_delta <= delta <= args.max_delta):
            continue
        dist, typ = best_distance_to_stochastic_idempotent(p)
        rec = Record(
            delta=delta,
            distance=dist,
            ratio_linear=dist / delta if delta else math.inf,
            ratio_sqrt=dist / math.sqrt(delta) if delta else math.inf,
            nearest_type=typ,
            p=np.round(p, 12).tolist(),
            u=np.round(u, 12).tolist(),
            v=np.round(v, 12).tolist(),
        )
        records.append(rec)
        bin_id = int(math.floor(-math.log10(delta))) if delta > 0 else 99
        old = best_by_bin.get(bin_id)
        if old is None or rec.ratio_linear > old.ratio_linear:
            best_by_bin[bin_id] = rec

    records.sort(key=lambda r: r.ratio_linear, reverse=True)
    return records[: args.keep]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20260602)
    parser.add_argument("--samples", type=int, default=20000)
    parser.add_argument("--min-delta", type=float, default=1e-6)
    parser.add_argument("--max-delta", type=float, default=0.08)
    parser.add_argument("--keep", type=int, default=50)
    parser.add_argument("--out-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()

    records = run(args)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.out_dir / "n3_rank2_search.json"
    csv_path = args.out_dir / "n3_rank2_search.csv"
    json_path.write_text(json.dumps([asdict(r) for r in records], indent=2), encoding="utf-8")
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["delta", "distance", "ratio_linear", "ratio_sqrt", "nearest_type"],
        )
        writer.writeheader()
        for rec in records:
            writer.writerow({
                "delta": rec.delta,
                "distance": rec.distance,
                "ratio_linear": rec.ratio_linear,
                "ratio_sqrt": rec.ratio_sqrt,
                "nearest_type": rec.nearest_type,
            })
    print(f"wrote {json_path}")
    for rec in records[:10]:
        print(
            f"delta={rec.delta:.6g} dist={rec.distance:.6g} "
            f"dist/delta={rec.ratio_linear:.6g} type={rec.nearest_type}"
        )


if __name__ == "__main__":
    main()
