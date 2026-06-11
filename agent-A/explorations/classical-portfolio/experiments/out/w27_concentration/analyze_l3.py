import itertools
import json
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.linalg import qr


ROOT = Path("/home/tobias/Projects/almost-idempotent-positive-maps")
CP = ROOT / "agent-A/explorations/classical-portfolio"
OUT = Path("/tmp/codex-sigma-wall/w27_concentration")


def val(x):
    if isinstance(x, (int, float)):
        return float(x)
    if isinstance(x, str):
        return float(Fraction(x))
    if isinstance(x, dict):
        if "str" in x:
            return float(Fraction(x["str"]))
        return float(Fraction(int(x["num"]), int(x["den"])))
    raise TypeError(type(x))


def mat(obj):
    return np.array([[val(x) for x in row] for row in obj], dtype=float)


def neg_mass_rows(P):
    return np.maximum(-P, 0.0).sum(axis=1)


def rank(P, tol=1e-9):
    return int(np.linalg.matrix_rank(P, tol=tol))


def row_l1(P, Q):
    return np.sum(np.abs(P - Q), axis=1)


def volume_score(B):
    G = B @ B.T
    sign, logdet = np.linalg.slogdet(G)
    if sign <= 0:
        return -np.inf
    return 0.5 * logdet


def maxvol_pivots(P, exact_limit=250000):
    n = P.shape[0]
    k = rank(P)
    combos = 1
    for a in range(n - k + 1, n + 1):
        combos *= a
    for a in range(1, k + 1):
        combos //= a
    if combos <= exact_limit:
        best = None
        best_score = -np.inf
        for inds in itertools.combinations(range(n), k):
            B = P[list(inds)]
            if rank(B) < k:
                continue
            score = volume_score(B)
            if score > best_score + 1e-12:
                best_score = score
                best = list(inds)
        if best is not None:
            return best, True
    _, _, piv = qr(P.T, pivoting=True, mode="economic")
    return sorted([int(i) for i in piv[:k]]), False


def coordinates(P, pivots):
    R = P[pivots]
    coeffs = []
    for row in P:
        c, *_ = np.linalg.lstsq(R.T, row, rcond=None)
        coeffs.append(c)
    return np.array(coeffs)


def pivot_ball_clusters(P, pivots, eta):
    clusters = []
    owner = {}
    for s, p in enumerate(pivots):
        members = [
            int(i)
            for i in range(P.shape[0])
            if np.sum(np.abs(P[i] - P[p])) <= eta + 1e-12
        ]
        clusters.append(members)
        for i in members:
            owner.setdefault(i, []).append(s)
    overlaps = {int(i): ss for i, ss in owner.items() if len(ss) > 1}
    covered = set(owner)
    return clusters, sorted(set(range(P.shape[0])) - covered), overlaps


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
    Q = np.zeros_like(P)
    laws = []
    for s, p in enumerate(pivots):
        laws.append(clip_probability_on_support(P[p], clusters[s]))
    for s, members in enumerate(clusters):
        for i in members:
            Q[i] = laws[s]
    for i in b_eta:
        lam = clip_simplex(coeffs[i])
        Q[i] = sum(lam[s] * laws[s] for s in range(len(laws)))
    return Q, laws


