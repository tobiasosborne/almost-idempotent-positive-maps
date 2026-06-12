#!/usr/bin/env python3
"""w34_scaling: dense transverse-pair SF/delta scaling in m at FIXED delta-cap.

Family (w33_sf_geom section 5): k = 2m+1 representatives e_0..e_{2m};
two extra coefficient rows x_pm = e_0 +- a*v, v = sum_{1..m} e_t - sum_{m+1..2m} e_t.
L is (2m+3) x (2m+1), rows sum to 1, max-volume minors <= 1 for a <= 1/2.

Structural LP (orchestrator, local, HiGHS): variables B ((2m+1) x d, d = 2m+3)
and epigraph z (d x d). Constraints: BL = I, row sums of B = 1, z >= -(LB),
z >= 0, sum_j z_ij <= cap for every row i. Restriction: B_0 >= 0 (the w33
active solutions had nonneg B_0; restricting only LOWERS the reported max, so
ratios here are LOWER BOUNDS on the true fixed-support max).
Objective: maximize SF = m*a*(B_{0,x+} + B_{0,x-})  [E_0 = m*a on x_pm, 0 else].

Question: at fixed cap, does max SF/cap grow with m (=> dimension-free SF false
at fixed delta_0) or saturate (=> fit C(delta_0))?
"""
import json
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix

OUT = Path(__file__).resolve().parent


def build_L(m, a):
    k = 2 * m + 1
    d = k + 2
    L = np.zeros((d, k))
    L[:k, :] = np.eye(k)
    v = np.zeros(k)
    v[1:m + 1] = 1.0
    v[m + 1:k] = -1.0
    L[k] = np.eye(k)[0] + a * v
    L[k + 1] = np.eye(k)[0] - a * v
    return L


def solve(m, a, cap):
    k = 2 * m + 1
    d = k + 2
    L = build_L(m, a)
    nB = k * d
    nZ = d * d
    n = nB + nZ

    def B_idx(r, j):
        return r * d + j

    def z_idx(i, j):
        return nB + i * d + j

    # objective: maximize m*a*(B[0, k] + B[0, k+1])
    c = np.zeros(n)
    c[B_idx(0, k)] = -m * a
    c[B_idx(0, k + 1)] = -m * a

    A_eq = lil_matrix((k * k + k, n))
    b_eq = np.zeros(k * k + k)
    row = 0
    # BL = I  : sum_j B[r,j] * L[j,t] = delta_rt
    for r in range(k):
        for t in range(k):
            for j in range(d):
                if L[j, t] != 0.0:
                    A_eq[row, B_idx(r, j)] = L[j, t]
            b_eq[row] = 1.0 if r == t else 0.0
            row += 1
    # row sums of B = 1
    for r in range(k):
        for j in range(d):
            A_eq[row, B_idx(r, j)] = 1.0
        b_eq[row] = 1.0
        row += 1

    # inequalities: z_ij >= -(LB)_ij  i.e.  -(LB)_ij - z_ij <= 0
    # (LB)_ij = sum_t L[i,t] B[t,j]
    A_ub = lil_matrix((d * d + d, n))
    b_ub = np.zeros(d * d + d)
    row = 0
    for i in range(d):
        for j in range(d):
            for t in range(k):
                if L[i, t] != 0.0:
                    A_ub[row, B_idx(t, j)] = -L[i, t]
            A_ub[row, z_idx(i, j)] = -1.0
            row += 1
    # sum_j z_ij <= cap
    for i in range(d):
        for j in range(d):
            A_ub[row, z_idx(i, j)] = 1.0
        b_ub[row] = cap
        row += 1

    bounds = []
    for r in range(k):
        for j in range(d):
            if r == 0:
                bounds.append((0.0, None))      # B_0 >= 0 restriction
            else:
                bounds.append((None, None))
    bounds += [(0.0, None)] * nZ                # z >= 0

    res = linprog(c, A_ub=A_ub.tocsr(), b_ub=b_ub, A_eq=A_eq.tocsr(),
                  b_eq=b_eq, bounds=bounds, method="highs")
    if not res.success:
        return None
    sf = -res.fun
    return sf


def main():
    caps = [0.05, 0.1, 0.2, 6 / 17, 0.5]
    ms = [2, 3, 5, 8, 12, 18, 25]
    amps = [0.1, 0.25, 0.4, 0.5]
    records = []
    lines = []
    for cap in caps:
        for m in ms:
            best = (0.0, None)
            for a in amps:
                sf = solve(m, a, cap)
                if sf is not None and sf > best[0]:
                    best = (sf, a)
            ratio = best[0] / cap
            rec = {"cap": cap, "m": m, "k": 2 * m + 1,
                   "best_a": best[1], "SF": best[0], "ratio": ratio}
            records.append(rec)
            line = (f"cap={cap:.6f} m={m:2d} k={2*m+1:2d} "
                    f"best_a={best[1]} SF={best[0]:.6f} ratio={ratio:.6f}")
            print(line, flush=True)
            lines.append(line)
    (OUT / "dense_scaling_results.json").write_text(json.dumps(records, indent=1))
    (OUT / "dense_scaling_summary.txt").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    sys.exit(main())
