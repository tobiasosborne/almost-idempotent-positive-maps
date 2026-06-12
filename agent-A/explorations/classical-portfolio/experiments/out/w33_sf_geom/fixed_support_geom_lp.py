#!/usr/bin/env python3
from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
from scipy.optimize import linprog


TOL = 1e-9


def excess_values(L: np.ndarray, s: int) -> np.ndarray:
    vals = []
    for x in L:
        mu = float(np.maximum(-np.delete(x, s), 0.0).sum())
        lam = float(1.0 - x[s])
        vals.append(max(mu - lam, 0.0))
    return np.array(vals)


def signed_pair_support(k: int, a: float, s: int = 0, t: int = 1, r: int = 2) -> np.ndarray:
    rows = [np.eye(k)[i] for i in range(k)]
    xp = np.eye(k)[s].copy()
    xm = np.eye(k)[s].copy()
    xp[t] += a
    xp[r] -= a
    xm[t] -= a
    xm[r] += a
    rows.extend([xp, xm])
    return np.array(rows, dtype=float)


def all_transverse_pairs(k: int, a: float, s: int = 0) -> np.ndarray:
    rows = [np.eye(k)[i] for i in range(k)]
    for t in range(k):
        for r in range(t + 1, k):
            if s in (t, r):
                continue
            xp = np.eye(k)[s].copy()
            xm = np.eye(k)[s].copy()
            xp[t] += a
            xp[r] -= a
            xm[t] -= a
            xm[r] += a
            rows.extend([xp, xm])
    return unique_rows(np.array(rows, dtype=float))


def cycle_support(k: int, a: float, s: int = 0) -> np.ndarray:
    rows = [np.eye(k)[i] for i in range(k)]
    foreign = [t for t in range(k) if t != s]
    if len(foreign) < 2:
        return np.array(rows, dtype=float)
    pairs = list(zip(foreign, foreign[1:] + foreign[:1]))
    for t, r in pairs:
        xp = np.eye(k)[s].copy()
        xm = np.eye(k)[s].copy()
        xp[t] += a
        xp[r] -= a
        xm[t] -= a
        xm[r] += a
        rows.extend([xp, xm])
    return unique_rows(np.array(rows, dtype=float))


def simplex_signed_grid(k: int, step: float, s: int = 0, cap: float = 1.0) -> np.ndarray:
    """Small deterministic chart grid with sum 1 and coordinates in [-cap, cap]."""
    vals = np.arange(-cap, cap + 0.5 * step, step)
    rows = [np.eye(k)[i] for i in range(k)]
    for coords in itertools.product(vals, repeat=k - 1):
        x = np.zeros(k)
        idx = 0
        for t in range(k):
            if t == s:
                continue
            x[t] = coords[idx]
            idx += 1
        x[s] = 1.0 - float(np.sum(x))
        if np.all(x <= cap + 1e-10) and np.all(x >= -cap - 1e-10):
            rows.append(x)
    return unique_rows(np.array(rows, dtype=float))


def unique_rows(L: np.ndarray) -> np.ndarray:
    seen = set()
    rows = []
    for row in L:
        key = tuple(np.round(row, 12))
        if key not in seen:
            seen.add(key)
            rows.append(row)
    return np.array(rows, dtype=float)


def max_abs_minor(L: np.ndarray, k: int) -> tuple[float, tuple[int, ...] | None]:
    best = 0.0
    arg = None
    for inds in itertools.combinations(range(len(L)), k):
        val = abs(float(np.linalg.det(L[list(inds)])))
        if val > best + 1e-10:
            best = val
            arg = inds
    return best, arg


@dataclass
class LPLayout:
    k: int
    n: int
    nb: int
    nz: int
    didx: int
    total: int

    def bidx(self, r: int, j: int) -> int:
        return r * self.n + j

    def zidx(self, i: int, j: int) -> int:
        return self.nb + i * self.n + j


