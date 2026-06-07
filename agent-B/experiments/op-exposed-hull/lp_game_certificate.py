#!/usr/bin/env python3
"""Frozen-P LP/game diagnostics for op-exposed-hull closed bad classes.

This is Agent B sandbox code.  It does not prove the theorem; it mines finite
LP certificates for the negation of the closed-bad-class augmentation lemma
after the exact signed retraction P has been fixed.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from exposed_hull import (  # noqa: E402
    exposed_hull_report,
    exposedness_modulus,
    l1_distance_to_conv,
    max_negative_mass,
    retraction_errors,
    vertex_indices,
)
from families import (  # noqa: E402
    hume,
    hume_product,
    random_similarity_retraction,
    regular_polygon_projection,
)


LP_TOL = 1e-8


@dataclass
class LPResult:
    success: bool
    value: float | None
    status: int
    message: str
    payload: dict


def parse_indices(text: str | None) -> list[int] | None:
    if text is None or text.strip() == "":
        return None
    return [int(part) for part in text.split(",") if part.strip()]


def safe_float(x: float | None) -> float | str | None:
    if x is None:
        return None
    if math.isnan(x):
        return "nan"
    if math.isinf(x):
        return "inf" if x > 0 else "-inf"
    return float(x)


def repaired_kernel(rows: np.ndarray) -> tuple[np.ndarray, list[float]]:
    rows = np.asarray(rows, dtype=float)
    q = np.zeros_like(rows)
    negs: list[float] = []
    for i, row in enumerate(rows):
        pos = np.maximum(row, 0.0)
        mass = float(pos.sum())
        if mass <= 0.0:
            raise ValueError(f"row {i} has no positive mass")
        q[i] = pos / mass
        negs.append(float(np.maximum(-row, 0.0).sum()))
    return q, negs


def build_matrix(args: argparse.Namespace):
    if args.family == "hume":
        return hume(args.s)
    if args.family == "hume-product":
        return hume_product(args.s, args.power)
    if args.family == "regular-polygon":
        return regular_polygon_projection(args.n)
    if args.family == "random-similarity":
        return random_similarity_retraction(args.n, args.rank, args.amp, args.seed)
    raise ValueError(args.family)


def distances_to_skeleton(rows: np.ndarray, indices: list[int]) -> list[dict]:
    if not indices:
        return [
            {"value": "inf", "success": False, "status": -1, "message": "empty skeleton"}
            for _ in range(len(rows))
        ]
    hull = rows[indices]
    out = []
    for row in rows:
        dist = l1_distance_to_conv(row, hull)
        out.append(
            {
                "value": safe_float(dist.value),
                "success": dist.success,
                "status": dist.status,
                "message": dist.message,
            }
        )
    return out


def common_separator_lp(
    rows: np.ndarray,
    bad: list[int],
    skeleton: list[int],
    margin: float,
) -> LPResult:
    """Find a single l_infty-dual separator for B above conv(skeleton)."""

    rows = np.asarray(rows, dtype=float)
    n, d = rows.shape
    if not bad or not skeleton:
        return LPResult(False, None, -1, "empty bad set or skeleton", {})

    # Variables: phi_0,...,phi_{d-1}, s.  Bounds |phi_k|<=1, s free.
    c = np.zeros(d + 1)
    a_ub = []
    b_ub = []
    for idx in skeleton:
        row = np.zeros(d + 1)
        row[:d] = rows[idx]
        row[d] = -1.0
        a_ub.append(row)
        b_ub.append(0.0)
    for idx in bad:
        row = np.zeros(d + 1)
        row[:d] = -rows[idx]
        row[d] = 1.0
        a_ub.append(row)
        b_ub.append(-margin)

    res = linprog(
        c,
        A_ub=np.asarray(a_ub),
        b_ub=np.asarray(b_ub),
        bounds=[(-1.0, 1.0)] * d + [(None, None)],
        method="highs",
    )
    payload: dict = {}
    value = None
    if res.success:
        phi = np.asarray(res.x[:d])
        s = float(res.x[d])
        skeleton_slack = [float(phi @ rows[i] - s) for i in skeleton]
        bad_margin = [float(phi @ rows[i] - s) for i in bad]
        value = min(bad_margin) if bad_margin else None
        payload = {
            "phi": phi.tolist(),
            "s": s,
            "skeleton_slack_max": max(skeleton_slack) if skeleton_slack else None,
            "bad_margin_min": value,
            "bad_margins": bad_margin,
        }
    return LPResult(bool(res.success), value, int(res.status), str(res.message), payload)


def quasi_closed_lp(
    q: np.ndarray,
    bad: list[int],
    exit_tol: float,
    stationarity_tol: float,
) -> LPResult:
    """Search for a quasi-stationary bad distribution for fixed repaired Q."""

    q = np.asarray(q, dtype=float)
    if not bad:
        return LPResult(False, None, -1, "empty bad set", {})

    m = len(bad)
    bad_pos = {idx: pos for pos, idx in enumerate(bad)}
    good = [j for j in range(q.shape[1]) if j not in bad_pos]
    t_block = q[np.ix_(bad, bad)]
    exits = q[np.ix_(bad, good)].sum(axis=1) if good else np.zeros(m)

    # Variables: mu_0,...,mu_{m-1}, r_0,...,r_{m-1}.
    c = np.zeros(2 * m)
    a_eq = np.zeros((1, 2 * m))
    a_eq[0, :m] = 1.0
    b_eq = np.array([1.0])

    a_ub = []
    b_ub = []
    exit_row = np.zeros(2 * m)
    exit_row[:m] = exits
    a_ub.append(exit_row)
    b_ub.append(exit_tol)

    stat_sum = np.zeros(2 * m)
    stat_sum[m:] = 1.0
    a_ub.append(stat_sum)
    b_ub.append(stationarity_tol)

    # defect_k = mu_k - sum_i mu_i T_{i,k}; impose |defect_k| <= r_k.
    for k in range(m):
        coeff = np.zeros(2 * m)
        coeff[:m] = -t_block[:, k]
        coeff[k] += 1.0
        coeff[m + k] = -1.0
        a_ub.append(coeff)
        b_ub.append(0.0)

        coeff = np.zeros(2 * m)
        coeff[:m] = t_block[:, k]
        coeff[k] -= 1.0
        coeff[m + k] = -1.0
        a_ub.append(coeff)
        b_ub.append(0.0)

    res = linprog(
        c,
        A_ub=np.asarray(a_ub),
        b_ub=np.asarray(b_ub),
        A_eq=a_eq,
        b_eq=b_eq,
        bounds=[(0.0, None)] * (2 * m),
        method="highs",
    )
    payload: dict = {}
    value = None
    if res.success:
        mu = np.asarray(res.x[:m])
        defect = mu - mu @ t_block
        exit_value = float(mu @ exits)
        stat_value = float(np.abs(defect).sum())
        value = exit_value
        payload = {
            "mu": {str(idx): float(mu[pos]) for pos, idx in enumerate(bad)},
            "exit": exit_value,
            "stationarity_l1": stat_value,
            "row_exits": {str(idx): float(exits[pos]) for pos, idx in enumerate(bad)},
        }
    return LPResult(bool(res.success), value, int(res.status), str(res.message), payload)


def failed_exposedness_dual_lp(
    rows: np.ndarray,
    vertex: int,
    rho: float,
) -> LPResult:
    """Minimize the beta mass in the LP-dual failed-exposedness circuit."""

    rows = np.asarray(rows, dtype=float)
    n, d = rows.shape
    v = rows[vertex]
    outside = [i for i in range(n) if np.linalg.norm(rows[i] - v, ord=1) >= rho]
    if not outside:
        return LPResult(False, None, -1, "outside set empty", {"outside": []})

    m = len(outside)
    # Variables: mu(outside), alpha(all rows), beta(all rows).
    total_vars = m + 2 * n
    beta_offset = m + n
    c = np.zeros(total_vars)
    c[beta_offset : beta_offset + n] = 1.0

    a_eq = []
    b_eq = []
    row = np.zeros(total_vars)
    row[:m] = 1.0
    a_eq.append(row)
    b_eq.append(1.0)

    z = rows - v
    for coord in range(d):
        row = np.zeros(total_vars)
        for pos, idx in enumerate(outside):
            row[pos] = z[idx, coord]
        row[m : m + n] = z[:, coord]
        row[beta_offset : beta_offset + n] = -z[:, coord]
        a_eq.append(row)
        b_eq.append(0.0)

    res = linprog(
        c,
        A_eq=np.asarray(a_eq),
        b_eq=np.asarray(b_eq),
        bounds=[(0.0, None)] * total_vars,
        method="highs",
    )
    payload: dict = {"outside": outside}
    value = None
    if res.success:
        x = np.asarray(res.x)
        mu = x[:m]
        alpha = x[m : m + n]
        beta = x[beta_offset : beta_offset + n]
        value = float(beta.sum())
        payload.update(
            {
                "beta_mass": value,
                "alpha_mass": float(alpha.sum()),
                "mu_support": {
                    str(outside[pos]): float(weight)
                    for pos, weight in enumerate(mu)
                    if weight > 1e-9
                },
                "beta_support": {
                    str(i): float(weight) for i, weight in enumerate(beta) if weight > 1e-9
                },
                "alpha_support": {
                    str(i): float(weight) for i, weight in enumerate(alpha) if weight > 1e-9
                },
            }
        )
    return LPResult(bool(res.success), value, int(res.status), str(res.message), payload)


def choose_sets(args: argparse.Namespace, rows: np.ndarray, report: dict) -> tuple[list[int], list[int]]:
    vertices = report["vertices"]
    w_indices = report["W_indices"]
    skeleton = parse_indices(args.skeleton_indices)
    if skeleton is None:
        if args.skeleton_mode == "W":
            skeleton = list(w_indices)
        elif args.skeleton_mode == "first-W":
            skeleton = list(w_indices[:1])
        elif args.skeleton_mode == "first-vertex":
            skeleton = list(vertices[:1])
        else:
            raise ValueError(args.skeleton_mode)

    bad = parse_indices(args.bad_indices)
    if bad is None:
        distances = distances_to_skeleton(rows, skeleton)
        delta = report["delta"]
        tau = math.sqrt(max(delta, 0.0))
        margin = args.bad_mult * tau
        bad = []
        for idx in vertices:
            if idx in skeleton:
                continue
            value = distances[idx]["value"]
            if isinstance(value, float) and value > margin:
                bad.append(idx)
    return skeleton, bad


def verdict(
    bad: list[int],
    individually_far: bool,
    exposed_failures: dict[str, dict],
    separator: LPResult,
    quasi_closed: LPResult,
) -> str:
    if not bad:
        return "no_bad_vertices"
    if not individually_far:
        return "bad_set_not_far_from_skeleton"
    exposed_in_bad = [
        idx for idx, row in exposed_failures.items() if row.get("well_exposed_at_threshold")
    ]
    if exposed_in_bad:
        return "augmentation_vertex_present"
    if not separator.success:
        return "no_common_separator_for_bad_set"
    if not quasi_closed.success:
        return "bad_set_not_quasi_closed"
    return "frozen_linear_negation_feasible"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--family",
        choices=["hume", "hume-product", "regular-polygon", "random-similarity"],
        required=True,
    )
    parser.add_argument("--s", type=float, default=0.01)
    parser.add_argument("--power", type=int, default=2)
    parser.add_argument("--n", type=int, default=12)
    parser.add_argument("--rank", type=int, default=3)
    parser.add_argument("--amp", type=float, default=0.05)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--rho-mult", type=float, default=1.0)
    parser.add_argument("--kappa-mult", type=float, default=0.25)
    parser.add_argument("--bad-mult", type=float, default=1.0)
    parser.add_argument("--exit-mult", type=float, default=1.0)
    parser.add_argument("--stationarity-mult", type=float, default=2.0)
    parser.add_argument("--skeleton-mode", choices=["W", "first-W", "first-vertex"], default="W")
    parser.add_argument("--skeleton-indices")
    parser.add_argument("--bad-indices")
    parser.add_argument("--out-json", type=Path, required=True)
    args = parser.parse_args()

    generated = build_matrix(args)
    rows = np.asarray(generated.matrix, dtype=float)
    report = exposed_hull_report(rows, args.rho_mult, args.kappa_mult)
    delta = max_negative_mass(rows)
    tau = math.sqrt(max(delta, 0.0))
    rho = args.rho_mult * tau
    kappa = args.kappa_mult * tau
    bad_margin = args.bad_mult * tau
    exit_tol = args.exit_mult * tau
    stationarity_tol = args.stationarity_mult * tau
    q, negs = repaired_kernel(rows)
    skeleton, bad = choose_sets(args, rows, report)
    distances = distances_to_skeleton(rows, skeleton)

    exposed_failures = {}
    for idx in bad:
        primal = exposedness_modulus(rows, idx, rho)
        dual = failed_exposedness_dual_lp(rows, idx, rho)
        dual_value = dual.value if dual.value is not None else math.inf
        exposed_failures[str(idx)] = {
            "primal_exposedness": safe_float(primal.value),
            "primal_success": primal.success,
            "dual_beta_min": safe_float(dual_value),
            "dual_success": dual.success,
            "dual_message": dual.message,
            "well_exposed_at_threshold": bool(primal.success and primal.value + 1e-8 >= kappa),
            "dual_payload": dual.payload,
        }

    separator = common_separator_lp(rows, bad, skeleton, bad_margin)
    quasi_closed = quasi_closed_lp(q, bad, exit_tol, stationarity_tol)
    far_flags = []
    for idx in bad:
        value = distances[idx]["value"]
        far_flags.append(isinstance(value, float) and value > bad_margin)
    individually_far = bool(bad) and all(far_flags)

    output = {
        "command": " ".join(sys.argv),
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "model_scope": "frozen_P_linear_subproblem",
        "metadata": generated.metadata,
        "constants": {
            "rho_mult": args.rho_mult,
            "kappa_mult": args.kappa_mult,
            "bad_mult": args.bad_mult,
            "exit_mult": args.exit_mult,
            "stationarity_mult": args.stationarity_mult,
            "delta": delta,
            "tau": tau,
            "rho": rho,
            "kappa": kappa,
            "bad_margin": bad_margin,
            "exit_tol": exit_tol,
            "stationarity_tol": stationarity_tol,
        },
        "sets": {
            "vertices": vertex_indices(rows),
            "W_indices": report["W_indices"],
            "skeleton_indices": skeleton,
            "bad_indices": bad,
            "bad_individually_far": individually_far,
        },
        "errors": retraction_errors(rows),
        "negative_masses": negs,
        "distances_to_skeleton": distances,
        "common_separator": {
            "success": separator.success,
            "value": safe_float(separator.value),
            "status": separator.status,
            "message": separator.message,
            "payload": separator.payload,
        },
        "quasi_closed_distribution": {
            "success": quasi_closed.success,
            "value": safe_float(quasi_closed.value),
            "status": quasi_closed.status,
            "message": quasi_closed.message,
            "payload": quasi_closed.payload,
        },
        "failed_exposedness_witnesses": exposed_failures,
    }
    output["verdict"] = verdict(bad, individually_far, exposed_failures, separator, quasi_closed)

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(args.out_json)
    print(output["verdict"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
