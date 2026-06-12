#!/usr/bin/env python3
from __future__ import annotations

import numpy as np

from audit_compute import solve_margin_sign_enum


def pair_support(a: float) -> np.ndarray:
    rows = [np.eye(3)[i] for i in range(3)]
    rows.append(np.array([1.0, a, -a]))
    rows.append(np.array([1.0, -a, a]))
    return np.array(rows)


def cycle4_support(a: float) -> np.ndarray:
    rows = [np.eye(4)[i] for i in range(4)]
    for u, v in [(1, 2), (2, 3), (3, 1)]:
        plus = np.eye(4)[0].copy()
        minus = np.eye(4)[0].copy()
        plus[u] += a
        plus[v] -= a
        minus[u] -= a
        minus[v] += a
        rows.extend([plus, minus])
    return np.array(rows)


for name, maker, formula in [
    ("pair", pair_support, lambda a: 1 + 4 * a * a),
    ("cycle4", cycle4_support, lambda a: 1 + 3 * a * a),
]:
    for a in [0.2, 0.5]:
        C = formula(a)
        rec = solve_margin_sign_enum(maker(a), C)
        best = rec["best"]
        rec_low = solve_margin_sign_enum(maker(a), C - 1e-4)
        best_low = rec_low["best"]
        print(
            name,
            "a",
            a,
            "C",
            C,
            "patterns",
            rec["patterns"],
            "margin_at_C",
            best["margin"],
            "ratio_at_C",
            best["ratio"],
            "margin_C_minus_1e-4",
            best_low["margin"],
            "ratio_low",
            best_low["ratio"],
        )