def chart_metrics(name, P):
    delta = float(neg_mass_rows(P).max())
    eta = float(np.sqrt(delta)) if delta > 0 else 0.0
    pivots, exact = maxvol_pivots(P)
    coeffs = coordinates(P, pivots)
    clusters, b_eta, overlaps = pivot_ball_clusters(P, pivots, eta)
    Q, laws = hm_candidate(P, pivots, coeffs, clusters, b_eta)
    rep_records = []
    for s, p in enumerate(pivots):
        own = set(clusters[s])
        other_clusters = set().union(*[set(c) for t, c in enumerate(clusters) if t != s])
        bset = set(b_eta)
        row = P[p]
        rep_records.append(
            {
                "pivot": int(p),
                "cluster_size": len(own),
                "positive_mass_own": float(np.maximum(row[list(own)], 0.0).sum()) if own else 0.0,
                "positive_mass_other_clusters": float(np.maximum(row[list(other_clusters)], 0.0).sum()) if other_clusters else 0.0,
                "positive_mass_B_eta": float(np.maximum(row[list(bset)], 0.0).sum()) if bset else 0.0,
                "l1_mass_other_clusters": float(np.abs(row[list(other_clusters)]).sum()) if other_clusters else 0.0,
                "l1_mass_B_eta": float(np.abs(row[list(bset)]).sum()) if bset else 0.0,
                "neg_mass": float(np.maximum(-row, 0.0).sum()),
            }
        )
    coeff_neg = np.maximum(-coeffs, 0.0).sum(axis=1)
    return {
        "name": name,
        "n": int(P.shape[0]),
        "rank": rank(P),
        "delta": delta,
        "eta": eta,
        "rowsum_inf": float(np.max(np.abs(P.sum(axis=1) - 1.0))),
        "idempotence_inf": float(np.max(np.abs(P @ P - P))),
        "maxvol_pivots": [int(i) for i in pivots],
        "maxvol_exact": bool(exact),
        "max_abs_coeff": float(np.max(np.abs(coeffs))),
        "max_coeff_neg_mass_all_rows": float(np.max(coeff_neg)),
        "max_coeff_neg_mass_B_eta": float(np.max(coeff_neg[b_eta])) if b_eta else 0.0,
        "clusters": clusters,
        "B_eta": b_eta,
        "overlaps": overlaps,
        "rep_records": rep_records,
        "max_rep_positive_mass_other_clusters": float(max(r["positive_mass_other_clusters"] for r in rep_records)) if rep_records else 0.0,
        "max_rep_positive_mass_B_eta": float(max(r["positive_mass_B_eta"] for r in rep_records)) if rep_records else 0.0,
        "max_rep_l1_mass_outside_own": float(max(r["l1_mass_other_clusters"] + r["l1_mass_B_eta"] for r in rep_records)) if rep_records else 0.0,
        "hm_candidate_max_row_l1": float(row_l1(P, Q).max()),
        "hm_candidate_row_l1": [float(x) for x in row_l1(P, Q)],
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
    w = 1.0 - mass + delta
    B = np.array(
        [
            [w, -delta, mass],
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
    P = L @ B
    return P


def load_w16():
    path = CP / "experiments/out/w16_cert_audit/w16_best_rational_instance.json"
    data = json.loads(path.read_text())
    return mat(data["P_frac"])


def load_w17(fname):
    path = CP / f"experiments/out/w17_cert_audit/{fname}"
    data = json.loads(path.read_text())
    return mat(data["P"])


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


def main():
    records = []
    for eps in [1e-3, 1e-4, 1e-5]:
        records.append(chart_metrics(f"split_block_eps_{eps:g}", split_block(eps)))
    for eps in [1e-3, 1e-4, 1e-5]:
        records.append(chart_metrics(f"w19_leftcone_eps_{eps:g}", leftcone(eps)))
    for delta in [1e-3, 1e-4, 1e-5]:
        records.append(chart_metrics(f"leakage_family_delta_{delta:g}", leakage_family(delta)))
    records.append(chart_metrics("w16_best_rational_above_corner", load_w16()))
    records.append(chart_metrics("w17_main_rational_above_corner", load_w17("main_rational_instance.json")))
    records.append(chart_metrics("w17_robust_rational_above_corner", load_w17("robust_rational_instance.json")))

    rng = np.random.default_rng(2701)
    random_records = []
    for target in [1e-3, 1e-4]:
        for trial in range(8):
            P0 = random_hm(6, 3, rng)
            P = conjugate_to_delta(P0, target, rng)
            rec = chart_metrics(f"random_conjugate_delta_{target:g}_trial_{trial}", P)
            random_records.append(
                {
                    "name": rec["name"],
                    "delta": rec["delta"],
                    "eta": rec["eta"],
                    "max_rep_B_eta": rec["max_rep_positive_mass_B_eta"],
                    "max_rep_cross": rec["max_rep_positive_mass_other_clusters"],
                    "hm_candidate_max_row_l1": rec["hm_candidate_max_row_l1"],
                    "max_coeff_neg_mass_B_eta": rec["max_coeff_neg_mass_B_eta"],
                    "idempotence_inf": rec["idempotence_inf"],
                }
            )
    records.append({"name": "random_small_delta_conjugation_summary", "records": random_records})

    (OUT / "l3_numeric_results.json").write_text(json.dumps(records, indent=2, sort_keys=True))

    lines = []
    for rec in records:
        if rec["name"] == "random_small_delta_conjugation_summary":
            max_candidate = max(r["hm_candidate_max_row_l1"] for r in rec["records"])
            max_b = max(r["max_rep_B_eta"] for r in rec["records"])
            max_cross = max(r["max_rep_cross"] for r in rec["records"])
            lines.append(
                f"random small-delta conjugations: samples={len(rec['records'])} "
                f"max_candidate_l1={max_candidate:.6g} max_rep_B_eta={max_b:.6g} "
                f"max_rep_cross={max_cross:.6g}"
            )
            continue
        ratio = rec["hm_candidate_max_row_l1"] / rec["eta"] if rec["eta"] > 0 else 0.0
        b_ratio = rec["max_rep_positive_mass_B_eta"] / rec["eta"] if rec["eta"] > 0 else 0.0
        lines.append(
            f"{rec['name']}: delta={rec['delta']:.6g} eta={rec['eta']:.6g} "
            f"pivots={rec['maxvol_pivots']} B_eta={rec['B_eta']} "
            f"rep_cross={rec['max_rep_positive_mass_other_clusters']:.6g} "
            f"rep_B={rec['max_rep_positive_mass_B_eta']:.6g} "
            f"rep_B/eta={b_ratio:.6g} coeffneg_B={rec['max_coeff_neg_mass_B_eta']:.6g} "
            f"HMdist={rec['hm_candidate_max_row_l1']:.6g} HMdist/eta={ratio:.6g}"
        )
    (OUT / "l3_numeric_summary.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
