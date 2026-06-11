#!/usr/bin/env python3
import itertools
import json
import math
from pathlib import Path

import numpy as np


ROOT = Path("/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio")
W16 = ROOT / "experiments/out/w16_cert_audit/w16_best_rational_instance.json"


def neg_mass(x):
    x = np.asarray(x, dtype=float)
    return float(np.maximum(-x, 0.0).sum())


def row_delta(P):
    return max(neg_mass(row) for row in P)


def left_fixed_affine(P, tol=1e-10):
    """Return l0,V so every left-fixed sum-one vector is l0 + y @ V."""
    n = P.shape[0]
    A = np.vstack([(P.T - np.eye(n)), np.ones((1, n))])
    b = np.zeros(n + 1)
    b[-1] = 1.0
    l0, *_ = np.linalg.lstsq(A, b, rcond=None)

    E = np.vstack([(P.T - np.eye(n)), np.ones((1, n))])
    _, s, vh = np.linalg.svd(E)
    rank = int((s > tol).sum())
    V = vh[rank:, :]
    return l0, V


def subset_halfspaces(l0, V, radius):
    n = l0.shape[0]
    d = V.shape[0]
    rows = []
    labels = []
    for mask in range(1, 1 << n):
        c = np.array([(mask >> j) & 1 for j in range(n)], dtype=float)
        # c @ (l0 + y @ V) >= -radius, stored as A y <= b.
        rows.append(-(V @ c))
        labels.append(mask)
    return np.asarray(rows).reshape((-1, d)), np.asarray([radius + np.dot(
        np.array([(mask >> j) & 1 for j in range(n)], dtype=float), l0
    ) for mask in labels]), labels


def enumerate_vertices(P, C=1.0, tol=1e-8):
    delta = row_delta(P)
    radius = C * delta
    l0, V = left_fixed_affine(P)
    d = V.shape[0]
    if d == 0:
        return np.array([l0])
    A, b, labels = subset_halfspaces(l0, V, radius)
    verts = []
    active_labels = []
    for comb in itertools.combinations(range(len(labels)), d):
        M = A[list(comb)]
        if np.linalg.matrix_rank(M, tol=1e-9) < d:
            continue
        try:
            y = np.linalg.solve(M, b[list(comb)])
        except np.linalg.LinAlgError:
            continue
        slack = b - A @ y
        if slack.min() < -5e-7:
            continue
        l = l0 + y @ V
        if abs(l.sum() - 1.0) > 1e-6:
            continue
        if np.linalg.norm(l @ P - l, ord=np.inf) > 2e-6:
            continue
        if neg_mass(l) > radius + 2e-6:
            continue
        if not any(np.linalg.norm(l - v, ord=np.inf) < 2e-6 for v in verts):
            verts.append(l)
            active_labels.append(tuple(labels[i] for i in comb))
    return np.asarray(verts), active_labels


def min_l1_to_set(x, rows):
    return float(min(np.abs(x - r).sum() for r in rows))


def load_w16():
    data = json.loads(W16.read_text())
    return np.array(data["P_decimal"], dtype=float)


def chart_instance(rng, n=7, k=4, scale=0.02):
    m = n - k
    X = rng.dirichlet(np.ones(k), size=m)
    Q = rng.normal(size=(k, m))
    Q -= Q.mean(axis=0, keepdims=True) * 0.0
    Q *= scale / max(1.0, np.max(np.abs(Q)))
    B = np.hstack([np.eye(k) - Q @ X, Q])
    Lam = np.vstack([np.eye(k), X])
    P = Lam @ B
    return P


def summarize_vertices(P, C, visible=None):
    verts, _ = enumerate_vertices(P, C=C)
    rows = P
    if visible is None:
        visible_rows = rows
    else:
        visible_rows = rows[visible]
    out = []
    for idx, v in enumerate(verts):
        out.append(
            {
                "vertex": idx,
                "neg": neg_mass(v),
                "dist_rows": min_l1_to_set(v, rows),
                "dist_visible": min_l1_to_set(v, visible_rows),
                "nearest_row": int(np.argmin([np.abs(v - r).sum() for r in rows])),
                "nearest_visible": int(visible[np.argmin([np.abs(v - r).sum() for r in visible_rows])])
                if visible is not None
                else int(np.argmin([np.abs(v - r).sum() for r in rows])),
            }
        )
    return verts, out


def random_chart_sweep():
    rng = np.random.default_rng(20260611)
    rows = []
    for scale in [0.002, 0.01, 0.05]:
        best = None
        for trial in range(12):
            P = chart_instance(rng, n=6, k=3, scale=scale)
            delta = row_delta(P)
            if delta < 1e-10:
                continue
            verts, info = summarize_vertices(P, C=1.0, visible=list(range(3)))
            max_dr = max((item["dist_rows"] for item in info), default=0.0)
            max_dv = max((item["dist_visible"] for item in info), default=0.0)
            rec = {
                "scale": scale,
                "trial": trial,
                "delta": delta,
                "num_vertices": len(info),
                "max_dist_rows": max_dr,
                "max_dist_rows_over_delta": max_dr / delta,
                "max_dist_visible": max_dv,
                "max_dist_visible_over_delta": max_dv / delta,
                "idempotence_inf": float(np.linalg.norm(P @ P - P, ord=np.inf)),
                "rowsum_inf": float(np.linalg.norm(P @ np.ones(P.shape[0]) - 1, ord=np.inf)),
            }
            if best is None or rec["max_dist_rows_over_delta"] > best["max_dist_rows_over_delta"]:
                best = rec
        rows.append(best)
    return rows


def main():
    output = {}
    P = load_w16()
    output["w16"] = {
        "delta": row_delta(P),
        "tau": math.sqrt(row_delta(P)),
        "idempotence_inf": float(np.linalg.norm(P @ P - P, ord=np.inf)),
        "rowsum_inf": float(np.linalg.norm(P @ np.ones(P.shape[0]) - 1, ord=np.inf)),
        "C": {},
    }
    for C in [1.0, 2.0, 4.0, 10.0]:
        _, info = summarize_vertices(P, C=C, visible=[0, 1, 2, 3])
        output["w16"]["C"][str(C)] = {
            "num_vertices": len(info),
            "max_dist_rows": max(item["dist_rows"] for item in info),
            "max_dist_rows_over_delta": max(item["dist_rows"] for item in info) / output["w16"]["delta"],
            "max_dist_visible": max(item["dist_visible"] for item in info),
            "max_dist_visible_over_delta": max(item["dist_visible"] for item in info) / output["w16"]["delta"],
            "vertices": info,
        }
    output["random_chart_sweep"] = random_chart_sweep()
    Path("leftcone_vertex_results.json").write_text(json.dumps(output, indent=2, sort_keys=True))
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
