import itertools
import json
from fractions import Fraction
from pathlib import Path

import numpy as np


ROOT = Path("/home/tobias/Projects/almost-idempotent-positive-maps")
CP = ROOT / "agent-A/explorations/classical-portfolio"
OUT = Path("/tmp/codex-sigma-wall/w28_face")


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


def rank(P, tol=1e-10):
    return int(np.linalg.matrix_rank(P, tol=tol))


def neg_mass_rows(P):
    return np.maximum(-P, 0.0).sum(axis=1)


def row_l1(P, Q):
    return np.sum(np.abs(P - Q), axis=1)


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


def pivot_ball_clusters(P, pivots, eta):
    clusters = []
    owner = {}
    for s, pivot in enumerate(pivots):
        members = [
            int(i)
            for i in range(P.shape[0])
            if np.sum(np.abs(P[i] - P[pivot])) <= eta + 1e-12
        ]
        clusters.append(members)
        for i in members:
            owner.setdefault(i, []).append(s)
    overlaps = {int(i): ss for i, ss in owner.items() if len(ss) > 1}
    covered = set(owner)
    b_eta = sorted(set(range(P.shape[0])) - covered)
    return clusters, b_eta, overlaps


def clip_probability_on_support(row, support):
    out = np.zeros_like(row)
    if not support:
        out[int(np.argmax(row))] = 1.0
        return out
    vals = np.maximum(row[support], 0.0)
    total = float(vals.sum())
    if total <= 0:
        out[support[0]] = 1.0
    else:
        out[support] = vals / total
    return out


def clip_simplex(a):
    pos = np.maximum(a, 0.0)
    total = float(pos.sum())
    if total <= 0:
        out = np.zeros_like(a)
        out[int(np.argmax(a))] = 1.0
        return out
    return pos / total


def hm_candidate(P, pivots, coeffs, clusters, b_eta):
    laws = [clip_probability_on_support(P[pivot], clusters[s]) for s, pivot in enumerate(pivots)]
    Q = np.zeros_like(P)
    for s, members in enumerate(clusters):
        for i in members:
            Q[i] = laws[s]
    for i in b_eta:
        lam = clip_simplex(coeffs[i])
        Q[i] = sum(lam[s] * laws[s] for s in range(len(laws)))
    return Q


def chart_metrics(name, P):
    delta = float(neg_mass_rows(P).max())
    eta = float(np.sqrt(delta)) if delta > 0 else 0.0
    denom = float(eta + delta / eta) if eta > 0 else 0.0
    pivots = maxvol_pivots(P)
    coeffs = coordinates(P, pivots)
    clusters, b_eta, overlaps = pivot_ball_clusters(P, pivots, eta)
    Q = hm_candidate(P, pivots, coeffs, clusters, b_eta)
    all_cluster_indices = set().union(*[set(c) for c in clusters]) if clusters else set()
    rep_records = []
    row_neg = neg_mass_rows(P)
    for s, pivot in enumerate(pivots):
        own = set(clusters[s])
        outside_own = sorted(set(range(P.shape[0])) - own)
        other_clusters = sorted(all_cluster_indices - own)
        bset = sorted(set(b_eta))
        row = P[pivot]
        row_distances = np.sum(np.abs(P - P[pivot]), axis=1)
        off_l1 = float(np.abs(row[outside_own]).sum()) if outside_own else 0.0
        off_pos = float(np.maximum(row[outside_own], 0.0).sum()) if outside_own else 0.0
        rep_records.append(
            {
                "cluster_index": int(s),
                "pivot": int(pivot),
                "cluster_size": int(len(own)),
                "outside_own_l1": off_l1,
                "outside_own_positive": off_pos,
                "outside_own_l1_ratio": float(off_l1 / denom) if denom > 0 else 0.0,
                "other_clusters_l1": float(np.abs(row[other_clusters]).sum()) if other_clusters else 0.0,
                "B_eta_l1": float(np.abs(row[bset]).sum()) if bset else 0.0,
                "B_eta_positive": float(np.maximum(row[bset], 0.0).sum()) if bset else 0.0,
                "neg_mass": float(np.maximum(-row, 0.0).sum()),
                "positive_avg_row_displacement": float(np.maximum(row, 0.0) @ row_distances),
                "positive_weighted_successor_negativity": float(np.maximum(row, 0.0) @ row_neg),
            }
        )
    coeff_neg = np.maximum(-coeffs, 0.0).sum(axis=1)
    max_off_l1 = max((r["outside_own_l1"] for r in rep_records), default=0.0)
    hm_dist = float(row_l1(P, Q).max())
    return {
        "name": name,
        "n": int(P.shape[0]),
        "rank": rank(P),
        "delta": delta,
        "eta": eta,
        "denom_eta_plus_delta_over_eta": denom,
        "rowsum_inf": float(np.max(np.abs(P.sum(axis=1) - 1.0))),
        "idempotence_inf": float(np.max(np.abs(P @ P - P))),
        "pivots": [int(i) for i in pivots],
        "max_abs_coeff": float(np.max(np.abs(coeffs))),
        "max_coeff_neg_mass_all_rows": float(np.max(coeff_neg)),
        "max_coeff_neg_mass_B_eta": float(np.max(coeff_neg[b_eta])) if b_eta else 0.0,
        "clusters": clusters,
        "B_eta": b_eta,
        "overlaps": overlaps,
        "rep_records": rep_records,
        "target_max_offcluster_l1": max_off_l1,
        "target_ratio": float(max_off_l1 / denom) if denom > 0 else 0.0,
        "max_rep_positive_avg_row_displacement": float(
            max((r["positive_avg_row_displacement"] for r in rep_records), default=0.0)
        ),
        "max_rep_positive_avg_row_displacement_over_delta": float(
            max((r["positive_avg_row_displacement"] for r in rep_records), default=0.0) / delta
        )
        if delta > 0
        else 0.0,
        "max_rep_positive_weighted_successor_negativity": float(
            max((r["positive_weighted_successor_negativity"] for r in rep_records), default=0.0)
        ),
        "hm_candidate_max_row_l1": hm_dist,
        "hm_candidate_ratio": float(hm_dist / denom) if denom > 0 else 0.0,
    }


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


