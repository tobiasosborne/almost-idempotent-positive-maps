#!/usr/bin/env python3
from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable

import sympy as sp


def rat(x) -> sp.Rational:
    if isinstance(x, sp.Rational):
        return x
    if isinstance(x, Fraction):
        return sp.Rational(x.numerator, x.denominator)
    return sp.Rational(x)


def ffrac(x) -> Fraction:
    x = sp.Rational(x)
    return Fraction(int(x.p), int(x.q))


def fstr(x) -> str:
    return str(ffrac(x))


def ffloat(x) -> float:
    return float(ffrac(x))


def pos(x):
    return x if x > 0 else sp.Rational(0)


def neg_part(x):
    return -x if x < 0 else sp.Rational(0)


def row_neg_mass(row) -> sp.Rational:
    return sp.factor(sum(neg_part(x) for x in row))


def sign_for_index(m: int, r: int) -> int:
    if not 1 <= r <= 2 * m:
        raise ValueError(r)
    return 1 if r <= m else -1


def build_L(m: int, a: sp.Rational) -> sp.Matrix:
    """Dense transverse-pair support in the block-sign convention."""
    k = 2 * m + 1
    d = k + 2
    rows = []
    for i in range(k):
        rows.append([sp.Rational(1) if j == i else sp.Rational(0) for j in range(k)])
    plus = [sp.Rational(0)] * k
    minus = [sp.Rational(0)] * k
    plus[0] = minus[0] = sp.Rational(1)
    for j in range(1, k):
        sigma = sign_for_index(m, j)
        plus[j] = a * sigma
        minus[j] = -a * sigma
    rows.append(plus)
    rows.append(minus)
    assert len(rows) == d
    return sp.Matrix(rows)


def build_B(m: int, a: sp.Rational, c: sp.Rational, rho: sp.Rational = sp.Rational(1)) -> sp.Matrix:
    """Closed-form left inverse for the dense transverse-pair support.

    Row 0 puts mass rho/2 on each signed row and 1-rho on e_0.
    Foreign row r has q_r = sigma_r*c and pair entries +-sigma_r*c/(2a).
    """
    k = 2 * m + 1
    d = k + 2
    p = k
    n = k + 1
    rows = []

    row0 = [sp.Rational(0)] * d
    row0[0] = 1 - rho
    row0[p] = rho / 2
    row0[n] = rho / 2
    rows.append(row0)

    for r in range(1, k):
        sigma_r = sign_for_index(m, r)
        row = [sp.Rational(0)] * d
        for t in range(1, k):
            sigma_t = sign_for_index(m, t)
            row[t] = (sp.Rational(1) if t == r else sp.Rational(0)) - sigma_t * sigma_r * c
        row[p] = sigma_r * c / (2 * a)
        row[n] = -sigma_r * c / (2 * a)
        rows.append(row)
    return sp.Matrix(rows)


def closed_form_instance(
    m: int,
    a: sp.Rational = sp.Rational(1, 2),
    cap: sp.Rational = sp.Rational(1, 2),
    c: sp.Rational | None = None,
    rho: sp.Rational = sp.Rational(1),
) -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Rational]:
    if c is None:
        c = cap / (sp.Rational(m - 1) + sp.Rational(1, 2) / a)
    L = build_L(m, a)
    B = build_B(m, a, c, rho)
    P = sp.factor(L * B)
    return L, B, P, c


def volume_sq(rows: sp.Matrix) -> sp.Rational:
    gram = rows * rows.T
    return sp.factor(gram.det())


def dense_dependency_matrix(m: int, a: sp.Rational) -> sp.Matrix:
    k = 2 * m + 1
    d = k + 2
    dep_plus = [sp.Rational(0)] * d
    dep_minus = [sp.Rational(0)] * d
    dep_plus[0] = -1
    dep_minus[0] = -1
    for j in range(1, k):
        sigma = sign_for_index(m, j)
        dep_plus[j] = -a * sigma
        dep_minus[j] = a * sigma
    dep_plus[k] = 1
    dep_minus[k + 1] = 1
    return sp.Matrix.hstack(sp.Matrix(dep_plus), sp.Matrix(dep_minus))


