#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path

import sympy as sp

import verify_reduction as V


def det_abs(L: sp.Matrix, basis: tuple[int, ...]) -> sp.Expr:
    return abs(sp.factor(L[list(basis), :].det()))


def single_swaps(name: str, L: sp.Matrix, B: sp.Matrix) -> dict[str, object]:
    P = sp.simplify(L * B)
    delta = V.max_row_neg_mass(P)
    maxvol, rows = V.select_chart(P, L, sp.Rational(1, 2))
    star = rows[0]
    star_basis = tuple(star["basis"])
    nonbasis = [i for i in range(L.rows) if i not in star_basis]
    swaps = []
    for pos in range(len(star_basis)):
        for row in nonbasis:
            cand = list(star_basis)
            old = cand[pos]
            cand[pos] = row
            if len(set(cand)) < len(cand):
                continue
            cand_t = tuple(cand)
            vol = det_abs(L, cand_t)
            if vol == 0 or vol < sp.Rational(1, 2) * maxvol:
                continue
            rec = V.chart_values(P, L, cand_t)
            swaps.append(
                {
                    "replace_pos": pos,
                    "old": old,
                    "new": row,
                    "basis": rec["basis"],
                    "phi": rec["phi"],
                    "phi_over_delta": V.fstr(sp.Rational(rec["phi"]) / delta),
                    "volume": V.fstr(vol),
                }
            )
    swaps.sort(key=lambda r: (Fraction(r["phi_over_delta"]), tuple(r["basis"])))
    return {
        "name": name,
        "delta": V.fstr(delta),
        "theta_maxvol": V.fstr(maxvol),
        "star_basis": list(star_basis),
        "star_phi_over_delta": V.fstr(sp.Rational(star["phi"]) / delta),
        "single_swap_count": len(swaps),
        "best_single_swap": swaps[0] if swaps else None,
        "all_best_single_swaps": [r for r in swaps if swaps and r["phi_over_delta"] == swaps[0]["phi_over_delta"]],
    }


def main() -> None:
    cases = [
        ("staircase_m3",) + V.staircase(3),
        ("perturbed_staircase_m5_eps1e-3",) + V.perturbed_staircase(5, sp.Rational(1, 1000)),
    ]
    data = [single_swaps(name, L, B) for name, L, B in cases]
    Path("single_swap_check.json").write_text(json.dumps(data, indent=2, sort_keys=True))
    lines = []
    for rec in data:
        best = rec["best_single_swap"]
        lines.append(
            f"{rec['name']}: star={rec['star_basis']} star_ratio={rec['star_phi_over_delta']} "
            f"swaps={rec['single_swap_count']} best_swap_ratio={best['phi_over_delta'] if best else 'none'} "
            f"best_swap={best['basis'] if best else 'none'}"
        )
    Path("single_swap_check.out").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
