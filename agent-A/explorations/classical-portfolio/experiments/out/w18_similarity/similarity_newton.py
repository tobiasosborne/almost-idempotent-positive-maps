#!/usr/bin/env python3
"""Corner-splitting and positivity/retraction experiments.

The script is intentionally self-contained.  It loads the certified w16
rational idempotent, builds a natural singleton-block H-M anchor from the saved
factorization, and compares two iterations:

  moving: clip to the nonnegative stochastic cone, then retract in the Peirce
          chart based at the current exact idempotent;
  fixed:  same clip, then retract in the Peirce chart based at a fixed H-M
          anchor.

It also generates a few small exact signed idempotents by row-sum-preserving
similarity conjugation of a known H-M point.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

import numpy as np
import scipy.linalg as la


ROOT = Path("/home/tobias/Projects/almost-idempotent-positive-maps")
W16_JSON = (
    ROOT
    / "agent-A/explorations/classical-portfolio/experiments/out/"
    / "w16_cert_audit/w16_best_rational_instance.json"
)


def frac_to_float(x: str | int | float) -> float:
    if isinstance(x, str):
        return float(Fraction(x))
    return float(x)


def parse_matrix_frac(rows: list[list[str | int | float]]) -> np.ndarray:
    return np.array([[frac_to_float(x) for x in row] for row in rows], dtype=float)


def row_norm(A: np.ndarray) -> float:
    return float(np.max(np.sum(np.abs(A), axis=1)))


def row_resid(P: np.ndarray) -> float:
    return float(np.max(np.abs(P @ np.ones(P.shape[0]) - 1.0)))


def idem_resid(P: np.ndarray) -> float:
    return row_norm(P @ P - P)


def delta_neg(P: np.ndarray) -> float:
    return float(np.max(np.sum(np.maximum(-P, 0.0), axis=1)))


def total_neg(P: np.ndarray) -> float:
    return float(np.sum(np.maximum(-P, 0.0)))


def min_entry(P: np.ndarray) -> float:
    return float(np.min(P))


def positive_row_project(P: np.ndarray) -> np.ndarray:
    """Row-wise clipping to the simplex by clipping negatives and renormalizing."""
    Y = np.maximum(P, 0.0)
    sums = Y.sum(axis=1)
    if np.any(sums <= 0):
        raise ValueError("row lost all positive mass during clipping")
    return Y / sums[:, None]


@dataclass
class Chart:
    P0: np.ndarray
    T: np.ndarray
    Ti: np.ndarray
    rank: int
    cond_T: float


def chart_for_idempotent(P0: np.ndarray, tol: float = 1e-8) -> Chart:
    """Return a basis in which P0 is diag(I_r, 0).

    SVD gives a numerically stable basis for range(P0) and ker(P0).  For an
    idempotent these subspaces are complementary, so concatenating the bases is
    invertible unless the projection is extremely oblique.
    """
    U, s, Vt = la.svd(P0)
    rank = int(np.sum(s > tol))
    range_basis = U[:, :rank]
    kernel_basis = Vt.T[:, rank:]
    T = np.column_stack([range_basis, kernel_basis])
    Ti = la.inv(T)
    return Chart(P0=P0, T=T, Ti=Ti, rank=rank, cond_T=float(np.linalg.cond(T)))


def real_close(A: np.ndarray, tol: float = 1e-8) -> np.ndarray:
    A = np.real_if_close(A, tol=1000)
    if np.iscomplexobj(A):
        imag = float(np.max(np.abs(A.imag)))
        if imag > tol:
            raise ValueError(f"non-negligible imaginary part from sqrtm: {imag:g}")
        A = A.real
    return np.asarray(A, dtype=float)


def corner_retract(P0: np.ndarray, Y: np.ndarray) -> tuple[np.ndarray, dict[str, float]]:
    """Retract Y to the idempotent variety in the local Peirce chart at P0.

    In coordinates P0 = diag(I,0), write X=Y-P0 with off-diagonal blocks B,C.
    The retracted idempotent is

        [[I + f(BC), B],
         [C,        -f(CB)]],

    where f(Z)=(-I+sqrt(I-4Z))/2 is the small branch.  This is the exact
    quadratic graph over E10+E01 whenever the branch is defined.
    """
    ch = chart_for_idempotent(P0)
    n = P0.shape[0]
    r = ch.rank
    X = ch.Ti @ (Y - P0) @ ch.T
    B = X[:r, r:]
    C = X[r:, :r]
    I1 = np.eye(r)
    I0 = np.eye(n - r)

    BC = B @ C
    CB = C @ B
    sqrt_BC = real_close(la.sqrtm(I1 - 4.0 * BC))
    sqrt_CB = real_close(la.sqrtm(I0 - 4.0 * CB))
    a = (-I1 + sqrt_BC) / 2.0
    d = (I0 - sqrt_CB) / 2.0

    Ptilde = np.zeros((n, n), dtype=float)
    Ptilde[:r, :r] = I1 + a
    Ptilde[:r, r:] = B
    Ptilde[r:, :r] = C
    Ptilde[r:, r:] = d
    Pnew = real_close(ch.T @ Ptilde @ ch.Ti)

    tangent_tilde = np.zeros((n, n), dtype=float)
    tangent_tilde[:r, r:] = B
    tangent_tilde[r:, :r] = C
    tangent_full = ch.T @ tangent_tilde @ ch.Ti
    diag_correction = Pnew - (P0 + tangent_full)
    old_diag = (Y - P0) - tangent_full

    diag = {
        "rank": float(r),
        "chart_cond": ch.cond_T,
        "offdiag_norm": row_norm(tangent_full),
        "old_diag_norm": row_norm(old_diag),
        "diag_correction_norm": row_norm(diag_correction),
        "project_to_retract_norm": row_norm(Pnew - Y),
        "bc_norm_chart": row_norm(BC),
        "cb_norm_chart": row_norm(CB),
        "branch_margin": float(
            min(
                0.25 - row_norm(BC),
                0.25 - row_norm(CB),
            )
        ),
    }
    return Pnew, diag


def hm_singleton_anchor_from_lambda(Lambda: np.ndarray, k: int) -> np.ndarray:
    """Build the singleton recurrent-block H-M anchor in the saved coordinates."""
    n = Lambda.shape[0]
    Lam0 = np.zeros((n, k), dtype=float)
    Lam0[:k, :] = np.eye(k)
    for i in range(k, n):
        row = np.maximum(Lambda[i], 0.0)
        if row.sum() == 0:
            row[:] = 1.0 / k
        else:
            row /= row.sum()
        Lam0[i] = row
    B0 = np.zeros((k, n), dtype=float)
    B0[:, :k] = np.eye(k)
    return Lam0 @ B0


def load_w16() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    data = json.loads(W16_JSON.read_text())
    P = parse_matrix_frac(data["P_frac"])
    Lambda = parse_matrix_frac(data["Lambda_frac"])
    B = parse_matrix_frac(data["B_frac"])
    return P, Lambda, B


def similarity_diagnostics(P: np.ndarray, Q: np.ndarray) -> dict[str, float]:
    n = P.shape[0]
    I = np.eye(n)
    eps = row_norm(P - Q)
    S = Q @ P + (I - Q) @ (I - P)
    T = P @ Q + (I - P) @ (I - Q)
    D = I - (P - Q) @ (P - Q)
    inv_bound = np.inf
    inv_norm = np.inf
    try:
        Sinv = la.solve(S, I)
        inv_norm = row_norm(Sinv)
    except la.LinAlgError:
        pass
    if eps < 1:
        inv_bound = row_norm(T) / (1.0 - eps * eps)
    return {
        "dist": eps,
        "S_minus_I": row_norm(S - I),
        "S_bound_row": row_norm(P - Q) * row_norm(2 * P - I),
        "S_min_entry": min_entry(S),
        "S_delta": delta_neg(S),
        "S_row_resid": row_resid(S),
        "intertwine_resid": row_norm(S @ P - Q @ S),
        "D_min_svd": float(np.min(la.svdvals(D))),
        "Sinv_norm": float(inv_norm),
        "Sinv_neumann_bound": float(inv_bound),
    }


def iterate(
    P_start: np.ndarray,
    steps: int,
    mode: str,
    anchor: np.ndarray | None = None,
) -> tuple[np.ndarray, list[dict[str, Any]]]:
    P = P_start.copy()
    trace: list[dict[str, Any]] = []
    fixed_anchor = anchor.copy() if anchor is not None else None
    for m in range(steps):
        base = P if mode == "moving" else fixed_anchor
        if base is None:
            raise ValueError("fixed mode requires an anchor")
        before = {
            "iter": m,
            "mode": mode,
            "delta_before": delta_neg(P),
            "total_neg_before": total_neg(P),
            "min_entry_before": min_entry(P),
            "idem_before": idem_resid(P),
            "row_before": row_resid(P),
            "norm_before": row_norm(P),
        }
        Y = positive_row_project(P)
        before["project_step_norm"] = row_norm(Y - P)
        before["project_idem_resid"] = idem_resid(Y)
        before["project_delta"] = delta_neg(Y)
        try:
            Pnext, diag = corner_retract(base, Y)
            before.update(diag)
            before.update(
                {
                    "delta_after": delta_neg(Pnext),
                    "total_neg_after": total_neg(Pnext),
                    "min_entry_after": min_entry(Pnext),
                    "idem_after": idem_resid(Pnext),
                    "row_after": row_resid(Pnext),
                    "norm_after": row_norm(Pnext),
                    "step_norm": row_norm(Pnext - P),
                    "status": "ok",
                }
            )
            P = Pnext
        except Exception as exc:  # record escapes instead of hiding them
            before["status"] = "fail"
            before["error"] = str(exc)
            trace.append(before)
            break
        trace.append(before)
        if before["delta_after"] < 1e-13:
            break
        if before["delta_after"] > 10 or before["norm_after"] > 100:
            break
    return P, trace


def make_hm(n: int, k: int, rng: np.random.Generator) -> np.ndarray:
    Lam = np.zeros((n, k), dtype=float)
    Lam[:k, :] = np.eye(k)
    for i in range(k, n):
        Lam[i, :] = rng.dirichlet(np.ones(k))
    B = np.zeros((k, n), dtype=float)
    B[:, :k] = np.eye(k)
    return Lam @ B


def random_rowsum_zero(n: int, rng: np.random.Generator) -> np.ndarray:
    A = rng.normal(size=(n, n))
    A -= A.sum(axis=1, keepdims=True) / n
    return A


def conjugate_instance(
    Q: np.ndarray,
    target_delta: float,
    rng: np.random.Generator,
) -> tuple[np.ndarray, float]:
    n = Q.shape[0]
    A = random_rowsum_zero(n, rng)

    def build(eps: float) -> np.ndarray:
        S = np.eye(n) + eps * A
        return S @ Q @ la.inv(S)

    lo = 0.0
    hi = 0.02
    while True:
        try:
            P_hi = build(hi)
            if delta_neg(P_hi) >= target_delta or hi > 2.0:
                break
        except la.LinAlgError:
            break
        hi *= 2.0
    for _ in range(80):
        mid = (lo + hi) / 2.0
        try:
            P_mid = build(mid)
            d = delta_neg(P_mid)
        except la.LinAlgError:
            hi = mid
            continue
        if d < target_delta:
            lo = mid
        else:
            hi = mid
    eps = hi
    return build(eps), eps


def write_trace(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    keys: list[str] = []
    for row in rows:
        for key in row:
            if key not in keys:
                keys.append(key)
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)


def save_matrix(path: Path, A: np.ndarray) -> None:
    np.savetxt(path, A, delimiter=",", fmt="%.17g")


def summarize_trace(label: str, trace: list[dict[str, Any]]) -> dict[str, Any]:
    if not trace:
        return {"label": label, "status": "empty"}
    first = trace[0]
    last = trace[-1]
    return {
        "label": label,
        "status": last.get("status", "ok"),
        "iters": len(trace),
        "delta0": first["delta_before"],
        "delta_last": last.get("delta_after", last.get("delta_before")),
        "min_entry_last": last.get("min_entry_after", last.get("min_entry_before")),
        "idem_last": last.get("idem_after", last.get("idem_before")),
        "row_last": last.get("row_after", last.get("row_before")),
        "last_project_step": last.get("project_step_norm"),
        "last_project_to_retract": last.get("project_to_retract_norm"),
        "last_offdiag": last.get("offdiag_norm"),
        "last_old_diag": last.get("old_diag_norm"),
        "last_diag_correction": last.get("diag_correction_norm"),
        "last_branch_margin": last.get("branch_margin"),
        "last_chart_cond": last.get("chart_cond"),
        "error": last.get("error", ""),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default="out")
    ap.add_argument("--steps", type=int, default=20)
    ap.add_argument("--seed", type=int, default=18018)
    args = ap.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    all_traces: dict[str, list[dict[str, Any]]] = {}
    summary: dict[str, Any] = {"w16": {}, "random": []}

    P16, Lam16, _B16 = load_w16()
    Q16 = hm_singleton_anchor_from_lambda(Lam16, 4)
    summary["w16"]["P_metrics"] = {
        "delta": delta_neg(P16),
        "idem": idem_resid(P16),
        "row": row_resid(P16),
        "norm": row_norm(P16),
    }
    summary["w16"]["anchor_metrics"] = {
        "delta": delta_neg(Q16),
        "idem": idem_resid(Q16),
        "row": row_resid(Q16),
        "dist_P_anchor": row_norm(P16 - Q16),
        "dist_over_delta": row_norm(P16 - Q16) / delta_neg(P16),
    }
    summary["w16"]["similarity_to_anchor"] = similarity_diagnostics(P16, Q16)

    Pm, tr = iterate(P16, args.steps, "moving")
    all_traces["w16_moving"] = tr
    save_matrix(outdir / "w16_moving_final.csv", Pm)
    summary["w16"]["moving"] = summarize_trace("w16_moving", tr)
    summary["w16"]["moving"]["dist_start_final"] = row_norm(Pm - P16)
    summary["w16"]["moving"]["dist_final_anchor"] = row_norm(Pm - Q16)

    Pf, tr = iterate(P16, args.steps, "fixed", Q16)
    all_traces["w16_fixed_anchor"] = tr
    save_matrix(outdir / "w16_fixed_anchor_final.csv", Pf)
    summary["w16"]["fixed_anchor"] = summarize_trace("w16_fixed_anchor", tr)
    summary["w16"]["fixed_anchor"]["dist_start_final"] = row_norm(Pf - P16)
    summary["w16"]["fixed_anchor"]["dist_final_anchor"] = row_norm(Pf - Q16)

    rng = np.random.default_rng(args.seed)
    random_specs = [(5, 2, 0.01), (6, 3, 0.03), (7, 3, 0.06)]
    for idx, (n, k, target) in enumerate(random_specs, start=1):
        Q = make_hm(n, k, rng)
        P, eps = conjugate_instance(Q, target, rng)
        item: dict[str, Any] = {
            "idx": idx,
            "n": n,
            "k": k,
            "target_delta": target,
            "eps": eps,
            "P_metrics": {
                "delta": delta_neg(P),
                "idem": idem_resid(P),
                "row": row_resid(P),
                "dist_to_true_Q": row_norm(P - Q),
                "dist_over_delta": row_norm(P - Q) / max(delta_neg(P), 1e-300),
            },
            "similarity_to_true_Q": similarity_diagnostics(P, Q),
        }
        Pm, trm = iterate(P, args.steps, "moving")
        label_m = f"random{idx}_moving"
        all_traces[label_m] = trm
        save_matrix(outdir / f"{label_m}_final.csv", Pm)
        item["moving"] = summarize_trace(label_m, trm)
        item["moving"]["dist_start_final"] = row_norm(Pm - P)
        item["moving"]["dist_final_true_Q"] = row_norm(Pm - Q)

        Pf, trf = iterate(P, args.steps, "fixed", Q)
        label_f = f"random{idx}_fixed_anchor"
        all_traces[label_f] = trf
        save_matrix(outdir / f"{label_f}_final.csv", Pf)
        item["fixed_anchor"] = summarize_trace(label_f, trf)
        item["fixed_anchor"]["dist_start_final"] = row_norm(Pf - P)
        item["fixed_anchor"]["dist_final_true_Q"] = row_norm(Pf - Q)
        summary["random"].append(item)

    for label, trace in all_traces.items():
        write_trace(outdir / f"{label}.csv", trace)
    (outdir / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True))

    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