def maxvol_ties(
    P: sp.Matrix,
    dependency_matrix: sp.Matrix | None = None,
    compute_volume: bool = True,
    rank_hint: int | None = None,
) -> tuple[list[tuple[int, ...]], sp.Rational | None]:
    n = P.rows
    k = rank_hint if rank_hint is not None else P.rank()
    if n - k == 2:
        N = dependency_matrix
        if N is None:
            null = P.T.nullspace()
            if len(null) == 2:
                N = sp.Matrix.hstack(null[0], null[1])
        if N is not None:
            best_minor = None
            omitted_ties: list[tuple[int, int]] = []
            for omit in itertools.combinations(range(n), 2):
                minor = sp.factor(N[list(omit), :].det() ** 2)
                if best_minor is None or minor > best_minor:
                    best_minor = minor
                    omitted_ties = [omit]
                elif minor == best_minor:
                    omitted_ties.append(omit)
            if best_minor is not None and best_minor > 0:
                ties = [tuple(i for i in range(n) if i not in omit) for omit in omitted_ties]
                vol = volume_sq(P[list(ties[0]), :]) if compute_volume else None
                return ties, vol
    best = None
    ties: list[tuple[int, ...]] = []
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
    return ties, sp.factor(best) if compute_volume else None


def coordinates(P: sp.Matrix, pivots: tuple[int, ...]) -> sp.Matrix:
    basis = P[list(pivots), :]
    gram_inv = (basis * basis.T).inv()
    rows = []
    for i in range(P.rows):
        c = P[i, :] * basis.T * gram_inv
        rows.append([sp.factor(c[0, t]) for t in range(len(pivots))])
    return sp.Matrix(rows)


def coordinates_from_L(L: sp.Matrix, pivots: tuple[int, ...]) -> sp.Matrix:
    basis_L = L[list(pivots), :]
    inv_basis_L = basis_L.inv()
    rows = []
    for i in range(L.rows):
        c = L[i, :] * inv_basis_L
        rows.append([sp.factor(c[0, t]) for t in range(len(pivots))])
    return sp.Matrix(rows)


def dense_row(m: int, a: sp.Rational, idx: int) -> list[sp.Rational]:
    k = 2 * m + 1
    p = k
    n = k + 1
    if 0 <= idx < k:
        return [sp.Rational(1) if j == idx else sp.Rational(0) for j in range(k)]
    row = [sp.Rational(0)] * k
    row[0] = sp.Rational(1)
    sign = 1 if idx == p else -1
    if idx not in {p, n}:
        raise ValueError(idx)
    for j in range(1, k):
        row[j] = sign * a * sign_for_index(m, j)
    return row


def coordinates_dense_L(m: int, a: sp.Rational, pivots: tuple[int, ...]) -> sp.Matrix:
    k = 2 * m + 1
    d = k + 2
    pivot_set = set(pivots)
    omitted_id = [i for i in range(k) if i not in pivot_set]
    signed = [i for i in [k, k + 1] if i in pivot_set]
    if len(omitted_id) != len(signed):
        raise ValueError("non-square dense replacement basis")

    signed_rows = {idx: dense_row(m, a, idx) for idx in signed}
    if omitted_id:
        M = sp.Matrix([[signed_rows[e][r] for e in signed] for r in omitted_id])
        if M.det() == 0:
            raise ValueError("singular dense replacement basis")
        Minv = M.inv()
    else:
        Minv = sp.Matrix(0, 0, [])

    rows = []
    for idx in range(d):
        y = dense_row(m, a, idx)
        coeff_by_pivot: dict[int, sp.Rational] = {}
        if omitted_id:
            rhs = sp.Matrix([y[r] for r in omitted_id])
            lambdas = Minv * rhs
            for col, e in enumerate(signed):
                coeff_by_pivot[e] = sp.factor(lambdas[col, 0])
        else:
            for e in signed:
                coeff_by_pivot[e] = sp.Rational(0)
        for j in range(k):
            if j in pivot_set:
                correction = sum(coeff_by_pivot.get(e, 0) * signed_rows[e][j] for e in signed)
                coeff_by_pivot[j] = sp.factor(y[j] - correction)
        rows.append([sp.factor(coeff_by_pivot[p]) for p in pivots])
    return sp.Matrix(rows)


