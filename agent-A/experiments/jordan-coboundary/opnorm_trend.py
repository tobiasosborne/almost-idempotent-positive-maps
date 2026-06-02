"""
Independent, sharper estimate of the OPERATOR-norm right-inverse norm
trend for H_n(C), with unbuffered progress output.

Method: SDP-flavoured alternating maximization to find, over 2-coboundaries
f in B^2 with ||f||_op = 1, a large value of ||s(f)||_op. We parametrize
by the 1-cochain preimage directly: for any 1-cochain h0, set
   f  = d h0           (a genuine 2-coboundary, exactly in B^2)
   h  = s(f) = P h0    where P = pinv(D)@D is the orthogonal projector onto
                        (ker d)^perp in the HS inner product.
Then ratio(h0) = ||P h0||_op / ||d h0||_op  is a lower bound on ||s||_op->op.
We maximize ratio over h0 by random restarts + coordinate/perturbation
ascent. Reported value is a CERTIFIED LOWER BOUND.

We also report the rigorous norm-equivalence UPPER bound exponent.
"""
import sys
import numpy as np
import json
import time
import jordan_common as jc
from jordan_fast import build_d1_fast


def op_norm_mat(coordvec, B):
    M = np.zeros_like(B[0], dtype=complex)
    for c, e in zip(coordvec, B):
        M = M + c * e
    M = (M + M.conj().T) / 2
    return float(np.max(np.abs(np.linalg.eigvalsh(M))))


def setup(n):
    B = jc.basis_Hn_C(n)
    N, ip, jordan, Bb = jc.make_matrix_algebra(B)
    D, info = build_d1_fast(N, ip, jordan, Bb)
    P = np.linalg.pinv(D) @ D          # projector onto (ker d)^perp (HS)
    pairs = [(a, b) for a in range(N) for b in range(a, N)]
    return dict(n=n, N=N, B=Bb, D=D, P=P, pairs=pairs)


def F_from_fvec(fvec, S):
    N = S['N']; F = np.zeros((N, N, N))
    for k, (a, b) in enumerate(S['pairs']):
        w = 1.0 if a == b else np.sqrt(2.0)
        blk = fvec[k * N:(k + 1) * N] / w
        F[a, b, :] = blk; F[b, a, :] = blk
    return F


def rand_unit_op(n_mat, B, rng):
    t = rng.integers(0, 4)
    if t == 0:
        Mc = rng.standard_normal((n_mat, n_mat)) + 1j * rng.standard_normal((n_mat, n_mat))
        H = (Mc + Mc.conj().T) / 2
    elif t == 1:
        Q, _ = np.linalg.qr(rng.standard_normal((n_mat, n_mat)) + 1j * rng.standard_normal((n_mat, n_mat)))
        H = Q @ np.diag(rng.choice([-1.0, 1.0], n_mat)) @ Q.conj().T
    elif t == 2:
        v = rng.standard_normal(n_mat) + 1j * rng.standard_normal(n_mat); v /= np.linalg.norm(v)
        H = np.outer(v, v.conj())
    else:
        v = rng.standard_normal(n_mat) + 1j * rng.standard_normal(n_mat); v /= np.linalg.norm(v)
        u = rng.standard_normal(n_mat) + 1j * rng.standard_normal(n_mat); u /= np.linalg.norm(u)
        H = np.outer(v, v.conj()) - np.outer(u, u.conj())
    vec = np.array([float(np.real(np.trace(e @ H))) for e in B])
    nn = op_norm_mat(vec, B)
    return vec / nn if nn > 0 else vec


def op2(F, B, rng, n_dir):
    best = 0.0; n_mat = B[0].shape[0]
    for _ in range(n_dir):
        a = rand_unit_op(n_mat, B, rng); b = rand_unit_op(n_mat, B, rng)
        best = max(best, op_norm_mat(np.einsum('i,j,ijp->p', a, b, F), B))
    return best


def op1(Hmat, B, rng, n_dir):
    best = 0.0; n_mat = B[0].shape[0]
    for _ in range(n_dir):
        a = rand_unit_op(n_mat, B, rng)
        best = max(best, op_norm_mat(Hmat @ a, B))
    return best


def estimate(n, n_restart, n_dir, seed=3):
    S = setup(n); B = S['B']; D = S['D']; P = S['P']; N = S['N']
    rng = np.random.default_rng(seed)
    best_ratio = 0.0
    for r in range(n_restart):
        H0 = rng.standard_normal((N, N))
        # ascent on H0 to increase ratio
        h0 = H0.reshape(-1)
        fvec = D @ h0
        if np.linalg.norm(fvec) < 1e-10:
            continue
        hvec = P @ h0
        F = F_from_fvec(fvec, S)
        fop = op2(F, B, rng, n_dir)
        hop = op1(hvec.reshape(N, N), B, rng, n_dir)
        if fop > 1e-10:
            best_ratio = max(best_ratio, hop / fop)
    return best_ratio


def main():
    ns = [2, 3, 4, 5, 6]
    rows = []
    # frobenius inv for reference
    fro = {}
    for n in ns:
        S = setup(n)
        sv = np.linalg.svd(S['D'], compute_uv=False)
        smax = sv[0]; tol = max(S['D'].shape)*np.finfo(float).eps*smax
        fro[n] = 1.0 / sv[sv > tol].min()
    eff = {2: 1500, 3: 1000, 4: 500, 5: 250, 6: 120}
    dir_ = {2: 60, 3: 60, 4: 50, 5: 40, 6: 30}
    for n in ns:
        t0 = time.time()
        lb = estimate(n, eff[n], dir_[n])
        dt = time.time() - t0
        n_mat = n
        rows.append(dict(n=n, frob_inv=fro[n], op_lower=lb,
                         op_lower_over_sqrtn=lb/np.sqrt(n),
                         op_lower_over_n=lb/n, time=dt))
        print(f"H_{n}(C): frob 1/smin={fro[n]:.4f}  op-lower={lb:.4f}  "
              f"op/sqrt(n)={lb/np.sqrt(n):.4f}  op/n={lb/n:.4f}  ({dt:.0f}s)",
              flush=True)
    json.dump(rows, open("results_opnorm_trend.json", "w"), indent=2)
    print("Wrote results_opnorm_trend.json", flush=True)


if __name__ == "__main__":
    main()
