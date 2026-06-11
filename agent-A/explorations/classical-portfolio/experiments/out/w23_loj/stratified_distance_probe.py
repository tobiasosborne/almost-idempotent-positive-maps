#!/usr/bin/env python3
"""Numerics for the repaired stratified distance-to-HM-locus estimate.

The probe works in the exact w18 graph chart around an H-M base point P0.
For each sampled variety point P(C,D), it minimizes chart distance to the
local delta=0 locus by enumerating the locally reachable H-M support profiles:
pure transient rows may either remain transient or be promoted into the
matching recurrent block.  This is the support-addition move that refuted the
fixed-stratum estimate in w22_jet.
"""

from __future__ import annotations

import itertools
import json
import math
from dataclasses import asdict, dataclass
from typing import Iterable

import numpy as np
from scipy.linalg import null_space, orth
from scipy.optimize import minimize


def delta(P: np.ndarray) -> float:
    return float(np.max(np.sum(np.maximum(-P, 0.0), axis=1)))


def row_stoch_err(P: np.ndarray) -> float:
    return float(np.max(np.abs(P.sum(axis=1) - 1.0)))


def idem_err(P: np.ndarray) -> float:
    return float(np.max(np.abs(P @ P - P)))


def simplex_l1_dist_to_simplex(x: np.ndarray) -> float:
    """Euclidean distance to the probability simplex, squared.

    Used only for a cheap sanity check in rank-one comments; the actual probe
    uses nonlinear H-M profile fitting.
    """

    if len(x) == 1:
        return float((x[0] - 1.0) ** 2)
    u = np.sort(x)[::-1]
    cssv = np.cumsum(u) - 1.0
    ind = np.arange(1, len(x) + 1)
    cond = u - cssv / ind > 0
    rho = ind[cond][-1]
    theta = cssv[cond][-1] / rho
    y = np.maximum(x - theta, 0.0)
    return float(np.sum((x - y) ** 2))


@dataclass
class HMBase:
    name: str
    n: int
    k: int
    blocks: list[list[int]]
    transients: list[int]
    pis: list[list[float]]
    alpha: dict[int, list[float]]
    P0: list[list[float]]


@dataclass(frozen=True)
class Profile:
    name: str
    blocks: tuple[tuple[int, ...], ...]
    transients: tuple[int, ...]


@dataclass
class ChartSetup:
    S: np.ndarray
    Sinv: np.ndarray
    k: int
    m: int
    one_E: np.ndarray


@dataclass
class FitResult:
    profile: str
    dist2: float
    success: bool
    objective: float
    nit: int


@dataclass
class Record:
    kind: str
    base: str
    scale: float
    sample: int
    delta: float
    dist2: float
    ratio: str
    best_profile: str
    fit_success: bool
    row_stoch_err: float
    idem_err: float


def build_p0(
    n: int,
    blocks: list[list[int]],
    transients: list[int],
    pis: list[np.ndarray],
    alpha: dict[int, np.ndarray],
) -> np.ndarray:
    P = np.zeros((n, n), dtype=float)
    for s, block in enumerate(blocks):
        row = np.zeros(n, dtype=float)
        row[block] = pis[s]
        for i in block:
            P[i] = row
    for i in transients:
        row = np.zeros(n, dtype=float)
        for s, block in enumerate(blocks):
            row[block] += alpha[i][s] * pis[s]
        P[i] = row
    return P


def make_base(
    name: str,
    n: int,
    blocks: list[list[int]],
    transients: list[int],
    pis_raw: list[list[float]],
    alpha_raw: dict[int, list[float]],
) -> HMBase:
    pis = [np.array(p, dtype=float) for p in pis_raw]
    alpha = {i: np.array(a, dtype=float) for i, a in alpha_raw.items()}
    P0 = build_p0(n, blocks, transients, pis, alpha)
    return HMBase(
        name=name,
        n=n,
        k=len(blocks),
        blocks=[list(b) for b in blocks],
        transients=list(transients),
        pis=[list(map(float, p)) for p in pis],
        alpha={i: list(map(float, a)) for i, a in alpha.items()},
        P0=P0.tolist(),
    )


