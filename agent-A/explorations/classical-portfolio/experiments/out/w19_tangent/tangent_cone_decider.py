#!/usr/bin/env python3
"""
Numerical tangent-cone decider for the H-M normal-form linear law.

The script samples stochastic idempotent H-M strata, builds the exact linear
tangent equations

    P0 A + A P0 = A,        A 1 = 0,

and solves LPs for the recurrent-hull upper derivative D(A).  D(A) is an
upper bound for the limsup height derivative because, along exact arcs, the
visible hull contains the recurrent row hull to first order.

The LPs first test the dangerous cone ddelta(A)=0.  A positive optimum there
would be an analytic-arc counterexample seed.  If that cone is clean, the same
LPs measure max D(A) with ddelta(A)<=1 and ||A||_infty<=1.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import os
import time
from dataclasses import dataclass

import numpy as np
from scipy.optimize import linprog


@dataclass
class HMStratum:
    n: int
    k: int
    blocks: list[list[int]]
    transients: list[int]
    pi: list[np.ndarray]
    alpha: dict[int, np.ndarray]
    P0: np.ndarray


def dirichlet_positive(rng: np.random.Generator, m: int, floor: float = 0.05) -> np.ndarray:
    x = rng.gamma(1.0, 1.0, size=m)
    x = x / x.sum()
    if floor > 0 and m > 1:
        x = (1.0 - m * floor) * x + floor
    return x / x.sum()


def random_partition(rng: np.random.Generator, n: int, k: int) -> tuple[list[list[int]], list[int]]:
    # Give each recurrent block one state, then distribute the remaining states
    # between recurrent blocks and the transient set.
    labels = list(range(n))
    rng.shuffle(labels)
    blocks = [[labels.pop()] for _ in range(k)]
    transients: list[int] = []
    for idx in labels:
        if rng.random() < 0.45:
            transients.append(idx)
        else:
            blocks[int(rng.integers(k))].append(idx)
    blocks = [sorted(b) for b in blocks]
    transients = sorted(transients)
    return blocks, transients


def make_hm(
    blocks: list[list[int]],
    transients: list[int],
    rng: np.random.Generator,
    boundary_alpha_prob: float = 0.55,
) -> HMStratum:
    n = sum(len(b) for b in blocks) + len(transients)
    k = len(blocks)
    pi: list[np.ndarray] = []
    P0 = np.zeros((n, n))
    for s, block in enumerate(blocks):
        p = dirichlet_positive(rng, len(block), floor=min(0.03, 0.4 / max(1, len(block))))
        pi.append(p)
        row = np.zeros(n)
        row[block] = p
        for i in block:
            P0[i] = row
    alpha: dict[int, np.ndarray] = {}
    for i in transients:
        if rng.random() < boundary_alpha_prob and k > 1:
            support_size = int(rng.integers(1, k + 1))
            support = rng.choice(k, size=support_size, replace=False)
            a = np.zeros(k)
            vals = dirichlet_positive(rng, support_size, floor=0.0)
            a[support] = vals
        else:
            a = dirichlet_positive(rng, k, floor=0.0)
        alpha[i] = a
        row = np.zeros(n)
        for s, block in enumerate(blocks):
            row[block] = a[s] * pi[s]
        P0[i] = row
    return HMStratum(n=n, k=k, blocks=blocks, transients=transients, pi=pi, alpha=alpha, P0=P0)


def deterministic_cases() -> list[HMStratum]:
    rng = np.random.default_rng(123)
    cases: list[HMStratum] = []

    # n=3,k=2 model with two singleton recurrent blocks and one transient.
    for a in (0.0, 0.2, 0.5, 0.8, 1.0):
        blocks = [[0], [1]]
        trans = [2]
        st = make_hm(blocks, trans, rng, boundary_alpha_prob=0.0)
        st.pi = [np.array([1.0]), np.array([1.0])]
        st.alpha = {2: np.array([a, 1.0 - a])}
        P = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [a, 1.0 - a, 0.0]])
        st.P0 = P
        cases.append(st)

    # A larger boundary-support case designed to stress transient rows on a face.
    blocks = [[0, 1], [2], [3]]
    trans = [4, 5]
    st = make_hm(blocks, trans, rng, boundary_alpha_prob=1.0)
    st.pi = [np.array([0.37, 0.63]), np.array([1.0]), np.array([1.0])]
    st.alpha = {4: np.array([1.0, 0.0, 0.0]), 5: np.array([0.25, 0.75, 0.0])}
    P = np.zeros((6, 6))
    for i in blocks[0]:
        P[i, blocks[0]] = st.pi[0]
    P[2, 2] = 1.0
    P[3, 3] = 1.0
    for i, a in st.alpha.items():
        P[i, blocks[0]] = a[0] * st.pi[0]
        P[i, blocks[1]] = a[1] * st.pi[1]
        P[i, blocks[2]] = a[2] * st.pi[2]
    st.P0 = P
    cases.append(st)
    return cases


def flat(i: int, j: int, n: int) -> int:
    return i * n + j


def tangent_equalities(P0: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    n = P0.shape[0]
    rows = []
    rhs = []
    for i in range(n):
        for j in range(n):
            row = np.zeros(n * n)
            for l in range(n):
                row[flat(l, j, n)] += P0[i, l]
                row[flat(i, l, n)] += P0[l, j]
            row[flat(i, j, n)] -= 1.0
            rows.append(row)
            rhs.append(0.0)
    for i in range(n):
        row = np.zeros(n * n)
        for j in range(n):
            row[flat(i, j, n)] = 1.0
        rows.append(row)
        rhs.append(0.0)
    return np.array(rows), np.array(rhs)


def active_positions(P0: np.ndarray, tol: float = 1e-10) -> list[tuple[int, int]]:
    n = P0.shape[0]
    return [(i, j) for i in range(n) for j in range(n) if abs(P0[i, j]) <= tol]


def gamma_coeff(st: HMStratum, row_i: int, q: int) -> np.ndarray:
    """Linear coefficients of Gamma_q(A_i), as a vector in flat A variables."""
    n = st.n
    coeff = np.zeros(n * n)
    for j in st.blocks[q]:
        coeff[flat(row_i, j, n)] += 1.0
    for j in st.transients:
        coeff[flat(row_i, j, n)] += st.alpha[j][q]
    return coeff


def lp_for_row_subset(
    st: HMStratum,
    row_i: int,
    neg_subset: tuple[int, ...],
    budget: float,
    norm_bound: float,
) -> dict:
    """Maximize 2*sum_{q in neg_subset} -Gamma_iq under a fixed sign chamber."""
    n = st.n
    base_vars = n * n
    active = active_positions(st.P0)
    u_offset = base_vars
    num_vars = base_vars + len(active)

    c = np.zeros(num_vars)
    for q in neg_subset:
        c[:base_vars] += 2.0 * gamma_coeff(st, row_i, q)
    # linprog minimizes; c above is 2 Gamma, so min = - max 2(-Gamma).

    Aeq0, beq = tangent_equalities(st.P0)
    A_eq = np.zeros((Aeq0.shape[0], num_vars))
    A_eq[:, :base_vars] = Aeq0

    Aub = []
    bub = []

    # Active negative-mass epigraph: u_ij >= -A_ij, u_ij >= 0,
    # and every row's active u-sum <= budget.
    active_by_row: dict[int, list[int]] = {i: [] for i in range(n)}
    for idx, (i, j) in enumerate(active):
        active_by_row[i].append(idx)
        row = np.zeros(num_vars)
        row[flat(i, j, n)] = -1.0
        row[u_offset + idx] = -1.0
        Aub.append(row)
        bub.append(0.0)
    for i in range(n):
        row = np.zeros(num_vars)
        for idx in active_by_row[i]:
            row[u_offset + idx] = 1.0
        Aub.append(row)
        bub.append(budget)

    # Sign chamber for the selected outside-support Gamma coordinates.
    support = set(np.flatnonzero(st.alpha[row_i] > 1e-10))
    outside = [q for q in range(st.k) if q not in support]
    neg_set = set(neg_subset)
    for q in outside:
        coeff = gamma_coeff(st, row_i, q)
        row = np.zeros(num_vars)
        if q in neg_set:
            row[:base_vars] = coeff
            Aub.append(row)
            bub.append(0.0)  # Gamma <= 0
        else:
            row[:base_vars] = -coeff
            Aub.append(row)
            bub.append(0.0)  # Gamma >= 0

    bounds = [(-norm_bound, norm_bound)] * base_vars + [(0.0, None)] * len(active)
    res = linprog(
        c,
        A_ub=np.array(Aub) if Aub else None,
        b_ub=np.array(bub) if bub else None,
        A_eq=A_eq,
        b_eq=beq,
        bounds=bounds,
        method="highs",
    )
    if not res.success:
        return {"success": False, "status": int(res.status), "message": res.message}
    A = res.x[:base_vars].reshape((n, n))
    value = -float(res.fun)
    gammas = [float(gamma_coeff(st, row_i, q) @ res.x[:base_vars]) for q in range(st.k)]
    active_neg_by_row = []
    for i in range(n):
        s = 0.0
        for j in range(n):
            if abs(st.P0[i, j]) <= 1e-10:
                s += max(-A[i, j], 0.0)
        active_neg_by_row.append(s)
    return {
        "success": True,
        "value": value,
        "A": A,
        "gammas": gammas,
        "ddelta": float(max(active_neg_by_row) if active_neg_by_row else 0.0),
        "active_neg_by_row": active_neg_by_row,
        "max_abs_A": float(np.max(np.abs(A))),
    }


def solve_stratum(st: HMStratum, budget: float, norm_bound: float) -> dict:
    best = {
        "value": -math.inf,
        "row": None,
        "neg_subset": None,
        "gammas": None,
        "ddelta": None,
        "A": None,
    }
    for i in st.transients:
        support = set(np.flatnonzero(st.alpha[i] > 1e-10))
        outside = [q for q in range(st.k) if q not in support]
        for r in range(len(outside) + 1):
            for subset in itertools.combinations(outside, r):
                rec = lp_for_row_subset(st, i, subset, budget=budget, norm_bound=norm_bound)
                if rec.get("success") and rec["value"] > best["value"] + 1e-9:
                    best.update(
                        {
                            "value": rec["value"],
                            "row": i,
                            "neg_subset": list(subset),
                            "gammas": rec["gammas"],
                            "ddelta": rec["ddelta"],
                            "A": rec["A"],
                            "active_neg_by_row": rec["active_neg_by_row"],
                            "max_abs_A": rec["max_abs_A"],
                        }
                    )
    if best["value"] == -math.inf:
        best["value"] = 0.0
    return best


def tangent_residual(P0: np.ndarray, A: np.ndarray) -> float:
    return float(max(np.max(np.abs(P0 @ A + A @ P0 - A)), np.max(np.abs(A @ np.ones(P0.shape[0])))))


def summarize_stratum(st: HMStratum, idx: int, norm_bound: float) -> dict:
    zero = solve_stratum(st, budget=0.0, norm_bound=norm_bound)
    one = solve_stratum(st, budget=1.0, norm_bound=norm_bound)
    rec = {
        "idx": idx,
        "n": st.n,
        "k": st.k,
        "blocks": st.blocks,
        "transients": st.transients,
        "alpha": {str(i): st.alpha[i].tolist() for i in st.transients},
        "zero_budget_value": float(max(0.0, zero["value"])),
        "budget1_value": float(max(0.0, one["value"])),
        "budget1_row": one["row"],
        "budget1_neg_subset": one["neg_subset"],
        "budget1_gammas": one["gammas"],
        "budget1_ddelta": one["ddelta"],
        "budget1_max_abs_A": one.get("max_abs_A"),
        "idem_residual": float(np.max(np.abs(st.P0 @ st.P0 - st.P0))),
        "row_sum_residual": float(np.max(np.abs(st.P0 @ np.ones(st.n) - 1.0))),
    }
    if one.get("A") is not None:
        A = one["A"]
        rec["budget1_tangent_residual"] = tangent_residual(st.P0, A)
        rec["budget1_A"] = A.tolist()
    if zero.get("A") is not None and zero["value"] > 1e-8:
        rec["counterexample_seed_A"] = zero["A"].tolist()
        rec["counterexample_seed_row"] = zero["row"]
        rec["counterexample_seed_gammas"] = zero["gammas"]
        rec["counterexample_seed_tangent_residual"] = tangent_residual(st.P0, zero["A"])
    return rec


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=80)
    parser.add_argument("--seed", type=int, default=19019)
    parser.add_argument("--norm-bound", type=float, default=1.0)
    parser.add_argument("--outdir", default="out")
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    rng = np.random.default_rng(args.seed)
    strata = deterministic_cases()
    for _ in range(args.samples):
        k = int(rng.integers(2, 6))
        n = int(rng.integers(k + 1, min(11, k + 6)))
        blocks, trans = random_partition(rng, n, k)
        if not trans:
            # Force at least one transient row because recurrent rows have zero height
            # derivative relative to the recurrent hull.
            donor = max(range(k), key=lambda s: len(blocks[s]))
            trans = [blocks[donor].pop()]
        strata.append(make_hm(blocks, trans, rng))

    t0 = time.time()
    records = []
    for idx, st in enumerate(strata):
        rec = summarize_stratum(st, idx, args.norm_bound)
        records.append(rec)
        print(
            f"[{idx:03d}] n={rec['n']} k={rec['k']} t={len(rec['transients'])} "
            f"zero={rec['zero_budget_value']:.3e} budget1={rec['budget1_value']:.6f}",
            flush=True,
        )

    vals = np.array([r["budget1_value"] for r in records], dtype=float)
    zeros = np.array([r["zero_budget_value"] for r in records], dtype=float)
    summary = {
        "created": time.strftime("%Y-%m-%d %H:%M:%S"),
        "seed": args.seed,
        "samples_random": args.samples,
        "samples_total": len(records),
        "norm": "entrywise infinity",
        "norm_bound": args.norm_bound,
        "zero_budget_max": float(zeros.max()) if len(zeros) else 0.0,
        "budget1_min": float(vals.min()) if len(vals) else 0.0,
        "budget1_median": float(np.median(vals)) if len(vals) else 0.0,
        "budget1_mean": float(vals.mean()) if len(vals) else 0.0,
        "budget1_p90": float(np.quantile(vals, 0.90)) if len(vals) else 0.0,
        "budget1_p99": float(np.quantile(vals, 0.99)) if len(vals) else 0.0,
        "budget1_max": float(vals.max()) if len(vals) else 0.0,
        "counterexample_count": int(np.sum(zeros > 1e-8)),
        "elapsed_s": time.time() - t0,
    }
    out = {"summary": summary, "records": records}
    json_path = os.path.join(args.outdir, "tangent_decider_summary.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    txt_path = os.path.join(args.outdir, "tangent_decider_summary.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write("tangent-cone decider summary\n")
        for key, val in summary.items():
            f.write(f"{key}: {val}\n")
        f.write("\ntop budget1 strata\n")
        for rec in sorted(records, key=lambda r: r["budget1_value"], reverse=True)[:10]:
            f.write(
                f"idx={rec['idx']} n={rec['n']} k={rec['k']} t={len(rec['transients'])} "
                f"zero={rec['zero_budget_value']:.6g} budget1={rec['budget1_value']:.6g} "
                f"row={rec['budget1_row']} neg_subset={rec['budget1_neg_subset']} "
                f"gammas={rec['budget1_gammas']}\n"
            )
    print(json.dumps(summary, indent=2), flush=True)
    print(f"saved {json_path} and {txt_path}", flush=True)


if __name__ == "__main__":
    main()
