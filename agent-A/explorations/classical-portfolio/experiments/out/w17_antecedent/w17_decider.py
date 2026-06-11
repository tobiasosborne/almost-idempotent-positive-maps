#!/usr/bin/env python3
"""
w17_decider.py

Standalone numerical decider for the sigma_tilde > tau antecedent with real
height.  All reported candidates are verified from P itself:

  * P 1 = 1 and P^2 = P;
  * multiplicity-correct row vertices;
  * exposedness LP with rho=4*sqrt(delta), kappa=sqrt(delta)/4;
  * height to conv(W);
  * sigma_tilde with self-term included;
  * quotient carrier diagnostics for duplicate rows.

The search layer keeps exactness by working in the factor gauge

    Lambda = [I_k; X],  R = [I_k - Q X | Q],  P = Lambda R,

where every row of X sums to one.  Coupling probes additionally use
row-sum-preserving similarities A P A^{-1}, with A 1 = 1.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
from scipy.optimize import linprog


ROOT = Path("/home/tobias/Projects/almost-idempotent-positive-maps")
PORT = ROOT / "agent-A/explorations/classical-portfolio"
W16 = PORT / "experiments/out/w16_nlopt/w16_best_factorization.json"
CORNER = PORT / "experiments/out/d14_logs/corner_edge.json"

C_RHO = 4.0
C_KAPPA = 0.25
LP_TOL = 1e-9
EDGE_TOL = 1e-12


def finite(x: Any) -> Any:
    if isinstance(x, np.ndarray):
        return finite(x.tolist())
    if isinstance(x, dict):
        return {str(k): finite(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [finite(v) for v in x]
    if isinstance(x, (np.integer, int)):
        return int(x)
    if isinstance(x, (np.floating, float)):
        y = float(x)
        return y if math.isfinite(y) else None
    return x


def robust_linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None, presolve=True):
    last = None
    for method, pre in (
        ("highs-ipm", presolve),
        ("highs", presolve),
        ("highs-ds", presolve),
        ("highs-ipm", False),
        ("highs", False),
    ):
        res = linprog(
            c,
            A_ub=A_ub,
            b_ub=b_ub,
            A_eq=A_eq,
            b_eq=b_eq,
            bounds=bounds,
            method=method,
            options={"presolve": pre},
        )
        if res.success:
            return res
        last = res
        if getattr(res, "status", None) == 2:
            return res
    return last


def check_idempotent(P: np.ndarray, tol: float = 1e-8) -> dict[str, Any]:
    P = np.asarray(P, dtype=float)
    n = P.shape[0]
    row_sum_resid = float(np.abs(P @ np.ones(n) - 1.0).max())
    idem_resid = float(np.abs(P @ P - P).max())
    return {
        "row_sum_resid": row_sum_resid,
        "idem_resid": idem_resid,
        "ok": bool(row_sum_resid < tol and idem_resid < tol),
    }


def neg_mass(P: np.ndarray) -> tuple[np.ndarray, float]:
    nm = np.maximum(-np.asarray(P, dtype=float), 0.0).sum(axis=1)
    return nm, float(nm.max())


def dist1_to_conv(rows: np.ndarray, W_idx: list[int], i: int) -> tuple[float, np.ndarray | None]:
    rows = np.asarray(rows, dtype=float)
    n, d = rows.shape
    if not W_idx:
        return math.inf, None
    A = rows[W_idx].T
    b = rows[i]
    m = len(W_idx)
    nv = m + d
    c = np.concatenate([np.zeros(m), np.ones(d)])
    A_ub = []
    b_ub = []
    for j in range(d):
        row = np.zeros(nv)
        row[:m] = A[j]
        row[m + j] = -1.0
        A_ub.append(row)
        b_ub.append(b[j])

        row = np.zeros(nv)
        row[:m] = -A[j]
        row[m + j] = -1.0
        A_ub.append(row)
        b_ub.append(-b[j])
    A_eq = np.zeros((1, nv))
    A_eq[0, :m] = 1.0
    res = robust_linprog(
        c,
        A_ub=np.array(A_ub),
        b_ub=np.array(b_ub),
        A_eq=A_eq,
        b_eq=[1.0],
        bounds=[(0, None)] * m + [(0, None)] * d,
    )
    if res is None or not res.success:
        return math.inf, None
    return float(res.fun), res.x[:m]


def is_row_vertex(rows: np.ndarray, i: int, tol: float = 1e-7, dup_tol: float = 1e-9) -> tuple[bool, float]:
    rows = np.asarray(rows, dtype=float)
    n, d = rows.shape
    v = rows[i]
    others = [j for j in range(n) if j != i and np.abs(rows[j] - v).sum() > dup_tol]
    if not others:
        return True, 0.0
    A = rows[others].T
    m = len(others)
    nv = m + d
    c = np.concatenate([np.zeros(m), np.ones(d)])
    A_ub = []
    b_ub = []
    for j in range(d):
        row = np.zeros(nv)
        row[:m] = A[j]
        row[m + j] = -1.0
        A_ub.append(row)
        b_ub.append(v[j])

        row = np.zeros(nv)
        row[:m] = -A[j]
        row[m + j] = -1.0
        A_ub.append(row)
        b_ub.append(-v[j])
    A_eq = np.zeros((1, nv))
    A_eq[0, :m] = 1.0
    res = robust_linprog(
        c,
        A_ub=np.array(A_ub),
        b_ub=np.array(b_ub),
        A_eq=A_eq,
        b_eq=[1.0],
        bounds=[(0, None)] * m + [(0, None)] * d,
    )
    if res is None or not res.success:
        return True, math.inf
    return bool(res.fun > tol), float(res.fun)


def exposed_margin(rows: np.ndarray, i: int, rho: float, kappa: float) -> tuple[bool, float | None, dict[str, Any]]:
    rows = np.asarray(rows, dtype=float)
    n, d = rows.shape
    di = np.abs(rows - rows[i]).sum(axis=1)
    far = [j for j in range(n) if j != i and di[j] >= rho - 1e-12]
    if not far:
        return True, math.inf, {"far": [], "distances": di.tolist()}

    nv = d + 2
    c = np.zeros(nv)
    c[-1] = -1.0
    A_ub = []
    b_ub = []

    def hvec(row_idx: int) -> np.ndarray:
        out = np.zeros(nv)
        out[:d] = rows[row_idx]
        out[d] = 1.0
        return out

    for j in range(n):
        hj = hvec(j)
        A_ub.append(hj.copy())
        b_ub.append(1.0)
        A_ub.append(-hj.copy())
        b_ub.append(0.0)
    for j in far:
        hj = hvec(j)
        row = -hj
        row[-1] = 1.0
        A_ub.append(row)
        b_ub.append(0.0)
    res = robust_linprog(
        c,
        A_ub=np.array(A_ub),
        b_ub=np.array(b_ub),
        A_eq=np.array([hvec(i)]),
        b_eq=[0.0],
        bounds=[(None, None)] * d + [(None, None), (None, 1.0)],
        presolve=False,
    )
    if res is None or not res.success:
        return False, None, {"far": far, "distances": di.tolist(), "solver_failed": True}
    tstar = -float(res.fun)
    return bool(tstar >= kappa - 1e-9), tstar, {"far": far, "distances": di.tolist()}


def exposedness_lp_certificate(P: np.ndarray, i: int, rho: float, kappa: float) -> dict[str, Any]:
    rows = np.asarray(P, dtype=float)
    n, d = rows.shape
    di = np.abs(rows - rows[i]).sum(axis=1)
    far = [j for j in range(n) if j != i and di[j] >= rho - 1e-12]
    nv = d + 2
    c = np.zeros(nv)
    c[-1] = -1.0
    A_ub = []
    b_ub = []
    names = []

    def hvec(row_idx: int) -> np.ndarray:
        out = np.zeros(nv)
        out[:d] = rows[row_idx]
        out[d] = 1.0
        return out

    for j in range(n):
        hj = hvec(j)
        A_ub.append(hj.copy())
        b_ub.append(1.0)
        names.append(f"h(row {j}) <= 1")
        A_ub.append(-hj.copy())
        b_ub.append(0.0)
        names.append(f"h(row {j}) >= 0")
    for j in far:
        hj = hvec(j)
        row = -hj
        row[-1] = 1.0
        A_ub.append(row)
        b_ub.append(0.0)
        names.append(f"t <= h(row {j})")

    res = robust_linprog(
        c,
        A_ub=np.array(A_ub),
        b_ub=np.array(b_ub),
        A_eq=np.array([hvec(i)]),
        b_eq=[0.0],
        bounds=[(None, None)] * d + [(None, None), (None, 1.0)],
        presolve=False,
    )
    if res is None or not res.success:
        return {"success": False, "far": [int(x) for x in far], "message": getattr(res, "message", None)}
    h_values = rows @ res.x[:d] + res.x[d]
    active = []
    for idx, slack in enumerate(np.asarray(res.slack)):
        if abs(float(slack)) <= 1e-7:
            active.append(
                {
                    "constraint": names[idx],
                    "slack": float(slack),
                    "dual_marginal": float(res.ineqlin.marginals[idx]),
                }
            )
    tstar = -float(res.fun)
    return {
        "success": True,
        "target": int(i),
        "rho": float(rho),
        "kappa": float(kappa),
        "tstar": tstar,
        "tstar_over_kappa": float(tstar / kappa) if kappa > 0 else None,
        "far": [int(x) for x in far],
        "distances_from_target": [float(x) for x in di],
        "h_values": [float(x) for x in h_values],
        "active_constraints": active,
        "affine_w": [float(x) for x in res.x[:d]],
        "affine_b": float(res.x[d]),
    }


def well_exposed_set(rows: np.ndarray, rho: float, kappa: float) -> tuple[list[int], dict[int, dict[str, Any]]]:
    W = []
    info: dict[int, dict[str, Any]] = {}
    for i in range(len(rows)):
        vert, verr = is_row_vertex(rows, i)
        if not vert:
            info[i] = {"vertex": False, "vertex_error": verr}
            continue
        exposed, margin, ex = exposed_margin(rows, i, rho, kappa)
        info[i] = {
            "vertex": True,
            "vertex_error": verr,
            "exposed": exposed,
            "margin": margin,
            "far": [int(x) for x in ex.get("far", [])],
        }
        if exposed:
            W.append(i)
    return W, info


def sigma_tilde(P: np.ndarray, W: list[int], v: int) -> tuple[float, list[int], list[float]]:
    outside = []
    dists = []
    for j in range(P.shape[0]):
        d, _ = dist1_to_conv(P, W, j)
        dists.append(float(d))
        if d > 1e-9:
            outside.append(j)
    sig = float(sum(max(P[v, j], 0.0) for j in outside))
    return sig, outside, dists


def canonical_separator(P: np.ndarray, W: list[int], v: int) -> tuple[np.ndarray, float, np.ndarray, float, np.ndarray, float]:
    n = P.shape[0]
    nv = n + 1
    c = np.zeros(nv)
    c[:n] = -P[v]
    c[n] = 1.0
    A_ub = []
    b_ub = []
    for u in W:
        row = np.zeros(nv)
        row[:n] = P[u]
        row[n] = -1.0
        A_ub.append(row)
        b_ub.append(0.0)
    res = robust_linprog(
        c,
        A_ub=np.array(A_ub),
        b_ub=np.array(b_ub),
        bounds=[(-1, 1)] * n + [(None, None)],
        presolve=False,
    )
    if res is None or not res.success:
        raise RuntimeError("canonical separator LP failed")
    w = res.x[:n]
    s = float(res.x[n])
    phi = P @ w - s
    H = float(phi[v])
    g = H - phi
    Omega = float(g.max() - g.min())
    return w, s, phi, H, g, Omega


def tarjan_scc(vertices: list[int], adj: dict[int, list[int]]) -> list[list[int]]:
    index = 0
    stack: list[int] = []
    onstack: set[int] = set()
    indices: dict[int, int] = {}
    lowlink: dict[int, int] = {}
    comps: list[list[int]] = []

    def strongconnect(v: int) -> None:
        nonlocal index
        indices[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)
        onstack.add(v)
        for w in adj.get(v, []):
            if w not in indices:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif w in onstack:
                lowlink[v] = min(lowlink[v], indices[w])
        if lowlink[v] == indices[v]:
            comp = []
            while True:
                w = stack.pop()
                onstack.remove(w)
                comp.append(w)
                if w == v:
                    break
            comps.append(sorted(comp))

    for v in vertices:
        if v not in indices:
            strongconnect(v)
    return comps


def component_path_product(M: np.ndarray, comp: list[int], edge_tol: float = EDGE_TOL) -> tuple[float, int]:
    comp = list(comp)
    m = len(comp)
    if m <= 1:
        return 1.0, 0
    idx = {v: a for a, v in enumerate(comp)}
    best = np.zeros((m, m))
    dist = np.full((m, m), np.inf)
    for a in range(m):
        best[a, a] = 1.0
        dist[a, a] = 0
    for i in comp:
        a = idx[i]
        for j in comp:
            p = float(M[i, j])
            if p > edge_tol:
                b = idx[j]
                best[a, b] = max(best[a, b], p)
                dist[a, b] = min(dist[a, b], 1)
    for k in range(m):
        for i in range(m):
            for j in range(m):
                if dist[i, k] + dist[k, j] < dist[i, j]:
                    dist[i, j] = dist[i, k] + dist[k, j]
    finite_dist = dist[np.isfinite(dist)]
    L = int(np.max(finite_dist)) if finite_dist.size else 0
    cur = best.copy()
    out = best.copy()
    for _ in range(2, m + 1):
        nxt = np.zeros((m, m))
        for i in range(m):
            for k in range(m):
                if cur[i, k] <= 0:
                    continue
                nxt[i, :] = np.maximum(nxt[i, :], cur[i, k] * best[k, :])
        out = np.maximum(out, nxt)
        cur = nxt
    off = [out[i, j] for i in range(m) for j in range(m) if i != j]
    return float(min(off)) if off else 1.0, L


def row_classes(P: np.ndarray, dup_tol: float = 1e-9) -> tuple[list[list[int]], list[int]]:
    classes: list[list[int]] = []
    cls_of = [-1] * P.shape[0]
    for i in range(P.shape[0]):
        placed = False
        for cidx, cls in enumerate(classes):
            if float(np.abs(P[i] - P[cls[0]]).sum()) <= dup_tol:
                cls.append(i)
                cls_of[i] = cidx
                placed = True
                break
        if not placed:
            cls_of[i] = len(classes)
            classes.append([i])
    return classes, cls_of


def quotient_matrix(P: np.ndarray, classes: list[list[int]], cls_of: list[int]) -> np.ndarray:
    q = len(classes)
    out = np.zeros((q, q))
    for a, cls in enumerate(classes):
        rep = cls[0]
        for b, target_cls in enumerate(classes):
            out[a, b] = float(P[rep, target_cls].sum())
    return out


def shallow_components(M: np.ndarray, v: int, g: np.ndarray, Omega: float, tau: float, kappa: float) -> list[dict[str, Any]]:
    thresholds = [0.5 * kappa * Omega, 0.75 * kappa * Omega, kappa * Omega]
    records = []
    n = M.shape[0]
    for t in thresholds:
        S = [i for i in range(n) if g[i] < t + 1e-12]
        adj = {i: [j for j in S if M[i, j] > EDGE_TOL] for i in S}
        comps = tarjan_scc(S, adj)
        for comp in comps:
            mass_from_v = float(sum(max(M[v, j], 0.0) for j in comp))
            if mass_from_v <= 1e-12:
                continue
            Pi, L = component_path_product(M, comp)
            records.append(
                {
                    "t": float(t),
                    "t_over_kappaOmega": float(t / (kappa * Omega)) if kappa * Omega > 0 else None,
                    "component": [int(x) for x in comp],
                    "size": len(comp),
                    "mass_from_v": mass_from_v,
                    "Pi_C": Pi,
                    "L": L,
                    "Pi_over_tau": float(Pi / tau) if tau > 0 else None,
                    "min_edge": float(min((M[i, j] for i in comp for j in comp if M[i, j] > EDGE_TOL), default=0.0)),
                }
            )
    records.sort(key=lambda r: (r["Pi_C"], r["size"]))
    return records


def quotient_diagnostics(P: np.ndarray, W: list[int], v: int, g: np.ndarray, Omega: float, tau: float, kappa: float) -> dict[str, Any]:
    classes, cls_of = row_classes(P)
    Qbar = quotient_matrix(P, classes, cls_of)
    qchk = check_idempotent(Qbar, tol=1e-8)
    nm, qdelta = neg_mass(Qbar)
    gv = np.array([g[cls[0]] for cls in classes], dtype=float)
    comps = shallow_components(Qbar, cls_of[v], gv, Omega, tau, kappa)
    return {
        "num_classes": len(classes),
        "classes": [[int(x) for x in cls] for cls in classes],
        "class_of_v": int(cls_of[v]),
        "class_of_W": sorted({int(cls_of[w]) for w in W}),
        "quotient_idem": qchk,
        "quotient_delta": float(qdelta),
        "quotient_row_neg": [float(x) for x in nm],
        "quotient_shallow_components": comps[:12],
        "quotient_best_component": comps[0] if comps else None,
    }


def verify_instance(P: np.ndarray, label: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    P = np.asarray(P, dtype=float)
    chk = check_idempotent(P)
    nm, delta = neg_mass(P)
    rec: dict[str, Any] = {
        "label": label,
        "params": params or {},
        "n": int(P.shape[0]),
        "delta": float(delta),
        "row_neg": [float(x) for x in nm],
        "idem": chk,
    }
    if not chk["ok"] or delta <= 1e-14:
        rec["gate"] = "FAIL_idempotent_or_delta"
        return rec

    tau = math.sqrt(delta)
    rho = C_RHO * tau
    kappa = C_KAPPA * tau
    W, winfo = well_exposed_set(P, rho, kappa)
    rec.update({"tau": tau, "rho": rho, "kappa": kappa, "W": [int(x) for x in W], "nW": len(W)})
    if not W:
        rec["gate"] = "FAIL_W_empty"
        return rec

    dists_to_W = []
    for i in range(P.shape[0]):
        d, _ = dist1_to_conv(P, W, i)
        dists_to_W.append(float(d))
    outside_CW_all = [i for i, d in enumerate(dists_to_W) if d > 1e-9]

    vertex_info = {}
    hidden_vertices = []
    for i in range(P.shape[0]):
        d = dists_to_W[i]
        vert, verr = is_row_vertex(P, i)
        sig_i = float(sum(max(P[i, j], 0.0) for j in outside_CW_all)) if vert and i not in W else 0.0
        info = {
            "vertex": bool(vert),
            "vertex_error": float(verr) if math.isfinite(verr) else None,
            "inW": bool(i in W),
            "dist_to_CW": float(d),
            "exposed_margin": winfo.get(i, {}).get("margin"),
            "far": winfo.get(i, {}).get("far"),
        }
        if vert and i not in W and d > 1e-9:
            info["sigma_tilde"] = sig_i
            info["sigma_tilde_over_tau"] = float(sig_i / tau)
            info["outside_CW"] = [int(x) for x in outside_CW_all]
            hidden_vertices.append(i)
        vertex_info[i] = info

    rec["vertex_info"] = {int(k): v for k, v in vertex_info.items()}
    rec["hidden_vertices"] = [int(x) for x in hidden_vertices]
    rec["all_dist_to_CW"] = dists_to_W
    if not hidden_vertices:
        rec["gate"] = "FAIL_no_hidden_vertex"
        rec["H"] = 0.0
        return rec

    vbest = max(hidden_vertices, key=lambda i: dists_to_W[i])
    sig = float(sum(max(P[vbest, j], 0.0) for j in outside_CW_all))
    outside = outside_CW_all
    w, s, phi, Hsep, g, Omega = canonical_separator(P, W, vbest)
    comps = shallow_components(P, vbest, g, Omega, tau, kappa)
    qdiag = quotient_diagnostics(P, W, vbest, g, Omega, tau, kappa)
    rec.update(
        {
            "gate": "PASS",
            "v": int(vbest),
            "H": float(dists_to_W[vbest]),
            "H_separator": float(Hsep),
            "H_over_delta": float(dists_to_W[vbest] / delta) if delta > 0 else None,
            "H_over_tau": float(dists_to_W[vbest] / tau) if tau > 0 else None,
            "sigma_tilde": sig,
            "sigma_tilde_over_tau": float(sig / tau) if tau > 0 else None,
            "outside_CW": [int(x) for x in outside],
            "P_vv": float(P[vbest, vbest]),
            "nu_v": float(nm[vbest]),
            "phi": [float(x) for x in phi],
            "g": [float(x) for x in g],
            "Omega": float(Omega),
            "sep_resid_Pg": float(np.abs(P @ g - g).max()),
            "shallow_components": comps[:12],
            "best_component": comps[0] if comps else None,
            "quotient": qdiag,
            "antecedent_realized": bool(sig > tau and dists_to_W[vbest] > 0.1 * tau and delta <= 0.25),
        }
    )
    if comps:
        rec["best_Pi_over_tau"] = comps[0]["Pi_over_tau"]
    return rec


def load_w16() -> tuple[np.ndarray, np.ndarray]:
    payload = json.loads(W16.read_text())
    X = np.array(payload["X_hidden_rows"], dtype=float)
    Q = np.array(payload["Q"], dtype=float)
    return X, Q


def build_projection(X: np.ndarray, Q: np.ndarray) -> np.ndarray:
    k = Q.shape[0]
    Lam = np.vstack([np.eye(k), X])
    R = np.c_[np.eye(k) - Q @ X, Q]
    return Lam @ R


def factor_residuals(X: np.ndarray, Q: np.ndarray) -> dict[str, float]:
    k = Q.shape[0]
    Lam = np.vstack([np.eye(k), X])
    R = np.c_[np.eye(k) - Q @ X, Q]
    P = Lam @ R
    return {
        "R_Lambda_minus_I_max": float(np.abs(R @ Lam - np.eye(k)).max()),
        "Lambda_R_minus_P_max": float(np.abs(Lam @ R - P).max()),
        "row_sum_resid": float(np.abs(P @ np.ones(P.shape[0]) - 1.0).max()),
        "idem_resid": float(np.abs(P @ P - P).max()),
    }


def verify_from_factors(X: np.ndarray, Q: np.ndarray, label: str, params: dict[str, Any] | None = None) -> tuple[dict[str, Any], np.ndarray]:
    P = build_projection(X, Q)
    rec = verify_instance(P, label, params)
    rec["factor_residuals"] = factor_residuals(X, Q)
    if rec.get("gate") == "PASS":
        sig = rec.get("sigma_tilde") or 0.0
        rec["delta_over_sigma2"] = float(rec["delta"] / (sig * sig)) if sig > 0 else None
        rec["barrier_crossed"] = bool(rec["delta"] <= 0.25 and (rec.get("sigma_tilde_over_tau") or 0.0) > 1.0)
    return rec, P


def compact_record(rec: dict[str, Any] | None) -> dict[str, Any] | None:
    if not rec:
        return None
    keys = [
        "label",
        "gate",
        "n",
        "delta",
        "tau",
        "rho",
        "kappa",
        "W",
        "v",
        "H",
        "H_over_delta",
        "H_over_tau",
        "sigma_tilde",
        "sigma_tilde_over_tau",
        "delta_over_sigma2",
        "barrier_crossed",
        "antecedent_realized",
        "P_vv",
        "nu_v",
        "hidden_vertices",
        "best_component",
        "quotient",
    ]
    out = {k: rec.get(k) for k in keys if k in rec}
    if "params" in rec:
        out["params"] = rec.get("params")
    return out


@dataclass
class Candidate:
    score: float
    rec: dict[str, Any]
    P: np.ndarray
    X: np.ndarray | None = None
    Q: np.ndarray | None = None


def branch_score(rec: dict[str, Any]) -> float:
    if rec.get("gate") != "PASS" or rec.get("delta", math.inf) > 0.25:
        return -1e100
    sig = rec.get("sigma_tilde_over_tau") or 0.0
    h = rec.get("H_over_tau") or 0.0
    if sig <= 1.0:
        return -1e6 + sig + 0.01 * h
    return 100.0 * h + 2.0 * min(sig, 3.0)


def record_point(rec: dict[str, Any], source: str) -> dict[str, Any]:
    out = compact_record(rec) or {}
    out["source"] = source
    return out


def scale_project(X: np.ndarray, Qdir: np.ndarray, scales: np.ndarray, label: str) -> tuple[Candidate | None, list[dict[str, Any]]]:
    best: Candidate | None = None
    points = []
    for s in scales:
        rec, P = verify_from_factors(X, float(s) * Qdir, label, {"scale": float(s)})
        if rec.get("gate") == "PASS":
            points.append(record_point(rec, label))
        sc = branch_score(rec)
        if sc > -1e90 and (best is None or sc > best.score):
            best = Candidate(sc, rec, P, X.copy(), float(s) * Qdir)
    return best, points


def warm_continuation(X0: np.ndarray, Q0: np.ndarray, rng: np.random.Generator, iters: int) -> dict[str, Any]:
    points: list[dict[str, Any]] = []
    accepted: list[dict[str, Any]] = []
    scales = np.r_[np.linspace(0.18, 3.95, 70), np.linspace(3.2, 4.05, 36), np.linspace(0.08, 6.0, 36)]
    base_best, p0 = scale_project(X0, Q0, scales, "w16_scale_path")
    points.extend(p0)
    if base_best is None:
        raise RuntimeError("w16 scale projection found no feasible branch point")
    current = base_best
    global_best = base_best
    accepted.append(record_point(current.rec, "warm_start_best"))

    m, k = X0.shape
    step_grid = [0.002, 0.005, 0.01, 0.02, 0.04, -0.002, -0.005, -0.01]
    for it in range(iters):
        Xbase = current.X.copy() if current.X is not None else X0.copy()
        Qbase = current.Q.copy() if current.Q is not None else Q0.copy()
        proposals: list[tuple[np.ndarray, np.ndarray, str]] = []

        # Random tangent steps in X, preserving each row sum by reconstructing the last column.
        for amp in (0.002, 0.007, 0.02):
            X = Xbase.copy()
            noise = rng.normal(size=(m, k - 1))
            X[:, :-1] += amp * noise
            X[:, -1] = 1.0 - X[:, :-1].sum(axis=1)
            proposals.append((X, Qbase, f"homotopy_randomX_a{amp:g}"))

        # Targeted height pushes on every hidden-row coordinate.
        for h in range(min(m, 2)):
            for c in range(k):
                for eps in (0.004, 0.012, -0.004):
                    X = Xbase.copy()
                    donors = [j for j in range(k) if j != c]
                    X[h, c] -= eps
                    X[h, donors] += eps / len(donors)
                    X[h, -1] += 1.0 - X[h].sum()
                    proposals.append((X, Qbase, f"homotopy_push_h{h}_c{c}_e{eps:g}"))

        # Small Q-direction perturbations to let the sigma gate re-balance.
        for amp in (0.004, 0.015):
            proposals.append((Xbase.copy(), Qbase + amp * rng.normal(size=Qbase.shape), f"homotopy_randomQ_a{amp:g}"))

        local_best = current
        for X, Qdir, tag in proposals:
            norm = np.linalg.norm(Qdir)
            if not np.isfinite(norm) or norm <= 1e-12:
                continue
            scan = np.r_[np.linspace(0.72, 1.08, 7), np.linspace(0.45, 1.35, 9), np.linspace(0.25, 1.65, 7)]
            cand, pts = scale_project(X, Qdir, scan, tag)
            points.extend(pts)
            if cand and cand.score > local_best.score + 1e-10:
                local_best = cand
        current = local_best
        if current.score > global_best.score + 1e-10:
            global_best = current
            accepted.append(record_point(current.rec, f"accepted_iter_{it}"))
        elif it % 5 == 4:
            accepted.append(record_point(current.rec, f"stall_iter_{it}"))

    return {
        "points": points,
        "accepted": accepted,
        "best": global_best,
    }


def embed_factors(X0: np.ndarray, Q0: np.ndarray, n: int, k: int, rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    old_m, old_k = X0.shape
    m = n - k
    X = rng.dirichlet(np.ones(k), size=m)
    copy_m = min(old_m, m)
    copy_k = min(old_k, k)
    X[:copy_m, :copy_k] = X0[:copy_m, :copy_k]
    if k > old_k:
        X[:copy_m, old_k:] = 0.0
    X[:copy_m, -1] += 1.0 - X[:copy_m].sum(axis=1)
    Q = np.zeros((k, m))
    Q[:copy_k, :copy_m] = Q0[:copy_k, :copy_m]
    return X, Q


def larger_dimension_search(X0: np.ndarray, Q0: np.ndarray, rng: np.random.Generator, trials: int) -> dict[str, Any]:
    shapes = [(8, 4), (9, 4), (10, 5), (12, 6)]
    out: dict[str, Any] = {}
    all_points = []
    best: Candidate | None = None
    for n, k in shapes:
        shape = f"n{n}_k{k}"
        Xbase, Qbase = embed_factors(X0, Q0, n, k, rng)
        points = []
        shape_best: Candidate | None = None
        base_scales = np.r_[np.linspace(0.4, 1.25, 45), np.linspace(0.05, 2.5, 50)]
        cand, pts = scale_project(Xbase, Qbase, base_scales, f"embed_{shape}")
        points.extend(pts)
        if cand:
            shape_best = cand
            if best is None or cand.score > best.score:
                best = cand
        for t in range(trials):
            X = Xbase.copy()
            Q = Qbase.copy()
            ax = 10 ** rng.uniform(-3.5, -1.2)
            aq = 10 ** rng.uniform(-3.4, -1.0)
            X[:, :-1] += ax * rng.normal(size=X[:, :-1].shape)
            X[:, -1] = 1.0 - X[:, :-1].sum(axis=1)
            Q += aq * rng.normal(size=Q.shape)
            # Bias one hidden row outside the simplex and one new column into return flow.
            h = int(rng.integers(0, n - k))
            c = int(rng.integers(0, k))
            eps = 10 ** rng.uniform(-3.2, -1.0)
            X[h, c] -= eps
            X[h, np.arange(k) != c] += eps / (k - 1)
            X[h, -1] += 1.0 - X[h].sum()
            cand, pts = scale_project(X, Q, np.linspace(0.3, 1.6, 26), f"larger_{shape}")
            points.extend(pts)
            if cand and (shape_best is None or cand.score > shape_best.score):
                shape_best = cand
            if cand and (best is None or cand.score > best.score):
                best = cand
        out[shape] = {
            "num_points": len(points),
            "best": compact_record(shape_best.rec) if shape_best else None,
        }
        all_points.extend(points)
    return {"by_shape": out, "points": all_points, "best": best}


def direct_sum(P: np.ndarray, Q: np.ndarray) -> np.ndarray:
    n = P.shape[0]
    m = Q.shape[0]
    out = np.zeros((n + m, n + m))
    out[:n, :n] = P
    out[n:, n:] = Q
    return out


def row_sum_similarity(P: np.ndarray, rng: np.random.Generator, eps: float) -> np.ndarray | None:
    n = P.shape[0]
    K = rng.normal(size=(n, n))
    K -= K.mean(axis=1, keepdims=True)
    A = np.eye(n) + eps * K
    try:
        Ainv = np.linalg.inv(A)
    except np.linalg.LinAlgError:
        return None
    return A @ P @ Ainv


def coupling_search(P_w16: np.ndarray, rng: np.random.Generator, trials: int) -> dict[str, Any]:
    corner_payload = json.loads(CORNER.read_text())
    P_corner = np.array(corner_payload["P"], dtype=float)
    P_sum = direct_sum(P_w16, P_corner)
    points = []
    best: Candidate | None = None
    for label, P in (("direct_sum_w16_corner", P_sum), ("w16_only_similarity_base", P_w16)):
        rec = verify_instance(P, label)
        points.append(record_point(rec, label))
        sc = branch_score(rec)
        if sc > -1e90 and (best is None or sc > best.score):
            best = Candidate(sc, rec, P)
    eps_grid = list(np.geomspace(5e-4, 0.18, 18))
    for t in range(trials):
        eps = float(eps_grid[t % len(eps_grid)] * math.exp(rng.normal(0.0, 0.25)))
        base = P_sum if t % 3 != 0 else P_w16
        P = row_sum_similarity(base, rng, eps)
        if P is None:
            continue
        _, delta = neg_mass(P)
        if delta > 0.32:
            continue
        rec = verify_instance(P, "coupled_similarity", {"eps": eps, "base": "sum" if base is P_sum else "w16"})
        if rec.get("gate") == "PASS":
            points.append(record_point(rec, "coupled_similarity"))
        sc = branch_score(rec)
        if sc > -1e90 and (best is None or sc > best.score):
            best = Candidate(sc, rec, P)
    return {
        "points": points,
        "best": best,
        "corner_source_summary": {
            "delta": corner_payload.get("delta"),
            "H_over_tau": corner_payload.get("H_over_tau"),
            "sigma_tilde_note": "formal sigma recomputed by verifier in direct sum",
        },
    }


def reverse_frontier(points: list[dict[str, Any]]) -> dict[str, Any]:
    levels = [0.05, 0.1, 0.2]
    out: dict[str, Any] = {}
    valid = [p for p in points if p.get("gate") == "PASS" and p.get("delta", math.inf) <= 0.25]
    for h0 in levels:
        eligible = [p for p in valid if (p.get("H_over_tau") or 0.0) >= h0]
        if eligible:
            best = max(eligible, key=lambda p: p.get("sigma_tilde_over_tau") or -1)
            out[str(h0)] = {
                "num_eligible": len(eligible),
                "max_sigma_over_tau": best.get("sigma_tilde_over_tau"),
                "record": best,
            }
        else:
            out[str(h0)] = {"num_eligible": 0, "max_sigma_over_tau": None, "record": None}
    sig_bins = [(0.0, 0.5), (0.5, 0.75), (0.75, 1.0), (1.0, 1.25), (1.25, 1.75), (1.75, 10.0)]
    by_sig = []
    for lo, hi in sig_bins:
        eligible = [p for p in valid if lo <= (p.get("sigma_tilde_over_tau") or 0.0) < hi]
        if eligible:
            best = max(eligible, key=lambda p: p.get("H_over_tau") or -1)
            by_sig.append({"sigma_bin": [lo, hi], "num": len(eligible), "max_H_over_tau": best.get("H_over_tau"), "record": best})
        else:
            by_sig.append({"sigma_bin": [lo, hi], "num": 0, "max_H_over_tau": None, "record": None})
    out["max_H_by_sigma_bin"] = by_sig
    return out


def fit_boundary(points: list[dict[str, Any]]) -> dict[str, Any]:
    valid = [
        p
        for p in points
        if p.get("gate") == "PASS"
        and p.get("delta", math.inf) <= 0.25
        and (p.get("H") or 0.0) > 1e-10
        and (p.get("sigma_tilde") or 0.0) > 0
    ]
    if not valid:
        return {"num_valid": 0}
    delta = np.array([p["delta"] for p in valid])
    H = np.array([p["H"] for p in valid])
    sig_ratio = np.array([p.get("sigma_tilde_over_tau") or 0.0 for p in valid])
    H_tau = np.array([p.get("H_over_tau") or 0.0 for p in valid])
    # Robust-ish slopes through origin for the linear law delta >= c H.
    c_med = float(np.median(delta / H))
    c_min = float(np.min(delta / H))
    # A sigma-aware obstruction score: H/tau * max(1, sigma/tau).
    prod = H_tau * np.maximum(1.0, sig_ratio)
    branch = [p for p in valid if (p.get("sigma_tilde_over_tau") or 0.0) > 1.0]
    return {
        "num_valid": len(valid),
        "linear_delta_over_H_min": c_min,
        "linear_delta_over_H_median": c_med,
        "max_H_over_tau": float(np.max(H_tau)),
        "max_sigma_over_tau": float(np.max(sig_ratio)),
        "max_H_over_tau_times_max1sigma": float(np.max(prod)),
        "branch_sigma_gt_tau": {
            "num": len(branch),
            "max_H_over_tau": max((p.get("H_over_tau") or 0.0) for p in branch) if branch else None,
            "min_delta_over_H": min((p.get("delta") or math.inf) / (p.get("H") or math.inf) for p in branch) if branch else None,
            "best": max(branch, key=lambda p: p.get("H_over_tau") or -1) if branch else None,
        },
    }


def save_candidate(outdir: Path, name: str, cand: Candidate | None) -> None:
    if cand is None:
        return
    (outdir / f"{name}_certificate.json").write_text(json.dumps(finite(cand.rec), indent=2))
    np.savetxt(outdir / f"{name}_matrix.txt", cand.P, fmt="%.17g")
    (outdir / f"{name}_matrix.json").write_text(json.dumps(finite(cand.P), indent=2))
    if cand.X is not None and cand.Q is not None:
        payload = {
            "X_hidden_rows": cand.X,
            "Q": cand.Q,
            "P": cand.P,
            "rank_k": int(cand.Q.shape[0]),
            "n": int(cand.P.shape[0]),
            "factor_residuals": factor_residuals(cand.X, cand.Q),
        }
        (outdir / f"{name}_factorization.json").write_text(json.dumps(finite(payload), indent=2))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default=".")
    ap.add_argument("--seed", type=int, default=1717)
    ap.add_argument("--homotopy-iters", type=int, default=5)
    ap.add_argument("--larger-trials", type=int, default=6)
    ap.add_argument("--coupling-trials", type=int, default=18)
    args = ap.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(args.seed)
    t0 = time.time()

    X0, Q0 = load_w16()
    warm = warm_continuation(X0, Q0, rng, args.homotopy_iters)
    P_w16 = build_projection(X0, Q0)
    larger = larger_dimension_search(X0, Q0, rng, args.larger_trials)
    coupling = coupling_search(P_w16, rng, args.coupling_trials)

    all_points: list[dict[str, Any]] = []
    all_points.extend(warm["points"])
    all_points.extend(warm["accepted"])
    all_points.extend(larger["points"])
    all_points.extend(coupling["points"])

    candidates = [warm["best"], larger["best"], coupling["best"]]
    candidates = [c for c in candidates if c is not None]
    best_branch = max(candidates, key=lambda c: c.score) if candidates else None
    realized = [c for c in candidates if c.rec.get("antecedent_realized")]
    best_realized = max(realized, key=lambda c: c.rec.get("H_over_tau") or -1) if realized else None

    # Full hiddenness LP certificate for the best branch/realized candidate.
    for cand in [best_branch, best_realized]:
        if cand is None or cand.rec.get("gate") != "PASS":
            continue
        v = int(cand.rec["v"])
        cand.rec["hiddenness_lp_certificate"] = exposedness_lp_certificate(cand.P, v, cand.rec["rho"], cand.rec["kappa"])

    frontier = {
        "created": time.strftime("%Y-%m-%d %H:%M:%S"),
        "elapsed_seconds": time.time() - t0,
        "seed": args.seed,
        "warm": {
            "accepted": warm["accepted"],
            "best": compact_record(warm["best"].rec) if warm["best"] else None,
            "num_points": len(warm["points"]),
        },
        "larger": {
            "by_shape": larger["by_shape"],
            "best": compact_record(larger["best"].rec) if larger["best"] else None,
        },
        "coupling": {
            "best": compact_record(coupling["best"].rec) if coupling["best"] else None,
            "corner_source_summary": coupling["corner_source_summary"],
        },
        "reverse_frontier": reverse_frontier(all_points),
        "fit": fit_boundary(all_points),
        "best_branch": compact_record(best_branch.rec) if best_branch else None,
        "best_realized": compact_record(best_realized.rec) if best_realized else None,
        "verdict": "ANTECEDENT_REALIZED" if best_realized else "NOT_REALIZED",
    }
    (outdir / "w17_pareto_front.json").write_text(json.dumps(finite(frontier), indent=2))
    (outdir / "w17_points.json").write_text(json.dumps(finite(all_points), indent=2))
    save_candidate(outdir, "w17_best_branch", best_branch)
    save_candidate(outdir, "w17_best_realized", best_realized)

    console_summary = {
        "verdict": frontier["verdict"],
        "elapsed_seconds": frontier["elapsed_seconds"],
        "best_branch": frontier["best_branch"],
        "best_realized": frontier["best_realized"],
        "reverse_frontier": frontier["reverse_frontier"],
        "fit": frontier["fit"],
        "artifacts": {
            "pareto": str(outdir / "w17_pareto_front.json"),
            "points": str(outdir / "w17_points.json"),
        },
    }
    print(json.dumps(finite(console_summary), indent=2))


if __name__ == "__main__":
    main()
