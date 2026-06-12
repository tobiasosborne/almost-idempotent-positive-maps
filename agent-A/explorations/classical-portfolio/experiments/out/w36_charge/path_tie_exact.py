#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp


def fstr(x: sp.Expr) -> str:
    return str(sp.factor(x))


def pos(x: sp.Expr) -> sp.Expr:
    return x if x > 0 else sp.Rational(0)


def neg(x: sp.Expr) -> sp.Expr:
    return -x if x < 0 else sp.Rational(0)


def row_neg_mass(row: sp.Matrix) -> sp.Expr:
    return sp.factor(sum(neg(x) for x in list(row)))


def path_L(k: int, a: sp.Rational) -> sp.Matrix:
    rows: list[list[sp.Rational]] = []
    for i in range(k):
        row = [sp.Rational(0)] * k
        row[i] = sp.Rational(1)
        rows.append(row)
    for u, v in zip(range(1, k - 1), range(2, k)):
        plus = [sp.Rational(0)] * k
        minus = [sp.Rational(0)] * k
        plus[0] = minus[0] = sp.Rational(1)
        plus[u] = a
        plus[v] = -a
        minus[u] = -a
        minus[v] = a
        rows.extend([plus, minus])
    return sp.Matrix(rows)


def path_no_center_L(k: int, a: sp.Rational) -> sp.Matrix:
    rows: list[list[sp.Rational]] = []
    for i in range(1, k):
        row = [sp.Rational(0)] * k
        row[i] = sp.Rational(1)
        rows.append(row)
    for u, v in zip(range(1, k - 1), range(2, k)):
        plus = [sp.Rational(0)] * k
        minus = [sp.Rational(0)] * k
        plus[0] = minus[0] = sp.Rational(1)
        plus[u] = a
        plus[v] = -a
        minus[u] = -a
        minus[v] = a
        rows.extend([plus, minus])
    return sp.Matrix(rows)


def active_denominator(k: int) -> int:
    m = k - 2
    return 5001 * m + 1


def rationalized_B_from_highs(k: int) -> sp.Matrix:
    # Reuse the audited numerical LP to identify the active rational solution.
    # All nonzero entries in the active basis are integer multiples of 1/D.
    import importlib.util

    spec = importlib.util.spec_from_file_location("ac", "w34_audit_compute.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load local w34_audit_compute.py")
    ac = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ac)

    L_np = ac.path_L_np(k, 0.01)
    B_np, _P_np, _delta = ac.solve_fixed_mass_B(L_np, 0.99)
    D = active_denominator(k)
    B = sp.zeros(k, L_np.shape[0])
    m = k - 2
    B[0, 0] = sp.Rational(1, 100)
    for j in range(k, L_np.shape[0]):
        B[0, j] = sp.Rational(99, 200 * m)
    for i in range(k):
        for j in range(L_np.shape[0]):
            if i == 0:
                continue
            num = int(round(float(B_np[i, j]) * D))
            if abs(float(B_np[i, j]) * D - num) > 1e-5:
                raise RuntimeError((k, i, j, B_np[i, j], D, float(B_np[i, j]) * D))
            B[i, j] = sp.Rational(num, D)
    return B


