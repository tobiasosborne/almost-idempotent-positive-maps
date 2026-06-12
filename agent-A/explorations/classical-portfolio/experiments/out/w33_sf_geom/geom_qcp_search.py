#!/usr/bin/env python3
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path
from typing import Any

import gurobipy as gp
from gurobipy import GRB


def powers(radix: int, n: int):
    for value in range(radix**n):
        out = []
        x = value
        for _ in range(n):
            out.append(x % radix)
            x //= radix
        yield tuple(out)


def signed_face_expr(L: dict[tuple[int, int], gp.Var], j: int, k: int, s: int, sign_bits: tuple[int, ...]):
    """Linear expression for mu_s(j) - (1-a_s(j)) under a fixed foreign sign pattern.

    sign_bits are ordered by foreign coordinates t != s; 1 means L[j,t] <= 0,
    0 means L[j,t] >= 0. Under the pattern, (-L[j,t])_+ is either -L[j,t] or 0.
    """

    expr = L[j, s] - 1.0
    idx = 0
    for t in range(k):
        if t == s:
            continue
        if sign_bits[idx]:
            expr += -L[j, t]
        idx += 1
    return expr


def solve_pattern(
    *,
    k: int,
    nextra: int,
    delta: float,
    s: int,
    coeff_signs: tuple[tuple[int, ...], ...],
    e_active: tuple[int, ...],
    bpos_bits: tuple[int, ...],
    timelimit: float,
    mipgap: float,
    log_path: Path | None,
) -> dict[str, Any]:
    d = k + nextra
    extras = list(range(k, d))
    m = gp.Model("sf_geom_qcp")
    m.Params.OutputFlag = 0 if log_path is None else 1
    if log_path is not None:
        m.Params.LogFile = str(log_path)
    m.Params.NonConvex = 2
    m.Params.TimeLimit = timelimit
    m.Params.MIPGap = mipgap
    m.Params.FeasibilityTol = 1e-8
    m.Params.OptimalityTol = 1e-8

    L: dict[tuple[int, int], gp.Var] = {}
    B: dict[tuple[int, int], gp.Var] = {}
    P: dict[tuple[int, int], gp.Var] = {}
    Z: dict[tuple[int, int], gp.Var] = {}

    for i in range(d):
        for t in range(k):
            if i < k:
                L[i, t] = m.addVar(lb=1.0 if i == t else 0.0, ub=1.0 if i == t else 0.0, name=f"L[{i},{t}]")
            else:
                L[i, t] = m.addVar(lb=-1.0, ub=1.0, name=f"L[{i},{t}]")

    for r in range(k):
        for j in range(d):
            B[r, j] = m.addVar(lb=-delta, ub=1.0 + delta, name=f"B[{r},{j}]")

    p_abs_bound = float(k) * (1.0 + delta)
    for i in range(d):
        for j in range(d):
            P[i, j] = m.addVar(lb=-p_abs_bound, ub=p_abs_bound, name=f"P[{i},{j}]")
            Z[i, j] = m.addVar(lb=0.0, ub=delta, name=f"Z[{i},{j}]")

    m.update()

    for i in extras:
        m.addConstr(gp.quicksum(L[i, t] for t in range(k)) == 1.0, name=f"coeff_sum[{i}]")
        bits = coeff_signs[i - k]
        idx = 0
        for t in range(k):
            if t == s:
                continue
            if bits[idx]:
                m.addConstr(L[i, t] <= 0.0, name=f"coeff_neg[{i},{t}]")
            else:
                m.addConstr(L[i, t] >= 0.0, name=f"coeff_pos[{i},{t}]")
            idx += 1

    for r in range(k):
        m.addConstr(gp.quicksum(B[r, j] for j in range(d)) == 1.0, name=f"B_rowsum[{r}]")

    # B L = I_k is the exact structural idempotence condition for P = L B.
    for r in range(k):
        for t in range(k):
            q = gp.QuadExpr()
            for j in range(d):
                q += B[r, j] * L[j, t]
            m.addQConstr(q == (1.0 if r == t else 0.0), name=f"BL[{r},{t}]")

    for i in range(d):
        for j in range(d):
            q = gp.QuadExpr()
            for r in range(k):
                q += L[i, r] * B[r, j]
            m.addQConstr(P[i, j] == q, name=f"P_def[{i},{j}]")
            m.addConstr(Z[i, j] >= -P[i, j], name=f"neg_epigraph[{i},{j}]")
        m.addConstr(gp.quicksum(Z[i, j] for j in range(d)) <= delta, name=f"row_neg[{i}]")

    for jj, j in enumerate(extras):
        if bpos_bits[jj]:
            m.addConstr(B[s, j] >= 0.0, name=f"B_s_pos[{j}]")
        else:
            m.addConstr(B[s, j] <= 0.0, name=f"B_s_neg[{j}]")
        expr = signed_face_expr(L, j, k, s, coeff_signs[jj])
        if e_active[jj]:
            m.addConstr(expr >= 0.0, name=f"E_active[{j}]")
        else:
            m.addConstr(expr <= 0.0, name=f"E_inactive[{j}]")

    obj = gp.QuadExpr()
    for jj, j in enumerate(extras):
        if bpos_bits[jj] and e_active[jj]:
            obj += B[s, j] * signed_face_expr(L, j, k, s, coeff_signs[jj])
    m.setObjective(obj, GRB.MAXIMIZE)
    m.optimize()

    rec: dict[str, Any] = {
        "status": int(m.Status),
        "status_name": status_name(m.Status),
        "obj_bound": None if m.Status in {GRB.INFEASIBLE, GRB.INF_OR_UNBD, GRB.UNBOUNDED} else float(m.ObjBound),
        "obj_val": None,
        "gap": None,
        "runtime": float(m.Runtime),
        "coeff_signs": coeff_signs,
        "e_active": e_active,
        "bpos_bits": bpos_bits,
    }
    if m.SolCount > 0:
        rec["obj_val"] = float(m.ObjVal)
        if abs(m.ObjVal) > 1e-12:
            rec["gap"] = float(abs(m.ObjBound - m.ObjVal) / abs(m.ObjVal))
        rec["L"] = [[float(L[i, t].X) for t in range(k)] for i in range(d)]
        rec["B"] = [[float(B[r, j].X) for j in range(d)] for r in range(k)]
        rec["P"] = [[float(P[i, j].X) for j in range(d)] for i in range(d)]
        rec["row_neg"] = [
            float(sum(max(-rec["P"][i][j], 0.0) for j in range(d)))
            for i in range(d)
        ]
        rec["idempotence_inf"] = idempotence_error(rec["P"])
        rec["BL_error_inf"] = bl_error(rec["B"], rec["L"])
        rec["target_check"] = target_value(rec["B"], rec["L"], s)
    return rec


