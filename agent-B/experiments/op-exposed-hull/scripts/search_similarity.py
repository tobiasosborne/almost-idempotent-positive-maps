#!/usr/bin/env python3
"""Random and local search over similarity-conjugated stochastic projections."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from exposed_hull import exposed_hull_report, max_negative_mass  # noqa: E402
from families import row_sum_zero_direction, scale_direction_to_delta  # noqa: E402


def score_report(report: dict) -> float:
    value = report["max_distance_ratio"]
    if math.isfinite(value):
        return float(value)
    return 1_000.0


def evaluate_direction(
    direction: np.ndarray,
    n: int,
    rank: int,
    target_delta: float,
    max_amp: float,
    rho_mult: float,
    kappa_mult: float,
) -> dict:
    generated = scale_direction_to_delta(n, rank, direction, target_delta, max_amp)
    report = exposed_hull_report(generated.matrix, rho_mult, kappa_mult)
    return {
        "metadata": generated.metadata,
        "delta": max_negative_mass(generated.matrix),
        "report": report,
        "score": score_report(report),
        "direction": np.asarray(direction, dtype=float).reshape(n, n).tolist(),
    }


def local_polish(best: dict, args: argparse.Namespace) -> dict:
    x0 = np.asarray(best["direction"], dtype=float).reshape(args.n * args.n)

    def objective(x: np.ndarray) -> float:
        direction = x.reshape(args.n, args.n)
        try:
            entry = evaluate_direction(
                direction,
                args.n,
                args.rank,
                args.target_delta,
                args.max_amp,
                args.rho_mult,
                args.kappa_mult,
            )
        except Exception:
            return 1_000_000.0
        return -entry["score"]

    result = minimize(
        objective,
        x0,
        method="Nelder-Mead",
        options={"maxiter": args.polish_iters, "xatol": 1e-3, "fatol": 1e-3},
    )
    polished = evaluate_direction(
        result.x.reshape(args.n, args.n),
        args.n,
        args.rank,
        args.target_delta,
        args.max_amp,
        args.rho_mult,
        args.kappa_mult,
    )
    polished["polish_result"] = {
        "success": bool(result.success),
        "status": int(result.status),
        "message": str(result.message),
        "fun": float(result.fun),
        "nit": int(result.nit),
        "nfev": int(result.nfev),
    }
    return polished


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=6)
    parser.add_argument("--rank", type=int, default=3)
    parser.add_argument("--target-delta", type=float, default=1e-3)
    parser.add_argument("--max-amp", type=float, default=0.5)
    parser.add_argument("--rho-mult", type=float, default=4.0)
    parser.add_argument("--kappa-mult", type=float, default=0.25)
    parser.add_argument("--samples", type=int, default=100)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--keep", type=int, default=10)
    parser.add_argument("--polish", action="store_true")
    parser.add_argument("--polish-iters", type=int, default=80)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    top: list[dict] = []
    for sample in range(args.samples):
        direction = row_sum_zero_direction(args.n, args.seed + sample)
        try:
            entry = evaluate_direction(
                direction,
                args.n,
                args.rank,
                args.target_delta,
                args.max_amp,
                args.rho_mult,
                args.kappa_mult,
            )
        except Exception as exc:
            entry = {
                "sample": sample,
                "seed": args.seed + sample,
                "error": repr(exc),
                "score": -math.inf,
            }
        entry["sample"] = sample
        entry["seed"] = args.seed + sample
        top.append(entry)
        top.sort(key=lambda item: item.get("score", -math.inf), reverse=True)
        top = top[: args.keep]

    parameters = {
        key: str(value) if isinstance(value, Path) else value
        for key, value in vars(args).items()
    }
    payload = {
        "command": " ".join(sys.argv),
        "parameters": parameters,
        "top": top,
    }
    if args.polish and top and top[0].get("score", -math.inf) > -math.inf:
        payload["polished"] = local_polish(top[0], args)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
