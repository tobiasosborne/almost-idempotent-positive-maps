#!/usr/bin/env python3
"""Numerics for w20_curve.

The script reuses the audited w19 tangent machinery.  It is deliberately small:
it reproduces the tiny recurrent-mass visibility transition and then samples
exact idempotent arcs through boundary/tiny strata, recording H/delta.
"""

from __future__ import annotations

import importlib.util
import json
import math
import sys
from pathlib import Path

import numpy as np


AUDIT_PATH = Path(
    "/home/tobias/Projects/almost-idempotent-positive-maps/"
    "agent-A/explorations/classical-portfolio/experiments/out/"
    "w19_tangent_audit/tangent_audit.py"
)


def load_audit_module():
    spec = importlib.util.spec_from_file_location("tangent_audit", AUDIT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load {AUDIT_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def min_positive_recurrent_mass(st) -> float:
    vals = []
    for pi in st.pis:
        vals.extend([float(x) for x in pi if x > 0])
    return min(vals) if vals else 1.0


def summarize_samples(samples):
    finite = [s for s in samples if math.isfinite(s["H_over_delta"])]
    if not finite:
        return {"count": len(samples), "finite_count": 0}
    worst = max(finite, key=lambda s: s["H_over_delta"])
    return {
        "count": len(samples),
        "finite_count": len(finite),
        "max_H_over_delta": worst["H_over_delta"],
        "worst": worst,
    }


def height_visible_clustered(audit, P: np.ndarray, cluster_tol: float = 1e-8) -> dict:
    """A numerically stable version of audit.height_visible.

    The audit code intentionally uses very small duplicate tolerances.  At the
    tiny-mass boundary scale, LP vertex tests can then discard a whole
    near-duplicate recurrent cluster.  For this stress script we cluster rows
    below cluster_tol before the vertex/exposedness tests.
    """
    rows, rep_indices = audit.unique_rows(P, tol=cluster_tol)
    delta = max(float(np.maximum(-row, 0.0).sum()) for row in P)
    tau = math.sqrt(max(delta, 0.0))
    rho = 4.0 * tau
    kappa = tau / 4.0
    vertex_flags = []
    visible_flags = []
    margins = []
    for idx, row in enumerate(rows):
        others = np.array([r for j, r in enumerate(rows) if j != idx])
        dist = math.inf if len(others) == 0 else audit.l1_distance_to_conv(row, others)
        is_vertex = len(others) == 0 or dist > max(1e-11, cluster_tol / 10.0)
        vertex_flags.append(is_vertex)
        if not is_vertex:
            visible_flags.append(False)
            margins.append(None)
            continue
        if delta <= 1e-14:
            margin = math.inf
        else:
            margin = audit.exposed_margin(row, rows, rho)
        margins.append(margin)
        visible_flags.append(math.isinf(margin) or margin + 1e-9 >= kappa)
    visible_points = np.array([row for row, flag in zip(rows, visible_flags) if flag])
    heights = [audit.l1_distance_to_conv(row, visible_points) for row in P] if len(visible_points) else [math.inf]
    return {
        "delta": delta,
        "tau": tau,
        "rho": rho,
        "kappa": kappa,
        "unique_rows": len(rows),
        "representatives": rep_indices,
        "vertices": int(sum(vertex_flags)),
        "visible": int(sum(visible_flags)),
        "margins": [None if m is None else ("inf" if math.isinf(m) else m) for m in margins],
        "H": max(heights),
        "row_heights": heights,
    }


def main() -> None:
    audit = load_audit_module()
    rng = np.random.default_rng(20260611)
    strata = audit.deterministic_strata(rng)
    tiny = next(st for st in strata if st.name == "tiny_pi_many_transients_k3")
    zero = audit.solve_stratum(tiny, 0.0, 1.0)
    budget = audit.solve_stratum(tiny, 1.0, 1.0)

    ts = [1e-4, 3e-5, 1e-5, 3e-6, 1e-6, 3e-7, 1e-7, 3e-8]
    P0_tiny = audit.build_p0(tiny)
    mu = min_positive_recurrent_mass(tiny)
    tiny_records = []
    for t in ts:
        P = audit.exact_arc(P0_tiny, np.array(zero["A"]), t)
        hv = height_visible_clustered(audit, P)
        delta = hv["delta"]
        H = hv["H"]
        h_over_delta = math.inf if delta == 0 and H > 0 else (
            0.0 if delta == 0 else H / delta
        )
        tiny_records.append(
            {
                "t": t,
                "delta": delta,
                "H": H,
                "H_over_t": H / t if math.isfinite(H) else math.inf,
                "delta_over_t": delta / t,
                "visible": hv["visible"],
                "vertices": hv["vertices"],
                "unique_rows": hv["unique_rows"],
                "H_over_delta": h_over_delta,
            }
        )

    boundary_samples = []
    test_strata = strata + audit.random_strata(20, rng)
    for st in test_strata:
        for budget_value in (0.0, 1.0):
            sol = audit.solve_stratum(st, budget_value, 1.0)
            if "A" not in sol or sol.get("A") is None:
                continue
            A = np.array(sol["A"])
            for t in [1e-3, 3e-4, 1e-4, 3e-5, 1e-5, 3e-6]:
                P = audit.exact_arc(audit.build_p0(st), A, t)
                hv = height_visible_clustered(audit, P)
                delta = hv["delta"]
                H = hv["H"]
                if delta <= 1e-14:
                    ratio = 0.0 if H <= 1e-12 else math.inf
                else:
                    ratio = H / delta
                boundary_samples.append(
                    {
                        "name": st.name,
                        "n": st.n,
                        "k": st.k,
                        "budget": budget_value,
                        "t": t,
                        "mu": min_positive_recurrent_mass(st),
                        "delta": delta,
                        "H": H,
                        "H_over_delta": ratio,
                        "visible": hv["visible"],
                        "vertices": hv["vertices"],
                    }
                )

    result = {
        "audit_module": str(AUDIT_PATH),
        "tiny_stratum": {
            "name": tiny.name,
            "n": tiny.n,
            "k": tiny.k,
            "mu": mu,
            "zero_budget_value": zero["value"],
            "zero_budget_dot_delta": zero["ddelta"],
            "budget1_value": budget["value"],
            "samples": tiny_records,
        },
        "boundary_arc_summary": summarize_samples(boundary_samples),
        "boundary_samples": boundary_samples,
    }

    Path("numerics_results.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    lines = []
    lines.append("w20_curve numerics")
    lines.append(f"audit_module: {AUDIT_PATH}")
    lines.append("")
    lines.append("tiny recurrent-mass zero-budget visibility transition")
    lines.append(f"name: {tiny.name}")
    lines.append(f"mu: {mu:.12g}")
    lines.append(f"zero_budget_value: {zero['value']:.12g}")
    lines.append(f"zero_budget_dot_delta: {zero['ddelta']:.12g}")
    for s in tiny_records:
        lines.append(
            "t={t:.3g} delta/t={delta_over_t:.12g} H/t={H_over_t:.12g} "
            "H/delta={H_over_delta:.12g} visible={visible} vertices={vertices}".format(**s)
        )
    lines.append("")
    lines.append("boundary/tiny exact-arc sweep")
    summary = result["boundary_arc_summary"]
    lines.append(f"samples: {summary['count']}")
    lines.append(f"finite_samples: {summary['finite_count']}")
    lines.append(f"max_H_over_delta: {summary.get('max_H_over_delta')}")
    if "worst" in summary:
        w = summary["worst"]
        lines.append(
            "worst: name={name} budget={budget} t={t:.3g} mu={mu:.3g} "
            "delta={delta:.12g} H={H:.12g} H/delta={H_over_delta:.12g} "
            "visible={visible} vertices={vertices}".format(**w)
        )
    Path("numerics_summary.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
