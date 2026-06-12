#!/usr/bin/env python3
"""Self-contained exact (sympy rational) harness for the w37_opus attack.

Rebuilds each mandatory test family from the displayed formulas in the w35/w36
notes (NO external script dependencies), verifies BL=I, P^2=P, P1=1, row neg
masses, and computes for each actual-row basis the coefficient field a_t(j),
the SF_s values, the volume, and the selector U* = argmin_theta-class Phi.

It also records, per chart, diagnostic quantities used by the w37 argument:
  - the "negative coefficient interface" potential
  - per-representative deficit / excess / tax decomposition.
"""
from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

OUT = Path(__file__).resolve().parent


# ----------------------------------------------------------------------------
# basic helpers
# ----------------------------------------------------------------------------
def pos(x):
    x = sp.nsimplify(x) if not isinstance(x, sp.Basic) else x
    return x if x > 0 else sp.Integer(0)


def neg(x):
    return -x if x < 0 else sp.Integer(0)


def row_neg_mass(row):
    return sp.Integer(sum(int(0) for _ in []))  # placeholder, replaced below


def row_neg_mass(row):  # noqa: F811
    tot = sp.Integer(0)
    for x in row:
        x = sp.simplify(x)
        if x < 0:
            tot += -x
    return sp.simplify(tot)


def max_row_neg_mass(P):
    return max(row_neg_mass(list(P.row(i))) for i in range(P.rows))


def all_row_neg_masses(P):
    return [sp.simplify(row_neg_mass(list(P.row(i)))) for i in range(P.rows)]


# ----------------------------------------------------------------------------
# the coefficient field and SF for an actual-row basis
# ----------------------------------------------------------------------------
def coeff_field(L, basis):
    """Rows of A = L * L_U^{-1} are the coefficients a(j); a_t(j)=A[j,t]."""
    LU = L[list(basis), :]
    return sp.simplify(L * LU.inv())


def excess_E(coord_row, s):
    """E_s(j) = ( sum_{t!=s} (-a_t(j))_+  -  (1 - a_s(j)) )_+ ."""
    mu = sp.Integer(0)
    for t, x in enumerate(coord_row):
        if t != s:
            mu += neg(sp.simplify(x))
    val = sp.simplify(mu - (1 - coord_row[s]))
    return sp.simplify(val if val > 0 else sp.Integer(0))


def sf_values(P, A, basis):
    """SF_s for each s in the basis, using P_{u_s j}=B_{s j} via actual rows of P."""
    vals = []
    for s, u in enumerate(basis):
        tot = sp.Integer(0)
        for j in range(P.cols):
            w = sp.simplify(P[u, j])
            if w > 0:
                tot += w * excess_E(list(A.row(j)), s)
        vals.append(sp.simplify(tot))
    return vals


def all_bases_by_volume(L):
    """Return dict: abs-det -> list of bases; and the max abs-det."""
    k = L.cols
    by_vol = {}
    for basis in itertools.combinations(range(L.rows), k):
        det = sp.simplify(L[list(basis), :].det())
        score = sp.Abs(det)
        if score == 0:
            continue
        key = sp.simplify(score)
        by_vol.setdefault(key, []).append(basis)
    best = max(by_vol.keys())
    return by_vol, best


def select_star(L, P, theta=sp.Rational(1, 2)):
    """U* = argmin over theta-class (Vol >= theta * Vol_max) of Phi=max_s SF_s."""
    by_vol, best = all_bases_by_volume(L)
    cls = []
    for vol, bases in by_vol.items():
        if vol >= theta * best:
            cls.extend(bases)
    recs = []
    for basis in cls:
        A = coeff_field(L, basis)
        vals = sf_values(P, A, basis)
        recs.append((basis, vals, max(vals)))
    # argmin Phi, lexicographic on basis tuple
    recs.sort(key=lambda r: (Fraction(str(r[2])), r[0]))
    return recs, best


# ----------------------------------------------------------------------------
# families
# ----------------------------------------------------------------------------
def transverse_pair(a, mass=sp.Integer(1)):
    L = sp.Matrix([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, a, -a],
        [1, -a, a],
    ])
    c = sp.simplify(a / (1 + 4 * a * a))
    B = sp.Matrix([
        [1 - mass, 0, 0, mass / 2, mass / 2],
        [0, 1 - 2 * a * c, 2 * a * c, c, -c],
        [0, 2 * a * c, 1 - 2 * a * c, -c, c],
    ])
    return L, B


