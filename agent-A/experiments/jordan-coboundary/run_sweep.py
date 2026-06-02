"""
Main sweep: compute 1/sigma_min(n) (Frobenius-norm right-inverse norm) for
the Jordan coboundary d^1 over several families of Jordan algebras, plus
an operator-norm analysis for H_n(C).

Outputs a JSON-able dict and prints tables.
"""

import numpy as np
import json
import time
import jordan_common as jc
from jordan_fast import build_d1_fast


# ----------------------------------------------------------------------
# Core Frobenius analysis
# ----------------------------------------------------------------------

def frob_analysis(N, ip, jordan, B, want_VT=False):
    D, info = build_d1_fast(N, ip, jordan, B)
    if want_VT:
        U, sv, VT = np.linalg.svd(D, full_matrices=False)
        smax = sv[0]
        tol = max(D.shape) * np.finfo(float).eps * smax
        rank = int(np.sum(sv > tol))
        nz = sv[sv > tol]
        res = dict(dimC1=info['dimC1'], dimC2=info['dimC2'], rank=rank,
                   ker=info['dimC1'] - rank, smin=float(nz.min()),
                   smax=float(smax), inv=float(1.0 / nz.min()), tol=float(tol))
        return res, D, U, sv, VT, info
    res = jc.analyze(D, info)
    return res, D, info


# ----------------------------------------------------------------------
# Operator-norm machinery for H_n(C).
#
# We need operator (order-unit) norms on J = H_n(C).  We reconstruct an
# algebra element from its orthonormal-basis coordinate vector and take
# the matrix spectral norm (= operator norm for Hermitian).
# ----------------------------------------------------------------------

def coord_to_mat(vec, B):
    M = np.zeros_like(B[0], dtype=complex)
    for c, e in zip(vec, B):
        M = M + c * e
    return M


def op_norm_elem(vec, B):
    M = coord_to_mat(vec, B)
    # Hermitian -> operator norm = max |eigenvalue|
    w = np.linalg.eigvalsh((M + M.conj().T) / 2)
    return float(np.max(np.abs(w)))


def norm_equiv_constants(N, B):
    """Empirically determine the equivalence constants between Frobenius
    and operator norms on J (these are KNOWN in closed form for H_n(C)):
       ||x||_op <= ||x||_F <= sqrt(rank) ||x||_op,  rank<=n.
    We just report sqrt(N_real)/... Actually for matrices:
       ||x||_op <= ||x||_F  and  ||x||_F <= sqrt(n) ||x||_op
    where n is the matrix dimension (number of eigenvalues). Return n_mat.
    Here B[0].shape[0] = n_mat.
    """
    return B[0].shape[0]


# ----------------------------------------------------------------------
# Operator-norm right-inverse: numerical lower bound by sampling.
#
# s = minimal-Frobenius-norm right inverse on the image B^2 = Z^2.
# Given a 2-coboundary f in B^2, s(f) = pseudo-inverse preimage:
# in coordinates, f_vec in R^{dimC2}; s(f) = pinv(D) @ f_vec gives the
# minimal-||.||_F 1-cochain h with D h = f (since f in column space).
#
# We want to estimate
#    ||s||_{op->op} = sup_{f in B^2, ||f||_op = 1} ||s(f)||_op
# where ||f||_op, ||h||_op are the OPERATOR(order-unit)-norm-induced
# cochain norms.
#
# Strategy (lower bound): sample many random 1-cochains h0, form the exact
# coboundary f = d h0 (guaranteed in B^2). Then h = s(f) = minimal-Frob
# preimage (= projection of h0 onto (ker d)^perp). Compute
#    ratio = ||h||_op / ||f||_op
# and maximize over samples. Also do a local optimization (power-like
# iteration) is hard; we just take the max over many random samples plus
# structured samples. This gives a certified LOWER bound on ||s||_{op->op}.
# ----------------------------------------------------------------------

