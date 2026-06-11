#!/usr/bin/env python3
"""Reduced thin-chain LP/SOS obstruction search.

This script tests the scalar polynomial model written in formalization.md.
It does not claim to solve the full signed-idempotent matrix problem; the
point is to show that the scalar inequalities extracted from w13 alone are
too weak for a path-product floor.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


@dataclass(frozen=True)
class Witness:
    L: int
    c: Fraction
    C: Fraction
    N: int

    @property
    def tau(self) -> Fraction:
        return Fraction(1, self.N)

    @property
    def delta(self) -> Fraction:
        return Fraction(1, self.N * self.N)

    @property
    def sigma(self) -> Fraction:
        return Fraction(2, self.N)

    @property
    def edge(self) -> Fraction:
        return Fraction(1, self.N)

    @property
    def gap(self) -> Fraction:
        return Fraction(1, self.N)

    @property
    def pi(self) -> Fraction:
        return self.edge ** self.L

    @property
    def floor_poly(self) -> Fraction:
        return self.pi + self.C * self.L * self.delta - self.c * self.tau


def choose_N(L: int, c: Fraction, C: Fraction, min_n: int = 100) -> int:
    """Choose N so N^(1-L) + C L/N - c < 0."""
    if c <= 0 or C < 0:
        raise ValueError("expected c > 0 and C >= 0")
    n = max(4, min_n)
    while True:
        lhs = Fraction(1, n ** (L - 1)) + C * L * Fraction(1, n)
        if lhs < c:
            return n
        n += 1


def exact_checks(w: Witness) -> dict:
    tau, delta, sigma, a, d = w.tau, w.delta, w.sigma, w.edge, w.gap
    checks = {
        "delta_equals_tau_squared": delta == tau * tau,
        "tau_in_box": Fraction(0) <= tau <= Fraction(1, 4),
        "sigma_gt_tau": sigma > tau,
        "sigma_le_1_plus_delta": sigma <= 1 + delta,
        "edge_in_box": Fraction(0) <= a <= 1,
        "gap_in_box": Fraction(0) <= d <= tau,
        "link_budget_tight": a * d == delta,
        "floor_violated": w.floor_poly < 0,
    }
    return checks


def frac_str(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def linearized_lp(w: Witness) -> dict:
    """Minimize the first-order model of F around the exact thin ray.

    Variables:
      dtau, ddelta, dsigma, da_1..da_L, dd_1..dd_L
    Bounds are a small trust box. Constraints are the linearizations of
    delta=tau^2, sigma>=tau, and a_i d_i<=delta.
    """
    L = w.L
    tau = float(w.tau)
    delta = float(w.delta)
    sigma = float(w.sigma)
    a = float(w.edge)
    d = float(w.gap)
    c = float(w.c)
    C = float(w.C)
    nvar = 3 + 2 * L
    idx_tau, idx_delta, idx_sigma = 0, 1, 2
    idx_a = 3
    idx_d = 3 + L

    # F = prod(a_i) + C L delta - c tau.
    pi = a ** L
    grad = np.zeros(nvar)
    grad[idx_tau] = -c
    grad[idx_delta] = C * L
    for i in range(L):
        grad[idx_a + i] = pi / a
    f0 = pi + C * L * delta - c * tau

    A_eq = np.zeros((1, nvar))
    A_eq[0, idx_delta] = 1.0
    A_eq[0, idx_tau] = -2.0 * tau
    b_eq = np.array([0.0])

    A_ub = []
    b_ub = []

    # Linearized sigma - tau >= 0 -> dtau - dsigma <= sigma - tau.
    row = np.zeros(nvar)
    row[idx_tau] = 1.0
    row[idx_sigma] = -1.0
    A_ub.append(row)
    b_ub.append(sigma - tau)

    # Linearized a_i d_i - delta <= 0.
    for i in range(L):
        row = np.zeros(nvar)
        row[idx_a + i] = d
        row[idx_d + i] = a
        row[idx_delta] = -1.0
        A_ub.append(row)
        b_ub.append(delta - a * d)

    # Trust box small enough to stay in the same local branch.
    radius = tau / 4.0
    bounds = [(-radius, radius)] * nvar
    result = linprog(
        grad,
        A_ub=np.array(A_ub),
        b_ub=np.array(b_ub),
        A_eq=A_eq,
        b_eq=b_eq,
        bounds=bounds,
        method="highs",
    )

    out = {
        "success": bool(result.success),
        "status": int(result.status),
        "message": result.message,
        "f0": f0,
    }
    if result.success:
        out["linearized_min_delta"] = float(result.fun)
        out["linearized_min_total"] = float(f0 + result.fun)
        out["active_link_budget_rows"] = [
            i for i, slack in enumerate(result.ineqlin.residual[1:], start=1)
            if abs(slack) < 1e-9
        ]
        out["dual_ineqlin_marginals"] = [float(x) for x in result.ineqlin.marginals]
        out["dual_eqlin_marginals"] = [float(x) for x in result.eqlin.marginals]
    return out


def main() -> None:
    c = Fraction(1, 1)
    C = Fraction(1, 1)
    rows = []
    for L in (2, 3, 4, 5):
        N = choose_N(L, c, C)
        w = Witness(L=L, c=c, C=C, N=N)
        checks = exact_checks(w)
        lp = linearized_lp(w)
        rows.append({
            "L": L,
            "constants": {"c": frac_str(c), "C": frac_str(C)},
            "witness": {
                "N": N,
                "tau": frac_str(w.tau),
                "delta": frac_str(w.delta),
                "sigma_tilde": frac_str(w.sigma),
                "edges": [frac_str(w.edge)] * L,
                "gaps": [frac_str(w.gap)] * L,
                "path_product": frac_str(w.pi),
                "F": frac_str(w.floor_poly),
            },
            "exact_checks": checks,
            "lp_linearization": lp,
            "sos_degree_2": "blocked_by_exact_negative_witness",
            "sos_degree_4": "blocked_by_exact_negative_witness",
            "geometric_reading": (
                "all link budgets a_i*d_i=delta are tight; sigma_tilde>tau is slack; "
                "the path product collapses as tau^L while every local correction is "
                "only order delta"
            ),
        })

    out = {
        "model": "scalar necessary thin-chain model from formalization.md",
        "certificate_target": "prod_i a_i + C*L*delta - c*tau >= 0",
        "note": (
            "The exact rational witnesses falsify this scalar target, so no valid "
            "LP/SOS certificate exists for this reduced model at any degree."
        ),
        "results": rows,
    }
    Path("outputs").mkdir(exist_ok=True)
    Path("outputs/thin_chain_search.json").write_text(
        json.dumps(out, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    lines = []
    for row in rows:
        w = row["witness"]
        lines.append(
            f"L={row['L']}: N={w['N']} tau={w['tau']} "
            f"Pi={w['path_product']} F={w['F']} "
            f"LP_total={row['lp_linearization'].get('linearized_min_total')}"
        )
    Path("outputs/thin_chain_search.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