def leakage_family(delta):
    eta = np.sqrt(delta)
    eps = eta
    mass = delta / eps
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
            [1.0 - eps, eps],
        ]
    )
    return L @ B


def load_w16():
    path = CP / "experiments/out/w16_cert_audit/w16_best_rational_instance.json"
    data = json.loads(path.read_text())
    return matrix(data["P_frac"])


def load_w17(fname):
    path = CP / f"experiments/out/w17_cert_audit/{fname}"
    data = json.loads(path.read_text())
    return matrix(data["P"])


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
    for _ in range(30):
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


def summarize(records):
    lines = []
    for rec in records:
        if rec["name"] == "random_small_delta_conjugation_summary":
            samples = rec["records"]
            lines.append(
                "random small-delta conjugations: "
                f"samples={len(samples)} "
                f"max_target_ratio={max(r['target_ratio'] for r in samples):.6g} "
                f"max_target_l1={max(r['target_max_offcluster_l1'] for r in samples):.6g} "
                f"max_HM_ratio={max(r['hm_candidate_ratio'] for r in samples):.6g}"
            )
            continue
        lines.append(
            f"{rec['name']}: delta={rec['delta']:.8g} eta={rec['eta']:.8g} "
            f"denom={rec['denom_eta_plus_delta_over_eta']:.8g} pivots={rec['pivots']} "
            f"B_eta={rec['B_eta']} target_l1={rec['target_max_offcluster_l1']:.8g} "
            f"target_ratio={rec['target_ratio']:.6g} HMdist={rec['hm_candidate_max_row_l1']:.8g} "
            f"HMratio={rec['hm_candidate_ratio']:.6g} coeffneg_B={rec['max_coeff_neg_mass_B_eta']:.6g} "
            f"rep_disp/delta={rec['max_rep_positive_avg_row_displacement_over_delta']:.6g}"
        )
    return "\n".join(lines) + "\n"


def main():
    records = []
    for delta in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6]:
        records.append(chart_metrics(f"w27_rank2_leakage_delta_{delta:g}", leakage_family(delta)))
    for eps in [1e-2, 1e-3, 1e-4, 1e-5]:
        records.append(chart_metrics(f"split_block_eps_{eps:g}", split_block(eps)))
    for eps in [1e-2, 1e-3, 1e-4, 1e-5]:
        records.append(chart_metrics(f"w19_leftcone_eps_{eps:g}", leftcone(eps)))
    records.append(chart_metrics("w16_best_rational_above_corner", load_w16()))
    records.append(chart_metrics("w17_main_rational_above_corner", load_w17("main_rational_instance.json")))
    records.append(chart_metrics("w17_robust_rational_above_corner", load_w17("robust_rational_instance.json")))

    rng = np.random.default_rng(2801)
    random_records = []
    for target in [1e-2, 1e-3, 1e-4]:
        for trial in range(12):
            P0 = random_hm(7, 3, rng)
            P = conjugate_to_delta(P0, target, rng)
            rec = chart_metrics(f"random_conjugate_delta_{target:g}_trial_{trial}", P)
            random_records.append(
                {
                    "name": rec["name"],
                    "delta": rec["delta"],
                    "eta": rec["eta"],
                    "target_max_offcluster_l1": rec["target_max_offcluster_l1"],
                    "target_ratio": rec["target_ratio"],
                    "hm_candidate_max_row_l1": rec["hm_candidate_max_row_l1"],
                    "hm_candidate_ratio": rec["hm_candidate_ratio"],
                    "B_eta": rec["B_eta"],
                    "pivots": rec["pivots"],
                    "idempotence_inf": rec["idempotence_inf"],
                }
            )
    records.append({"name": "random_small_delta_conjugation_summary", "records": random_records})

    (OUT / "w28_face_numeric_results.json").write_text(json.dumps(records, indent=2, sort_keys=True))
    summary = summarize(records)
    (OUT / "w28_face_numeric_summary.txt").write_text(summary)
    print(summary, end="")


if __name__ == "__main__":
    main()
