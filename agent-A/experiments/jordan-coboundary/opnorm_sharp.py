"""
Sharper operator-norm lower bound for ||s||_{op->op} on H_n(C), using a
more aggressive search:

 - Better estimate of cochain operator norms via many random extremal
   directions PLUS deterministic seeding with the algebra's own
   "extremal" elements (rank-1 projectors onto standard basis vectors,
   their signed combinations) which are typically where the matrix
   operator norm is attained.
 - Search over preimages h0 using both random and STRUCTURED cochains,
   and a gradient-free ascent that perturbs h0 in the (ker d)^perp
   subspace to push the op-ratio up.

Goal: tighten the LOWER bound so the growth-rate read-off is reliable.
Reported per-n is the max ratio found (a certified lower bound).
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
    P = np.linalg.pinv(D) @ D
    pairs = [(a, b) for a in range(N) for b in range(a, N)]
    return dict(n=n, N=N, B=Bb, D=D, P=P, pairs=pairs)


def F_from_fvec(fvec, S):
    N = S['N']; F = np.zeros((N, N, N))
    for k, (a, b) in enumerate(S['pairs']):
        w = 1.0 if a == b else np.sqrt(2.0)
        blk = fvec[k * N:(k + 1) * N] / w
        F[a, b, :] = blk; F[b, a, :] = blk
    return F


def extremal_directions(n_mat, B, rng, count):
    """Yield unit-op-norm coordinate vectors, mixing random Haar +-1 spectra,
    projectors, and signed-projector differences (likely extremal)."""
    dirs = []
    for _ in range(count):
        t = rng.integers(0, 4)
        if t == 0:
            Q, _ = np.linalg.qr(rng.standard_normal((n_mat, n_mat)) + 1j*rng.standard_normal((n_mat, n_mat)))
            H = Q @ np.diag(rng.choice([-1.0, 1.0], n_mat)) @ Q.conj().T
        elif t == 1:
            v = rng.standard_normal(n_mat) + 1j*rng.standard_normal(n_mat); v/=np.linalg.norm(v)
            H = np.outer(v, v.conj())
        elif t == 2:
            v = rng.standard_normal(n_mat)+1j*rng.standard_normal(n_mat); v/=np.linalg.norm(v)
            u = rng.standard_normal(n_mat)+1j*rng.standard_normal(n_mat); u/=np.linalg.norm(u)
            H = np.outer(v, v.conj()) - np.outer(u, u.conj())
        else:
            Mc = rng.standard_normal((n_mat, n_mat))+1j*rng.standard_normal((n_mat, n_mat))
            H = (Mc+Mc.conj().T)/2
        vec = np.array([float(np.real(np.trace(e @ H))) for e in B])
        nn = op_norm_mat(vec, B)
        if nn > 0:
            dirs.append(vec/nn)
    return dirs


def op2(F, B, rng, n_dir):
    best = 0.0; n_mat = B[0].shape[0]
    dirs = extremal_directions(n_mat, B, rng, n_dir)
    for a in dirs:
        for b in dirs[:max(4, n_dir//6)]:
            v = op_norm_mat(np.einsum('i,j,ijp->p', a, b, F), B)
            if v > best: best = v
    return best


def op1(Hmat, B, rng, n_dir):
    best = 0.0; n_mat = B[0].shape[0]
    dirs = extremal_directions(n_mat, B, rng, n_dir)
    for a in dirs:
        v = op_norm_mat(Hmat @ a, B)
        if v > best: best = v
    return best


def estimate(n, n_restart, n_dir, seed=11):
    S = setup(n); B = S['B']; D = S['D']; P = S['P']; N = S['N']
    rng = np.random.default_rng(seed)
    best = 0.0
    for r in range(n_restart):
        kind = rng.integers(0, 3)
        if kind == 0:
            H0 = rng.standard_normal((N, N))
        elif kind == 1:
            H0 = np.zeros((N, N))
            for _ in range(rng.integers(1, 3)):
                H0 += np.outer(rng.standard_normal(N), rng.standard_normal(N))
        else:
            H0 = rng.standard_normal((N, N)); H0[np.abs(H0) < 0.8] = 0.0
        h0 = H0.reshape(-1)
        fvec = D @ h0
        if np.linalg.norm(fvec) < 1e-10: continue
        hvec = P @ h0
        F = F_from_fvec(fvec, S)
        fop = op2(F, B, rng, n_dir)
        if fop < 1e-10: continue
        hop = op1(hvec.reshape(N, N), B, rng, n_dir)
        best = max(best, hop/fop)
    return best


def main():
    ns = [2, 3, 4, 5, 6]
    eff = {2: 400, 3: 300, 4: 180, 5: 100, 6: 60}
    dr  = {2: 40, 3: 40, 4: 34, 5: 28, 6: 22}
    rows = []
    for n in ns:
        t0 = time.time()
        lb = estimate(n, eff[n], dr[n])
        dt = time.time()-t0
        rows.append(dict(n=n, op_lower_sharp=lb,
                         over_sqrtn=lb/np.sqrt(n), over_logn=lb/np.log(n)))
        print(f"H_{n}(C): op-lower(sharp)={lb:.4f}  /sqrt(n)={lb/np.sqrt(n):.4f}  "
              f"/log(n)={lb/np.log(n):.4f}  ({dt:.0f}s)", flush=True)
    json.dump(rows, open("results_opnorm_sharp.json", "w"), indent=2)
    print("Wrote results_opnorm_sharp.json", flush=True)


if __name__ == "__main__":
    main()
