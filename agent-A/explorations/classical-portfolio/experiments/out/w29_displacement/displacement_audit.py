#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

import numpy as np


ROOT = Path("/home/tobias/Projects/almost-idempotent-positive-maps")
CP = ROOT / "agent-A/explorations/classical-portfolio"
OUT = Path("/tmp/codex-sigma-wall/w29_displacement")


def scalar(x):
    if isinstance(x, (int, float)):
        return float(x)
    if isinstance(x, str):
        return float(Fraction(x))
    if isinstance(x, dict):
        if "str" in x:
            return float(Fraction(x["str"]))
        return float(Fraction(int(x["num"]), int(x["den"])))
    raise TypeError(type(x))


def matrix(obj):
    return np.array([[scalar(x) for x in row] for row in obj], dtype=float)


def row_l1_norm(A):
    return np.sum(np.abs(A), axis=1)


def neg_mass_rows(P):
    return np.maximum(-P, 0.0).sum(axis=1)


def rank(P, tol=1e-10):
    return int(np.linalg.matrix_rank(P, tol=tol))


def volume_score(rows):
    G = rows @ rows.T
    sign, logdet = np.linalg.slogdet(G)
    if sign <= 0:
        return -np.inf
    return 0.5 * logdet


def maxvol_pivots(P):
    n = P.shape[0]
    k = rank(P)
    best = None
    best_score = -np.inf
    for inds in itertools.combinations(range(n), k):
        rows = P[list(inds)]
        if rank(rows) < k:
            continue
        score = volume_score(rows)
        if score > best_score + 1e-12:
            best_score = score
            best = list(inds)
    if best is None:
        raise RuntimeError("no row basis found")
    return best


def coordinates(P, pivots):
    basis = P[pivots]
    coeffs = []
    for row in P:
        c, *_ = np.linalg.lstsq(basis.T, row, rcond=None)
        coeffs.append(c)
    return np.array(coeffs)


def free_identity_row(P, u):
    row = P[u]
    d = P - P[u]
    signed = row @ d
    pos_vec = np.maximum(row, 0.0) @ d
    neg_vec = np.maximum(-row, 0.0) @ d
    return {
        "signed_l1": float(np.sum(np.abs(signed))),
        "pos_minus_neg_l1": float(np.sum(np.abs(pos_vec - neg_vec))),
        "pos_vec_l1": float(np.sum(np.abs(pos_vec))),
        "neg_vec_l1": float(np.sum(np.abs(neg_vec))),
    }


def row_transport_metrics(P, u):
    row = P[u]
    dist = np.sum(np.abs(P - P[u]), axis=1)
    pos = np.maximum(row, 0.0)
    T = float(pos @ dist)
    M2 = float(pos @ (dist * dist))
    return {
        "row": int(u),
        "neg_mass": float(np.maximum(-row, 0.0).sum()),
        "positive_mass": float(pos.sum()),
        "transport_T": T,
        "second_moment": M2,
        "max_successor_distance": float(dist.max()),
        "free_identity": free_identity_row(P, u),
    }


def metrics(name, P):
    P = np.asarray(P, dtype=float)
    delta = float(neg_mass_rows(P).max())
    pivots = maxvol_pivots(P)
    coeffs = coordinates(P, pivots)
    rows = [row_transport_metrics(P, u) for u in range(P.shape[0])]
    for rec in rows:
        rec["T_over_delta"] = (
            float(rec["transport_T"] / delta) if delta > 0 else ("inf" if rec["transport_T"] > 1e-12 else 0.0)
        )
        rec["M2_over_delta"] = (
            float(rec["second_moment"] / delta) if delta > 0 else ("inf" if rec["second_moment"] > 1e-12 else 0.0)
        )
    pivot_set = set(pivots)
    pivot_rows = [rec for rec in rows if rec["row"] in pivot_set]
    return {
        "name": name,
        "n": int(P.shape[0]),
        "rank": rank(P),
        "delta": delta,
        "rowsum_inf": float(np.max(np.abs(P.sum(axis=1) - 1.0))),
        "idempotence_inf": float(np.max(np.abs(P @ P - P))),
        "pivots": [int(i) for i in pivots],
        "max_abs_coeff": float(np.max(np.abs(coeffs))),
        "max_coeff_neg_mass": float(np.maximum(-coeffs, 0.0).sum(axis=1).max()),
        "max_row_T": max((r["transport_T"] for r in rows), default=0.0),
        "max_row_T_over_delta": max_mixed((r["T_over_delta"] for r in rows), default=0.0),
        "max_pivot_T": max((r["transport_T"] for r in pivot_rows), default=0.0),
        "max_pivot_T_over_delta": max_mixed((r["T_over_delta"] for r in pivot_rows), default=0.0),
        "max_pivot_second_moment_over_delta": max_mixed((r["M2_over_delta"] for r in pivot_rows), default=0.0),
        "rows": rows,
    }


