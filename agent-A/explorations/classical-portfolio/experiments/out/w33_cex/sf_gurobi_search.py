#!/usr/bin/env python3
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import gurobipy as gp
import numpy as np
from gurobipy import GRB


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
    signed = []
    for u, v in edges:
        plus = np.eye(k)[0].copy()
        plus[u] += amp
        plus[v] -= amp
        minus = np.eye(k)[0].copy()
        minus[u] -= amp
        minus[v] += amp
        signed.extend([len(rows), len(rows) + 1])
        rows.extend([plus, minus])
    return np.array(rows, dtype=float), edges, signed


def excesses(L: np.ndarray, s: int = 0):
    out = []
    for row in L:
        mu = sum(max(-row[t], 0.0) for t in range(L.shape[1]) if t != s)
        deficit = 1.0 - row[s]
        out.append(max(mu - deficit, 0.0))
    return np.array(out)


def combo_count(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)


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


def neg_mass_rows(P: np.ndarray):
    return np.maximum(-P, 0.0).sum(axis=1)


def maxvol_float(P: np.ndarray, limit: int = 200000):
    n = P.shape[0]
    k = int(np.linalg.matrix_rank(P, tol=1e-9))
    total = combo_count(n, k)
    if total > limit:
        return None, None, total
    best = -1e300
    arg = None
    for inds in itertools.combinations(range(n), k):
        R = P[list(inds), :]
        if np.linalg.matrix_rank(R, tol=1e-9) < k:
            continue
        G = R @ R.T
        sign, logdet = np.linalg.slogdet(G)
        if sign > 0 and logdet > best:
            best = logdet
            arg = inds
    return arg, best, total


def coeffs_float(P: np.ndarray, pivots):
    basis = P[list(pivots), :]
    return P @ basis.T @ np.linalg.inv(basis @ basis.T)


def sf_float(P: np.ndarray, pivots):
    A = coeffs_float(P, pivots)
    vals = []
    for spos, u in enumerate(pivots):
        E = []
        for j in range(P.shape[0]):
            mu = sum(max(-A[j, t], 0.0) for t in range(A.shape[1]) if t != spos)
            E.append(max(mu - (1.0 - A[j, spos]), 0.0))
        vals.append(float(np.maximum(P[u], 0.0) @ np.array(E)))
    return vals


def solve_fixed_mass(L: np.ndarray, mass: float, label: str):
    n, k = L.shape
    E = excesses(L, 0)
    model = gp.Model(f"fixed_mass_{label}")
    model.Params.OutputFlag = 0
    B = model.addVars(k, n, lb=-GRB.INFINITY, ub=GRB.INFINITY, name="B")
    z = model.addVars(n, n, lb=0.0, name="z")
    delta = model.addVar(lb=0.0, name="delta")

    for r in range(k):
        for t in range(k):
            model.addConstr(gp.quicksum(B[r, j] * L[j, t] for j in range(n)) == (1.0 if r == t else 0.0))

    signed_count = n - k
    fixed_b0 = [0.0] * n
    fixed_b0[0] = 1.0 - mass
    for j in range(k, n):
        fixed_b0[j] = mass / signed_count
    for j, val in enumerate(fixed_b0):
        model.addConstr(B[0, j] == val)

    for i in range(n):
        for j in range(n):
            pij = gp.quicksum(L[i, r] * B[r, j] for r in range(k))
            model.addConstr(z[i, j] >= -pij)
        model.addConstr(gp.quicksum(z[i, j] for j in range(n)) <= delta)

    model.setObjective(delta, GRB.MINIMIZE)
    model.optimize()
    if model.Status != GRB.OPTIMAL:
        return {"label": label, "success": False, "status": model.Status}

    Bv = np.array([[B[r, j].X for j in range(n)] for r in range(k)])
    P = L @ Bv
    piv, _, total = maxvol_float(P)
    if piv is None:
        sf_recomputed = None
        pivots = None
    else:
        sf_recomputed = sf_float(P, piv)
        pivots = list(piv)
    minor, minor_arg, minor_total = max_minor_abs(L)
    sf_intended = float(np.maximum(Bv[0], 0.0) @ E)
    delta_actual = float(neg_mass_rows(P).max())
    return {
        "label": label,
        "success": True,
        "n": n,
        "k": k,
        "mass": mass,
        "intended_sf": sf_intended,
        "delta": delta_actual,
        "sf_over_delta": sf_intended / delta_actual if delta_actual > 0 else None,
        "max_row_neg_mass_B": float(np.maximum(-Bv, 0.0).sum(axis=1).max()),
        "idempotence_inf": float(np.max(np.abs(P @ P - P))),
        "rowsum_inf": float(np.max(np.abs(P.sum(axis=1) - 1.0))),
        "max_abs_minor_L": minor,
        "max_abs_minor_arg_L": list(minor_arg) if minor_arg is not None else None,
        "minor_combo_count": minor_total,
        "maxvol_pivots": pivots,
        "maxvol_combo_count": total,
        "maxvol_sf": sf_recomputed,
        "maxvol_max_sf_over_delta": (max(sf_recomputed) / delta_actual if sf_recomputed is not None and delta_actual > 0 else None),
    }


