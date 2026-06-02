"""
Common machinery for the Jordan-cohomology coboundary experiment.

We study the Jordan coboundary operator
    (d^1 h)(a,b) = a o h(b) + h(a) o b - h(a o b)
mapping 1-cochains C^1 = Lin(J,J) to 2-cochains C^2 = Sym^2(J) -> J
(symmetric bilinear maps J x J -> J), for the ADJOINT module M = J.

Everything is done in an ORTHONORMAL real basis of J w.r.t. the
Frobenius inner product <x,y> = Re tr(x* y) = Re tr(x y) for Hermitian x,y.

Inner products on cochain spaces (so singular values are meaningful):

  C^1:  identify h with its matrix H_{ij}, h(e_j)=sum_i H_{ij} e_i.
        <h,h'> = sum_{i,j} H_{ij} H'_{ij}   (Hilbert-Schmidt, standard R^{N^2}).

  C^2:  a symmetric bilinear f is determined by f(e_i,e_j), i<=j.
        The Frobenius-induced inner product on bilinear maps is
            <f,f'> = sum_{i,j over ALL ordered pairs} <f(e_i,e_j), f'(e_i,e_j)>.
        For SYMMETRIC f this equals
            sum_{i<j} 2 <f(e_i,e_j),f'(e_i,e_j)> + sum_i <f(e_i,e_i),f'(e_i,e_i)>.
        We build d^1 as a matrix in an ORTHONORMAL basis of (C^2, this IP),
        using basis 2-cochains weighted so that diagonal pairs get weight 1
        and off-diagonal pairs get weight sqrt(2). Then the singular values
        of the matrix are exactly the singular values w.r.t. these IPs.

The matrix representation:
  C^1 coordinate index = (i,j) for h-matrix entry H_{ij}, dimension N^2.
  C^2 coordinate index = (p; i<=j) where p indexes the output basis vector
    e_p and (i,j) the (orthonormal) input pair, dimension N*N(N+1)/2.

Author: agent-A experiment
"""

import numpy as np
import itertools


# ----------------------------------------------------------------------
# Jordan algebras: each returns a list of N real ORTHONORMAL basis
# matrices (as complex or real numpy arrays) together with the unit and a
# Jordan-product function on the algebra elements.
# ----------------------------------------------------------------------

def basis_Hn_C(n):
    """Orthonormal real basis of H_n(C) (n x n complex Hermitian),
    real dimension N = n^2, orthonormal w.r.t. <x,y>=Re tr(xy)."""
    B = []
    # diagonal: E_kk
    for k in range(n):
        M = np.zeros((n, n), dtype=complex)
        M[k, k] = 1.0
        B.append(M)
    # off-diagonal real & imaginary parts
    for j in range(n):
        for k in range(j + 1, n):
            S = np.zeros((n, n), dtype=complex)
            S[j, k] = 1.0 / np.sqrt(2.0)
            S[k, j] = 1.0 / np.sqrt(2.0)
            B.append(S)
            A = np.zeros((n, n), dtype=complex)
            A[j, k] = 1j / np.sqrt(2.0)
            A[k, j] = -1j / np.sqrt(2.0)
            B.append(A)
    return B


def basis_Hn_R(n):
    """Orthonormal real basis of H_n(R) (n x n real symmetric),
    real dimension N = n(n+1)/2."""
    B = []
    for k in range(n):
        M = np.zeros((n, n), dtype=float)
        M[k, k] = 1.0
        B.append(M)
    for j in range(n):
        for k in range(j + 1, n):
            S = np.zeros((n, n), dtype=float)
            S[j, k] = 1.0 / np.sqrt(2.0)
            S[k, j] = 1.0 / np.sqrt(2.0)
            B.append(S)
    return B


def make_matrix_algebra(B):
    """Given an orthonormal basis B of a Jordan algebra of matrices,
    return (N, ip, jordan) where
       ip(x,y)   = Re tr(x y)   (the Frobenius inner product)
       jordan(x,y) = (xy+yx)/2.
    """
    N = len(B)

    def ip(x, y):
        return float(np.real(np.trace(x @ y)))

    def jordan(x, y):
        return 0.5 * (x @ y + y @ x)

    return N, ip, jordan, B


def make_spin_factor(n):
    """Spin factor V_n = R (+) R^n, dim N = n+1, product
       (s,v) o (t,w) = (s t + <v,w>,  s w + t v).
    Unit = (1, 0). We represent elements as vectors of length n+1:
    coordinate 0 = scalar part, coordinates 1..n = vector part.
    The natural inner product making the standard basis orthonormal is
    the Euclidean inner product on R^{n+1}; one checks the standard basis
    is orthonormal and the Jordan identity holds. Returns (N, ip, jordan, B)
    with B the standard orthonormal basis vectors e_0,...,e_n.
    """
    N = n + 1
    B = [np.eye(N)[k].copy() for k in range(N)]

    def ip(x, y):
        return float(np.dot(x, y))

    def jordan(x, y):
        s, v = x[0], x[1:]
        t, w = y[0], y[1:]
        out = np.zeros(N)
        out[0] = s * t + float(np.dot(v, w))
        out[1:] = s * w + t * v
        return out

    return N, ip, jordan, B


