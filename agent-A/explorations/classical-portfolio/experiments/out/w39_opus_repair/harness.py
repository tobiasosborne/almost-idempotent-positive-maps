#!/usr/bin/env python3
"""w39_opus_repair harness.

Corrected reduction object S*_s := sum_j (beta_s)_+ [ sigma_s(j) + 2(-lambda_s(j))_+ ]
plus the overshoot term V_s := sum_j (beta_s)_+ (-lambda_s(j))_+  and the
positive-deficit pieces D+_s := sum_j (beta_s)_+ lambda_s(j)_+,
D-_s := sum_j (-beta_s(j))_+ lambda_s(j).

All exact sympy rationals. Families lifted verbatim from w38_sb/verify_reduction.py
(transverse pair, dense pair k=7, staircase m, perturbed staircase) plus a
no-center path family (k=6,8) for the C~2 calibration.
"""
from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


def pos(x):
    x = sp.simplify(x)
    return x if x > 0 else sp.Integer(0)


def neg(x):
    x = sp.simplify(x)
    return -x if x < 0 else sp.Integer(0)


def fstr(x):
    return str(sp.factor(x))


def row_neg_mass(row):
    return sp.factor(sum(neg(x) for x in list(row)))


def max_row_neg_mass(P):
    return max(row_neg_mass(P.row(i)) for i in range(P.rows))


def coeff_field(L, basis):
    return sp.simplify(L * L[list(basis), :].inv())


def per_coord(coord_row, s):
    """Return lam, mu, sigma, E for representative s at this coordinate row."""
    lam = sp.simplify(1 - coord_row[s])
    mu = sp.factor(sum(neg(coord_row[t]) for t in range(len(coord_row)) if t != s))
    sigma = sp.factor(sum(pos(coord_row[t]) for t in range(len(coord_row)) if t != s))
    E = pos(mu - lam)
    return lam, mu, sigma, sp.factor(E)


def chart_values(P, L, basis):
    A = coeff_field(L, basis)
    out = {
        "basis": list(basis),
        "sf": [], "splus": [], "sstar": [], "V": [],
        "Dpos": [], "Dneg": [], "def": [],
        "R_ok": True, "ptbound_ok": True,
        "sig_fail": [],
    }
    for s, u in enumerate(basis):
        SF = sp.Integer(0)
        Splus = sp.Integer(0)
        Sstar = sp.Integer(0)
        V = sp.Integer(0)
        Dpos = sp.Integer(0)
        Dneg = sp.Integer(0)
        Def = sp.Integer(0)
        for j in range(P.cols):
            beta = sp.simplify(P[u, j])
            lam, mu, sigma, E = per_coord(A.row(j), s)
            # (R) check
            if sp.simplify(E - pos(sigma - 2 * lam)) != 0:
                out["R_ok"] = False
            # pointwise corrected bound: E <= sigma + 2(-lambda)_+
            if sp.simplify((sigma + 2 * neg(lam)) - E) < 0:
                out["ptbound_ok"] = False
            Def += beta * lam
            bp = pos(beta)
            bn = neg(beta)
            if bp != 0:
                SF += bp * E
                Splus += bp * sigma
                Sstar += bp * (sigma + 2 * neg(lam))
                V += bp * neg(lam)
                Dpos += bp * pos(lam)
                if E > sigma:
                    out["sig_fail"].append({
                        "s": s, "u": int(u), "j": j,
                        "lambda": fstr(lam), "sigma": fstr(sigma), "E": fstr(E),
                        "overshoot_2neglam": fstr(2 * neg(lam)),
                    })
            if bn != 0:
                Dneg += bn * lam
        out["sf"].append(sp.factor(SF))
        out["splus"].append(sp.factor(Splus))
        out["sstar"].append(sp.factor(Sstar))
        out["V"].append(sp.factor(V))
        out["Dpos"].append(sp.factor(Dpos))
        out["Dneg"].append(sp.factor(Dneg))
        out["def"].append(sp.factor(Def))
    out["phi"] = fstr(max(out["sf"]))
    out["sstar_max"] = fstr(max(out["sstar"]))
    out["splus_max"] = fstr(max(out["splus"]))
    out["V_max"] = fstr(max(out["V"]))
    out["Dpos_max"] = fstr(max(out["Dpos"]))
    out["sf"] = [fstr(x) for x in out["sf"]]
    out["splus"] = [fstr(x) for x in out["splus"]]
    out["sstar"] = [fstr(x) for x in out["sstar"]]
    out["V"] = [fstr(x) for x in out["V"]]
    out["Dpos"] = [fstr(x) for x in out["Dpos"]]
    out["Dneg"] = [fstr(x) for x in out["Dneg"]]
    out["def"] = [fstr(x) for x in out["def"]]
    return out


