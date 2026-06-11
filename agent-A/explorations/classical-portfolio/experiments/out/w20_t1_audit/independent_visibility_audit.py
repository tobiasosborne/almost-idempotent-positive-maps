#!/usr/bin/env python3
"""Independent numerical checks for the w20 T1 audit.

This script deliberately does not import the prover's numerics.  It rebuilds
H-M points, exact similarity arcs, row-vertex/exposedness LPs, and the T1
pointwise visibility check using numpy/scipy only.
"""

from __future__ import annotations

import json
import math
import itertools
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog


TOL = 1e-9


@dataclass
class HM:
    blocks: list[list[int]]
    transients: list[int]
    pis: list[np.ndarray]
    alphas: dict[int, np.ndarray]

    @property
    def n(self) -> int:
        return sum(len(b) for b in self.blocks) + len(self.transients)

    @property
    def k(self) -> int:
        return len(self.blocks)


def embedded_pi(n: int, block: list[int], pi: np.ndarray) -> np.ndarray:
    out = np.zeros(n)
    out[block] = pi
    return out


def build_p0(st: HM) -> np.ndarray:
    n = st.n
    P = np.zeros((n, n))
    pi_full = [embedded_pi(n, b, pi) for b, pi in zip(st.blocks, st.pis)]
    for s, block in enumerate(st.blocks):
        for i in block:
            P[i] = pi_full[s]
    for i in st.transients:
        P[i] = sum(st.alphas[i][s] * pi_full[s] for s in range(st.k))
    return P


def gamma_weights(st: HM) -> np.ndarray:
    W = np.zeros((st.n, st.k))
    for s, block in enumerate(st.blocks):
        W[block, s] = 1.0
    for i in st.transients:
        W[i] = st.alphas[i]
    return W


def min_recurrent_mass(st: HM) -> float:
    return min(float(x) for pi in st.pis for x in pi if x > 0.0)


def delta(P: np.ndarray) -> float:
    return max(float(np.maximum(-row, 0.0).sum()) for row in P)


def row_l1_eps(P: np.ndarray, Q: np.ndarray) -> float:
    return max(float(np.abs(P[i] - Q[i]).sum()) for i in range(P.shape[0]))


def exact_arc_from_Y(P0: np.ndarray, Y: np.ndarray, t: float) -> np.ndarray:
    E = expm(t * Y)
    Einv = expm(-t * Y)
    return E @ P0 @ Einv


def exact_arc_from_A(P0: np.ndarray, A: np.ndarray, t: float) -> np.ndarray:
    n = P0.shape[0]
    I = np.eye(n)
    C = P0 @ A @ (I - P0)
    D = (I - P0) @ A @ P0
    Y = D - C
    return exact_arc_from_Y(P0, Y, t)


def unique_rows(P: np.ndarray, tol: float = 1e-10) -> tuple[np.ndarray, list[int], list[int]]:
    rows: list[np.ndarray] = []
    reps: list[int] = []
    labels: list[int] = []
    for i, row in enumerate(P):
        found = None
        for j, old in enumerate(rows):
            if np.abs(row - old).sum() <= tol:
                found = j
                break
        if found is None:
            labels.append(len(rows))
            rows.append(row.copy())
            reps.append(i)
        else:
            labels.append(found)
    return np.array(rows), reps, labels


def l1_distance_to_conv(x: np.ndarray, pts: np.ndarray) -> float:
    if len(pts) == 0:
        return math.inf
    m, n = pts.shape
    # Variables: lambdas(m), u(n).  Minimize sum u subject to
    # -u <= x - lambda*pts <= u, lambda >= 0, sum lambda = 1.
    c = np.r_[np.zeros(m), np.ones(n)]
    A_eq = [np.r_[np.ones(m), np.zeros(n)]]
    b_eq = [1.0]
    A_ub = []
    b_ub = []
    for j in range(n):
        row = np.zeros(m + n)
        row[:m] = pts[:, j]
        row[m + j] = -1.0
        A_ub.append(row)
        b_ub.append(x[j])
        row = np.zeros(m + n)
        row[:m] = -pts[:, j]
        row[m + j] = -1.0
        A_ub.append(row)
        b_ub.append(-x[j])
    bounds = [(0.0, None)] * m + [(0.0, None)] * n
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                  A_eq=np.array(A_eq), b_eq=np.array(b_eq),
                  bounds=bounds, method="highs")
    if not res.success:
        return math.inf
    return float(res.fun)


