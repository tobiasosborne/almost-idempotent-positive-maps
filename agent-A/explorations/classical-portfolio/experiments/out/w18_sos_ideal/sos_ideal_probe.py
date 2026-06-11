#!/usr/bin/env python3
"""Small SOS-on-variety probes for the signed idempotent row problem.

The script is intentionally modest:
  * rank-chart parametrisation P = L B, B L = I_k, P 1 = 1;
  * n=3,k=2 segment-exposure certificate checks;
  * Groebner-flavoured standard monomial counts for tiny rank components.

It does not solve the full lifted hiddenness SDP.  For n=3,k=2 the hiddenness
branch is empty, so the degree-2 SOS certificate is the trivial tau^2 square.
"""

from __future__ import annotations

import itertools
import json
import math
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import numpy as np
import scipy.optimize as opt
import sympy as sp


OUT = Path("outputs")


def rank_chart_symbolic(n: int, k: int):
    """Return symbolic L, B, P=L*B for the standard chart.

    L = [I_k; X], X rows have sum 1.
    B = [I_k - Q X, Q].
    Then B L = I_k and B 1 = 1, hence P^2=P and P 1=1.
    """
    assert 1 <= k <= n
    m = n - k
    q = sp.Matrix(k, m, lambda i, j: sp.symbols(f"q{i+1}_{j+1}"))
    x_symbols = []
    x_rows = []
    for a in range(m):
        row = []
        for b in range(k - 1):
            s = sp.symbols(f"x{a+1}_{b+1}")
            x_symbols.append(s)
            row.append(s)
        row.append(1 - sum(row))
        x_rows.append(row)
    X = sp.Matrix(x_rows) if m else sp.zeros(0, k)
    L = sp.Matrix.vstack(sp.eye(k), X)
    B = sp.Matrix.hstack(sp.eye(k) - q * X, q) if m else sp.eye(k)
    P = sp.simplify(L * B)
    return {
        "X": X,
        "Q": q,
        "L": L,
        "B": B,
        "P": P,
        "variables": x_symbols + list(q),
    }


def n3k2_parametric_certificate():
    """Symbolic certificate that rank-2 n=3 row geometry is a segment."""
    chart = rank_chart_symbolic(3, 2)
    x = chart["variables"][0]
    P = chart["P"]
    p0 = sp.Matrix(P[0, :]).T
    p1 = sp.Matrix(P[1, :]).T
    p2 = sp.Matrix(P[2, :]).T
    relation = [sp.simplify(p2[j] - (x * p0[j] + (1 - x) * p1[j])) for j in range(3)]
    idem = sp.simplify(P * P - P)
    rowsum = [sp.simplify(sum(P[i, j] for j in range(3)) - 1) for i in range(3)]
    return {
        "P": [[str(sp.expand(P[i, j])) for j in range(3)] for i in range(3)],
        "row2_affine_relation_residual": [str(r) for r in relation],
        "idempotence_residual": [[str(sp.expand(idem[i, j])) for j in range(3)] for i in range(3)],
        "rowsum_residual": [str(r) for r in rowsum],
        "exposure_argument": (
            "All rows lie on the affine line p(lambda)=lambda*p0+(1-lambda)*p1 "
            "with lambdas {1,0,x}.  The row-polytope endpoints are the min/max "
            "lambda rows.  The endpoint coordinate h=(lambda-lambda_min)/Dlambda "
            "is affine, lies in [0,1] on all rows, and h >= rho/D on rows at "
            "l1-distance at least rho. Since every signed row has l1 norm "
            "<= 1+2 delta, D <= 2+4 delta, so for delta<=1/4 and rho=4 tau, "
            "the margin is >= 4 tau/(2+4 delta) >= 4 tau/3 > tau/4=kappa."
        ),
        "sos_certificate_degree2": "delta - c*H = tau^2 - c*0 = tau^2",
    }


def exposed_margin_lp(P: np.ndarray, v: int, rho: float):
    """Solve the exposedness LP directly for a row v.

    h_i = a . (p_i - p_v), 0<=h_i<=1, h_j>=t for far j.
    """
    n = P.shape[0]
    D = P - P[v]
    far = [i for i in range(n) if np.abs(P[i] - P[v]).sum() >= rho - 1e-10 and i != v]
    if not far:
        return math.inf, far, True
    # variables are a_0..a_{n-1}, t. Max t -> min -t.
    c = np.zeros(n + 1)
    c[-1] = -1
    A_ub = []
    b_ub = []
    for i in range(n):
        # h_i <= 1
        row = np.zeros(n + 1)
        row[:n] = D[i]
        A_ub.append(row)
        b_ub.append(1.0)
        # -h_i <= 0
        row = np.zeros(n + 1)
        row[:n] = -D[i]
        A_ub.append(row)
        b_ub.append(0.0)
    for j in far:
        # t - h_j <= 0
        row = np.zeros(n + 1)
        row[:n] = -D[j]
        row[-1] = 1.0
        A_ub.append(row)
        b_ub.append(0.0)
    bounds = [(None, None)] * n + [(0.0, 1.0)]
    res = opt.linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub), bounds=bounds, method="highs")
    if not res.success:
        return None, far, False
    return -float(res.fun), far, True