# ----------------------------------------------------------------------
# Build the coboundary matrix.
# ----------------------------------------------------------------------

def build_d1_matrix(N, ip, jordan, B):
    """
    Build d^1 : C^1 -> C^2 as a real matrix in orthonormal coordinates.

    Returns (D, info) where D has shape (dimC2, dimC1).

    dimC1 = N^2
    dimC2 = N * N(N+1)/2

    Coordinates:
      C^1 column index c = i*N + j  <-> H_{ij} (h(e_j) = sum_i H_{ij} e_i).
        The basis 1-cochain h_{ij} is: h_{ij}(e_j)=e_i, else 0. It has
        Hilbert-Schmidt norm 1, so these are an orthonormal basis of C^1.

      C^2 row index r runs over (p, pair_index) where p in 0..N-1 is the
        output coordinate and pair_index enumerates pairs (a<=b).
        The orthonormal basis 2-cochains of C^2 are:
           g_{p,(a,a)}: f(e_a,e_a)=e_p, else 0.            norm 1
           g_{p,(a,b)} (a<b): f(e_a,e_b)=f(e_b,e_a)= e_p/sqrt(2). norm 1
        (Check: <g,g> for a<b = 2 * (1/sqrt2)^2 * 1 = 1.)
        The coordinate of a 2-cochain f along g_{p,(a,a)} is
           <f, g_{p,(a,a)}> = <f(e_a,e_a), e_p>.
        Along g_{p,(a,b)}, a<b:
           <f, g_{p,(a,b)}> = 2 * <f(e_a,e_b), e_p/sqrt2> = sqrt(2)*<f(e_a,e_b),e_p>.
    """
    # Precompute Jordan products of basis pairs, and Jordan products needed.
    # We need, for the coboundary: a o h(b), h(a) o b, h(a o b).
    # With h = h_{ij}: h(e_b) = delta_{j,b} e_i.
    # So (d h_{ij})(e_a,e_b) =
    #     delta_{j,b} (e_a o e_i)  +  delta_{j,a} (e_i o e_b)
    #     - <e_a o e_b , basis>... we need h(e_a o e_b).
    # e_a o e_b = sum_q M[a,b,q] e_q, with M[a,b,q] = <e_a o e_b, e_q>.
    # h_{ij}(e_a o e_b) = sum_q M[a,b,q] h_{ij}(e_q) = M[a,b,j] e_i.
    #
    # Therefore in coordinates (output along e_p):
    #   (d h_{ij})(e_a,e_b)_p =
    #       delta_{j,b} <e_a o e_i, e_p>
    #     + delta_{j,a} <e_i o e_b, e_p>
    #     - M[a,b,j] delta_{i,p}.

    # structure constants M[a,b,q] = <e_a o e_b, e_q>
    M = np.zeros((N, N, N))
    JP = [[jordan(B[a], B[b]) for b in range(N)] for a in range(N)]
    for a in range(N):
        for b in range(N):
            jab = JP[a][b]
            for q in range(N):
                M[a, b, q] = ip(jab, B[q])

    # enumerate symmetric pairs a<=b
    pairs = [(a, b) for a in range(N) for b in range(a, N)]
    npairs = len(pairs)
    assert npairs == N * (N + 1) // 2
    pair_index = {pr: k for k, pr in enumerate(pairs)}

    dimC1 = N * N
    dimC2 = N * npairs
    D = np.zeros((dimC2, dimC1))

    # For each 1-cochain basis element h_{ij}, compute its image's coords.
    for i in range(N):
        for j in range(N):
            col = i * N + j
            # image f = d h_{ij}; compute f(e_a,e_b)_p for all pairs a<=b
            for (a, b) in pairs:
                pk = pair_index[(a, b)]
                # weight for the orthonormal C^2 basis along this pair
                w = 1.0 if a == b else np.sqrt(2.0)
                for p in range(N):
                    val = 0.0
                    # delta_{j,b} <e_a o e_i, e_p>
                    if j == b:
                        val += M[a, i, p]
                    # delta_{j,a} <e_i o e_b, e_p>
                    if j == a:
                        val += M[i, b, p]
                    # - M[a,b,j] delta_{i,p}
                    if i == p:
                        val -= M[a, b, j]
                    if val != 0.0:
                        row = pk * N + p
                        D[row, col] += w * val
    info = dict(dimC1=dimC1, dimC2=dimC2, N=N, npairs=npairs)
    return D, info


def analyze(D, info, tol=None):
    """Compute SVD-based quantities. Returns a dict."""
    sv = np.linalg.svd(D, compute_uv=False)
    smax = sv[0] if len(sv) else 0.0
    # numerical rank threshold
    if tol is None:
        tol = max(D.shape) * np.finfo(float).eps * (smax if smax > 0 else 1.0)
    rank = int(np.sum(sv > tol))
    nonzero = sv[sv > tol]
    smin = nonzero.min() if len(nonzero) else 0.0
    res = dict(
        dimC1=info['dimC1'],
        dimC2=info['dimC2'],
        rank=rank,
        ker=info['dimC1'] - rank,
        smin=float(smin),
        smax=float(smax),
        inv=float(1.0 / smin) if smin > 0 else np.inf,
        tol=float(tol),
        sv=sv,
    )
    return res
