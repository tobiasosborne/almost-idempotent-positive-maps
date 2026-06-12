#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from fractions import Fraction
from pathlib import Path


def load_module(name: str, path: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def halfcex_cap_quarter() -> list[dict[str, object]]:
    h = load_module("h", "w34_halfcex_audit.py")
    cap = Fraction(1, 4)
    rows = []
    for m in range(2, 13):
        a = h.max_feasible_amplitude(m, cap)
        if a is None:
            continue
        c = h.feasible_c_for_cap(m, a, cap)
        rec = h.audit_instance(
            f"cap1_4_m{m}",
            m,
            h.rat(a),
            h.rat(cap),
            c=h.rat(c),
            keep_tie_details=False,
        )
        rows.append(
            {
                "m": m,
                "a": rec["a"],
                "delta": rec["verification"]["delta"],
                "selected_min_ratio": rec["tie_worst_ratio"],
                "max_tie_ratio": rec["tie_best_ratio"],
            }
        )
    return rows


def path_no_center_float_scan() -> list[dict[str, object]]:
    import numpy as np
    from scipy.optimize import linprog

    ac = load_module("ac", "w34_audit_compute.py")

    def path_no_center_l(k: int, a: float) -> np.ndarray:
        rows = [np.eye(k)[i].copy() for i in range(1, k)]
        for u, v in zip(range(1, k - 1), range(2, k)):
            plus = np.eye(k)[0].copy()
            plus[u] += a
            plus[v] -= a
            minus = np.eye(k)[0].copy()
            minus[u] -= a
            minus[v] += a
            rows.extend([plus, minus])
        return np.array(rows, dtype=float)

    def solve(k: int) -> tuple[np.ndarray, np.ndarray, float]:
        l_mat = path_no_center_l(k, 0.01)
        eq_rows, eq_rhs, ub_rows, ub_rhs, layout = ac.lp_base(l_mat, add_row_sums=False)
        fixed = np.zeros(layout.n)
        signed_start = k - 1
        for j in range(signed_start, layout.n):
            fixed[j] = 1.0 / (2 * (k - 2))
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
        b_mat = res.x[: layout.nb].reshape(layout.k, layout.n)
        p_mat = l_mat @ b_mat
        delta = float(np.maximum(-p_mat, 0.0).sum(axis=1).max())
        return l_mat, p_mat, delta

    def sf(l_mat: np.ndarray, p_mat: np.ndarray, basis: list[int]) -> list[float]:
        coords = l_mat @ np.linalg.inv(l_mat[basis, :])
        out = []
        for s, u in enumerate(basis):
            e_vals = []
            for row in coords:
                mu = sum(max(-row[t], 0.0) for t in range(coords.shape[1]) if t != s)
                e_vals.append(max(mu - (1.0 - row[s]), 0.0))
            out.append(float(np.maximum(p_mat[u], 0.0) @ np.array(e_vals)))
        return out

    rows = []
    for k in [6, 8, 10, 12, 20, 40]:
        l_mat, p_mat, delta = solve(k)
        chart_ratios = []
        for j in range(k - 1, l_mat.shape[0]):
            basis = list(range(k - 1)) + [j]
            chart_ratios.append(max(sf(l_mat, p_mat, basis)) / delta)
        rows.append(
            {
                "k": k,
                "m_edges": k - 2,
                "delta_float": delta,
                "selected_ratio_float": min(chart_ratios),
                "worst_tie_ratio_float": max(chart_ratios),
            }
        )
    return rows


def main() -> None:
    data = {
        "halfcex_cap_1_4": halfcex_cap_quarter(),
        "path_no_center_float_scan": path_no_center_float_scan(),
    }
    Path("selected_family_scan.json").write_text(json.dumps(data, indent=2, sort_keys=True))
    lines = ["halfcex cap=1/4:"]
    for row in data["halfcex_cap_1_4"]:
        lines.append(
            f"  m={row['m']} a={row['a']} delta={row['delta']} "
            f"selected={row['selected_min_ratio']} max_tie={row['max_tie_ratio']}"
        )
    lines.append("path no-center a=1/100 float scan:")
    for row in data["path_no_center_float_scan"]:
        lines.append(
            f"  k={row['k']} edges={row['m_edges']} "
            f"delta={row['delta_float']:.10g} "
            f"selected={row['selected_ratio_float']:.10f} "
            f"worst={row['worst_tie_ratio_float']:.10f}"
        )
    Path("selected_family_scan_summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
