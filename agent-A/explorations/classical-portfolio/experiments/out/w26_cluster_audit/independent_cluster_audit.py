import itertools
import json
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.linalg import qr
from scipy.optimize import linprog


ROOT = Path("/home/tobias/Projects/almost-idempotent-positive-maps")
CP = ROOT / "agent-A/explorations/classical-portfolio"
OUT = Path("/tmp/codex-sigma-wall/w26_cluster_audit")


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


def l1_dist_to_span(v, basis):
    basis = np.asarray(basis, dtype=float)
    if basis.size == 0:
        return float(np.sum(np.abs(v)))
    m, n = basis.shape
    c = np.r_[np.zeros(m), np.ones(n)]
    a1 = np.c_[basis.T, -np.eye(n)]
    a2 = np.c_[-basis.T, -np.eye(n)]
    A_ub = np.r_[a1, a2]
    b_ub = np.r_[v, -v]
    bounds = [(None, None)] * m + [(0, None)] * n
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")
    if not res.success:
        raise RuntimeError(res.message)
    return float(res.fun)


def greedy_gap_pivots(P, tol=1e-8):
    n = P.shape[0]
    k = rank(P)
    pivots = [0]
    while len(pivots) < k:
        basis = P[pivots]
        chosen = None
        distances = []
        for i in range(n):
            if i in pivots:
                continue
            if rank(P[pivots + [i]]) <= len(pivots):
                continue
            d = l1_dist_to_span(P[i], basis)
            distances.append((d, i))
            if d >= 1.0 - tol and chosen is None:
                chosen = i
        if chosen is None:
            # Numerical fallback: rank gap says this should be at least one.
            chosen = max(distances)[1]
        pivots.append(chosen)
    return pivots


def volume_score(B):
    G = B @ B.T
    sign, logdet = np.linalg.slogdet(G)
    if sign <= 0:
        return -np.inf
    return 0.5 * logdet


def maxvol_pivots(P, exact_limit=100000):
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


def coordinate_lipschitz_l1(P, pivots):
    R = P[pivots]
    k, n = R.shape
    out = []
    for s in range(k):
        c = np.r_[np.zeros(n), 1.0]
        A_eq = np.c_[R, np.zeros(k)]
        b_eq = np.eye(k)[s]
        A_ub = []
        b_ub = []
        for j in range(n):
            row = np.zeros(n + 1)
            row[j] = 1.0
            row[-1] = -1.0
            A_ub.append(row)
            b_ub.append(0.0)
            row = np.zeros(n + 1)
            row[j] = -1.0
            row[-1] = -1.0
            A_ub.append(row)
            b_ub.append(0.0)
        bounds = [(None, None)] * n + [(0, None)]
        res = linprog(
            c,
            A_ub=np.array(A_ub),
            b_ub=np.array(b_ub),
            A_eq=A_eq,
            b_eq=b_eq,
            bounds=bounds,
            method="highs",
        )
        if not res.success:
            out.append(float("nan"))
        else:
            out.append(float(res.fun))
    return out


def pivot_ball_clusters(P, pivots, eta):
    clusters = []
    memberships = {}
    for s, p in enumerate(pivots):
        members = [
            int(i)
            for i in range(P.shape[0])
            if np.sum(np.abs(P[i] - P[p])) <= eta + 1e-12
        ]
        clusters.append(members)
        for i in members:
            memberships.setdefault(i, []).append(s)
    overlaps = {int(i): ss for i, ss in memberships.items() if len(ss) > 1}
    covered = set(memberships)
    return clusters, sorted(set(range(P.shape[0])) - covered), overlaps


def threshold_components(P, eta):
    n = P.shape[0]
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for i in range(n):
        for j in range(i + 1, n):
            if np.sum(np.abs(P[i] - P[j])) <= eta + 1e-12:
                union(i, j)
    comps = {}
    for i in range(n):
        comps.setdefault(find(i), []).append(i)
    return sorted([v for v in comps.values()], key=lambda x: (x[0], len(x)))


