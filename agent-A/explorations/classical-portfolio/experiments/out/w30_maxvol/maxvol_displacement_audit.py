#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

import numpy as np


ROOT = Path("/home/tobias/Projects/almost-idempotent-positive-maps")
CP = ROOT / "agent-A/explorations/classical-portfolio"
OUT = Path("/tmp/codex-sigma-wall/w30_maxvol")


def scalar(x):
    if isinstance(x, (int, float)):
        return float(x)
    if isinstance(x, str):
        return float(Fraction(x))
    if isinstance(x, dict):
        if "str" in x:
            return float(Fraction(x["str"]))
        return float(Fraction(int(x["num"]), int(x["den"])))
    raise TypeError(type(x))


def matrix(obj):
    return np.array([[scalar(x) for x in row] for row in obj], dtype=float)


def neg_mass_rows(P):
    return np.maximum(-P, 0.0).sum(axis=1)


def rank(P, tol=1e-10):
    return int(np.linalg.matrix_rank(P, tol=tol))


def volume_score(rows):
    G = rows @ rows.T
    sign, logdet = np.linalg.slogdet(G)
    if sign <= 0:
        return -np.inf
    return 0.5 * logdet


def maxvol_pivots(P):
    n = P.shape[0]
    k = rank(P)
    best = None
    best_score = -np.inf
    for inds in itertools.combinations(range(n), k):
        rows = P[list(inds)]
        if rank(rows) < k:
            continue
        score = volume_score(rows)
        if score > best_score + 1e-12:
            best_score = score
            best = list(inds)
    if best is None:
        raise RuntimeError("no row basis found")
    return best


def coordinates(P, pivots):
    basis = P[pivots]
    coeffs = []
    for row in P:
        c, *_ = np.linalg.lstsq(basis.T, row, rcond=None)
        coeffs.append(c)
    return np.array(coeffs)


def ratio(num, den):
    num = float(num)
    den = float(den)
    if abs(den) < 1e-15:
        return "inf" if abs(num) >= 1e-15 else 0.0
    return float(num / den)


def fmt(x):
    if isinstance(x, str):
        return x
    return f"{float(x):.6g}"


def quantile(vals, q):
    if not vals:
        return 0.0
    idx = int(round(q * (len(vals) - 1)))
    return vals[idx]


def row_metrics(P, pivots, coeffs, s_pos):
    u = pivots[s_pos]
    row = P[u]
    pos = np.maximum(row, 0.0)
    delta = float(neg_mass_rows(P).max())
    R = 1.0 + 2.0 * delta
    dist = np.sum(np.abs(P - P[u]), axis=1)
    T = float(pos @ dist)

    e = np.zeros(len(pivots))
    e[s_pos] = 1.0
    dev = coeffs - e
    coeff_l1 = np.sum(np.abs(dev), axis=1)
    lambda_loss = 1.0 - coeffs[:, s_pos]
    off = np.delete(coeffs, s_pos, axis=1)
    mu = np.maximum(-off, 0.0).sum(axis=1)
    off_abs = np.sum(np.abs(off), axis=1)

    basis = P[pivots]
    basis_diam_s = float(np.max(np.sum(np.abs(basis - basis[s_pos]), axis=1)))
    basis_diam = float(
        max(
            np.sum(np.abs(basis[a] - basis[b]))
            for a in range(len(pivots))
            for b in range(len(pivots))
        )
    )

    lambda_avg = float(pos @ lambda_loss)
    mu_avg = float(pos @ mu)
    coeff_l1_avg = float(pos @ coeff_l1)
    off_abs_avg = float(pos @ off_abs)

    signed_coord_resid = row @ dev
    geom_bound = basis_diam_s * off_abs_avg
    crude_bound = R * coeff_l1_avg
    proved_part_bound = basis_diam_s * lambda_avg
    missing_part_bound = 2.0 * basis_diam_s * mu_avg

    # Volume ratio when replacing pivot s by row j is |a_s(j)|.  Rows with
    # a_s(j)=1 are invisible to the swap test even if transverse coordinates move.
    face_mask = np.abs(coeffs[:, s_pos] - 1.0) <= 1e-9
    face_T = float(pos[face_mask] @ dist[face_mask])
    face_mu = float(pos[face_mask] @ mu[face_mask])

    return {
        "pivot": int(u),
        "pivot_position": int(s_pos),
        "T": T,
        "T_over_delta": ratio(T, delta),
        "basis_diam_s": basis_diam_s,
        "basis_diam": basis_diam,
        "lambda_avg": lambda_avg,
        "lambda_avg_over_delta": ratio(lambda_avg, delta),
        "mu_avg": mu_avg,
        "mu_avg_over_delta": ratio(mu_avg, delta),
        "coeff_l1_avg": coeff_l1_avg,
        "coeff_l1_avg_over_delta": ratio(coeff_l1_avg, delta),
        "off_abs_avg": off_abs_avg,
        "off_abs_avg_over_delta": ratio(off_abs_avg, delta),
        "signed_coord_resid_linf": float(np.max(np.abs(signed_coord_resid))),
        "geom_bound": geom_bound,
        "geom_bound_minus_T": geom_bound - T,
        "crude_bound": crude_bound,
        "crude_bound_minus_T": crude_bound - T,
        "proved_part_bound": proved_part_bound,
        "missing_part_bound": missing_part_bound,
        "face_T_at_a_s_eq_1": face_T,
        "face_T_over_delta": ratio(face_T, delta),
        "face_mu": face_mu,
        "face_mu_over_delta": ratio(face_mu, delta),
        "positive_mass": float(pos.sum()),
    }