def status_name(status: int) -> str:
    for name in dir(GRB):
        if name.isupper() and getattr(GRB, name) == status:
            return name
    return str(status)


def matmul(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    return [
        [sum(A[i][r] * B[r][j] for r in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def idempotence_error(P: list[list[float]]) -> float:
    PP = matmul(P, P)
    return max(abs(PP[i][j] - P[i][j]) for i in range(len(P)) for j in range(len(P)))


def bl_error(B: list[list[float]], L: list[list[float]]) -> float:
    k = len(B)
    d = len(L)
    return max(
        abs(sum(B[r][j] * L[j][t] for j in range(d)) - (1.0 if r == t else 0.0))
        for r in range(k)
        for t in range(k)
    )


def excess(x: list[float], s: int) -> float:
    mu = sum(max(-x[t], 0.0) for t in range(len(x)) if t != s)
    lam = 1.0 - x[s]
    return max(mu - lam, 0.0)


def target_value(B: list[list[float]], L: list[list[float]], s: int) -> float:
    return sum(max(B[s][j], 0.0) * excess(L[j], s) for j in range(len(L)))


def search(args: argparse.Namespace) -> dict[str, Any]:
    k = args.k
    nextra = args.nextra
    s = args.s
    foreign_count = k - 1
    sign_patterns = list(powers(2, foreign_count))
    best: dict[str, Any] | None = None
    tried = 0
    solved = 0
    statuses: dict[str, int] = {}
    log_dir = Path(args.log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)

    pattern_iter = itertools.product(sign_patterns, repeat=nextra)
    active_iter_all = list(powers(2, nextra))
    bpos_iter_all = list(powers(2, nextra))

    for coeff_signs in pattern_iter:
        for e_active in active_iter_all:
            # Cheap pruning: if no E is active, the objective is zero.
            if not any(e_active):
                continue
            for bpos_bits in bpos_iter_all:
                if not any(a and b for a, b in zip(e_active, bpos_bits)):
                    continue
                tried += 1
                if args.max_patterns and tried > args.max_patterns:
                    break
                log_path = None
                if args.keep_logs and (best is None or tried <= args.log_first):
                    log_path = log_dir / f"qcp_k{k}_n{nextra}_pat{tried:05d}.log"
                rec = solve_pattern(
                    k=k,
                    nextra=nextra,
                    delta=args.delta,
                    s=s,
                    coeff_signs=coeff_signs,
                    e_active=e_active,
                    bpos_bits=bpos_bits,
                    timelimit=args.pattern_timelimit,
                    mipgap=args.mipgap,
                    log_path=log_path,
                )
                statuses[rec["status_name"]] = statuses.get(rec["status_name"], 0) + 1
                if rec["obj_val"] is not None:
                    solved += 1
                    if best is None or rec["obj_val"] > (best.get("obj_val") or -math.inf):
                        best = rec
                if args.max_patterns and tried >= args.max_patterns:
                    break
            if args.max_patterns and tried >= args.max_patterns:
                break
        if args.max_patterns and tried >= args.max_patterns:
            break

    return {
        "kind": "geometry_first_qcp",
        "k": k,
        "nextra": nextra,
        "d": k + nextra,
        "delta": args.delta,
        "s": s,
        "tried_patterns": tried,
        "solved_with_incumbent": solved,
        "statuses": statuses,
        "best": best,
        "best_ratio": None if best is None or args.delta <= 0 else (best.get("obj_val") or 0.0) / args.delta,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", type=int, default=3)
    parser.add_argument("--nextra", type=int, default=2)
    parser.add_argument("--delta", type=float, default=0.05)
    parser.add_argument("--s", type=int, default=0)
    parser.add_argument("--pattern-timelimit", type=float, default=4.0)
    parser.add_argument("--mipgap", type=float, default=1e-4)
    parser.add_argument("--max-patterns", type=int, default=0)
    parser.add_argument("--keep-logs", action="store_true")
    parser.add_argument("--log-first", type=int, default=5)
    parser.add_argument("--log-dir", default="gurobi_logs")
    parser.add_argument("--out", default=None)
    args = parser.parse_args()

    rec = search(args)
    out = Path(args.out) if args.out else Path(f"geom_qcp_k{args.k}_n{args.nextra}_delta{args.delta:g}.json")
    out.write_text(json.dumps(rec, indent=2, sort_keys=True))
    best = rec.get("best")
    print(
        f"k={rec['k']} nextra={rec['nextra']} d={rec['d']} delta={rec['delta']} "
        f"patterns={rec['tried_patterns']} statuses={rec['statuses']}"
    )
    if best is None:
        print("no incumbent")
    else:
        print(
            f"best target={best['obj_val']:.12g} ratio={rec['best_ratio']:.12g} "
            f"bound={best['obj_bound']} gap={best['gap']} "
            f"idemp={best['idempotence_inf']:.3g} BL={best['BL_error_inf']:.3g}"
        )
        print("best L:")
        for row in best["L"]:
            print("  " + " ".join(f"{x:+.8f}" for x in row))
        print("best B_s:")
        print("  " + " ".join(f"{x:+.8f}" for x in best["B"][args.s]))
        print("row neg:")
        print("  " + " ".join(f"{x:.8g}" for x in best["row_neg"]))


if __name__ == "__main__":
    main()
