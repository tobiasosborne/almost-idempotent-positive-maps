#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

import numpy as np
import sympy as sp
from scipy.optimize import linprog


def S(x: Any) -> sp.Rational:
    if isinstance(x, Fraction):
        return sp.Rational(x.numerator, x.denominator)
    if isinstance(x, sp.Basic):
        return x
    return sp.Rational(x)


def mat(rows: list[list[Any]]) -> sp.Matrix:
    return sp.Matrix([[S(x) for x in row] for row in rows])


def fstr(x: Any) -> str:
    x = sp.factor(S(x))
    return str(x)


def pos(x: sp.Rational) -> sp.Rational:
    return x if x > 0 else sp.Rational(0)


def neg(x: sp.Rational) -> sp.Rational:
    return -x if x < 0 else sp.Rational(0)


def row_neg_mass(row: list[sp.Rational]) -> sp.Rational:
    return sp.factor(sum(neg(x) for x in row))


def excess_coeff(row: list[sp.Rational], s: int) -> sp.Rational:
    mu = sum(neg(row[t]) for t in range(len(row)) if t != s)
    deficit = 1 - row[s]
    return sp.factor(pos(mu - deficit))


def maxvol_ties_L(L: sp.Matrix) -> tuple[sp.Rational, list[tuple[int, ...]], list[dict[str, Any]]]:
    n, k = L.rows, L.cols
    best: sp.Rational | None = None
    ties: list[tuple[int, ...]] = []
    all_rows = []
    for inds in itertools.combinations(range(n), k):
        det = sp.factor(L[list(inds), :].det())
        val = abs(det)
        all_rows.append({"basis": list(inds), "det": fstr(det), "abs_det": fstr(val)})
        if best is None or val > best:
            best = val
            ties = [inds]
        elif val == best:
            ties.append(inds)
    assert best is not None
    return best, ties, all_rows


def maxvol_ties_P(P: sp.Matrix) -> tuple[sp.Rational, list[tuple[int, ...]]]:
    n, rank = P.rows, P.rank()
    best: sp.Rational | None = None
    ties: list[tuple[int, ...]] = []
    for inds in itertools.combinations(range(n), rank):
        R = P[list(inds), :]
        if R.rank() < rank:
            continue
        vol = sp.factor((R * R.T).det())
        if best is None or vol > best:
            best = vol
            ties = [inds]
        elif vol == best:
            ties.append(inds)
    assert best is not None
    return best, ties


def sf_for_basis(L: sp.Matrix, B: sp.Matrix, basis: tuple[int, ...]) -> list[dict[str, Any]]:
    P = L * B
    C = L[list(basis), :]
    A = sp.simplify(L * C.inv())
    rows = []
    for s_pos, u in enumerate(basis):
        sf = sp.Rational(0)
        contributors = []
        for j in range(P.cols):
            e = excess_coeff([A[j, t] for t in range(A.cols)], s_pos)
            contribution = sp.factor(pos(P[u, j]) * e)
            sf += contribution
            if contribution:
                contributors.append(
                    {
                        "j": j,
                        "P_pos": fstr(pos(P[u, j])),
                        "E": fstr(e),
                        "contribution": fstr(contribution),
                        "coeff": [fstr(A[j, t]) for t in range(A.cols)],
                    }
                )
        rows.append(
            {
                "s_pos": s_pos,
                "pivot": int(u),
                "sf": fstr(sp.factor(sf)),
                "contributors": contributors,
            }
        )
    return rows


def transverse_LB(a: sp.Rational, m: sp.Rational) -> tuple[sp.Matrix, sp.Matrix, sp.Rational]:
    c = sp.factor(a / (1 + 4 * a * a))
    L = mat(
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, a, -a],
            [1, -a, a],
        ]
    )
    B = mat(
        [
            [1 - m, 0, 0, m / 2, m / 2],
            [0, 1 - 2 * a * c, 2 * a * c, c, -c],
            [0, 2 * a * c, 1 - 2 * a * c, -c, c],
        ]
    )
    return L, B, c


