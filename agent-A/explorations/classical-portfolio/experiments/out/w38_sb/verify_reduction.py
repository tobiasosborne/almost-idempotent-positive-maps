#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


def pos(x: sp.Expr) -> sp.Expr:
    x = sp.simplify(x)
    return x if x > 0 else sp.Integer(0)


def neg(x: sp.Expr) -> sp.Expr:
    x = sp.simplify(x)
    return -x if x < 0 else sp.Integer(0)


def fstr(x: sp.Expr) -> str:
    return str(sp.factor(x))


def row_neg_mass(row: sp.Matrix) -> sp.Expr:
    return sp.factor(sum(neg(x) for x in list(row)))


def max_row_neg_mass(P: sp.Matrix) -> sp.Expr:
    return max(row_neg_mass(P.row(i)) for i in range(P.rows))


def coeff_field(L: sp.Matrix, basis: tuple[int, ...]) -> sp.Matrix:
    return sp.simplify(L * L[list(basis), :].inv())


def lambda_mu_sigma_E(coord_row: sp.Matrix, s: int) -> tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]:
    lam = sp.simplify(1 - coord_row[s])
    mu = sp.factor(sum(neg(coord_row[t]) for t in range(len(coord_row)) if t != s))
    sigma = sp.factor(sum(pos(coord_row[t]) for t in range(len(coord_row)) if t != s))
    E = pos(mu - lam)
    return lam, mu, sigma, sp.factor(E)


def chart_values(P: sp.Matrix, L: sp.Matrix, basis: tuple[int, ...]) -> dict[str, object]:
    A = coeff_field(L, basis)
    sf = []
    sp_budget = []
    sig_fail_terms = []
    r_fail_terms = []
    def_fail = []
    m_budget = []
    for s, u in enumerate(basis):
        total_sf = sp.Integer(0)
        total_sp = sp.Integer(0)
        total_m = sp.Integer(0)
        total_def = sp.Integer(0)
        for j in range(P.cols):
            beta = sp.simplify(P[u, j])
            lam, mu, sigma, E = lambda_mu_sigma_E(A.row(j), s)
            if sp.simplify(mu - (sigma - lam)) != 0:
                r_fail_terms.append((s, int(u), j, fstr(lam), fstr(mu), fstr(sigma)))
            if sp.simplify(E - pos(sigma - 2 * lam)) != 0:
                r_fail_terms.append(("E", s, int(u), j, fstr(E), fstr(sigma - 2 * lam)))
            total_def += beta * lam
            if beta > 0:
                total_sf += beta * E
                total_sp += beta * sigma
                total_m += beta * mu
                if E > sigma:
                    sig_fail_terms.append(
                        {
                            "s": s,
                            "u": int(u),
                            "j": j,
                            "beta": fstr(beta),
                            "lambda": fstr(lam),
                            "mu": fstr(mu),
                            "sigma": fstr(sigma),
                            "E": fstr(E),
                            "w_E_minus_sigma": fstr(beta * (E - sigma)),
                        }
                    )
        sf.append(sp.factor(total_sf))
        sp_budget.append(sp.factor(total_sp))
        m_budget.append(sp.factor(total_m))
        def_fail.append(sp.factor(total_def))
    return {
        "basis": list(basis),
        "sf": [fstr(x) for x in sf],
        "splus": [fstr(x) for x in sp_budget],
        "m": [fstr(x) for x in m_budget],
        "phi": fstr(max(sf)),
        "splus_max": fstr(max(sp_budget)),
        "def": [fstr(x) for x in def_fail],
        "R_ok": not r_fail_terms,
        "sig_point_fail_terms": sig_fail_terms,
    }


def all_bases_by_volume(L: sp.Matrix) -> tuple[dict[sp.Expr, list[tuple[int, ...]]], sp.Expr]:
    by_vol: dict[sp.Expr, list[tuple[int, ...]]] = {}
    for basis in itertools.combinations(range(L.rows), L.cols):
        det = sp.factor(L[list(basis), :].det())
        vol = abs(det)
        if vol == 0:
            continue
        by_vol.setdefault(vol, []).append(basis)
    best = max(by_vol.keys())
    return by_vol, best


def theta_class(L: sp.Matrix, theta: sp.Expr = sp.Rational(1, 2)) -> tuple[sp.Expr, list[tuple[int, ...]]]:
    by_vol, best = all_bases_by_volume(L)
    bases: list[tuple[int, ...]] = []
    for vol, vals in by_vol.items():
        if vol >= theta * best:
            bases.extend(vals)
    bases.sort()
    return best, bases