def exposed_margin(row: np.ndarray, rows: np.ndarray, rho: float) -> float:
    far = [j for j, r in enumerate(rows) if np.abs(r - row).sum() >= rho - 1e-10]
    if not far:
        return math.inf
    n = rows.shape[1]
    # Variables a(n), b, z. h(x)=a.x+b. Max z.
    c = np.r_[np.zeros(n + 1), -1.0]
    A_ub = []
    b_ub = []
    for r in rows:
        h = np.r_[r, 1.0, 0.0]
        A_ub.append(-h)
        b_ub.append(0.0)
        A_ub.append(h)
        b_ub.append(1.0)
    for j in far:
        h = np.r_[rows[j], 1.0, -1.0]
        A_ub.append(-h)
        b_ub.append(0.0)
    A_eq = [np.r_[row, 1.0, 0.0]]
    b_eq = [0.0]
    bounds = [(None, None)] * (n + 1) + [(0.0, 1.0)]
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                  A_eq=np.array(A_eq), b_eq=np.array(b_eq),
                  bounds=bounds, method="highs")
    if not res.success:
        return -math.inf
    return float(res.x[-1])


def visibility(P: np.ndarray, cluster_tol: float = 1e-10) -> dict:
    rows, reps, labels = unique_rows(P, cluster_tol)
    d = delta(P)
    tau = math.sqrt(max(d, 0.0))
    rho = 4.0 * tau
    kappa = tau / 4.0
    vertex = []
    margins = []
    visible = []
    for i, row in enumerate(rows):
        others = np.array([r for j, r in enumerate(rows) if j != i])
        dist = l1_distance_to_conv(row, others) if len(others) else math.inf
        is_vertex = dist > max(1e-9, 10.0 * cluster_tol)
        vertex.append(is_vertex)
        if not is_vertex:
            margins.append(None)
            visible.append(False)
            continue
        m = math.inf if d <= 1e-15 else exposed_margin(row, rows, rho)
        margins.append(m)
        visible.append(math.isinf(m) or m + 2e-8 >= kappa)
    visible_pts = np.array([r for r, flag in zip(rows, visible) if flag])
    heights = [l1_distance_to_conv(row, visible_pts) for row in P] if len(visible_pts) else [math.inf]
    return {
        "delta": d,
        "tau": tau,
        "rho": rho,
        "kappa": kappa,
        "unique_rows": len(rows),
        "representatives": reps,
        "labels": labels,
        "vertex": vertex,
        "visible": visible,
        "margins": margins,
        "H": max(heights),
    }


def eta_star_for_block_vertex(st: HM, P: np.ndarray, P0: np.ndarray, row_index: int, block_s: int) -> float:
    rows, reps, labels = unique_rows(P, 1e-10)
    vlabel = labels[row_index]
    row = rows[vlabel]
    W = gamma_weights(st)
    gamma = P @ W[:, block_s]
    shifted = gamma[row_index] - gamma  # g_i-g_v = (1-gamma_i)-(1-gamma_v)
    target_labels = sorted({labels[i] for i, val in enumerate(shifted) if val < -1e-10})
    target_labels = [j for j in target_labels if j != vlabel]
    if not target_labels:
        return math.inf
    n = rows.shape[1]
    # Maximize z over support functions ell(row_v)=0, 0<=ell(rows)<=1,
    # ell(targets)>=z.
    c = np.r_[np.zeros(n + 1), -1.0]
    A_ub = []
    b_ub = []
    for r in rows:
        h = np.r_[r, 1.0, 0.0]
        A_ub.append(-h)
        b_ub.append(0.0)
        A_ub.append(h)
        b_ub.append(1.0)
    for j in target_labels:
        h = np.r_[rows[j], 1.0, -1.0]
        A_ub.append(-h)
        b_ub.append(0.0)
    A_eq = [np.r_[row, 1.0, 0.0]]
    b_eq = [0.0]
    bounds = [(None, None)] * (n + 1) + [(0.0, 1.0)]
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                  A_eq=np.array(A_eq), b_eq=np.array(b_eq),
                  bounds=bounds, method="highs")
    if not res.success:
        return -math.inf
    return float(res.x[-1])


