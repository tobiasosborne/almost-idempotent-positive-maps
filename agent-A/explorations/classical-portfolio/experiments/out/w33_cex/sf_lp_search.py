#!/usr/bin/env python3
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


def coordinate_rows(k: int, amp: float, graph: str, copies: int = 1):
    rows = [np.eye(k)[i].copy() for i in range(k)]
    foreign = list(range(1, k))
    if graph == "single":
        edges = [(1, 2)]
    elif graph == "duplicate":
        edges = [(1, 2)] * copies
    elif graph == "cycle":
        edges = list(zip(foreign, foreign[1:] + foreign[:1]))
        if len(edges) == 2:
            edges = [(1, 2)]
    elif graph == "path":
        edges = list(zip(foreign, foreign[1:]))
    elif graph == "star":
        edges = [(1, j) for j in foreign[1:]]
    elif graph == "complete":
        edges = list(itertools.combinations(foreign, 2))
    else:
        raise ValueError(graph)
    for u, v in edges:
        plus = np.eye(k)[0].copy()
        plus[u] += amp
        plus[v] -= amp
        minus = np.eye(k)[0].copy()
        minus[u] -= amp
        minus[v] += amp
        rows.extend([plus, minus])
    return np.array(rows, dtype=float), edges


def excesses(L: np.ndarray, s: int = 0):
    out = []
    for row in L:
        mu = sum(max(-row[t], 0.0) for t in range(L.shape[1]) if t != s)
        deficit = 1.0 - row[s]
        out.append(max(mu - deficit, 0.0))
    return np.array(out)


def neg_mass_rows(P: np.ndarray):
    return np.maximum(-P, 0.0).sum(axis=1)


def combo_count(n: int, k: int) -> int:
    return math.comb(n, k) if 0 <= k <= n else 0


def max_minor_abs(L: np.ndarray, limit: int = 200000):
    n, k = L.shape
    total = combo_count(n, k)
    if total > limit:
        return None, None, total
    best = -1.0
    arg = None
    for inds in itertools.combinations(range(n), k):
        val = abs(float(np.linalg.det(L[list(inds), :])))
        if val > best:
            best = val
            arg = inds
    return best, arg, total


def maxvol_float(P: np.ndarray, limit: int = 200000):
    n = P.shape[0]
    k = int(np.linalg.matrix_rank(P, tol=1e-9))
    total = combo_count(n, k)
    if total > limit:
        return None, total
    best = -1e300
    arg = None
    for inds in itertools.combinations(range(n), k):
        R = P[list(inds), :]
        if np.linalg.matrix_rank(R, tol=1e-9) < k:
            continue
        sign, logdet = np.linalg.slogdet(R @ R.T)
        if sign > 0 and logdet > best:
            best = logdet
            arg = inds
    return arg, total


def coeffs_float(P: np.ndarray, pivots):
    basis = P[list(pivots), :]
    return P @ basis.T @ np.linalg.inv(basis @ basis.T)


def sf_float(P: np.ndarray, pivots):
    A = coeffs_float(P, pivots)
    vals = []
    for spos, u in enumerate(pivots):
        e = []
        for j in range(P.shape[0]):
            mu = sum(max(-A[j, t], 0.0) for t in range(A.shape[1]) if t != spos)
            e.append(max(mu - (1.0 - A[j, spos]), 0.0))
        vals.append(float(np.maximum(P[u], 0.0) @ np.array(e)))
    return vals


class LPIndex:
    def __init__(self, k: int, n: int):
        self.k = k
        self.n = n
        self.nb = k * n
        self.nz = n * n
        self.delta = self.nb + self.nz
        self.total = self.delta + 1

    def b(self, r, j):
        return r * self.n + j

    def z(self, i, j):
        return self.nb + i * self.n + j