def in_conv_others(P: np.ndarray, i: int):
    n = P.shape[0]
    others = [j for j in range(n) if j != i]
    Aeq = np.vstack([P[others].T, np.ones(len(others))])
    beq = np.r_[P[i], 1.0]
    res = opt.linprog(
        np.zeros(len(others)),
        A_eq=Aeq,
        b_eq=beq,
        bounds=[(0, None)] * len(others),
        method="highs",
    )
    return bool(res.success and np.linalg.norm(Aeq @ res.x - beq, ord=np.inf) < 1e-8)


def l1_distance_to_conv(P: np.ndarray, W: list[int], i: int):
    n = P.shape[0]
    m = len(W)
    c = np.r_[np.zeros(m), np.ones(n), np.ones(n)]
    Aeq = []
    beq = []
    for a in range(n):
        row = np.zeros(m + 2 * n)
        row[:m] = P[W, a]
        row[m + a] = 1.0
        row[m + n + a] = -1.0
        Aeq.append(row)
        beq.append(P[i, a])
    row = np.zeros(m + 2 * n)
    row[:m] = 1.0
    Aeq.append(row)
    beq.append(1.0)
    res = opt.linprog(
        c,
        A_eq=np.array(Aeq),
        b_eq=np.array(beq),
        bounds=[(0, None)] * (m + 2 * n),
        method="highs",
    )
    if not res.success:
        return None
    return float(res.fun)


def classify_visible_hidden(P: np.ndarray):
    neg = np.maximum(-P, 0).sum(axis=1)
    delta = float(neg.max())
    tau = math.sqrt(delta)
    rho = 4 * tau
    kappa = tau / 4
    vertices = [i for i in range(P.shape[0]) if not in_conv_others(P, i)]
    margins = {}
    far_sets = {}
    visible = []
    hidden = []
    for v in vertices:
        t, far, ok = exposed_margin_lp(P, v, rho)
        margins[str(v)] = t
        far_sets[str(v)] = far
        if ok and t >= kappa - 1e-8:
            visible.append(v)
        if ok and t < kappa - 1e-8:
            hidden.append(v)
    distances = {}
    H = None
    if visible:
        for i in range(P.shape[0]):
            distances[str(i)] = l1_distance_to_conv(P, visible, i)
        H = max(d for d in distances.values() if d is not None)
    return {
        "delta": delta,
        "tau": tau,
        "rho": rho,
        "kappa": kappa,
        "vertices": vertices,
        "visible": visible,
        "hidden": hidden,
        "margins": margins,
        "far_sets": far_sets,
        "distances_to_conv_visible": distances,
        "H": H,
        "H_over_tau": None if H is None else H / tau,
    }


def sample_n3k2_margins(samples=200, seed=1):
    """Randomly sample the n=3,k=2 chart and compare LP margins to kappa."""
    rng = np.random.default_rng(seed)
    chart = rank_chart_symbolic(3, 2)
    vars_ = chart["variables"]
    Pf = sp.lambdify(vars_, chart["P"], "numpy")
    worst = None
    rows = []
    for _ in range(samples):
        # Mild random range; only keep delta <= 1/4.
        vals = rng.uniform(-1.5, 1.5, size=len(vars_))
        P = np.array(Pf(*vals), dtype=float)
        neg = np.maximum(-P, 0).sum(axis=1)
        delta = float(neg.max())
        if not (1e-12 < delta <= 0.25):
            continue
        tau = math.sqrt(delta)
        rho = 4 * tau
        kappa = tau / 4
        # Vertices are endpoints in the lambda coordinate values 1,0,x.
        lambdas = np.array([1.0, 0.0, vals[0]])
        endpoints = [int(np.argmin(lambdas)), int(np.argmax(lambdas))]
        margins = []
        for v in endpoints:
            t, far, ok = exposed_margin_lp(P, v, rho)
            margins.append(t)
        ratio = min(margins) / kappa if all(math.isfinite(t) for t in margins) else math.inf
        row = {
            "delta": delta,
            "tau": tau,
            "kappa": kappa,
            "endpoints": endpoints,
            "margins": margins,
            "min_margin_over_kappa": ratio,
        }
        rows.append(row)
        if worst is None or ratio < worst["min_margin_over_kappa"]:
            worst = row
    return {"num_kept": len(rows), "worst": worst, "samples": rows[:10]}


