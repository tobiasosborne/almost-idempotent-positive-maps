#!/usr/bin/env python3
"""Task 2: investigate the overshoot term V_s and the positive deficit D+_s.

Identities to verify EXACTLY across the whole theta=1/2 class (not just argmin):
  (DEF)  sum_j beta_s lambda_s = 0.
  (V-ID) V_s = D+_s - Dneg_s   where Dneg_s := sum_j (beta_s)_- lambda_s.
         [since sum (beta)_+ lambda = sum(beta)_- lambda and
          sum(beta)_+ lambda = D+_s - V_s.]
  |Dneg_s| <= 3 delta  (|lambda|<=3 in theta=1/2 box, sum(beta)_- <= delta).
  => V_s <= D+_s + 3 delta.

QUESTION A: is V_s small over the WHOLE class, or only at argmin?
QUESTION B: is D+_s <= C' delta at the argmin (and what is C')?  Over the whole class?
QUESTION C: does max-volume-ness alone (factor 1/2) bound D+_s, independent of selection?

We report, for every basis in the theta=1/2 class of each family:
  V_s/delta, D+_s/delta, Dneg_s/delta, and check V-ID, and |lambda| range,
  and the Cramer box max|a_t(j)|.
"""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
import sympy as sp
import harness as H


def box_max(A):
    return max(abs(sp.simplify(A[i, j])) for i in range(A.rows) for j in range(A.cols))


def analyze(name, L, B):
    P = sp.simplify(L * B)
    delta = H.max_row_neg_mass(P)
    best, bases = H.theta_class(L, sp.Rational(1, 2))
    out = {"name": name, "delta": str(delta), "class_size": len(bases), "rows": []}
    Vmax_class = Fraction(0)
    Dpmax_class = Fraction(0)
    vid_ok = True
    for basis in bases:
        A = H.coeff_field(L, basis)
        boxmax = box_max(A)
        rec = {"basis": list(basis), "box": str(boxmax),
               "V": [], "Dpos": [], "Dneg": [], "vid_ok": True}
        for s, u in enumerate(basis):
            V = sp.Integer(0); Dp = sp.Integer(0); Dn = sp.Integer(0)
            sbl = sp.Integer(0)  # sum beta_+ lambda
            for j in range(P.cols):
                beta = sp.simplify(P[u, j])
                lam = sp.simplify(1 - A[j, s])
                bp = H.pos(beta); bn = H.neg(beta)
                if bp != 0:
                    V += bp * H.neg(lam)
                    Dp += bp * H.pos(lam)
                    sbl += bp * lam
                if bn != 0:
                    Dn += bn * lam
            V = sp.factor(V); Dp = sp.factor(Dp); Dn = sp.factor(Dn)
            # V-ID: V = Dp - Dn  (Dn = sum beta_- lambda)
            if sp.simplify(V - (Dp - Dn)) != 0:
                rec["vid_ok"] = False; vid_ok = False
            rec["V"].append(str(V)); rec["Dpos"].append(str(Dp)); rec["Dneg"].append(str(Dn))
            if delta:
                Vmax_class = max(Vmax_class, Fraction(str(sp.Rational(V / delta))))
                Dpmax_class = max(Dpmax_class, Fraction(str(sp.Rational(Dp / delta))))
        out["rows"].append(rec)
    out["V_over_delta_max_class"] = str(Vmax_class)
    out["Dpos_over_delta_max_class"] = str(Dpmax_class)
    out["vid_ok_all"] = vid_ok
    # box max over class
    out["box_max_class"] = str(max(Fraction(str(r["box"])) for r in out["rows"]))
    return out


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
    Path("overshoot.json").write_text(json.dumps(recs, indent=2))
    lines = []
    for r in recs:
        lines.append(
            f"{r['name']}: delta={r['delta']} class={r['class_size']} "
            f"V/d_max_CLASS={r['V_over_delta_max_class']} "
            f"Dpos/d_max_CLASS={r['Dpos_over_delta_max_class']} "
            f"box_max_CLASS={r['box_max_class']} VID_ok={r['vid_ok_all']}")
    Path("overshoot.out").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