def sf_rows_for_chart(
    P: sp.Matrix,
    pivots: tuple[int, ...],
    L: sp.Matrix | None = None,
    dense_params: tuple[int, sp.Rational] | None = None,
) -> tuple[list[dict], sp.Matrix]:
    if dense_params is not None:
        A = coordinates_dense_L(dense_params[0], dense_params[1], pivots)
    else:
        A = coordinates_from_L(L, pivots) if L is not None else coordinates(P, pivots)
    out = []
    for s_pos, u in enumerate(pivots):
        total = sp.Rational(0)
        nonzero = []
        for j in range(P.cols):
            ppos = pos(P[u, j])
            mu = sum(neg_part(A[j, t]) for t in range(A.cols) if t != s_pos)
            deficit = 1 - A[j, s_pos]
            excess = pos(mu - deficit)
            contrib = sp.factor(ppos * excess)
            total += contrib
            if contrib:
                nonzero.append(
                    {
                        "j": j,
                        "P_u_j_pos": fstr(ppos),
                        "E": fstr(excess),
                        "contrib": fstr(contrib),
                        "coeff": [fstr(A[j, t]) for t in range(A.cols)],
                    }
                )
        nonzero.sort(key=lambda r: Fraction(r["contrib"]), reverse=True)
        out.append(
            {
                "s_pos": s_pos,
                "pivot": u,
                "sf": fstr(sp.factor(total)),
                "sf_float": ffloat(total),
                "top": nonzero[:8],
            }
        )
    return out, A


def matrix_exact_zero(M: sp.Matrix) -> bool:
    return all(x == 0 for x in M)


def verify_instance(L: sp.Matrix, B: sp.Matrix, P: sp.Matrix, structural: bool = False) -> dict:
    k = B.rows
    d = P.rows
    BL_err = sp.factor(B * L - sp.eye(k))
    B_rowsum_err = sp.factor(B * sp.ones(d, 1) - sp.ones(k, 1))
    P_rowsum_err = sp.factor(P * sp.ones(d, 1) - sp.ones(d, 1))
    BL_exact = matrix_exact_zero(BL_err)
    if structural:
        P2_exact = BL_exact
        rank = k if BL_exact else None
    else:
        P2_err = sp.factor(P * P - P)
        P2_exact = matrix_exact_zero(P2_err)
        rank = P.rank()
    negs = [row_neg_mass(list(P[i, :])) for i in range(P.rows)]
    B_negs = [row_neg_mass(list(B[i, :])) for i in range(B.rows)]
    delta = max(negs) if negs else sp.Rational(0)
    return {
        "BL_exact": BL_exact,
        "P2_exact": P2_exact,
        "P2_verification": "structural_from_BL" if structural else "direct_matrix_multiply",
        "B_rowsum_exact": matrix_exact_zero(B_rowsum_err),
        "P_rowsum_exact": matrix_exact_zero(P_rowsum_err),
        "rank": rank,
        "delta": fstr(delta),
        "delta_float": ffloat(delta),
        "row_neg_masses": [fstr(x) for x in negs],
        "B_row_neg_masses": [fstr(x) for x in B_negs],
        "max_B_row_neg_mass": fstr(max(B_negs) if B_negs else 0),
    }


def intended_chart_sf(m: int, a: sp.Rational, rho: sp.Rational, delta: sp.Rational) -> dict:
    sf = sp.factor(sp.Rational(m) * a * rho)
    ratio = None if delta == 0 else sp.factor(sf / delta)
    return {
        "sf": fstr(sf),
        "sf_float": ffloat(sf),
        "sf_over_delta": "inf" if ratio is None and sf else (fstr(ratio) if ratio is not None else "0"),
        "sf_over_delta_float": None if ratio is None else ffloat(ratio),
    }