def audit_instance(name, P):
    P = np.asarray(P, dtype=float)
    pivots = maxvol_pivots(P)
    coeffs = coordinates(P, pivots)
    rows = [row_metrics(P, pivots, coeffs, s) for s in range(len(pivots))]
    delta = float(neg_mass_rows(P).max())
    return {
        "name": name,
        "n": int(P.shape[0]),
        "rank": rank(P),
        "delta": delta,
        "pivots": [int(x) for x in pivots],
        "idempotence_inf": float(np.max(np.abs(P @ P - P))),
        "rowsum_inf": float(np.max(np.abs(P.sum(axis=1) - 1.0))),
        "max_abs_coeff": float(np.max(np.abs(coeffs))),
        "max_coeff_neg_mass": float(np.maximum(-coeffs, 0.0).sum(axis=1).max()),
        "pivot_rows": rows,
    }


def leakage_family(delta):
    eta = np.sqrt(delta)
    mass = delta / eta
    B = np.array(
        [
            [1.0 - mass + delta, -delta, mass],
            [0.0, 1.0, 0.0],
        ]
    )
    L = np.array(
        [
            [1.0, 0.0],
            [0.0, 1.0],
            [1.0 - eta, eta],
        ]
    )
    return L @ B


def split_block(eps):
    q1 = np.array([0.5, 0.5 + eps, -eps])
    q2 = np.array([1.0 / (2.0 * (1.0 + 2.0 * eps)), 0.5, eps / (1.0 + 2.0 * eps)])
    q3 = np.array([0.0, 0.0, 1.0])
    return np.vstack([q1, q2, q3])


def leftcone(eps):
    return np.array(
        [
            [1 - eps / 3, -eps / 3, -eps / 3, eps],
            [eps / 3, 1 + eps / 3, eps / 3, -eps],
            [0.0, 0.0, 1.0, 0.0],
            [1 / 3, 1 / 3, 1 / 3, 0.0],
        ]
    )


def transverse_pair(a, m):
    c = a / (1.0 + 4.0 * a * a)
    B0 = np.array([1.0 - m, 0.0, 0.0, m / 2.0, m / 2.0])
    B1 = np.array([0.0, 1.0 - 2.0 * a * c, 2.0 * a * c, c, -c])
    B2 = np.array([0.0, 2.0 * a * c, 1.0 - 2.0 * a * c, -c, c])
    B = np.vstack([B0, B1, B2])
    L = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [1.0, a, -a],
            [1.0, -a, a],
        ]
    )
    return L @ B


def load_w16():
    path = CP / "experiments/out/w16_cert_audit/w16_best_rational_instance.json"
    return matrix(json.loads(path.read_text())["P_frac"])


def load_w17(fname):
    path = CP / f"experiments/out/w17_cert_audit/{fname}"
    return matrix(json.loads(path.read_text())["P"])


def random_hm(n, k, rng):
    blocks = [[] for _ in range(k)]
    for s in range(k):
        blocks[s].append(s)
    for j in range(k, n):
        blocks[int(rng.integers(k))].append(j)
    P = np.zeros((n, n))
    for block in blocks:
        weights = rng.random(len(block)) + 0.2
        weights /= weights.sum()
        law = np.zeros(n)
        law[block] = weights
        for i in block:
            P[i] = law
    return P


def rowsum_zero_matrix(n, rng):
    K = rng.normal(size=(n, n))
    K -= K.mean(axis=1, keepdims=True)
    norm = np.linalg.norm(K, ord=np.inf)
    return K / norm


def conjugate_to_delta(P0, target_delta, rng):
    K = rowsum_zero_matrix(P0.shape[0], rng)

    def make(t):
        S = np.eye(P0.shape[0]) + t * K
        return S @ P0 @ np.linalg.inv(S)

    lo, hi = 0.0, 1.0
    for _ in range(50):
        if neg_mass_rows(make(hi)).max() >= target_delta:
            break
        hi *= 2.0
    for _ in range(70):
        mid = 0.5 * (lo + hi)
        if neg_mass_rows(make(mid)).max() < target_delta:
            lo = mid
        else:
            hi = mid
    return make(hi)