def chart_metrics(P, name, eta=None):
    delta = float(neg_mass_rows(P).max())
    if eta is None:
        eta = float(np.sqrt(delta))
    k = rank(P)
    R = 1.0 + 2.0 * delta
    greedy = greedy_gap_pivots(P)
    maxvol, maxvol_exact = maxvol_pivots(P)
    coeff_g = coordinates(P, greedy)
    coeff_m = coordinates(P, maxvol)
    lam_g = coordinate_lipschitz_l1(P, greedy)
    lam_m = coordinate_lipschitz_l1(P, maxvol)
    clusters_g, b_g, overlap_g = pivot_ball_clusters(P, greedy, eta)
    clusters_m, b_m, overlap_m = pivot_ball_clusters(P, maxvol, eta)
    comps = threshold_components(P, eta) if eta > 0 else [[i] for i in range(P.shape[0])]
    return {
        "name": name,
        "n": int(P.shape[0]),
        "rank": k,
        "delta": delta,
        "eta": eta,
        "R": R,
        "rowsum_inf": float(np.max(np.abs(P.sum(axis=1) - 1.0))),
        "idempotence_inf": float(np.max(np.abs(P @ P - P))),
        "greedy_pivots": [int(i) for i in greedy],
        "greedy_max_abs_coeff": float(np.max(np.abs(coeff_g))),
        "greedy_max_neg_coeff_mass": float(np.max(np.maximum(-coeff_g, 0.0).sum(axis=1))),
        "greedy_lambda_max": float(np.nanmax(lam_g)),
        "greedy_lambda_by_coord": lam_g,
        "claimed_A_bound": float(R * (1.0 + R) ** (k - 1)),
        "claimed_Lambda_bound": float((1.0 + R) ** (k - 1)),
        "greedy_clusters": clusters_g,
        "greedy_B_eta": b_g,
        "greedy_cluster_overlaps": overlap_g,
        "single_linkage_components": comps,
        "maxvol_pivots": [int(i) for i in maxvol],
        "maxvol_exact": bool(maxvol_exact),
        "maxvol_max_abs_coeff": float(np.max(np.abs(coeff_m))),
        "maxvol_max_neg_coeff_mass": float(np.max(np.maximum(-coeff_m, 0.0).sum(axis=1))),
        "maxvol_lambda_max": float(np.nanmax(lam_m)),
        "maxvol_lambda_by_coord": lam_m,
        "maxvol_clusters": clusters_m,
        "maxvol_B_eta": b_m,
        "maxvol_cluster_overlaps": overlap_m,
        "improved_A_bound": 1.0,
        "improved_Lambda_bound": 1.0,
        "improved_sum_rule_E_bound": float(R * eta),
    }


def split_block(eps):
    q1 = np.array([0.5, 0.5 + eps, -eps])
    q2 = np.array([1.0 / (2.0 * (1.0 + 2.0 * eps)), 0.5, eps / (1.0 + 2.0 * eps)])
    q3 = np.array([0.0, 0.0, 1.0])
    P = np.vstack([q1, q2, q3])
    m = chart_metrics(P, f"split_block_eps_{eps:g}")
    old_coeff = np.array(
        [[1.0, 0.0], [0.0, 1.0], [-1.0 / (2.0 * eps), 1.0 + 1.0 / (2.0 * eps)]]
    )
    pi = np.array([0.5, 0.5, 0.0])
    Q_merge = np.vstack([pi, pi, q3])
    m.update(
        {
            "old_reps": [0, 1],
            "old_max_abs_coeff": float(np.max(np.abs(old_coeff))),
            "old_max_neg_coeff_mass": float(np.max(np.maximum(-old_coeff, 0.0).sum(axis=1))),
            "q1_q2_l1": float(np.sum(np.abs(q1 - q2))),
            "merged_HM_l1": float(np.max(row_l1(P, Q_merge))),
            "merged_HM_l1_over_delta": float(np.max(row_l1(P, Q_merge)) / eps),
        }
    )
    return P, m


def leftcone(eps):
    P = np.array(
        [
            [1 - eps / 3, -eps / 3, -eps / 3, eps],
            [eps / 3, 1 + eps / 3, eps / 3, -eps],
            [0.0, 0.0, 1.0, 0.0],
            [1 / 3, 1 / 3, 1 / 3, 0.0],
        ]
    )
    return P, chart_metrics(P, f"w19_leftcone_eps_{eps:g}")


def load_w16():
    path = CP / "experiments/out/w16_cert_audit/w16_best_rational_instance.json"
    data = json.loads(path.read_text())
    P = mat(data["P_frac"])
    return P, chart_metrics(P, "w16_best_rational")


def load_w17(fname, label):
    path = CP / f"experiments/out/w17_cert_audit/{fname}"
    data = json.loads(path.read_text())
    P = mat(data["P"])
    return P, chart_metrics(P, label)


def simplex_bad_order(k):
    n = k + 1
    P = np.zeros((n, n))
    P[0, 1:] = 1.0 / k
    for s in range(k):
        P[s + 1, s + 1] = 1.0
    return P


def random_rowsum_zero_matrix(n, seed):
    rng = np.random.default_rng(seed)
    K = rng.normal(size=(n, n))
    K -= K.mean(axis=1, keepdims=True)
    norm = np.linalg.norm(K, ord=np.inf)
    return K / norm


def conjugation_smear(P0, target_delta, seed=1):
    n = P0.shape[0]
    K = random_rowsum_zero_matrix(n, seed)

    def make(t):
        S = np.eye(n) + t * K
        return S @ P0 @ np.linalg.inv(S)

    lo, hi = 0.0, 1.0
    for _ in range(20):
        if neg_mass_rows(make(hi)).max() >= target_delta:
            break
        hi *= 2.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if neg_mass_rows(make(mid)).max() < target_delta:
            lo = mid
        else:
            hi = mid
    return make(hi), hi


