#!/usr/bin/env python3
"""
Targeted template audit for w15.

This script reuses w15_refuter_search.py and records concise obstruction data:
  - s5/thin-cycle frame sweeps,
  - positive-diagonal self-mass probes, minimizing delta/sigma^2,
  - stochastic-idempotent conjugations.

The output is w15_template_audit.json.
"""

from __future__ import annotations

import argparse
import json
import math
import time

import numpy as np

from w15_refuter_search import (
    cycle_B,
    random_L,
    s5_family_L,
    optimize_Q_for_LB,
    verify_instance,
    random_conjugate_instance,
)


def slim(rec):
    keys = [
        "label", "gate", "n", "delta", "tau", "W", "v", "H", "H_over_delta",
        "H_over_tau", "sigma_tilde", "sigma_tilde_over_tau", "P_vv", "nu_v",
        "best_component", "best_Pi_over_tau",
    ]
    return {k: rec.get(k) for k in keys}


def update_best(bests, name, rec, key, larger=True):
    if rec.get("gate") != "PASS" or rec.get("delta", math.inf) > 0.25:
        return
    val = rec.get(key)
    if val is None:
        return
    cur = bests.get(name)
    if cur is None or ((val > cur["value"]) if larger else (val < cur["value"])):
        bests[name] = {"value": float(val), "record": slim(rec)}


def audit_s5_cycles():
    bests = {}
    counts = {"cases": 0, "lp_ok": 0, "pass_regime": 0, "branch": 0}
    for m in [2, 3, 4, 5, 6]:
        for a in [1e-4, 2e-4, 5e-4, 1e-3, 2e-3, 5e-3, 1e-2, 2e-2]:
            for edge in [1e-4, 2e-4, 5e-4, 1e-3, 2e-3, 5e-3, 1e-2, 2e-2, 5e-2, 0.1, 0.2]:
                sep = min(0.16, 0.85 / max(m - 1, 1))
                L = s5_family_L(a, 0.04, sep, m)
                for neg in [0.0, 0.1 * edge, 0.3 * edge, 0.6 * edge]:
                    counts["cases"] += 1
                    B = cycle_B(m, edge, neg_back=neg)
                    P, meta = optimize_Q_for_LB(L, B, q_bound=250.0)
                    if P is None:
                        continue
                    counts["lp_ok"] += 1
                    rec = verify_instance(P, "audit_s5_cycle", {"m": m, "a": a, "edge": edge, "neg_back": neg})
                    if rec.get("gate") == "PASS" and rec.get("delta", math.inf) <= 0.25:
                        counts["pass_regime"] += 1
                        if (rec.get("sigma_tilde_over_tau") or 0.0) > 1.0:
                            counts["branch"] += 1
                    update_best(bests, "max_sigma_over_tau", rec, "sigma_tilde_over_tau")
                    update_best(bests, "max_H_over_tau", rec, "H_over_tau")
                    update_best(bests, "max_H_over_delta", rec, "H_over_delta")
                    update_best(bests, "min_Pi_over_tau", rec, "best_Pi_over_tau", larger=False)
    return {"counts": counts, "bests": bests}