def audit_A1() -> dict[str, Any]:
    a, m = sp.symbols("a m", positive=True)
    Lsym, Bsym, csym = transverse_LB(a, m)
    BL = sp.simplify(Bsym * Lsym)
    row_sums_L = [sp.factor(sum(Lsym[i, j] for j in range(Lsym.cols))) for i in range(Lsym.rows)]
    row_sums_B = [sp.factor(sum(Bsym[i, j] for j in range(Bsym.cols))) for i in range(Bsym.rows)]
    dets = []
    for inds in itertools.combinations(range(5), 3):
        dets.append({"basis": list(inds), "det_L": str(sp.factor(Lsym[list(inds), :].det()))})

    sample_a = sp.Rational(1, 100)
    sample_m = sp.Rational(99, 100)
    L, B, c = transverse_LB(sample_a, sample_m)
    P = L * B
    best_L, ties_L, _ = maxvol_ties_L(L)
    best_P, ties_P = maxvol_ties_P(P)
    delta = max(row_neg_mass([P[i, j] for j in range(P.cols)]) for i in range(P.rows))
    tie_sf = []
    for basis in ties_L:
        rows = sf_for_basis(L, B, basis)
        for row in rows:
            row["sf_over_delta"] = fstr(S(row["sf"]) / delta) if delta else "inf"
        tie_sf.append({"basis": list(basis), "sf_rows": rows})
    intended_sf = next(x for x in tie_sf if x["basis"] == [0, 1, 2])["sf_rows"][0]["sf"]
    return {
        "symbolic_BL_minus_I_zero": bool(sp.simplify(BL - sp.eye(3)) == sp.zeros(3)),
        "symbolic_c": str(csym),
        "symbolic_row_sums_L": [str(x) for x in row_sums_L],
        "symbolic_row_sums_B": [str(x) for x in row_sums_B],
        "symbolic_L_minors": dets,
        "formula_conditions_noted": "delta=c requires a>0, a<=1/2 for intended/tie max minors, and m/2>=2*a*c for signed-row last entries nonnegative",
        "sample": {
            "a": fstr(sample_a),
            "m": fstr(sample_m),
            "c_delta": fstr(c),
            "P2_minus_P_zero": bool(P * P - P == sp.zeros(P.rows)),
            "row_sums_P": [fstr(sum(P[i, j] for j in range(P.cols))) for i in range(P.rows)],
            "row_neg_masses": [fstr(row_neg_mass([P[i, j] for j in range(P.cols)])) for i in range(P.rows)],
            "delta": fstr(delta),
            "max_abs_det_L": fstr(best_L),
            "maxvol_ties_L": [list(t) for t in ties_L],
            "maxvol_ties_P": [list(t) for t in ties_P],
            "maxvol_volume_sq_P": fstr(best_P),
            "intended_sf": intended_sf,
            "intended_ratio": fstr(S(intended_sf) / delta),
            "claimed_ratio_m_1_plus_4a2": fstr(sample_m * (1 + 4 * sample_a * sample_a)),
            "all_tie_sf": tie_sf,
        },
    }


def duplicate_L_np(q: int, a: float) -> np.ndarray:
    rows = [np.eye(3)[0], np.eye(3)[1], np.eye(3)[2]]
    for _ in range(q):
        rows.append(np.array([1.0, a, -a]))
        rows.append(np.array([1.0, -a, a]))
    return np.array(rows, dtype=float)


class LPLayout:
    def __init__(self, k: int, n: int):
        self.k = k
        self.n = n
        self.nb = k * n
        self.nz = n * n
        self.d = self.nb + self.nz
        self.total = self.d + 1

    def b(self, r: int, j: int) -> int:
        return r * self.n + j

    def z(self, i: int, j: int) -> int:
        return self.nb + i * self.n + j


def lp_base(L: np.ndarray, add_row_sums: bool = True) -> tuple[list[np.ndarray], list[float], list[np.ndarray], list[float], LPLayout]:
    n, k = L.shape
    layout = LPLayout(k, n)
    eq_rows: list[np.ndarray] = []
    eq_rhs: list[float] = []
    for r in range(k):
        if add_row_sums:
            row = np.zeros(layout.total)
            for j in range(n):
                row[layout.b(r, j)] = 1.0
            eq_rows.append(row)
            eq_rhs.append(1.0)
        for t in range(k):
            row = np.zeros(layout.total)
            for j in range(n):
                row[layout.b(r, j)] = L[j, t]
            eq_rows.append(row)
            eq_rhs.append(1.0 if r == t else 0.0)
    ub_rows: list[np.ndarray] = []
    ub_rhs: list[float] = []
    for i in range(n):
        for j in range(n):
            row = np.zeros(layout.total)
            row[layout.z(i, j)] = -1.0
            for r in range(k):
                row[layout.b(r, j)] -= L[i, r]
            ub_rows.append(row)
            ub_rhs.append(0.0)
    for i in range(n):
        row = np.zeros(layout.total)
        for j in range(n):
            row[layout.z(i, j)] = 1.0
        row[layout.d] = -1.0
        ub_rows.append(row)
        ub_rhs.append(0.0)
    return eq_rows, eq_rhs, ub_rows, ub_rhs, layout