def n4k3_first_hidden_witness():
    """A strict rational chart witness showing n=4,k=3 can have hidden geometry."""
    chart = rank_chart_symbolic(4, 3)
    vars_ = chart["variables"]
    # Found by a deterministic bounded random search, then rationalized.
    params = [Fraction(-1, 136), Fraction(29, 181), Fraction(7, 72), Fraction(-26, 149), Fraction(13, 132)]
    subs = {v: sp.Rational(f.numerator, f.denominator) for v, f in zip(vars_, params)}
    P_exact = sp.simplify(chart["P"].subs(subs))
    Pf = sp.lambdify(vars_, chart["P"], "numpy")
    P = np.array(Pf(*[float(f) for f in params]), dtype=float)
    info = classify_visible_hidden(P)
    neg_exact = []
    for i in range(4):
        total = sp.Rational(0)
        for j in range(4):
            if P_exact[i, j] < 0:
                total += -P_exact[i, j]
        neg_exact.append(total)
    delta_exact = max(neg_exact)
    return {
        "chart": "n=4,k=3 with L=[I_3; X], B=[I_3-QX,Q]",
        "variables": [str(v) for v in vars_],
        "rational_parameters": [str(f) for f in params],
        "P_frac": [[str(P_exact[i, j]) for j in range(4)] for i in range(4)],
        "P_decimal": P.tolist(),
        "negative_masses_frac": [str(x) for x in neg_exact],
        "delta_frac": str(delta_exact),
        "idempotence_residual_exact": [[str(sp.expand((P_exact * P_exact - P_exact)[i, j])) for j in range(4)] for i in range(4)],
        "rowsum_residual_exact": [str(sp.expand(sum(P_exact[i, j] for j in range(4)) - 1)) for i in range(4)],
        "classification": info,
        "exactness_note": "The parameters are rational in the rank chart, so BL=I, P^2=P, and P1=1 hold exactly over Q.",
    }


def groebner_rank_component(n: int, k: int, max_degree: int = 4):
    """Groebner leading data after eliminating row sums p_i,n = 1 - sum_{j<n} p_i,j."""
    vars_ = sp.symbols(" ".join(f"p{i+1}{j+1}" for i in range(n) for j in range(n - 1)))
    def var(i, j):
        if j < n - 1:
            return vars_[i * (n - 1) + j]
        return 1 - sum(vars_[i * (n - 1) + a] for a in range(n - 1))

    P = sp.Matrix(n, n, lambda i, j: var(i, j))
    polys = []
    R = P * P - P
    for i in range(n):
        for j in range(n):
            polys.append(sp.expand(R[i, j]))
    polys.append(sp.expand(sum(P[i, i] for i in range(n)) - k))
    # Remove zero/duplicate polys cheaply.
    uniq = []
    seen = set()
    for p in polys:
        p = sp.expand(p)
        if p == 0:
            continue
        s = str(p)
        if s not in seen:
            seen.add(s)
            uniq.append(p)
    G = sp.groebner(uniq, *vars_, order="grevlex")
    leading = [g.as_poly(*vars_).LM(order="grevlex") for g in G.polys]
    leading_tuples = [tuple(m) for m in leading]

    standard_counts = {}
    standard_examples = {}
    for d in range(max_degree + 1):
        count = 0
        examples = []
        for exps in itertools.product(range(d + 1), repeat=len(vars_)):
            if sum(exps) != d:
                continue
            divisible = any(all(e >= lm_i for e, lm_i in zip(exps, lm)) for lm in leading_tuples)
            if not divisible:
                count += 1
                if len(examples) < 20:
                    examples.append("*".join(
                        str(v) if e == 1 else f"{v}^{e}"
                        for v, e in zip(vars_, exps) if e
                    ) or "1")
        standard_counts[str(d)] = count
        standard_examples[str(d)] = examples
    return {
        "n": n,
        "k": k,
        "num_variables_after_rowsum": len(vars_),
        "num_input_polynomials": len(uniq),
        "num_groebner_polynomials": len(G.polys),
        "leading_monomials": [
            "*".join(
                str(v) if e == 1 else f"{v}^{e}"
                for v, e in zip(vars_, lm) if e
            ) or "1"
            for lm in leading_tuples
        ],
        "standard_monomial_counts_by_degree": standard_counts,
        "standard_monomial_examples_by_degree": standard_examples,
    }


def main():
    OUT.mkdir(exist_ok=True)
    data = {
        "rank_chart_n3k2": n3k2_parametric_certificate(),
        "sample_n3k2": sample_n3k2_margins(),
        "n4k3_first_hidden_witness": n4k3_first_hidden_witness(),
        "groebner": [],
    }
    for n, k in [(2, 1), (3, 1), (3, 2)]:
        data["groebner"].append(groebner_rank_component(n, k, max_degree=4))
    out = OUT / "sos_ideal_probe.json"
    out.write_text(json.dumps(data, indent=2, default=float))
    print(json.dumps({
        "wrote": str(out),
        "n3k2_worst_sample": data["sample_n3k2"]["worst"],
        "groebner_summaries": [
            {
                "n": g["n"],
                "k": g["k"],
                "vars": g["num_variables_after_rowsum"],
                "gb_polys": g["num_groebner_polynomials"],
                "std_counts": g["standard_monomial_counts_by_degree"],
            }
            for g in data["groebner"]
        ],
    }, indent=2, default=float))


if __name__ == "__main__":
    main()