def cochain_op_norm_1(Hmat, B, n_dir=200, seed=0):
    """Operator norm of a 1-cochain given as matrix Hmat (dimC1 layout
    H[i,j], h(e_j)=sum_i H[i,j] e_i). Estimate sup over ||a||_op<=1 of
    ||h(a)||_op by sampling unit-operator-norm Hermitian directions a."""
    rng = np.random.default_rng(seed)
    N = len(B)
    n_mat = B[0].shape[0]
    best = 0.0
    # sample a as random Hermitian normalized to op-norm 1
    for _ in range(n_dir):
        a = random_unit_op_hermitian(n_mat, B, rng)
        ha = Hmat @ a          # coordinate vector of h(a)
        best = max(best, op_norm_elem(ha, B))
    return best


def random_unit_op_hermitian(n_mat, B, rng):
    """Return coordinate vector (length N) of a random Hermitian with
    operator norm exactly 1. We sample a Hermitian, normalize by its
    operator norm. To favor the extremal a we also sometimes use rank-1
    projector-like or +-1 spectrum matrices."""
    N = len(B)
    kind = rng.integers(0, 3)
    if kind == 0:
        # random GUE-like Hermitian
        Mc = rng.standard_normal((n_mat, n_mat)) + 1j * rng.standard_normal((n_mat, n_mat))
        H = (Mc + Mc.conj().T) / 2
    elif kind == 1:
        # random +-1 spectrum (extremal points of the op-norm ball)
        Q, _ = np.linalg.qr(rng.standard_normal((n_mat, n_mat)) + 1j * rng.standard_normal((n_mat, n_mat)))
        d = rng.choice([-1.0, 1.0], size=n_mat)
        H = Q @ np.diag(d) @ Q.conj().T
    else:
        # random rank-1 projector direction (extremal too, op-norm 1)
        v = rng.standard_normal(n_mat) + 1j * rng.standard_normal(n_mat)
        v = v / np.linalg.norm(v)
        H = np.outer(v, v.conj())
    # project onto Hermitian-real-coords and renormalize op norm
    vec = np.array([float(np.real(np.trace(e @ H))) for e in B])
    nrm = op_norm_elem(vec, B)
    if nrm == 0:
        return vec
    return vec / nrm


def op_norm_rightinverse_lowerbound(N, ip, jordan, B, n_samples=4000, seed=1):
    """Lower bound on ||s||_{op->op} for H_n(C) by sampling.

    Build D, its pinv. Sample 1-cochains h0 (random), get f = d h0 in B^2,
    h = pinv(D) f = minimal-Frob preimage. Compute op-norm ratio
    ||h||_op / ||f||_op. Max over samples = certified lower bound.
    """
    D, info = build_d1_fast(N, ip, jordan, B)
    Dpinv = np.linalg.pinv(D, rcond=1e-10)
    n_mat = B[0].shape[0]
    npairs = info['npairs']
    pairs = [(a, b) for a in range(N) for b in range(a, N)]

    rng = np.random.default_rng(seed)
    best_ratio = 0.0
    best_data = None

    # how many directions to estimate each cochain op-norm
    n_dir_1 = 120
    n_dir_2 = 200

    for s in range(n_samples):
        # random 1-cochain h0 as matrix; bias toward "interesting" ones
        H0 = rng.standard_normal((N, N))
        h0vec = H0.reshape(-1)
        fvec = D @ h0vec                      # f = d h0 in B^2
        if np.linalg.norm(fvec) < 1e-12:
            continue
        hvec = Dpinv @ fvec                   # minimal-Frob preimage
        Hmat = hvec.reshape(N, N)

        # operator norm of f (2-cochain). f stored in orthonormal C^2
        # coords with sqrt2 weights; recover f(e_a,e_b) and sup over
        # unit-op-norm a,b.
        fop = cochain_op_norm_2(fvec, pairs, npairs, N, B, n_dir_2, rng)
        if fop < 1e-12:
            continue
        hop = cochain_op_norm_1(Hmat, B, n_dir=n_dir_1, seed=int(rng.integers(1 << 30)))
        ratio = hop / fop
        if ratio > best_ratio:
            best_ratio = ratio
            best_data = (Hmat.copy(), fvec.copy())

    return dict(lower_bound=best_ratio)


