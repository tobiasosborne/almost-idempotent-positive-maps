#!/usr/bin/env python3
"""Exact/CAS small-case probes for the op-exposed-hull route.

This is Agent B sandbox evidence, not a canonical proof.  It combines exact
SymPy identities with finite-row LP certificates for exposedness and distance
to a selected exposed hull.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import shutil
import subprocess
from dataclasses import asdict, dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable

import numpy as np
import sympy as sp
from scipy.optimize import linprog


ROOT = Path(__file__).resolve().parent


@dataclass
class LpVertexResult:
    vertex: int
    rho: float
    exposedness: float
    exposedness_over_tau: float | None
    outside: list[int]


@dataclass
class CaseResult:
    name: str
    n: int
    exact_delta: str
    delta: float
    tau: float
    matrix_rank_numeric: int
    affine_dimension_numeric: int
    vertex_indices: list[int]
    max_distance_to_vertex_hull: float
    min_exposedness: float
    min_exposedness_over_tau: float | None
    lp_vertices: list[LpVertexResult]
    exact_rows: list[list[str]]
    exact_certificate: str


def fstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def to_float_matrix(rows: list[list[Fraction]]) -> np.ndarray:
    return np.array([[float(x) for x in row] for row in rows], dtype=float)


def neg_mass_exact(rows: list[list[Fraction]]) -> Fraction:
    return max(sum(max(-x, Fraction(0)) for x in row) for row in rows)


def row_l1_distance(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.sum(np.abs(a - b)))


def distance_to_conv(point: np.ndarray, hull_points: np.ndarray) -> float:
    if len(hull_points) == 0:
        return math.inf
    m, dim = hull_points.shape
    c = np.r_[np.zeros(m), np.ones(dim)]
    a_eq = np.zeros((1, m + dim))
    a_eq[0, :m] = 1.0
    b_eq = np.array([1.0])
    a_ub: list[np.ndarray] = []
    b_ub: list[float] = []
    for j in range(dim):
        row = np.zeros(m + dim)
        row[:m] = hull_points[:, j]
        row[m + j] = -1.0
        a_ub.append(row)
        b_ub.append(float(point[j]))
        row = np.zeros(m + dim)
        row[:m] = -hull_points[:, j]
        row[m + j] = -1.0
        a_ub.append(row)
        b_ub.append(float(-point[j]))
    res = linprog(
        c,
        A_ub=np.array(a_ub),
        b_ub=np.array(b_ub),
        A_eq=a_eq,
        b_eq=b_eq,
        bounds=[(0, None)] * m + [(0, None)] * dim,
        method="highs",
    )
    if not res.success:
        raise RuntimeError(res.message)
    return float(res.fun)


def vertex_indices(rows: np.ndarray, tol: float = 1e-9) -> list[int]:
    out: list[int] = []
    for i, row in enumerate(rows):
        others = np.array([rows[j] for j in range(len(rows)) if j != i])
        if distance_to_conv(row, others) > tol:
            out.append(i)
    return out


def exposedness_modulus(rows: np.ndarray, vertex: int, rho: float) -> tuple[float, list[int]]:
    outside = [
        i
        for i, row in enumerate(rows)
        if row_l1_distance(row, rows[vertex]) >= rho - 1e-12
    ]
    if not outside:
        return 1.0, []

    dim = rows.shape[1]
    # Variables are affine coefficients a in R^dim, offset b, and objective t.
    # h(x)=a.x+b.  Maximize t subject to 0<=h(row)<=1, h(v)=0, and
    # h(outside row)>=t.
    c = np.zeros(dim + 2)
    c[-1] = -1.0
    a_ub: list[np.ndarray] = []
    b_ub: list[float] = []
    for row in rows:
        a_ub.append(np.r_[row, 1.0, 0.0])
        b_ub.append(1.0)
        a_ub.append(np.r_[-row, -1.0, 0.0])
        b_ub.append(0.0)
    for i in outside:
        a_ub.append(np.r_[-rows[i], -1.0, 1.0])
        b_ub.append(0.0)
    a_eq = np.array([np.r_[rows[vertex], 1.0, 0.0]])
    b_eq = np.array([0.0])
    res = linprog(
        c,
        A_ub=np.array(a_ub),
        b_ub=np.array(b_ub),
        A_eq=a_eq,
        b_eq=b_eq,
        bounds=[(None, None)] * (dim + 1) + [(0, 1)],
        method="highs",
    )
    if not res.success:
        raise RuntimeError(res.message)
    return float(-res.fun), outside


def hume_family(n: int, t: Fraction) -> list[list[Fraction]]:
    """Hume sharp family, with the transient mass split if n=4."""
    if n not in (3, 4):
        raise ValueError("hume_family implemented only for n=3,4")
    v = [Fraction(0) for _ in range(n)]
    v[0] = Fraction(1)
    v[1] = -1 + t
    for k in range(2, n):
        v[k] = -t / Fraction(n - 2)
    u = [Fraction(0) for _ in range(n)]
    u[0] = 1 - t + t * t
    u[1] = -t
    return projection_i_minus_uv(n, u, v)


def quadrilateral_family(t: Fraction) -> list[list[Fraction]]:
    """A rational 4-row corank-one quadrilateral with delta=t^2.

    The affine circuit is

        (1-t^2)p0 + t^2 p1 = (1-t^2)p2 + t^2 p3.

    For 0<t<=1/4 this is a genuine quadrilateral.  It is designed to hit the
    first non-simplex n=4 geometry while remaining exactly idempotent.
    """
    n = 4
    v = [1 - t * t, t * t, -1 + t * t, -t * t]
    u = [Fraction(1), Fraction(0), -t * t / (1 - t * t), Fraction(0)]
    return projection_i_minus_uv(n, u, v)


def projection_i_minus_uv(
    n: int, u: list[Fraction], v: list[Fraction]
) -> list[list[Fraction]]:
    rows: list[list[Fraction]] = []
    for i in range(n):
        row: list[Fraction] = []
        for j in range(n):
            row.append((Fraction(1) if i == j else Fraction(0)) - u[i] * v[j])
        rows.append(row)
    return rows


def matrix_rank(rows: np.ndarray) -> int:
    return int(np.linalg.matrix_rank(rows, tol=1e-9))


def affine_dimension(rows: np.ndarray) -> int:
    if len(rows) <= 1:
        return 0
    return int(np.linalg.matrix_rank(rows[1:] - rows[0], tol=1e-9))


def analyze_case(name: str, exact_rows: list[list[Fraction]], rho_factor: float = 1.0) -> CaseResult:
    rows = to_float_matrix(exact_rows)
    delta_q = neg_mass_exact(exact_rows)
    delta = float(delta_q)
    tau = math.sqrt(delta) if delta > 0 else 0.0
    rho = rho_factor * tau
    verts = vertex_indices(rows)
    lp_results: list[LpVertexResult] = []
    for v in verts:
        e, outside = exposedness_modulus(rows, v, rho)
        lp_results.append(
            LpVertexResult(
                vertex=v,
                rho=rho,
                exposedness=e,
                exposedness_over_tau=e / tau if tau > 0 else None,
                outside=outside,
            )
        )

    hull = rows[verts]
    distances = [distance_to_conv(row, hull) for row in rows]
    min_e = min((r.exposedness for r in lp_results), default=1.0)
    return CaseResult(
        name=name,
        n=len(exact_rows),
        exact_delta=fstr(delta_q),
        delta=delta,
        tau=tau,
        matrix_rank_numeric=matrix_rank(rows),
        affine_dimension_numeric=affine_dimension(rows),
        vertex_indices=verts,
        max_distance_to_vertex_hull=max(distances) if distances else 0.0,
        min_exposedness=min_e,
        min_exposedness_over_tau=min_e / tau if tau > 0 else None,
        lp_vertices=lp_results,
        exact_rows=[[fstr(x) for x in row] for row in exact_rows],
        exact_certificate="LP exposedness at rho=sqrt(delta); vertices form the reported hull.",
    )


def sympy_identity_checks() -> dict[str, str | bool]:
    n = 4
    u = sp.symbols("u0:4")
    v = sp.symbols("v0:4")
    one = sp.ones(n, 1)
    umat = sp.Matrix(n, 1, u)
    vmat = sp.Matrix(1, n, v)
    p = sp.eye(n) - umat * vmat
    sum_v_zero = sp.Eq(sum(v), 0)
    dot_uv_one = sp.Eq(sum(u[i] * v[i] for i in range(n)), 1)
    row_unital = sp.simplify(p * one - one)
    idempotent = sp.simplify(p * p - p)
    row_unital_reduced = [sp.simplify(x.subs(sum_v_zero.lhs, 0)) for x in row_unital]
    idem_reduced = [
        [sp.factor(idempotent[i, j].subs(dot_uv_one.lhs, 1)) for j in range(n)]
        for i in range(n)
    ]
    return {
        "rank_one_defect_row_unital_if_sum_v_zero": all(x == 0 for x in row_unital_reduced),
        "rank_one_defect_idempotent_if_v_dot_u_one": all(
            idem_reduced[i][j] == 0 for i in range(n) for j in range(n)
        ),
        "classification_note": (
            "For rank n-1 idempotents, I-P has rank 1, hence P=I-u v^T; "
            "P1=1 gives sum(v)=0 and P^2=P gives v^T u=1."
        ),
    }


def lp_expr(coeffs: list[tuple[float, str]]) -> str:
    parts: list[str] = []
    for coeff, name in coeffs:
        if abs(coeff) < 1e-14:
            continue
        sign = "+" if coeff >= 0 else "-"
        mag = abs(coeff)
        if not parts:
            parts.append(("- " if coeff < 0 else "") + f"{mag:.17g} {name}")
        else:
            parts.append(f" {sign} {mag:.17g} {name}")
    return "".join(parts) if parts else "0"


def write_exposedness_lp(rows: list[list[Fraction]], vertex: int, rho: Fraction, path: Path) -> None:
    outside = [
        i
        for i, row in enumerate(rows)
        if sum(abs(row[j] - rows[vertex][j]) for j in range(len(row))) >= rho
    ]
    dim = len(rows[0])
    lines = ["Maximize", " obj: tvar", "Subject To"]
    for i, row in enumerate(rows):
        h = [(float(row[j]), f"a{j}") for j in range(dim)] + [(1.0, "beta")]
        lines.append(f" h{i}_ub: {lp_expr(h)} <= 1")
        lines.append(f" h{i}_lb: {lp_expr([(-c, name) for c, name in h])} <= 0")
    for i in outside:
        row = rows[i]
        coeffs = [(-float(row[j]), f"a{j}") for j in range(dim)] + [
            (-1.0, "beta"),
            (1.0, "tvar"),
        ]
        lines.append(f" outside{i}: {lp_expr(coeffs)} <= 0")
    vrow = rows[vertex]
    lines.append(
        " vertex_zero: "
        + lp_expr([(float(vrow[j]), f"a{j}") for j in range(dim)] + [(1.0, "beta")])
        + " = 0"
    )
    lines.append("Bounds")
    for j in range(dim):
        lines.append(f" a{j} free")
    lines.append(" beta free")
    lines.append(" 0 <= tvar <= 1")
    lines.append("End")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_gurobi_cross_check() -> dict[str, str | bool]:
    gurobi = shutil.which("gurobi_cl")
    if not gurobi:
        return {"available": False, "status": "gurobi_cl missing"}
    lp_path = ROOT / "gurobi_exposedness_quad_t_1_10_v1.lp"
    log_path = ROOT / "gurobi_exposedness_quad_t_1_10_v1.log"
    sol_path = ROOT / "gurobi_exposedness_quad_t_1_10_v1.sol"
    write_exposedness_lp(quadrilateral_family(Fraction(1, 10)), 1, Fraction(1, 10), lp_path)
    proc = subprocess.run(
        [
            gurobi,
            f"LogFile={log_path}",
            f"ResultFile={sol_path}",
            str(lp_path),
        ],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    status = "ok" if proc.returncode == 0 else "failed"
    objective = "unknown"
    for line in proc.stdout.splitlines():
        if "Optimal objective" in line:
            objective = line.strip().split()[-1]
    return {
        "available": True,
        "status": status,
        "lp": str(lp_path.relative_to(ROOT)),
        "log": str(log_path.relative_to(ROOT)),
        "solution": str(sol_path.relative_to(ROOT)),
        "objective": objective,
    }


def tool_versions() -> dict[str, str]:
    versions = {
        "python": subprocess.check_output(["python3", "--version"], text=True).strip(),
        "numpy": np.__version__,
        "scipy": subprocess.check_output(
            ["python3", "-c", "import scipy; print(scipy.__version__)"], text=True
        ).strip(),
        "sympy": sp.__version__,
        "gurobi_cl": "missing",
        "wolframscript": "missing",
    }
    gurobi = shutil.which("gurobi_cl")
    if gurobi:
        versions["gurobi_cl"] = subprocess.check_output(
            [gurobi, "--version"], text=True
        ).strip().splitlines()[0]
    wolfram = shutil.which("wolframscript")
    if wolfram:
        proc = subprocess.run(
            [wolfram, "-code", "Print[$Version]"],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        versions["wolframscript"] = (
            proc.stdout.strip().splitlines()[0] if proc.returncode == 0 else "installed but not licensed"
        )
    return versions


def script_sha256() -> str:
    h = hashlib.sha256()
    h.update(Path(__file__).read_bytes())
    return h.hexdigest()


def write_csv(cases: Iterable[CaseResult], path: Path) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "name",
                "n",
                "exact_delta",
                "tau",
                "rank",
                "affine_dimension",
                "vertices",
                "min_exposedness",
                "min_exposedness_over_tau",
                "max_distance_to_vertex_hull",
            ],
        )
        writer.writeheader()
        for case in cases:
            writer.writerow(
                {
                    "name": case.name,
                    "n": case.n,
                    "exact_delta": case.exact_delta,
                    "tau": case.tau,
                    "rank": case.matrix_rank_numeric,
                    "affine_dimension": case.affine_dimension_numeric,
                    "vertices": " ".join(map(str, case.vertex_indices)),
                    "min_exposedness": case.min_exposedness,
                    "min_exposedness_over_tau": case.min_exposedness_over_tau,
                    "max_distance_to_vertex_hull": case.max_distance_to_vertex_hull,
                }
            )


def main() -> None:
    cases: list[CaseResult] = []
    for n in (3, 4):
        for denom in (10, 20, 50):
            t = Fraction(1, denom)
            cases.append(analyze_case(f"hume_split_n{n}_t_1_{denom}", hume_family(n, t)))
    for denom in (10, 20, 50):
        t = Fraction(1, denom)
        case = analyze_case(f"quadrilateral_n4_t_1_{denom}", quadrilateral_family(t))
        case.exact_certificate = (
            "For t<=1/4 and rho=t, the affine circuit is "
            "(1-t^2)p0+t^2 p1=(1-t^2)p2+t^2 p3.  Exposing values "
            "for p0,p2 are (0,1,0,1), giving e>=1 on their outside rows. "
            "For p1 use (1,0,1-t^2,1-t^2), and for p3 use "
            "(1-t^2,1-t^2,1,0), giving e>=1-t^2.  Hence all four "
            "vertices lie in W_{rho,kappa} for any kappa<=1-t^2, so the "
            "distance to conv W is exactly 0."
        )
        cases.append(case)

    payload = {
        "status": "Agent B sandbox evidence only; not a canonical proof.",
        "command": "python3 agent-B/experiments/op-exposed-hull/small_cases_exact.py",
        "script_sha256": script_sha256(),
        "tool_versions": tool_versions(),
        "sympy_identity_checks": sympy_identity_checks(),
        "gurobi_cross_check": run_gurobi_cross_check(),
        "generic_exact_certificates": [
            {
                "case": "matrix rank <= 2",
                "certificate": (
                    "Rows have affine dimension <=1.  If K=[a,b] and D=||a-b||_1, "
                    "the endpoint coordinate h has e_a(rho),e_b(rho)>=min(1,rho/D). "
                    "Since each signed probability row has ||p_i||_1<=1+2delta, "
                    "D<=2+4delta; for delta<=1/2 and rho=C tau this gives "
                    "e>=C tau/4.  Thus both endpoints are in W for kappa<=C tau/4, "
                    "and every row is in conv W with zero error."
                ),
            },
            {
                "case": "n=3",
                "certificate": (
                    "Rank 1 is a point, rank 2 is the segment case, and rank 3 "
                    "forces P=I.  Therefore op-exposed-hull has zero reconstruction "
                    "error in all exact n=3 cases, with the segment endpoint bound above."
                ),
            },
        ],
        "cases": [asdict(c) for c in cases],
    }
    out_json = ROOT / "small_cases_exact.json"
    out_csv = ROOT / "small_cases_exact.csv"
    out_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    write_csv(cases, out_csv)
    print(f"wrote {out_json}")
    print(f"wrote {out_csv}")
    for case in cases:
        ratio = case.min_exposedness_over_tau
        ratio_s = "inf" if ratio is None else f"{ratio:.6g}"
        print(
            f"{case.name}: delta={case.exact_delta} rank={case.matrix_rank_numeric} "
            f"affdim={case.affine_dimension_numeric} vertices={case.vertex_indices} "
            f"min_e/tau={ratio_s} hull_dist={case.max_distance_to_vertex_hull:.3g}"
        )


if __name__ == "__main__":
    main()
