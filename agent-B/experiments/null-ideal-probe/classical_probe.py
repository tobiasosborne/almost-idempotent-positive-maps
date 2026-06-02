#!/usr/bin/env python3
"""Numerical probe for the approximate Effros-Stormer null-ideal term.

Classical model:
  V = R^n with sup norm and pointwise Jordan product.
  Phi is a row-stochastic matrix T acting on column vectors.
  eta = ||T^2 - T||_{infty -> infinity}.
  P is the spectral projection of T onto the near-1 eigenvalue cluster.

For r,s in Im P with ||r||_inf, ||s||_inf <= 1, the script maximizes
  || P( (r*s - P(r*s))^2 ) ||_inf
by randomized search plus differential evolution in range coordinates.

All generated examples are perturbations T=(1-a)P0+aS of exact stochastic
idempotents P0 with singleton recurrent states and transient rows.
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
from scipy import linalg, optimize


Array = NDArray[np.float64]


@dataclass
class Record:
    n: int
    k: int
    a: float
    eta: float
    defect: float
    ratio_sqrt: float
    ratio_linear: float
    rank: int
    eig_cond: float
    trial: int
    seed: int
    p0_weights: list[list[float]]
    stochastic_s: list[list[float]]
    p_matrix: list[list[float]]
    r: list[float]
    s: list[float]


def row_stochastic(rng: np.random.Generator, n: int) -> Array:
    return rng.dirichlet(np.ones(n), size=n)


def exact_absorbing_projection(
    rng: np.random.Generator, n: int, k: int, weights: Array | None = None
) -> tuple[Array, Array]:
    """Return a rank-k stochastic idempotent with k absorbing singleton states."""
    if not (1 <= k < n):
        raise ValueError("need 1 <= k < n")
    p0 = np.zeros((n, n), dtype=float)
    for i in range(k):
        p0[i, i] = 1.0
    if weights is None:
        weights = rng.dirichlet(np.ones(k), size=n - k)
    for row, w in enumerate(weights, start=k):
        p0[row, :k] = w
    return p0, np.array(weights, dtype=float)


def linf_op_norm(m: Array) -> float:
    return float(np.max(np.sum(np.abs(m), axis=1)))


def spectral_projection_near_one(t: Array, threshold: float = 0.5) -> tuple[Array, int, float]:
    vals, vecs = linalg.eig(t)
    mask = np.abs(vals - 1.0) < threshold
    rank = int(np.count_nonzero(mask))
    if rank == 0:
        raise ValueError("no near-one eigenvalue cluster")
    cond = float(np.linalg.cond(vecs))
    inv_vecs = linalg.inv(vecs)
    p = vecs[:, mask] @ inv_vecs[mask, :]
    p = np.real_if_close(p, tol=1000)
    if np.max(np.abs(np.imag(p))) > 1e-7:
        raise ValueError("spectral projection has non-negligible imaginary part")
    return np.array(np.real(p), dtype=float), rank, cond


def range_basis(p: Array, tol: float = 1e-8) -> Array:
    u, svals, _ = linalg.svd(p)
    rank = int(np.count_nonzero(svals > tol))
    return np.array(u[:, :rank], dtype=float)


def normalized_range_vector(basis: Array, coeffs: Array) -> Array | None:
    x = basis @ coeffs
    norm = float(np.max(np.abs(x)))
    if norm < 1e-12:
        return None
    return x / norm


def defect_for_vectors(p: Array, r: Array, s: Array) -> float:
    raw = r * s
    h = raw - p @ raw
    return float(np.max(np.abs(p @ (h * h))))


def maximize_defect(
    p: Array,
    rng: np.random.Generator,
    samples: int,
    de_iters: int,
) -> tuple[float, Array, Array]:
    basis = range_basis(p)
    rank = basis.shape[1]
    best = -1.0
    best_r: Array | None = None
    best_s: Array | None = None

    def eval_coeffs(z: Array) -> float:
        a = z[:rank]
        b = z[rank:]
        r = normalized_range_vector(basis, a)
        s = normalized_range_vector(basis, b)
        if r is None or s is None:
            return 0.0
        return defect_for_vectors(p, r, s)

    for _ in range(samples):
        z = rng.normal(size=2 * rank)
        val = eval_coeffs(z)
        if val > best:
            r = normalized_range_vector(basis, z[:rank])
            s = normalized_range_vector(basis, z[rank:])
            if r is not None and s is not None:
                best = val
                best_r = r
                best_s = s

    # Coordinate axes and sign combinations help when rank is tiny.
    for z in np.eye(2 * rank):
        for sign in (1.0, -1.0):
            zz = sign * z + 0.37 * rng.normal(size=2 * rank)
            val = eval_coeffs(zz)
            if val > best:
                r = normalized_range_vector(basis, zz[:rank])
                s = normalized_range_vector(basis, zz[rank:])
                if r is not None and s is not None:
                    best = val
                    best_r = r
                    best_s = s

    if de_iters > 0:
        bounds = [(-2.0, 2.0)] * (2 * rank)
        result = optimize.differential_evolution(
            lambda z: -eval_coeffs(np.array(z, dtype=float)),
            bounds=bounds,
            maxiter=de_iters,
            popsize=10,
            polish=True,
            tol=1e-7,
            seed=int(rng.integers(0, 2**31 - 1)),
            workers=1,
            updating="immediate",
        )
        val = -float(result.fun)
        if val > best:
            z = np.array(result.x, dtype=float)
            r = normalized_range_vector(basis, z[:rank])
            s = normalized_range_vector(basis, z[rank:])
            if r is not None and s is not None:
                best = val
                best_r = r
                best_s = s

    assert best_r is not None and best_s is not None
    return best, best_r, best_s


def run_search(args: argparse.Namespace) -> list[Record]:
    rng = np.random.default_rng(args.seed)
    records: list[Record] = []

    for n, k in args.dims:
        for p0_trial in range(args.p0_trials):
            p0, weights = exact_absorbing_projection(rng, n, k)
            for trial in range(args.trials):
                s_mat = row_stochastic(rng, n)
                for a in args.a_values:
                    t = (1.0 - a) * p0 + a * s_mat
                    eta = linf_op_norm(t @ t - t)
                    if eta <= 0 or eta > args.max_eta:
                        continue
                    try:
                        p, rank, cond = spectral_projection_near_one(t)
                    except Exception:
                        continue
                    if rank != k or not math.isfinite(cond) or cond > args.max_cond:
                        continue
                    defect, r, s_vec = maximize_defect(
                        p, rng, samples=args.samples, de_iters=args.de_iters
                    )
                    rec = Record(
                        n=n,
                        k=k,
                        a=float(a),
                        eta=float(eta),
                        defect=float(defect),
                        ratio_sqrt=float(defect / math.sqrt(eta)),
                        ratio_linear=float(defect / eta),
                        rank=rank,
                        eig_cond=cond,
                        trial=trial + args.trials * p0_trial,
                        seed=args.seed,
                        p0_weights=np.round(weights, 12).tolist(),
                        stochastic_s=np.round(s_mat, 12).tolist(),
                        p_matrix=np.round(p, 12).tolist(),
                        r=np.round(r, 12).tolist(),
                        s=np.round(s_vec, 12).tolist(),
                    )
                    records.append(rec)
    return records


def parse_dims(raw: str) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for part in raw.split(","):
        n_s, k_s = part.split(":")
        out.append((int(n_s), int(k_s)))
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20260602)
    parser.add_argument("--dims", type=parse_dims, default=parse_dims("3:2,4:2,4:3,5:2,5:3"))
    parser.add_argument("--p0-trials", type=int, default=8)
    parser.add_argument("--trials", type=int, default=40)
    parser.add_argument("--samples", type=int, default=300)
    parser.add_argument("--de-iters", type=int, default=18)
    parser.add_argument("--max-eta", type=float, default=0.25)
    parser.add_argument("--max-cond", type=float, default=1e6)
    parser.add_argument(
        "--a-values",
        type=lambda s: [float(x) for x in s.split(",")],
        default=[1e-1, 3e-2, 1e-2, 3e-3, 1e-3],
    )
    parser.add_argument("--out-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()

    records = run_search(args)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.out_dir / "classical_probe_results.json"
    csv_path = args.out_dir / "classical_probe_results.csv"

    with json_path.open("w", encoding="utf-8") as f:
        json.dump([asdict(r) for r in records], f, indent=2)

    fieldnames = [
        "n",
        "k",
        "a",
        "eta",
        "defect",
        "ratio_sqrt",
        "ratio_linear",
        "rank",
        "eig_cond",
        "trial",
        "seed",
    ]
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in records:
            row = asdict(r)
            writer.writerow({key: row[key] for key in fieldnames})

    print(f"records: {len(records)}")
    print(f"json: {json_path}")
    print(f"csv: {csv_path}")
    if records:
        by_linear = sorted(records, key=lambda r: r.ratio_linear, reverse=True)[:10]
        by_sqrt = sorted(records, key=lambda r: r.ratio_sqrt, reverse=True)[:10]
        print("\nTop ratio defect/eta:")
        for r in by_linear:
            print(
                f"n={r.n} k={r.k} a={r.a:g} eta={r.eta:.6g} "
                f"def={r.defect:.6g} def/eta={r.ratio_linear:.6g} "
                f"def/sqrt(eta)={r.ratio_sqrt:.6g} trial={r.trial}"
            )
        print("\nTop ratio defect/sqrt(eta):")
        for r in by_sqrt:
            print(
                f"n={r.n} k={r.k} a={r.a:g} eta={r.eta:.6g} "
                f"def={r.defect:.6g} def/eta={r.ratio_linear:.6g} "
                f"def/sqrt(eta)={r.ratio_sqrt:.6g} trial={r.trial}"
            )


if __name__ == "__main__":
    main()