def arbitrary_row_delta_zero_counterexample():
    return np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.5, 0.5, 0.0],
        ]
    )


def leakage_family(delta):
    eta = np.sqrt(delta)
    mass = delta / eta
    B = np.array(
        [
            [1.0 - mass + delta, -delta, mass],
            [0.0, 1.0, 0.0],
        ]
    )
    L = np.array(
        [
            [1.0, 0.0],
            [0.0, 1.0],
            [1.0 - eta, eta],
        ]
    )
    return L @ B


def split_block(eps):
    q1 = np.array([0.5, 0.5 + eps, -eps])
    q2 = np.array([1.0 / (2.0 * (1.0 + 2.0 * eps)), 0.5, eps / (1.0 + 2.0 * eps)])
    q3 = np.array([0.0, 0.0, 1.0])
    return np.vstack([q1, q2, q3])


def leftcone(eps):
    return np.array(
        [
            [1 - eps / 3, -eps / 3, -eps / 3, eps],
            [eps / 3, 1 + eps / 3, eps / 3, -eps],
            [0.0, 0.0, 1.0, 0.0],
            [1 / 3, 1 / 3, 1 / 3, 0.0],
        ]
    )


def transverse_pair(a, m):
    """Exact 5x5 LB family with coordinates e0 +/- a(e1-e2).

    The symmetric left inverse is the LP optimum found in the stress search:
    c = a/(1+4a^2).  For small a, delta ~ a and pivot transport ~ 2ma.
    """
    c = a / (1.0 + 4.0 * a * a)
    B0 = np.array([1.0 - m, 0.0, 0.0, m / 2.0, m / 2.0])
    B1 = np.array([0.0, 1.0 - 2.0 * a * c, 2.0 * a * c, c, -c])
    B2 = np.array([0.0, 2.0 * a * c, 1.0 - 2.0 * a * c, -c, c])
    B = np.vstack([B0, B1, B2])
    L = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [1.0, a, -a],
            [1.0, -a, a],
        ]
    )
    return L @ B


def load_w16():
    path = CP / "experiments/out/w16_cert_audit/w16_best_rational_instance.json"
    return matrix(json.loads(path.read_text())["P_frac"])


def load_w17(fname):
    path = CP / f"experiments/out/w17_cert_audit/{fname}"
    return matrix(json.loads(path.read_text())["P"])


def random_hm(n, k, rng):
    blocks = [[] for _ in range(k)]
    for s in range(k):
        blocks[s].append(s)
    for j in range(k, n):
        blocks[int(rng.integers(k))].append(j)
    P = np.zeros((n, n))
    laws = []
    for block in blocks:
        weights = rng.random(len(block)) + 0.2
        weights = weights / weights.sum()
        law = np.zeros(n)
        law[block] = weights
        laws.append(law)
    for s, block in enumerate(blocks):
        for i in block:
            P[i] = laws[s]
    return P


def rowsum_zero_matrix(n, rng):
    K = rng.normal(size=(n, n))
    K -= K.mean(axis=1, keepdims=True)
    norm = np.linalg.norm(K, ord=np.inf)
    return K / norm


def conjugate_to_delta(P0, target_delta, rng):
    K = rowsum_zero_matrix(P0.shape[0], rng)

    def make(t):
        S = np.eye(P0.shape[0]) + t * K
        return S @ P0 @ np.linalg.inv(S)

    lo, hi = 0.0, 1.0
    for _ in range(40):
        if neg_mass_rows(make(hi)).max() >= target_delta:
            break
        hi *= 2.0
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if neg_mass_rows(make(mid)).max() < target_delta:
            lo = mid
        else:
            hi = mid
    return make(hi)