def solve_support_margin(
    L: np.ndarray,
    s: int,
    C: float,
    keep_solution: bool = False,
    delta_cap: float | None = None,
) -> dict[str, Any]:
    """Maximize target_s(B)-C*delta for a fixed coefficient support L.

    The variables are the representative rows B, full-row negative epigraphs for
    P=L B, and delta.  The constraints BL=I and row negative mass <= delta make
    P exactly idempotent through the H-M converse parametrization.
    """

    k = L.shape[1]
    n = L.shape[0]
    E = excess_values(L, s)
    layout = LPLayout(k=k, n=n, nb=k * n, nz=n * n, didx=k * n + n * n, total=k * n + n * n + 1)

    eq_rows = []
    eq_rhs = []
    for r in range(k):
        # representative rows are stochastic
        row = np.zeros(layout.total)
        for j in range(n):
            row[layout.bidx(r, j)] = 1.0
        eq_rows.append(row)
        eq_rhs.append(1.0)
        # exact left inverse BL=I
        for t in range(k):
            row = np.zeros(layout.total)
            for j in range(n):
                row[layout.bidx(r, j)] = L[j, t]
            eq_rows.append(row)
            eq_rhs.append(1.0 if r == t else 0.0)

    A_eq = np.array(eq_rows)
    b_eq = np.array(eq_rhs)

    base_ub = []
    base_rhs = []
    for i in range(n):
        for j in range(n):
            row = np.zeros(layout.total)
            row[layout.zidx(i, j)] = -1.0
            for r in range(k):
                row[layout.bidx(r, j)] -= L[i, r]
            base_ub.append(row)
            base_rhs.append(0.0)
    for i in range(n):
        row = np.zeros(layout.total)
        for j in range(n):
            row[layout.zidx(i, j)] = 1.0
        row[layout.didx] = -1.0
        base_ub.append(row)
        base_rhs.append(0.0)

    delta_bound = (0.0, None if delta_cap is None else float(delta_cap))
    bounds = [(None, None)] * layout.nb + [(0.0, None)] * layout.nz + [delta_bound]

    best: dict[str, Any] | None = None
    status_counts: dict[int, int] = {}
    for mask in range(1 << n):
        ub_rows = list(base_ub)
        ub_rhs = list(base_rhs)
        pos = []
        for j in range(n):
            row = np.zeros(layout.total)
            if (mask >> j) & 1:
                row[layout.bidx(s, j)] = -1.0
                pos.append(j)
            else:
                row[layout.bidx(s, j)] = 1.0
            ub_rows.append(row)
            ub_rhs.append(0.0)

        c = np.zeros(layout.total)
        for j in pos:
            c[layout.bidx(s, j)] -= E[j]
        c[layout.didx] = C

        res = linprog(
            c,
            A_ub=np.array(ub_rows),
            b_ub=np.array(ub_rhs),
            A_eq=A_eq,
            b_eq=b_eq,
            bounds=bounds,
            method="highs",
        )
        status_counts[res.status] = status_counts.get(res.status, 0) + 1
        if not res.success:
            continue
        margin = -float(res.fun)
        if best is None or margin > best["margin"] + 1e-11:
            B = res.x[: layout.nb].reshape(k, n)
            P = L @ B
            target = float(sum(max(B[s, j], 0.0) * E[j] for j in range(n)))
            delta = float(np.maximum(-P, 0.0).sum(axis=1).max())
            best = {
                "margin": margin,
                "target": target,
                "delta": delta,
                "ratio": None if delta <= 1e-11 else target / delta,
                "mask": int(mask),
                "positive_columns": [int(j) for j in pos],
                "idempotence_inf": float(np.max(np.abs(P @ P - P))),
                "BL_error_inf": float(np.max(np.abs(B @ L - np.eye(k)))),
                "rowsum_inf": float(np.max(np.abs(P.sum(axis=1) - 1.0))),
                "min_entry": float(P.min()),
                "max_row_negative_mass": delta,
            }
            if keep_solution:
                best["B"] = B.tolist()
                best["P"] = P.tolist()
                best["E"] = E.tolist()
                best["row_negative_masses"] = np.maximum(-P, 0.0).sum(axis=1).tolist()

    return {
        "C": C,
        "patterns": 1 << n,
        "status_counts": {str(k): v for k, v in status_counts.items()},
        "best": best if best is not None else {"margin": None},
    }


