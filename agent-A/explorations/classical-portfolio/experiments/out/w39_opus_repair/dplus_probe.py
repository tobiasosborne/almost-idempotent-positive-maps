#!/usr/bin/env python3
"""Probe: is D+_s = sum_j (beta_s)_+ lambda_s,+ bounded by C' delta from
(DEF) + Cramer box ALONE (no selection)?  And hence V_s, S*_s?

Candidate clean bound chain (theta=1/2, box B=2, so |lambda_s|<=3, lambda_s in [-1,2]):
  (DEF):  sum_j beta_s lambda_s = 0
       => sum_j (beta_s)_+ lambda_s = sum_j (beta_s)_- lambda_s =: Dneg_s,
          |Dneg_s| <= 3 delta.
  Now sum_j (beta_s)_+ lambda_s = D+_s - V_s, so  D+_s - V_s = Dneg_s.   ... (I)
  This is ONE equation in (D+, V).  Neither is pinned without a second relation.

SECOND RELATION attempts (test each numerically over the class):
  (a) trivial:  V_s <= sum_j (beta_s)_+ (a_s(j)-1)_+ , box gives (a_s-1)_+ <= 1.
  (b) sub-face bound: does max-volume bound D+ directly?  At theta=1 D+ <= 2 delta
      (classic, since lambda>=0 there).  At theta=1/2 check D+/delta over class.
  (c) the ANSWER we want: S*_s = S+_s + 2 V_s.  Test whether S*_s <= S+_s + C'' delta
      i.e. whether V_s <= (C''/2) delta over the class, and at argmin.

We tabulate, per family, over the whole class AND at argmin:
  max_s V_s/delta, max_s D+_s/delta, and the gap S*_s - S+_s = 2 V_s, /delta.
"""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
import sympy as sp
import harness as H


def per_basis(P, L, basis):
    A = H.coeff_field(L, basis)
    res = []
    for s, u in enumerate(basis):
        V = sp.Integer(0); Dp = sp.Integer(0); Sp = sp.Integer(0)
        for j in range(P.cols):
            beta = sp.simplify(P[u, j]); bp = H.pos(beta)
            if bp == 0:
                continue
            lam = sp.simplify(1 - A[j, s])
            sigma = sp.factor(sum(H.pos(A[j, t]) for t in range(A.cols) if t != s))
            V += bp * H.neg(lam)
            Dp += bp * H.pos(lam)
            Sp += bp * sigma
        res.append((sp.factor(V), sp.factor(Dp), sp.factor(Sp)))
    return res


def analyze(name, L, B):
    P = sp.simplify(L * B)
    delta = H.max_row_neg_mass(P)
    best, bases = H.theta_class(L, sp.Rational(1, 2))
    # argmin
    rows = [H.chart_values(P, L, b) for b in bases]
    rows.sort(key=lambda r: (Fraction(r["phi"]), tuple(r["basis"])))
    star_basis = tuple(rows[0]["basis"])
    Vmax_cls = Fraction(0); Dpmax_cls = Fraction(0); Sgapmax_cls = Fraction(0)
    Vmax_star = Fraction(0); Dpmax_star = Fraction(0)
    for basis in bases:
        pb = per_basis(P, L, basis)
        for (V, Dp, Sp) in pb:
            vr = Fraction(str(sp.Rational(V / delta)))
            dr = Fraction(str(sp.Rational(Dp / delta)))
            Vmax_cls = max(Vmax_cls, vr); Dpmax_cls = max(Dpmax_cls, dr)
            Sgapmax_cls = max(Sgapmax_cls, 2 * vr)
            if tuple(basis) == star_basis:
                Vmax_star = max(Vmax_star, vr); Dpmax_star = max(Dpmax_star, dr)
    return {
        "name": name, "delta": str(delta), "class_size": len(bases),
        "V/d max over CLASS": str(Vmax_cls),
        "D+/d max over CLASS": str(Dpmax_cls),
        "2V/d (=S*-S+ gap) max over CLASS": str(Sgapmax_cls),
        "V/d at ARGMIN": str(Vmax_star),
        "D+/d at ARGMIN": str(Dpmax_star),
    }


def main():
    cases = [
        ("transverse_pair_a1_4",) + H.transverse_pair(sp.Rational(1, 4)),
        ("dense_pair_k7_a1_4",) + H.dense_pair_k7(),
        ("staircase_m2",) + H.staircase(2),
        ("staircase_m3",) + H.staircase(3),
        ("perturbed_staircase_m5_eps1e-3",) + H.perturbed_staircase(5, sp.Rational(1, 1000)),
    ]
    for k in (6, 8):
        out = H.no_center_path(k)
        if out:
            L, B = out
            cases.append((f"no_center_path_k{k}", L, B))
    recs = [analyze(n, L, B) for n, L, B in cases]
    Path("dplus_probe.json").write_text(json.dumps(recs, indent=2))
    for r in recs:
        print(json.dumps(r))


if __name__ == "__main__":
    main()