def summarize(records):
    lines = []
    for rec in records:
        if rec["name"] == "random_small_delta_similarity_summary":
            samples = rec["samples"]
            pivot_vals = sorted(float(s["max_pivot_T_over_delta"]) for s in samples)
            row_vals = sorted(float(s["max_row_T_over_delta"]) for s in samples)
            lines.append(
                "random_small_delta_similarity_summary: "
                f"samples={len(samples)} "
                f"max_pivot_T_over_delta={max(s['max_pivot_T_over_delta'] for s in samples):.6g} "
                f"median_pivot_T_over_delta={quantile(pivot_vals, 0.5):.6g} "
                f"p90_pivot_T_over_delta={quantile(pivot_vals, 0.9):.6g} "
                f"max_row_T_over_delta={max_num(s['max_row_T_over_delta'] for s in samples):.6g} "
                f"median_row_T_over_delta={quantile(row_vals, 0.5):.6g} "
                f"p90_row_T_over_delta={quantile(row_vals, 0.9):.6g}"
            )
            continue
        lines.append(
            f"{rec['name']}: n={rec['n']} rank={rec['rank']} delta={rec['delta']:.8g} "
            f"pivots={rec['pivots']} max_pivot_T/delta={fmt(rec['max_pivot_T_over_delta'])} "
            f"max_row_T/delta={fmt(rec['max_row_T_over_delta'])} "
            f"max_pivot_M2/delta={fmt(rec['max_pivot_second_moment_over_delta'])} "
            f"max_coeff_neg={rec['max_coeff_neg_mass']:.6g} "
            f"idem={rec['idempotence_inf']:.3g} rowsum={rec['rowsum_inf']:.3g}"
        )
    return "\n".join(lines) + "\n"


def max_num(values):
    out = 0.0
    for v in values:
        if isinstance(v, str):
            return float("inf")
        out = max(out, float(v))
    return out


def quantile(vals, q):
    if not vals:
        return 0.0
    idx = int(round(q * (len(vals) - 1)))
    return vals[idx]


def max_mixed(values, default=0.0):
    out = default
    for v in values:
        if isinstance(v, str):
            return v
        if isinstance(out, str):
            return out
        out = max(float(out), float(v))
    return out


def fmt(x):
    if isinstance(x, str):
        return x
    return f"{float(x):.6g}"


def main():
    records = []
    records.append(metrics("general_row_delta0_transient_counterexample", arbitrary_row_delta_zero_counterexample()))
    for delta in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
        records.append(metrics(f"w27_rank2_leakage_delta_{delta:g}", leakage_family(delta)))
    for eps in [1e-2, 1e-3, 1e-4, 1e-5]:
        records.append(metrics(f"split_block_eps_{eps:g}", split_block(eps)))
    for eps in [1e-2, 1e-3, 1e-4, 1e-5]:
        records.append(metrics(f"w19_leftcone_eps_{eps:g}", leftcone(eps)))
    for a in [0.02, 0.05, 0.1, 0.2]:
        records.append(metrics(f"transverse_pair_a_{a:g}_m_0.99", transverse_pair(a, 0.99)))
    records.append(metrics("w16_best_rational_above_corner", load_w16()))
    records.append(metrics("w17_main_rational_above_corner", load_w17("main_rational_instance.json")))
    records.append(metrics("w17_robust_rational_above_corner", load_w17("robust_rational_instance.json")))

    rng = np.random.default_rng(2901)
    samples = []
    for target in [1e-2, 1e-3, 1e-4]:
        for trial in range(12):
            P0 = random_hm(7, 3, rng)
            P = conjugate_to_delta(P0, target, rng)
            rec = metrics(f"random_similarity_delta_{target:g}_trial_{trial}", P)
            samples.append(
                {
                    "name": rec["name"],
                    "delta": rec["delta"],
                    "pivots": rec["pivots"],
                    "max_pivot_T_over_delta": rec["max_pivot_T_over_delta"],
                    "max_row_T_over_delta": rec["max_row_T_over_delta"],
                    "max_coeff_neg_mass": rec["max_coeff_neg_mass"],
                    "idempotence_inf": rec["idempotence_inf"],
                    "rowsum_inf": rec["rowsum_inf"],
                }
            )
    records.append({"name": "random_small_delta_similarity_summary", "samples": samples})

    (OUT / "displacement_numeric_results.json").write_text(json.dumps(records, indent=2, sort_keys=True))
    summary = summarize(records)
    (OUT / "displacement_numeric_summary.txt").write_text(summary)
    print(summary, end="")


if __name__ == "__main__":
    main()