def random_row_sum_zero_Y(n: int, rng: np.random.Generator, scale: float) -> np.ndarray:
    Y = rng.normal(size=(n, n))
    Y -= Y.mean(axis=1, keepdims=True)
    norm = max(np.abs(Y).sum(axis=1))
    return scale * Y / norm


def fixed_mass_sanity() -> dict:
    rng = np.random.default_rng(20260611)
    st = HM(
        blocks=[[0, 1], [2], [3]],
        transients=[4, 5],
        pis=[np.array([0.35, 0.65]), np.array([1.0]), np.array([1.0])],
        alphas={
            4: np.array([0.55, 0.45, 0.0]),
            5: np.array([0.20, 0.30, 0.50]),
        },
    )
    P0 = build_p0(st)
    records = []
    violations = []
    for case in range(20):
        Y = random_row_sum_zero_Y(st.n, rng, 0.75)
        M = max(np.abs(Y).sum(axis=1))
        for t in np.geomspace(2e-7, 2e-2, 28):
            P = exact_arc_from_Y(P0, Y, float(t))
            hv = visibility(P)
            eps = row_l1_eps(P, P0)
            tau = hv["tau"]
            for s, block in enumerate(st.blocks):
                for row_index in block:
                    label = hv["labels"][row_index]
                    if not hv["vertex"][label]:
                        continue
                    eta = eta_star_for_block_vertex(st, P, P0, row_index, s)
                    eta_eff = 1.0 if math.isinf(eta) else max(eta, 0.0)
                    threshold = min(min_recurrent_mass(st) / 8.0, tau / 64.0,
                                    eta_eff * tau / 64.0, 1.0 / 64.0)
                    condition = eps <= threshold + 1e-12
                    r_implicit = (1.0 / (4.0 * st.n * M)) * threshold if M > 0 else math.inf
                    formula_condition = t < r_implicit
                    visible = bool(hv["visible"][label])
                    if condition and not visible:
                        violations.append({"case": case, "t": float(t), "row": row_index, "eps": eps,
                                           "threshold": threshold, "tau": tau, "eta": eta})
                    records.append({
                        "case": case,
                        "t": float(t),
                        "row": row_index,
                        "delta": hv["delta"],
                        "H": hv["H"],
                        "eps": eps,
                        "tau": tau,
                        "eta": "inf" if math.isinf(eta) else eta,
                        "threshold": threshold,
                        "condition": condition,
                        "formula_condition": formula_condition,
                        "visible": visible,
                    })
    return {
        "records": len(records),
        "condition_true": sum(1 for r in records if r["condition"]),
        "formula_condition_true": sum(1 for r in records if r["formula_condition"]),
        "violations": violations[:10],
    }


def tiny_stress_stratum(mu: float = 1e-6) -> HM:
    pi0 = np.array([mu, (1.0 - mu) / 2.0, (1.0 - mu) / 2.0])
    pi1 = np.array([mu, 1.0])
    pi1 = pi1 / pi1.sum()
    pi2 = np.array([1.0])
    return HM(
        blocks=[[0, 1, 2], [3, 4], [5]],
        transients=[6, 7, 8, 9, 10, 11],
        pis=[pi0, pi1, pi2],
        alphas={
            6: np.array([1.0, 0.0, 0.0]),
            7: np.array([0.0, 1.0, 0.0]),
            8: np.array([0.0, 0.0, 1.0]),
            9: np.array([mu, 1.0 - mu, 0.0]),
            10: np.array([1.0 - mu, 0.0, mu]),
            11: np.array([mu, 0.3, 0.7 - mu]),
        },
    )


