#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

import numpy as np


ROOT = Path("/home/tobias/Projects/almost-idempotent-positive-maps")
CP = ROOT / "agent-A/explorations/classical-portfolio"
OUT = Path("/tmp/codex-sigma-wall/w30_telescope")


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
    laws = []
    for block in blocks:
        weights = rng.random(len(block)) + 0.2
        weights = weights / weights.sum()
        law = np.zeros(n)
        law[block] = weights
        laws.append(law)
    for s, block in enumerate(blocks):
        for i in block:
            P[i] = laws[s]
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
    for _ in range(40):
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


def row_audit(P, u, coeffs, pivot_position):
    delta = float(neg_mass_rows(P).max())
    R = 1.0 + 2.0 * delta
    D = 2.0 * R
    Ppos = np.maximum(P, 0.0)
    Pneg = np.maximum(-P, 0.0)
    a = Ppos[u]
    f = np.sum(np.abs(P - P[u]), axis=1)
    T = float(a @ f)
    sub_rhs = Ppos @ f + D * neg_mass_rows(P)
    sub_slack = sub_rhs - f
    two = a @ Ppos
    S2 = float(two @ f)
    b = Pneg[u]
    neg_return_T = float(b @ f)
    a_neg_f = float(a @ Pneg @ f)
    b_pos_f = float(b @ Ppos @ f)
    b_neg_f = float(b @ Pneg @ f)
    decomp_rhs = T - neg_return_T + a_neg_f + b_pos_f - b_neg_f
    err = float(D * (a @ neg_mass_rows(P)))
    signed_return = P[u] @ P
    signed_return_inf = float(np.max(np.abs(signed_return - P[u])))

    lam = 1.0 - coeffs[:, pivot_position]
    mu_off = np.maximum(-np.delete(coeffs, pivot_position, axis=1), 0.0).sum(axis=1)
    lam_pos_avg = float(a @ lam)
    mu_pos_avg = float(a @ mu_off)
    coord_bound_rhs = float(2.0 * R * (lam_pos_avg + mu_pos_avg))

    iter_vals = []
    kernel = a.copy()
    for m in range(1, 9):
        kernel = kernel @ Ppos
        iter_vals.append(float(kernel @ f))

    eta = float(np.sqrt(delta)) if delta > 0 else 0.0
    near = f <= eta + 1e-12
    off_mass = float(a[~near].sum())
    off_T = float(a[~near] @ f[~near])
    near_T = float(a[near] @ f[near])

    return {
        "row": int(u),
        "delta": delta,
        "T": T,
        "T_over_delta": ratio(T, delta),
        "subharmonic_min_slack": float(np.min(sub_slack)),
        "subharmonic_max_violation": float(max(0.0, -np.min(sub_slack))),
        "two_step_positive_T": S2,
        "two_step_ratio_to_T": ratio(S2, T),
        "two_step_decomposition_residual": float(S2 - decomp_rhs),
        "negative_return_T": neg_return_T,
        "aPneg_f": a_neg_f,
        "bPpos_f": b_pos_f,
        "bPneg_f": b_neg_f,
        "two_step_error_bound": err,
        "two_step_inequality_slack": float(S2 + err - T),
        "signed_return_inf": signed_return_inf,
        "lambda_pos_average": lam_pos_avg,
        "lambda_pos_average_over_delta": ratio(lam_pos_avg, delta),
        "mu_pos_average": mu_pos_avg,
        "mu_pos_average_over_delta": ratio(mu_pos_avg, delta),
        "coordinate_bound_rhs": coord_bound_rhs,
        "coordinate_bound_slack": coord_bound_rhs - T,
        "eta": eta,
        "near_mass_at_eta": float(a[near].sum()),
        "off_mass_at_eta": off_mass,
        "near_T_at_eta": near_T,
        "off_T_at_eta": off_T,
        "markov_off_bound_T_over_eta": ratio(T, eta),
        "positive_iterate_T_values_m1_to_m8": iter_vals,
        "positive_iterate_ratios_to_T_m1_to_m8": [ratio(v, T) for v in iter_vals],
    }


def audit_instance(name, P):
    P = np.asarray(P, dtype=float)
    pivots = maxvol_pivots(P)
    coeffs = coordinates(P, pivots)
    rows = [row_audit(P, u, coeffs, s) for s, u in enumerate(pivots)]
    delta = float(neg_mass_rows(P).max())
    return {
        "name": name,
        "n": int(P.shape[0]),
        "rank": rank(P),
        "delta": delta,
        "rowsum_inf": float(np.max(np.abs(P.sum(axis=1) - 1.0))),
        "idempotence_inf": float(np.max(np.abs(P @ P - P))),
        "pivots": [int(u) for u in pivots],
        "max_abs_coeff": float(np.max(np.abs(coeffs))),
        "max_coeff_neg_mass": float(np.maximum(-coeffs, 0.0).sum(axis=1).max()),
        "pivot_rows": rows,
    }


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