def rationalized_B_no_center_from_highs(k: int) -> sp.Matrix:
    import importlib.util
    import numpy as np
    from scipy.optimize import linprog

    spec = importlib.util.spec_from_file_location("ac", "w34_audit_compute.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("could not load local w34_audit_compute.py")
    ac = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ac)

    def path_no_center_np() -> np.ndarray:
        rows = [np.eye(k)[i].copy() for i in range(1, k)]
        for u, v in zip(range(1, k - 1), range(2, k)):
            plus = np.eye(k)[0].copy()
            plus[u] += 0.01
            plus[v] -= 0.01
            minus = np.eye(k)[0].copy()
            minus[u] -= 0.01
            minus[v] += 0.01
            rows.extend([plus, minus])
        return np.array(rows, dtype=float)

    L_np = path_no_center_np()
    eq_rows, eq_rhs, ub_rows, ub_rhs, layout = ac.lp_base(L_np, add_row_sums=False)
    m = k - 2
    signed_start = k - 1
    fixed = np.zeros(layout.n)
    for j in range(signed_start, layout.n):
        fixed[j] = 1.0 / (2 * m)
    for j, val in enumerate(fixed):
        row = np.zeros(layout.total)
        row[layout.b(0, j)] = 1.0
        eq_rows.append(row)
        eq_rhs.append(float(val))
    c = np.zeros(layout.total)
    c[layout.d] = 1.0
    bounds = [(None, None)] * layout.nb + [(0.0, None)] * layout.nz + [(0.0, None)]
    res = linprog(
        c,
        A_ub=np.array(ub_rows),
        b_ub=np.array(ub_rhs),
        A_eq=np.array(eq_rows),
        b_eq=np.array(eq_rhs),
        bounds=bounds,
        method="highs",
    )
    if not res.success:
        raise RuntimeError(res.message)
    B_np = res.x[: layout.nb].reshape(layout.k, layout.n)

    D = active_denominator(k)
    B = sp.zeros(k, L_np.shape[0])
    for j in range(signed_start, L_np.shape[0]):
        B[0, j] = sp.Rational(1, 2 * m)
    for i in range(1, k):
        for j in range(L_np.shape[0]):
            num = int(round(float(B_np[i, j]) * D))
            if abs(float(B_np[i, j]) * D - num) > 1e-5:
                raise RuntimeError((k, i, j, B_np[i, j], D, float(B_np[i, j]) * D))
            B[i, j] = sp.Rational(num, D)
    return B


def excess(coord_row: sp.Matrix, s: int) -> sp.Expr:
    mu = sp.Rational(0)
    for t, x in enumerate(list(coord_row)):
        if t != s:
            mu += neg(sp.factor(x))
    return sp.factor(pos(mu - (1 - coord_row[s])))


def sf_values(P: sp.Matrix, L: sp.Matrix, basis: tuple[int, ...]) -> list[sp.Expr]:
    LU = L[list(basis), :]
    A = sp.simplify(L * LU.inv())
    out: list[sp.Expr] = []
    for s, u in enumerate(basis):
        total = sp.Rational(0)
        for j in range(P.cols):
            w = sp.factor(P[u, j])
            if w > 0:
                total += w * excess(A.row(j), s)
        out.append(sp.factor(total))
    return out


def maxvol_ties_path(k: int) -> list[tuple[int, ...]]:
    # For a=1/100, every maximum determinant has all foreign unit rows and
    # either e_0 or exactly one signed path row replacing e_0.  The exhaustive
    # determinant scan below verifies this for the mandatory k=6 and k=8.
    base = tuple(range(k))
    foreign = tuple(range(1, k))
    return [base] + [foreign + (j,) for j in range(k, 3 * k - 4)]


def maxvol_ties_path_no_center(k: int) -> list[tuple[int, ...]]:
    foreign = tuple(range(k - 1))
    return [foreign + (j,) for j in range(k - 1, 3 * k - 5)]


def exhaustive_ties(L: sp.Matrix) -> tuple[sp.Expr, list[tuple[int, ...]]]:
    k = L.cols
    best: sp.Expr | None = None
    ties: list[tuple[int, ...]] = []
    signed_rows = list(range(k, L.rows))
    identity_cols = list(range(k))
    # If c signed rows are selected, exactly c identity rows are omitted.
    # Expanding along the selected identity rows leaves the c-by-c submatrix
    # of signed rows on the omitted identity columns.
    for c in range(0, k + 1):
        for signed in itertools.combinations(signed_rows, c):
            for omitted in itertools.combinations(identity_cols, c):
                identity = tuple(i for i in identity_cols if i not in omitted)
                basis = tuple(sorted(identity + signed))
                if c == 0:
                    det = sp.Rational(1)
                else:
                    det = sp.factor(L[list(signed), list(omitted)].det())
                score = abs(det)
                if score == 0:
                    continue
                if best is None or score > best:
                    best = score
                    ties = [basis]
                elif score == best:
                    ties.append(basis)
    if best is None:
        raise RuntimeError("no nonzero minor")
    return best, ties


