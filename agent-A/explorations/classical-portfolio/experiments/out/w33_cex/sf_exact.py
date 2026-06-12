#!/usr/bin/env python3
from __future__ import annotations

import argparse
import itertools
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


def Q(text: str | int | Fraction) -> Fraction:
    return text if isinstance(text, Fraction) else Fraction(text)


def mat(rows):
    return sp.Matrix([[sp.Rational(x.numerator, x.denominator) if isinstance(x, Fraction) else sp.Rational(x) for x in row] for row in rows])


def frac(x) -> Fraction:
    x = sp.Rational(x)
    return Fraction(int(x.p), int(x.q))


def fstr(x) -> str:
    return str(frac(x))


def ffloat(x) -> float:
    return float(frac(x))


def pos(x):
    return x if x > 0 else sp.Rational(0)


def neg_part(x):
    return -x if x < 0 else sp.Rational(0)


def row_neg_mass(row) -> sp.Rational:
    return sum(neg_part(x) for x in row)


def volume_sq(rows: sp.Matrix) -> sp.Rational:
    gram = rows * rows.T
    return sp.factor(gram.det())


def maxvol_pivots(P: sp.Matrix):
    n = P.rows
    k = P.rank()
    best = None
    ties = []
    for inds in itertools.combinations(range(n), k):
        R = P[list(inds), :]
        if R.rank() < k:
            continue
        vol = volume_sq(R)
        if best is None or vol > best:
            best = vol
            ties = [inds]
        elif vol == best:
            ties.append(inds)
    if best is None:
        raise RuntimeError("no row basis")
    return list(ties[0]), ties, sp.factor(best)


def coordinates(P: sp.Matrix, pivots: list[int]) -> sp.Matrix:
    basis = P[pivots, :]
    gram_inv = (basis * basis.T).inv()
    rows = []
    for i in range(P.rows):
        c = P[i, :] * basis.T * gram_inv
        rows.append([sp.factor(c[0, t]) for t in range(len(pivots))])
    return sp.Matrix(rows)


def sf_for_chart(P: sp.Matrix, pivots: list[int]):
    A = coordinates(P, pivots)
    out = []
    for s_pos, u in enumerate(pivots):
        total = sp.Rational(0)
        top = []
        for j in range(P.cols):
            ppos = pos(P[u, j])
            mu = sum(neg_part(A[j, t]) for t in range(A.cols) if t != s_pos)
            deficit = 1 - A[j, s_pos]
            excess = pos(mu - deficit)
            contrib = sp.factor(ppos * excess)
            total += contrib
            if contrib:
                top.append(
                    {
                        "j": j,
                        "P_u_j_pos": fstr(ppos),
                        "E": fstr(excess),
                        "contrib": fstr(contrib),
                        "coeff": [fstr(A[j, t]) for t in range(A.cols)],
                    }
                )
        top.sort(key=lambda r: Fraction(r["contrib"]), reverse=True)
        out.append(
            {
                "s_pos": s_pos,
                "pivot": u,
                "sf": fstr(sp.factor(total)),
                "sf_float": ffloat(total),
                "top": top[:10],
            }
        )
    return out, A


def audit(P: sp.Matrix, label: str):
    P2_err = P * P - P
    rowsum_err = P * sp.ones(P.cols, 1) - sp.ones(P.rows, 1)
    negs = [sp.factor(row_neg_mass(list(P[i, :]))) for i in range(P.rows)]
    delta = max(negs) if negs else sp.Rational(0)
    pivots, ties, best_vol = maxvol_pivots(P)
    sf_rows, A = sf_for_chart(P, pivots)
    for row in sf_rows:
        sf = Fraction(row["sf"])
        row["sf_over_delta"] = "inf" if delta == 0 and sf else (fstr(sp.Rational(sf.numerator, sf.denominator) / delta) if delta else "0")
        row["sf_over_delta_float"] = None if delta == 0 else float(sp.Rational(sf.numerator, sf.denominator) / delta)
    coeff_abs = [abs(A[i, t]) for i in range(A.rows) for t in range(A.cols)]
    return {
        "label": label,
        "n": P.rows,
        "rank": P.rank(),
        "idempotence_exact": all(x == 0 for x in P2_err),
        "rowsum_exact": all(x == 0 for x in rowsum_err),
        "delta": fstr(delta),
        "delta_float": ffloat(delta),
        "row_neg_masses": [fstr(x) for x in negs],
        "pivots": pivots,
        "maxvol_tie_count": len(ties),
        "maxvol_ties_first_20": [list(t) for t in ties[:20]],
        "maxvol_volume_sq": fstr(best_vol),
        "max_abs_coeff": fstr(max(coeff_abs) if coeff_abs else 0),
        "sf_rows": sf_rows,
    }