def deterministic_bases() -> list[HMBase]:
    return [
        make_base(
            "rank1_n2_boundary",
            2,
            [[0]],
            [1],
            [[1.0]],
            {1: [1.0]},
        ),
        make_base(
            "rank2_n3_pure_transient",
            3,
            [[0], [1]],
            [2],
            [[1.0], [1.0]],
            {2: [1.0, 0.0]},
        ),
        make_base(
            "rank2_n3_interior_transient",
            3,
            [[0], [1]],
            [2],
            [[1.0], [1.0]],
            {2: [0.4, 0.6]},
        ),
        make_base(
            "rank2_n4_block_and_face",
            4,
            [[0, 1], [2]],
            [3],
            [[0.35, 0.65], [1.0]],
            {3: [1.0, 0.0]},
        ),
        make_base(
            "rank2_n5_two_pure_additions",
            5,
            [[0, 1], [2]],
            [3, 4],
            [[0.25, 0.75], [1.0]],
            {3: [1.0, 0.0], 4: [0.0, 1.0]},
        ),
        make_base(
            "rank3_n5_mixed_boundary",
            5,
            [[0], [1, 2], [3]],
            [4],
            [[1.0], [0.2, 0.8], [1.0]],
            {4: [0.0, 0.55, 0.45]},
        ),
    ]


def chart_setup(P0: np.ndarray, k: int) -> ChartSetup:
    E = orth(P0)
    if E.shape[1] != k:
        raise ValueError(f"image rank mismatch: got {E.shape[1]}, expected {k}")
    F = null_space(P0)
    if F.shape[1] != P0.shape[0] - k:
        raise ValueError("kernel rank mismatch")
    S = np.column_stack([E, F])
    Sinv = np.linalg.inv(S)
    one_coords = Sinv @ np.ones(P0.shape[0])
    if np.linalg.norm(one_coords[k:]) > 1e-8:
        raise ValueError("row-stochastic one-vector not in image coordinates")
    return ChartSetup(S=S, Sinv=Sinv, k=k, m=P0.shape[0] - k, one_E=one_coords[:k])


def P_from_CD(setup: ChartSetup, C: np.ndarray, D: np.ndarray) -> np.ndarray:
    k, m = setup.k, setup.m
    R = np.linalg.inv(np.eye(k) + C @ D)
    top = np.column_stack([R, R @ C])
    bottom = np.column_stack([D @ R, D @ R @ C])
    Pcoord = np.vstack([top, bottom])
    return setup.S @ Pcoord @ setup.Sinv


def coords_from_P(setup: ChartSetup, P: np.ndarray) -> tuple[np.ndarray, np.ndarray] | None:
    k, m = setup.k, setup.m
    Q = setup.Sinv @ P @ setup.S
    R = Q[:k, :k]
    if abs(np.linalg.det(R)) < 1e-10:
        return None
    C = np.linalg.solve(R, Q[:k, k:])
    D = np.linalg.solve(R.T, Q[k:, :k].T).T
    if np.linalg.norm(D @ setup.one_E) > 1e-6:
        return None
    if C.shape != (k, m) or D.shape != (m, k):
        return None
    return C, D


def local_profiles(base: HMBase, pure_tol: float = 1e-10) -> list[Profile]:
    blocks0 = [tuple(b) for b in base.blocks]
    pure: list[tuple[int, int]] = []
    for i in base.transients:
        a = np.array(base.alpha[i], dtype=float)
        s = int(np.argmax(a))
        if a[s] >= 1.0 - pure_tol:
            pure.append((i, s))

    profiles: list[Profile] = []
    for mask in range(1 << len(pure)):
        blocks = [list(b) for b in blocks0]
        transients = set(base.transients)
        promoted: list[str] = []
        for bit, (i, s) in enumerate(pure):
            if mask & (1 << bit):
                blocks[s].append(i)
                transients.remove(i)
                promoted.append(f"{i}->C{s}")
        blocks = [tuple(sorted(b)) for b in blocks]
        name = "base" if not promoted else "promote_" + "_".join(promoted)
        profiles.append(Profile(name=name, blocks=tuple(blocks), transients=tuple(sorted(transients))))
    return profiles