def all_bases_by_volume(L):
    by_vol = {}
    for basis in itertools.combinations(range(L.rows), L.cols):
        det = sp.factor(L[list(basis), :].det())
        vol = abs(det)
        if vol == 0:
            continue
        by_vol.setdefault(vol, []).append(basis)
    best = max(by_vol.keys())
    return by_vol, best


def theta_class(L, theta=sp.Rational(1, 2)):
    by_vol, best = all_bases_by_volume(L)
    bases = []
    for vol, vals in by_vol.items():
        if vol >= theta * best:
            bases.extend(vals)
    bases.sort()
    return best, bases


def select_chart(P, L, theta=sp.Rational(1, 2)):
    best, bases = theta_class(L, theta)
    rows = [chart_values(P, L, b) for b in bases]
    rows.sort(key=lambda r: (Fraction(r["phi"]), tuple(r["basis"])))
    return best, rows, bases


# ---------- families (verbatim from w38) ----------

def transverse_pair(a, mass=sp.Integer(1)):
    L = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, a, -a], [1, -a, a]])
    c = sp.factor(a / (1 + 4 * a * a))
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
    sigma = [0] + [1] * m + [-1] * m
    rows = []
    for i in range(k):
        r = [sp.Integer(0)] * k
        r[i] = sp.Integer(1)
        rows.append(r)
    xp = [sp.Integer(0)] * k
    xm = [sp.Integer(0)] * k
    xp[0] = xm[0] = sp.Integer(1)
    for t in range(1, k):
        xp[t] = a * sigma[t]
        xm[t] = -a * sigma[t]
    rows.extend([xp, xm])
    L = sp.Matrix(rows)
    B = sp.zeros(k, k + 2)
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
    sigma = [0] + [1] * m + [-1] * m
    rows = []
    for i in range(k):
        r = [sp.Integer(0)] * k
        r[i] = sp.Integer(1)
        rows.append(r)
    xp = [sp.Integer(0)] * k
    xm = [sp.Integer(0)] * k
    xp[0] = xm[0] = sp.Integer(1)
    for t in range(1, k):
        xp[t] = sp.Rational(1, 2) * sigma[t]
        xm[t] = -sp.Rational(1, 2) * sigma[t]
    rows.extend([xp, xm])
    L = sp.Matrix(rows)
    B = sp.zeros(k, k + 2)
    B[0, k] = B[0, k + 1] = sp.Rational(1, 2)
    for r in range(1, k):
        for t in range(1, k):
            B[r, t] = (1 if r == t else 0) - sp.Rational(sigma[r] * sigma[t], 2 * m)
        B[r, k] = sp.Rational(sigma[r], 2 * m)
        B[r, k + 1] = -sp.Rational(sigma[r], 2 * m)
    return L, B


def perturbed_staircase(m, eps):
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
    B = sp.zeros(k, k + 2)
    B[0, 0] = eps
    for t in range(1, k):
        B[0, t] = -d
    B[0, k] = B[0, k + 1] = sp.Rational(1, 2)
    for r in range(1, k):
        for t in range(1, k):
            B[r, t] = (1 if r == t else 0) - sp.Rational(sigma[r] * sigma[t], 2 * m)
        B[r, k] = sp.Rational(sigma[r], 2 * m)
        B[r, k + 1] = -sp.Rational(sigma[r], 2 * m)
    return L, B