def excess_np(L: np.ndarray, s: int = 0) -> np.ndarray:
    vals = []
    for row in L:
        mu = np.maximum(-np.delete(row, s), 0.0).sum()
        vals.append(max(float(mu - (1.0 - row[s])), 0.0))
    return np.array(vals)


def solve_min_delta_fixed_b0(L: np.ndarray, fixed_b0: np.ndarray) -> dict[str, Any]:
    eq_rows, eq_rhs, ub_rows, ub_rhs, layout = lp_base(L)
    for j, val in enumerate(fixed_b0):
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
    out: dict[str, Any] = {"success": bool(res.success), "status": int(res.status), "message": res.message}
    if not res.success:
        return out
    B = res.x[: layout.nb].reshape(layout.k, layout.n)
    P = L @ B
    E = excess_np(L, 0)
    target = float(np.maximum(B[0], 0.0) @ E)
    delta = float(np.maximum(-P, 0.0).sum(axis=1).max())
    out.update(
        {
            "delta": delta,
            "target": target,
            "ratio": target / delta if delta > 1e-14 else None,
            "BL_error_inf": float(np.max(np.abs(B @ L - np.eye(layout.k)))),
            "idempotence_inf": float(np.max(np.abs(P @ P - P))),
            "rowsum_inf": float(np.max(np.abs(P.sum(axis=1) - 1.0))),
            "row_negative_masses": np.maximum(-P, 0.0).sum(axis=1).tolist(),
            "B0": B[0].tolist(),
        }
    )
    return out


def solve_margin_row0_signed_nonnegative(L: np.ndarray, C: float) -> dict[str, Any]:
    eq_rows, eq_rhs, ub_rows, ub_rhs, layout = lp_base(L)
    E = excess_np(L, 0)
    c = np.zeros(layout.total)
    for j in range(layout.n):
        c[layout.b(0, j)] = -E[j]
    c[layout.d] = C
    bounds = [(None, None)] * layout.nb + [(0.0, None)] * layout.nz + [(0.0, None)]
    for j, e in enumerate(E):
        if e > 0:
            bounds[layout.b(0, j)] = (0.0, None)
    res = linprog(
        c,
        A_ub=np.array(ub_rows),
        b_ub=np.array(ub_rhs),
        A_eq=np.array(eq_rows),
        b_eq=np.array(eq_rhs),
        bounds=bounds,
        method="highs",
    )
    out: dict[str, Any] = {"success": bool(res.success), "status": int(res.status), "message": res.message}
    if not res.success:
        return out
    B = res.x[: layout.nb].reshape(layout.k, layout.n)
    P = L @ B
    target = float(np.maximum(B[0], 0.0) @ E)
    delta = float(np.maximum(-P, 0.0).sum(axis=1).max())
    out.update(
        {
            "margin": -float(res.fun),
            "target": target,
            "delta": delta,
            "ratio": target / delta if delta > 1e-14 else None,
            "positive_signed_mass": float(sum(B[0, j] for j, e in enumerate(E) if e > 0)),
            "B0": B[0].tolist(),
        }
    )
    return out


