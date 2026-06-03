#!/usr/bin/env python3
"""
Crossover probe: is the 1/lambda in  ||q_a|| <= C eta/lambda  REAL or LOOSE?

Family E continuously interpolates faithful <-> transient.  Take Agent B's
absorbing/transient R^3 family and add a leak rho from the absorbing state 1
back into state 3, making the chain irreducible (hence faithful) with a
stationary mass on {2,3} that ~ rho.  As rho -> 0 we recover Agent B's family
(lambda -> 0, ||q_a|| -> Theta(1)); for rho > 0 the chain is faithful.

We hold the almost-idempotency parameter a fixed (so eta ~ const) and sweep rho,
recording eta, lambda, ||q_a||, and the invariant-state overlap omega(q_a^+),
which is the quantity the proof actually bounds:  ||q^+|| <= omega(q^+)/lambda.

Discriminating predictions:
  (i)  1/lambda TIGHT  : ||q_a|| ~ min(eta/lambda, O(1)), crossover at lambda~eta,
                          AND omega(q^+) ~ eta (lambda-independent).
  (ii) 1/lambda LOOSE  : ||q_a|| ~ C eta for all lambda>0 (jumps to O(1) only at
                          lambda=0 exactly), AND omega(q^+) ~ lambda*eta (the
                          1/lambda is cancelled by suppressed overlap).
"""
import numpy as np, json, os
from hole_scaling import (eta_of, riesz_projector, stationary, imP_basis)

np.set_printoptions(precision=5, suppress=True)


def family_E(a, rho):
    """Agent B's T_a with a leak rho from state 1 -> state 3."""
    P0 = np.array([[1, 0, 0], [0, 1, 0], [1/3, 2/3, 0]], float)
    S = np.array([[1, 0, 0], [0, 0, 1], [0, 0, 1]], float)
    T = (1 - a) * P0 + a * S
    # leak from absorbing state 1 to state 3
    T[0, 0] -= rho
    T[0, 2] += rho
    return T


def square_hole_with_overlap(P, pi, n_grid=4000):
    """Maximise ||q_a||_inf over a in Im P, ||a||_inf=1; also report, at that
    maximiser, the invariant-state overlap of the positive part:
        omega(q^+) = sum_i pi_i * max(q_i, 0).
    Returns (max ||q_a||, omega(q^+) at the argmax, omega(|q|) at argmax)."""
    B, r = imP_basis(P)
    best = (0.0, 0.0, 0.0)
    if r == 1:
        cands = [B[:, 0]]
    elif r == 2:
        th = np.linspace(0, np.pi, n_grid, endpoint=False)
        cands = [np.cos(t) * B[:, 0] + np.sin(t) * B[:, 1] for t in th]
    else:
        rng = np.random.default_rng(0)
        cands = [B @ rng.standard_normal(r) for _ in range(n_grid)]
    for a in cands:
        nrm = np.max(np.abs(a))
        if nrm < 1e-12:
            continue
        a = a / nrm
        a2 = a * a
        q = P @ a2 - a2
        nq = np.max(np.abs(q))
        if nq > best[0]:
            omega_plus = float(np.sum(pi * np.maximum(q, 0.0)))
            omega_abs = float(np.sum(pi * np.abs(q)))
            best = (nq, omega_plus, omega_abs)
    return best


def run(a, rhos):
    print(f"\n=== FAMILY E crossover, a={a:.1e} (eta~const), sweeping leak rho ===")
    print(f"  {'rho':>9} {'eta':>11} {'lambda':>11} {'||q_a||':>11} "
          f"{'q*lam/eta':>11} {'q/eta':>9} {'om(q+)':>11} {'om(q+)/eta':>11} "
          f"{'om(q+)/lam':>11}")
    rows = []
    for rho in rhos:
        T = family_E(a, rho)
        e = eta_of(T)
        P = riesz_projector(T)
        pi, lam = stationary(T)
        if pi.min() < -1e-7:      # safety
            continue
        nq, omp, oma = square_hole_with_overlap(P, pi)
        rows.append(dict(rho=rho, eta=e, lam=lam, q=nq, omega_plus=omp))
        print(f"  {rho:9.2e} {e:11.3e} {lam:11.3e} {nq:11.3e} "
              f"{(nq*lam/e):11.4f} {(nq/e):9.3f} {omp:11.3e} {(omp/e):11.4f} "
              f"{(omp/lam if lam>0 else np.inf):11.3e}")
    return rows


if __name__ == "__main__":
    outdir = os.path.dirname(os.path.abspath(__file__))
    a = 1e-3
    rhos = [0.3, 1e-1, 3e-2, 1e-2, 3e-3, 1e-3, 3e-4, 1e-4, 3e-5, 1e-5, 0.0]
    rows = run(a, rhos)

    print("\nReading guide:")
    print("  * q/eta column ~ const  => ||q_a|| = Theta(eta), 1/lambda is LOOSE")
    print("  * q*lam/eta column ~ const => 1/lambda is TIGHT")
    print("  * om(q+)/eta vs om(q+)/lam: which is stable tells how overlap scales")
    with open(os.path.join(outdir, "crossover_results.json"), "w") as f:
        json.dump(rows, f, indent=2, default=float)
    print("[saved crossover_results.json]")
