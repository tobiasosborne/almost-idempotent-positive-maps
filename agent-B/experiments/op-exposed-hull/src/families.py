"""Exact signed affine retraction families for op-exposed-hull searches."""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

from exposed_hull import max_negative_mass


@dataclass
class GeneratedRetraction:
    matrix: np.ndarray
    metadata: dict


def hume(s: float) -> GeneratedRetraction:
    v = np.array([1.0, -1.0 + s, -s])
    u = np.array([1.0 - s + s * s, -s, 0.0])
    p = np.eye(3) - np.outer(u, v)
    return GeneratedRetraction(p, {"family": "hume", "s": float(s)})


def kronecker_power(p: np.ndarray, power: int) -> np.ndarray:
    out = np.array([[1.0]])
    for _ in range(power):
        out = np.kron(out, p)
    return out


def hume_product(s: float, power: int) -> GeneratedRetraction:
    base = hume(s).matrix
    p = kronecker_power(base, power)
    return GeneratedRetraction(p, {"family": "hume_product", "s": float(s), "power": int(power)})


def regular_polygon_projection(n: int) -> GeneratedRetraction:
    angles = 2.0 * math.pi * np.arange(n) / n
    x = np.column_stack([np.ones(n), np.cos(angles), np.sin(angles)])
    p = x @ np.linalg.inv(x.T @ x) @ x.T
    return GeneratedRetraction(p, {"family": "regular_polygon_projection", "n": int(n)})


def balanced_partition(n: int, rank: int) -> list[np.ndarray]:
    if not 1 <= rank <= n:
        raise ValueError("rank must satisfy 1 <= rank <= n")
    indices = np.arange(n)
    return [chunk for chunk in np.array_split(indices, rank) if len(chunk) > 0]


def stochastic_cluster_idempotent(n: int, rank: int) -> np.ndarray:
    clusters = balanced_partition(n, rank)
    e = np.zeros((n, n))
    for cluster in clusters:
        weights = np.zeros(n)
        weights[cluster] = 1.0 / len(cluster)
        for idx in cluster:
            e[idx] = weights
    return e


def row_sum_zero_direction(n: int, seed: int | None = None) -> np.ndarray:
    rng = np.random.default_rng(seed)
    m = rng.normal(size=(n, n))
    m -= m.mean(axis=1, keepdims=True)
    scale = np.max(np.abs(m))
    if scale > 0:
        m /= scale
    return m


def similarity_retraction(
    n: int,
    rank: int,
    direction: np.ndarray,
    amp: float,
) -> GeneratedRetraction:
    e = stochastic_cluster_idempotent(n, rank)
    direction = np.asarray(direction, dtype=float).reshape(n, n)
    direction = direction - direction.mean(axis=1, keepdims=True)
    scale = np.max(np.abs(direction))
    if scale > 0:
        direction = direction / scale
    s = np.eye(n) + amp * direction
    cond = float(np.linalg.cond(s))
    p = s @ e @ np.linalg.inv(s)
    return GeneratedRetraction(
        p,
        {
            "family": "similarity_cluster",
            "n": int(n),
            "rank": int(rank),
            "amp": float(amp),
            "condition_number": cond,
        },
    )


def random_similarity_retraction(
    n: int,
    rank: int,
    amp: float,
    seed: int,
) -> GeneratedRetraction:
    direction = row_sum_zero_direction(n, seed)
    generated = similarity_retraction(n, rank, direction, amp)
    generated.metadata["seed"] = int(seed)
    return generated


def scale_direction_to_delta(
    n: int,
    rank: int,
    direction: np.ndarray,
    target_delta: float,
    max_amp: float,
    steps: int = 36,
) -> GeneratedRetraction:
    if target_delta < 0:
        raise ValueError("target_delta must be nonnegative")

    def try_amp(amp: float) -> tuple[float, GeneratedRetraction | None]:
        try:
            generated = similarity_retraction(n, rank, direction, amp)
        except np.linalg.LinAlgError:
            return math.inf, None
        return max_negative_mass(generated.matrix), generated

    lo = 0.0
    hi = max_amp
    hi_delta, hi_gen = try_amp(hi)
    if not math.isfinite(hi_delta):
        hi = max_amp / 2.0
        hi_delta, hi_gen = try_amp(hi)

    if hi_gen is None:
        raise np.linalg.LinAlgError("similarity matrix singular at search amplitudes")

    if hi_delta <= target_delta:
        hi_gen.metadata["target_delta"] = float(target_delta)
        hi_gen.metadata["delta_scaling_status"] = "max_amp_below_target"
        return hi_gen

    best = hi_gen
    for _ in range(steps):
        mid = 0.5 * (lo + hi)
        mid_delta, mid_gen = try_amp(mid)
        if mid_gen is None or mid_delta > target_delta:
            hi = mid
        else:
            lo = mid
            best = mid_gen

    best.metadata["target_delta"] = float(target_delta)
    best.metadata["delta_scaling_status"] = "binary_search_under_target"
    return best