def solve_margin_sign_enum(L: np.ndarray, C: float) -> dict[str, Any]:
    eq_rows, eq_rhs, base_ub, base_rhs, layout = lp_base(L)
    E = excess_np(L, 0)
    bounds = [(None, None)] * layout.nb + [(0.0, None)] * layout.nz + [(0.0, None)]
    best: dict[str, Any] | None = None
    status: dict[int, int] = {}
    for mask in range(1 << layout.n):
        ub_rows = list(base_ub)
        ub_rhs = list(base_rhs)
        pos_cols = []
        for j in range(layout.n):
            row = np.zeros(layout.total)
            if (mask >> j) & 1:
                row[layout.b(0, j)] = -1.0
                pos_cols.append(j)
            else:
                row[layout.b(0, j)] = 1.0
            ub_rows.append(row)
            ub_rhs.append(0.0)
        c = np.zeros(layout.total)
        for j in pos_cols:
            c[layout.b(0, j)] = -E[j]
        c[layout.d] = C
        res = linprog(
            c,
            A_ub=np.array(ub_rows),
            b_ub=np.array(ub_rhs),
            A_eq=np.array(eq_rows),
            b_eq=np.array(eq_rhs),
            bounds=bounds,
            method="highs",
        )
        status[res.status] = status.get(res.status, 0) + 1
        if not res.success:
            continue
        margin = -float(res.fun)
        if best is None or margin > best["margin"] + 1e-10:
            B = res.x[: layout.nb].reshape(layout.k, layout.n)
            P = L @ B
            target = float(sum(max(B[0, j], 0.0) * E[j] for j in range(layout.n)))
            delta = float(np.maximum(-P, 0.0).sum(axis=1).max())
            best = {
                "margin": margin,
                "target": target,
                "delta": delta,
                "ratio": target / delta if delta > 1e-14 else None,
                "mask": int(mask),
                "positive_columns": [int(j) for j in pos_cols],
                "B0": B[0].tolist(),
            }
    return {"patterns": 1 << layout.n, "status_counts": {str(k): v for k, v in sorted(status.items())}, "best": best}


def fixed_b0_for_split(q: int, a: float, m: float, copy_weights: list[float], plus_fraction: float = 0.5) -> np.ndarray:
    signed_mass = float(m)
    plus_total = signed_mass * plus_fraction
    minus_total = signed_mass * (1.0 - plus_fraction)
    D = plus_total - minus_total
    b0 = np.zeros(3 + 2 * q)
    b0[0] = 1.0 - signed_mass
    b0[1] = -a * D
    b0[2] = a * D
    for i, w in enumerate(copy_weights):
        b0[3 + 2 * i] = plus_total * w
        b0[3 + 2 * i + 1] = minus_total * w
    return b0


def audit_A2() -> dict[str, Any]:
    a = 0.01
    C = 1.0 + 4.0 * a * a
    q = 5
    L5 = duplicate_L_np(q, a)
    splits = {
        "symmetric": [1 / q] * q,
        "concentrated_one_copy": [1.0] + [0.0] * (q - 1),
        "skewed_geometric": [0.5, 0.25, 0.125, 0.0625, 0.0625],
    }
    fixed = {}
    for name, weights in splits.items():
        fixed[name] = solve_min_delta_fixed_b0(L5, fixed_b0_for_split(q, a, 0.99, weights, 0.5))
    fixed["unbalanced_plus_70_minus_30"] = solve_min_delta_fixed_b0(
        L5, fixed_b0_for_split(q, a, 0.99, splits["skewed_geometric"], 0.7)
    )
    sign_enum = {}
    for qq in [2, 3, 4]:
        sign_enum[f"q{qq}"] = solve_margin_sign_enum(duplicate_L_np(qq, a), C)
    nonnegative = {}
    for qq in [5, 10, 25]:
        nonnegative[f"q{qq}"] = solve_margin_row0_signed_nonnegative(duplicate_L_np(qq, a), C)
    return {"a": a, "C_single_pair": C, "fixed_B0_asymmetric_splits_q5": fixed, "full_sign_enum_small_q": sign_enum, "signed_nonnegative_large_q": nonnegative}


def path_L_np(k: int, a: float) -> np.ndarray:
    rows = [np.eye(k)[i].copy() for i in range(k)]
    for u, v in zip(range(1, k - 1), range(2, k)):
        plus = np.eye(k)[0].copy()
        plus[u] += a
        plus[v] -= a
        minus = np.eye(k)[0].copy()
        minus[u] -= a
        minus[v] += a
        rows.extend([plus, minus])
    return np.array(rows, dtype=float)