def audit_posdiag(rng, trials_per_diag):
    bests = {}
    per_diag = {}
    counts = {"cases": 0, "lp_ok": 0, "pass_regime": 0, "branch": 0}
    for diag in [0.05, 0.08, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.70, 0.90]:
        drec = {
            "diag": diag,
            "min_delta_over_diag2": math.inf,
            "best_sigma_over_tau": -math.inf,
            "best_H_over_tau": -math.inf,
            "best_record": None,
        }
        for _ in range(trials_per_diag):
            r = int(rng.choice([4, 5, 6]))
            m = int(rng.choice([3, 4, 5]))
            a_scale = 10 ** rng.uniform(-4.2, -1.0)
            L = random_L(r, m, rng, a_scale=a_scale, a_spread=0.7)
            edge = 10 ** rng.uniform(-5.0, -1.5)
            B = cycle_B(m, edge, neg_back=(edge * rng.uniform(0.0, 0.5)))
            B[0, 0] = diag
            counts["cases"] += 1
            P, meta = optimize_Q_for_LB(L, B, q_bound=300.0)
            if P is None:
                continue
            counts["lp_ok"] += 1
            rec = verify_instance(P, "audit_posdiag", {"diag": diag, "edge": edge, "a_scale": a_scale})
            if rec.get("gate") == "PASS" and rec.get("delta", math.inf) <= 0.25:
                counts["pass_regime"] += 1
                if (rec.get("sigma_tilde_over_tau") or 0.0) > 1.0:
                    counts["branch"] += 1
                ratio = rec["delta"] / max(rec["sigma_tilde"], 1e-150) ** 2
                if ratio < drec["min_delta_over_diag2"]:
                    drec["min_delta_over_diag2"] = float(ratio)
                    drec["best_record"] = slim(rec)
                drec["best_sigma_over_tau"] = max(drec["best_sigma_over_tau"], rec.get("sigma_tilde_over_tau") or -math.inf)
                drec["best_H_over_tau"] = max(drec["best_H_over_tau"], rec.get("H_over_tau") or -math.inf)
            update_best(bests, "max_sigma_over_tau", rec, "sigma_tilde_over_tau")
            update_best(bests, "max_H_over_tau", rec, "H_over_tau")
            update_best(bests, "min_delta_over_sigma2", {
                **rec,
                "delta_over_sigma2": rec.get("delta", math.inf) / max(rec.get("sigma_tilde") or 0.0, 1e-150) ** 2,
            }, "delta_over_sigma2", larger=False)
        per_diag[str(diag)] = drec
    return {"counts": counts, "per_diag": per_diag, "bests": bests}


def audit_conjugates(rng, trials):
    bests = {}
    counts = {"cases": 0, "pass_regime": 0, "branch": 0}
    for _ in range(trials):
        n = int(rng.choice([5, 6, 7, 8, 9]))
        k = int(rng.integers(2, min(5, n)))
        eps = 10 ** rng.uniform(-4.0, -0.15)
        P = random_conjugate_instance(n, k, rng, eps)
        if P is None:
            continue
        counts["cases"] += 1
        rec = verify_instance(P, "audit_conjugate", {"n": n, "k": k, "eps": eps})
        if rec.get("gate") == "PASS" and rec.get("delta", math.inf) <= 0.25:
            counts["pass_regime"] += 1
            if (rec.get("sigma_tilde_over_tau") or 0.0) > 1.0:
                counts["branch"] += 1
        update_best(bests, "max_sigma_over_tau", rec, "sigma_tilde_over_tau")
        update_best(bests, "max_H_over_tau", rec, "H_over_tau")
        update_best(bests, "max_H_over_delta", rec, "H_over_delta")
    return {"counts": counts, "bests": bests}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int, default=424242)
    ap.add_argument("--posdiag-trials", type=int, default=35)
    ap.add_argument("--conj-trials", type=int, default=150)
    ap.add_argument("--out", default="w15_template_audit.json")
    args = ap.parse_args()

    rng = np.random.default_rng(args.seed)
    t0 = time.time()
    out = {"created": time.strftime("%Y-%m-%d %H:%M:%S"), "seed": args.seed}
    print("[audit] s5 cycles", flush=True)
    out["s5_cycles"] = audit_s5_cycles()
    print("[audit] positive diagonal", flush=True)
    out["positive_diagonal"] = audit_posdiag(rng, args.posdiag_trials)
    print("[audit] conjugates", flush=True)
    out["conjugates"] = audit_conjugates(rng, args.conj_trials)
    out["elapsed_s"] = time.time() - t0
    with open(args.out, "w") as f:
        json.dump(out, f, indent=2, default=float)
    print(json.dumps({
        "elapsed_s": out["elapsed_s"],
        "s5_counts": out["s5_cycles"]["counts"],
        "posdiag_counts": out["positive_diagonal"]["counts"],
        "conj_counts": out["conjugates"]["counts"],
        "s5_bests": out["s5_cycles"]["bests"],
        "posdiag_bests": out["positive_diagonal"]["bests"],
        "conj_bests": out["conjugates"]["bests"],
    }, indent=2, default=float), flush=True)


if __name__ == "__main__":
    main()
