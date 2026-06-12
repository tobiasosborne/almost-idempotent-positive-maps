#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


OUT = Path(__file__).resolve().parent


def fstr(x: sp.Expr) -> str:
    return str(sp.factor(x))


def row_neg_mass(row: sp.Matrix) -> sp.Rational:
    total = sp.Rational(0)
    for x in list(row):
        x = sp.simplify(x)
        if x < 0:
            total += -x
    return sp.simplify(total)


def max_row_neg_mass(P: sp.Matrix) -> sp.Rational:
    return max(row_neg_mass(P.row(i)) for i in range(P.rows))


def excess(coord_row: sp.Matrix, s: int) -> sp.Rational:
    mu = sp.Rational(0)
    for t, x in enumerate(list(coord_row)):
        if t == s:
            continue
        x = sp.simplify(x)
        if x < 0:
            mu += -x
    val = sp.simplify(mu - (1 - coord_row[s]))
    return sp.simplify(max(val, sp.Rational(0)))


def sf_values(P: sp.Matrix, L: sp.Matrix, basis: tuple[int, ...]) -> list[sp.Rational]:
    LU = L[list(basis), :]
    C = sp.simplify(L * LU.inv())
    vals: list[sp.Rational] = []
    for s, u in enumerate(basis):
        total = sp.Rational(0)
        for j in range(P.cols):
            w = sp.simplify(P[u, j])
            if w > 0:
                total += w * excess(C.row(j), s)
        vals.append(sp.simplify(total))
    return vals


def maxvol_ties(L: sp.Matrix) -> tuple[sp.Rational, list[tuple[int, ...]]]:
    k = L.cols
    best: sp.Rational | None = None
    ties: list[tuple[int, ...]] = []
    for basis in itertools.combinations(range(L.rows), k):
        det = sp.simplify(L[list(basis), :].det())
        score = abs(det)
        if score == 0:
            continue
        if best is None or score > best:
            best = score
            ties = [basis]
        elif score == best:
            ties.append(basis)
    if best is None:
        raise ValueError("no full-rank row basis")
    return best, ties


def audit(name: str, L: sp.Matrix, B: sp.Matrix) -> dict[str, object]:
    P = sp.simplify(L * B)
    delta = max_row_neg_mass(P)
    volume, ties = maxvol_ties(L)
    chart_rows = []
    for basis in ties:
        vals = sf_values(P, L, basis)
        max_sf = max(vals)
        ratio = sp.oo if delta == 0 and max_sf > 0 else sp.simplify(max_sf / delta if delta else 0)
        chart_rows.append(
            {
                "basis": list(basis),
                "sf": [fstr(v) for v in vals],
                "max_sf": fstr(max_sf),
                "max_ratio": fstr(ratio),
            }
        )
    chart_rows.sort(key=lambda r: Fraction(r["max_ratio"]) if r["max_ratio"] != "oo" else Fraction(10**18))
    return {
        "name": name,
        "n": L.rows,
        "k": L.cols,
        "delta": fstr(delta),
        "maxvol_abs_det": fstr(volume),
        "tie_count": len(ties),
        "idempotence_ok": bool(sp.simplify(P * P - P) == sp.zeros(P.rows, P.cols)),
        "rowsum_ok": all(sp.simplify(sum(P.row(i)) - 1) == 0 for i in range(P.rows)),
        "BL_ok": bool(sp.simplify(B * L - sp.eye(L.cols)) == sp.zeros(L.cols, L.cols)),
        "best_chart": chart_rows[0],
        "worst_chart": chart_rows[-1],
        "all_charts": chart_rows,
    }


def transverse_pair(a: sp.Rational, mass: sp.Rational) -> tuple[sp.Matrix, sp.Matrix]:
    L = sp.Matrix(
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, a, -a],
            [1, -a, a],
        ]
    )
    c = sp.simplify(a / (1 + 4 * a * a))
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
    rows = []
    for i in range(k):
        row = [sp.Rational(0)] * k
        row[i] = sp.Rational(1)
        rows.append(row)
    sigma = [0] + [1] * m + [-1] * m
    xp = [sp.Rational(0)] * k
    xm = [sp.Rational(0)] * k
    xp[0] = xm[0] = sp.Rational(1)
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


def staircase(m: int) -> tuple[sp.Matrix, sp.Matrix]:
    k = 2 * m + 1
    rows = []
    for i in range(k):
        row = [sp.Rational(0)] * k
        row[i] = sp.Rational(1)
        rows.append(row)
    sigma = [0] + [1] * m + [-1] * m
    xp = [sp.Rational(0)] * k
    xm = [sp.Rational(0)] * k
    xp[0] = xm[0] = sp.Rational(1)
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


def main() -> None:
    cases = []
    cases.append(("transverse_pair_a1_4",) + transverse_pair(sp.Rational(1, 4), sp.Rational(1)))
    cases.append(("dense_pair_k7_a1_4",) + dense_pair_k7())
    cases.append(("staircase_m2_a1_2",) + staircase(2))
    cases.append(("staircase_m3_a1_2",) + staircase(3))

    records = [audit(name, L, B) for name, L, B in cases]
    (OUT / "stress_checks.json").write_text(json.dumps(records, indent=2, sort_keys=True))

    lines = []
    for rec in records:
        best = rec["best_chart"]
        worst = rec["worst_chart"]
        lines.append(
            f"{rec['name']}: delta={rec['delta']} ties={rec['tie_count']} "
            f"best_basis={best['basis']} best_max_ratio={best['max_ratio']} "
            f"worst_max_ratio={worst['max_ratio']} checks="
            f"BL:{rec['BL_ok']} P2:{rec['idempotence_ok']} rows:{rec['rowsum_ok']}"
        )
    (OUT / "stress_checks_summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