def bridge_chain(rank_two_points, step_l1):
    # Nonnegative rank-2 idempotent with a single-linkage chain between two
    # recurrent rows. Used to test merge-order ambiguity, not delta scaling.
    n = rank_two_points + 2
    P = np.zeros((n, n))
    P[0, 0] = 1.0
    P[-1, 1] = 1.0
    for idx in range(1, n - 1):
        t = 1.0 - idx / (n - 1)
        P[idx, 0] = t
        P[idx, 1] = 1.0 - t
    eta = step_l1
    return P, chart_metrics(P, f"rank2_bridge_chain_{rank_two_points}_eta_{eta:g}", eta=eta)


def main():
    results = []
    for eps in [1e-3, 1e-4, 1e-5]:
        _, m = split_block(eps)
        results.append(m)
    for eps in [1e-3, 1e-4, 1e-5]:
        _, m = leftcone(eps)
        results.append(m)
    for loader in [
        load_w16,
        lambda: load_w17("main_rational_instance.json", "w17_main_rational"),
        lambda: load_w17("robust_rational_instance.json", "w17_robust_rational"),
    ]:
        _, m = loader()
        results.append(m)

    growth = []
    for k in range(2, 17):
        P0 = simplex_bad_order(k)
        base = chart_metrics(P0, f"simplex_bad_order_k{k}")
        Ps, smear_t = conjugation_smear(P0, 1e-5, seed=100 + k)
        smeared = chart_metrics(Ps, f"smeared_simplex_bad_order_k{k}_delta_1e-5")
        growth.append(
            {
                "k": k,
                "base_delta": base["delta"],
                "base_greedy_max_abs_coeff": base["greedy_max_abs_coeff"],
                "base_maxvol_max_abs_coeff": base["maxvol_max_abs_coeff"],
                "base_claimed_A": base["claimed_A_bound"],
                "smeared_delta": smeared["delta"],
                "smeared_eta": smeared["eta"],
                "smeared_t": smear_t,
                "smeared_greedy_max_abs_coeff": smeared["greedy_max_abs_coeff"],
                "smeared_maxvol_max_abs_coeff": smeared["maxvol_max_abs_coeff"],
                "smeared_maxvol_lambda_max": smeared["maxvol_lambda_max"],
                "smeared_greedy_lambda_max": smeared["greedy_lambda_max"],
                "smeared_claimed_A": smeared["claimed_A_bound"],
            }
        )
    results.append({"name": "rank_growth_simplex_bad_order", "records": growth})

    bridge_records = []
    for points in [6, 12, 24]:
        step = 2.0 / (points + 1)
        _, m = bridge_chain(points, step * 1.01)
        bridge_records.append(
            {
                "points": points,
                "audit_eta": m["eta"],
                "rank": m["rank"],
                "greedy_pivots": m["greedy_pivots"],
                "greedy_clusters": m["greedy_clusters"],
                "single_linkage_components": m["single_linkage_components"],
                "greedy_max_abs_coeff": m["greedy_max_abs_coeff"],
                "maxvol_max_abs_coeff": m["maxvol_max_abs_coeff"],
            }
        )
    results.append({"name": "single_linkage_bridge_ambiguity", "records": bridge_records})

    out_json = OUT / "independent_cluster_results.json"
    out_json.write_text(json.dumps(results, indent=2, sort_keys=True))

    lines = []
    for rec in results:
        if rec["name"] == "rank_growth_simplex_bad_order":
            last = rec["records"][-1]
            lines.append(
                "rank_growth k=16: "
                f"base_greedy={last['base_greedy_max_abs_coeff']:.6g} "
                f"smeared_greedy={last['smeared_greedy_max_abs_coeff']:.6g} "
                f"maxvol={last['smeared_maxvol_max_abs_coeff']:.6g} "
                f"maxvol_Lambda={last['smeared_maxvol_lambda_max']:.6g} "
                f"claimed_A={last['smeared_claimed_A']:.6g}"
            )
        elif rec["name"] == "single_linkage_bridge_ambiguity":
            last = rec["records"][-1]
            lines.append(
                "bridge_chain points=24: "
                f"pivot_clusters={last['greedy_clusters']} "
                f"single_linkage={last['single_linkage_components']}"
            )
        else:
            lines.append(
                f"{rec['name']}: delta={rec['delta']:.6g} eta={rec['eta']:.6g} "
                f"greedy_A={rec['greedy_max_abs_coeff']:.6g} "
                f"maxvol_A={rec['maxvol_max_abs_coeff']:.6g} "
                f"maxvol_Lambda={rec['maxvol_lambda_max']:.6g} "
                f"E_improved={rec['improved_sum_rule_E_bound']:.6g} "
                f"claimed_A={rec['claimed_A_bound']:.6g}"
            )
    (OUT / "independent_cluster_summary.txt").write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
