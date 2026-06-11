#!/usr/bin/env python3
"""
w15_refuter_search.py

Numerical refuter for the kernel/path-product floor question.

The script builds exact signed idempotents in three ways:
  1. LP-financed frame completions:
       Lambda = [I; L], R = [I - QL | Q], P = Lambda R, LQ = B.
     For fixed hidden geometry L and requested hidden-hidden block B, Q is chosen by
     a linear program minimizing row negative mass. This is the direct test of
     whether cancellation can avoid the old left-inverse tax.
  2. Positive-diagonal variants of the same frame, testing the self-mass loophole.
  3. Similarity conjugations of stochastic idempotents, P = A P0 A^{-1}, A1=1.

Every reported instance is verified from P itself:
  P1=1, P^2=P, robust multiplicity-correct W, hidden top vertex, H,
  sigma_tilde with the self term included, canonical shallow band components,
  path products, and row negative mass delta.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


np.set_printoptions(precision=8, suppress=True, linewidth=220)

C_RHO = 4.0
C_KAPPA = 0.25
LP_TOL = 1e-9


def robust_linprog(c, A_ub=None, b_ub=None, A_eq=None, b_eq=None, bounds=None, presolve=True):
    last = None
    for meth, pre in (("highs-ipm", presolve), ("highs", presolve), ("highs-ds", presolve),
                      ("highs-ipm", False), ("highs", False)):
        r = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                    bounds=bounds, method=meth, options={"presolve": pre})
        if r.success:
            return r
        last = r
        if getattr(r, "status", None) == 2:
            return r
    return last


def check_idempotent(P, tol=1e-8):
    P = np.asarray(P, float)
    n = P.shape[0]
    row_sum_resid = float(np.abs(P @ np.ones(n) - 1.0).max())
    idem_resid = float(np.abs(P @ P - P).max())
    return {
        "row_sum_resid": row_sum_resid,
        "idem_resid": idem_resid,
        "ok": bool(row_sum_resid < tol and idem_resid < tol),
    }


def neg_mass(P):
    nm = np.maximum(-np.asarray(P, float), 0.0).sum(axis=1)
    return nm, float(nm.max())


def dist1_to_conv(rows, W_idx, i):
    rows = np.asarray(rows, float)
    n, d = rows.shape
    if len(W_idx) == 0:
        return math.inf, None
    A = rows[W_idx].T
    b = rows[i]
    m = len(W_idx)
    nv = m + d
    c = np.concatenate([np.zeros(m), np.ones(d)])
    A_ub = []
    b_ub = []
    for j in range(d):
        rp = np.zeros(nv)
        rp[:m] = A[j]
        rp[m + j] = -1.0
        A_ub.append(rp)
        b_ub.append(b[j])
        rn = np.zeros(nv)
        rn[:m] = -A[j]
        rn[m + j] = -1.0
        A_ub.append(rn)
        b_ub.append(-b[j])
    A_eq = np.zeros((1, nv))
    A_eq[0, :m] = 1.0
    bounds = [(0, None)] * m + [(0, None)] * d
    res = robust_linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                         A_eq=A_eq, b_eq=[1.0], bounds=bounds)
    if res is None or not res.success:
        return math.inf, None
    return float(res.fun), res.x[:m]


def is_row_vertex_robust(rows, i, tol=1e-7, dup_tol=1e-9):
    rows = np.asarray(rows, float)
    n, d = rows.shape
    v = rows[i]
    others = [k for k in range(n) if k != i and np.abs(rows[k] - v).sum() > dup_tol]
    if not others:
        return True, 0.0
    A = rows[others].T
    m = len(others)
    nv = m + d
    c = np.concatenate([np.zeros(m), np.ones(d)])
    A_ub = []
    b_ub = []
    for j in range(d):
        rp = np.zeros(nv)
        rp[:m] = A[j]
        rp[m + j] = -1.0
        A_ub.append(rp)
        b_ub.append(v[j])
        rn = np.zeros(nv)
        rn[:m] = -A[j]
        rn[m + j] = -1.0
        A_ub.append(rn)
        b_ub.append(-v[j])
    A_eq = np.zeros((1, nv))
    A_eq[0, :m] = 1.0
    res = robust_linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                         A_eq=A_eq, b_eq=[1.0],
                         bounds=[(0, None)] * m + [(0, None)] * d)
    if res is None or not res.success:
        return True, math.inf
    return bool(res.fun > tol), float(res.fun)


def exposed_margin(rows, i, rho, kappa):
    rows = np.asarray(rows, float)
    n, d = rows.shape
    di = np.abs(rows - rows[i]).sum(axis=1)
    far = [k for k in range(n) if k != i and di[k] >= rho - 1e-12]
    if not far:
        return True, math.inf, {"far": 0}
    nv = d + 2
    c = np.zeros(nv)
    c[-1] = -1.0
    A_ub = []
    b_ub = []

    def hvec(k):
        v = np.zeros(nv)
        v[:d] = rows[k]
        v[d] = 1.0
        return v

    for k in range(n):
        hk = hvec(k)
        A_ub.append(hk.copy())
        b_ub.append(1.0)
        A_ub.append(-hk.copy())
        b_ub.append(0.0)
    for k in far:
        hk = hvec(k)
        row = -hk
        row[-1] = 1.0
        A_ub.append(row)
        b_ub.append(0.0)
    A_eq = [hvec(i)]
    bounds = [(None, None)] * d + [(None, None), (None, 1.0)]
    res = None
    for meth, pre in (("highs-ipm", False), ("highs", False), ("highs-ds", False),
                      ("highs-ipm", True)):
        r = linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                    A_eq=np.array(A_eq), b_eq=[0.0], bounds=bounds,
                    method=meth, options={"presolve": pre})
        if r.success:
            res = r
            break
    if res is None:
        return False, None, {"far": len(far), "solver_failed": True}
    tstar = -float(res.fun)
    return bool(tstar >= kappa - 1e-9), tstar, {"far": len(far)}


def well_exposed_set_robust(rows, rho, kappa):
    W = []
    info = {}
    for i in range(len(rows)):
        vert, verr = is_row_vertex_robust(rows, i)
        if not vert:
            info[i] = {"vertex": False, "verr": verr}
            continue
        ok, margin, ex = exposed_margin(rows, i, rho, kappa)
        info[i] = {"vertex": True, "exposed": ok, "margin": margin, **ex}
        if ok:
            W.append(i)
    return W, info


def canonical_separator(P, W, v):
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
    res = robust_linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                         bounds=[(-1, 1)] * n + [(None, None)], presolve=False)
    if res is None or not res.success:
        raise RuntimeError("canonical separator LP failed")
    w = res.x[:n]
    s = res.x[n]
    phi = P @ w - s
    H = float(phi[v])
    g = H - phi
    Omega = float(g.max() - g.min())
    return w, s, phi, H, g, Omega


def tarjan_scc(vertices, adj):
    index = 0
    stack = []
    onstack = set()
    indices = {}
    lowlink = {}
    comps = []

    def strongconnect(v):
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


def component_path_product(P, comp, edge_tol=1e-12):
    comp = list(comp)
    m = len(comp)
    if m <= 1:
        return 1.0, 0
    idx = {v: a for a, v in enumerate(comp)}
    # Shortest directed lengths for the diameter.
    dist = np.full((m, m), np.inf)
    best = np.zeros((m, m))
    for a in range(m):
        dist[a, a] = 0
        best[a, a] = 1.0
    for i in comp:
        a = idx[i]
        for j in comp:
            p = P[i, j]
            if p > edge_tol:
                b = idx[j]
                dist[a, b] = min(dist[a, b], 1)
                best[a, b] = max(best[a, b], float(p))
    # Floyd-Warshall for shortest lengths.
    for k in range(m):
        for i in range(m):
            for j in range(m):
                if dist[i, k] + dist[k, j] < dist[i, j]:
                    dist[i, j] = dist[i, k] + dist[k, j]
    L = int(np.max(dist[np.isfinite(dist)]))
    # Widest product over simple paths is enough for the thin-chain diagnostic.
    # Dynamic programming over path lengths up to m-1.
    cur = best.copy()
    out = best.copy()
    for _ in range(2, m + 1):
        nxt = np.zeros((m, m))
        for i in range(m):
            for k in range(m):
                if cur[i, k] <= 0:
                    continue
                vals = cur[i, k] * best[k, :]
                nxt[i, :] = np.maximum(nxt[i, :], vals)
        out = np.maximum(out, nxt)
        cur = nxt
    off = [out[i, j] for i in range(m) for j in range(m) if i != j]
    Pi = float(min(off)) if off else 1.0
    return Pi, L


def shallow_components(P, v, W, g, Omega, tau, kappa, thresholds=None):
    n = P.shape[0]
    if thresholds is None:
        thresholds = [0.5 * kappa * Omega, 0.75 * kappa * Omega, kappa * Omega]
    records = []
    for t in thresholds:
        S = [i for i in range(n) if g[i] < t + 1e-12]
        Sset = set(S)
        adj = {i: [j for j in S if P[i, j] > 1e-12] for i in S}
        comps = tarjan_scc(S, adj)
        for comp in comps:
            mass_from_v = float(sum(max(P[v, j], 0.0) for j in comp))
            if mass_from_v <= 1e-12:
                continue
            Pi, L = component_path_product(P, comp)
            records.append({
                "t": float(t),
                "t_over_kappaOmega": float(t / (kappa * Omega)) if kappa * Omega > 0 else None,
                "component": [int(x) for x in comp],
                "size": len(comp),
                "mass_from_v": mass_from_v,
                "Pi_C": Pi,
                "L": L,
                "Pi_over_tau": float(Pi / tau) if tau > 0 else None,
                "min_edge": float(min((P[i, j] for i in comp for j in comp if P[i, j] > 1e-12),
                                      default=0.0)),
            })
    records.sort(key=lambda r: (r["Pi_C"], r["size"]))
    return records


def sigma_tilde_def(P, W, v):
    outside = []
    dists = []
    for j in range(P.shape[0]):
        d, _ = dist1_to_conv(P, W, j)
        dists.append(float(d))
        if d > 1e-9:
            outside.append(j)
    sig = float(sum(max(P[v, j], 0.0) for j in outside))
    return sig, outside, dists


def verify_instance(P, label, params=None):
    P = np.asarray(P, float)
    chk = check_idempotent(P)
    nm, delta = neg_mass(P)
    rec = {
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
    W, winfo = well_exposed_set_robust(P, rho, kappa)
    rec.update({"tau": tau, "rho": rho, "kappa": kappa, "W": [int(x) for x in W],
                "nW": len(W)})
    if not W:
        rec["gate"] = "FAIL_W_empty"
        return rec
    hidden_vertices = []
    maxH = -1.0
    vbest = -1
    dists_to_W = []
    vertex_info = {}
    for i in range(P.shape[0]):
        d, _ = dist1_to_conv(P, W, i)
        dists_to_W.append(float(d))
        vert, verr = is_row_vertex_robust(P, i)
        vertex_info[i] = {"vertex": bool(vert), "verr": float(verr) if np.isfinite(verr) else None,
                          "inW": i in W, "dist_to_CW": float(d),
                          "exposed_margin": winfo.get(i, {}).get("margin")}
        if vert and i not in W and d > 1e-9:
            hidden_vertices.append(i)
            if d > maxH:
                maxH = d
                vbest = i
    rec["vertex_info"] = {int(k): v for k, v in vertex_info.items()}
    rec["hidden_vertices"] = [int(x) for x in hidden_vertices]
    rec["all_dist_to_CW"] = dists_to_W
    if vbest < 0:
        rec["gate"] = "FAIL_no_hidden_vertex"
        rec["H"] = 0.0
        return rec
    sig, outside, outside_dists = sigma_tilde_def(P, W, vbest)
    w, s, phi, H, g, Omega = canonical_separator(P, W, vbest)
    comps = shallow_components(P, vbest, W, g, Omega, tau, kappa)
    rec.update({
        "gate": "PASS",
        "v": int(vbest),
        "H": float(maxH),
        "H_separator": float(H),
        "H_over_delta": float(maxH / delta) if delta > 0 else None,
        "H_over_tau": float(maxH / tau) if tau > 0 else None,
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
    })
    if comps:
        rec["best_Pi_over_tau"] = comps[0]["Pi_over_tau"]
    return rec


def build_P_from_LBQ(L, B, Q):
    L = np.asarray(L, float)
    B = np.asarray(B, float)
    Q = np.asarray(Q, float)
    r = L.shape[1]
    A = np.eye(r) - Q @ L
    top = np.concatenate([A, Q], axis=1)
    bottom = np.concatenate([L @ A, B], axis=1)
    return np.concatenate([top, bottom], axis=0)


def optimize_Q_for_LB(L, B, q_bound=50.0):
    L = np.asarray(L, float)
    B = np.asarray(B, float)
    m, r = L.shape
    n = r + m
    nq = r * m
    nentries = n * n
    D_idx = nq + nentries
    nv = D_idx + 1

    def q_index(a, h):
        return a * m + h

    def entry_expr(row, col):
        const = 0.0
        coeff = np.zeros(nq)
        if row < r and col < r:
            const = 1.0 if row == col else 0.0
            for h in range(m):
                coeff[q_index(row, h)] -= L[h, col]
        elif row < r and col >= r:
            h = col - r
            coeff[q_index(row, h)] = 1.0
        elif row >= r and col < r:
            i = row - r
            const = L[i, col] - float(B[i, :] @ L[:, col])
        else:
            i = row - r
            h = col - r
            const = B[i, h]
        return const, coeff

    c = np.zeros(nv)
    c[D_idx] = 1.0
    A_eq = []
    b_eq = []
    # LQ = B.
    for i in range(m):
        for h in range(m):
            row = np.zeros(nv)
            for a in range(r):
                row[q_index(a, h)] = L[i, a]
            A_eq.append(row)
            b_eq.append(B[i, h])
    A_ub = []
    b_ub = []
    entry_no = 0
    row_slacks = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            z = nq + entry_no
            row_slacks[i].append(z)
            const, coeff = entry_expr(i, j)
            # z >= -entry  <=> -z - coeff*q <= const
            row = np.zeros(nv)
            row[:nq] = -coeff
            row[z] = -1.0
            A_ub.append(row)
            b_ub.append(const)
            entry_no += 1
    for i in range(n):
        row = np.zeros(nv)
        for z in row_slacks[i]:
            row[z] = 1.0
        row[D_idx] = -1.0
        A_ub.append(row)
        b_ub.append(0.0)
    bounds = [(-q_bound, q_bound)] * nq + [(0, None)] * nentries + [(0, None)]
    res = robust_linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                         A_eq=np.array(A_eq), b_eq=np.array(b_eq),
                         bounds=bounds)
    if res is None or not res.success:
        return None, {"lp_success": False, "message": getattr(res, "message", None)}
    Q = res.x[:nq].reshape((r, m))
    P = build_P_from_LBQ(L, B, Q)
    nm, delta = neg_mass(P)
    return P, {"lp_success": True, "lp_delta": float(res.fun), "actual_delta": float(delta),
               "Q": Q.tolist()}


def s5_family_L(a, y0, sep, m_hidden=2):
    ys = [y0 + sep * i for i in range(m_hidden)]
    L = []
    for y in ys:
        L.append([-a, y, 1.0 + a - y])
    return np.array(L, float)


def random_L(r, m, rng, a_scale=0.01, a_spread=0.5):
    L = []
    for _ in range(m):
        a = a_scale * math.exp(rng.normal(0.0, a_spread))
        probs = rng.dirichlet(np.ones(r - 1))
        row = np.empty(r)
        row[0] = -a
        row[1:] = (1.0 + a) * probs
        L.append(row)
    return np.array(L)


def cycle_B(m, edge, neg_back=0.0, diag=0.0, diagonal_vertex=None):
    B = np.zeros((m, m))
    for i in range(m):
        B[i, (i + 1) % m] = edge
        if neg_back:
            B[i, (i - 1) % m] -= neg_back
        if diag:
            B[i, i] += diag
    if diagonal_vertex is not None:
        B[diagonal_vertex, diagonal_vertex] += diag if diag == 0 else 0.0
    return B


def chain_return_B(m, edge, ret, neg_cancel=0.0, diag0=0.0):
    B = np.zeros((m, m))
    for i in range(m - 1):
        B[i, i + 1] = edge
        if neg_cancel and i > 0:
            B[i, i - 1] = -neg_cancel
    B[m - 1, 0] = ret
    if diag0:
        B[0, 0] = diag0
    return B


def stochastic_idempotent(n, k, rng):
    P0 = np.zeros((n, n))
    for a in range(k):
        P0[a, a] = 1.0
    for i in range(k, n):
        probs = rng.dirichlet(np.ones(k))
        P0[i, :k] = probs
    return P0


def random_conjugate_instance(n, k, rng, eps):
    P0 = stochastic_idempotent(n, k, rng)
    K = rng.normal(size=(n, n))
    K -= K.mean(axis=1, keepdims=True)  # K 1 = 0, hence A 1 = 1.
    # Dampen the recurrent block less often; this preserves a recognizable base.
    K *= rng.choice([0.2, 0.5, 1.0])
    A = np.eye(n) + eps * K
    try:
        Ainv = np.linalg.inv(A)
    except np.linalg.LinAlgError:
        return None
    P = A @ P0 @ Ainv
    return P


@dataclass
class SearchState:
    best_score: float
    best_record: dict | None
    best_P: np.ndarray | None
    best_regime_score: float
    best_regime_record: dict | None
    best_regime_P: np.ndarray | None
    best_branch_score: float
    best_branch_record: dict | None
    best_branch_P: np.ndarray | None
    counts: dict


def score_record(rec):
    if rec.get("gate") != "PASS":
        return -1e9
    if rec.get("delta", math.inf) > 0.25:
        return -1e6 + (rec.get("H_over_tau") or 0.0)
    sig_ratio = rec.get("sigma_tilde_over_tau") or 0.0
    h_tau = rec.get("H_over_tau") or 0.0
    h_delta = rec.get("H_over_delta") or 0.0
    pi_tau = rec.get("best_Pi_over_tau")
    pi_bonus = 0.0 if pi_tau is None else max(0.0, 1.0 - min(pi_tau, 1.0))
    # Prioritize entering the sigma>tau branch, then height.
    return 20.0 * min(sig_ratio, 2.0) + 5.0 * h_tau + 0.05 * min(h_delta, 200.0) + pi_bonus


def consider(state, P, label, params):
    rec = verify_instance(P, label, params=params)
    state.counts["verified"] = state.counts.get("verified", 0) + 1
    state.counts[rec.get("gate", "UNKNOWN")] = state.counts.get(rec.get("gate", "UNKNOWN"), 0) + 1
    sc = score_record(rec)
    if sc > state.best_score:
        state.best_score = sc
        state.best_record = rec
        state.best_P = np.array(P)
        print(
            f"[best] {label} score={sc:.3f} gate={rec.get('gate')} "
            f"delta={rec.get('delta'):.4g} H/tau={rec.get('H_over_tau')} "
            f"H/delta={rec.get('H_over_delta')} sig/tau={rec.get('sigma_tilde_over_tau')} "
            f"Pi/tau={rec.get('best_Pi_over_tau')}",
            flush=True,
        )
    if rec.get("gate") == "PASS" and rec.get("delta", math.inf) <= 0.25:
        regime_score = score_record(rec)
        if regime_score > state.best_regime_score:
            state.best_regime_score = regime_score
            state.best_regime_record = rec
            state.best_regime_P = np.array(P)
        if (rec.get("sigma_tilde_over_tau") or 0.0) > 1.0:
            branch_score = 10.0 * (rec.get("H_over_tau") or 0.0) + 0.1 * min(rec.get("H_over_delta") or 0.0, 500.0)
            if branch_score > state.best_branch_score:
                state.best_branch_score = branch_score
                state.best_branch_record = rec
                state.best_branch_P = np.array(P)
                print(
                    f"[branch] {label} delta={rec.get('delta'):.4g} H/tau={rec.get('H_over_tau')} "
                    f"H/delta={rec.get('H_over_delta')} sig/tau={rec.get('sigma_tilde_over_tau')} "
                    f"Pi/tau={rec.get('best_Pi_over_tau')}",
                    flush=True,
                )
    return rec


def run_frame_search(state, rng, seconds):
    t0 = time.time()
    trials = 0
    while time.time() - t0 < seconds:
        trials += 1
        kind = rng.choice(["s5line", "cycle", "chain", "diagcycle"], p=[0.25, 0.35, 0.25, 0.15])
        if kind == "s5line":
            m = int(rng.choice([2, 3, 4]))
            a = 10 ** rng.uniform(-4.0, -0.8)
            y0 = rng.uniform(0.03, 0.45)
            sep = rng.uniform(0.03, min(0.35, (0.95 - y0) / max(m - 1, 1)))
            L = s5_family_L(a, y0, sep, m)
            edge = 10 ** rng.uniform(-4.0, -0.25)
            if m == 2:
                B = cycle_B(m, edge)
            else:
                B = cycle_B(m, edge, neg_back=10 ** rng.uniform(-5.0, -1.5) if rng.random() < 0.5 else 0.0)
        else:
            r = int(rng.choice([4, 5, 6]))
            m = int(rng.choice([3, 4, 5, 6]))
            a_scale = 10 ** rng.uniform(-4.0, -0.6)
            L = random_L(r, m, rng, a_scale=a_scale, a_spread=1.0)
            edge = 10 ** rng.uniform(-4.0, -0.2)
            if kind == "cycle":
                B = cycle_B(m, edge, neg_back=(edge * rng.uniform(0.02, 0.6) if rng.random() < 0.55 else 0.0))
            elif kind == "chain":
                ret = edge * rng.uniform(0.03, 0.8)
                B = chain_return_B(m, edge, ret, neg_cancel=(edge * rng.uniform(0.02, 0.6) if rng.random() < 0.5 else 0.0))
            else:
                diag = rng.uniform(0.1, 0.95)
                B = cycle_B(m, edge, neg_back=(edge * rng.uniform(0.02, 0.5) if rng.random() < 0.5 else 0.0),
                            diag=0.0)
                B[0, 0] = diag
                if m > 1:
                    B[0, 1] = max(B[0, 1], edge)
        opt = optimize_Q_for_LB(L, B, q_bound=100.0)
        if opt[0] is None:
            state.counts["frame_lp_fail"] = state.counts.get("frame_lp_fail", 0) + 1
            continue
        P, meta = opt
        params = {"kind": kind, "L": L.tolist(), "B": B.tolist(), **meta}
        consider(state, P, "frame_" + kind, params)
    state.counts["frame_trials"] = state.counts.get("frame_trials", 0) + trials


def run_structured_sweeps(state):
    # Deterministic maps around the known s5 seed, but with the LP-optimal completion.
    for m in [2, 3, 4, 5]:
        for a in [2e-4, 5e-4, 1e-3, 2e-3, 5e-3, 1e-2, 2e-2]:
            for edge in [2e-4, 5e-4, 1e-3, 2e-3, 5e-3, 1e-2, 2e-2, 5e-2, 0.1, 0.2]:
                sep = min(0.18, 0.8 / max(m - 1, 1))
                L = s5_family_L(a, 0.05, sep, m)
                for neg in [0.0, edge * 0.1, edge * 0.5]:
                    B = cycle_B(m, edge, neg_back=neg)
                    P, meta = optimize_Q_for_LB(L, B, q_bound=200.0)
                    if P is None:
                        continue
                    consider(state, P, "sweep_s5cycle",
                             {"m": m, "a": a, "edge": edge, "neg_back": neg,
                              "L": L.tolist(), "B": B.tolist(), **meta})
    # Positive diagonal self-mass probes.
    for a in [1e-4, 3e-4, 1e-3, 3e-3, 1e-2]:
        for diag in [0.2, 0.5, 0.8, 0.95]:
            for edge in [1e-4, 1e-3, 1e-2, 0.05]:
                L = random_L(4, 3, np.random.default_rng(int(a * 1e8 + diag * 1000 + edge * 1e6)),
                             a_scale=a, a_spread=0.15)
                B = cycle_B(3, edge)
                B[0, 0] = diag
                P, meta = optimize_Q_for_LB(L, B, q_bound=200.0)
                if P is None:
                    continue
                consider(state, P, "sweep_posdiag",
                         {"a": a, "diag": diag, "edge": edge,
                          "L": L.tolist(), "B": B.tolist(), **meta})


def run_conjugation_search(state, rng, seconds):
    t0 = time.time()
    trials = 0
    while time.time() - t0 < seconds:
        trials += 1
        n = int(rng.choice([5, 6, 7, 8]))
        k = int(rng.integers(2, min(5, n)))
        eps = 10 ** rng.uniform(-4.0, -0.2)
        P = random_conjugate_instance(n, k, rng, eps)
        if P is None:
            continue
        consider(state, P, "conjugate", {"n": n, "k": k, "eps": eps})
    state.counts["conj_trials"] = state.counts.get("conj_trials", 0) + trials


def save_outputs(state, outdir):
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    summary = {
        "created": time.strftime("%Y-%m-%d %H:%M:%S"),
        "counts": state.counts,
        "best_score": state.best_score,
        "best_record": state.best_record,
        "best_regime_score": state.best_regime_score,
        "best_regime_record": state.best_regime_record,
        "best_branch_score": state.best_branch_score,
        "best_branch_record": state.best_branch_record,
    }
    (outdir / "w15_summary.json").write_text(json.dumps(summary, indent=2, default=float))
    if state.best_P is not None:
        np.savetxt(outdir / "w15_best_matrix.txt", state.best_P, fmt="%.17g")
        (outdir / "w15_best_matrix.json").write_text(json.dumps(state.best_P.tolist(), indent=2))
    if state.best_regime_P is not None:
        np.savetxt(outdir / "w15_best_regime_matrix.txt", state.best_regime_P, fmt="%.17g")
        (outdir / "w15_best_regime_matrix.json").write_text(json.dumps(state.best_regime_P.tolist(), indent=2))
    if state.best_branch_P is not None:
        np.savetxt(outdir / "w15_best_branch_matrix.txt", state.best_branch_P, fmt="%.17g")
        (outdir / "w15_best_branch_matrix.json").write_text(json.dumps(state.best_branch_P.tolist(), indent=2))
    return summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seconds", type=float, default=90.0)
    ap.add_argument("--seed", type=int, default=1515)
    ap.add_argument("--outdir", default=".")
    ap.add_argument("--skip-sweeps", action="store_true")
    args = ap.parse_args()

    rng = np.random.default_rng(args.seed)
    state = SearchState(best_score=-1e18, best_record=None, best_P=None,
                        best_regime_score=-1e18, best_regime_record=None, best_regime_P=None,
                        best_branch_score=-1e18, best_branch_record=None, best_branch_P=None,
                        counts={})

    t0 = time.time()
    if not args.skip_sweeps:
        print("[stage] deterministic structured sweeps", flush=True)
        run_structured_sweeps(state)
    remaining = max(0.0, args.seconds - (time.time() - t0))
    frame_s = 0.72 * remaining
    conj_s = remaining - frame_s
    print(f"[stage] random LP-financed frames for {frame_s:.1f}s", flush=True)
    run_frame_search(state, rng, frame_s)
    print(f"[stage] random stochastic conjugations for {conj_s:.1f}s", flush=True)
    run_conjugation_search(state, rng, conj_s)

    summary = save_outputs(state, args.outdir)
    best = summary["best_record"]
    print("\n=== W15 SEARCH SUMMARY ===", flush=True)
    print(json.dumps({k: summary[k] for k in ["counts", "best_score"]}, indent=2), flush=True)
    if best:
        print("=== BEST CERTIFICATE (SCORING) ===", flush=True)
        keys = ["label", "gate", "n", "delta", "tau", "rho", "kappa", "W", "v", "H",
                "H_over_delta", "H_over_tau", "sigma_tilde", "sigma_tilde_over_tau",
                "P_vv", "nu_v", "best_component", "best_Pi_over_tau"]
        print(json.dumps({k: best.get(k) for k in keys}, indent=2, default=float), flush=True)
    for name in ["best_regime_record", "best_branch_record"]:
        rec = summary.get(name)
        if rec:
            print(f"=== {name} ===", flush=True)
            keys = ["label", "gate", "n", "delta", "tau", "rho", "kappa", "W", "v", "H",
                    "H_over_delta", "H_over_tau", "sigma_tilde", "sigma_tilde_over_tau",
                    "P_vv", "nu_v", "best_component", "best_Pi_over_tau"]
            print(json.dumps({k: rec.get(k) for k in keys}, indent=2, default=float), flush=True)


if __name__ == "__main__":
    main()
