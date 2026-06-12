#!/usr/bin/env python3
"""w37_opus independent diagnostic: reverse-engineer the (CHARGE) dual weights.

For each mandatory family, build the selected chart U* (theta=1/2 class, argmin
Phi), then for each representative s with SF_s(U*) > 0 solve the LP

    minimize   C
    s.t.       SF_s(U*) <= sum_i q_i nu_i(P)
               sum_i q_i <= C
               q_i >= 0

which is just C_s := SF_s / max_i nu_i unless we DEMAND structure.  The
INTERESTING object is the *structured* charge: restrict support of q to rows that
actually appear (with positive B_{sj}) in the SF_s sum, AND look at the
per-coordinate decomposition of E_s(j) to see WHICH row negativities pay.

We expose three diagnostics:
  (1) C_s = SF_s/delta   (the trivial ratio; calibration target ~2)
  (2) the excess decomposition: E_s(j) = (mu_s(j) - lambda_s(j))_+, broken into
      the coordinates t!=s contributing (-a_t(j))_+, and which rows i have nu_i>0.
  (3) a *localized* charge: for each (s,j) with E_s(j)>0, try to charge E_s(j) to
      the row negativities nu_i along the support of a(j) -- i.e. test whether
      E_s(j) <= sum_{t: a_t(j)<0} (something) * nu_{u_t} or to the actual rows.

Everything exact (sympy).  Imports the harness families directly.
"""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
import sympy as sp

import harness as H

OUT = Path(__file__).resolve().parent


def nu_row(P, i):
    tot = sp.Integer(0)
    for x in P.row(i):
        x = sp.simplify(x)
        if x < 0:
            tot += -x
    return sp.simplify(tot)


def analyze(name, L, B, theta=sp.Rational(1, 2)):
    P = sp.simplify(L * B)
    delta = H.max_row_neg_mass(P)
    recs, best = H.select_star(L, P, theta=theta)
    star_basis, star_vals, star_phi = recs[0]
    A = H.coeff_field(L, star_basis)  # A[j,t] = a_t(j)
    nu = [nu_row(P, i) for i in range(P.rows)]

    out = {"name": name, "delta": str(delta), "star_basis": list(star_basis),
           "star_phi": str(star_phi), "phi_over_delta": str(sp.simplify(star_phi/delta)) if delta!=0 else "inf",
           "reps": []}

    for s_idx, u_s in enumerate(star_basis):
        SF = star_vals[s_idx]
        if SF == 0:
            continue
        rep = {"s": s_idx, "u_s": int(u_s), "SF": str(SF),
               "SF_over_delta": str(sp.simplify(SF/delta)) if delta!=0 else "inf",
               "terms": []}
        for j in range(P.cols):
            w = sp.simplify(P[u_s, j])  # = B_{s j}
            if w <= 0:
                continue
            row = list(A.row(j))
            mu = sum(H.neg(sp.simplify(x)) for t, x in enumerate(row) if t != s_idx)
            lam = sp.simplify(1 - row[s_idx])
            E = sp.simplify(mu - lam)
            E = E if E > 0 else sp.Integer(0)
            if E == 0:
                continue
            # which coordinates t carry the negative coeff mass:
            neg_coords = [(t, str(sp.simplify(-row[t])), int(star_basis[t]), str(nu[star_basis[t]]))
                          for t in range(len(row)) if t != s_idx and sp.simplify(row[t]) < 0]
            rep["terms"].append({
                "j": j, "B_sj": str(w), "mu": str(mu), "lambda": str(lam),
                "E": str(E), "wE": str(sp.simplify(w*E)),
                "neg_coords_t_(val,u_t,nu_ut)": neg_coords,
            })
        out["reps"].append(rep)
    return out


def main():
    cases = [
        ("transverse_pair_a1_4", *H.transverse_pair(sp.Rational(1, 4))),
        ("dense_pair_k7_a1_4", *H.dense_pair_k7()),
        ("staircase_m2", *H.staircase(2)),
        ("staircase_m3", *H.staircase(3)),
        ("perturbed_staircase_m5_eps1e-3", *H.perturbed_staircase(5, sp.Rational(1, 1000))),
        ("no_center_path_k6", *H.no_center_path(6)),
        ("no_center_path_k8", *H.no_center_path(8)),
    ]
    res = []
    for n, L, B in cases:
        r = analyze(n, L, B)
        res.append(r)
        print(f"\n=== {r['name']}  delta={r['delta']} Phi/delta={r['phi_over_delta']} "
              f"basis={r['star_basis']} ===")
        for rep in r["reps"]:
            print(f"  s={rep['s']} u_s={rep['u_s']} SF/delta={rep['SF_over_delta']} "
                  f"({len(rep['terms'])} excess terms)")
            for tm in rep["terms"][:6]:
                print(f"    j={tm['j']} B_sj={tm['B_sj']} mu={tm['mu']} lam={tm['lambda']} "
                      f"E={tm['E']} wE={tm['wE']} negcoords={tm['neg_coords_t_(val,u_t,nu_ut)']}")
    (OUT / "charge_lp.json").write_text(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