def solve_fixed_mass_B(L: np.ndarray, mass: float) -> tuple[np.ndarray, np.ndarray, float]:
    eq_rows, eq_rhs, ub_rows, ub_rhs, layout = lp_base(L, add_row_sums=False)
    fixed = np.zeros(layout.n)
    fixed[0] = 1.0 - mass
    for j in range(layout.k, layout.n):
        fixed[j] = mass / (layout.n - layout.k)
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
    B = res.x[: layout.nb].reshape(layout.k, layout.n)
    P = L @ B
    delta = float(np.maximum(-P, 0.0).sum(axis=1).max())
    return B, P, delta


def sf_float_for_L_basis(L: np.ndarray, P: np.ndarray, basis: list[int]) -> list[float]:
    C = L[basis, :]
    A = L @ np.linalg.inv(C)
    vals = []
    for s_pos, u in enumerate(basis):
        E = []
        for j in range(L.shape[0]):
            mu = sum(max(-A[j, t], 0.0) for t in range(A.shape[1]) if t != s_pos)
            E.append(max(mu - (1.0 - A[j, s_pos]), 0.0))
        vals.append(float(np.maximum(P[u], 0.0) @ np.array(E)))
    return vals


def audit_A3() -> dict[str, Any]:
    a = 0.01
    ks = [4, 5, 6, 8, 10, 12, 15, 20, 30, 40]
    rows = []
    for k in ks:
        L = path_L_np(k, a)
        _B, P, delta = solve_fixed_mass_B(L, 0.99)
        basis = list(range(1, k)) + [L.shape[0] - 1]
        vals = sf_float_for_L_basis(L, P, basis)
        best = max(vals)
        rows.append({"k": k, "n": int(L.shape[0]), "basis": basis, "delta": delta, "ratio": best / delta, "best_s": int(np.argmax(vals)), "pivot": int(basis[int(np.argmax(vals))])})
    x = np.array([r["k"] for r in rows], dtype=float)
    y = np.array([r["ratio"] for r in rows], dtype=float)
    fits = {}
    for name, X in {
        "free_L_minus_c_over_k": np.column_stack([np.ones_like(x), 1.0 / x]),
        "forced_2_minus_c_over_k": (1.0 / x)[:, None],
        "log_linear": np.column_stack([np.ones_like(x), np.log(x)]),
    }.items():
        if name == "forced_2_minus_c_over_k":
            coef, *_ = np.linalg.lstsq(X, 2.0 - y, rcond=None)
            pred = 2.0 - X @ coef
            params = {"c": float(coef[0])}
        else:
            coef, *_ = np.linalg.lstsq(X, y, rcond=None)
            pred = X @ coef
            params = {f"beta{i}": float(v) for i, v in enumerate(coef)}
        fits[name] = {"params": params, "rmse": float(np.sqrt(np.mean((pred - y) ** 2))), "pred_k100": float((2.0 - np.array([[1 / 100]]) @ np.array([fits["forced_2_minus_c_over_k"]["params"]["c"]]))[0]) if False else None}
    c_forced = fits["forced_2_minus_c_over_k"]["params"]["c"]
    fits["forced_2_minus_c_over_k"]["pred_k100"] = float(2.0 - c_forced / 100.0)
    b0, b1 = fits["log_linear"]["params"]["beta0"], fits["log_linear"]["params"]["beta1"]
    fits["log_linear"]["pred_k100"] = float(b0 + b1 * math.log(100.0))
    Lhat, chat = fits["free_L_minus_c_over_k"]["params"]["beta0"], -fits["free_L_minus_c_over_k"]["params"]["beta1"]
    fits["free_L_minus_c_over_k"]["asymptote_L"] = float(Lhat)
    fits["free_L_minus_c_over_k"]["c"] = float(chat)
    fits["free_L_minus_c_over_k"]["pred_k100"] = float(Lhat - chat / 100.0)
    return {"a": a, "mass": 0.99, "path_pattern_rows": rows, "fits": fits}


def pair_candidate_symbolic() -> dict[str, Any]:
    a = sp.symbols("a", positive=True)
    m = sp.Rational(1)
    L, B, c = transverse_LB(a, m)
    P = sp.simplify(L * B)
    target = a
    delta = c
    return {
        "support": "k=3 signed pair",
        "candidate_c": str(c),
        "BL_minus_I_zero": bool(sp.simplify(B * L - sp.eye(3)) == sp.zeros(3)),
        "P2_minus_P_zero": bool(sp.simplify(P * P - P) == sp.zeros(5)),
        "target": str(target),
        "delta": str(delta),
        "ratio": str(sp.factor(target / delta)),
        "active_row_neg_masses_assuming_0<a<=1/2": ["0", str(c), str(c), str(c), str(c)],
    }


