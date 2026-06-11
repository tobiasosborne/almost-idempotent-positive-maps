#!/usr/bin/env python3
"""Independent verifier for the w17 antecedent claim.

This intentionally does not import or call the claimant's decider.  It reads the
published JSON matrices and recomputes the row geometry from the definitions in
kernel-conjecture.tex.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from collections import defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

import numpy as np
import sympy as sp
from scipy.optimize import linprog


LP_TOL = 1e-9
ACTIVE_TOL = 2e-8
ROW_EQ_TOL = 1e-9


@dataclass
class ExposednessResult:
    target: int
    far: list[int]
    tstar: float
    h_values: np.ndarray
    a: np.ndarray
    b: float
    primal_success: bool
    dual_success: bool
    dual_obj: float
    dual_gap: float
    active_upper: list[int]
    active_lower: list[int]
    active_far: list[int]
    dual_positive_upper: list[tuple[int, float]]
    dual_positive_lower: list[tuple[int, float]]
    dual_positive_far: list[tuple[int, float]]
    dual_mu: float


def load_matrix(path: str | Path) -> np.ndarray:
    with open(path) as f:
        obj = json.load(f)
    if "P" not in obj:
        raise ValueError(f"{path} does not contain a P matrix")
    return np.array(obj["P"], dtype=float)


def load_json(path: str | Path) -> Any:
    with open(path) as f:
        return json.load(f)


def row_negative_masses(P: np.ndarray) -> np.ndarray:
    return np.maximum(-P, 0.0).sum(axis=1)


def scales(P: np.ndarray) -> dict[str, float | np.ndarray]:
    row_neg = row_negative_masses(P)
    delta = float(row_neg.max())
    tau = math.sqrt(delta)
    return {
        "row_neg": row_neg,
        "delta": delta,
        "tau": tau,
        "rho": 4.0 * tau,
        "kappa": tau / 4.0,
    }


def l1_distances_from(P: np.ndarray, i: int) -> np.ndarray:
    return np.abs(P - P[i]).sum(axis=1)


def distinct_row_classes(P: np.ndarray, tol: float = ROW_EQ_TOL) -> list[list[int]]:
    classes: list[list[int]] = []
    for i in range(P.shape[0]):
        for cls in classes:
            if np.max(np.abs(P[i] - P[cls[0]])) <= tol:
                cls.append(i)
                break
        else:
            classes.append([i])
    return classes


def linprog_checked(*, c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None) -> Any:
    res = linprog(
        c=np.array(c, dtype=float),
        A_ub=None if A_ub is None else np.array(A_ub, dtype=float),
        b_ub=None if b_ub is None else np.array(b_ub, dtype=float),
        A_eq=None if A_eq is None else np.array(A_eq, dtype=float),
        b_eq=None if b_eq is None else np.array(b_eq, dtype=float),
        bounds=bounds,
        method="highs",
        options={"primal_feasibility_tolerance": 1e-10, "dual_feasibility_tolerance": 1e-10},
    )
    return res


def distance_to_conv(P: np.ndarray, x: np.ndarray, indices: list[int]) -> tuple[float, np.ndarray, np.ndarray]:
    """Return L1 distance from x to conv{P[j]: j in indices}."""
    if not indices:
        return math.inf, np.array([]), np.array([])
    m = len(indices)
    n = P.shape[1]
    # Variables are lambdas (m) and abs slacks u (n).
    c = np.r_[np.zeros(m), np.ones(n)]
    A_ub = []
    b_ub = []
    rows = P[indices]
    for col in range(n):
        coeff = np.zeros(m + n)
        coeff[:m] = rows[:, col]
        coeff[m + col] = -1.0
        A_ub.append(coeff)
        b_ub.append(x[col])
        coeff = np.zeros(m + n)
        coeff[:m] = -rows[:, col]
        coeff[m + col] = -1.0
        A_ub.append(coeff)
        b_ub.append(-x[col])
    A_eq = [np.r_[np.ones(m), np.zeros(n)]]
    b_eq = [1.0]
    bounds = [(0.0, None)] * m + [(0.0, None)] * n
    res = linprog_checked(c=c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
    if not res.success:
        raise RuntimeError(f"distance LP failed: {res.message}")
    return float(res.fun), res.x[:m], res.x[m:]


def row_vertex_distances(P: np.ndarray) -> tuple[list[bool], list[float]]:
    classes = distinct_row_classes(P)
    rep_for = {}
    for cls in classes:
        for i in cls:
            rep_for[i] = cls[0]

    is_vertex = [False] * P.shape[0]
    dist = [0.0] * P.shape[0]
    for i in range(P.shape[0]):
        other_reps = [cls[0] for cls in classes if cls[0] != rep_for[i]]
        d, _, _ = distance_to_conv(P, P[i], other_reps)
        dist[i] = d
        is_vertex[i] = d > 1e-8
    return is_vertex, dist


def exposedness_primal(P: np.ndarray, v: int, rho: float) -> tuple[Any, list[int]]:
    n = P.shape[0]
    dists = l1_distances_from(P, v)
    far = [j for j in range(n) if j != v and dists[j] >= rho - 1e-10]
    if not far:
        raise ValueError("far set is empty; t*=+inf convention not represented by LP")

    # Variables: a_0..a_{n-1}, b, t.  h(row)=a.row+b.
    num_vars = n + 2
    t_idx = n + 1
    c = np.zeros(num_vars)
    c[t_idx] = -1.0
    A_ub = []
    b_ub = []
    for j in range(n):
        h = np.r_[P[j], 1.0, 0.0]
        A_ub.append(h)
        b_ub.append(1.0)
        A_ub.append(-h)
        b_ub.append(0.0)
    for j in far:
        coeff = np.r_[-P[j], -1.0, 1.0]
        A_ub.append(coeff)
        b_ub.append(0.0)
    A_eq = [np.r_[P[v], 1.0, 0.0]]
    b_eq = [0.0]
    bounds = [(None, None)] * num_vars
    res = linprog_checked(c=c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
    return res, far


def exposedness_dual(P: np.ndarray, v: int, far: list[int]) -> Any:
    """Solve the explicit dual of the exposedness LP.

    Primal is max t subject to h_v=0, 0<=h_j<=1, t<=h_j for j in far.
    Dual variables:
      u_j >= 0 for h_j <= 1,
      ell_j >= 0 for -h_j <= 0,
      r_j >= 0 for t - h_j <= 0,
      mu free for h_v = 0.
    Objective min sum_j u_j.
    """
    n = P.shape[0]
    m = len(far)
    u0 = 0
    ell0 = n
    r0 = 2 * n
    mu_idx = 2 * n + m
    num = mu_idx + 1
    c = np.zeros(num)
    c[u0 : u0 + n] = 1.0

    A_eq = []
    b_eq = []
    # Coordinate equations.
    for col in range(n):
        row = np.zeros(num)
        row[u0 : u0 + n] = P[:, col]
        row[ell0 : ell0 + n] = -P[:, col]
        for pos, j in enumerate(far):
            row[r0 + pos] = -P[j, col]
        row[mu_idx] = P[v, col]
        A_eq.append(row)
        b_eq.append(0.0)
    # Affine constant equation.
    row = np.zeros(num)
    row[u0 : u0 + n] = 1.0
    row[ell0 : ell0 + n] = -1.0
    row[r0 : r0 + m] = -1.0
    row[mu_idx] = 1.0
    A_eq.append(row)
    b_eq.append(0.0)
    # t coefficient equation: sum r_j = 1.
    row = np.zeros(num)
    row[r0 : r0 + m] = 1.0
    A_eq.append(row)
    b_eq.append(1.0)

    bounds = [(0.0, None)] * (2 * n + m) + [(None, None)]
    return linprog_checked(c=c, A_eq=A_eq, b_eq=b_eq, bounds=bounds)


def exposedness(P: np.ndarray, v: int, rho: float) -> ExposednessResult:
    pres, far = exposedness_primal(P, v, rho)
    if not pres.success:
        raise RuntimeError(f"exposedness primal failed for {v}: {pres.message}")
    a = pres.x[: P.shape[1]]
    b = float(pres.x[P.shape[1]])
    tstar = float(pres.x[P.shape[1] + 1])
    h_values = P @ a + b

    dres = exposedness_dual(P, v, far)
    if not dres.success:
        raise RuntimeError(f"exposedness dual failed for {v}: {dres.message}")
    n = P.shape[0]
    m = len(far)
    u = dres.x[:n]
    ell = dres.x[n : 2 * n]
    r = dres.x[2 * n : 2 * n + m]
    mu = float(dres.x[-1])

    active_upper = [j for j in range(n) if abs(1.0 - h_values[j]) <= ACTIVE_TOL]
    active_lower = [j for j in range(n) if abs(h_values[j]) <= ACTIVE_TOL]
    active_far = [j for j in far if abs(h_values[j] - tstar) <= ACTIVE_TOL]
    pos_upper = [(j, float(u[j])) for j in range(n) if u[j] > ACTIVE_TOL]
    pos_lower = [(j, float(ell[j])) for j in range(n) if ell[j] > ACTIVE_TOL]
    pos_far = [(far[pos], float(r[pos])) for pos in range(m) if r[pos] > ACTIVE_TOL]

    return ExposednessResult(
        target=v,
        far=far,
        tstar=tstar,
        h_values=h_values,
        a=a,
        b=b,
        primal_success=True,
        dual_success=True,
        dual_obj=float(dres.fun),
        dual_gap=abs(float(dres.fun) - tstar),
        active_upper=active_upper,
        active_lower=active_lower,
        active_far=active_far,
        dual_positive_upper=pos_upper,
        dual_positive_lower=pos_lower,
        dual_positive_far=pos_far,
        dual_mu=mu,
    )


def visible_set(P: np.ndarray, rho: float, kappa: float, vertices: list[bool]) -> tuple[list[int], dict[int, ExposednessResult]]:
    W = []
    exp = {}
    for i, is_vtx in enumerate(vertices):
        if not is_vtx:
            continue
        res = exposedness(P, i, rho)
        exp[i] = res
        if res.tstar >= kappa - 1e-8:
            W.append(i)
    return W, exp


def height_separator(P: np.ndarray, W: list[int], v: int) -> tuple[float, np.ndarray, float, np.ndarray]:
    n = P.shape[1]
    # Variables a_0..a_{n-1}, b. Maximize a.p_v+b with |a_i|<=1 and h(W)<=0.
    c = -np.r_[P[v], 1.0]
    A_ub = [np.r_[P[w], 1.0] for w in W]
    b_ub = [0.0] * len(W)
    bounds = [(-1.0, 1.0)] * n + [(None, None)]
    res = linprog_checked(c=c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
    if not res.success:
        raise RuntimeError(f"height separator failed: {res.message}")
    a = res.x[:n]
    b = float(res.x[n])
    phi = P @ a + b
    return float(phi[v]), a, b, phi


def all_heights(P: np.ndarray, W: list[int]) -> tuple[np.ndarray, list[np.ndarray]]:
    heights = []
    coeffs = []
    for i in range(P.shape[0]):
        d, lam, _ = distance_to_conv(P, P[i], W)
        heights.append(d)
        coeffs.append(lam)
    return np.array(heights), coeffs


def quotient_classes(P: np.ndarray) -> tuple[list[list[int]], list[int]]:
    classes = distinct_row_classes(P)
    class_of = [0] * P.shape[0]
    for c, cls in enumerate(classes):
        for i in cls:
            class_of[i] = c
    return classes, class_of


def quotient_matrix(P: np.ndarray, classes: list[list[int]]) -> np.ndarray:
    q = len(classes)
    Pbar = np.zeros((q, q))
    for a, cls_a in enumerate(classes):
        rep = cls_a[0]
        for b, cls_b in enumerate(classes):
            Pbar[a, b] = P[rep, cls_b].sum()
    return Pbar


def strongly_connected_components(nodes: list[int], adj: dict[int, list[int]]) -> list[list[int]]:
    nodes_set = set(nodes)
    index = 0
    stack: list[int] = []
    on_stack = set()
    indices: dict[int, int] = {}
    low: dict[int, int] = {}
    comps: list[list[int]] = []

    def visit(v: int) -> None:
        nonlocal index
        indices[v] = index
        low[v] = index
        index += 1
        stack.append(v)
        on_stack.add(v)
        for w in adj.get(v, []):
            if w not in nodes_set:
                continue
            if w not in indices:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in on_stack:
                low[v] = min(low[v], indices[w])
        if low[v] == indices[v]:
            comp = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                comp.append(w)
                if w == v:
                    break
            comps.append(sorted(comp))

    for node in nodes:
        if node not in indices:
            visit(node)
    return sorted(comps, key=lambda c: (len(c), c))


def directed_diameter(component: list[int], weights: np.ndarray, positive_tol: float = 1e-12) -> int | None:
    comp = list(component)
    max_dist = 0
    for src in comp:
        q = deque([(src, 0)])
        seen = {src}
        while q:
            u, d = q.popleft()
            for v in comp:
                if v not in seen and weights[u, v] > positive_tol:
                    seen.add(v)
                    q.append((v, d + 1))
        if len(seen) != len(comp):
            return None
        max_dist = max(max_dist, max(d for _, d in q) if False else 0)
        # Recompute distances without relying on exhausted queue.
        dist = {src: 0}
        q = deque([src])
        while q:
            u = q.popleft()
            for v in comp:
                if v not in dist and weights[u, v] > positive_tol:
                    dist[v] = dist[u] + 1
                    q.append(v)
        max_dist = max(max_dist, max(dist.values()))
    return max_dist


def max_product_paths(component: list[int], weights: np.ndarray, positive_tol: float = 1e-12) -> tuple[float, float]:
    comp = list(component)
    idx = {node: pos for pos, node in enumerate(comp)}
    m = len(comp)
    best = np.zeros((m, m))
    min_edge = math.inf
    for i in comp:
        best[idx[i], idx[i]] = 1.0
        for j in comp:
            w = weights[i, j]
            if w > positive_tol:
                best[idx[i], idx[j]] = max(best[idx[i], idx[j]], w)
                min_edge = min(min_edge, float(w))
    # Floyd-Warshall in max-times semiring.  Component weights here are <1, so
    # cycles cannot improve indefinitely; this also gives the best simple path.
    for k in range(m):
        for i in range(m):
            if best[i, k] <= 0:
                continue
            for j in range(m):
                cand = best[i, k] * best[k, j]
                if cand > best[i, j]:
                    best[i, j] = cand
    pi = float(best.min())
    return pi, float(min_edge)


def quotient_carrier(P: np.ndarray, W: list[int], v: int, phi: np.ndarray, kappa: float, tau: float) -> dict[str, Any]:
    classes, class_of = quotient_classes(P)
    Pbar = quotient_matrix(P, classes)
    g = float(phi[v]) - phi
    # Descend by representative; exact duplicates have equal phi.
    gbar = np.array([g[cls[0]] for cls in classes])
    omega = float(gbar.max() - gbar.min())
    W_classes = sorted({class_of[w] for w in W})
    v_class = class_of[v]
    comps_out = []
    for frac in [0.5, 0.75, 1.0]:
        threshold = frac * kappa * omega
        nodes = [c for c in range(len(classes)) if gbar[c] < threshold + 1e-12]
        adj = {
            c: [d for d in nodes if Pbar[c, d] > 1e-12]
            for c in nodes
        }
        comps = strongly_connected_components(nodes, adj)
        for comp in comps:
            mass = sum(max(Pbar[v_class, c], 0.0) for c in comp)
            if mass <= 1e-12:
                continue
            L = directed_diameter(comp, Pbar)
            pi, min_edge = max_product_paths(comp, Pbar)
            comps_out.append(
                {
                    "t": threshold,
                    "t_over_kappaOmega": frac,
                    "component": comp,
                    "size": len(comp),
                    "mass_from_v": mass,
                    "Pi_C": pi,
                    "L": L,
                    "Pi_over_tau": pi / tau,
                    "min_edge": min_edge,
                }
            )
    best = min(comps_out, key=lambda d: d["Pi_C"]) if comps_out else None
    return {
        "num_classes": len(classes),
        "classes": classes,
        "class_of_v": v_class,
        "class_of_W": W_classes,
        "Pbar": Pbar,
        "g": g,
        "Omega": omega,
        "quotient_shallow_components": comps_out,
        "quotient_best_component": best,
    }


def analyze_matrix(P: np.ndarray, claimed: dict[str, Any] | None = None) -> dict[str, Any]:
    n = P.shape[0]
    sc = scales(P)
    delta = float(sc["delta"])
    tau = float(sc["tau"])
    rho = float(sc["rho"])
    kappa = float(sc["kappa"])
    row_sum_resid = float(np.max(np.abs(P.sum(axis=1) - 1.0)))
    idem_resid = float(np.max(np.abs(P @ P - P)))
    pair_dists = np.array(
        [np.sum(np.abs(P[i] - P[j])) for i in range(n) for j in range(i + 1, n)]
    )
    min_pair_l1 = float(pair_dists.min())

    vertices, vertex_dist = row_vertex_distances(P)
    W, exp = visible_set(P, rho, kappa, vertices)
    heights, height_coeffs = all_heights(P, W)
    H = float(heights.max())
    top = int(np.argmax(heights))
    height_value, sep_a, sep_b, phi = height_separator(P, W, top)
    outside = [i for i, h in enumerate(heights) if h > 1e-8]
    sigma = {
        i: float(sum(max(P[i, j], 0.0) for j in outside))
        for i, is_vtx in enumerate(vertices)
        if is_vtx
    }
    q = quotient_carrier(P, W, top, phi, kappa, tau)

    exp_out = {}
    for i, r in exp.items():
        exp_out[i] = {
            "far": r.far,
            "tstar": r.tstar,
            "tstar_over_kappa": r.tstar / kappa,
            "h_values": r.h_values.tolist(),
            "active_upper": r.active_upper,
            "active_lower": r.active_lower,
            "active_far": r.active_far,
            "dual_obj": r.dual_obj,
            "dual_gap": r.dual_gap,
            "dual_positive_upper": r.dual_positive_upper,
            "dual_positive_lower": r.dual_positive_lower,
            "dual_positive_far": r.dual_positive_far,
            "dual_mu": r.dual_mu,
            "a_l1": float(np.sum(np.abs(r.a))),
        }

    return {
        "n": n,
        "delta": delta,
        "tau": tau,
        "rho": rho,
        "kappa": kappa,
        "row_neg": np.asarray(sc["row_neg"]).tolist(),
        "row_sum_resid": row_sum_resid,
        "idem_resid": idem_resid,
        "all_rows_distinct": bool(min_pair_l1 > 1e-8),
        "min_pair_l1": min_pair_l1,
        "vertices": [i for i, x in enumerate(vertices) if x],
        "vertex_dist": vertex_dist,
        "W": W,
        "hidden_vertices": [i for i, is_vtx in enumerate(vertices) if is_vtx and i not in W],
        "exposedness": exp_out,
        "heights": heights.tolist(),
        "H": H,
        "H_over_tau": H / tau,
        "H_over_delta": H / delta,
        "top": top,
        "height_separator_value": height_value,
        "height_separator_phi": phi.tolist(),
        "outside_CW": outside,
        "sigma_tilde": sigma,
        "sigma_tilde_over_tau": {str(i): s / tau for i, s in sigma.items()},
        "quotient": {
            "num_classes": q["num_classes"],
            "classes": q["classes"],
            "class_of_v": q["class_of_v"],
            "class_of_W": q["class_of_W"],
            "Omega": q["Omega"],
            "quotient_shallow_components": q["quotient_shallow_components"],
            "quotient_best_component": q["quotient_best_component"],
        },
    }


def frac_from_float(x: float, max_den: int) -> Fraction:
    return Fraction(str(float(x))).limit_denominator(max_den)


def fsum(vals: list[Fraction]) -> Fraction:
    out = Fraction(0)
    for v in vals:
        out += v
    return out


def matmul_frac(A: list[list[Fraction]], B: list[list[Fraction]]) -> list[list[Fraction]]:
    rows = len(A)
    cols = len(B[0])
    inner = len(B)
    return [[sum(A[i][k] * B[k][j] for k in range(inner)) for j in range(cols)] for i in range(rows)]


def mat_sub_frac(A: list[list[Fraction]], B: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def eye_frac(n: int) -> list[list[Fraction]]:
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def transpose_frac(A: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*A)]


def rationalize_block_factorization(factor_path: str | Path, max_den: int) -> dict[str, Any]:
    obj = load_json(factor_path)
    Xf = np.array(obj["X_hidden_rows"], dtype=float)
    Qf = np.array(obj["Q"], dtype=float)
    k = Qf.shape[0]
    h = Xf.shape[0]
    X: list[list[Fraction]] = []
    for i in range(h):
        row = [frac_from_float(float(Xf[i, j]), max_den) for j in range(k - 1)]
        row.append(Fraction(1) - fsum(row))
        X.append(row)
    Q = [[frac_from_float(float(Qf[i, j]), max_den) for j in range(h)] for i in range(k)]
    I = eye_frac(k)
    QX = matmul_frac(Q, X)
    A = mat_sub_frac(I, QX)
    XA = matmul_frac(X, A)
    XQ = matmul_frac(X, Q)
    P = [A[i] + Q[i] for i in range(k)] + [XA[i] + XQ[i] for i in range(h)]
    B = eye_frac(k) + X
    L = [A[i] + Q[i] for i in range(k)]
    return {
        "max_den": max_den,
        "X": X,
        "Q": Q,
        "B": B,
        "L": L,
        "P": P,
    }


def frac_matrix_to_float(P: list[list[Fraction]]) -> np.ndarray:
    return np.array([[float(x) for x in row] for row in P], dtype=float)


def frac_to_json(x: Fraction) -> dict[str, int | str]:
    return {"num": x.numerator, "den": x.denominator, "str": f"{x.numerator}/{x.denominator}"}


def save_rational_instance(path: str | Path, rat: dict[str, Any], source: str) -> None:
    P = rat["P"]
    payload = {
        "source_factorization": source,
        "max_den": rat["max_den"],
        "construction": "B=[I;X], L=[I-QX,Q], P=B L; X rows sum exactly 1, hence L B=I and P 1=1 exactly",
        "X": [[frac_to_json(x) for x in row] for row in rat["X"]],
        "Q": [[frac_to_json(x) for x in row] for row in rat["Q"]],
        "P": [[frac_to_json(x) for x in row] for row in P],
        "P_decimal": [[float(x) for x in row] for row in P],
    }
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)


def exact_row_neg(P: list[list[Fraction]]) -> tuple[list[Fraction], Fraction]:
    row_neg = [sum((-x if x < 0 else Fraction(0)) for x in row) for row in P]
    return row_neg, max(row_neg)


def exact_bl_residual(rat: dict[str, Any]) -> Fraction:
    L = rat["L"]
    B = rat["B"]
    LB = matmul_frac(L, B)
    I = eye_frac(len(L))
    return max(abs(LB[i][j] - I[i][j]) for i in range(len(I)) for j in range(len(I)))


def exact_row_sum_residual(P: list[list[Fraction]]) -> Fraction:
    return max(abs(sum(row) - 1) for row in P)


def exact_compare_gt_c_sqrt_delta(value: Fraction, c: Fraction, delta: Fraction) -> bool:
    if value <= 0:
        return False
    return value * value > c * c * delta


def exact_compare_lt_sqrt_delta_over_4(value: Fraction, delta: Fraction) -> bool:
    if value < 0:
        return True
    return 16 * value * value < delta


def sp_rat(x: Fraction) -> sp.Rational:
    return sp.Rational(x.numerator, x.denominator)


def sympy_to_json(x: sp.Rational) -> dict[str, str | float]:
    return {"str": str(x), "decimal": float(x)}


def exact_hidden_dual_certificate(
    P: list[list[Fraction]],
    delta: Fraction,
    v: int,
    upper_support: list[int],
    lower_support: list[int],
    far_support: list[int],
) -> dict[str, Any]:
    """Solve the exposedness dual exactly on a supplied active support."""
    n = len(P)
    variables = []
    names: list[tuple[str, int | None]] = []
    for j in upper_support:
        names.append(("u", j))
        variables.append(sp.symbols(f"u_{j}"))
    for j in lower_support:
        names.append(("ell", j))
        variables.append(sp.symbols(f"ell_{j}"))
    for j in far_support:
        names.append(("r", j))
        variables.append(sp.symbols(f"r_{j}"))
    names.append(("mu", None))
    variables.append(sp.symbols("mu"))

    equations = []
    for col in range(n):
        expr = 0
        for (typ, j), var in zip(names, variables):
            if typ == "u":
                expr += var * sp_rat(P[int(j)][col])
            elif typ == "ell":
                expr -= var * sp_rat(P[int(j)][col])
            elif typ == "r":
                expr -= var * sp_rat(P[int(j)][col])
            else:
                expr += var * sp_rat(P[v][col])
        equations.append(sp.Eq(expr, 0))

    expr = 0
    for (typ, _j), var in zip(names, variables):
        if typ == "u":
            expr += var
        elif typ == "ell":
            expr -= var
        elif typ == "r":
            expr -= var
        else:
            expr += var
    equations.append(sp.Eq(expr, 0))
    equations.append(sp.Eq(sum(var for (typ, _), var in zip(names, variables) if typ == "r"), 1))

    solutions = sp.solve(equations, variables, dict=True, rational=True, simplify=False)
    if not solutions:
        return {"success": False, "reason": "active support linear system has no exact solution"}
    sol = solutions[0]
    nonnegative = all(sol[var] >= 0 for (typ, _), var in zip(names, variables) if typ != "mu")
    objective = sum(sol[var] for (typ, _), var in zip(names, variables) if typ == "u")
    hidden = bool(16 * objective * objective < sp_rat(delta))
    return {
        "success": True,
        "target": v,
        "supports": {
            "upper": upper_support,
            "lower": lower_support,
            "far": far_support,
        },
        "variables": [
            {"kind": typ, "index": j, "value": sympy_to_json(sol[var])}
            for (typ, j), var in zip(names, variables)
        ],
        "objective": sympy_to_json(objective),
        "nonnegative": bool(nonnegative),
        "objective_lt_kappa": hidden,
        "objective_over_kappa_float": float(objective) / (math.sqrt(float(delta)) / 4.0),
    }


def exact_visible_primal_certificate(
    P: list[list[Fraction]],
    Pf: np.ndarray,
    delta: Fraction,
    w: int,
    far: list[int],
    coeff_den: int = 1_000_000,
) -> dict[str, Any]:
    """Rationalize an admissible exposer and check min_far >= kappa exactly."""
    res, _ = exposedness_primal(Pf, w, math.sqrt(float(delta)) * 4.0)
    if not res.success:
        return {"success": False, "target": w, "reason": res.message}
    a = [frac_from_float(float(x), coeff_den) for x in res.x[: len(P)]]
    b0 = -sum(a[col] * P[w][col] for col in range(len(P)))
    vals = [sum(a[col] * P[i][col] for col in range(len(P))) + b0 for i in range(len(P))]
    min_val = min(vals)
    max_val = max(vals)
    if min_val < 0:
        return {
            "success": False,
            "target": w,
            "reason": "rationalized exposer has a negative row value",
            "min_value": str(min_val),
        }
    scale = Fraction(1)
    if max_val > 1:
        scale = Fraction(1, 1) / max_val
    scaled_vals = [scale * value for value in vals]
    min_far = min(scaled_vals[j] for j in far)
    return {
        "success": True,
        "target": w,
        "far": far,
        "scale": str(scale),
        "min_value": str(min(scaled_vals)),
        "max_value": str(max(scaled_vals)),
        "min_far": str(min_far),
        "min_far_decimal": float(min_far),
        "min_far_ge_kappa": bool(16 * min_far * min_far >= sp_rat(delta)),
        "min_far_over_kappa_float": float(min_far) / (math.sqrt(float(delta)) / 4.0),
    }


def exact_separator_witness(
    P: list[list[Fraction]],
    Pf: np.ndarray,
    positive_index: int,
    nonpositive_indices: list[int],
    coeff_den: int = 1_000_000,
) -> dict[str, Any]:
    """Rational L1-Lipschitz affine separator with h(nonpositive)<=0<h(positive)."""
    n = len(P)
    c = -np.r_[Pf[positive_index], 1.0]
    A_ub = [np.r_[Pf[j], 1.0] for j in nonpositive_indices]
    b_ub = [0.0] * len(nonpositive_indices)
    res = linprog_checked(c=c, A_ub=A_ub, b_ub=b_ub, bounds=[(-1.0, 1.0)] * n + [(None, None)])
    if not res.success:
        return {"success": False, "target": positive_index, "reason": res.message}
    a = [frac_from_float(float(x), coeff_den) for x in res.x[:n]]
    raw = [sum(a[col] * P[j][col] for col in range(n)) for j in nonpositive_indices]
    b = -max(raw)
    value = sum(a[col] * P[positive_index][col] for col in range(n)) + b
    max_nonpositive = max(sum(a[col] * P[j][col] for col in range(n)) + b for j in nonpositive_indices)
    return {
        "success": bool(value > 0 and max_nonpositive <= 0),
        "target": positive_index,
        "value": str(value),
        "value_decimal": float(value),
        "max_nonpositive": str(max_nonpositive),
        "coeff_linf": str(max(abs(x) for x in a)),
    }


def exact_height_certificate(
    P: list[list[Fraction]],
    Pf: np.ndarray,
    delta: Fraction,
    W: list[int],
    v: int,
    coeff_den: int = 1_000_000,
) -> dict[str, Any]:
    n = len(P)
    _height, a_float, _b_float, _phi = height_separator(Pf, W, v)
    a = [frac_from_float(float(x), coeff_den) for x in a_float]
    raw_w = [sum(a[col] * P[w][col] for col in range(n)) for w in W]
    b = -max(raw_w)
    value = sum(a[col] * P[v][col] for col in range(n)) + b
    max_w = max(sum(a[col] * P[w][col] for col in range(n)) + b for w in W)
    return {
        "success": bool(value > 0 and max_w <= 0),
        "target": v,
        "W": W,
        "value": str(value),
        "value_decimal": float(value),
        "max_W_value": str(max_w),
        "value_gt_0p1_tau": bool(100 * sp_rat(value) * sp_rat(value) > sp_rat(delta)),
        "value_over_tau_float": float(value) / math.sqrt(float(delta)),
    }


def exact_nonvertex_certificates_from_X(rat: dict[str, Any], top_count: int = 5) -> dict[str, Any]:
    """Rows whose X coefficient row is a nonnegative convex combo of top rows."""
    out = {}
    X = rat["X"]
    for local_idx, coeffs in enumerate(X):
        row_index = top_count + local_idx
        if all(c >= 0 for c in coeffs):
            out[row_index] = {
                "combo_rows": list(range(top_count)),
                "coefficients": [str(c) for c in coeffs],
                "min_coefficient": str(min(coeffs)),
                "sum": str(sum(coeffs)),
            }
    return out


def exact_rational_certificate(
    rat: dict[str, Any],
    rat_comp: dict[str, Any],
    coeff_den: int = 1_000_000,
) -> dict[str, Any]:
    P = rat["P"]
    Pf = frac_matrix_to_float(P)
    row_neg_exact, delta = exact_row_neg(P)
    W = rat_comp["W"]
    top = rat_comp["top"]
    hidden_duals = {}
    for v in rat_comp["hidden_vertices"]:
        exp = rat_comp["exposedness"][v]
        hidden_duals[v] = exact_hidden_dual_certificate(
            P,
            delta,
            v,
            [j for j, _ in exp["dual_positive_upper"]],
            [j for j, _ in exp["dual_positive_lower"]],
            [j for j, _ in exp["dual_positive_far"]],
        )
    visible_primals = {}
    for w in W:
        exp = rat_comp["exposedness"][w]
        visible_primals[w] = exact_visible_primal_certificate(P, Pf, delta, w, exp["far"], coeff_den)
    vertex_witnesses = {
        i: exact_separator_witness(P, Pf, i, [j for j in range(len(P)) if j != i], coeff_den)
        for i in rat_comp["vertices"]
    }
    nonvertices = exact_nonvertex_certificates_from_X(rat, top_count=len(rat["Q"]))
    height_cert = exact_height_certificate(P, Pf, delta, W, top, coeff_den)
    pvv = P[top][top]
    sigma_cert = {
        "P_vv": str(pvv),
        "P_vv_decimal": float(pvv),
        "P_vv_gt_tau": bool(sp_rat(pvv) * sp_rat(pvv) > sp_rat(delta)),
        "row_v_outside_CW_by_height_witness": bool(height_cert["success"] and height_cert["value_decimal"] > 0),
    }
    W_exact = (
        all(c["success"] and c["min_far_ge_kappa"] for c in visible_primals.values())
        and all(c["success"] and c["objective_lt_kappa"] for c in hidden_duals.values())
        and 8 in nonvertices
        and 9 in nonvertices
    )
    antecedent_exact = (
        W_exact
        and hidden_duals.get(top, {}).get("objective_lt_kappa", False)
        and height_cert["value_gt_0p1_tau"]
        and sigma_cert["P_vv_gt_tau"]
    )
    return {
        "max_den": rat["max_den"],
        "BL_minus_I_max": str(exact_bl_residual(rat)),
        "row_sum_residual": str(exact_row_sum_residual(P)),
        "delta": str(delta),
        "delta_float": float(delta),
        "row_neg": [str(x) for x in row_neg_exact],
        "hidden_duals": hidden_duals,
        "visible_primals": visible_primals,
        "vertex_witnesses": vertex_witnesses,
        "nonvertex_convex_combos": nonvertices,
        "height_witness": height_cert,
        "sigma_witness": sigma_cert,
        "W_exact_certified": bool(W_exact),
        "antecedent_exact_certified": bool(antecedent_exact),
    }


def write_report(path: str | Path, data: dict[str, Any]) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=2, sort_keys=True)


def compare_claim(computed: dict[str, Any], cert: dict[str, Any] | None) -> dict[str, Any]:
    if cert is None:
        return {}
    out = {}
    for key in ["delta", "tau", "rho", "kappa", "W", "H"]:
        if key in cert and key in computed:
            out[key] = {"computed": computed[key], "claimed": cert[key]}
    v = cert.get("v")
    if v is not None:
        s = computed["sigma_tilde"].get(v)
        if s is None:
            s = computed["sigma_tilde"].get(str(v))
        out["v"] = v
        out["sigma_tilde_v"] = {
            "computed": s,
            "claimed": cert.get("vertex_info", {}).get(str(v), {}).get("sigma_tilde"),
        }
        out["tstar_v"] = {
            "computed": computed["exposedness"][v]["tstar"] if v in computed["exposedness"] else None,
            "claimed": cert.get("vertex_info", {}).get(str(v), {}).get("exposed_margin"),
        }
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--main-factor", required=True)
    ap.add_argument("--main-cert", required=True)
    ap.add_argument("--robust-factor", required=True)
    ap.add_argument("--robust-cert", required=True)
    ap.add_argument("--outdir", default=".")
    ap.add_argument("--max-den", type=int, default=1_000_000)
    args = ap.parse_args()
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    jobs = {
        "MAIN": (args.main_factor, args.main_cert),
        "ROBUST": (args.robust_factor, args.robust_cert),
    }
    final: dict[str, Any] = {}
    for name, (factor, cert_path) in jobs.items():
        P = load_matrix(factor)
        cert = load_json(cert_path)
        computed = analyze_matrix(P, cert)
        computed["claim_comparison"] = compare_claim(computed, cert)
        final[name] = computed

        rat = rationalize_block_factorization(factor, args.max_den)
        ratP = frac_matrix_to_float(rat["P"])
        rat_comp = analyze_matrix(ratP, cert)
        row_neg_exact, delta_exact = exact_row_neg(rat["P"])
        rat_comp["exact_rational"] = {
            "max_den": args.max_den,
            "BL_minus_I_max": str(exact_bl_residual(rat)),
            "row_sum_residual": str(exact_row_sum_residual(rat["P"])),
            "delta": str(delta_exact),
            "delta_float": float(delta_exact),
            "row_neg": [str(x) for x in row_neg_exact],
            "max_entry_drift_from_float": float(np.max(np.abs(ratP - P))),
        }
        rat_comp["exact_certificate"] = exact_rational_certificate(rat, rat_comp)
        final[name + "_RATIONALIZED_FLOATCHECK"] = rat_comp
        save_rational_instance(outdir / f"{name.lower()}_rational_instance.json", rat, factor)

    write_report(outdir / "verification_report.json", final)


if __name__ == "__main__":
    main()
