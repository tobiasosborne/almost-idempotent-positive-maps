#!/usr/bin/env python3
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path

import numpy as np


def neg_mass_rows(P):
    return np.maximum(-P, 0.0).sum(axis=1)


def rank(P, tol=1e-9):
    return int(np.linalg.matrix_rank(P, tol=tol))


def volume_score(rows):
    sign, logdet = np.linalg.slogdet(rows @ rows.T)
    return -np.inf if sign <= 0 else 0.5 * logdet


def maxvol_pivots(P):
    n = P.shape[0]
    k = rank(P)
    best = None
    best_score = -np.inf
    for inds in itertools.combinations(range(n), k):
        R = P[list(inds)]
        if rank(R) < k:
            continue
        score = volume_score(R)
        if score > best_score + 1e-11:
            best_score = score
            best = inds
    if best is None:
        raise RuntimeError("no basis")
    return list(best)


def coeffs(P, pivots):
    basis = P[pivots]
    return P @ basis.T @ np.linalg.inv(basis @ basis.T)


def sf_values(P, pivots):
    A = coeffs(P, pivots)
    vals = []
    tops = []
    for s, u in enumerate(pivots):
        E = []
        for j in range(P.shape[0]):
            mu = sum(max(-A[j, t], 0.0) for t in range(A.shape[1]) if t != s)
            E.append(max(mu - (1.0 - A[j, s]), 0.0))
        E = np.array(E)
        contrib = np.maximum(P[u], 0.0) * E
        vals.append(float(contrib.sum()))
        top = []
        for j in np.argsort(-contrib)[:5]:
            if contrib[j] > 1e-12:
                top.append(
                    {
                        "j": int(j),
                        "contrib": float(contrib[j]),
                        "Ppos": float(max(P[u, j], 0.0)),
                        "E": float(E[j]),
                        "coeff": [float(x) for x in A[j]],
                    }
                )
        tops.append(top)
    return vals, tops, A


def random_hm(n, k, rng):
    blocks = [[] for _ in range(k)]
    for s in range(k):
        blocks[s].append(s)
    for j in range(k, n):
        blocks[int(rng.integers(k))].append(j)
    P = np.zeros((n, n))
    for block in blocks:
        weights = rng.random(len(block)) + 0.1
        weights /= weights.sum()
        law = np.zeros(n)
        law[block] = weights
        for i in block:
            P[i] = law
    return P


def rowsum_zero_matrix(n, rng):
    K = rng.normal(size=(n, n))
    K -= K.mean(axis=1, keepdims=True)
    norm = np.linalg.norm(K, ord=np.inf)
    return K / norm


def conjugate_to_delta(P0, target, rng):
    K = rowsum_zero_matrix(P0.shape[0], rng)

    def make(t):
        S = np.eye(P0.shape[0]) + t * K
        return S @ P0 @ np.linalg.inv(S)

    lo, hi = 0.0, 1.0
    for _ in range(80):
        try:
            d = neg_mass_rows(make(hi)).max()
        except np.linalg.LinAlgError:
            d = np.inf
        if d >= target:
            break
        hi *= 2.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        try:
            d = neg_mass_rows(make(mid)).max()
        except np.linalg.LinAlgError:
            d = np.inf
        if d < target:
            lo = mid
        else:
            hi = mid
    return make(hi)


def audit(P, label):
    delta = float(neg_mass_rows(P).max())
    pivots = maxvol_pivots(P)
    vals, tops, A = sf_values(P, pivots)
    ratios = [v / delta if delta > 0 else (np.inf if v > 1e-12 else 0.0) for v in vals]
    s = int(np.argmax(ratios))
    return {
        "label": label,
        "n": int(P.shape[0]),
        "rank": rank(P),
        "delta": delta,
        "pivots": [int(x) for x in pivots],
        "best_s_pos": s,
        "best_pivot": int(pivots[s]),
        "best_sf": float(vals[s]),
        "best_sf_over_delta": float(ratios[s]),
        "idempotence_inf": float(np.max(np.abs(P @ P - P))),
        "rowsum_inf": float(np.max(np.abs(P.sum(axis=1) - 1.0))),
        "max_abs_coeff": float(np.max(np.abs(A))),
        "top": tops[s],
    }


def run(samples, seed):
    rng = np.random.default_rng(seed)
    records = []
    best = None
    configs = [(8, 3), (9, 4), (10, 4), (12, 5)]
    targets = [0.002, 0.005, 0.01, 0.02]
    for idx in range(samples):
        n, k = configs[idx % len(configs)]
        target = targets[(idx // len(configs)) % len(targets)]
        P0 = random_hm(n, k, rng)
        try:
            P = conjugate_to_delta(P0, target, rng)
            rec = audit(P, f"sample_{idx}_n{n}_k{k}_target{target:g}")
        except Exception as exc:  # numerical singular or rank issue
            rec = {"label": f"sample_{idx}", "failed": repr(exc)}
        records.append(rec)
        if rec.get("best_sf_over_delta") is not None and (
            best is None or rec["best_sf_over_delta"] > best["best_sf_over_delta"]
        ):
            best = rec
    return records, best


def summarize(records, best):
    good = [r for r in records if "best_sf_over_delta" in r]
    ratios = sorted(r["best_sf_over_delta"] for r in good)
    lines = [
        f"samples={len(records)} good={len(good)}",
        f"best={best['best_sf_over_delta']:.6g} label={best['label']} delta={best['delta']:.6g} pivots={best['pivots']}" if best else "best=None",
    ]
    if ratios:
        for q, name in [(0.5, "median"), (0.9, "p90"), (0.99, "p99")]:
            lines.append(f"{name}={ratios[min(len(ratios)-1, int(q*(len(ratios)-1)) )]:.6g}")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=240)
    parser.add_argument("--seed", type=int, default=20260612)
    parser.add_argument("--out-json", default="sf_random_results.json")
    parser.add_argument("--out-summary", default="sf_random_summary.txt")
    args = parser.parse_args()
    records, best = run(args.samples, args.seed)
    Path(args.out_json).write_text(json.dumps({"records": records, "best": best}, indent=2, sort_keys=True))
    summary = summarize(records, best)
    Path(args.out_summary).write_text(summary)
    print(summary, end="")


if __name__ == "__main__":
    main()