def solve_milp_max_sf(L: np.ndarray, delta_cap: float, label: str, time_limit: float = 20.0):
    n, k = L.shape
    E = excesses(L, 0)
    model = gp.Model(f"milp_sf_{label}")
    model.Params.OutputFlag = 0
    model.Params.TimeLimit = time_limit
    model.Params.MIPGap = 1e-8
    B = model.addVars(k, n, lb=-delta_cap, ub=1.0 + delta_cap, name="B")
    z = model.addVars(n, n, lb=0.0, name="z")
    p = model.addVars(n, lb=0.0, ub=1.0 + delta_cap, name="p")
    y = model.addVars(n, vtype=GRB.BINARY, name="y")
    for r in range(k):
        for t in range(k):
            model.addConstr(gp.quicksum(B[r, j] * L[j, t] for j in range(n)) == (1.0 if r == t else 0.0))
    for i in range(n):
        for j in range(n):
            pij = gp.quicksum(L[i, r] * B[r, j] for r in range(k))
            model.addConstr(z[i, j] >= -pij)
        model.addConstr(gp.quicksum(z[i, j] for j in range(n)) <= delta_cap)
    for j in range(n):
        b = B[0, j]
        model.addConstr(b <= (1.0 + delta_cap) * y[j])
        model.addConstr(b >= -delta_cap * (1 - y[j]))
        model.addConstr(p[j] >= b)
        model.addConstr(p[j] <= b + delta_cap * (1 - y[j]))
        model.addConstr(p[j] <= (1.0 + delta_cap) * y[j])
    model.setObjective(gp.quicksum(float(E[j]) * p[j] for j in range(n)), GRB.MAXIMIZE)
    model.optimize()
    if model.Status not in (GRB.OPTIMAL, GRB.TIME_LIMIT):
        return {"label": label, "success": False, "status": model.Status}
    Bv = np.array([[B[r, j].X for j in range(n)] for r in range(k)])
    P = L @ Bv
    sf = float(np.maximum(Bv[0], 0.0) @ E)
    return {
        "label": label,
        "success": True,
        "status": model.Status,
        "objective_bound": float(model.ObjBound),
        "objective": float(model.ObjVal),
        "n": n,
        "k": k,
        "delta_cap": delta_cap,
        "intended_sf": sf,
        "sf_over_cap": sf / delta_cap if delta_cap > 0 else None,
        "actual_delta": float(neg_mass_rows(P).max()),
        "idempotence_inf": float(np.max(np.abs(P @ P - P))),
        "rowsum_inf": float(np.max(np.abs(P.sum(axis=1) - 1.0))),
        "row0_positive_mass": float(np.maximum(Bv[0], 0.0).sum()),
        "row0_negative_mass": float(np.maximum(-Bv[0], 0.0).sum()),
        "positive_support": [int(j) for j in range(n) if Bv[0, j] > 1e-8],
    }


def run_suite():
    records = []
    milp_records = []
    specs = []
    for amp in [0.005, 0.01, 0.02, 0.05]:
        specs.append((3, "single", 1, amp))
    for copies in [2, 5, 10, 25, 50]:
        specs.append((3, "duplicate", copies, 0.01))
    for k in [4, 5, 6, 8]:
        for graph in ["path", "cycle", "star", "complete"]:
            specs.append((k, graph, 1, 0.01))
    for k, graph, copies, amp in specs:
        L, edges, signed = coordinate_rows(k, amp, graph, copies)
        label = f"{graph}_k{k}_copies{copies}_a{amp:g}_edges{len(edges)}"
        rec = solve_fixed_mass(L, 0.99, label)
        rec["edges"] = len(edges)
        rec["graph"] = graph
        rec["amp"] = amp
        rec["copies"] = copies
        records.append(rec)
    for k, graph, copies, amp in [(3, "single", 1, 0.01), (3, "duplicate", 5, 0.01), (5, "cycle", 1, 0.01), (5, "complete", 1, 0.01)]:
        L, _, _ = coordinate_rows(k, amp, graph, copies)
        fixed = solve_fixed_mass(L, 0.99, f"milp_reference_{graph}_k{k}_a{amp:g}")
        cap = fixed["delta"] * 1.0001
        milp_records.append(solve_milp_max_sf(L, cap, f"{graph}_k{k}_a{amp:g}_cap_min"))
        milp_records.append(solve_milp_max_sf(L, 2.0 * fixed["delta"], f"{graph}_k{k}_a{amp:g}_cap_2min"))
    return records, milp_records


def summarize(records, milp_records):
    lines = ["fixed-mass LP searches:"]
    for rec in records:
        if not rec.get("success"):
            lines.append(f"{rec['label']}: failed status={rec.get('status')}")
            continue
        mv = rec["maxvol_max_sf_over_delta"]
        mv_s = "skip" if mv is None else f"{mv:.6g}"
        minor = rec["max_abs_minor_L"]
        minor_s = "skip" if minor is None else f"{minor:.6g}"
        lines.append(
            f"{rec['label']}: n={rec['n']} edges={rec['edges']} delta={rec['delta']:.8g} "
            f"sf/delta={rec['sf_over_delta']:.6g} maxvol_sf/delta={mv_s} "
            f"max_minor_L={minor_s}"
        )
    lines.append("")
    lines.append("MILP max-SF checks:")
    for rec in milp_records:
        if not rec.get("success"):
            lines.append(f"{rec['label']}: failed status={rec.get('status')}")
            continue
        lines.append(
            f"{rec['label']}: cap={rec['delta_cap']:.8g} actual_delta={rec['actual_delta']:.8g} "
            f"sf/cap={rec['sf_over_cap']:.6g} row0_pos={rec['row0_positive_mass']:.6g} "
            f"support={rec['positive_support']}"
        )
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-json", default="sf_gurobi_results.json")
    parser.add_argument("--out-summary", default="sf_gurobi_summary.txt")
    args = parser.parse_args()
    records, milp_records = run_suite()
    data = {"fixed_mass": records, "milp": milp_records}
    Path(args.out_json).write_text(json.dumps(data, indent=2, sort_keys=True))
    summary = summarize(records, milp_records)
    Path(args.out_summary).write_text(summary)
    print(summary, end="")


if __name__ == "__main__":
    main()