def base_constraints(L: np.ndarray, idx: LPIndex):
    n, k = L.shape
    eq_rows = []
    eq_rhs = []
    for r in range(k):
        for t in range(k):
            row = np.zeros(idx.total)
            for j in range(n):
                row[idx.b(r, j)] = L[j, t]
            eq_rows.append(row)
            eq_rhs.append(1.0 if r == t else 0.0)
    ub_rows = []
    ub_rhs = []
    for i in range(n):
        for j in range(n):
            row = np.zeros(idx.total)
            row[idx.z(i, j)] = -1.0
            for r in range(k):
                row[idx.b(r, j)] -= L[i, r]
            ub_rows.append(row)
            ub_rhs.append(0.0)
    for i in range(n):
        row = np.zeros(idx.total)
        for j in range(n):
            row[idx.z(i, j)] = 1.0
        row[idx.delta] = -1.0
        ub_rows.append(row)
        ub_rhs.append(0.0)
    return eq_rows, eq_rhs, ub_rows, ub_rhs


def solve_fixed_mass(L: np.ndarray, mass: float, label: str):
    n, k = L.shape
    idx = LPIndex(k, n)
    E = excesses(L)
    c = np.zeros(idx.total)
    c[idx.delta] = 1.0
    eq_rows, eq_rhs, ub_rows, ub_rhs = base_constraints(L, idx)
    fixed = [0.0] * n
    fixed[0] = 1.0 - mass
    for j in range(k, n):
        fixed[j] = mass / (n - k)
    for j, val in enumerate(fixed):
        row = np.zeros(idx.total)
        row[idx.b(0, j)] = 1.0
        eq_rows.append(row)
        eq_rhs.append(val)
    bounds = [(None, None)] * idx.nb + [(0.0, None)] * idx.nz + [(0.0, None)]
    res = linprog(
        c,
        A_ub=np.array(ub_rows),
        b_ub=np.array(ub_rhs),
        A_eq=np.array(eq_rows),
        b_eq=np.array(eq_rhs),
        bounds=bounds,
        method="highs",
    )
    if not res.success:
        return {"label": label, "success": False, "message": res.message}
    B = res.x[: idx.nb].reshape(k, n)
    P = L @ B
    delta = float(neg_mass_rows(P).max())
    sf = float(np.maximum(B[0], 0.0) @ E)
    piv, mv_total = maxvol_float(P)
    sf_mv = None if piv is None else sf_float(P, piv)
    minor, minor_arg, minor_total = max_minor_abs(L)
    return {
        "label": label,
        "success": True,
        "n": n,
        "k": k,
        "mass": mass,
        "delta": delta,
        "sf": sf,
        "sf_over_delta": sf / delta if delta > 0 else None,
        "idempotence_inf": float(np.max(np.abs(P @ P - P))),
        "rowsum_inf": float(np.max(np.abs(P.sum(axis=1) - 1.0))),
        "max_abs_minor_L": minor,
        "max_abs_minor_arg_L": list(minor_arg) if minor_arg is not None else None,
        "minor_combo_count": minor_total,
        "maxvol_pivots": list(piv) if piv is not None else None,
        "maxvol_combo_count": mv_total,
        "maxvol_sf": sf_mv,
        "maxvol_max_sf_over_delta": max(sf_mv) / delta if sf_mv is not None and delta > 0 else None,
        "max_B_row_neg": float(np.maximum(-B, 0.0).sum(axis=1).max()),
    }


def solve_max_sf_row0_nonnegative(L: np.ndarray, delta_cap: float, label: str):
    n, k = L.shape
    idx = LPIndex(k, n)
    E = excesses(L)
    c = np.zeros(idx.total)
    for j in range(n):
        c[idx.b(0, j)] = -E[j]
    eq_rows, eq_rhs, ub_rows, ub_rhs = base_constraints(L, idx)
    row = np.zeros(idx.total)
    row[idx.delta] = 1.0
    ub_rows.append(row)
    ub_rhs.append(delta_cap)
    bounds = [(None, None)] * idx.nb + [(0.0, None)] * idx.nz + [(0.0, None)]
    for j in range(n):
        bounds[idx.b(0, j)] = (0.0, None)
    res = linprog(
        c,
        A_ub=np.array(ub_rows),
        b_ub=np.array(ub_rhs),
        A_eq=np.array(eq_rows),
        b_eq=np.array(eq_rhs),
        bounds=bounds,
        method="highs",
    )
    if not res.success:
        return {"label": label, "success": False, "message": res.message}
    B = res.x[: idx.nb].reshape(k, n)
    P = L @ B
    sf = float(B[0] @ E)
    return {
        "label": label,
        "success": True,
        "n": n,
        "k": k,
        "delta_cap": delta_cap,
        "actual_delta": float(neg_mass_rows(P).max()),
        "sf": sf,
        "sf_over_cap": sf / delta_cap if delta_cap > 0 else None,
        "row0_support": [int(j) for j, x in enumerate(B[0]) if x > 1e-8],
        "row0_weights": [float(x) for x in B[0]],
        "idempotence_inf": float(np.max(np.abs(P @ P - P))),
        "rowsum_inf": float(np.max(np.abs(P.sum(axis=1) - 1.0))),
    }


