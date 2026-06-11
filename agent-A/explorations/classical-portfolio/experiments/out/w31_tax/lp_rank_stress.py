#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


OUT = Path("/tmp/codex-sigma-wall/w31_tax")


def max_minor_abs(L, k):
    best = 0.0
    arg = None
    for inds in itertools.combinations(range(len(L)), k):
        val = abs(np.linalg.det(L[list(inds)]))
        if val > best:
            best = val
            arg = inds
    return best, arg


def coordinate_rows(k, a):
    rows = [np.eye(k)[s] for s in range(k)]
    foreign = list(range(1, k))
    if len(foreign) == 2:
        pairs = [(foreign[0], foreign[1])]
    else:
        pairs = list(zip(foreign, foreign[1:] + foreign[:1]))
    for t, r in pairs:
        x = np.eye(k)[0].copy()
        x[t] += a
        x[r] -= a
        rows.append(x)
        x = np.eye(k)[0].copy()
        x[t] -= a
        x[r] += a
        rows.append(x)
    return np.array(rows), pairs


def solve_case(k, a, mass):
    L, pairs = coordinate_rows(k, a)
    n = len(L)
    minor, minor_arg = max_minor_abs(L, k)
    nb = k * n
    nz = n * n
    didx = nb + nz
    total_vars = didx + 1

    def bidx(r, j):
        return r * n + j

    def zidx(i, j):
        return nb + i * n + j

    objective = np.zeros(total_vars)
    objective[didx] = 1.0
    eq_rows = []
    eq_rhs = []

    for r in range(k):
        for t in range(k):
            row = np.zeros(total_vars)
            for j in range(n):
                row[bidx(r, j)] = L[j, t]
            eq_rows.append(row)
            eq_rhs.append(1.0 if r == t else 0.0)

    signed_cols = range(k, n)
    for j in signed_cols:
        row = np.zeros(total_vars)
        row[bidx(0, j)] = 1.0
        eq_rows.append(row)
        eq_rhs.append(mass / (n - k))
    row = np.zeros(total_vars)
    row[bidx(0, 0)] = 1.0
    eq_rows.append(row)
    eq_rhs.append(1.0 - mass)
    for j in range(1, k):
        row = np.zeros(total_vars)
        row[bidx(0, j)] = 1.0
        eq_rows.append(row)
        eq_rhs.append(0.0)

    ub_rows = []
    ub_rhs = []
    for i in range(n):
        for j in range(n):
            row = np.zeros(total_vars)
            row[zidx(i, j)] = -1.0
            for r in range(k):
                row[bidx(r, j)] -= L[i, r]
            ub_rows.append(row)
            ub_rhs.append(0.0)
    for i in range(n):
        row = np.zeros(total_vars)
        for j in range(n):
            row[zidx(i, j)] = 1.0
        row[didx] = -1.0
        ub_rows.append(row)
        ub_rhs.append(0.0)

    bounds = [(None, None)] * nb + [(0.0, None)] * nz + [(0.0, None)]
    result = linprog(
        objective,
        A_ub=np.array(ub_rows),
        b_ub=np.array(ub_rhs),
        A_eq=np.array(eq_rows),
        b_eq=np.array(eq_rhs),
        bounds=bounds,
        method="highs",
    )
    if not result.success:
        return {
            "k": k,
            "a": a,
            "mass": mass,
            "success": False,
            "message": result.message,
        }

    B = result.x[:nb].reshape(k, n)
    P = L @ B
    delta = float(np.maximum(-P, 0.0).sum(axis=1).max())
    tax = 0.0
    for j in range(n):
        mu = float(np.maximum(-np.delete(L[j], 0), 0.0).sum())
        tax += max(float(B[0, j]), 0.0) * mu
    return {
        "k": k,
        "n": n,
        "edges": len(pairs),
        "a": a,
        "mass": mass,
        "success": True,
        "max_abs_minor": float(minor),
        "minor_arg": list(minor_arg),
        "delta": delta,
        "tax": float(tax),
        "tax_over_delta": float(tax / delta),
        "max_basis_neg_mass": float(np.maximum(-B, 0.0).sum(axis=1).max()),
        "idempotence_inf": float(np.max(np.abs(P @ P - P))),
        "rowsum_inf": float(np.max(np.abs(P.sum(axis=1) - 1.0))),
    }


def main():
    records = []
    for a in [0.05, 0.2]:
        for k in [3, 4, 5, 6, 8, 10]:
            if k == 3 and a == 0.2:
                continue
            records.append(solve_case(k, a, 0.99))

    (OUT / "lp_rank_stress_results.json").write_text(json.dumps(records, indent=2, sort_keys=True))
    lines = []
    for rec in records:
        if not rec["success"]:
            lines.append(f"k={rec['k']} a={rec['a']}: LP failed {rec['message']}")
            continue
        lines.append(
            f"k={rec['k']} n={rec['n']} edges={rec['edges']} a={rec['a']} "
            f"minor={rec['max_abs_minor']:.6g} delta={rec['delta']:.8g} "
            f"tax={rec['tax']:.8g} tax/delta={rec['tax_over_delta']:.6g}"
        )
    summary = "\n".join(lines) + "\n"
    (OUT / "lp_rank_stress_summary.txt").write_text(summary)
    print(summary, end="")


if __name__ == "__main__":
    main()
