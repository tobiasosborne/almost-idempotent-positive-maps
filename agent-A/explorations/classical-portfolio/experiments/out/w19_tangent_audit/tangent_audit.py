#!/usr/bin/env python3
"""Independent audit for the w19 tangent-cone lemma.

This script deliberately does not import or execute the claimant's decider.
It rebuilds H-M normal forms, tangent LPs, the frozen height derivative, and
small exact arcs in the idempotent variety.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog


TOL = 1e-9


@dataclass
class Stratum:
    name: str
    blocks: list[list[int]]
    transients: list[int]
    pis: list[np.ndarray]
    alpha_transient: dict[int, np.ndarray]

    @property
    def n(self) -> int:
        return sum(len(b) for b in self.blocks) + len(self.transients)

    @property
    def k(self) -> int:
        return len(self.blocks)


def embedded_pi(n: int, block: list[int], pi_local: np.ndarray) -> np.ndarray:
    row = np.zeros(n)
    row[block] = pi_local
    return row


def build_p0(st: Stratum) -> np.ndarray:
    n = st.n
    P = np.zeros((n, n))
    pi_full = [embedded_pi(n, block, pi) for block, pi in zip(st.blocks, st.pis)]
    for s, block in enumerate(st.blocks):
        for i in block:
            P[i] = pi_full[s]
    for i in st.transients:
        alpha = st.alpha_transient[i]
        P[i] = sum(alpha[s] * pi_full[s] for s in range(st.k))
    return P


def row_alphas(st: Stratum) -> np.ndarray:
    alpha = np.zeros((st.n, st.k))
    for s, block in enumerate(st.blocks):
        for i in block:
            alpha[i, s] = 1.0
    for i in st.transients:
        alpha[i] = st.alpha_transient[i]
    return alpha


def gamma_weights(st: Stratum) -> np.ndarray:
    """W[j, q] so Gamma_q(x) = sum_j W[j, q] x_j."""
    W = np.zeros((st.n, st.k))
    for q, block in enumerate(st.blocks):
        W[block, q] = 1.0
    for j in st.transients:
        W[j] = st.alpha_transient[j]
    return W


def active_zero_mask(P0: np.ndarray) -> np.ndarray:
    return P0 <= 1e-12


def tangent_equalities(P0: np.ndarray, total_vars: int) -> tuple[np.ndarray, np.ndarray]:
    n = P0.shape[0]
    rows: list[np.ndarray] = []
    rhs: list[float] = []
    for i in range(n):
        for j in range(n):
            row = np.zeros(total_vars)
            for a in range(n):
                row[a * n + j] += P0[i, a]
            for b in range(n):
                row[i * n + b] += P0[b, j]
            row[i * n + j] -= 1.0
            rows.append(row)
            rhs.append(0.0)
    for i in range(n):
        row = np.zeros(total_vars)
        for j in range(n):
            row[i * n + j] = 1.0
        rows.append(row)
        rhs.append(0.0)
    return np.array(rows), np.array(rhs)


def gamma_coeff(n: int, W: np.ndarray, row_i: int, q: int, total_vars: int) -> np.ndarray:
    coeff = np.zeros(total_vars)
    for j in range(n):
        coeff[row_i * n + j] = W[j, q]
    return coeff


def solve_one_lp(
    st: Stratum,
    budget: float,
    norm_bound: float,
    target_row: int,
    neg_subset: tuple[int, ...],
    sign_forbidden: list[int],
) -> dict | None:
    P0 = build_p0(st)
    n = st.n
    W = gamma_weights(st)
    zeros = active_zero_mask(P0)
    active_pairs = [(i, j) for i in range(n) for j in range(n) if zeros[i, j]]
    u_offset = n * n
    total_vars = n * n + len(active_pairs)

    Aeq, beq = tangent_equalities(P0, total_vars)
    Aub: list[np.ndarray] = []
    bub: list[float] = []

    # u_ij >= -A_ij for active zero entries.
    for u_idx, (i, j) in enumerate(active_pairs):
        row = np.zeros(total_vars)
        row[i * n + j] = -1.0
        row[u_offset + u_idx] = -1.0
        Aub.append(row)
        bub.append(0.0)

    # Per-row negative active-zero budget.
    for i in range(n):
        row = np.zeros(total_vars)
        for u_idx, (ii, _j) in enumerate(active_pairs):
            if ii == i:
                row[u_offset + u_idx] = 1.0
        Aub.append(row)
        bub.append(budget)

    neg_set = set(neg_subset)
    for q in sign_forbidden:
        coeff = gamma_coeff(n, W, target_row, q, total_vars)
        if q in neg_set:
            Aub.append(coeff)
            bub.append(0.0)
        else:
            Aub.append(-coeff)
            bub.append(0.0)

    c = np.zeros(total_vars)
    for q in neg_subset:
        c += 2.0 * gamma_coeff(n, W, target_row, q, total_vars)

    bounds = [(-norm_bound, norm_bound)] * (n * n) + [(0.0, None)] * len(active_pairs)
    res = linprog(
        c,
        A_ub=np.array(Aub) if Aub else None,
        b_ub=np.array(bub) if bub else None,
        A_eq=Aeq,
        b_eq=beq,
        bounds=bounds,
        method="highs",
    )
    if not res.success:
        return None
    A = res.x[: n * n].reshape((n, n))
    value = max(0.0, -float(res.fun))
    gammas = [float(np.dot(W[:, q], A[target_row])) for q in range(st.k)]
    return {
        "value": value,
        "A": A,
        "row": target_row,
        "neg_subset": list(neg_subset),
        "gammas": gammas,
    }


def frozen_D(st: Stratum, A: np.ndarray) -> float:
    alpha = row_alphas(st)
    W = gamma_weights(st)
    best = 0.0
    for i in range(st.n):
        forbidden = [q for q in range(st.k) if alpha[i, q] <= 1e-10]
        val = 0.0
        for q in forbidden:
            gamma = float(np.dot(W[:, q], A[i]))
            val += max(-gamma, 0.0)
        best = max(best, 2.0 * val)
    return best


def dot_delta(st: Stratum, A: np.ndarray) -> float:
    P0 = build_p0(st)
    zeros = active_zero_mask(P0)
    vals = []
    for i in range(st.n):
        vals.append(float(np.maximum(-A[i][zeros[i]], 0.0).sum()))
    return max(vals) if vals else 0.0


def tangent_residual(P0: np.ndarray, A: np.ndarray) -> float:
    return float(
        max(
            np.max(np.abs(P0 @ A + A @ P0 - A)),
            np.max(np.abs(A @ np.ones(P0.shape[0]))),
        )
    )


def solve_stratum(st: Stratum, budget: float, norm_bound: float) -> dict:
    alpha = row_alphas(st)
    best: dict | None = None
    lp_count = 0
    for i in range(st.n):
        forbidden = [q for q in range(st.k) if alpha[i, q] <= 1e-10]
        for r in range(len(forbidden) + 1):
            for neg_subset in itertools.combinations(forbidden, r):
                lp_count += 1
                out = solve_one_lp(st, budget, norm_bound, i, neg_subset, forbidden)
                if out is not None and (best is None or out["value"] > best["value"] + 1e-9):
                    best = out
    if best is None:
        return {"value": math.nan, "lp_count": lp_count}
    P0 = build_p0(st)
    A = best["A"]
    return {
        "value": float(best["value"]),
        "lp_count": lp_count,
        "row": int(best["row"]),
        "neg_subset": best["neg_subset"],
        "gammas": best["gammas"],
        "ddelta": dot_delta(st, A),
        "frozen_D": frozen_D(st, A),
        "max_abs_A": float(np.max(np.abs(A))),
        "tangent_residual": tangent_residual(P0, A),
        "A": A.tolist(),
    }


def simplex_point(k: int, support: Iterable[int], weights: Iterable[float] | None = None) -> np.ndarray:
    support = list(support)
    out = np.zeros(k)
    if weights is None:
        out[support] = 1.0 / len(support)
    else:
        w = np.array(list(weights), dtype=float)
        w = w / w.sum()
        out[support] = w
    return out


def local_pi(size: int, mode: str, rng: np.random.Generator) -> np.ndarray:
    if size == 1:
        return np.array([1.0])
    if mode == "uniform":
        return np.ones(size) / size
    if mode == "tiny":
        eps = 1e-6
        v = np.ones(size) * ((1.0 - eps) / (size - 1))
        v[0] = eps
        return v
    if mode == "double_tiny":
        eps = 1e-6
        if size == 2:
            return np.array([eps, 1.0 - eps])
        v = np.ones(size) * ((1.0 - 2 * eps) / (size - 2))
        v[0] = eps
        v[1] = eps
        return v
    if mode == "skew":
        weights = np.geomspace(1e-6, 1.0, size)
        return weights / weights.sum()
    return rng.dirichlet(np.ones(size) * 0.7)


def make_stratum(
    name: str,
    block_sizes: list[int],
    t: int,
    pi_modes: list[str],
    alphas: list[np.ndarray],
    rng: np.random.Generator,
) -> Stratum:
    blocks = []
    cursor = 0
    for size in block_sizes:
        blocks.append(list(range(cursor, cursor + size)))
        cursor += size
    transients = list(range(cursor, cursor + t))
    pis = [local_pi(size, pi_modes[min(s, len(pi_modes) - 1)], rng) for s, size in enumerate(block_sizes)]
    alpha_transient = {i: np.array(alphas[idx], dtype=float) for idx, i in enumerate(transients)}
    return Stratum(name, blocks, transients, pis, alpha_transient)


def deterministic_strata(rng: np.random.Generator) -> list[Stratum]:
    out: list[Stratum] = []
    for a in [0.0, 0.2, 0.5, 0.8, 1.0]:
        out.append(
            make_stratum(
                f"n3_k2_endpoint_sweep_{a:g}",
                [1, 1],
                1,
                ["uniform", "uniform"],
                [np.array([a, 1.0 - a])],
                rng,
            )
        )
    out.append(make_stratum("k1_rank1_many_transients", [3], 6, ["tiny"], [np.ones(1) for _ in range(6)], rng))
    out.append(
        make_stratum(
            "tiny_pi_many_transients_k3",
            [3, 2, 1],
            6,
            ["tiny", "skew", "uniform"],
            [
                simplex_point(3, [0]),
                simplex_point(3, [1]),
                simplex_point(3, [2]),
                simplex_point(3, [0, 1], [1e-6, 1.0]),
                simplex_point(3, [0, 2], [1.0, 1e-6]),
                simplex_point(3, [0, 1, 2], [1e-6, 0.3, 0.7]),
            ],
            rng,
        )
    )
    out.append(
        make_stratum(
            "n12_boundary_faces_k4",
            [2, 2, 1, 1],
            6,
            ["double_tiny", "tiny", "uniform", "uniform"],
            [
                simplex_point(4, [0]),
                simplex_point(4, [1]),
                simplex_point(4, [2]),
                simplex_point(4, [3]),
                simplex_point(4, [0, 2], [1e-6, 1.0]),
                simplex_point(4, [1, 2, 3], [0.2, 0.3, 0.5]),
            ],
            rng,
        )
    )
    out.append(
        make_stratum(
            "leftcone_shape_hm_anchor",
            [1, 1, 1],
            1,
            ["uniform", "uniform", "uniform"],
            [np.array([1 / 3, 1 / 3, 1 / 3])],
            rng,
        )
    )
    return out


def random_alpha(k: int, rng: np.random.Generator) -> np.ndarray:
    kind = rng.choice(["onehot", "face", "tiny_face", "full"], p=[0.25, 0.30, 0.20, 0.25])
    if kind == "onehot":
        return simplex_point(k, [int(rng.integers(k))])
    if kind == "face":
        m = int(rng.integers(1, k + 1))
        support = sorted(rng.choice(k, size=m, replace=False).tolist())
        return simplex_point(k, support, rng.random(m) + 0.05)
    if kind == "tiny_face":
        m = int(rng.integers(2, k + 1)) if k > 1 else 1
        support = sorted(rng.choice(k, size=m, replace=False).tolist())
        weights = rng.random(m) + 0.05
        weights[0] = 1e-6
        return simplex_point(k, support, weights)
    return rng.dirichlet(np.ones(k) * 0.6)


def random_strata(count: int, rng: np.random.Generator) -> list[Stratum]:
    out = []
    for idx in range(count):
        k = int(rng.integers(1, 6))
        recurrent_n = int(rng.integers(k, min(8, 12) + 1))
        cuts = sorted(rng.choice(range(1, recurrent_n), size=k - 1, replace=False).tolist()) if k > 1 else []
        sizes = []
        last = 0
        for c in cuts + [recurrent_n]:
            sizes.append(c - last)
            last = c
        t = int(rng.integers(0, 13 - recurrent_n))
        if t == 0 and recurrent_n < 12 and rng.random() < 0.75:
            t = 1
        modes = rng.choice(["uniform", "tiny", "skew", "random"], size=k, replace=True).tolist()
        alphas = [random_alpha(k, rng) for _ in range(t)]
        out.append(make_stratum(f"random_{idx:03d}", sizes, t, modes, alphas, rng))
    return out


def l1_distance_to_conv(x: np.ndarray, points: np.ndarray) -> float:
    if len(points) == 0:
        return math.inf
    n = len(x)
    m = len(points)
    # variables lambda_m, pos_n, neg_n with sum lambda*p + pos - neg = x.
    c = np.r_[np.zeros(m), np.ones(n), np.ones(n)]
    Aeq = []
    beq = []
    for d in range(n):
        row = np.zeros(m + 2 * n)
        row[:m] = points[:, d]
        row[m + d] = 1.0
        row[m + n + d] = -1.0
        Aeq.append(row)
        beq.append(x[d])
    row = np.zeros(m + 2 * n)
    row[:m] = 1.0
    Aeq.append(row)
    beq.append(1.0)
    bounds = [(0.0, None)] * (m + 2 * n)
    res = linprog(c, A_eq=np.array(Aeq), b_eq=np.array(beq), bounds=bounds, method="highs")
    if not res.success:
        return math.inf
    return max(0.0, float(res.fun))


def unique_rows(rows: np.ndarray, tol: float = 1e-8) -> tuple[np.ndarray, list[int]]:
    reps: list[np.ndarray] = []
    rep_indices: list[int] = []
    for i, row in enumerate(rows):
        if not any(np.linalg.norm(row - r, ord=1) <= tol for r in reps):
            reps.append(row.copy())
            rep_indices.append(i)
    return np.array(reps), rep_indices


def exposed_margin(vertex: np.ndarray, rows: np.ndarray, rho: float) -> float:
    far = [idx for idx, row in enumerate(rows) if np.linalg.norm(row - vertex, ord=1) >= rho - 1e-10]
    if not far:
        return math.inf
    n = len(vertex)
    # variables a_n, b, m; h(x)=a.x+b; maximize m.
    c = np.zeros(n + 2)
    c[-1] = -1.0
    Aeq = np.zeros((1, n + 2))
    Aeq[0, :n] = vertex
    Aeq[0, n] = 1.0
    beq = np.array([0.0])
    Aub = []
    bub = []
    for row_pt in rows:
        hi = np.zeros(n + 2)
        hi[:n] = row_pt
        hi[n] = 1.0
        Aub.append(hi)
        bub.append(1.0)
        Aub.append(-hi)
        bub.append(0.0)
    for idx in far:
        hi = np.zeros(n + 2)
        hi[:n] = -rows[idx]
        hi[n] = -1.0
        hi[-1] = 1.0
        Aub.append(hi)
        bub.append(0.0)
    bounds = [(None, None)] * (n + 2)
    res = linprog(c, A_ub=np.array(Aub), b_ub=np.array(bub), A_eq=Aeq, b_eq=beq, bounds=bounds, method="highs")
    if not res.success:
        return -math.inf
    return max(0.0, float(-res.fun))


def height_visible(P: np.ndarray) -> dict:
    rows, rep_indices = unique_rows(P, tol=1e-12)
    delta = max(float(np.maximum(-row, 0.0).sum()) for row in P)
    tau = math.sqrt(max(delta, 0.0))
    rho = 4.0 * tau
    kappa = tau / 4.0
    if delta <= 1e-14:
        vertex_flags = []
        for idx, row in enumerate(rows):
            others = np.array([r for j, r in enumerate(rows) if j != idx])
            vertex_flags.append(len(others) == 0 or l1_distance_to_conv(row, others) > 1e-11)
        return {
            "delta": delta,
            "tau": tau,
            "rho": rho,
            "kappa": kappa,
            "unique_rows": len(rows),
            "representatives": rep_indices,
            "vertices": int(sum(vertex_flags)),
            "visible": int(sum(vertex_flags)),
            "margins": ["delta0" if flag else None for flag in vertex_flags],
            "H": 0.0,
            "row_heights": [0.0 for _ in range(P.shape[0])],
        }
    vertex_flags = []
    visible_flags = []
    margins = []
    for idx, row in enumerate(rows):
        others = np.array([r for j, r in enumerate(rows) if j != idx])
        is_vertex = len(others) == 0 or l1_distance_to_conv(row, others) > 1e-11
        vertex_flags.append(is_vertex)
        if not is_vertex:
            visible_flags.append(False)
            margins.append(None)
            continue
        margin = exposed_margin(row, rows, rho)
        margins.append(margin)
        visible_flags.append(math.isinf(margin) or margin + 1e-9 >= kappa)
    visible_points = np.array([row for row, flag in zip(rows, visible_flags) if flag])
    heights = [l1_distance_to_conv(row, visible_points) for row in P] if len(visible_points) else [math.inf]
    return {
        "delta": delta,
        "tau": tau,
        "rho": rho,
        "kappa": kappa,
        "unique_rows": len(rows),
        "representatives": rep_indices,
        "vertices": int(sum(vertex_flags)),
        "visible": int(sum(visible_flags)),
        "margins": [None if m is None else ("inf" if math.isinf(m) else m) for m in margins],
        "H": max(heights),
        "row_heights": heights,
    }


def exact_arc(P0: np.ndarray, A: np.ndarray, t: float) -> np.ndarray:
    n = P0.shape[0]
    I = np.eye(n)
    C = P0 @ A @ (I - P0)
    D = (I - P0) @ A @ P0
    Y = D - C
    E = expm(t * Y)
    Einv = expm(-t * Y)
    return E @ P0 @ Einv


def arc_spot_check(st: Stratum, A: np.ndarray, ts: list[float]) -> dict:
    P0 = build_p0(st)
    ddel = dot_delta(st, A)
    out = []
    for t in ts:
        P = exact_arc(P0, A, t)
        hv = height_visible(P)
        out.append(
            {
                "t": t,
                "delta": hv["delta"],
                "H": hv["H"],
                "H_over_t": hv["H"] / t if math.isfinite(hv["H"]) else math.inf,
                "delta_over_t": hv["delta"] / t,
                "visible": hv["visible"],
                "vertices": hv["vertices"],
                "unique_rows": hv["unique_rows"],
                "idempotence_residual": float(np.max(np.abs(P @ P - P))),
                "row_sum_residual": float(np.max(np.abs(P @ np.ones(P.shape[0]) - 1.0))),
            }
        )
    return {"dot_delta_A": ddel, "two_dot_delta_A": 2.0 * ddel, "samples": out}


def compress_record(rec: dict, keep_A: bool = False) -> dict:
    out = dict(rec)
    if not keep_A:
        out.pop("budget1", None)
        out.pop("zero_budget", None)
    return out


def run(args: argparse.Namespace) -> dict:
    rng = np.random.default_rng(args.seed)
    strata = deterministic_strata(rng) + random_strata(args.samples_random, rng)
    records = []
    t0 = time.time()
    for idx, st in enumerate(strata):
        zero = solve_stratum(st, 0.0, args.norm_bound)
        budget1 = solve_stratum(st, 1.0, args.norm_bound)
        records.append(
            {
                "idx": idx,
                "name": st.name,
                "n": st.n,
                "k": st.k,
                "t": len(st.transients),
                "block_sizes": [len(b) for b in st.blocks],
                "alpha_supports": [np.flatnonzero(row_alphas(st)[i] > 1e-10).tolist() for i in st.transients],
                "zero_budget": zero,
                "budget1": budget1,
            }
        )
    elapsed = time.time() - t0
    finite_zero = [r["zero_budget"]["value"] for r in records if math.isfinite(r["zero_budget"]["value"])]
    finite_budget = [r["budget1"]["value"] for r in records if math.isfinite(r["budget1"]["value"])]
    best = max(records, key=lambda r: r["budget1"]["value"])
    best_zero = max(records, key=lambda r: r["zero_budget"]["value"])
    A_best = np.array(best["budget1"]["A"])
    st_best = strata[best["idx"]]
    arc = arc_spot_check(st_best, A_best, args.arc_t)
    summary = {
        "created": time.strftime("%Y-%m-%d %H:%M:%S"),
        "seed": args.seed,
        "samples_random": args.samples_random,
        "samples_total": len(strata),
        "norm_bound": args.norm_bound,
        "elapsed_s": elapsed,
        "zero_budget_max": max(finite_zero) if finite_zero else math.nan,
        "zero_budget_positive_count": sum(v > 1e-7 for v in finite_zero),
        "budget1_min": min(finite_budget) if finite_budget else math.nan,
        "budget1_median": float(np.median(finite_budget)) if finite_budget else math.nan,
        "budget1_mean": float(np.mean(finite_budget)) if finite_budget else math.nan,
        "budget1_p90": float(np.quantile(finite_budget, 0.90)) if finite_budget else math.nan,
        "budget1_p99": float(np.quantile(finite_budget, 0.99)) if finite_budget else math.nan,
        "budget1_max": max(finite_budget) if finite_budget else math.nan,
        "best_idx": best["idx"],
        "best_name": best["name"],
        "best_zero_idx": best_zero["idx"],
        "best_zero_name": best_zero["name"],
    }
    top = sorted(records, key=lambda r: r["budget1"]["value"], reverse=True)[: args.top]
    top_zero = sorted(records, key=lambda r: r["zero_budget"]["value"], reverse=True)[: args.top]
    return {
        "summary": summary,
        "top_budget1": top,
        "top_zero_budget": top_zero,
        "arc_spot_check": arc,
        "records": records if args.full_records else [],
    }


def write_text_summary(result: dict, path: Path) -> None:
    s = result["summary"]
    lines = ["independent tangent audit summary"]
    for key in [
        "created",
        "seed",
        "samples_random",
        "samples_total",
        "norm_bound",
        "elapsed_s",
        "zero_budget_max",
        "zero_budget_positive_count",
        "budget1_min",
        "budget1_median",
        "budget1_mean",
        "budget1_p90",
        "budget1_p99",
        "budget1_max",
        "best_idx",
        "best_name",
    ]:
        lines.append(f"{key}: {s[key]}")
    lines.append("")
    lines.append("top budget1 strata")
    for rec in result["top_budget1"]:
        b = rec["budget1"]
        lines.append(
            "idx={idx} name={name} n={n} k={k} t={t} value={value:.12g} "
            "row={row} neg_subset={neg_subset} ddelta={ddelta:.12g} max_abs={max_abs_A:.12g}".format(
                idx=rec["idx"], name=rec["name"], n=rec["n"], k=rec["k"], t=rec["t"], **b
            )
        )
        lines.append(f"  gammas={b['gammas']}")
    lines.append("")
    lines.append("top zero-budget strata")
    for rec in result["top_zero_budget"]:
        z = rec["zero_budget"]
        lines.append(
            "idx={idx} name={name} n={n} k={k} t={t} value={value:.12g} row={row} neg_subset={neg_subset}".format(
                idx=rec["idx"], name=rec["name"], n=rec["n"], k=rec["k"], t=rec["t"], **z
            )
        )
    lines.append("")
    lines.append("arc spot check for best budget1 direction")
    arc = result["arc_spot_check"]
    lines.append(f"dot_delta_A: {arc['dot_delta_A']}")
    lines.append(f"two_dot_delta_A: {arc['two_dot_delta_A']}")
    for sample in arc["samples"]:
        lines.append(
            "t={t:.3g} delta/t={delta_over_t:.12g} H/t={H_over_t:.12g} "
            "visible={visible} vertices={vertices} idem_res={idempotence_residual:.3g}".format(**sample)
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=19020)
    parser.add_argument("--samples-random", type=int, default=80)
    parser.add_argument("--norm-bound", type=float, default=1.0)
    parser.add_argument("--out-json", type=Path, default=Path("independent_decider_results.json"))
    parser.add_argument("--out-txt", type=Path, default=Path("independent_decider_summary.txt"))
    parser.add_argument("--full-records", action="store_true")
    parser.add_argument("--top", type=int, default=12)
    parser.add_argument("--arc-t", type=float, nargs="*", default=[1e-1, 3e-2, 1e-2, 3e-3, 1e-3, 3e-4])
    args = parser.parse_args()
    result = run(args)
    args.out_json.write_text(json.dumps(result, indent=2), encoding="utf-8")
    write_text_summary(result, args.out_txt)
    print(args.out_txt.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
