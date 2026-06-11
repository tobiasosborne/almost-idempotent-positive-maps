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
    return np.maximum(-P, 0).sum(axis=1)


def clip_simplex_by_positive(a):
    pos = np.maximum(a, 0.0)
    s = pos.sum()
    if s <= 0:
        out = np.zeros_like(a)
        out[int(np.argmax(a))] = 1.0
        return out
    return pos / s


def hm_candidate_singletons(P, reps, coeffs):
    """H-M candidate for singleton C_s: recurrent reps become e_s; B rows use clipped coeffs."""
    n = P.shape[0]
    k = len(reps)
    Q = np.zeros_like(P)
    for s, r in enumerate(reps):
        Q[r, r] = 1.0
    for i in range(n):
        if i in reps:
            continue
        a = coeffs[i]
        ac = clip_simplex_by_positive(a)
        for s, r in enumerate(reps):
            Q[i, r] = ac[s]
    return Q


def metrics(name, P, reps, coeffs):
    n = P.shape[0]
    k = len(reps)
    Q = hm_candidate_singletons(P, reps, coeffs)
    delta_rows = neg_mass_rows(P)
    delta = float(delta_rows.max())
    row_dist = np.abs(P - Q).sum(axis=1)
    coeff_neg = {int(i): float(np.maximum(-coeffs[i], 0).sum()) for i in range(n) if i not in reps}
    coeff_l1 = {int(i): float(np.abs(coeffs[i]).sum()) for i in range(n) if i not in reps}
    rep_to_singleton = {
        int(r): float(np.abs(P[r] - np.eye(n)[r]).sum())
        for r in reps
    }
    cross_from_reps = {}
    for s, r in enumerate(reps):
        cross_from_reps[int(r)] = float(np.abs(np.delete(P[r, reps], s)).sum() + np.abs(np.delete(P[r], reps)).sum())
    return {
        "name": name,
        "n": n,
        "k": k,
        "rank": int(np.linalg.matrix_rank(P, tol=1e-8)),
        "delta": delta,
        "rowsum_inf": float(np.max(np.abs(P.sum(axis=1) - 1))),
        "idem_inf": float(np.max(np.abs(P @ P - P))),
        "reps": [int(r) for r in reps],
        "max_candidate_l1": float(row_dist.max()),
        "max_candidate_l1_over_delta": float(row_dist.max() / delta) if delta > 0 else None,
        "rep_to_singleton_l1": rep_to_singleton,
        "max_rep_to_singleton_l1": float(max(rep_to_singleton.values())) if rep_to_singleton else 0.0,
        "coeff_neg_mass": coeff_neg,
        "max_coeff_neg_mass": float(max(coeff_neg.values())) if coeff_neg else 0.0,
        "coeff_l1": coeff_l1,
        "max_coeff_l1": float(max(coeff_l1.values())) if coeff_l1 else 0.0,
        "cross_from_reps_l1": cross_from_reps,
        "max_cross_from_reps_l1": float(max(cross_from_reps.values())) if cross_from_reps else 0.0,
    }


def load_w16():
    path = CP / "experiments/out/w16_cert_audit/w16_best_rational_instance.json"
    data = json.loads(path.read_text())
    P = mat(data["P_frac"])
    Lam = mat(data["Lambda_frac"])
    k = Lam.shape[1]
    reps = list(range(k))
    coeffs = np.zeros((P.shape[0], k))
    coeffs[:k, :] = np.eye(k)
    coeffs[k:, :] = Lam[k:, :]
    return metrics("w16_best_rational", P, reps, coeffs)


def load_w17(fname, label):
    path = CP / f"experiments/out/w17_cert_audit/{fname}"
    data = json.loads(path.read_text())
    P = mat(data["P"])
    X = mat(data["X"])
    k = X.shape[1]
    reps = list(range(k))
    coeffs = np.zeros((P.shape[0], k))
    coeffs[:k, :] = np.eye(k)
    coeffs[k:, :] = X
    return metrics(label, P, reps, coeffs)


def leftcone(eps):
    P = np.array(
        [
            [1 - eps / 3, -eps / 3, -eps / 3, eps],
            [eps / 3, 1 + eps / 3, eps / 3, -eps],
            [0, 0, 1, 0],
            [1 / 3, 1 / 3, 1 / 3, 0],
        ],
        dtype=float,
    )
    reps = [0, 1, 2]
    coeffs = np.zeros((4, 3))
    coeffs[:3, :] = np.eye(3)
    coeffs[3, :] = [1 / 3, 1 / 3, 1 / 3]
    return metrics(f"w19_leftcone_eps_{eps:g}", P, reps, coeffs)


def split_block(eps):
    M = 1.0 / (2.0 * eps)
    a = -M
    b = -eps
    c = (1.0 - a * b) / (1.0 - a)
    q1 = np.array([1 - a * b, -(1 - a) * b, b], dtype=float)
    q2 = np.array([-a * c, 1 - (1 - a) * c, c], dtype=float)
    q3 = np.array([0.0, 0.0, 1.0], dtype=float)
    P = np.vstack([q1, q2, q3])
    coeffs = np.array([[1.0, 0.0], [0.0, 1.0], [a, 1.0 - a]], dtype=float)
    m = metrics(f"split_block_eps_{eps:g}", P, [0, 1], coeffs)
    pi = np.array([0.5, 0.5, 0.0])
    Q_merge = np.vstack([pi, pi, q3])
    dist_merge = np.abs(P - Q_merge).sum(axis=1)
    m["merge_candidate_max_l1"] = float(dist_merge.max())
    m["merge_candidate_over_delta"] = float(dist_merge.max() / eps)
    m["large_coeff_a"] = float(a)
    return m


if __name__ == "__main__":
    results = [
        load_w16(),
        load_w17("main_rational_instance.json", "w17_main_rational"),
        load_w17("robust_rational_instance.json", "w17_robust_rational"),
        leftcone(1e-3),
        split_block(1e-3),
        split_block(1e-4),
    ]
    print(json.dumps(results, indent=2, sort_keys=True))