class ProfileParam:
    def __init__(self, profile: Profile, k: int):
        self.profile = profile
        self.k = k
        self.slices: list[tuple[str, int, slice, int]] = []
        offset = 0
        for s, block in enumerate(profile.blocks):
            m = len(block)
            if m > 1:
                self.slices.append(("pi", s, slice(offset, offset + m), m))
                offset += m
        for i in profile.transients:
            if k > 1:
                self.slices.append(("alpha", i, slice(offset, offset + k), k))
                offset += k
        self.dim = offset

    def constraints(self) -> list[dict]:
        cons: list[dict] = []
        for _kind, _idx, sl, _m in self.slices:
            cons.append({"type": "eq", "fun": lambda x, sl=sl: float(np.sum(x[sl]) - 1.0)})
        return cons

    def bounds(self) -> list[tuple[float, float]]:
        return [(0.0, 1.0)] * self.dim

    def unpack(self, x: np.ndarray) -> tuple[list[np.ndarray], dict[int, np.ndarray]]:
        pis: list[np.ndarray] = []
        alpha: dict[int, np.ndarray] = {}
        for block in self.profile.blocks:
            pis.append(np.ones(len(block), dtype=float))
        for i in self.profile.transients:
            alpha[i] = np.ones(self.k, dtype=float) / self.k
        for kind, idx, sl, _m in self.slices:
            if kind == "pi":
                pis[idx] = np.array(x[sl], dtype=float)
            else:
                alpha[idx] = np.array(x[sl], dtype=float)
        return pis, alpha

    def vector_from_base(self, base: HMBase, eps: float = 0.0) -> np.ndarray:
        vals = np.zeros(self.dim, dtype=float)
        base_pi_by_state: dict[int, tuple[int, float]] = {}
        for s, block in enumerate(base.blocks):
            for pos, state in enumerate(block):
                base_pi_by_state[state] = (s, base.pis[s][pos])
        for kind, idx, sl, m in self.slices:
            if kind == "pi":
                block = self.profile.blocks[idx]
                raw = np.zeros(m, dtype=float)
                for pos, state in enumerate(block):
                    old = base_pi_by_state.get(state)
                    if old is not None and old[0] == idx:
                        raw[pos] = old[1]
                if eps > 0:
                    raw += eps
                if raw.sum() <= 0:
                    raw[:] = 1.0 / m
                else:
                    raw /= raw.sum()
                vals[sl] = raw
            else:
                if idx in base.alpha:
                    raw = np.array(base.alpha[idx], dtype=float)
                else:
                    raw = np.ones(self.k, dtype=float) / self.k
                if eps > 0:
                    raw = raw + eps
                    raw = raw / raw.sum()
                vals[sl] = raw
        return vals

    def random_vector(self, rng: np.random.Generator) -> np.ndarray:
        vals = np.zeros(self.dim, dtype=float)
        for _kind, _idx, sl, m in self.slices:
            raw = rng.gamma(1.0, 1.0, size=m)
            vals[sl] = raw / raw.sum()
        return vals


def build_profile_P(profile: Profile, k: int, param: ProfileParam, x: np.ndarray) -> np.ndarray:
    n = sum(len(b) for b in profile.blocks) + len(profile.transients)
    pis, alpha = param.unpack(x)
    return build_p0(n, [list(b) for b in profile.blocks], list(profile.transients), pis, alpha)