def row_alphas(st: HM) -> np.ndarray:
    alpha = np.zeros((st.n, st.k))
    for s, block in enumerate(st.blocks):
        for i in block:
            alpha[i, s] = 1.0
    for i in st.transients:
        alpha[i] = st.alphas[i]
    return alpha


def tangent_equalities(P0: np.ndarray, total_vars: int) -> tuple[np.ndarray, np.ndarray]:
    n = P0.shape[0]
    rows = []
    rhs = []
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
        row[i * n:(i + 1) * n] = 1.0
        rows.append(row)
        rhs.append(0.0)
    return np.array(rows), np.array(rhs)


def gamma_coeff(n: int, W: np.ndarray, row_i: int, q: int, total_vars: int) -> np.ndarray:
    coeff = np.zeros(total_vars)
    for j in range(n):
        coeff[row_i * n + j] = W[j, q]
    return coeff


def solve_one_tangent_lp(
    st: HM,
    budget: float,
    target_row: int,
    neg_subset: tuple[int, ...],
    forbidden: list[int],
) -> dict | None:
    P0 = build_p0(st)
    n = st.n
    W = gamma_weights(st)
    active_pairs = [(i, j) for i in range(n) for j in range(n) if P0[i, j] <= 1e-12]
    u_offset = n * n
    total = n * n + len(active_pairs)
    Aeq, beq = tangent_equalities(P0, total)
    Aub = []
    bub = []
    for u_idx, (i, j) in enumerate(active_pairs):
        # u_ij >= -A_ij.
        row = np.zeros(total)
        row[i * n + j] = -1.0
        row[u_offset + u_idx] = -1.0
        Aub.append(row)
        bub.append(0.0)
    for i in range(n):
        row = np.zeros(total)
        for u_idx, (ii, _j) in enumerate(active_pairs):
            if ii == i:
                row[u_offset + u_idx] = 1.0
        Aub.append(row)
        bub.append(budget)
    neg_set = set(neg_subset)
    for q in forbidden:
        coeff = gamma_coeff(n, W, target_row, q, total)
        if q in neg_set:
            Aub.append(coeff)
            bub.append(0.0)
        else:
            Aub.append(-coeff)
            bub.append(0.0)
    c = np.zeros(total)
    for q in neg_subset:
        c += 2.0 * gamma_coeff(n, W, target_row, q, total)
    res = linprog(c, A_ub=np.array(Aub), b_ub=np.array(bub),
                  A_eq=Aeq, b_eq=beq,
                  bounds=[(-1.0, 1.0)] * (n * n) + [(0.0, None)] * len(active_pairs),
                  method="highs")
    if not res.success:
        return None
    A = res.x[:n * n].reshape((n, n))
    return {"value": max(0.0, -float(res.fun)), "A": A, "row": target_row,
            "neg_subset": list(neg_subset)}


def solve_tangent_lp(st: HM, budget: float) -> dict:
    alpha = row_alphas(st)
    best = None
    lp_count = 0
    for i in range(st.n):
        forbidden = [q for q in range(st.k) if alpha[i, q] <= 1e-10]
        for r in range(len(forbidden) + 1):
            for neg_subset in itertools.combinations(forbidden, r):
                lp_count += 1
                out = solve_one_tangent_lp(st, budget, i, neg_subset, forbidden)
                if out is not None and (best is None or out["value"] > best["value"] + 1e-10):
                    best = out
    if best is None:
        raise RuntimeError("no tangent LP solution")
    P0 = build_p0(st)
    A = best["A"]
    active_cost = max(float(np.maximum(-A[i][P0[i] <= 1e-12], 0.0).sum()) for i in range(st.n))
    residual = max(float(np.max(np.abs(P0 @ A + A @ P0 - A))), float(np.max(np.abs(A @ np.ones(st.n)))))
    best.update({"lp_count": lp_count, "active_cost": active_cost, "tangent_residual": residual})
    return best


