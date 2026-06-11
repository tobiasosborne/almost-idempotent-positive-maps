import json
from fractions import Fraction
from pathlib import Path

import numpy as np


ROOT = Path("/home/tobias/Projects/almost-idempotent-positive-maps")
CP = ROOT / "agent-A/explorations/classical-portfolio"


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


def max_row_l1(P, Q):
    return float(np.max(np.sum(np.abs(P - Q), axis=1)))


def pairwise_rows(P, rows):
    out = {}
    for pos, i in enumerate(rows):
        for j in rows[pos + 1 :]:
            out[f"{i}-{j}"] = float(np.sum(np.abs(P[i] - P[j])))
    return out


def threshold_components(P, rows, eta):
    parent = {r: r for r in rows}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for pos, i in enumerate(rows):
        for j in rows[pos + 1 :]:
            if np.sum(np.abs(P[i] - P[j])) <= eta:
                union(i, j)
    comps = {}
    for r in rows:
        comps.setdefault(find(r), []).append(r)
    return sorted([sorted(v) for v in comps.values()])


def clip_simplex(a):
    pos = np.maximum(a, 0.0)
    s = pos.sum()
    if s == 0:
        out = np.zeros_like(a)
        out[int(np.argmax(a))] = 1.0
        return out
    return pos / s


def old_singleton_candidate(P, reps, coeffs):
    Q = np.zeros_like(P)
    for s, r in enumerate(reps):
        Q[r, r] = 1.0
    for i in range(P.shape[0]):
        if i in reps:
            continue
        ac = clip_simplex(coeffs[i])
        for s, r in enumerate(reps):
            Q[i, r] = ac[s]
    return Q


def summarize_known(name, P, reps, coeffs):
    delta = float(neg_mass_rows(P).max())
    eta_sqrt = float(np.sqrt(delta)) if delta >= 0 else float("nan")
    Q_old = old_singleton_candidate(P, reps, coeffs)
    coeff_neg = [
        float(np.maximum(-coeffs[i], 0.0).sum())
        for i in range(P.shape[0])
        if i not in reps
    ]
    return {
        "name": name,
        "n": int(P.shape[0]),
        "rank_numeric": int(np.linalg.matrix_rank(P, tol=1e-9)),
        "delta": delta,
        "sqrt_delta": eta_sqrt,
        "idempotence_inf": float(np.max(np.abs(P @ P - P))),
        "rowsum_inf": float(np.max(np.abs(P.sum(axis=1) - 1.0))),
        "reps": [int(r) for r in reps],
        "rep_pair_l1": pairwise_rows(P, reps),
        "sqrt_delta_components_on_given_reps": threshold_components(P, reps, eta_sqrt),
        "max_old_singleton_l1": max_row_l1(P, Q_old),
        "max_coeff_negative_mass": max(coeff_neg) if coeff_neg else 0.0,
    }


def load_w16():
    path = CP / "experiments/out/w16_cert_audit/w16_best_rational_instance.json"
    data = json.loads(path.read_text())
    P = mat(data["P_frac"])
    Lam = mat(data["Lambda_frac"])
    k = Lam.shape[1]
    coeffs = np.zeros((P.shape[0], k))
    coeffs[:k, :] = np.eye(k)
    coeffs[k:, :] = Lam[k:, :]
    return summarize_known("w16_best_rational", P, list(range(k)), coeffs)


def load_w17(fname, label):
    path = CP / f"experiments/out/w17_cert_audit/{fname}"
    data = json.loads(path.read_text())
    P = mat(data["P"])
    X = mat(data["X"])
    k = X.shape[1]
    coeffs = np.zeros((P.shape[0], k))
    coeffs[:k, :] = np.eye(k)
    coeffs[k:, :] = X
    return summarize_known(label, P, list(range(k)), coeffs)


def leftcone(eps):
    P = np.array(
        [
            [1 - eps / 3, -eps / 3, -eps / 3, eps],
            [eps / 3, 1 + eps / 3, eps / 3, -eps],
            [0.0, 0.0, 1.0, 0.0],
            [1 / 3, 1 / 3, 1 / 3, 0.0],
        ]
    )
    coeffs = np.zeros((4, 3))
    coeffs[:3, :] = np.eye(3)
    coeffs[3, :] = [1 / 3, 1 / 3, 1 / 3]
    out = summarize_known(f"w19_leftcone_eps_{eps:g}", P, [0, 1, 2], coeffs)
    out["comment"] = "no merge at sqrt(delta); transient coefficient is convex"
    return out


def split_block(eps):
    q1 = np.array([0.5, 0.5 + eps, -eps])
    q2 = np.array([1.0 / (2.0 * (1.0 + 2.0 * eps)), 0.5, eps / (1.0 + 2.0 * eps)])
    q3 = np.array([0.0, 0.0, 1.0])
    P = np.vstack([q1, q2, q3])
    old_coeffs = np.array(
        [[1.0, 0.0], [0.0, 1.0], [-1.0 / (2.0 * eps), 1.0 + 1.0 / (2.0 * eps)]]
    )
    old = summarize_known(f"split_block_unmerged_eps_{eps:g}", P, [0, 1], old_coeffs)

    # Repaired merged basis: keep q1 for the close q1/q2 cluster and promote q3.
    merged_coeffs = np.array(
        [
            [1.0, 0.0],
            [1.0 / (1.0 + 2.0 * eps), 2.0 * eps / (1.0 + 2.0 * eps)],
            [0.0, 1.0],
        ]
    )
    pi = np.array([0.5, 0.5, 0.0])
    Q = np.vstack([pi, pi, q3])
    merged = {
        "basis_reps": [0, 2],
        "clustered_rows": [[0, 1], [2]],
        "coefficients": merged_coeffs.tolist(),
        "max_abs_coeff": float(np.max(np.abs(merged_coeffs))),
        "max_negative_coeff_mass": float(np.max(np.maximum(-merged_coeffs, 0.0).sum(axis=1))),
        "merged_HM_candidate_l1": max_row_l1(P, Q),
        "merged_HM_candidate_over_delta": float(max_row_l1(P, Q) / eps),
        "q1_q2_l1": float(np.sum(np.abs(q1 - q2))),
    }
    old["repaired_merged_chart"] = merged
    return old


def main():
    results = [
        split_block(1e-3),
        split_block(1e-4),
        leftcone(1e-3),
        load_w16(),
        load_w17("main_rational_instance.json", "w17_main_rational"),
        load_w17("robust_rational_instance.json", "w17_robust_rational"),
    ]
    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