def support_constant_upper(L: np.ndarray, s: int, hi0: float = 1.0) -> dict[str, Any]:
    lo = 0.0
    hi = hi0
    last = None
    while True:
        rec = solve_support_margin(L, s, hi)
        last = rec
        best = rec["best"]
        if best.get("margin") is not None and best["margin"] <= 1e-8:
            break
        hi *= 2.0
        if hi > 1024:
            return {"status": "failed_to_bracket", "hi": hi, "last": last}

    for _ in range(45):
        mid = 0.5 * (lo + hi)
        rec = solve_support_margin(L, s, mid)
        best = rec["best"]
        if best.get("margin") is not None and best["margin"] <= 1e-8:
            hi = mid
            last = rec
        else:
            lo = mid
    final = solve_support_margin(L, s, hi, keep_solution=True)
    return {"status": "bracketed", "upper_C": hi, "last_nonpositive": final}


def make_cases(args: argparse.Namespace) -> list[tuple[str, np.ndarray]]:
    cases: list[tuple[str, np.ndarray]] = []
    for k in args.ks:
        for a in args.amplitudes:
            if k >= 3:
                cases.append((f"pair_k{k}_a{a:g}", signed_pair_support(k, a)))
                cases.append((f"cycle_k{k}_a{a:g}", cycle_support(k, a)))
                cases.append((f"allpairs_k{k}_a{a:g}", all_transverse_pairs(k, a)))
        if args.grid_step > 0 and k <= 4:
            cases.append((f"grid_k{k}_h{args.grid_step:g}", simplex_signed_grid(k, args.grid_step)))
    return cases


def summarize(records: list[dict[str, Any]]) -> str:
    lines = []
    for rec in records:
        if rec["kind"] == "skipped":
            lines.append(f"SKIP {rec['name']}: n={rec['n']} max_minor={rec['max_abs_minor']:.6g} {rec['reason']}")
            continue
        upper = rec["upper"].get("upper_C")
        best = rec["upper"].get("last_nonpositive", {}).get("best", {})
        lines.append(
            f"FULL-GEOM {rec['name']}: k={rec['k']} n={rec['n']} "
            f"max_minor={rec['max_abs_minor']:.6g} upper_C={upper:.8g} "
            f"target={best.get('target')} delta={best.get('delta')} ratio={best.get('ratio')} "
            f"idemp={best.get('idempotence_inf')} BL={best.get('BL_error_inf')}"
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ks", type=int, nargs="+", default=[3, 4])
    parser.add_argument("--amplitudes", type=float, nargs="+", default=[0.05, 0.1, 0.2, 0.35, 0.5])
    parser.add_argument("--grid-step", type=float, default=0.0)
    parser.add_argument("--max-n", type=int, default=12)
    parser.add_argument("--out-json", default="fixed_support_geom_lp_results.json")
    parser.add_argument("--out-summary", default="fixed_support_geom_lp_summary.txt")
    args = parser.parse_args()

    records: list[dict[str, Any]] = []
    for name, L in make_cases(args):
        k = L.shape[1]
        n = L.shape[0]
        minor, arg = max_abs_minor(L, k)
        if n > args.max_n:
            records.append(
                {
                    "kind": "skipped",
                    "name": name,
                    "k": k,
                    "n": n,
                    "max_abs_minor": minor,
                    "reason": f"support too large for sign enumeration max_n={args.max_n}",
                }
            )
            continue
        if minor > 1.0 + 1e-8:
            records.append(
                {
                    "kind": "skipped",
                    "name": name,
                    "k": k,
                    "n": n,
                    "max_abs_minor": minor,
                    "reason": "violates max-volume determinant bound",
                }
            )
            continue
        upper = support_constant_upper(L, 0)
        records.append(
            {
                "kind": "fixed_support_full_geometry_lp",
                "name": name,
                "k": k,
                "n": n,
                "L": L.tolist(),
                "max_abs_minor": minor,
                "max_minor_rows": list(arg) if arg is not None else None,
                "upper": upper,
            }
        )

    Path(args.out_json).write_text(json.dumps(records, indent=2, sort_keys=True))
    summary = summarize(records)
    Path(args.out_summary).write_text(summary)
    print(summary, end="")


if __name__ == "__main__":
    main()
