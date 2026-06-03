#!/usr/bin/env python3
"""
Faithful-invariant-state transfer experiment (Agent A).

Colleague's question: an EXACT idempotent unital positive P with a faithful
invariant state has range closed under the ORDINARY Jordan product (not only the
projected product a•b=P(a∘b)).  Does this transfer to the APPROXIMATE setting?

Agent A's analytical claim:
    ‖a∘b − P(a∘b)‖ ≤ C (η/λ) ‖a‖‖b‖      (a,b ∈ A = Im P)
where P=θ(2Φ−I), ‖Φ²−Φ‖≤η, ω a (near-)invariant FAITHFUL state with density
ρ_ω ≥ λ·1 (λ = least eigenvalue).  Equivalently the square hole
    q_a := P(a²) − a²              ( = −h_{a,a} in Agent B's notation )
satisfies ‖q_a‖ ≤ C(η/λ)‖a‖².

Falsifiable prediction this script tests:
  * NO faithful invariant state (λ=0, absorbing/transient) ⇒ ‖q_a‖ = Θ(√η).
    [This is exactly Agent B's 32/27 family — state 1 is absorbing.]
  * FAITHFUL well-conditioned invariant state (λ=Θ(1)) ⇒ ‖q_a‖ = Θ(η).
  * Tunable λ ⇒ crossover ‖q_a‖ ≈ min(C η/λ, C'√η) at λ ~ √η.

Classical (commutative) model: Φ = row-stochastic matrix T on R^n with sup norm.
Jordan product = pointwise (Hadamard) product.  P = Riesz spectral projector of
T onto eigenvalues with Re μ > 1/2  (= θ(2T−I) = (I+sign(2T−I))/2).
"""

import numpy as np
import json, os

np.set_printoptions(precision=5, suppress=True)


# ----------------------------------------------------------------------------
# core objects
# ----------------------------------------------------------------------------
def eta_of(T):
    """eta = ||T^2 - T||_{inf->inf} = max row-abs-sum  (operator norm on (R^n,sup))."""
    D = T @ T - T
    return np.max(np.sum(np.abs(D), axis=1))


def riesz_projector(T, thresh=0.5):
    """P = theta(2T - I): spectral projector onto eigenvalues with Re mu > thresh.
    Non-symmetric T => use right/left eigenvectors. Returns real P."""
    w, VR = np.linalg.eig(T)
    VRi = np.linalg.inv(VR)
    sel = (w.real > thresh).astype(float)
    P = VR @ np.diag(sel) @ VRi
    Pr = P.real
    assert np.max(np.abs(P.imag)) < 1e-8, f"imag part {np.max(np.abs(P.imag))}"
    assert np.max(np.abs(Pr @ Pr - Pr)) < 1e-6, "P not idempotent"
    return Pr


def stationary(T):
    """Stationary distribution pi: pi T = pi, pi>=0, sum pi=1 (Perron left eigvec).
    Returns (pi, lambda_min) where lambda_min = min_i pi_i."""
    w, VL = np.linalg.eig(T.T)
    k = np.argmin(np.abs(w - 1.0))
    pi = VL[:, k].real
    pi = pi / pi.sum()
    # numerical sign clean-up
    if pi.min() < -1e-9:
        pi = -pi / pi.sum() if (-pi).min() >= -1e-9 else pi
    return pi, pi.min()


def imP_basis(P):
    """Orthonormal basis (columns) of Im P = column space of P."""
    U, s, _ = np.linalg.svd(P)
    r = int(np.sum(s > 1e-8))
    return U[:, :r], r