def audit_instance(
    label: str,
    m: int,
    a: sp.Rational,
    cap: sp.Rational,
    c: sp.Rational | None = None,
    rho: sp.Rational = sp.Rational(1),
    keep_tie_details: bool = True,
) -> dict:
    L, B, P, c_used = closed_form_instance(m, a=a, cap=cap, c=c, rho=rho)
    structural_verify = (not keep_tie_details) and m > 8
    ver = verify_instance(L, B, P, structural=structural_verify)
    delta = rat(ver["delta"])
    ties, best_vol = maxvol_ties(
        P,
        dependency_matrix=dense_dependency_matrix(m, a),
        compute_volume=keep_tie_details or m <= 8,
        rank_hint=2 * m + 1,
    )
    tie_records = []
    best_row = None
    best_chart = None
    worst_chart = None
    for pivots in ties:
        sf_rows, A = sf_rows_for_chart(P, pivots, L=L, dense_params=(m, a))
        for row in sf_rows:
            sf = rat(row["sf"])
            ratio = None if delta == 0 else sp.factor(sf / delta)
            row["sf_over_delta"] = "inf" if ratio is None and sf else (fstr(ratio) if ratio is not None else "0")
            row["sf_over_delta_float"] = None if ratio is None else ffloat(ratio)
        chart_best = max(sf_rows, key=lambda r: -1 if r["sf_over_delta_float"] is None else r["sf_over_delta_float"])
        chart_rec = {
            "pivots": list(pivots),
            "chart_best_sf": chart_best["sf"],
            "chart_best_ratio": chart_best["sf_over_delta"],
            "chart_best_ratio_float": chart_best["sf_over_delta_float"],
            "chart_best_pivot": chart_best["pivot"],
            "sf_rows": sf_rows if keep_tie_details else None,
        }
        tie_records.append(chart_rec)
        if best_row is None or chart_best["sf_over_delta_float"] > best_row["sf_over_delta_float"]:
            best_row = chart_best | {"pivots": list(pivots)}
            best_chart = chart_rec
        if worst_chart is None or chart_best["sf_over_delta_float"] < worst_chart["chart_best_ratio_float"]:
            worst_chart = chart_rec
    out = {
        "label": label,
        "m": m,
        "k": 2 * m + 1,
        "d": 2 * m + 3,
        "a": fstr(a),
        "cap": fstr(cap),
        "c": fstr(c_used),
        "rho": fstr(rho),
        "verification": ver,
        "intended_chart": intended_chart_sf(m, a, rho, delta),
        "maxvol_volume_sq": fstr(best_vol) if best_vol is not None else "not_computed",
        "maxvol_tie_count": len(ties),
        "maxvol_ties": [list(t) for t in ties],
        "tie_best_ratio": best_chart["chart_best_ratio"] if best_chart else "0",
        "tie_best_ratio_float": best_chart["chart_best_ratio_float"] if best_chart else 0.0,
        "tie_worst_ratio": worst_chart["chart_best_ratio"] if worst_chart else "0",
        "tie_worst_ratio_float": worst_chart["chart_best_ratio_float"] if worst_chart else 0.0,
        "tie_best_record": best_chart,
        "tie_worst_record": worst_chart,
        "tie_records": tie_records if keep_tie_details else None,
    }
    return out


def feasible_c_for_cap(m: int, a: Fraction, cap: Fraction) -> Fraction | None:
    """Largest c allowed by foreign rows, if the pair rows are also within cap."""
    aa = Fraction(a)
    cc = cap / (Fraction(m - 1, 1) + Fraction(1, 2) / aa)
    pair_neg = Fraction(m, 1) * aa * abs(Fraction(1, 1) - 2 * m * cc)
    if pair_neg <= cap:
        return cc
    return None


def max_feasible_amplitude(m: int, cap: Fraction, denom: int = 2400) -> Fraction | None:
    """Grid search for the largest feasible a in (0,1/2]."""
    best = None
    max_num = denom // 2
    for num in range(1, max_num + 1):
        a = Fraction(num, denom)
        if feasible_c_for_cap(m, a, cap) is not None:
            best = a
    return best


def nearby_amplitudes(a: Fraction, denom: int = 2400) -> list[Fraction]:
    nums = set()
    base = round(a * denom)
    for off in [-4, -2, -1, 0, 1, 2, 4]:
        n = base + off
        if 1 <= n <= denom // 2:
            nums.add(n)
    return [Fraction(n, denom) for n in sorted(nums)]


