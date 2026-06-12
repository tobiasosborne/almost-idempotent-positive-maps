#!/usr/bin/env python3
from __future__ import annotations

import itertools
from fractions import Fraction

import sympy as sp


def neg_mass(row: sp.Matrix) -> sp.Rational:
    return sp.simplify(sum(-x for x in list(row) if x < 0))


def delta(P: sp.Matrix) -> sp.Rational:
    return max(neg_mass(P.row(i)) for i in range(P.rows))


def excess(coord_row: sp.Matrix, s: int) -> sp.Rational:
    mu = sp.Rational(0)
    for t, x in enumerate(list(coord_row)):
        if t != s and x < 0:
            mu -= x
    return sp.simplify(max(mu - (1 - coord_row[s]), sp.Rational(0)))


def coords_from_actual_rows(P: sp.Matrix, basis: tuple[int, ...]) -> sp.Matrix:
    R = P[list(basis), :]
    return sp.simplify(P * R.T * (R * R.T).inv())


def sf_values_actual(P: sp.Matrix, basis: tuple[int, ...]) -> list[sp.Rational]:
    C = coords_from_actual_rows(P, basis)
    vals = []
    for s, u in enumerate(basis):
        total = sp.Rational(0)
        for j in range(P.cols):
            w = sp.simplify(P[u, j])
            if w > 0:
                total += w * excess(C.row(j), s)
        vals.append(sp.simplify(total))
    return vals


def maxvol_ties_actual(P: sp.Matrix, k: int) -> tuple[sp.Rational, list[tuple[int, ...]]]:
    best = None
    ties: list[tuple[int, ...]] = []
    for basis in itertools.combinations(range(P.rows), k):
        R = P[list(basis), :]
        vol2 = sp.simplify((R * R.T).det())
        if vol2 == 0:
            continue
        if best is None or vol2 > best:
            best = vol2
            ties = [basis]
        elif vol2 == best:
            ties.append(basis)
    if best is None:
        raise RuntimeError("no basis")
    return best, ties


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
    sigma = [0] + [1] * m + [-1] * m
    rows = []
    for i in range(k):
        row = [sp.Rational(0)] * k
        row[i] = 1
        rows.append(row)
    rows.append([1] + [a * sigma[t] for t in range(1, k)])
    rows.append([1] + [-a * sigma[t] for t in range(1, k)])
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


def staircase(m: int, eps: sp.Rational = sp.Rational(0)) -> tuple[sp.Matrix, sp.Matrix]:
    k = 2 * m + 1
    sigma = [0] + [1] * m + [-1] * m
    h = 1 - eps
    d = eps / (2 * m)
    a = sp.Rational(1, 2)
    rows = []
    for i in range(k):
        row = [sp.Rational(0)] * k
        row[i] = 1
        rows.append(row)
    rows.append([h] + [d + a * sigma[t] for t in range(1, k)])
    rows.append([h] + [d - a * sigma[t] for t in range(1, k)])
    L = sp.Matrix(rows)
    B = sp.zeros(k, k + 2)
    B[0, 0] = eps
    for t in range(1, k):
        B[0, t] = -d
    B[0, k] = B[0, k + 1] = sp.Rational(1, 2)
    c = sp.Rational(1, 2 * m)
    for r in range(1, k):
        for t in range(1, k):
            B[r, t] = (1 if r == t else 0) - sigma[r] * sigma[t] * c
        B[r, k] = sigma[r] * c
        B[r, k + 1] = -sigma[r] * c
    return L, B


def summarize(name: str, L: sp.Matrix, B: sp.Matrix, theta_floor: sp.Rational | None = None) -> None:
    P = sp.simplify(L * B)
    k = L.cols
    d = delta(P)
    vol2, ties = maxvol_ties_actual(P, k)
    rows = []
    for basis in ties:
        vals = sf_values_actual(P, basis)
        rows.append((max(vals), basis))
    rows.sort()
    best_sf, best_basis = rows[0]
    worst_sf, worst_basis = rows[-1]
    print(
        f"{name}: delta={sp.factor(d)} ties={len(ties)} "
        f"best_basis={list(best_basis)} best_ratio={sp.factor(best_sf / d)} "
        f"worst_ratio={sp.factor(worst_sf / d)}"
    )
    if theta_floor is not None:
        near = []
        for basis in itertools.combinations(range(P.rows), k):
            R = P[list(basis), :]
            v2 = sp.simplify((R * R.T).det())
            if v2 != 0 and sp.simplify(v2 / vol2 - theta_floor**2) >= 0:
                vals = sf_values_actual(P, basis)
                near.append((sp.simplify(v2 / vol2), max(vals), basis))
        near.sort(key=lambda x: (x[1], x[2]))
        print(
            f"  theta>={theta_floor}: count={len(near)} "
            f"best_basis={list(near[0][2])} best_ratio={sp.factor(near[0][1] / d)} "
            f"best_vol_ratio={sp.factor(sp.sqrt(near[0][0]))}"
        )


def main() -> None:
    summarize("transverse_pair_a1_4", *transverse_pair(sp.Rational(1, 4), sp.Rational(1)))
    summarize("dense_pair_k7_a1_4", *dense_pair_k7())
    summarize("staircase_m2", *staircase(2))
    summarize("staircase_m3", *staircase(3))
    eps = sp.Rational(1, 1000)
    summarize("perturbed_staircase_m5_eps1e-3_exact", *staircase(5, eps))
    summarize("perturbed_staircase_m5_eps1e-3_quasi", *staircase(5, eps), theta_floor=1 - eps)


if __name__ == "__main__":
    main()