def max_square_hole(P, n_grid=2000, seed=0):
    """Maximize over a in Im P, ||a||_inf <= 1, of:
        ||q_a||_inf  where q_a = P(a^2) - a^2  (a^2 = pointwise square)
    Also returns ||P(q_a^2)|| at the maximiser (Agent B's quantity) and the
    P(q_a^2) maximiser value separately.
    dim Im P is small here so a dense angular grid is exhaustive enough."""
    B, r = imP_basis(P)
    best_q = 0.0
    best_Pq2 = 0.0
    rng = np.random.default_rng(seed)
    if r == 1:
        cand = [B[:, 0]]
    elif r == 2:
        thetas = np.linspace(0, np.pi, n_grid, endpoint=False)
        cand = [np.cos(t) * B[:, 0] + np.sin(t) * B[:, 1] for t in thetas]
    else:
        cand = [B @ rng.standard_normal(r) for _ in range(n_grid)]
    for a in cand:
        nrm = np.max(np.abs(a))
        if nrm < 1e-12:
            continue
        a = a / nrm                      # ||a||_inf = 1
        a2 = a * a                       # pointwise square (classical Jordan square)
        q = P @ a2 - a2                  # square hole, lives in Ker P
        best_q = max(best_q, np.max(np.abs(q)))
        q2 = q * q
        Pq2 = P @ q2
        best_Pq2 = max(best_Pq2, np.max(np.abs(Pq2)))
    return best_q, best_Pq2


def loglog_slope(xs, ys):
    xs = np.log(np.asarray(xs)); ys = np.log(np.asarray(ys))
    A = np.vstack([xs, np.ones_like(xs)]).T
    m, _ = np.linalg.lstsq(A, ys, rcond=None)[0]
    return m


# ----------------------------------------------------------------------------
# family A : Agent B's absorbing/transient R^3 family  (lambda = 0)
# ----------------------------------------------------------------------------
def family_B_absorbing(a):
    P0 = np.array([[1, 0, 0], [0, 1, 0], [1/3, 2/3, 0]], float)
    S = np.array([[1, 0, 0], [0, 0, 1], [0, 0, 1]], float)
    return (1 - a) * P0 + a * S


# ----------------------------------------------------------------------------
# family C : FAITHFUL block family.  Classes {1,2} (recurrent) + {3} (recurrent).
#   Q0 = [[p,1-p,0],[p,1-p,0],[0,0,1]] is an exact stochastic idempotent whose
#   range = {f constant on {1,2}} IS closed under pointwise product (holes = 0).
#   Perturb Q0 by a generic stochastic M:  T = (1-a)Q0 + a M.
#   Faithful invariant states exist (mass on all 3 states); lambda tunable via
#   the eventual stationary distribution.
# ----------------------------------------------------------------------------
def block_idempotent(p):
    return np.array([[p, 1 - p, 0], [p, 1 - p, 0], [0, 0, 1]], float)


def random_stochastic(n, rng):
    M = rng.random((n, n))
    return M / M.sum(axis=1, keepdims=True)


def family_C_faithful(a, p=0.5, seed=1):
    rng = np.random.default_rng(seed)
    Q0 = block_idempotent(p)
    M = random_stochastic(3, rng)
    return (1 - a) * Q0 + a * M


# ----------------------------------------------------------------------------
# family D : tunable-lambda.  Two recurrent classes coupled by a small leak
#   parameter; the smaller the secondary mass, the smaller lambda.  Built so
#   that lambda can be driven to ~0 while eta stays ~ a.
# ----------------------------------------------------------------------------
def family_D_tunable(a, p=0.5, w=0.5, seed=2):
    """Q0 with stationary mass w on class {1,2} (split p,1-p) and 1-w on {3}.
    A generic perturbation moves lambda ~ min(w p, w(1-p), 1-w)."""
    rng = np.random.default_rng(seed)
    Q0 = block_idempotent(p)
    # bias the perturbation slightly toward state 3 to control mass, but keep
    # it a genuine stochastic matrix:
    M = random_stochastic(3, rng)
    T = (1 - a) * Q0 + a * M
    return T