def run_suite():
    fixed = []
    maxsf = []
    specs = []
    for amp in [0.005, 0.01, 0.02, 0.05]:
        specs.append((3, "single", 1, amp))
    for copies in [2, 5, 10, 25]:
        specs.append((3, "duplicate", copies, 0.01))
    for k in [4, 5, 6, 8, 10]:
        for graph in ["path", "cycle", "star", "complete"]:
            if graph == "complete" and k > 6:
                continue
            specs.append((k, graph, 1, 0.01))
    for k, graph, copies, amp in specs:
        L, edges = coordinate_rows(k, amp, graph, copies)
        label = f"{graph}_k{k}_copies{copies}_a{amp:g}_edges{len(edges)}"
        rec = solve_fixed_mass(L, 0.99, label)
        rec["graph"] = graph
        rec["copies"] = copies
        rec["amp"] = amp
        rec["edges"] = len(edges)
        fixed.append(rec)
    for k, graph, copies, amp in [(3, "single", 1, 0.01), (3, "duplicate", 5, 0.01), (5, "cycle", 1, 0.01), (5, "complete", 1, 0.01), (8, "cycle", 1, 0.01)]:
        L, _ = coordinate_rows(k, amp, graph, copies)
        ref = solve_fixed_mass(L, 0.99, f"reference_{graph}_k{k}_a{amp:g}")
        if not ref.get("success"):
            continue
        for mult in [1.0001, 2.0, 5.0]:
            cap = ref["delta"] * mult
            maxsf.append(solve_max_sf_row0_nonnegative(L, cap, f"{graph}_k{k}_a{amp:g}_cap_{mult:g}min"))
    return fixed, maxsf


def summarize(fixed, maxsf):
    lines = ["fixed B0 mass=0.99 LP searches:"]
    for rec in fixed:
        if not rec.get("success"):
            lines.append(f"{rec['label']}: failed {rec.get('message')}")
            continue
        mv = "skip" if rec["maxvol_max_sf_over_delta"] is None else f"{rec['maxvol_max_sf_over_delta']:.6g}"
        minor = "skip" if rec["max_abs_minor_L"] is None else f"{rec['max_abs_minor_L']:.6g}"
        lines.append(
            f"{rec['label']}: n={rec['n']} edges={rec['edges']} delta={rec['delta']:.8g} "
            f"sf/delta={rec['sf_over_delta']:.6g} maxvol_sf/delta={mv} max_minor_L={minor}"
        )
    lines.append("")
    lines.append("row0 nonnegative max-SF LP checks:")
    for rec in maxsf:
        if not rec.get("success"):
            lines.append(f"{rec['label']}: failed {rec.get('message')}")
            continue
        lines.append(
            f"{rec['label']}: cap={rec['delta_cap']:.8g} actual_delta={rec['actual_delta']:.8g} "
            f"sf/cap={rec['sf_over_cap']:.6g} support={rec['row0_support']}"
        )
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-json", default="sf_lp_results.json")
    parser.add_argument("--out-summary", default="sf_lp_summary.txt")
    args = parser.parse_args()
    fixed, maxsf = run_suite()
    Path(args.out_json).write_text(json.dumps({"fixed": fixed, "maxsf": maxsf}, indent=2, sort_keys=True))
    summary = summarize(fixed, maxsf)
    Path(args.out_summary).write_text(summary)
    print(summary, end="")


if __name__ == "__main__":
    main()