def transverse_pair(a: Fraction, m: Fraction) -> sp.Matrix:
    c = a / (1 + 4 * a * a)
    B = mat(
        [
            [1 - m, 0, 0, m / 2, m / 2],
            [0, 1 - 2 * a * c, 2 * a * c, c, -c],
            [0, 2 * a * c, 1 - 2 * a * c, -c, c],
        ]
    )
    L = mat(
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, a, -a],
            [1, -a, a],
        ]
    )
    return L * B


def duplicate_pair(q: int, a: Fraction, m: Fraction) -> sp.Matrix:
    c = a / (1 + 4 * a * a)
    L_rows = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    for _ in range(q):
        L_rows.append([1, a, -a])
        L_rows.append([1, -a, a])
    B0 = [1 - m, 0, 0]
    B1 = [0, 1 - 2 * a * c, 2 * a * c]
    B2 = [0, 2 * a * c, 1 - 2 * a * c]
    for _ in range(q):
        B0 += [m / (2 * q), m / (2 * q)]
        B1 += [c / q, -c / q]
        B2 += [-c / q, c / q]
    return mat(L_rows) * mat([B0, B1, B2])


def split_block(eps: Fraction) -> sp.Matrix:
    return mat(
        [
            [Fraction(1, 2), Fraction(1, 2) + eps, -eps],
            [1 / (2 * (1 + 2 * eps)), Fraction(1, 2), eps / (1 + 2 * eps)],
            [0, 0, 1],
        ]
    )


def run_suite():
    records = []
    for a in [Fraction(1, 200), Fraction(1, 100), Fraction(1, 50), Fraction(1, 20)]:
        records.append(audit(transverse_pair(a, Fraction(99, 100)), f"transverse_pair_a_{a}_m_99/100"))
    for q in [2, 5, 10, 25]:
        records.append(audit(duplicate_pair(q, Fraction(1, 100), Fraction(99, 100)), f"duplicate_pair_q_{q}_a_1/100_m_99/100"))
    for eps in [Fraction(1, 100), Fraction(1, 1000), Fraction(1, 10000)]:
        records.append(audit(split_block(eps), f"split_block_eps_{eps}"))
    return records


def summarize(records):
    lines = []
    for rec in records:
        best = max(rec["sf_rows"], key=lambda r: r["sf_over_delta_float"] if r["sf_over_delta_float"] is not None else -1)
        lines.append(
            f"{rec['label']}: n={rec['n']} rank={rec['rank']} delta={rec['delta']} "
            f"pivots={rec['pivots']} max|a|={rec['max_abs_coeff']} "
            f"max_sf/delta={best['sf_over_delta']} sf={best['sf']} pivot={best['pivot']} "
            f"maxvol_ties={rec['maxvol_tie_count']}"
        )
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-json", default="sf_exact_results.json")
    parser.add_argument("--out-summary", default="sf_exact_summary.txt")
    args = parser.parse_args()
    records = run_suite()
    Path(args.out_json).write_text(json.dumps(records, indent=2, sort_keys=True))
    summary = summarize(records)
    Path(args.out_summary).write_text(summary)
    print(summary, end="")


if __name__ == "__main__":
    main()
