#!/usr/bin/env python3
"""Qubit positive-map probe for the null-ideal term.

Representation:
  x = x0 I + v.sigma, with ||x|| = |x0| + ||v||_2.
  A unital self-adjoint map is represented as
      Phi(x0, v) = (x0 + t.v, M v).

The sufficient positivity check used for random perturbations is
  sup_{||u||=1} (||M u|| + |t.u|) <= 1.
The search constructs Phi_a=(1-a)Phi0+aPhi1, where Phi0 has t=0 and M an
orthogonal projection. This keeps Phi_a positive and nearly idempotent.
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
class QubitRecord:
    vector_rank: int
    a: float
    eta: float
    defect: float
    ratio_sqrt: float
    ratio_linear: float
    rank: int
    eig_cond: float
    positivity_margin_phi1: float
    trial: int
    seed: int
    t1: list[float]
    m1: list[list[float]]
    p_matrix: list[list[float]]
    r: list[float]
    s: list[float]


def herm_norm(x: Array) -> float:
    return float(abs(x[0]) + np.linalg.norm(x[1:]))


def jordan_product(x: Array, y: Array) -> Array:
    out = np.empty(4, dtype=float)
    out[0] = x[0] * y[0] + float(np.dot(x[1:], y[1:]))
    out[1:] = x[0] * y[1:] + y[0] * x[1:]
    return out


def square(x: Array) -> Array:
    out = np.empty(4, dtype=float)
    out[0] = x[0] * x[0] + float(np.dot(x[1:], x[1:]))
    out[1:] = 2.0 * x[0] * x[1:]
    return out


def map_matrix(t: Array, m: Array) -> Array:
    l_mat = np.zeros((4, 4), dtype=float)
    l_mat[0, 0] = 1.0
    l_mat[0, 1:] = t
    l_mat[1:, 1:] = m
    return l_mat


def sphere_point(theta: float, phi: float) -> Array:
    return np.array(
        [
            math.sin(theta) * math.cos(phi),
            math.sin(theta) * math.sin(phi),
            math.cos(theta),
        ],
        dtype=float,
    )


def sup_sphere(t: Array, m: Array, samples: int, rng: np.random.Generator) -> float:
    best = 0.0
    dirs = rng.normal(size=(samples, 3))
    dirs /= np.linalg.norm(dirs, axis=1)[:, None]
    vals = np.abs(dirs @ t) + np.linalg.norm(dirs @ m.T, axis=1)
    best = float(np.max(vals))

    def obj(z: Array) -> float:
        theta = math.pi * z[0]
        phi = 2.0 * math.pi * z[1]
        u = sphere_point(theta, phi)
        return -(abs(float(np.dot(t, u))) + float(np.linalg.norm(m @ u)))

    result = optimize.differential_evolution(
        obj,
        bounds=[(0.0, 1.0), (0.0, 1.0)],
        maxiter=35,
        popsize=10,
        polish=True,
        seed=int(rng.integers(0, 2**31 - 1)),
        tol=1e-8,
    )
    return max(best, -float(result.fun))


def eta_norm(diff: Array, rng: np.random.Generator) -> float:
    c = diff[0, 1:]
    n = diff[1:, 1:]
    return sup_sphere(c, n, samples=600, rng=rng)


def spectral_projection_near_one(l_mat: Array, threshold: float = 0.5) -> tuple[Array, int, float]:
    vals, vecs = linalg.eig(l_mat)
    mask = np.abs(vals - 1.0) < threshold
    rank = int(np.count_nonzero(mask))
    if rank == 0:
        raise ValueError("no near-one cluster")
    cond = float(np.linalg.cond(vecs))
    inv_vecs = linalg.inv(vecs)
    p = vecs[:, mask] @ inv_vecs[mask, :]
    p = np.real_if_close(p, tol=1000)
    if np.max(np.abs(np.imag(p))) > 1e-7:
        raise ValueError("complex spectral projection")
    return np.array(np.real(p), dtype=float), rank, cond


def range_basis(p: Array, tol: float = 1e-8) -> Array:
    u, svals, _ = linalg.svd(p)
    rank = int(np.count_nonzero(svals > tol))
    return np.array(u[:, :rank], dtype=float)


def normalized_range_vector(basis: Array, coeffs: Array) -> Array | None:
    x = basis @ coeffs
    norm = herm_norm(x)
    if norm < 1e-12:
        return None
    return x / norm


def defect_for_vectors(p: Array, r: Array, s: Array) -> float:
    raw = jordan_product(r, s)
    h = raw - p @ raw
    return herm_norm(p @ square(h))


def maximize_defect(
    p: Array, rng: np.random.Generator, samples: int, de_iters: int
) -> tuple[float, Array, Array]:
    basis = range_basis(p)
    rank = basis.shape[1]
    best = -1.0
    best_r = None
    best_s = None

    def eval_coeffs(z: Array) -> float:
        r = normalized_range_vector(basis, z[:rank])
        s = normalized_range_vector(basis, z[rank:])
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

    if de_iters > 0:
        result = optimize.differential_evolution(
            lambda z: -eval_coeffs(np.array(z, dtype=float)),
            bounds=[(-2.0, 2.0)] * (2 * rank),
            maxiter=de_iters,
            popsize=10,
            polish=True,
            tol=1e-8,
            seed=int(rng.integers(0, 2**31 - 1)),
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


def random_rotation(rng: np.random.Generator) -> Array:
    q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    if np.linalg.det(q) < 0:
        q[:, 0] *= -1
    return q


def random_positive_perturbation(rng: np.random.Generator) -> tuple[Array, Array, float]:
    t = rng.normal(size=3)
    t_norm = np.linalg.norm(t)
    tau = rng.uniform(0.0, 0.85)
    if t_norm > 0:
        t = t / t_norm * tau
    left = random_rotation(rng)
    right = random_rotation(rng)
    singular = rng.uniform(0.0, max(0.0, 1.0 - tau), size=3)
    m = left @ np.diag(singular) @ right.T
    # This should already be positive by ||M||+||t|| <= 1, but compute margin.
    margin = 1.0 - (float(np.linalg.norm(m, 2)) + float(np.linalg.norm(t)))
    return t, m, margin


def projection_m(rank: int) -> Array:
    m = np.zeros((3, 3), dtype=float)
    for i in range(rank):
        m[i, i] = 1.0
    return m


def run(args: argparse.Namespace) -> list[QubitRecord]:
    rng = np.random.default_rng(args.seed)
    records: list[QubitRecord] = []
    for vector_rank in args.vector_ranks:
        l0 = map_matrix(np.zeros(3), projection_m(vector_rank))
        for trial in range(args.trials):
            t1, m1, margin = random_positive_perturbation(rng)
            l1 = map_matrix(t1, m1)
            for a in args.a_values:
                l_mat = (1.0 - a) * l0 + a * l1
                diff = l_mat @ l_mat - l_mat
                eta = eta_norm(diff, rng)
                if eta <= 0 or eta > args.max_eta:
                    continue
                try:
                    p, rank, cond = spectral_projection_near_one(l_mat)
                except Exception:
                    continue
                if rank != vector_rank + 1 or cond > args.max_cond:
                    continue
                defect, r, s = maximize_defect(
                    p, rng, samples=args.samples, de_iters=args.de_iters
                )
                records.append(
                    QubitRecord(
                        vector_rank=vector_rank,
                        a=float(a),
                        eta=float(eta),
                        defect=float(defect),
                        ratio_sqrt=float(defect / math.sqrt(eta)),
                        ratio_linear=float(defect / eta),
                        rank=rank,
                        eig_cond=cond,
                        positivity_margin_phi1=margin,
                        trial=trial,
                        seed=args.seed,
                        t1=np.round(t1, 12).tolist(),
                        m1=np.round(m1, 12).tolist(),
                        p_matrix=np.round(p, 12).tolist(),
                        r=np.round(r, 12).tolist(),
                        s=np.round(s, 12).tolist(),
                    )
                )
    return records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20260605)
    parser.add_argument("--vector-ranks", type=lambda s: [int(x) for x in s.split(",")], default=[1, 2])
    parser.add_argument("--trials", type=int, default=40)
    parser.add_argument("--samples", type=int, default=400)
    parser.add_argument("--de-iters", type=int, default=20)
    parser.add_argument("--max-eta", type=float, default=0.25)
    parser.add_argument("--max-cond", type=float, default=1e6)
    parser.add_argument(
        "--a-values",
        type=lambda s: [float(x) for x in s.split(",")],
        default=[1e-1, 3e-2, 1e-2, 3e-3, 1e-3],
    )
    parser.add_argument("--out-dir", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()

    records = run(args)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.out_dir / "qubit_probe_results.json"
    csv_path = args.out_dir / "qubit_probe_results.csv"
    json_path.write_text(json.dumps([asdict(r) for r in records], indent=2), encoding="utf-8")
    with csv_path.open("w", encoding="utf-8", newline="") as f:
        fieldnames = [
            "vector_rank",
            "a",
            "eta",
            "defect",
            "ratio_sqrt",
            "ratio_linear",
            "rank",
            "eig_cond",
            "positivity_margin_phi1",
            "trial",
            "seed",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for rec in records:
            row = asdict(rec)
            writer.writerow({key: row[key] for key in fieldnames})

    print(f"records: {len(records)}")
    print(f"json: {json_path}")
    print(f"csv: {csv_path}")
    for key in ("ratio_linear", "ratio_sqrt"):
        print(f"\nTop {key}:")
        for r in sorted(records, key=lambda x: getattr(x, key), reverse=True)[:10]:
            print(
                f"vrank={r.vector_rank} a={r.a:g} eta={r.eta:.6g} "
                f"def={r.defect:.6g} def/eta={r.ratio_linear:.6g} "
                f"def/sqrt(eta)={r.ratio_sqrt:.6g} trial={r.trial}"
            )


if __name__ == "__main__":
    main()