def select_chart(P: sp.Matrix, L: sp.Matrix, theta: sp.Expr = sp.Rational(1, 2)) -> tuple[sp.Expr, list[dict[str, object]]]:
    best, bases = theta_class(L, theta)
    rows = []
    for basis in bases:
        rec = chart_values(P, L, basis)
        rows.append(rec)
    rows.sort(key=lambda r: (Fraction(r["phi"]), tuple(r["basis"])))
    return best, rows


def transverse_pair(a: sp.Expr, mass: sp.Expr = sp.Integer(1)) -> tuple[sp.Matrix, sp.Matrix]:
    L = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, a, -a], [1, -a, a]])
    c = sp.factor(a / (1 + 4 * a * a))
    B = sp.Matrix(
        [
            [1 - mass, 0, 0, mass / 2, mass / 2],
            [0, 1 - 2 * a * c, 2 * a * c, c, -c],
            [0, 2 * a * c, 1 - 2 * a * c, -c, c],
        ]
    )
    return L, B


def dense_pair_k7() -> tuple[sp.Matrix, sp.Matrix]:
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


def staircase(m: int) -> tuple[sp.Matrix, sp.Matrix]:
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


def perturbed_staircase(m: int, eps: sp.Expr) -> tuple[sp.Matrix, sp.Matrix]:
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


def audit_case(name: str, L: sp.Matrix, B: sp.Matrix) -> dict[str, object]:
    P = sp.simplify(L * B)
    delta = max_row_neg_mass(P)
    best, rows = select_chart(P, L, sp.Rational(1, 2))
    star = rows[0]
    exact_best, exact_bases = theta_class(L, sp.Integer(1))
    exact_rows = [chart_values(P, L, b) for b in exact_bases]
    exact_rows.sort(key=lambda r: (Fraction(r["phi"]), tuple(r["basis"])))
    failures = [term for row in rows for term in row["sig_point_fail_terms"]]
    return {
        "name": name,
        "n": L.rows,
        "k": L.cols,
        "delta": fstr(delta),
        "maxvol": fstr(best),
        "theta_half_class_size": len(rows),
        "star_basis": star["basis"],
        "star_sf": star["sf"],
        "star_phi": star["phi"],
        "star_phi_over_delta": fstr(sp.Rational(star["phi"]) / delta) if delta else "inf",
        "star_splus": star["splus"],
        "star_splus_over_delta": [fstr(sp.Rational(x) / delta) if delta else "inf" for x in star["splus"]],
        "star_m": star["m"],
        "star_def": star["def"],
        "star_R_ok": star["R_ok"],
        "star_sig_fail_terms": star["sig_point_fail_terms"][:10],
        "any_sig_fail_count_in_theta_half": len(failures),
        "exact_class_size": len(exact_rows),
        "exact_best_basis": exact_rows[0]["basis"],
        "exact_best_phi_over_delta": fstr(sp.Rational(exact_rows[0]["phi"]) / delta) if delta else "inf",
        "exact_worst_phi_over_delta": fstr(sp.Rational(exact_rows[-1]["phi"]) / delta) if delta else "inf",
        "checks": {
            "BL": bool(sp.simplify(B * L - sp.eye(L.cols)) == sp.zeros(L.cols, L.cols)),
            "P2": bool(sp.simplify(P * P - P) == sp.zeros(P.rows, P.cols)),
            "rowsum": all(sp.simplify(sum(P.row(i)) - 1) == 0 for i in range(P.rows)),
        },
    }


def main() -> None:
    cases = [
        ("transverse_pair_a1_4",) + transverse_pair(sp.Rational(1, 4)),
        ("dense_pair_k7_a1_4",) + dense_pair_k7(),
        ("staircase_m2",) + staircase(2),
        ("staircase_m3",) + staircase(3),
        ("perturbed_staircase_m5_eps1e-3",) + perturbed_staircase(5, sp.Rational(1, 1000)),
    ]
    records = [audit_case(name, L, B) for name, L, B in cases]
    Path("verify_reduction.json").write_text(json.dumps(records, indent=2, sort_keys=True))
    lines = []
    for rec in records:
        lines.append(
            f"{rec['name']}: delta={rec['delta']} class={rec['theta_half_class_size']} "
            f"star={rec['star_basis']} Phi/delta={rec['star_phi_over_delta']} "
            f"S+*/delta={rec['star_splus_over_delta']} "
            f"SIG_fail_terms_in_class={rec['any_sig_fail_count_in_theta_half']} "
            f"checks={rec['checks']}"
        )
        if rec["star_sig_fail_terms"]:
            lines.append(f"  star SIG first failure: {rec['star_sig_fail_terms'][0]}")
    Path("verify_reduction.out").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