def summarize(records):
    lines = []
    for rec in records:
        if rec["name"] == "random_small_delta_similarity_summary":
            rows = rec["pivot_rows"]
            ratios = sorted(float(r["T_over_delta"]) for r in rows)
            two = sorted(float(r["two_step_ratio_to_T"]) for r in rows if not isinstance(r["two_step_ratio_to_T"], str))
            mu = sorted(float(r["mu_pos_average_over_delta"]) for r in rows)
            lines.append(
                "random_small_delta_similarity_summary: "
                f"pivot_rows={len(rows)} "
                f"max_T/delta={max(ratios):.6g} median_T/delta={quantile(ratios, 0.5):.6g} "
                f"max_two_step_ratio={max(two):.6g} median_two_step_ratio={quantile(two, 0.5):.6g} "
                f"max_mu/delta={max(mu):.6g} median_mu/delta={quantile(mu, 0.5):.6g}"
            )
            continue
        worst = max(rec["pivot_rows"], key=lambda r: numeric(r["T_over_delta"]))
        leakiest = max(rec["pivot_rows"], key=lambda r: numeric(r["mu_pos_average_over_delta"]))
        lines.append(
            f"{rec['name']}: n={rec['n']} rank={rec['rank']} delta={rec['delta']:.8g} "
            f"pivots={rec['pivots']} max_abs_coeff={rec['max_abs_coeff']:.6g} "
            f"worst_pivot={worst['row']} T/delta={fmt(worst['T_over_delta'])} "
            f"S2/T={fmt(worst['two_step_ratio_to_T'])} "
            f"iter8/T={fmt(worst['positive_iterate_ratios_to_T_m1_to_m8'][-1])} "
            f"mu/delta={fmt(worst['mu_pos_average_over_delta'])} "
            f"lambda/delta={fmt(worst['lambda_pos_average_over_delta'])} "
            f"max_mu_pivot={leakiest['row']} max_mu/delta={fmt(leakiest['mu_pos_average_over_delta'])} "
            f"max_mu_lambda/delta={fmt(leakiest['lambda_pos_average_over_delta'])} "
            f"subviol={worst['subharmonic_max_violation']:.3g} "
            f"twoslack={worst['two_step_inequality_slack']:.3g} "
            f"idem={rec['idempotence_inf']:.3g}"
        )
    return "\n".join(lines) + "\n"


def numeric(x):
    if isinstance(x, str):
        return float("inf")
    return float(x)


def quantile(vals, q):
    if not vals:
        return 0.0
    idx = int(round(q * (len(vals) - 1)))
    return vals[idx]


def main():
    records = []
    for delta in [1e-2, 1e-3, 1e-4, 1e-5]:
        records.append(audit_instance(f"w27_rank2_leakage_delta_{delta:g}", leakage_family(delta)))
    for eps in [1e-2, 1e-3, 1e-4, 1e-5]:
        records.append(audit_instance(f"split_block_eps_{eps:g}", split_block(eps)))
    for eps in [1e-2, 1e-3, 1e-4, 1e-5]:
        records.append(audit_instance(f"w19_leftcone_eps_{eps:g}", leftcone(eps)))
    for a in [0.02, 0.05, 0.1, 0.2]:
        records.append(audit_instance(f"transverse_pair_a_{a:g}_m_0.99", transverse_pair(a, 0.99)))
    records.append(audit_instance("w16_best_rational_above_corner", load_w16()))
    records.append(audit_instance("w17_main_rational_above_corner", load_w17("main_rational_instance.json")))
    records.append(audit_instance("w17_robust_rational_above_corner", load_w17("robust_rational_instance.json")))

    rng = np.random.default_rng(3001)
    random_pivots = []
    for target in [1e-2, 1e-3, 1e-4]:
        for trial in range(12):
            P0 = random_hm(7, 3, rng)
            P = conjugate_to_delta(P0, target, rng)
            rec = audit_instance(f"random_similarity_delta_{target:g}_trial_{trial}", P)
            random_pivots.extend(rec["pivot_rows"])
    records.append({"name": "random_small_delta_similarity_summary", "pivot_rows": random_pivots})

    (OUT / "telescope_numeric_results.json").write_text(json.dumps(records, indent=2, sort_keys=True))
    summary = summarize(records)
    (OUT / "telescope_numeric_summary.txt").write_text(summary)
    print(summary, end="")


if __name__ == "__main__":
    main()