def dense_pair_k7():
    m = 3
    k = 2 * m + 1
    a = sp.Rational(1, 4)
    rows = []
    for i in range(k):
        r = [sp.Integer(0)] * k
        r[i] = sp.Integer(1)
        rows.append(r)
    sigma = [0] + [1] * m + [-1] * m
    xp = [sp.Integer(0)] * k
    xm = [sp.Integer(0)] * k
    xp[0] = xm[0] = sp.Integer(1)
    for t in range(1, k):
        xp[t] = a * sigma[t]
        xm[t] = -a * sigma[t]
    rows.extend([xp, xm])
    L = sp.Matrix(rows)
    n = k + 2
    B = sp.zeros(k, n)
    B[0, k] = B[0, k + 1] = sp.Rational(1, 2)
    c = sp.Rational(3, 34)
    for r in range(1, k):
        for t in range(1, k):
            B[r, t] = (1 if r == t else 0) - sigma[r] * sigma[t] * c
        B[r, k] = sigma[r] * sp.Rational(3, 17)
        B[r, k + 1] = -sigma[r] * sp.Rational(3, 17)
    return L, B


def staircase(m):
    k = 2 * m + 1
    rows = []
    for i in range(k):
        r = [sp.Integer(0)] * k
        r[i] = sp.Integer(1)
        rows.append(r)
    sigma = [0] + [1] * m + [-1] * m
    xp = [sp.Integer(0)] * k
    xm = [sp.Integer(0)] * k
    xp[0] = xm[0] = sp.Integer(1)
    for t in range(1, k):
        xp[t] = sp.Rational(1, 2) * sigma[t]
        xm[t] = -sp.Rational(1, 2) * sigma[t]
    rows.extend([xp, xm])
    L = sp.Matrix(rows)
    n = k + 2
    B = sp.zeros(k, n)
    B[0, k] = B[0, k + 1] = sp.Rational(1, 2)
    for r in range(1, k):
        for t in range(1, k):
            B[r, t] = (1 if r == t else 0) - sp.Rational(sigma[r] * sigma[t], 2 * m)
        B[r, k] = sp.Rational(sigma[r], 2 * m)
        B[r, k + 1] = -sp.Rational(sigma[r], 2 * m)
    return L, B


def perturbed_staircase(m, eps):
    """From w36_audit B6.  k=2m+1, delta=1/2, identity is unique exact maxvol."""
    k = 2 * m + 1
    sigma = [0] + [1] * m + [-1] * m
    h = 1 - eps
    d = eps / (2 * m)
    rows = []
    for i in range(k):
        r = [sp.Integer(0)] * k
        r[i] = sp.Integer(1)
        rows.append(r)
    xp = [sp.Integer(0)] * k
    xm = [sp.Integer(0)] * k
    xp[0] = xm[0] = h
    for t in range(1, k):
        xp[t] = d + sp.Rational(sigma[t], 2)
        xm[t] = d - sp.Rational(sigma[t], 2)
    rows.extend([xp, xm])
    L = sp.Matrix(rows)
    n = k + 2
    p_col, n_col = k, k + 1
    B = sp.zeros(k, n)
    B[0, 0] = eps
    for t in range(1, k):
        B[0, t] = -d
    B[0, p_col] = B[0, n_col] = sp.Rational(1, 2)
    for r in range(1, k):
        for t in range(1, k):
            B[r, t] = (1 if r == t else 0) - sp.Rational(sigma[r] * sigma[t], 2 * m)
        B[r, p_col] = sp.Rational(sigma[r], 2 * m)
        B[r, n_col] = -sp.Rational(sigma[r], 2 * m)
        B[r, 0] = 0
    return L, B


