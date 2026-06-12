#!/usr/bin/env python3
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

from sf_lp_search import LPIndex, base_constraints, coordinate_rows, neg_mass_rows


def solve_fixed_mass_return_B(L: np.ndarray, mass: float):
    n, k = L.shape
    idx = LPIndex(k, n)
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
        raise RuntimeError(res.message)
    B = res.x[: idx.nb].reshape(k, n)
    return B, L @ B


def sf_for_basis(L: np.ndarray, P: np.ndarray, basis):
    C = L[list(basis), :]
    A = L @ np.linalg.inv(C)
    vals = []
    for spos, u in enumerate(basis):
        E = []
        for j in range(L.shape[0]):
            mu = sum(max(-A[j, t], 0.0) for t in range(A.shape[1]) if t != spos)
            E.append(max(mu - (1.0 - A[j, spos]), 0.0))
        vals.append(float(np.maximum(P[u], 0.0) @ np.array(E)))
    return vals


def scan_ties(L: np.ndarray, P: np.ndarray, max_combos: int = 1000000):
    n, k = L.shape
    total = math.comb(n, k)
    if total > max_combos:
        return {"scanned": False, "combo_count": total}
    dets = []
    best = -1.0
    for inds in itertools.combinations(range(n), k):
        det = abs(float(np.linalg.det(L[list(inds), :])))
        if det > best:
            best = det
        dets.append((det, inds))
    tol = max(1e-9, 1e-8 * best)
    delta = float(neg_mass_rows(P).max())
    best_sf = -1.0
    best_basis = None
    best_s = None
    tie_count = 0
    for det, inds in dets:
        if det + tol < best:
            continue
        tie_count += 1
        vals = sf_for_basis(L, P, inds)
        local_s = int(np.argmax(vals))
        if vals[local_s] > best_sf:
            best_sf = vals[local_s]
            best_basis = inds
            best_s = local_s
    return {
        "scanned": True,
        "combo_count": total,
        "max_abs_det_L": best,
        "maxvol_tie_count": tie_count,
        "best_basis": list(best_basis),
        "best_s_pos": best_s,
        "best_pivot": int(best_basis[best_s]),
        "best_sf": best_sf,
        "delta": delta,
        "best_sf_over_delta": best_sf / delta if delta > 0 else None,
    }


def run_suite():
    records = []
    specs = []
    for k in [4, 5, 6, 8]:
        for graph in ["path", "cycle", "star"]:
            specs.append((k, graph, 1, 0.01))
    for k in [4, 5, 6]:
        specs.append((k, "complete", 1, 0.01))
    for copies in [2, 5, 10, 25]:
        specs.append((3, "duplicate", copies, 0.01))
    for k, graph, copies, amp in specs:
        L, edges = coordinate_rows(k, amp, graph, copies)
        B, P = solve_fixed_mass_return_B(L, 0.99)
        rec = scan_ties(L, P)
        rec.update(
            {
                "label": f"{graph}_k{k}_copies{copies}_a{amp:g}_edges{len(edges)}",
                "k": k,
                "n": L.shape[0],
                "graph": graph,
                "copies": copies,
                "amp": amp,
                "edges": len(edges),
                "idempotence_inf": float(np.max(np.abs(P @ P - P))),
                "rowsum_inf": float(np.max(np.abs(P.sum(axis=1) - 1.0))),
            }
        )
        records.append(rec)
    return records


def summarize(records):
    lines = ["max-volume tie scan over coefficient minors:"]
    for rec in records:
        if not rec["scanned"]:
            lines.append(f"{rec['label']}: skipped combos={rec['combo_count']}")
            continue
        lines.append(
            f"{rec['label']}: combos={rec['combo_count']} ties={rec['maxvol_tie_count']} "
            f"best_sf/delta={rec['best_sf_over_delta']:.6g} basis={rec['best_basis']} "
            f"pivot={rec['best_pivot']}"
        )
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-json", default="sf_tie_scan_results.json")
    parser.add_argument("--out-summary", default="sf_tie_scan_summary.txt")
    args = parser.parse_args()
    records = run_suite()
    Path(args.out_json).write_text(json.dumps(records, indent=2, sort_keys=True))
    summary = summarize(records)
    Path(args.out_summary).write_text(summary)
    print(summary, end="")


if __name__ == "__main__":
    main()
