"""Direct exact-retraction generators for op-exposed-hull searches.

The constructors here enforce P=A B and B A=I by construction.  They are
numerical evidence tools only; exact proof work must be done separately.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from exposed_hull import max_negative_mass, retraction_errors


@dataclass
class DirectRetraction:
    matrix: np.ndarray
    a_matrix: np.ndarray
    b_matrix: np.ndarray
    metadata: dict


def balanced_labels(n: int, rank: int) -> np.ndarray:
    labels = np.empty(n, dtype=int)
    for label, chunk in enumerate(np.array_split(np.arange(n), rank)):
        labels[chunk] = label
    return labels


def orthogonal_left_inverse(a: np.ndarray) -> np.ndarray:
    gram = a.T @ a
    return np.linalg.solve(gram, a.T)


def make_retraction(a: np.ndarray, b: np.ndarray, metadata: dict) -> DirectRetraction:
    p = a @ b
    meta = dict(metadata)
    meta["rank_numeric"] = int(np.linalg.matrix_rank(p, tol=1e-9))
    meta["delta"] = max_negative_mass(p)
    meta["errors"] = retraction_errors(p)
    meta["BA_error_linf"] = float(np.max(np.abs(b @ a - np.eye(a.shape[1]))))
    return DirectRetraction(p, a, b, meta)


def anchor_barycentric_retraction(
    n: int,
    rank: int,
    target_delta: float,
    seed: int,
    outside_probability: float = 0.65,
) -> DirectRetraction:
    """Generate P from barycentric rows with the first rank rows as anchors.

    A is the n x rank matrix of affine coefficients.  B selects the first
    rank coordinates, so B A=I exactly when the first rank rows of A are I.
    Row sums of A equal one, hence P1=1.
    """
    if not (1 <= rank <= n):
        raise ValueError("rank must satisfy 1 <= rank <= n")

    rng = np.random.default_rng(seed)
    a = np.zeros((n, rank))
    a[:rank, :] = np.eye(rank)
    for row in range(rank, n):
        if rng.random() < outside_probability and rank > 1 and target_delta > 0.0:
            omitted = int(rng.integers(rank))
            weights = rng.dirichlet(np.ones(rank - 1))
            amount = float(target_delta * rng.beta(2.0, 1.5))
            coeff = np.zeros(rank)
            coeff[omitted] = -amount
            coeff[[j for j in range(rank) if j != omitted]] = (1.0 + amount) * weights
        else:
            coeff = rng.dirichlet(np.ones(rank))
        a[row] = coeff

    b = np.zeros((rank, n))
    b[:, :rank] = np.eye(rank)
    return make_retraction(
        a,
        b,
        {
            "family": "direct_anchor_barycentric",
            "n": int(n),
            "rank": int(rank),
            "seed": int(seed),
            "target_delta": float(target_delta),
            "outside_probability": float(outside_probability),
        },
    )


def cluster_affine_basis(n: int, rank: int, noise: float, seed: int) -> np.ndarray:
    """Affine basis [1,U] near a stochastic cluster projection range."""
    rng = np.random.default_rng(seed)
    labels = balanced_labels(n, rank)
    indicators = np.zeros((n, rank))
    indicators[np.arange(n), labels] = 1.0
    centered = indicators - indicators.mean(axis=0, keepdims=True)
    u, s, _ = np.linalg.svd(centered, full_matrices=False)
    features = u[:, : rank - 1] * s[: rank - 1]
    if noise > 0.0:
        features = features + noise * rng.normal(size=features.shape)
    features = features - features.mean(axis=0, keepdims=True)
    return np.column_stack([np.ones(n), features])


def free_left_inverse_retraction(
    n: int,
    rank: int,
    target_delta: float,
    seed: int,
    feature_noise: float,
    max_amp: float,
    amp_grid: int = 24,
) -> DirectRetraction:
    """Perturb a left inverse while preserving B A=I and P1=1."""
    if not (1 <= rank <= n):
        raise ValueError("rank must satisfy 1 <= rank <= n")
    if amp_grid < 2:
        raise ValueError("amp_grid must be at least 2")

    rng = np.random.default_rng(seed)
    a = cluster_affine_basis(n, rank, feature_noise, seed)
    b0 = orthogonal_left_inverse(a)
    nproj = np.eye(n) - a @ b0
    direction = rng.normal(size=(rank, n)) @ nproj
    norm = np.max(np.abs(a @ direction))
    if norm > 0.0:
        direction = direction / norm

    def delta_at(amp: float) -> float:
        return max_negative_mass(a @ (b0 + amp * direction))

    best_amp = 0.0
    best_delta = delta_at(0.0)
    scaling_status = "base_above_target"
    if best_delta <= target_delta + 1e-12:
        hi_delta = delta_at(max_amp)
        if hi_delta <= target_delta + 1e-12:
            best_amp = float(max_amp)
            best_delta = float(hi_delta)
            scaling_status = "max_amp_under_target"
        else:
            lo = 0.0
            hi = float(max_amp)
            for _ in range(max(amp_grid, 24)):
                mid = 0.5 * (lo + hi)
                mid_delta = delta_at(mid)
                if mid_delta <= target_delta + 1e-12:
                    lo = mid
                    best_amp = float(mid)
                    best_delta = float(mid_delta)
                else:
                    hi = mid
            scaling_status = "binary_search_under_target"

    b = b0 + best_amp * direction
    generated = make_retraction(
        a,
        b,
        {
            "family": "direct_free_left_inverse",
            "n": int(n),
            "rank": int(rank),
            "seed": int(seed),
            "target_delta": float(target_delta),
            "feature_noise": float(feature_noise),
            "max_amp": float(max_amp),
            "chosen_amp": float(best_amp),
            "amp_grid": int(amp_grid),
            "base_delta": float(max_negative_mass(a @ b0)),
            "delta_scaling_status": scaling_status,
            "direction_output_norm": float(norm),
        },
    )
    return generated