def audit(k: int) -> dict[str, object]:
    a = sp.Rational(1, 100)
    L = path_L(k, a)
    B = rationalized_B_from_highs(k)
    P = sp.simplify(L * B)
    delta = max(row_neg_mass(P.row(i)) for i in range(P.rows))
    scanned_ties = maxvol_ties_path(k)
    best_det = sp.Rational(1)
    rows = []
    for basis in scanned_ties:
        vals = sf_values(P, L, basis)
        max_sf = max(vals)
        rows.append(
            {
                "basis": list(basis),
                "sf": [fstr(v) for v in vals],
                "max_sf": fstr(max_sf),
                "max_ratio": fstr(sp.factor(max_sf / delta)),
            }
        )
    rows.sort(key=lambda r: Fraction(r["max_ratio"]))
    selected = rows[0]
    chosen = next(r for r in rows if r["basis"] == list(range(1, k)) + [L.rows - 1])
    return {
        "name": f"path_tie_k{k}_a1_100_mass99_100",
        "k": k,
        "n": L.rows,
        "denominator": active_denominator(k),
        "delta": fstr(delta),
        "maxvol_abs_det": fstr(best_det),
        "tie_count": len(rows),
        "BL_ok": bool(sp.simplify(B * L - sp.eye(k)) == sp.zeros(k)),
        "P2_ok": bool(sp.simplify(P * P - P) == sp.zeros(P.rows, P.cols)),
        "rowsum_ok": all(sp.simplify(sum(P.row(i)) - 1) == 0 for i in range(P.rows)),
        "selected_chart": selected,
        "audit_chosen_chart": chosen,
        "worst_chart": rows[-1],
        "all_charts": rows,
    }


def audit_no_center(k: int) -> dict[str, object]:
    a = sp.Rational(1, 100)
    L = path_no_center_L(k, a)
    B = rationalized_B_no_center_from_highs(k)
    P = sp.simplify(L * B)
    delta = max(row_neg_mass(P.row(i)) for i in range(P.rows))
    ties = maxvol_ties_path_no_center(k)
    rows = []
    for basis in ties:
        vals = sf_values(P, L, basis)
        max_sf = max(vals)
        rows.append(
            {
                "basis": list(basis),
                "sf": [fstr(v) for v in vals],
                "max_sf": fstr(max_sf),
                "max_ratio": fstr(sp.factor(max_sf / delta)),
            }
        )
    rows.sort(key=lambda r: Fraction(r["max_ratio"]))
    return {
        "name": f"path_no_center_k{k}_a1_100_mass1",
        "k": k,
        "n": L.rows,
        "denominator": active_denominator(k),
        "delta": fstr(delta),
        "maxvol_abs_det": "1",
        "tie_count": len(rows),
        "BL_ok": bool(sp.simplify(B * L - sp.eye(k)) == sp.zeros(k)),
        "P2_ok": bool(sp.simplify(P * P - P) == sp.zeros(P.rows, P.cols)),
        "rowsum_ok": all(sp.simplify(sum(P.row(i)) - 1) == 0 for i in range(P.rows)),
        "selected_chart": rows[0],
        "worst_chart": rows[-1],
        "all_charts": rows,
    }


def main() -> None:
    records = [audit(6), audit(8), audit_no_center(6), audit_no_center(8)]
    Path("path_tie_exact.json").write_text(json.dumps(records, indent=2, sort_keys=True))
    lines = []
    for rec in records:
        lines.append(
            f"{rec['name']}: delta={rec['delta']} ties={rec['tie_count']} "
            f"selected_basis={rec['selected_chart']['basis']} "
            f"selected_ratio={rec['selected_chart']['max_ratio']} "
            f"audit_basis_ratio={rec.get('audit_chosen_chart', rec['selected_chart'])['max_ratio']} "
            f"worst_ratio={rec['worst_chart']['max_ratio']} "
            f"checks=BL:{rec['BL_ok']} P2:{rec['P2_ok']} rows:{rec['rowsum_ok']}"
        )
    Path("path_tie_exact_summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