def fit_profile(
    setup: ChartSetup,
    base: HMBase,
    profile: Profile,
    target_C: np.ndarray,
    target_D: np.ndarray,
    rng: np.random.Generator,
    random_starts: int = 3,
) -> FitResult:
    param = ProfileParam(profile, base.k)

    def obj(x: np.ndarray) -> float:
        Q = build_profile_P(profile, base.k, param, x)
        coords = coords_from_P(setup, Q)
        if coords is None:
            return 1e6 + float(np.linalg.norm(Q - np.array(base.P0)) ** 2)
        Cq, Dq = coords
        return float(np.sum((Cq - target_C) ** 2) + np.sum((Dq - target_D) ** 2))

    starts = [param.vector_from_base(base, eps=0.0), param.vector_from_base(base, eps=1e-5)]
    starts.extend(param.random_vector(rng) for _ in range(random_starts))
    if param.dim == 0:
        value = obj(np.zeros(0, dtype=float))
        return FitResult(profile=profile.name, dist2=value, success=True, objective=value, nit=0)

    best: FitResult | None = None
    for x0 in starts:
        res = minimize(
            obj,
            x0,
            method="SLSQP",
            bounds=param.bounds(),
            constraints=param.constraints(),
            options={"maxiter": 250, "ftol": 1e-12, "disp": False},
        )
        value = float(res.fun)
        cand = FitResult(
            profile=profile.name,
            dist2=value,
            success=bool(res.success),
            objective=value,
            nit=int(res.nit),
        )
        if best is None or cand.dist2 < best.dist2:
            best = cand
    assert best is not None
    return best


def distance_to_local_hm(
    setup: ChartSetup,
    base: HMBase,
    target_C: np.ndarray,
    target_D: np.ndarray,
    rng: np.random.Generator,
) -> FitResult:
    fits = [
        fit_profile(setup, base, profile, target_C, target_D, rng)
        for profile in local_profiles(base)
    ]
    return min(fits, key=lambda r: r.dist2)


def ratio_string(num: float, den: float) -> str:
    if den <= 1e-15:
        if num <= 1e-14:
            return "0"
        return "inf"
    return f"{num / den:.17g}"


def random_CD(setup: ChartSetup, rng: np.random.Generator, scale: float) -> tuple[np.ndarray, np.ndarray]:
    C = scale * rng.normal(size=(setup.k, setup.m))
    D = scale * rng.normal(size=(setup.m, setup.k))
    e = setup.one_E
    denom = float(e @ e)
    for r in range(setup.m):
        D[r] -= (float(D[r] @ e) / denom) * e
    return C, D