# ----------------------------------------------------------------------------
# run
# ----------------------------------------------------------------------------
def sweep(name, builder, a_list, **kw):
    rows = []
    for a in a_list:
        T = builder(a, **kw)
        e = eta_of(T)
        P = riesz_projector(T)
        pi, lam = stationary(T)
        q, Pq2 = max_square_hole(P)
        rows.append(dict(a=a, eta=e, lam=lam, q=q, Pq2=Pq2,
                         q_over_sqrt_eta=q/np.sqrt(e) if e > 0 else 0,
                         q_over_eta=q/e if e > 0 else 0))
    # slopes (drop the largest a where higher-order terms pollute)
    use = rows[1:] if len(rows) > 3 else rows
    sl_q = loglog_slope([r['eta'] for r in use], [r['q'] for r in use])
    sl_Pq2 = loglog_slope([r['eta'] for r in use], [r['Pq2'] for r in use])
    print(f"\n=== {name}  (kw={kw}) ===")
    print(f"  {'a':>9} {'eta':>11} {'lambda':>9} {'||q_a||':>11} "
          f"{'q/sqrt(eta)':>12} {'q/eta':>10} {'||P(q^2)||':>11}")
    for r in rows:
        print(f"  {r['a']:9.2e} {r['eta']:11.3e} {r['lam']:9.4f} {r['q']:11.3e} "
              f"{r['q_over_sqrt_eta']:12.4f} {r['q_over_eta']:10.4f} {r['Pq2']:11.3e}")
    print(f"  --> log-log slope d log||q_a|| / d log eta  = {sl_q:.3f}   "
          f"(0.5 = sqrt(eta) regime, 1.0 = eta regime)")
    print(f"  --> log-log slope d log||P(q^2)|| / d log eta = {sl_Pq2:.3f}   "
          f"(matches Agent B's ||P(h^2)|| quantity)")
    return rows, sl_q, sl_Pq2


def lambda_sweep(a, p_list, **kw):
    print(f"\n=== lambda-sweep at fixed a={a:.2e} (faithful block, varying p->lambda) ===")
    print(f"  {'p':>7} {'eta':>11} {'lambda':>9} {'||q_a||':>11} "
          f"{'q*lambda/eta':>13} {'q/sqrt(eta)':>12}")
    rows = []
    for p in p_list:
        T = family_C_faithful(a, p=p, **kw)
        e = eta_of(T); P = riesz_projector(T); pi, lam = stationary(T)
        q, Pq2 = max_square_hole(P)
        rows.append(dict(p=p, eta=e, lam=lam, q=q, Pq2=Pq2))
        print(f"  {p:7.3f} {e:11.3e} {lam:9.4f} {q:11.3e} "
              f"{(q*lam/e if e>0 else 0):13.4f} {(q/np.sqrt(e) if e>0 else 0):12.4f}")
    return rows


if __name__ == "__main__":
    outdir = os.path.dirname(os.path.abspath(__file__))
    a_list = [3e-2, 1e-2, 3e-3, 1e-3, 3e-4, 1e-4]

    all_results = {}

    rB, sBq, sBPq2 = sweep("FAMILY B (Agent B absorbing/transient, lambda=0)",
                           family_B_absorbing, a_list)
    all_results["family_B_absorbing"] = dict(rows=rB, slope_q=sBq, slope_Pq2=sBPq2)

    rC, sCq, sCPq2 = sweep("FAMILY C (faithful block, lambda=Theta(1))",
                           family_C_faithful, a_list, p=0.5, seed=1)
    all_results["family_C_faithful"] = dict(rows=rC, slope_q=sCq, slope_Pq2=sCPq2)

    # a couple more faithful seeds to confirm it's not seed-luck
    rC2, sC2q, _ = sweep("FAMILY C (faithful block, seed=7)",
                         family_C_faithful, a_list, p=0.4, seed=7)
    all_results["family_C_faithful_seed7"] = dict(rows=rC2, slope_q=sC2q)

    # lambda crossover at fixed small a
    lam_rows = lambda_sweep(1e-3,
                            p_list=[0.5, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01, 0.003],
                            seed=1)
    all_results["lambda_sweep_a1e-3"] = lam_rows

    with open(os.path.join(outdir, "hole_scaling_results.json"), "w") as f:
        json.dump(all_results, f, indent=2, default=float)
    print("\n[saved hole_scaling_results.json]")
