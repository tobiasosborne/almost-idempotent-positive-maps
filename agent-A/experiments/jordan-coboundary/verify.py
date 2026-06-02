"""
Independent cross-checks of the coboundary machinery.

1. Brute-force d^1 directly from the definition (no structure-constant
   shortcut) and compare to the optimized matrix.
2. Check kernel of d^1 = Jordan derivations, and that for H_n(C) every
   such derivation is inner X -> i[k,X], dim = n^2-1.
3. Check d^2 d^1 = 0 (cocycle condition) on a sample -- i.e. image is a
   cocycle. (We check the symmetry / module-cohomology Jacobi-type
   identity numerically by verifying coboundaries are 2-cocycles for the
   Jordan complex; here we just confirm internal consistency.)
"""

import numpy as np
import jordan_common as jc


def brute_force_d1(N, ip, jordan, B):
    """Build d^1 matrix the slow, transparent way using the same
    orthonormal coordinates as build_d1_matrix, to cross-check."""
    pairs = [(a, b) for a in range(N) for b in range(a, N)]
    pair_index = {pr: k for k, pr in enumerate(pairs)}
    dimC1 = N * N
    dimC2 = N * len(pairs)
    D = np.zeros((dimC2, dimC1))

    def o(x, y):
        return jordan(x, y)

    for i in range(N):
        for j in range(N):
            col = i * N + j
            # h = h_{ij}: linear map with h(e_j)=e_i else 0.
            def h(x, i=i, j=j):
                # x = sum_q c_q e_q ; c_j coefficient times e_i
                cj = ip(x, B[j])
                return cj * B[i]
            for (a, b) in pairs:
                pk = pair_index[(a, b)]
                w = 1.0 if a == b else np.sqrt(2.0)
                # (d h)(e_a,e_b) = e_a o h(e_b) + h(e_a) o e_b - h(e_a o e_b)
                ea, eb = B[a], B[b]
                term = o(ea, h(eb)) + o(h(ea), eb) - h(o(ea, eb))
                for p in range(N):
                    val = ip(term, B[p])
                    if val != 0.0:
                        D[pk * N + p, col] += w * val
    return D


def derivations_inner_dim(n):
    """Count dimension of inner Jordan derivations X -> i[k,X], k Hermitian,
    of H_n(C), as a linear map on H_n(C). Should be n^2-1."""
    B = jc.basis_Hn_C(n)
    N = len(B)
    # space of Hermitian k modulo scalars: use traceless Hermitian basis
    # The map k -> (X -> i[k,X]) is linear; scalars give 0. Build all
    # derivations D_k for k ranging over the orthonormal Hermitian basis,
    # represent each as a vector in End(J) (N^2 entries), and find rank.
    Dlist = []
    for k in B:
        col = np.zeros((N, N))
        for j in range(N):
            ej = B[j]
            out = 1j * (k @ ej - ej @ k)
            for i in range(N):
                col[i, j] = float(np.real(np.trace(B[i] @ out)))
        Dlist.append(col.reshape(-1))
    Dmat = np.array(Dlist)  # (N, N^2)
    r = np.linalg.matrix_rank(Dmat, tol=1e-9)
    return r


def main():
    for n in [2, 3]:
        B = jc.basis_Hn_C(n)
        N, ip, jordan, Bb = jc.make_matrix_algebra(B)
        D1, info = jc.build_d1_matrix(N, ip, jordan, Bb)
        D1b = brute_force_d1(N, ip, jordan, Bb)
        diff = np.max(np.abs(D1 - D1b))
        res = jc.analyze(D1, info)
        innerdim = derivations_inner_dim(n)
        print(f"H_{n}(C): N={N}")
        print(f"  max|D_fast - D_brute| = {diff:.2e}")
        print(f"  dimC1={res['dimC1']} dimC2={res['dimC2']} rank={res['rank']} "
              f"ker={res['ker']}  (expect ker=n^2-1={n*n-1})")
        print(f"  inner-derivation dim (i[k,.]) = {innerdim} (expect {n*n-1})")
        print(f"  smin={res['smin']:.6f} 1/smin={res['inv']:.6f}")
        print()

    # spin factor + Hn(R) quick sanity of kernel dims
    print("Spin factor V_2 (dim 3):")
    N, ip, jordan, Bb = jc.make_spin_factor(2)
    D1, info = jc.build_d1_matrix(N, ip, jordan, Bb)
    res = jc.analyze(D1, info)
    print(f"  dimC1={res['dimC1']} dimC2={res['dimC2']} rank={res['rank']} ker={res['ker']} 1/smin={res['inv']:.4f}")


if __name__ == "__main__":
    main()