def coords_for_matrix_or_raise(setup: ChartSetup, P: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    coords = coords_from_P(setup, P)
    if coords is None:
        raise RuntimeError("matrix is outside the local chart")
    return coords


def support_arc_records(rng: np.random.Generator) -> list[Record]:
    records: list[Record] = []

    base = deterministic_bases()[0]
    setup = chart_setup(np.array(base.P0, dtype=float), base.k)
    for sample, c in enumerate([-1e-3, -1e-5, 0.0, 1e-8, 1e-5, 1e-3]):
        P = np.array([[1.0 - c, c], [1.0 - c, c]], dtype=float)
        C, D = coords_for_matrix_or_raise(setup, P)
        fit = distance_to_local_hm(setup, base, C, D, rng)
        d = delta(P)
        records.append(
            Record(
                kind="support_rank1",
                base=base.name,
                scale=abs(c),
                sample=sample,
                delta=d,
                dist2=fit.dist2,
                ratio=ratio_string(fit.dist2, d),
                best_profile=fit.profile,
                fit_success=fit.success,
                row_stoch_err=row_stoch_err(P),
                idem_err=idem_err(P),
            )
        )

    base = deterministic_bases()[1]
    setup = chart_setup(np.array(base.P0, dtype=float), base.k)
    for sample, eps in enumerate([0.0, 1e-8, 1e-6, 1e-4, 1e-3]):
        P = np.array(
            [
                [1.0 - eps, 0.0, eps],
                [0.0, 1.0, 0.0],
                [1.0 - eps, 0.0, eps],
            ],
            dtype=float,
        )
        C, D = coords_for_matrix_or_raise(setup, P)
        fit = distance_to_local_hm(setup, base, C, D, rng)
        d = delta(P)
        records.append(
            Record(
                kind="support_rank2",
                base=base.name,
                scale=eps,
                sample=sample,
                delta=d,
                dist2=fit.dist2,
                ratio=ratio_string(fit.dist2, d),
                best_profile=fit.profile,
                fit_success=fit.success,
                row_stoch_err=row_stoch_err(P),
                idem_err=idem_err(P),
            )
        )

    return records


def random_records(rng: np.random.Generator) -> list[Record]:
    records: list[Record] = []
    bases = deterministic_bases()
    scales = [3e-4, 1e-3, 3e-3, 1e-2]
    sample_id = 0
    for base in bases:
        P0 = np.array(base.P0, dtype=float)
        setup = chart_setup(P0, base.k)
        for scale in scales:
            for _ in range(4):
                C, D = random_CD(setup, rng, scale)
                P = P_from_CD(setup, C, D)
                d = delta(P)
                fit = distance_to_local_hm(setup, base, C, D, rng)
                records.append(
                    Record(
                        kind="random_chart",
                        base=base.name,
                        scale=scale,
                        sample=sample_id,
                        delta=d,
                        dist2=fit.dist2,
                        ratio=ratio_string(fit.dist2, d),
                        best_profile=fit.profile,
                        fit_success=fit.success,
                        row_stoch_err=row_stoch_err(P),
                        idem_err=idem_err(P),
                    )
                )
                sample_id += 1
    return records


def summarize(records: Iterable[Record]) -> dict:
    recs = list(records)
    finite = [
        float(r.ratio)
        for r in recs
        if r.ratio not in {"inf", "0"} and math.isfinite(float(r.ratio))
    ]
    support = [r for r in recs if r.kind.startswith("support")]
    support_positive = [r for r in support if r.delta <= 1e-15 and r.scale > 0.0 and r.dist2 <= 1e-12]
    return {
        "records": len(recs),
        "finite_ratio_count": len(finite),
        "max_finite_dist2_over_delta": max(finite) if finite else None,
        "median_finite_dist2_over_delta": float(np.median(finite)) if finite else None,
        "infinite_ratio_count": sum(1 for r in recs if r.ratio == "inf"),
        "support_delta0_dist0_count": len(support_positive),
        "support_records": len(support),
        "max_idempotence_err": max(r.idem_err for r in recs),
        "max_row_stoch_err": max(r.row_stoch_err for r in recs),
        "worst_records": [
            asdict(r)
            for r in sorted(
                [r for r in recs if r.ratio not in {"inf", "0"}],
                key=lambda r: float(r.ratio),
                reverse=True,
            )[:10]
        ],
    }


def main() -> None:
    rng = np.random.default_rng(20260611)
    records = support_arc_records(rng) + random_records(rng)
    summary = summarize(records)

    with open("stratified_distance_results.json", "w", encoding="utf-8") as f:
        json.dump({"summary": summary, "records": [asdict(r) for r in records]}, f, indent=2)

    lines = [
        "w23_loj stratified distance-to-local-HM numerics",
        json.dumps(summary, indent=2),
        "",
        "kind base scale sample delta dist2 dist2/delta best_profile success idem_err",
    ]
    for r in records:
        lines.append(
            f"{r.kind} {r.base} {r.scale:.17g} {r.sample} {r.delta:.17g} "
            f"{r.dist2:.17g} {r.ratio} {r.best_profile} {r.fit_success} {r.idem_err:.3g}"
        )
    with open("stratified_distance_summary.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
