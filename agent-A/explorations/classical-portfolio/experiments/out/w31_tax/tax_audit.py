#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

import numpy as np


ROOT = Path("/home/tobias/Projects/almost-idempotent-positive-maps")
CP = ROOT / "agent-A/explorations/classical-portfolio"
OUT = Path("/tmp/codex-sigma-wall/w31_tax")


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
    gram = rows @ rows.T
    sign, logdet = np.linalg.slogdet(gram)
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


def tax_split(P, pivots, coeffs, s_pos, eta):
    u = pivots[s_pos]
    pos = np.maximum(P[u], 0.0)
    foreign = np.delete(coeffs, s_pos, axis=1)
    mu = np.maximum(-foreign, 0.0).sum(axis=1)
    contrib = pos * mu
    dist_to_pivots = np.array(
        [np.sum(np.abs(P - P[pivot]), axis=1) for pivot in pivots]
    ).T
    in_cluster = dist_to_pivots <= eta + 1e-12
    own = in_cluster[:, s_pos]
    foreign_cluster = np.any(np.delete(in_cluster, s_pos, axis=1), axis=1)
    any_cluster = np.any(in_cluster, axis=1)
    top = []
    for j in np.argsort(-contrib)[:8]:
        if contrib[j] <= 1e-14:
            continue
        if own[j]:
            bucket = "own"
        elif foreign_cluster[j]:
            bucket = "foreign"
        elif any_cluster[j]:
            bucket = "other"
        else:
            bucket = "B_eta"
        top.append(
            {
                "j": int(j),
                "bucket": bucket,
                "P_u_j_pos": float(pos[j]),
                "mu": float(mu[j]),
                "tax_contrib": float(contrib[j]),
                "coeff": [float(x) for x in coeffs[j]],
                "dist_to_pivots": [float(x) for x in dist_to_pivots[j]],
            }
        )
    return {
        "pivot": int(u),
        "s_pos": int(s_pos),
        "tax": float(contrib.sum()),
        "own_cluster_tax": float(contrib[own].sum()),
        "foreign_cluster_tax": float(contrib[foreign_cluster].sum()),
        "B_eta_tax": float(contrib[~any_cluster].sum()),
        "top_tax_columns": top,
    }


def ratio(num, den):
    if abs(den) < 1e-15:
        return "inf" if abs(num) >= 1e-15 else 0.0
    return float(num / den)


def audit_instance(name, P, eta=None):
    P = np.asarray(P, dtype=float)
    delta = float(neg_mass_rows(P).max())
    eta = float(np.sqrt(delta) if eta is None and delta > 0 else (eta or 0.0))
    pivots = maxvol_pivots(P)
    coeffs = coordinates(P, pivots)
    rows = []
    for s in range(len(pivots)):
        split = tax_split(P, pivots, coeffs, s, eta)
        split["tax_over_delta"] = ratio(split["tax"], delta)
        split["own_over_delta"] = ratio(split["own_cluster_tax"], delta)
        split["foreign_over_delta"] = ratio(split["foreign_cluster_tax"], delta)
        split["B_eta_over_delta"] = ratio(split["B_eta_tax"], delta)
        rows.append(split)
    return {
        "name": name,
        "n": int(P.shape[0]),
        "rank": rank(P),
        "delta": delta,
        "eta": eta,
        "pivots": [int(x) for x in pivots],
        "idempotence_inf": float(np.max(np.abs(P @ P - P))),
        "rowsum_inf": float(np.max(np.abs(P.sum(axis=1) - 1.0))),
        "max_abs_coeff": float(np.max(np.abs(coeffs))),
        "rows": rows,
    }


def split_block(eps):
    q1 = np.array([0.5, 0.5 + eps, -eps])
    q2 = np.array([1.0 / (2.0 * (1.0 + 2.0 * eps)), 0.5, eps / (1.0 + 2.0 * eps)])
    q3 = np.array([0.0, 0.0, 1.0])
    return np.vstack([q1, q2, q3])


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
    for _ in range(60):
        if neg_mass_rows(make(hi)).max() >= target_delta:
            break
        hi *= 2.0
    for _ in range(80):
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
        coords.append(x)
    L = np.array(coords)
    B = np.linalg.inv(L.T @ L) @ L.T
    return L @ B


