#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


OUT = Path(".")
TOL = 1e-9


def max_abs_minor(L: np.ndarray, k: int) -> tuple[float, tuple[int, ...] | None]:
    best = 0.0
    arg = None
    for inds in itertools.combinations(range(len(L)), k):
        val = abs(float(np.linalg.det(L[list(inds)])))
        if val > best + 1e-12:
            best = val
            arg = inds
    return best, arg


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


def cycle_support(k: int, a: float) -> np.ndarray:
    rows = [np.eye(k)[i] for i in range(k)]
    foreign = list(range(1, k))
    if len(foreign) == 1:
        return np.array(rows, dtype=float)
    if len(foreign) == 2:
        pairs = [(foreign[0], foreign[1])]
    else:
        pairs = list(zip(foreign, foreign[1:] + foreign[:1]))
    for t, r in pairs:
        xp = np.eye(k)[0].copy()
        xm = np.eye(k)[0].copy()
        xp[t] += a
        xp[r] -= a
        xm[t] -= a
        xm[r] += a
        rows.extend([xp, xm])
    return np.array(rows, dtype=float)


def excess_values(L: np.ndarray, s: int) -> np.ndarray:
    vals = []
    for x in L:
        foreign = np.delete(x, s)
        mu = float(np.maximum(-foreign, 0.0).sum())
        lam = float(1.0 - x[s])
        vals.append(max(mu - lam, 0.0))
    return np.array(vals)


def relaxed_signed_pair_record(k: int, a: float) -> dict:
    L = signed_pair_support(k, a)
    E = excess_values(L, 0)
    q = np.zeros(len(L))
    q[k] = 0.5
    q[k + 1] = 0.5
    bary = q @ L
    minor, arg = max_abs_minor(L, k)
    return {
        "kind": "coefficient_only_relaxation",
        "k": k,
        "a": a,
        "n": int(len(L)),
        "max_abs_minor": minor,
        "max_minor_rows": list(arg) if arg is not None else None,
        "row_negative_mass_of_test_weight": float(np.maximum(-q, 0.0).sum()),
        "barycenter_error_inf": float(np.max(np.abs(bary - np.eye(k)[0]))),
        "signed_face_excess": float(q @ E),
        "realizable_comment": "violates the target at delta=0 if only the representative signed measure is kept; full row near-positivity is intentionally absent",
    }


def solve_support_margin(L: np.ndarray, s: int, C: float) -> dict:
    """Maximize target_s(B)-C*delta for fixed coefficient rows L.

    The LP includes BL=I and all row negative-mass constraints for P=L B.
    Positive parts of the selected basis row B_s are handled by enumerating
    every sign pattern of that row.
    """

    k = L.shape[1]
    n = L.shape[0]
    E = excess_values(L, s)
    nb = k * n
    nz = n * n
    didx = nb + nz
    total = didx + 1

    def bidx(r: int, j: int) -> int:
        return r * n + j

    def zidx(i: int, j: int) -> int:
        return nb + i * n + j

    eq_rows = []
    eq_rhs = []
    for r in range(k):
        for t in range(k):
            row = np.zeros(total)
            for j in range(n):
                row[bidx(r, j)] = L[j, t]
            eq_rows.append(row)
            eq_rhs.append(1.0 if r == t else 0.0)
    A_eq = np.array(eq_rows)
    b_eq = np.array(eq_rhs)

    base_ub = []
    base_rhs = []
    for i in range(n):
        for j in range(n):
            row = np.zeros(total)
            # z_ij >= -(L_i B)_j
            row[zidx(i, j)] = -1.0
            for r in range(k):
                row[bidx(r, j)] -= L[i, r]
            base_ub.append(row)
            base_rhs.append(0.0)
    for i in range(n):
        row = np.zeros(total)
        for j in range(n):
            row[zidx(i, j)] = 1.0
        row[didx] = -1.0
        base_ub.append(row)
        base_rhs.append(0.0)

    bounds = [(None, None)] * nb + [(0.0, None)] * nz + [(0.0, None)]

    best = None
    unbounded = 0
    infeasible = 0
    patterns = 0
    for mask in range(1 << n):
        patterns += 1
        ub_rows = list(base_ub)
        ub_rhs = list(base_rhs)
        pos = []
        for j in range(n):
            row = np.zeros(total)
            if (mask >> j) & 1:
                # B_sj >= 0, encoded as -B_sj <= 0.
                row[bidx(s, j)] = -1.0
                pos.append(j)
            else:
                # B_sj <= 0.
                row[bidx(s, j)] = 1.0
            ub_rows.append(row)
            ub_rhs.append(0.0)

        c = np.zeros(total)
        for j in pos:
            c[bidx(s, j)] -= E[j]
        c[didx] = C
        res = linprog(
            c,
            A_ub=np.array(ub_rows),
            b_ub=np.array(ub_rhs),
            A_eq=A_eq,
            b_eq=b_eq,
            bounds=bounds,
            method="highs",
        )
        if res.status == 3:
            unbounded += 1
            continue
        if not res.success:
            infeasible += 1
            continue
        margin = -float(res.fun)
        if best is None or margin > best["margin"]:
            B = res.x[:nb].reshape(k, n)
            P = L @ B
            target = float(sum(max(B[s, j], 0.0) * E[j] for j in range(n)))
            delta = float(np.maximum(-P, 0.0).sum(axis=1).max())
            best = {
                "margin": margin,
                "target": target,
                "delta": delta,
                "ratio": None if delta <= 1e-12 else target / delta,
                "mask": mask,
                "positive_columns": pos,
                "idempotence_inf": float(np.max(np.abs(P @ P - P))),
                "BL_error_inf": float(np.max(np.abs(B @ L - np.eye(k)))),
                "rowsum_inf": float(np.max(np.abs(P.sum(axis=1) - 1.0))),
                "min_entry": float(P.min()),
                "max_row_negative_mass": delta,
            }

    if best is None:
        best = {"margin": None, "target": None, "delta": None, "ratio": None}
    return {
        "C": C,
        "patterns": patterns,
        "unbounded_patterns": unbounded,
        "infeasible_patterns": infeasible,
        "best": best,
    }


