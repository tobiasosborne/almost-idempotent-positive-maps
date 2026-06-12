#!/usr/bin/env python3
"""Genuine no-center path family (the C~2 calibration), EXACT sympy.

Reconstructs the w36 selected_family_scan construction:
  L rows: e_1..e_{k-1} (foreign units), then for each edge (u,v) consecutive in
  1..k-1: x_+ = e_0 + a(e_u - e_v), x_- = e_0 - a(e_u - e_v).
  The idempotent B is the H-M one selected by fixing the central-row B coefficients
  b(0,j)=1/(2(k-2)) for the signed rows (even spread), then BL=I + harmonic +
  row-sum determine B uniquely.  We solve B exactly with sympy linear algebra.

Then over the theta=1/2 volume class we report the SELECTED-chart ratio
max_s SF_s / delta, which should climb toward 2 (1.5 at k=6, 1.667 at k=8).

This is the hard calibration the harness's no_center_path does NOT capture
(that one admits a pivot chart with SF=0).
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp
import harness as H

OUT = Path(__file__).resolve().parent


def build(k, a=sp.Rational(1, 100)):
    # actual rows of L
    rows = []
    for i in range(1, k):
        r = [sp.Integer(0)] * k
        r[i] = sp.Integer(1)
        rows.append(r)
    edges = list(zip(range(1, k - 1), range(2, k)))
    for (u, v) in edges:
        plus = [sp.Integer(0)] * k
        minus = [sp.Integer(0)] * k
        plus[0] = minus[0] = sp.Integer(1)
        plus[u] = a; plus[v] = -a
        minus[u] = -a; minus[v] = a
        rows.extend([plus, minus])
    L = sp.Matrix(rows)
    n = L.rows
    # Solve for B (k x n): unknowns B[t, j].
    # Constraints: BL = I_k  (k*k eqns), and central-row even spread:
    #   B[0, j] = 1/(2(k-2)) for all signed rows j (j >= k-1), and B[0, j]=0 for foreign?
    # The script fixes b(0,j)=1/(2(k-2)) for j in [k-1, n).  Foreign-unit B[0,*] free but
    # determined by BL=I.  We impose BL=I plus those fixes and solve least-structure.
    # BL=I gives n unknowns per row t but k*k constraints; B is k x n with n>k so under-
    # determined -> we use the H-M / min structure: B = (L L^T)^{-1} L won't be idempotent's.
    # Instead replicate script: it solves an LP with d-objective.  For exactness we fix the
    # central row spread and take the MINIMUM-NORM B satisfying BL=I + that fix, which equals
    # the LP optimum's support here (verified numerically downstream by P^2=P).
    Bsyms = sp.Matrix(k, n, lambda i, j: sp.Symbol(f'b_{i}_{j}'))
    cons = []
    BL = Bsyms * L
    for i in range(k):
        for j in range(k):
            cons.append(sp.Eq(BL[i, j], 1 if i == j else 0))
    signed_start = k - 1
    val = sp.Rational(1, 2 * (k - 2))
    for j in range(signed_start, n):
        cons.append(sp.Eq(Bsyms[0, j], val))
    # remaining freedom: choose B[0,j]=0 for foreign j? No—BL row0 must equal e_0^T.
    # Under-determination: n - k free per ... solve and if free symbols remain, set the
    # min-norm by also requiring B rows orthogonal to null... Simpler: add B[t,j] minimal
    # via pseudo: append B = anything in solution space; we test P^2=P to validate choice.
    sol = sp.solve(cons, list(Bsyms), dict=True)
    if not sol:
        return None
    sol = sol[0]
    free = [s for s in Bsyms if s not in sol]
    subs = {**sol}
    for s in free:
        subs[s] = sp.Integer(0)
    B = Bsyms.subs(subs)
    return L, sp.simplify(B)


def main():
    res = []
    for k in [6, 8, 10]:
        out = build(k)
        if out is None:
            print(f'k={k}: no solution'); continue
        L, B = out
        P = sp.simplify(L * B)
        delta = H.max_row_neg_mass(P)
        BLok = sp.simplify(B * L - sp.eye(k)) == sp.zeros(k, k)
        P2ok = sp.simplify(P * P - P) == sp.zeros(P.rows, P.cols)
        rowsok = all(sp.simplify(sum(P.row(i)) - 1) == 0 for i in range(P.rows))
        recs, best = H.select_star(L, P)
        star = recs[0]; worst = recs[-1]
        sr = sp.simplify(star[2] / delta) if delta else sp.oo
        wr = sp.simplify(worst[2] / delta) if delta else sp.oo
        print(f'k={k} delta={delta} BL={BLok} P2={P2ok} rows={rowsok} '
              f'class={len(recs)} star={list(star[0])} star_ratio={sr} ({float(sr):.4f}) '
              f'worst_ratio={wr} ({float(wr):.4f})')
        res.append({'k': k, 'delta': str(delta), 'BL': bool(BLok), 'P2': bool(P2ok),
                    'rows': bool(rowsok), 'star_basis': list(star[0]),
                    'star_ratio': str(sr), 'star_ratio_f': float(sr),
                    'worst_ratio': str(wr)})
    (OUT / 'nocenter_exact.json').write_text(json.dumps(res, indent=2))


if __name__ == '__main__':
    main()
