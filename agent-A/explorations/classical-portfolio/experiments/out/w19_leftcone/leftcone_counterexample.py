#!/usr/bin/env python3
import json
from pathlib import Path

import numpy as np

from leftcone_vertex_check import enumerate_vertices, min_l1_to_set, neg_mass, row_delta


def family(eps):
    """Exact P=Lambda B with Lambda=[I;(1/3,1/3,1/3)], q=(eps,-eps,0)."""
    return np.array(
        [
            [1 - eps / 3, -eps / 3, -eps / 3, eps],
            [eps / 3, 1 + eps / 3, eps / 3, -eps],
            [0.0, 0.0, 1.0, 0.0],
            [1 / 3, 1 / 3, 1 / 3, 0.0],
        ],
        dtype=float,
    )


def claimed_vertex(eps, C):
    r = C * eps
    return np.array([(1 + r) / 2, (1 + r) / 2, -r, 0.0], dtype=float)


def main():
    records = []
    for eps in [1e-1, 1e-2, 1e-3, 1e-4]:
        P = family(eps)
        delta = row_delta(P)
        for C in [0.0, 1.0, 2.0]:
            l = claimed_vertex(eps, C)
            verts, _ = enumerate_vertices(P, C=C)
            distances_to_l = [float(np.abs(v - l).sum()) for v in verts]
            records.append(
                {
                    "eps": eps,
                    "C": C,
                    "delta": delta,
                    "idempotence_inf": float(np.linalg.norm(P @ P - P, ord=np.inf)),
                    "rowsum_inf": float(np.linalg.norm(P @ np.ones(4) - 1, ord=np.inf)),
                    "claimed_l": l.tolist(),
                    "claimed_neg": neg_mass(l),
                    "claimed_fixed_inf": float(np.linalg.norm(l @ P - l, ord=np.inf)),
                    "claimed_dist_rows": min_l1_to_set(l, P),
                    "claimed_dist_visible_rows_0_1_2": min_l1_to_set(l, P[:3]),
                    "enumerated_vertices": int(len(verts)),
                    "enumeration_contains_claimed": min(distances_to_l, default=999.0) < 1e-7,
                    "min_enum_distance_to_claimed": min(distances_to_l, default=None),
                    "max_enum_dist_rows": max((min_l1_to_set(v, P) for v in verts), default=0.0),
                }
            )
    Path("leftcone_counterexample_results.json").write_text(json.dumps(records, indent=2, sort_keys=True))
    print(json.dumps(records, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