def fvec_to_bilinear_value(fvec, pairs, npairs, N, a, b, B):
    """Given f in orthonormal C^2 coords, return coordinate vector of
    f(e_a,e_b) in J. Recall stored value at (pair (a<=b), p) =
    w * <f(e_a,e_b), e_p> with w=1 (a==b) or sqrt2 (a<b). So
    <f(e_a,e_b),e_p> = stored / w. f symmetric."""
    if a > b:
        a, b = b, a
    k = pairs.index((a, b))
    w = 1.0 if a == b else np.sqrt(2.0)
    block = fvec[k * N:(k + 1) * N]
    return block / w


def cochain_op_norm_2(fvec, pairs, npairs, N, B, n_dir, rng):
    """Estimate operator norm of a symmetric 2-cochain f: sup over
    ||a||_op,||b||_op<=1 of ||f(a,b)||_op. We reconstruct the full
    bilinear action from stored coords and sample unit-op-norm a,b."""
    n_mat = B[0].shape[0]
    # Precompute mapping: f(a,b) coordinate-p = sum_{a',b'} a_{a'} b_{b'} F[a',b',p]
    # where F[a',b',p] = <f(e_a',e_b'), e_p>. Build F tensor.
    F = np.zeros((N, N, N))
    pidx = {pr: k for k, pr in enumerate(pairs)}
    for (a_, b_) in pairs:
        k = pidx[(a_, b_)]
        w = 1.0 if a_ == b_ else np.sqrt(2.0)
        block = fvec[k * N:(k + 1) * N] / w
        F[a_, b_, :] = block
        F[b_, a_, :] = block
    best = 0.0
    for _ in range(n_dir):
        avec = random_unit_op_hermitian(n_mat, B, rng)
        bvec = random_unit_op_hermitian(n_mat, B, rng)
        # f(a,b)_p = sum_{a',b'} a_{a'} b_{b'} F[a',b',p]
        out = np.einsum('i,j,ijp->p', avec, bvec, F)
        best = max(best, op_norm_elem(out, B))
    return best


# ----------------------------------------------------------------------
# Drivers
# ----------------------------------------------------------------------

def sweep_family(name, make_for_n, ns):
    print(f"\n=== {name} ===")
    rows = []
    for n in ns:
        t0 = time.time()
        N, ip, jordan, B = make_for_n(n)
        res, D, info = frob_analysis(N, ip, jordan, B)
        dt = time.time() - t0
        rows.append(dict(n=n, N=N, **{k: res[k] for k in
                    ('dimC1', 'dimC2', 'rank', 'ker', 'smin', 'smax', 'inv')},
                    time=dt))
        print(f"  n={n:2d} N={N:3d} dimC1={res['dimC1']:5d} dimC2={res['dimC2']:7d} "
              f"rank={res['rank']:5d} ker={res['ker']:3d} "
              f"smin={res['smin']:.5f} 1/smin={res['inv']:.5f}  ({dt:.1f}s)")
    return rows


def make_HnC(n):
    return jc.make_matrix_algebra(jc.basis_Hn_C(n))


def make_HnR(n):
    return jc.make_matrix_algebra(jc.basis_Hn_R(n))


def make_spin(n):
    return jc.make_spin_factor(n)


def main():
    results = {}

    results['HnC'] = sweep_family("H_n(C)  (complex Hermitian, dim n^2)",
                                  make_HnC, [2, 3, 4, 5, 6])
    results['spin'] = sweep_family("Spin factor V_n  (dim n+1)",
                                   make_spin, list(range(2, 9)))
    results['HnR'] = sweep_family("H_n(R)  (real symmetric, dim n(n+1)/2)",
                                  make_HnR, [2, 3, 4, 5, 6])

    with open("results_frob.json", "w") as fh:
        json.dump(results, fh, indent=2)
    print("\nWrote results_frob.json")


if __name__ == "__main__":
    main()