def coordinate_projection(k, extra, amp, rng):
    coords = [np.eye(k)[s] for s in range(k)]
    for _ in range(extra):
        s = int(rng.integers(k))
        w = rng.normal(size=k)
        w -= w.mean()
        w /= max(np.max(np.abs(w)), 1e-12)
        x = np.eye(k)[s] + amp * w
        x -= (x.sum() - 1.0) / k
        if np.max(np.abs(x)) > 1.0:
            x = np.eye(k)[s] + (x - np.eye(k)[s]) / np.max(np.abs(x - np.eye(k)[s])) * amp
            x -= (x.sum() - 1.0) / k
        coords.append(x)
    L = np.array(coords)
    B = np.linalg.inv(L.T @ L) @ L.T
    return L @ B


def summarize(records):
    lines = []
    for rec in records:
        if rec["name"].endswith("_summary"):
            rows = rec["pivot_rows"]
            t = sorted(float(r["T_over_delta"]) for r in rows if not isinstance(r["T_over_delta"], str))
            mu = sorted(float(r["mu_avg_over_delta"]) for r in rows if not isinstance(r["mu_avg_over_delta"], str))
            face = sorted(float(r["face_T_over_delta"]) for r in rows if not isinstance(r["face_T_over_delta"], str))
            lines.append(
                f"{rec['name']}: pivot_rows={len(rows)} "
                f"max_T/delta={max(t):.6g} p90_T/delta={quantile(t, 0.9):.6g} "
                f"max_mu/delta={max(mu):.6g} p90_mu/delta={quantile(mu, 0.9):.6g} "
                f"max_face_T/delta={max(face):.6g}"
            )
            continue
        worst = max(rec["pivot_rows"], key=lambda r: float(r["T_over_delta"]) if not isinstance(r["T_over_delta"], str) else np.inf)
        mut = max(rec["pivot_rows"], key=lambda r: float(r["mu_avg_over_delta"]) if not isinstance(r["mu_avg_over_delta"], str) else np.inf)
        facet = max(rec["pivot_rows"], key=lambda r: float(r["face_T_over_delta"]) if not isinstance(r["face_T_over_delta"], str) else np.inf)
        lines.append(
            f"{rec['name']}: n={rec['n']} rank={rec['rank']} delta={rec['delta']:.8g} "
            f"pivots={rec['pivots']} maxcoeff={rec['max_abs_coeff']:.6g} "
            f"worst={worst['pivot']} T/delta={fmt(worst['T_over_delta'])} "
            f"lambda/delta={fmt(worst['lambda_avg_over_delta'])} "
            f"mu/delta={fmt(worst['mu_avg_over_delta'])} "
            f"maxmu={mut['pivot']} max_mu/delta={fmt(mut['mu_avg_over_delta'])} "
            f"maxface={facet['pivot']} max_faceT/delta={fmt(facet['face_T_over_delta'])} "
            f"geom_slack={worst['geom_bound_minus_T']:.3g} "
            f"coord_resid={worst['signed_coord_resid_linf']:.3g} "
            f"idem={rec['idempotence_inf']:.3g}"
        )
    return "\n".join(lines) + "\n"


def main():
    records = []
    for delta in [1e-2, 1e-3, 1e-4, 1e-5]:
        records.append(audit_instance(f"w27_rank2_leakage_delta_{delta:g}", leakage_family(delta)))
    for eps in [1e-2, 1e-3, 1e-4, 1e-5]:
        records.append(audit_instance(f"split_block_eps_{eps:g}", split_block(eps)))
    for eps in [1e-2, 1e-3, 1e-4, 1e-5]:
        records.append(audit_instance(f"w19_leftcone_eps_{eps:g}", leftcone(eps)))
    for a in [0.01, 0.02, 0.05, 0.1, 0.2]:
        records.append(audit_instance(f"transverse_pair_a_{a:g}_m_0.99", transverse_pair(a, 0.99)))
    records.append(audit_instance("w16_best_rational_above_corner", load_w16()))
    records.append(audit_instance("w17_main_rational_above_corner", load_w17("main_rational_instance.json")))
    records.append(audit_instance("w17_robust_rational_above_corner", load_w17("robust_rational_instance.json")))

    rng = np.random.default_rng(3007)
    conj_rows = []
    for target in [1e-2, 1e-3, 1e-4]:
        for trial in range(16):
            P = conjugate_to_delta(random_hm(8, 3, rng), target, rng)
            conj_rows.extend(audit_instance(f"conj_{target:g}_{trial}", P)["pivot_rows"])
    records.append({"name": "random_hm_conjugation_summary", "pivot_rows": conj_rows})

    coord_rows = []
    for k in [3, 4, 5, 6]:
        for amp in [0.01, 0.03, 0.08, 0.15]:
            for trial in range(10):
                P = coordinate_projection(k, 2 * k, amp, rng)
                rec = audit_instance(f"coord_k{k}_amp{amp:g}_{trial}", P)
                if rec["delta"] > 1e-10:
                    coord_rows.extend(rec["pivot_rows"])
    records.append({"name": "random_coordinate_projection_summary", "pivot_rows": coord_rows})

    (OUT / "maxvol_displacement_results.json").write_text(json.dumps(records, indent=2, sort_keys=True))
    summary = summarize(records)
    (OUT / "maxvol_displacement_summary.txt").write_text(summary)
    print(summary, end="")


if __name__ == "__main__":
    main()