def cycle4_candidate_symbolic() -> dict[str, Any]:
    a = sp.symbols("a", positive=True)
    k = 4
    edges = [(1, 2), (2, 3), (3, 1)]
    rows: list[list[Any]] = [[1 if i == j else 0 for j in range(k)] for i in range(k)]
    for u, v in edges:
        plus = [1, 0, 0, 0]
        minus = [1, 0, 0, 0]
        plus[u] += a
        plus[v] -= a
        minus[u] -= a
        minus[v] += a
        rows.append(plus)
        rows.append(minus)
    L = sp.Matrix(rows)
    delta = sp.factor(a / (1 + 3 * a * a))
    c = sp.factor(delta / 2)
    B = sp.zeros(k, 10)
    for j in range(4, 10):
        B[0, j] = sp.Rational(1, 6)
    for t in [1, 2, 3]:
        B[t, t] = 1 - 4 * a * c
        for u in [1, 2, 3]:
            if u != t:
                B[t, u] = 2 * a * c
        for eidx, (u, v) in enumerate(edges):
            plus_j = 4 + 2 * eidx
            minus_j = plus_j + 1
            inc = 0
            if t == u:
                inc = 1
            elif t == v:
                inc = -1
            B[t, plus_j] = c * inc
            B[t, minus_j] = -c * inc
    P = sp.simplify(L * B)
    return {
        "support": "k=4 cycle/all-pairs on three foreign coordinates",
        "candidate_c_per_incident_signed_column": str(c),
        "BL_minus_I_zero": bool(sp.simplify(B * L - sp.eye(k)) == sp.zeros(k)),
        "P2_minus_P_zero": bool(sp.simplify(P * P - P) == sp.zeros(10)),
        "target": str(a),
        "delta": str(delta),
        "ratio": str(sp.factor(a / delta)),
        "active_row_neg_masses_assuming_0<a<=1/2": ["0"] + [str(delta)] * 9,
    }


def audit_A4() -> dict[str, Any]:
    return {"pair": pair_candidate_symbolic(), "cycle4": cycle4_candidate_symbolic()}


def dense_pair_k7_LB() -> tuple[sp.Matrix, sp.Matrix]:
    k = 7
    a = sp.Rational(1, 4)
    rows: list[list[sp.Rational]] = []
    for i in range(k):
        rows.append([sp.Rational(1 if i == j else 0) for j in range(k)])
    v = [0, 1, 1, 1, -1, -1, -1]
    rows.append([sp.Rational(1 if j == 0 else 0) + a * v[j] for j in range(k)])
    rows.append([sp.Rational(1 if j == 0 else 0) - a * v[j] for j in range(k)])
    L = sp.Matrix(rows)
    B = sp.zeros(k, k + 2)
    B[0, 7] = sp.Rational(1, 2)
    B[0, 8] = sp.Rational(1, 2)
    signs = [0, 1, 1, 1, -1, -1, -1]
    for r in range(1, k):
        sr = signs[r]
        for j in range(1, k):
            if j == r:
                B[r, j] = sp.Rational(31, 34)
            elif signs[j] == sr:
                B[r, j] = sp.Rational(-3, 34)
            else:
                B[r, j] = sp.Rational(3, 34)
        B[r, 7] = sr * sp.Rational(3, 17)
        B[r, 8] = -sr * sp.Rational(3, 17)
    return L, B