def solve_zero_budget_generator(P0: np.ndarray, target: tuple[int, int]) -> np.ndarray:
    n = P0.shape[0]
    total = n * n
    def coeff_A(i: int, j: int) -> np.ndarray:
        c = np.zeros(total)
        # A = YP0 - P0Y.
        for a in range(n):
            c[i * n + a] += P0[a, j]
            c[a * n + j] -= P0[i, a]
        return c
    A_eq = []
    b_eq = []
    for i in range(n):
        row = np.zeros(total)
        row[i * n:(i + 1) * n] = 1.0
        A_eq.append(row)
        b_eq.append(0.0)
    A_ub = []
    b_ub = []
    zeros = P0 <= 1e-12
    for i in range(n):
        for j in range(n):
            if zeros[i, j]:
                A_ub.append(-coeff_A(i, j))
                b_ub.append(0.0)
    c = coeff_A(*target)
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                  A_eq=np.array(A_eq), b_eq=np.array(b_eq),
                  bounds=[(-1.0, 1.0)] * total, method="highs")
    if not res.success:
        raise RuntimeError(res.message)
    Y = res.x.reshape((n, n))
    Y -= Y.mean(axis=1, keepdims=True)
    norm = max(np.abs(Y).sum(axis=1))
    return Y / norm


def tiny_active_scale_sweep() -> dict:
    st = tiny_stress_stratum(1e-6)
    P0 = build_p0(st)
    sol = solve_tangent_lp(st, 0.0)
    A = sol["A"]
    active_cost = sol["active_cost"]
    records = []
    for t in [1e-4, 3e-5, 1e-5, 3e-6, 1e-6, 3e-7, 1e-7, 3e-8]:
        P = exact_arc_from_A(P0, A, t)
        hv = visibility(P, cluster_tol=1e-8)
        d = hv["delta"]
        H = 0.0 if d <= 1e-14 else hv["H"]
        records.append({
            "t": t,
            "delta": d,
            "H": H,
            "delta_over_t": d / t,
            "H_over_t": H / t if math.isfinite(H) else math.inf,
            "H_over_delta": (0.0 if d <= 1e-15 and H <= 1e-12 else (math.inf if d <= 1e-15 else H / d)),
            "visible": sum(1 for x in hv["visible"] if x),
            "vertices": sum(1 for x in hv["vertex"] if x),
        })
    return {
        "mu": min_recurrent_mass(st),
        "lp_value": sol["value"],
        "lp_row": sol["row"],
        "lp_neg_subset": sol["neg_subset"],
        "tangent_residual": sol["tangent_residual"],
        "max_abs_A": float(np.max(np.abs(A))),
        "active_zero_derivative_cost": active_cost,
        "records": records,
    }


def recode(st: HM, theta: float) -> HM:
    new_blocks: list[list[int]] = []
    new_transients = list(st.transients)
    new_pis: list[np.ndarray] = []
    old_to_new_block: dict[int, tuple[int, float]] = {}
    for s, (block, pi) in enumerate(zip(st.blocks, st.pis)):
        keep_pairs = [(idx, mass) for idx, mass in zip(block, pi) if mass >= theta]
        drop_pairs = [(idx, mass) for idx, mass in zip(block, pi) if mass < theta]
        if not keep_pairs:
            # Keep the largest coordinate so the recoding remains an H-M stratum.
            best = int(np.argmax(pi))
            keep_pairs = [(block[best], float(pi[best]))]
            drop_pairs = [(idx, mass) for idx, mass in zip(block, pi) if idx != block[best]]
        kept_indices = [idx for idx, _ in keep_pairs]
        kept_mass = np.array([mass for _, mass in keep_pairs], dtype=float)
        kept_mass = kept_mass / kept_mass.sum()
        ns = len(new_blocks)
        for idx in kept_indices:
            old_to_new_block[idx] = (ns, 1.0)
        for idx, _ in drop_pairs:
            new_transients.append(idx)
            old_to_new_block[idx] = (ns, 1.0)
        new_blocks.append(kept_indices)
        new_pis.append(kept_mass)
    # Any old transient row remains a mixture with the same block coefficients.
    new_alphas: dict[int, np.ndarray] = {}
    for i in new_transients:
        if i in st.alphas:
            new_alphas[i] = st.alphas[i].copy()
        else:
            s, _ = old_to_new_block[i]
            a = np.zeros(st.k)
            a[s] = 1.0
            new_alphas[i] = a
    return HM(new_blocks, sorted(new_transients), new_pis, new_alphas)