def fmt_ratio(x):
    return x if isinstance(x, str) else f"{x:.6g}"


def summarize(records):
    lines = []
    for rec in records:
        worst = max(
            rec["rows"],
            key=lambda r: float(r["tax_over_delta"])
            if not isinstance(r["tax_over_delta"], str)
            else np.inf,
        )
        lines.append(
            f"{rec['name']}: n={rec['n']} rank={rec['rank']} "
            f"delta={rec['delta']:.8g} eta={rec['eta']:.8g} pivots={rec['pivots']} "
            f"maxcoeff={rec['max_abs_coeff']:.6g} worst_pivot={worst['pivot']} "
            f"tax/delta={fmt_ratio(worst['tax_over_delta'])} "
            f"own/delta={fmt_ratio(worst['own_over_delta'])} "
            f"foreign/delta={fmt_ratio(worst['foreign_over_delta'])} "
            f"B_eta/delta={fmt_ratio(worst['B_eta_over_delta'])}"
        )
        for item in worst["top_tax_columns"][:3]:
            lines.append(
                f"  top j={item['j']} bucket={item['bucket']} "
                f"pos={item['P_u_j_pos']:.6g} mu={item['mu']:.6g} "
                f"contrib/delta={ratio(item['tax_contrib'], rec['delta']):.6g} "
                f"coeff={[round(x, 6) for x in item['coeff']]}"
            )
    return "\n".join(lines) + "\n"


def main():
    records = []
    for delta in [1e-2, 1e-3, 1e-4, 1e-5]:
        records.append(audit_instance(f"rank2_leakage_delta_{delta:g}", leakage_family(delta)))
    for eps in [1e-2, 1e-3, 1e-4, 1e-5]:
        records.append(audit_instance(f"split_block_eps_{eps:g}", split_block(eps)))
    for a in [0.01, 0.02, 0.05, 0.1, 0.2]:
        records.append(audit_instance(f"transverse_pair_a_{a:g}_m_0.99", transverse_pair(a, 0.99)))
    records.append(audit_instance("w16_best_rational", load_w16()))
    records.append(audit_instance("w17_main_rational", load_w17("main_rational_instance.json")))
    records.append(audit_instance("w17_robust_rational", load_w17("robust_rational_instance.json")))

    rng = np.random.default_rng(31131)
    for target in [1e-2, 1e-3, 1e-4]:
        best = None
        for trial in range(40):
            rec = audit_instance(
                f"random_conjugated_hm_delta_{target:g}_trial_{trial}",
                conjugate_to_delta(random_hm(8, 3, rng), target, rng),
            )
            row = max(
                rec["rows"],
                key=lambda r: float(r["tax_over_delta"])
                if not isinstance(r["tax_over_delta"], str)
                else -np.inf,
            )
            val = float(row["tax_over_delta"])
            if best is None or val > best[0]:
                best = (val, rec)
        records.append(best[1])

    for k in [3, 4, 5, 6]:
        best = None
        for amp in [0.01, 0.03, 0.08, 0.15]:
            for trial in range(30):
                rec = audit_instance(
                    f"random_coordinate_projection_k_{k}_amp_{amp:g}_trial_{trial}",
                    coordinate_projection(k, 2 * k, amp, rng),
                )
                if rec["delta"] < 1e-12:
                    continue
                row = max(
                    rec["rows"],
                    key=lambda r: float(r["tax_over_delta"])
                    if not isinstance(r["tax_over_delta"], str)
                    else -np.inf,
                )
                val = float(row["tax_over_delta"])
                if best is None or val > best[0]:
                    best = (val, rec)
        if best is not None:
            records.append(best[1])

    (OUT / "tax_audit_results.json").write_text(json.dumps(records, indent=2, sort_keys=True))
    summary = summarize(records)
    (OUT / "tax_audit_summary.txt").write_text(summary)
    print(summary, end="")


if __name__ == "__main__":
    main()