def audit_A5_A6() -> dict[str, Any]:
    L, B = dense_pair_k7_LB()
    P = L * B
    best_L, ties_L, all_minors = maxvol_ties_L(L)
    best_P, ties_P = maxvol_ties_P(P)
    delta = max(row_neg_mass([P[i, j] for j in range(P.cols)]) for i in range(P.rows))
    tie_records = []
    for basis in ties_L:
        rows = sf_for_basis(L, B, basis)
        for row in rows:
            row["sf_over_delta"] = fstr(S(row["sf"]) / delta) if delta else "inf"
        tie_records.append({"basis": list(basis), "sf_rows": rows})
    E0 = [excess_coeff([L[i, t] for t in range(L.cols)], 0) for i in range(L.rows)]
    lhs = sum(pos(B[0, j]) * E0[j] for j in range(L.rows))
    maxE = max(E0)
    return {
        "exact": {
            "BL_minus_I_zero": bool(B * L - sp.eye(7) == sp.zeros(7)),
            "P2_minus_P_zero": bool(P * P - P == sp.zeros(9)),
            "row_sums": [fstr(sum(P[i, j] for j in range(P.cols))) for i in range(P.rows)],
            "row_negative_masses": [fstr(row_neg_mass([P[i, j] for j in range(P.cols)])) for i in range(P.rows)],
            "delta": fstr(delta),
            "basis_0_sf": next(r for r in tie_records if r["basis"] == list(range(7)))["sf_rows"][0]["sf"],
            "basis_0_ratio": next(r for r in tie_records if r["basis"] == list(range(7)))["sf_rows"][0]["sf_over_delta"],
            "max_abs_det_L": fstr(best_L),
            "maxvol_ties_L": [list(t) for t in ties_L],
            "maxvol_ties_P": [list(t) for t in ties_P],
            "maxvol_volume_sq_P": fstr(best_P),
            "all_tie_sf": tie_records,
            "nonmax_minor_count": len([m for m in all_minors if m["abs_det"] != fstr(best_L)]),
        },
        "convexity_refutation": {
            "E0_values": [fstr(x) for x in E0],
            "E0_at_e0": fstr(E0[0]),
            "B0": [fstr(B[0, j]) for j in range(B.cols)],
            "B0_negative_mass": fstr(row_neg_mass([B[0, j] for j in range(B.cols)])),
            "P_row0_negative_mass": fstr(row_neg_mass([P[0, j] for j in range(P.cols)])),
            "lhs_sum_B0pos_E0": fstr(lhs),
            "max_E0": fstr(maxE),
            "global_delta_times_max_E0": fstr(delta * maxE),
        },
    }


def main() -> None:
    records = {
        "A1_transverse_pair": audit_A1(),
        "A2_duplicate_asymmetry": audit_A2(),
        "A3_path_tie_growth": audit_A3(),
        "A4_fixed_support_formulas": audit_A4(),
        "A5_A6_dense_pair_and_convexity": audit_A5_A6(),
    }
    Path("audit_compute.json").write_text(json.dumps(records, indent=2, sort_keys=True))
    lines = []
    a1 = records["A1_transverse_pair"]["sample"]
    lines.append(f"A1 sample delta={a1['delta']} intended_ratio={a1['intended_ratio']} ties={a1['maxvol_ties_L']}")
    a2 = records["A2_duplicate_asymmetry"]
    lines.append("A2 fixed q=5 splits:")
    for name, rec in a2["fixed_B0_asymmetric_splits_q5"].items():
        lines.append(f"  {name}: delta={rec.get('delta')} target={rec.get('target')} ratio={rec.get('ratio')}")
    lines.append("A2 sign-enum margins:")
    for name, rec in a2["full_sign_enum_small_q"].items():
        best = rec["best"]
        lines.append(f"  {name}: patterns={rec['patterns']} margin={best['margin']} ratio={best['ratio']}")
    a3 = records["A3_path_tie_growth"]
    lines.append("A3 path ratios:")
    for row in a3["path_pattern_rows"]:
        lines.append(f"  k={row['k']} ratio={row['ratio']:.10f} delta={row['delta']:.10g}")
    lines.append(f"A3 fits={json.dumps(a3['fits'], sort_keys=True)}")
    a4 = records["A4_fixed_support_formulas"]
    lines.append(f"A4 pair ratio={a4['pair']['ratio']} cycle4 ratio={a4['cycle4']['ratio']}")
    a5 = records["A5_A6_dense_pair_and_convexity"]["exact"]
    lines.append(f"A5 delta={a5['delta']} basis0_ratio={a5['basis_0_ratio']} ties={a5['maxvol_ties_L']}")
    a6 = records["A5_A6_dense_pair_and_convexity"]["convexity_refutation"]
    lines.append(f"A6 lhs={a6['lhs_sum_B0pos_E0']} row0_nu={a6['P_row0_negative_mass']} delta_maxE={a6['global_delta_times_max_E0']}")
    Path("audit_compute_summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
