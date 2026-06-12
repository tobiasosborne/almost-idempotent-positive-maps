#!/usr/bin/env python3
"""Pin the mechanism that keeps V_s = sum_j (beta_s)_+ (a_s(j)-1)_+ small.

For every basis in the theta=1/2 class, for every overshoot coordinate
(s, j) with a_s(j) > 1, record:
   beta_s(j) sign,  a_s(j),  the most-negative transverse coeff min_t a_t(j),
   sigma_s(j) (positive transverse mass).
Test conjectures:
  C1: overshoot rows carry beta_s(j) <= 0  (then (beta_s)_+ = 0 there, V=0).   [class V<=1 says NO in general]
  C2: V_s <= sigma_s-budget: on overshoot rows (a_s-1)_+ = -lambda = sigma - mu...
      indeed lambda = sigma - mu (from R-derivation mu = sigma - lambda), so
      -lambda = mu - sigma, and (a_s-1)_+ = (-lambda)_+ = (mu-sigma)_+.
      => V_s = sum (beta_s)_+ (mu_s - sigma_s)_+.  An overshoot row needs mu > sigma:
         MORE negative transverse mass than positive. Then  V <= sum (beta_s)_+ mu_s
         <= M_s (the transverse tax).  Is M_s <= C delta?  (That was the OLD theta=1
         tax, now signed.)
  C3: direct -- is V_s <= delta * (something) via row-negativity of the OVERSHOOT
      coordinate?  a_s(j)>1 with sum=1 forces a NEGATIVE transverse coeff; tie it to nu.
Report per family: max over class of  V_s/delta,  M_s/delta (transverse neg tax),
and whether every overshoot row has (beta_s)_+ * (a_s-1)_+ accompanied by negative
transverse mass >= (a_s-1).
"""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
import sympy as sp
import harness as H


def analyze(name, L, B):
    P = sp.simplify(L * B)
    delta = H.max_row_neg_mass(P)
    best, bases = H.theta_class(L, sp.Rational(1, 2))
    Vmax = Fraction(0); Mmax = Fraction(0)
    c1_ok = True       # overshoot => beta<=0
    c2_ok = True       # V <= M pointwise weighted (mu>=sigma on overshoot weighted rows)
    overshoot_examples = []
    for basis in bases:
        A = H.coeff_field(L, basis)
        for s, u in enumerate(basis):
            V = sp.Integer(0); M = sp.Integer(0)
            for j in range(P.cols):
                beta = sp.simplify(P[u, j]); bp = H.pos(beta)
                lam = sp.simplify(1 - A[j, s])
                mu = sp.factor(sum(H.neg(A[j, t]) for t in range(A.cols) if t != s))
                sigma = sp.factor(sum(H.pos(A[j, t]) for t in range(A.cols) if t != s))
                a_s = A[j, s]
                if sp.simplify(a_s - 1) > 0:  # overshoot
                    if bp > 0:
                        c1_ok = False
                        if len(overshoot_examples) < 6:
                            overshoot_examples.append({
                                "basis": list(basis), "s": s, "j": j,
                                "a_s": str(sp.factor(a_s)), "beta": str(sp.factor(beta)),
                                "mu": str(mu), "sigma": str(sigma),
                                "neg_minus_pos_transverse": str(sp.factor(mu - sigma)),
                            })
                    # c2: on overshoot, -lambda = mu - sigma must be >0
                    if sp.simplify((mu - sigma) - H.neg(lam)) != 0:
                        c2_ok = False
                if bp > 0:
                    V += bp * H.neg(lam)
                    M += bp * mu
            if delta:
                Vmax = max(Vmax, Fraction(str(sp.Rational(V / delta))))
                Mmax = max(Mmax, Fraction(str(sp.Rational(M / delta))))
    return {
        "name": name, "delta": str(delta),
        "V/d max class": str(Vmax),
        "M (transverse neg tax)/d max class": str(Mmax),
        "C1 (overshoot=>beta<=0)": c1_ok,
        "C2 (-lambda=mu-sigma on overshoot)": c2_ok,
        "overshoot_with_pos_beta": overshoot_examples,
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
    Path("v_mechanism.json").write_text(json.dumps(recs, indent=2))
    for r in recs:
        print(f"{r['name']}: V/d={r['V/d max class']} M/d={r['M (transverse neg tax)/d max class']} "
              f"C1={r['C1 (overshoot=>beta<=0)']} C2={r['C2 (-lambda=mu-sigma on overshoot)']} "
              f"n_overshoot_posbeta={len(r['overshoot_with_pos_beta'])}")
        for ex in r["overshoot_with_pos_beta"][:2]:
            print("   ", ex)


if __name__ == "__main__":
    main()
