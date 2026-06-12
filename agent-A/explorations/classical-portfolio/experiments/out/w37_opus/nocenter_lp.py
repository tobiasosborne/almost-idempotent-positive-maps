#!/usr/bin/env python3
"""Genuine no-center path C~2 calibration via float HiGHS LP (self-contained).

Reproduces w36 selected_family_scan's hard family: minimize total negative mass d
subject to BL=I, P=LB row-stochastic, and central-row B spread b(0,signed)=1/(2(k-2)).
Then over the foreign-units + one-signed-row charts (the theta-class reps) reports
SF_s/delta.  This is the family that pins C~2.  We also report, for the SELECTED
(min Phi) chart, the per-term transverse-tax structure to calibrate the candidate
bound B_{sj} * E_s(j) summed.
"""
from __future__ import annotations
import numpy as np
from scipy.optimize import linprog


def path_L(k, a):
    rows = [np.eye(k)[i].copy() for i in range(1, k)]
    for u, v in zip(range(1, k - 1), range(2, k)):
        p = np.eye(k)[0].copy(); p[u] += a; p[v] -= a
        m = np.eye(k)[0].copy(); m[u] -= a; m[v] += a
        rows.extend([p, m])
    return np.array(rows, float)


def solve_B(L, k):
    n = L.shape[0]
    # unknowns: B (k*n) flattened, plus d slack and per-row negative-part vars.
    # We model B entries free; P=L@B; constraints BL=I, rowsum(P)=1, and
    # negativity: introduce z_{i,l} >= max(-P_{i,l},0) via z>=-P_{i,l}, z>=0, and
    # d >= sum_l z_{i,l} for each row i; minimize d.
    nb = k * n
    nz = n * n   # z over P entries (n x n)
    nvar = nb + nz + 1
    di = nvar - 1
    def bidx(t, j): return t * n + j
    def zidx(i, l): return nb + i * n + l
    A_eq = []; b_eq = []
    # BL = I
    for i in range(k):
        for j in range(k):
            row = np.zeros(nvar)
            for t in range(n):
                row[bidx(i, t)] += L[t, j]
            A_eq.append(row); b_eq.append(1.0 if i == j else 0.0)
    # central-row spread: b(0,j)=1/(2(k-2)) for signed rows j>=k-1
    val = 1.0 / (2 * (k - 2))
    for j in range(k - 1, n):
        row = np.zeros(nvar); row[bidx(0, j)] = 1.0
        A_eq.append(row); b_eq.append(val)
    # row sums of P = 1: sum_l P_{i,l}=1 => sum_l sum_t L[i,t] B[t,l] =1
    for i in range(n):
        row = np.zeros(nvar)
        for l in range(n):
            for t in range(k):
                row[bidx(t, l)] += L[i, t]
        A_eq.append(row); b_eq.append(1.0)
    A_ub = []; b_ub = []
    # z_{i,l} >= -P_{i,l}  => -P_{i,l} - z <=0 => -sum_t L[i,t]B[t,l] - z <=0
    for i in range(n):
        for l in range(n):
            row = np.zeros(nvar)
            for t in range(k):
                row[bidx(t, l)] += -L[i, t]  # -P
            row[zidx(i, l)] = -1.0
            A_ub.append(row); b_ub.append(0.0)
    # d >= sum_l z_{i,l} => sum_l z - d <=0
    for i in range(n):
        row = np.zeros(nvar)
        for l in range(n):
            row[zidx(i, l)] = 1.0
        row[di] = -1.0
        A_ub.append(row); b_ub.append(0.0)
    c = np.zeros(nvar); c[di] = 1.0
    bounds = [(None, None)] * nb + [(0.0, None)] * nz + [(0.0, None)]
    res = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                  A_eq=np.array(A_eq), b_eq=np.array(b_eq), bounds=bounds, method="highs")
    if not res.success:
        raise RuntimeError(res.message)
    B = res.x[:nb].reshape(k, n)
    return B


def sf_terms(L, P, basis):
    coords = L @ np.linalg.inv(L[basis, :])  # coords[j,t]=a_t(j)
    out = []
    for s, u in enumerate(basis):
        e = np.zeros(coords.shape[0])
        for j, row in enumerate(coords):
            mu = sum(max(-row[t], 0.0) for t in range(coords.shape[1]) if t != s)
            e[j] = max(mu - (1.0 - row[s]), 0.0)
        out.append(float(np.maximum(P[u], 0.0) @ e))
    return out, coords


def main():
    for k in [6, 8, 10, 12, 20]:
        L = path_L(k, 0.01)
        B = solve_B(L, k)
        P = L @ B
        delta = float(np.maximum(-P, 0.0).sum(axis=1).max())
        # theta-class reps: foreign units (0..k-2) + one signed row
        ratios = []
        sel = None
        for j in range(k - 1, L.shape[0]):
            basis = list(range(k - 1)) + [j]
            sfv, coords = sf_terms(L, P, basis)
            r = max(sfv) / delta
            ratios.append(r)
            if sel is None or r < sel[0]:
                sel = (r, basis, sfv)
        print(f"k={k} delta={delta:.6g} selected_ratio={min(ratios):.6f} "
              f"worst_ratio={max(ratios):.6f}")
        # for selected chart, print the max-s transverse tax B_sj*E breakdown
        r, basis, sfv = sel
        s = int(np.argmax(sfv))
        coords = L @ np.linalg.inv(L[basis, :])
        u = basis[s]
        contribs = []
        for j, row in enumerate(coords):
            w = P[u, j]
            if w <= 1e-12: continue
            mu = sum(max(-row[t], 0.0) for t in range(len(row)) if t != s)
            E = max(mu - (1.0 - row[s]), 0.0)
            if E > 1e-12:
                contribs.append((j, round(w, 5), round(row[s], 5), round(E, 5), round(w * E / delta, 5)))
        print(f"   selected s={s} u_s={u}: {len(contribs)} excess terms; "
              f"top wE/delta: {sorted([c[4] for c in contribs], reverse=True)[:6]}")
        print(f"   sample terms (j,B_sj,a_s,E,wE/delta): {contribs[:6]}")


if __name__ == "__main__":
    main()
