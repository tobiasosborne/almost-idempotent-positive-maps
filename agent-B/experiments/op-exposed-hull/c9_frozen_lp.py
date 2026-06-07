#!/usr/bin/env python3
"""C9 frozen-row LP diagnostics for the shadow-exit interface.

Agent B sandbox code only.  The model fixes the row matrix P and tests the
linear pieces of a C9 failure pattern:

  q-quasi-closed high bad class
  + failed-exposedness shadow witnesses forced to leak below H1
  + no short repaired-kernel lifetime fallback.

It is not a proof and not a canonical artifact.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from hashlib import sha256
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))
sys.path.insert(0, str(ROOT))

from exposed_hull import (  # noqa: E402
    exposed_hull_report,
    exposedness_modulus,
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
from lp_game_certificate import (  # noqa: E402
    LPResult,
    distances_to_skeleton,
    failed_exposedness_dual_lp,
    parse_indices,
    quasi_closed_lp,
    repaired_kernel,
    safe_float,
)


LP_TOL = 1e-8


def build_rows(args: argparse.Namespace) -> tuple[np.ndarray, dict]:
    if args.matrix_json is not None:
        data = json.loads(args.matrix_json.read_text(encoding="utf-8"))
        item = data["top"][args.matrix_index]
        return np.asarray(item["matrix"], dtype=float), {
            "source": "matrix_json",
            "path": str(args.matrix_json),
            "matrix_index": int(args.matrix_index),
            "metadata": item.get("metadata", {}),
            "summary": item.get("summary", {}),
        }
    if args.family == "hume":
        generated = hume(args.s)
    elif args.family == "hume-product":
        generated = hume_product(args.s, args.power)
    elif args.family == "regular-polygon":
        generated = regular_polygon_projection(args.n)
    elif args.family == "random-similarity":
        generated = random_similarity_retraction(args.n, args.rank, args.amp, args.seed)
    else:
        raise ValueError(args.family)
    return np.asarray(generated.matrix, dtype=float), generated.metadata


def max_margin_separator(rows: np.ndarray, bad: list[int], skeleton: list[int]) -> LPResult:
    """Maximize the common l_infty separator margin for bad rows over skeleton."""

    rows = np.asarray(rows, dtype=float)
    n, d = rows.shape
    if not bad or not skeleton:
        return LPResult(False, None, -1, "empty bad set or skeleton", {})

    # Variables: phi_0,...,phi_{d-1}, s, t.  Maximize t.
    c = np.zeros(d + 2)
    c[d + 1] = -1.0
    a_ub = []
    b_ub = []
    for idx in skeleton:
        row = np.zeros(d + 2)
        row[:d] = rows[idx]
        row[d] = -1.0
        a_ub.append(row)
        b_ub.append(0.0)
    for idx in bad:
        row = np.zeros(d + 2)
        row[:d] = -rows[idx]
        row[d] = 1.0
        row[d + 1] = 1.0
        a_ub.append(row)
        b_ub.append(0.0)

    res = linprog(
        c,
        A_ub=np.asarray(a_ub),
        b_ub=np.asarray(b_ub),
        bounds=[(-1.0, 1.0)] * d + [(None, None), (0.0, None)],
        method="highs",
    )
    payload: dict = {}
    value = None
    if res.success:
        phi = np.asarray(res.x[:d])
        s = float(res.x[d])
        value = float(res.x[d + 1])
        heights = rows @ phi
        payload = {
            "phi": phi.tolist(),
            "s": s,
            "max_margin": value,
            "global_max_height": float(np.max(heights)),
            "row_heights": [float(x) for x in heights],
            "skeleton_slack_max": float(max(heights[i] - s for i in skeleton)),
            "bad_margin_min": float(min(heights[i] - s for i in bad)),
        }
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


def lifetime_to_exit(q: np.ndarray, indices: list[int]) -> dict:
    """Return repaired-kernel occupation lifetime on a fixed index set."""

    if not indices:
        return {
            "success": False,
            "message": "empty index set",
            "max_lifetime": None,
            "spectral_radius": None,
            "row_exits": {},
        }
    t = q[np.ix_(indices, indices)]
    row_exits = 1.0 - t.sum(axis=1)
    try:
        eigvals = np.linalg.eigvals(t)
        spectral_radius = float(np.max(np.abs(eigvals))) if len(eigvals) else 0.0
        v = np.linalg.solve(np.eye(len(indices)) - t, np.ones(len(indices)))
        return {
            "success": True,
            "message": "finite",
            "max_lifetime": float(np.max(v)),
            "min_lifetime": float(np.min(v)),
            "spectral_radius": spectral_radius,
            "row_exits": {str(i): float(row_exits[pos]) for pos, i in enumerate(indices)},
            "lifetimes": {str(i): float(v[pos]) for pos, i in enumerate(indices)},
        }
    except np.linalg.LinAlgError:
        return {
            "success": True,
            "message": "singular_or_closed",
            "max_lifetime": "inf",
            "min_lifetime": "inf",
            "spectral_radius": 1.0,
            "row_exits": {str(i): float(row_exits[pos]) for pos, i in enumerate(indices)},
            "lifetimes": {str(i): "inf" for i in indices},
        }


def shadow_leak_lp(
    rows: np.ndarray,
    vertex: int,
    rho: float,
    kappa: float,
    phi: np.ndarray,
    h1: set[int],
    average_drop: float,
) -> LPResult:
    """Minimize H1 leakage among failed-exposedness dual witnesses.

    Variables are the Step-5 dual circuit variables:
      mu on outside-rho rows, alpha on all rows, beta on all rows.
    Additional constraints enforce beta mass <= kappa and high average height.
    """

    rows = np.asarray(rows, dtype=float)
    phi = np.asarray(phi, dtype=float)
    n, d = rows.shape
    v = rows[vertex]
    outside = [i for i in range(n) if np.linalg.norm(rows[i] - v, ord=1) >= rho]
    if not outside:
        return LPResult(False, None, -1, "outside set empty", {"outside": []})

    m = len(outside)
    total_vars = m + 2 * n
    alpha_offset = m
    beta_offset = m + n

    c = np.zeros(total_vars)
    for pos, idx in enumerate(outside):
        if idx not in h1:
            c[pos] = 1.0

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
        row[alpha_offset : alpha_offset + n] = z[:, coord]
        row[beta_offset : beta_offset + n] = -z[:, coord]
        a_eq.append(row)
        b_eq.append(0.0)

    a_ub = []
    b_ub = []
    beta_cap = np.zeros(total_vars)
    beta_cap[beta_offset : beta_offset + n] = 1.0
    a_ub.append(beta_cap)
    b_ub.append(kappa)

    high_average = np.zeros(total_vars)
    for pos, idx in enumerate(outside):
        high_average[pos] = -float(phi @ rows[idx])
    a_ub.append(high_average)
    b_ub.append(-float(phi @ v) + average_drop)

    res = linprog(
        c,
        A_ub=np.asarray(a_ub),
        b_ub=np.asarray(b_ub),
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
        alpha = x[alpha_offset : alpha_offset + n]
        beta = x[beta_offset : beta_offset + n]
        value = float(res.fun)
        h1_mass = sum(float(mu[pos]) for pos, idx in enumerate(outside) if idx in h1)
        phi_average = sum(float(mu[pos]) * float(phi @ rows[idx]) for pos, idx in enumerate(outside))
        payload.update(
            {
                "leak_mass": value,
                "h1_mass": float(h1_mass),
                "phi_average": float(phi_average),
                "source_height": float(phi @ v),
                "beta_mass": float(beta.sum()),
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


def verdict(output: dict) -> str:
    if not output["sets"]["bad_indices"]:
        return "no_bad_vertices"
    if not output["sets"]["high_bad_indices"]:
        return "no_high_bad_class"
    if output["augmentation_present_in_high_bad"]:
        return "augmentation_vertex_present"
    if not output["separator"]["success"]:
        return "no_common_separator"
    if not output["quasi_closed_distribution"]["success"]:
        return "not_quasi_closed"
    if not output["lifetime"]["no_resolvent_fallback"]:
        return "resolvent_fallback_available"
    if output["shadow_leakage"]["aggregate_forced_leak"] <= output["constants"]["leak_tol"]:
        return "high_supported_shadow_witness_available"
    return "c9_frozen_failure_candidate"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--family",
        choices=["hume", "hume-product", "regular-polygon", "random-similarity"],
        default="hume",
    )
    parser.add_argument("--matrix-json", type=Path)
    parser.add_argument("--matrix-index", type=int, default=0)
    parser.add_argument("--s", type=float, default=0.01)
    parser.add_argument("--power", type=int, default=2)
    parser.add_argument("--n", type=int, default=12)
    parser.add_argument("--rank", type=int, default=3)
    parser.add_argument("--amp", type=float, default=0.05)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--rho-mult", type=float, default=1.0)
    parser.add_argument("--kappa-mult", type=float, default=0.25)
    parser.add_argument("--bad-mult", type=float, default=1.0)
    parser.add_argument("--h1-mult", type=float, default=4.0)
    parser.add_argument("--leak-mult", type=float, default=1.0)
    parser.add_argument("--exit-mult", type=float, default=1.0)
    parser.add_argument("--stationarity-mult", type=float, default=2.0)
    parser.add_argument("--lifetime-mult", type=float, default=1.0)
    parser.add_argument("--shadow-drop-mult", type=float, default=3.0)
    parser.add_argument("--skeleton-mode", choices=["W", "first-W", "first-vertex"], default="first-W")
    parser.add_argument("--skeleton-indices")
    parser.add_argument("--bad-indices")
    parser.add_argument("--out-json", type=Path, required=True)
    args = parser.parse_args()

    rows, metadata = build_rows(args)
    report = exposed_hull_report(rows, args.rho_mult, args.kappa_mult)
    delta = max_negative_mass(rows)
    tau = math.sqrt(max(delta, 0.0))
    rho = args.rho_mult * tau
    kappa = args.kappa_mult * tau
    bad_margin = args.bad_mult * tau
    h1_gap = args.h1_mult * tau
    leak_tol = args.leak_mult * tau
    exit_tol = args.exit_mult * tau
    stationarity_tol = args.stationarity_mult * tau
    average_drop = args.shadow_drop_mult * kappa
    lifetime_threshold = math.inf if tau == 0.0 else args.lifetime_mult / tau

    skeleton, bad = choose_sets(args, rows, report)
    distances = distances_to_skeleton(rows, skeleton)
    separator = max_margin_separator(rows, bad, skeleton)
    q, negs = repaired_kernel(rows)

    phi = np.asarray(separator.payload.get("phi", np.zeros(rows.shape[1])), dtype=float)
    heights = rows @ phi
    max_height = float(np.max(heights)) if len(heights) else 0.0
    h1 = {i for i, height in enumerate(heights) if max_height - float(height) <= h1_gap + 1e-10}
    high_bad = [i for i in bad if i in h1]

    exposure = {}
    augmentation_present = False
    leak_rows = {}
    aggregate_forced_leak = 0.0
    quasi_closed = quasi_closed_lp(q, high_bad, exit_tol, stationarity_tol)
    quasi_mu = {
        int(k): float(v)
        for k, v in quasi_closed.payload.get("mu", {}).items()
    }

    for idx in high_bad:
        primal = exposedness_modulus(rows, idx, rho)
        dual = failed_exposedness_dual_lp(rows, idx, rho)
        well_exposed = bool(primal.success and primal.value + 1e-8 >= kappa)
        augmentation_present = augmentation_present or well_exposed
        leak = shadow_leak_lp(rows, idx, rho, kappa, phi, h1, average_drop)
        leak_value = float(leak.value) if leak.value is not None else math.inf
        weight = quasi_mu.get(idx, 0.0)
        if weight > 0.0:
            if math.isfinite(leak_value) and math.isfinite(aggregate_forced_leak):
                aggregate_forced_leak += weight * leak_value
            else:
                aggregate_forced_leak = math.inf
        exposure[str(idx)] = {
            "primal_exposedness": safe_float(primal.value),
            "dual_beta_min": safe_float(dual.value),
            "well_exposed_at_threshold": well_exposed,
        }
        leak_rows[str(idx)] = {
            "success": leak.success,
            "value": safe_float(leak.value),
            "status": leak.status,
            "message": leak.message,
            "payload": leak.payload,
        }

    lifetime = lifetime_to_exit(q, high_bad)
    max_lifetime_raw = lifetime["max_lifetime"]
    if max_lifetime_raw == "inf":
        no_fallback = True
    elif max_lifetime_raw is None:
        no_fallback = False
    else:
        no_fallback = float(max_lifetime_raw) > lifetime_threshold
    lifetime["threshold"] = float(lifetime_threshold) if math.isfinite(lifetime_threshold) else "inf"
    lifetime["no_resolvent_fallback"] = bool(no_fallback)

    output = {
        "command": " ".join(sys.argv),
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "model_scope": "C9 frozen-P linear diagnostic",
        "metadata": metadata,
        "constants": {
            "delta": delta,
            "tau": tau,
            "rho": rho,
            "kappa": kappa,
            "bad_margin": bad_margin,
            "h1_gap": h1_gap,
            "leak_tol": leak_tol,
            "exit_tol": exit_tol,
            "stationarity_tol": stationarity_tol,
            "average_drop": average_drop,
            "rho_mult": args.rho_mult,
            "kappa_mult": args.kappa_mult,
            "bad_mult": args.bad_mult,
            "h1_mult": args.h1_mult,
            "leak_mult": args.leak_mult,
            "lifetime_mult": args.lifetime_mult,
        },
        "errors": retraction_errors(rows),
        "negative_masses": negs,
        "sets": {
            "vertices": vertex_indices(rows),
            "W_indices": report["W_indices"],
            "skeleton_indices": skeleton,
            "bad_indices": bad,
            "H1_indices": sorted(h1),
            "high_bad_indices": high_bad,
        },
        "distances_to_skeleton": distances,
        "separator": {
            "success": separator.success,
            "value": safe_float(separator.value),
            "status": separator.status,
            "message": separator.message,
            "payload": separator.payload,
        },
        "lifetime": lifetime,
        "quasi_closed_distribution": {
            "success": quasi_closed.success,
            "value": safe_float(quasi_closed.value),
            "status": quasi_closed.status,
            "message": quasi_closed.message,
            "payload": quasi_closed.payload,
        },
        "exposure": exposure,
        "augmentation_present_in_high_bad": bool(augmentation_present),
        "shadow_leakage": {
            "aggregate_forced_leak": safe_float(aggregate_forced_leak),
            "rows": leak_rows,
        },
    }
    output["verdict"] = verdict(output)

    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(args.out_json)
    print(output["verdict"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