def closed_form_suite() -> list[dict]:
    records = []
    for m in [2, 3, 5, 8]:
        records.append(audit_instance(f"closed_form_m{m}_a1/2_cap1/2", m, sp.Rational(1, 2), sp.Rational(1, 2), keep_tie_details=m <= 8))
    return records


def chart_recompute_suite() -> list[dict]:
    return [
        audit_instance(f"chart_recompute_m{m}_a1/2_cap1/2", m, sp.Rational(1, 2), sp.Rational(1, 2), keep_tie_details=True)
        for m in [2, 3, 5, 8]
    ]


def threshold_suite() -> list[dict]:
    caps = [Fraction(n, 1000) for n in range(300, 501, 25)]
    ms = list(range(2, 13))
    records = []
    for cap in caps:
        for m in ms:
            a0 = max_feasible_amplitude(m, cap)
            if a0 is None:
                continue
            best = None
            for a in [a0]:
                c = feasible_c_for_cap(m, a, cap)
                if c is None:
                    continue
                rec = audit_instance(
                    f"threshold_cap{cap}_m{m}_a{a}",
                    m,
                    rat(a),
                    rat(cap),
                    c=rat(c),
                    keep_tie_details=False,
                )
                rec["search_note"] = {
                    "grid_denom": 2400,
                    "max_feasible_a_grid": str(a0),
                    "candidate_a": str(a),
                }
                if best is None or rec["tie_best_ratio_float"] > best["tie_best_ratio_float"]:
                    best = rec
            if best is not None:
                records.append(best)
    return records


def summarize(records: Iterable[dict]) -> str:
    lines = []
    for rec in records:
        ver = rec["verification"]
        lines.append(
            " ".join(
                [
                    rec["label"],
                    f"m={rec['m']}",
                    f"k={rec['k']}",
                    f"a={rec['a']}",
                    f"c={rec['c']}",
                    f"delta={ver['delta']}",
                    f"intended={rec['intended_chart']['sf_over_delta']}",
                    f"recomp_best={rec['tie_best_ratio']}",
                    f"recomp_worst={rec['tie_worst_ratio']}",
                    f"ties={rec['maxvol_tie_count']}",
                    f"vol2={rec['maxvol_volume_sq']}",
                    f"okBL={ver['BL_exact']}",
                    f"okP2={ver['P2_exact']}",
                ]
            )
        )
    return "\n".join(lines) + ("\n" if lines else "")


def threshold_cap_summary(records: Iterable[dict]) -> str:
    by_cap: dict[str, list[dict]] = {}
    for rec in records:
        by_cap.setdefault(rec["cap"], []).append(rec)
    lines = []
    for cap in sorted(by_cap, key=lambda x: Fraction(x)):
        rows = sorted(by_cap[cap], key=lambda r: r["m"])
        best = max(rows, key=lambda r: r["tie_best_ratio_float"])
        parts = [
            f"cap={cap}",
            f"max_recomp_ratio={best['tie_best_ratio']}",
            f"at_m={best['m']}",
            f"a={best['a']}",
            "per_m="
            + ",".join(
                f"{r['m']}:{r['tie_best_ratio']}@a={r['a']}/int={r['intended_chart']['sf_over_delta']}"
                for r in rows
            ),
        ]
        lines.append(" ".join(parts))
    return "\n".join(lines) + ("\n" if lines else "")


def write_outputs(prefix: str, records: list[dict]) -> None:
    Path(f"{prefix}.json").write_text(json.dumps(records, indent=2, sort_keys=True))
    Path(f"{prefix}.txt").write_text(summarize(records))
    if prefix == "threshold_audit":
        Path("threshold_cap_summary.txt").write_text(threshold_cap_summary(records))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["closed-form", "chart", "threshold", "all"], default="all")
    args = parser.parse_args()

    if args.mode in {"closed-form", "all"}:
        records = closed_form_suite()
        write_outputs("closed_form_audit", records)
        print(summarize(records), end="")
    if args.mode in {"chart", "all"}:
        records = chart_recompute_suite()
        write_outputs("chart_recompute_audit", records)
        print(summarize(records), end="")
    if args.mode in {"threshold", "all"}:
        records = threshold_suite()
        write_outputs("threshold_audit", records)
        print(summarize(records), end="")
        print(threshold_cap_summary(records), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
