#!/usr/bin/env python3
"""LP probes for the robust-coordinate interpolation upgrade.

Sandbox evidence only.  Given exact signed affine retraction rows P and a
chosen representative set R, solve for a stochastic kernel U from row labels to
representatives that:

  * reconstructs every row within an l1 budget gamma, and
  * minimizes max_b sum_a |sum_j r^b_j U_{j,a} - delta_{ba}|.

The second quantity is the row-l1 representative interpolation defect of
G=P_R U.  This is stronger than entrywise control and is the dimension-free
quantity needed by the exactification step.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import numpy as np
from scipy.optimize import linprog


ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from exposed_hull import (  # noqa: E402
    LPValue,
    l1_distance_to_conv,
    max_negative_mass,
    vertex_indices,
)
from families import (  # noqa: E402
    hume,
    row_sum_zero_direction,
    scale_direction_to_delta,
)


@dataclass
class KernelResult:
    success: bool
    status: int
    message: str
    objective: float
    max_reconstruction_l1: float | None
    max_g_minus_i_l1_row: float | None
    max_g_minus_i: float | None
    g_matrix: list[list[float]] | None


@dataclass
class CaseResult:
    name: str
    n: int
    reps: list[int]
    delta: float
    tau: float
    gamma: float
    gamma_over_tau: float | None
    best_simplex_hull_error: float | None
    objective_over_delta: float | None
    objective_over_tau: float | None
    kernel: KernelResult


@dataclass
class Output:
    command: str
    script_sha256: str
    cases: list[CaseResult]


def script_hash() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def quadrilateral_family(t: float) -> np.ndarray:
    """The rank-three quadrilateral family from small_cases_exact.py."""

    v = np.array([1.0 - t * t, t * t, -1.0 + t * t, -t * t])
    u = np.array([1.0, 0.0, -t * t / (1.0 - t * t), 0.0])
    return np.eye(4) - np.outer(u, v)


def affine_dimension(rows: np.ndarray, tol: float = 1e-9) -> int:
    if len(rows) <= 1:
        return 0
    return int(np.linalg.matrix_rank(rows[1:] - rows[0], tol=tol))


def max_distance_to_hull(rows: np.ndarray, reps: Iterable[int]) -> float:
    hull = rows[list(reps)]
    values: list[float] = []
    for row in rows:
        dist: LPValue = l1_distance_to_conv(row, hull)
        if not dist.success:
            return math.inf
        values.append(dist.value)
    return float(max(values, default=0.0))


def best_simplex_reps(rows: np.ndarray) -> tuple[list[int], float]:
    verts = vertex_indices(rows)
    dim = affine_dimension(rows)
    size = dim + 1
    if len(verts) <= size:
        return verts, max_distance_to_hull(rows, verts)

    best_reps: tuple[int, ...] | None = None
    best_error = math.inf
    for reps in itertools.combinations(verts, size):
        error = max_distance_to_hull(rows, reps)
        if error < best_error:
            best_error = error
            best_reps = reps
    if best_reps is None:
        raise RuntimeError("no simplex representatives found")
    return list(best_reps), best_error


def solve_interpolation_kernel(
    rows: np.ndarray,
    reps: list[int],
    gamma: float,
) -> KernelResult:
    rows = np.asarray(rows, dtype=float)
    n, d = rows.shape
    m = len(reps)
    num_u = n * m
    num_e = n * d
    num_g_abs = m * m
    g_abs_start = num_u + num_e
    t_idx = g_abs_start + num_g_abs
    total = t_idx + 1

    def u_idx(j: int, a: int) -> int:
        return j * m + a

    def e_idx(j: int, k: int) -> int:
        return num_u + j * d + k

    def g_abs_idx(b_pos: int, a: int) -> int:
        return g_abs_start + b_pos * m + a

    c = np.zeros(total)
    c[t_idx] = 1.0

    a_eq: list[np.ndarray] = []
    b_eq: list[float] = []
    for j in range(n):
        row = np.zeros(total)
        for a in range(m):
            row[u_idx(j, a)] = 1.0
        a_eq.append(row)
        b_eq.append(1.0)

    a_ub: list[np.ndarray] = []
    b_ub: list[float] = []

    # l1 reconstruction budget for each row.
    rep_rows = rows[reps]
    for j in range(n):
        for k in range(d):
            upper = np.zeros(total)
            lower = np.zeros(total)
            for a in range(m):
                upper[u_idx(j, a)] = rep_rows[a, k]
                lower[u_idx(j, a)] = -rep_rows[a, k]
            upper[e_idx(j, k)] = -1.0
            lower[e_idx(j, k)] = -1.0
            a_ub.append(upper)
            b_ub.append(float(rows[j, k]))
            a_ub.append(lower)
            b_ub.append(float(-rows[j, k]))

        budget = np.zeros(total)
        for k in range(d):
            budget[e_idx(j, k)] = 1.0
        a_ub.append(budget)
        b_ub.append(float(gamma))

    # Representative interpolation matrix G=P_R U.
    for b_pos, b in enumerate(reps):
        for a in range(m):
            target = 1.0 if a == b_pos else 0.0

            plus = np.zeros(total)
            minus = np.zeros(total)
            for j in range(n):
                coeff = rows[b, j]
                plus[u_idx(j, a)] = coeff
                minus[u_idx(j, a)] = -coeff
            plus[g_abs_idx(b_pos, a)] = -1.0
            minus[g_abs_idx(b_pos, a)] = -1.0
            a_ub.append(plus)
            b_ub.append(target)
            a_ub.append(minus)
            b_ub.append(-target)

        row_l1 = np.zeros(total)
        for a in range(m):
            row_l1[g_abs_idx(b_pos, a)] = 1.0
        row_l1[t_idx] = -1.0
        a_ub.append(row_l1)
        b_ub.append(0.0)

    bounds = [(0.0, None)] * total
    res = linprog(
        c,
        A_ub=np.asarray(a_ub),
        b_ub=np.asarray(b_ub),
        A_eq=np.asarray(a_eq),
        b_eq=np.asarray(b_eq),
        bounds=bounds,
        method="highs",
    )
    if not res.success:
        return KernelResult(
            success=False,
            status=int(res.status),
            message=str(res.message),
            objective=math.inf,
            max_reconstruction_l1=None,
            max_g_minus_i_l1_row=None,
            max_g_minus_i=None,
            g_matrix=None,
        )

    x = np.asarray(res.x)
    u = x[:num_u].reshape(n, m)
    recon = u @ rep_rows
    max_recon = float(np.max(np.sum(np.abs(rows - recon), axis=1)))
    g = rows[reps] @ u
    target = np.eye(m)
    max_g_l1 = float(np.max(np.sum(np.abs(g - target), axis=1)))
    max_g = float(np.max(np.abs(g - target)))
    return KernelResult(
        success=True,
        status=int(res.status),
        message=str(res.message),
        objective=float(res.fun),
        max_reconstruction_l1=max_recon,
        max_g_minus_i_l1_row=max_g_l1,
        max_g_minus_i=max_g,
        g_matrix=np.round(g, 12).tolist(),
    )


def analyze_case(name: str, rows: np.ndarray, reps: list[int] | None = None) -> CaseResult:
    rows = np.asarray(rows, dtype=float)
    delta = max_negative_mass(rows)
    tau = math.sqrt(max(delta, 0.0))
    if reps is None:
        reps, hull_error = best_simplex_reps(rows)
    else:
        hull_error = max_distance_to_hull(rows, reps)
    # Allow the known hull error and a modest square-root margin.
    gamma = max(hull_error + 1e-10, 4.0 * tau)
    kernel = solve_interpolation_kernel(rows, reps, gamma)
    objective = kernel.objective if kernel.success else math.inf
    return CaseResult(
        name=name,
        n=int(rows.shape[0]),
        reps=list(reps),
        delta=float(delta),
        tau=float(tau),
        gamma=float(gamma),
        gamma_over_tau=float(gamma / tau) if tau > 0 else None,
        best_simplex_hull_error=float(hull_error),
        objective_over_delta=float(objective / delta) if delta > 0 and math.isfinite(objective) else None,
        objective_over_tau=float(objective / tau) if tau > 0 and math.isfinite(objective) else None,
        kernel=kernel,
    )


def main() -> None:
    out = ROOT / "interpolation_upgrade_probe.json"
    cases: list[CaseResult] = []

    for s in [0.2, 0.1, 0.05, 0.02, 0.01]:
        cases.append(analyze_case(f"hume_s_{s:g}", hume(s).matrix))

    for t in [0.2, 0.1, 0.05, 0.02, 0.01]:
        # Use the natural triangle after deleting the close mate p_2.
        cases.append(analyze_case(f"quadrilateral_t_{t:g}", quadrilateral_family(t), reps=[0, 1, 3]))

    for target_delta in [1e-2, 1e-3, 1e-4]:
        direction = row_sum_zero_direction(6, seed=20260607)
        generated = scale_direction_to_delta(
            6,
            3,
            direction,
            target_delta=target_delta,
            max_amp=0.25,
        )
        cases.append(
            analyze_case(
                f"similarity_n6_r3_target_delta_{target_delta:g}",
                generated.matrix,
            )
        )

    output = Output(
        command="python3 agent-B/experiments/op-exposed-hull/interpolation_upgrade_probe.py",
        script_sha256=script_hash(),
        cases=cases,
    )
    out.write_text(json.dumps(asdict(output), indent=2), encoding="utf-8")
    print(f"wrote {out}")
    for case in cases:
        obj = case.kernel.objective
        print(
            f"{case.name}: reps={case.reps} delta={case.delta:.3g} "
            f"tau={case.tau:.3g} gamma/tau={case.gamma_over_tau:.3g} "
            f"min row_l1||G-I||={obj:.3g} "
            f"obj/delta={case.objective_over_delta} obj/tau={case.objective_over_tau}"
        )


if __name__ == "__main__":
    main()