def support_constant_upper(L: np.ndarray, s: int, lo: float = 0.0, hi: float = 8.0) -> dict:
    while True:
        rec = solve_support_margin(L, s, hi)
        if rec["unbounded_patterns"] == 0 and rec["best"]["margin"] is not None and rec["best"]["margin"] <= 2e-8:
            break
        hi *= 2.0
        if hi > 512:
            return {"status": "failed_to_bracket", "hi": hi, "last": rec}
    last = rec
    for _ in range(32):
        mid = 0.5 * (lo + hi)
        rec = solve_support_margin(L, s, mid)
        if rec["unbounded_patterns"] == 0 and rec["best"]["margin"] is not None and rec["best"]["margin"] <= 2e-8:
            hi = mid
            last = rec
        else:
            lo = mid
    return {"status": "bracketed", "upper_C": hi, "last_nonpositive": last}


def summarize(records: list[dict]) -> str:
    lines = []
    for rec in records:
        if rec["kind"] == "coefficient_only_relaxation":
            lines.append(
                f"RELAX k={rec['k']} a={rec['a']}: delta={rec['row_negative_mass_of_test_weight']:.6g} "
                f"bary_err={rec['barycenter_error_inf']:.3g} excess={rec['signed_face_excess']:.6g} "
                f"max_minor={rec['max_abs_minor']:.6g}"
            )
            continue
        c2 = rec["C2"]["best"]
        upper = rec["upper"]
        upper_txt = upper.get("upper_C", upper.get("hi"))
        lines.append(
            f"FULL {rec['name']}: k={rec['k']} n={rec['n']} a={rec['a']} "
            f"max_minor={rec['max_abs_minor']:.6g} "
            f"C2_margin={c2['margin']:.3g} C2_target={c2['target']:.6g} "
            f"C2_delta={c2['delta']:.6g} C2_ratio={c2['ratio'] if c2['ratio'] is not None else 'na'} "
            f"cert_upper_C~{upper_txt:.6g}"
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    records: list[dict] = []
    records.append(relaxed_signed_pair_record(3, 0.5))
    records.append(relaxed_signed_pair_record(4, 0.5))

    cases = []
    for a in [0.05, 0.2, 0.5]:
        cases.append((f"pair_k3_a_{a:g}", signed_pair_support(3, a), a))
    for a in [0.05, 0.2, 0.35]:
        cases.append((f"cycle_k4_a_{a:g}", cycle_support(4, a), a))

    for name, L, a in cases:
        k = L.shape[1]
        minor, arg = max_abs_minor(L, k)
        if minor > 1.0 + 1e-9:
            records.append(
                {
                    "kind": "full_support_skipped",
                    "name": name,
                    "k": k,
                    "n": int(len(L)),
                    "a": a,
                    "max_abs_minor": minor,
                    "reason": "support violates max-volume minor bound",
                }
            )
            continue
        c2 = solve_support_margin(L, 0, 2.0)
        upper = support_constant_upper(L, 0)
        records.append(
            {
                "kind": "full_support_lp",
                "name": name,
                "k": k,
                "n": int(len(L)),
                "a": a,
                "max_abs_minor": minor,
                "max_minor_rows": list(arg) if arg is not None else None,
                "C2": c2,
                "upper": upper,
            }
        )

    (OUT / "lp_excess_audit_results.json").write_text(json.dumps(records, indent=2, sort_keys=True))
    summary = summarize([r for r in records if r["kind"] != "full_support_skipped"])
    skipped = [
        f"SKIP {r['name']}: max_minor={r['max_abs_minor']:.6g} {r['reason']}"
        for r in records
        if r["kind"] == "full_support_skipped"
    ]
    if skipped:
        summary += "".join(line + "\n" for line in skipped)
    (OUT / "lp_excess_audit_summary.txt").write_text(summary)
    print(summary, end="")


if __name__ == "__main__":
    main()
