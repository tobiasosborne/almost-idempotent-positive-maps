"""
Vectorized build of the d^1 coboundary matrix using the structure
constants M[a,b,q] = <e_a o e_b, e_q>.  Mathematically identical to
jordan_common.build_d1_matrix (verified against it), just faster for
larger N so n=6 (N=36) runs quickly.

Recall column = (i,j) -> h_{ij}; row = (pair k=(a<=b), output p).
(d h_{ij})(e_a,e_b)_p =
      delta_{j,b} M[a,i,p]  +  delta_{j,a} M[i,b,p]  -  delta_{i,p} M[a,b,j]
with orthonormal C^2 weight w = 1 (a==b) or sqrt(2) (a<b).
"""

import numpy as np
import jordan_common as jc


def structure_constants(N, ip, jordan, B):
    M = np.zeros((N, N, N))
    JP = [[jordan(B[a], B[b]) for b in range(N)] for a in range(N)]
    for a in range(N):
        for b in range(N):
            jab = JP[a][b]
            for q in range(N):
                M[a, b, q] = ip(jab, B[q])
    return M


def build_d1_fast(N, ip, jordan, B):
    M = structure_constants(N, ip, jordan, B)  # M[a,b,q]
    pairs = [(a, b) for a in range(N) for b in range(a, N)]
    npairs = len(pairs)
    dimC1 = N * N
    dimC2 = N * npairs
    D = np.zeros((dimC2, dimC1))

    # Column index col = i*N + j. We fill contributions.
    # Build by iterating over pairs (cheap: npairs ~ N^2/2), vectorizing
    # over (i, j, p) where possible.

    # term1: delta_{j,b} M[a,i,p]  -> for pair (a,b), and j=b fixed,
    #         contributes to col = i*N + b, row = (pair,p): value M[a,i,p].
    # term2: delta_{j,a} M[i,b,p]  -> j=a, col=i*N+a, row(pair,p): M[i,b,p].
    # term3: -delta_{i,p} M[a,b,j] -> i=p, col=p*N+j, row(pair,p): -M[a,b,j].

    for k, (a, b) in enumerate(pairs):
        w = 1.0 if a == b else np.sqrt(2.0)
        base = k * N  # rows base..base+N-1 correspond to p=0..N-1

        # term1: rows p=0..N-1, cols i*N + b for i=0..N-1, value M[a,i,p]
        # M[a,:,:] has shape (N_i, N_p); we need D[base+p, i*N+b] += w*M[a,i,p]
        Mai = M[a]              # shape (i, p)
        # add transpose so index by [p, i]
        cols_b = np.arange(N) * N + b
        D[base:base + N, cols_b] += w * Mai.T   # rows=p, cols=i

        # term2: rows p, cols i*N + a, value M[i,b,p]
        Mib = M[:, b, :]        # shape (i, p)
        cols_a = np.arange(N) * N + a
        D[base:base + N, cols_a] += w * Mib.T   # rows=p, cols=i

        # term3: rows p (with i=p), cols p*N + j, value -M[a,b,j]
        Mabj = M[a, b, :]       # shape (j,)
        # for each p: col = p*N + j, value -M[a,b,j]; only i=p row.
        # D[base+p, p*N + j] -= w*M[a,b,j]
        for p in range(N):
            D[base + p, p * N: p * N + N] -= w * Mabj

    info = dict(dimC1=dimC1, dimC2=dimC2, N=N, npairs=npairs)
    return D, info


if __name__ == "__main__":
    # cross check vs the slow builder for small N
    for builder, n in [(jc.basis_Hn_C, 2), (jc.basis_Hn_C, 3)]:
        B = builder(n)
        N, ip, jordan, Bb = jc.make_matrix_algebra(B)
        Dslow, info1 = jc.build_d1_matrix(N, ip, jordan, Bb)
        Dfast, info2 = build_d1_fast(N, ip, jordan, Bb)
        print(f"H_{n}(C): max|fast-slow| = {np.max(np.abs(Dfast-Dslow)):.2e}")