def recoding_degenerations() -> dict:
    rows = []
    for nsmall, theta in [(4, 1e-5), (8, 1e-5), (20, 1e-5), (20, 1e-4)]:
        small = theta * 0.99
        kept_tiny = theta * 1.01
        big = 1.0 - nsmall * small - kept_tiny
        block = list(range(nsmall + 1))
        pi = np.array([small] * nsmall + [kept_tiny, big])
        block = list(range(nsmall + 2))
        st = HM(blocks=[block, [nsmall + 2]], transients=[nsmall + 3],
                pis=[pi, np.array([1.0])],
                alphas={nsmall + 3: np.array([theta * 0.5, 1.0 - theta * 0.5])})
        P0 = build_p0(st)
        rec = recode(st, theta)
        Ptheta = build_p0(rec)
        eps_recode = row_l1_eps(P0, Ptheta)
        mu_theta = min_recurrent_mass(rec)
        rows.append({
            "nsmall": nsmall,
            "n": st.n,
            "theta": theta,
            "dropped_mass": float(nsmall * small),
            "eps_recode": eps_recode,
            "mu_after": mu_theta,
            "eps_over_theta": eps_recode / theta,
            "fixed_mass_mu_condition_ratio": eps_recode / (mu_theta / 8.0),
            "transient_alpha_to_dropped_block": theta * 0.5,
        })
    return {"cases": rows}


def main() -> None:
    out = {
        "fixed_mass_sanity": fixed_mass_sanity(),
        "tiny_active_scale_sweep": tiny_active_scale_sweep(),
        "recoding_degenerations": recoding_degenerations(),
    }
    Path("independent_visibility_results.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    lines = []
    f = out["fixed_mass_sanity"]
    lines.append("fixed-mass T1 pointwise check")
    lines.append(f"records: {f['records']}")
    lines.append(f"condition_true: {f['condition_true']}")
    lines.append(f"formula_condition_true: {f['formula_condition_true']}")
    lines.append(f"condition_violations: {len(f['violations'])}")
    lines.append("")
    tiny = out["tiny_active_scale_sweep"]
    lines.append("tiny active-entry stress")
    lines.append(f"mu: {tiny['mu']:.12g}")
    lines.append(f"lp_value: {tiny['lp_value']:.12g}")
    lines.append(f"lp_row: {tiny['lp_row']}")
    lines.append(f"lp_neg_subset: {tiny['lp_neg_subset']}")
    lines.append(f"tangent_residual: {tiny['tangent_residual']:.12g}")
    lines.append(f"active_zero_derivative_cost: {tiny['active_zero_derivative_cost']:.12g}")
    for r in tiny["records"]:
        lines.append(
            "t={t:.3g} delta/t={delta_over_t:.12g} H/t={H_over_t:.12g} "
            "H/delta={H_over_delta:.12g} visible={visible} vertices={vertices}".format(**r)
        )
    lines.append("")
    lines.append("recoding stress")
    for r in out["recoding_degenerations"]["cases"]:
        lines.append(
            "nsmall={nsmall} theta={theta:.1e} dropped={dropped_mass:.3g} "
            "eps_rec/theta={eps_over_theta:.3g} eps/(mu/8)={fixed_mass_mu_condition_ratio:.3g} "
            "alpha={transient_alpha_to_dropped_block:.1e}".format(**r)
        )
    text = "\n".join(lines) + "\n"
    Path("independent_visibility_summary.txt").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