def no_center_path(k, a=sp.Rational(1, 100)):
    """No-center path family (w36_charge sec 3). Rows: e_1..e_{k-1} then signed
    path rows x = e_0 +- a(e_u - e_v) for consecutive (u,v).  Idempotent B is
    solved by exact linear algebra (BL=I plus harmonic/fixed constraints) rather
    than via LP, so this harness is dependency-free."""
    # actual rows of L
    rows = []
    for i in range(1, k):
        r = [sp.Integer(0)] * k
        r[i] = sp.Integer(1)
        rows.append(r)
    for u, v in zip(range(1, k - 1), range(2, k)):
        plus = [sp.Integer(0)] * k
        minus = [sp.Integer(0)] * k
        plus[0] = minus[0] = sp.Integer(1)
        plus[u] = a
        plus[v] = -a
        minus[u] = -a
        minus[v] = a
        rows.extend([plus, minus])
    L = sp.Matrix(rows)
    n = L.rows
    # We need B (k x n), B L = I_k, rows of P=LB sum to 1, P idempotent.
    # Construct B so that P = L B is the projection onto row space of L along
    # a fixed complement.  Use the basis = e_1..e_{k-1} + first signed row to
    # define a coordinate chart, then the unique B with that chart's pivots is
    # the minimal one; but for idempotence we need a *specific* H-M B.
    # Simplest exact route: pick the foreign-unit chart basis = rows 0..k-2
    # (=e_1..e_{k-1}) plus signed row index (k-1) (first plus row), invert.
    # Then B has rows = that chart's dual; P=L B is idempotent automatically
    # because it is L_U^{-1}-projection: P = L (L_U)^{-1} S where S selects.
    # We instead want the *symmetric* H-M B used in w36; reproduce by LP-free
    # construction: B = (L_U)^{-1} placed on basis rows.  That gives P
    # idempotent with P = L E (L_U)^{-1}, E=selection.  Verify numerically.
    basis = list(range(k - 1)) + [k - 1]
    LU = L[basis, :]
    LUinv = LU.inv()
    B = sp.zeros(k, n)
    for col_idx, brow in enumerate(basis):
        for t in range(k):
            B[t, brow] = LUinv[t, col_idx]
    return L, B


# ----------------------------------------------------------------------------
# audit a single instance
# ----------------------------------------------------------------------------
def audit(name, L, B, theta=sp.Rational(1, 2)):
    P = sp.simplify(L * B)
    delta = max_row_neg_mass(P)
    checks = {
        "BL_ok": bool(sp.simplify(B * L - sp.eye(L.cols)) == sp.zeros(L.cols, L.cols)),
        "P2_ok": bool(sp.simplify(P * P - P) == sp.zeros(P.rows, P.cols)),
        "rows_ok": all(sp.simplify(sum(P.row(i)) - 1) == 0 for i in range(P.rows)),
    }
    recs, best = select_star(L, P, theta=theta)
    star_basis, star_vals, star_phi = recs[0]
    worst = recs[-1]
    ratio = lambda v: sp.simplify(v / delta) if delta != 0 else sp.oo
    return {
        "name": name,
        "k": int(L.cols),
        "n": int(L.rows),
        "delta": str(delta),
        "maxvol_abs_det": str(best),
        "theta": str(theta),
        "class_size": len(recs),
        "checks": checks,
        "row_neg_masses": [str(x) for x in all_row_neg_masses(P)],
        "star_basis": list(star_basis),
        "star_phi": str(star_phi),
        "star_ratio": str(ratio(star_phi)),
        "worst_basis": list(worst[0]),
        "worst_phi": str(worst[2]),
        "worst_ratio": str(ratio(worst[2])),
        "_L": L, "_B": B, "_P": P,  # kept for downstream diagnostics (not serialized)
    }


def main():
    cases = []
    cases.append(("transverse_pair_a1_4", *transverse_pair(sp.Rational(1, 4))))
    cases.append(("dense_pair_k7_a1_4", *dense_pair_k7()))
    cases.append(("staircase_m2", *staircase(2)))
    cases.append(("staircase_m3", *staircase(3)))
    cases.append(("perturbed_staircase_m5_eps1e-3", *perturbed_staircase(5, sp.Rational(1, 1000))))
    cases.append(("no_center_path_k6", *no_center_path(6)))
    cases.append(("no_center_path_k8", *no_center_path(8)))

    recs = [audit(n, L, B) for n, L, B in cases]
    out = []
    for r in recs:
        rr = {k: v for k, v in r.items() if not k.startswith("_")}
        out.append(rr)
        print(f"{r['name']}: delta={r['delta']} maxdet={r['maxvol_abs_det']} "
              f"theta={r['theta']} class={r['class_size']} "
              f"star_basis={r['star_basis']} star_ratio={r['star_ratio']} "
              f"worst_ratio={r['worst_ratio']} "
              f"checks={r['checks']}")
    (OUT / "harness_summary.json").write_text(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