def no_center_path(k, a=sp.Rational(1, 100)):
    """Genuine no-center path family (w36/w37 nocenter_exact.py, verbatim).
    L rows: e_1..e_{k-1} foreign units, then signed shear rows
      x_+ = e_0 + a(e_u - e_v),  x_- = e_0 - a(e_u - e_v)  for consecutive (u,v).
    B solved exactly via BL=I + central-row even spread + zero free vars.
    Returns (L, B)."""
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
    sol = sp.solve(cons, list(Bsyms), dict=True)
    if not sol:
        return None
    sol = sol[0]
    free = [s for s in Bsyms if s not in sol]
    zero = {s: sp.Integer(0) for s in free}
    B = Bsyms.subs(sol).subs(zero)
    return L, sp.simplify(B)


def audit_case(name, L, B):
    P = sp.simplify(L * B)
    delta = max_row_neg_mass(P)
    best, rows, bases = select_chart(P, L, sp.Rational(1, 2))
    star = rows[0]

    def over(x):
        return fstr(sp.Rational(x) / delta) if delta else "inf"

    rec = {
        "name": name, "n": L.rows, "k": L.cols,
        "delta": fstr(delta), "maxvol": fstr(best),
        "class_size": len(rows),
        "star_basis": star["basis"],
        "delta": fstr(delta),
        "Phi_over_delta": over(star["phi"]),
        "Sstar_over_delta": [over(x) for x in star["sstar"]],
        "Sstar_max_over_delta": over(star["sstar_max"]),
        "Splus_over_delta": [over(x) for x in star["splus"]],
        "V_over_delta": [over(x) for x in star["V"]],
        "V_max_over_delta": over(star["V_max"]),
        "Dpos_over_delta": [over(x) for x in star["Dpos"]],
        "Dpos_max_over_delta": over(star["Dpos_max"]),
        "Dneg": star["Dneg"],
        "def_zero": all(sp.simplify(sp.Rational(d)) == 0 for d in star["def"]),
        "R_ok": star["R_ok"],
        "ptbound_ok": star["ptbound_ok"],
        "n_sig_fail_in_star": len(star["sig_fail"]),
        "sig_fail_first": star["sig_fail"][0] if star["sig_fail"] else None,
        "checks": {
            "P2": bool(sp.simplify(P * P - P) == sp.zeros(P.rows, P.cols)),
            "rowsum": all(sp.simplify(sum(P.row(i)) - 1) == 0 for i in range(P.rows)),
        },
    }
    return rec, P


def main():
    cases = [
        ("transverse_pair_a1_4",) + transverse_pair(sp.Rational(1, 4)),
        ("dense_pair_k7_a1_4",) + dense_pair_k7(),
        ("staircase_m2",) + staircase(2),
        ("staircase_m3",) + staircase(3),
        ("perturbed_staircase_m5_eps1e-3",) + perturbed_staircase(5, sp.Rational(1, 1000)),
    ]
    records = []
    for name, L, B in cases:
        rec, _ = audit_case(name, L, B)
        records.append(rec)
    # no-center path k=6,8 (genuine C~2 family)
    for k in (6, 8):
        out = no_center_path(k)
        if out is None:
            continue
        L, B = out
        rec, _ = audit_case(f"no_center_path_k{k}", L, B)
        records.append(rec)

    Path("harness.json").write_text(json.dumps(records, indent=2, sort_keys=True))
    lines = []
    for r in records:
        lines.append(
            f"{r['name']}: delta={r['delta']} class={r['class_size']} "
            f"star={r['star_basis']} Phi/d={r['Phi_over_delta']} "
            f"S*/d_max={r['Sstar_max_over_delta']} S+/d={r['Splus_over_delta']} "
            f"V/d_max={r['V_max_over_delta']} Dpos/d_max={r['Dpos_max_over_delta']} "
            f"R_ok={r['R_ok']} ptbound_ok={r['ptbound_ok']} def0={r['def_zero']} "
            f"sigfail={r['n_sig_fail_in_star']} checks={r['checks']}"
        )
        if r["sig_fail_first"]:
            lines.append(f"    overshoot: {r['sig_fail_first']}")
    Path("harness.out").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
