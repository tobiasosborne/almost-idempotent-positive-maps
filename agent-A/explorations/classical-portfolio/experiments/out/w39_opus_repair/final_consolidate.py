#!/usr/bin/env python3
"""Consolidated exact verification of the REPAIRED reduction for proof.md.

Pointwise lemmas (verified at every (s,j) over the whole theta=1/2 class):
  (R)   E_s = (sigma_s - 2 lambda_s)_+ = (2 mu_s - sigma_s)_+      [since lambda=sigma-mu]
  (P1)  E_s <= sigma_s + 2(-lambda_s)_+                            [subadditivity of (.)_+]
  (P2)  (-lambda_s)_+ = (mu_s - sigma_s)_+ <= mu_s                 [sigma>=0]
Aggregate (at the ARGMIN chart U*):
  SF_s <= S*_s := S+_s + 2 V_s,  with V_s <= M_s.
Report S*_s/delta at U* (the (SB*) constant C) and the breakdown S+, V, M at U*.
"""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
import sympy as sp
import harness as H


def at_argmin(name, L, B):
    P = sp.simplify(L * B)
    delta = H.max_row_neg_mass(P)
    best, bases = H.theta_class(L, sp.Rational(1, 2))
    rows = [H.chart_values(P, L, b) for b in bases]
    rows.sort(key=lambda r: (Fraction(r["phi"]), tuple(r["basis"])))
    star = tuple(rows[0]["basis"])
    A = H.coeff_field(L, list(star))
    P1_ok = P2_ok = R_ok = True
    per_s = []
    for s, u in enumerate(star):
        SF = Sp = V = M = sp.Integer(0)
        for j in range(P.cols):
            beta = sp.simplify(P[u, j]); bp = H.pos(beta)
            lam = sp.simplify(1 - A[j, s])
            mu = sp.factor(sum(H.neg(A[j, t]) for t in range(A.cols) if t != s))
            sigma = sp.factor(sum(H.pos(A[j, t]) for t in range(A.cols) if t != s))
            E = H.pos(mu - lam)
            if sp.simplify(E - H.pos(sigma - 2 * lam)) != 0: R_ok = False
            if sp.simplify((sigma + 2 * H.neg(lam)) - E) < 0: P1_ok = False
            if sp.simplify(H.neg(lam) - H.pos(mu - sigma)) != 0: P2_ok = False
            if sp.simplify(mu - H.neg(lam)) < 0: P2_ok = False
            if bp > 0:
                SF += bp * E; Sp += bp * sigma; V += bp * H.neg(lam); M += bp * mu
        SF, Sp, V, M = map(sp.factor, (SF, Sp, V, M))
        Sstar = sp.factor(Sp + 2 * V)
        # consistency SF <= Sstar
        assert sp.simplify(Sstar - SF) >= 0, (name, s)
        assert sp.simplify(M - V) >= 0, (name, s)
        per_s.append({
            "s": s,
            "SF/d": str(sp.Rational(SF/delta)) if delta else "inf",
            "S*/d": str(sp.Rational(Sstar/delta)) if delta else "inf",
            "S+/d": str(sp.Rational(Sp/delta)) if delta else "inf",
            "V/d": str(sp.Rational(V/delta)) if delta else "inf",
            "M/d": str(sp.Rational(M/delta)) if delta else "inf",
        })
    Sstar_max = max(Fraction(p["S*/d"]) for p in per_s)
    return {
        "name": name, "delta": str(delta), "star_basis": list(star),
        "R_ok": R_ok, "P1_ok": P1_ok, "P2_ok": P2_ok,
        "S*/d max (= SB* constant)": str(Sstar_max),
        "per_s": per_s,
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
    recs = [at_argmin(n, L, B) for n, L, B in cases]
    Path("final_consolidate.json").write_text(json.dumps(recs, indent=2))
    lines = []
    for r in recs:
        lines.append(f"{r['name']}: delta={r['delta']} R_ok={r['R_ok']} P1_ok={r['P1_ok']} "
                     f"P2_ok={r['P2_ok']} S*/d_max(SB*const)={r['S*/d max (= SB* constant)']}")
        for p in r["per_s"]:
            lines.append(f"    s={p['s']}: SF/d={p['SF/d']} S*/d={p['S*/d']} "
                         f"S+/d={p['S+/d']} V/d={p['V/d']} M/d={p['M/d']}")
    Path("final_consolidate.out").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
