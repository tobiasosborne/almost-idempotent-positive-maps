# Sector-Preserving Schur Residual

Date: 2026-06-05.

This note isolates and then records the resolution of the real fixed-frame
sector-preserving residual left by
`agent-B/notes/fixed-frame-peirce-matrix-reduction.md`.

The exact formulas below show that the `H_n(R)` sector-preserving problem is a
bilinear Schur-multiplier lower-bound problem. That lower-bound problem is now
controlled dimension-free by
`agent-B/notes/real-symmetric-matching-reconstruction-theorem.md`.

## Setup

Let

```text
J=H_n(R)
```

with the standard Jordan frame `e_1,...,e_n` and off-diagonal symmetries

```text
s_ij=E_ij+E_ji,        i<j.
```

Assume the diagonal gauge has been fixed and the off-sector leakage has been
removed formally, so the residual primitive has

```text
h(e_i)=0,
h(s_ij)=m_ij s_ij,
```

with real symmetric edge weights `m_ij=m_ji` and `m_ii=0`.

This is the sector-preserving Schur multiplier

```text
M_m(x)_ij=m_ij x_ij        (i != j),        M_m(x)_ii=0.
```

The operator norm of this residual primitive is the Schur-multiplier norm of
`m` on real symmetric matrices with the usual operator norm. The reconstruction
argument below proves the stronger estimate for the all-matrix Schur
multiplier extension with the same ordered symbol.

## Coboundary Formula

For distinct indices, the Jordan products are

```text
s_ij o s_ij = e_i+e_j,
s_ij o s_jk = (1/2)s_ik,
s_ij o s_kl = 0        if {i,j} cap {k,l}=empty.
```

Therefore `f=d^1h` satisfies:

```text
f(s_ij,s_ij)=2m_ij(e_i+e_j),
```

and for distinct `i,j,k`,

```text
f(s_ij,s_jk)
  = (1/2)(m_ij+m_jk-m_ik)s_ik.
```

The analogous formula holds for every path of length two:

```text
f(s_ij,s_ik)
  = (1/2)(m_ij+m_ik-m_jk)s_jk.
```

For disjoint edges,

```text
f(s_ij,s_kl)=0.
```

Thus the residual is governed by:

1. the edge weights `m_ij`, detected pointwise by the square terms; and
2. the triangle coboundaries

```text
partial m(i,j,k)=m_ij+m_jk-m_ik.
```

For general real symmetric matrices `x,y`, the same computation gives the
coordinate formula

```text
(d^1M_m(x,y))_ik
 = (1/2) sum_j (m_ij+m_jk-m_ik)(x_ij y_jk+y_ij x_jk)
        for i != k,
```

and the diagonal formula

```text
(d^1M_m(x,y))_ii = 2 sum_{j != i} m_ij x_ij y_ij.
```

So the off-diagonal part is a symmetrized bilinear Schur multiplier with
three-index symbol `partial m(i,j,k)`, while the diagonal part detects edge
weights through squares.

## Exact Residual Target

The real sector-preserving estimate is:

```text
||M_m||_{S_infty->S_infty}
  <= C ||d^1 M_m||_{inj}
```

with a universal constant `C`, where `d^1M_m` is equivalently the bilinear
Schur-triangle multiplier described above.

Pointwise bounds are insufficient. The square terms give

```text
sup_ij |m_ij| <= (1/2)||d^1M_m||,
```

and the mixed edge terms give pointwise control of `partial m(i,j,k)`.
Neither pointwise estimate controls the Schur-multiplier norm of `m`
dimension-freely.

The full bilinear operator norm of `d^1M_m` must be used. The estimate is
proved in `agent-B/notes/real-symmetric-matching-reconstruction-theorem.md`
by reconstructing the all-matrix Schur multiplier from ordered matching
curvature slices and the square-detected edge weights.

## Middle-Slice Caveat

Fixing a base vertex `p` gives the exact identity

```text
m_ik=m_ip+m_pk-partial m(i,p,k).
```

The first two terms are controlled pointwise by the square part of `d^1M_m`.
It is therefore tempting to control the remaining Schur multiplier by the
middle slice

```text
partial m(i,p,k).
```

This is an amplification step. In the ordinary bilinear norm, testing
`d^1M_m` on star-supported matrices through the vertex `p` only sees products

```text
x_ip y_pk,
```

i.e. rank-one matrices on the `i,k` indices. A full Schur multiplier norm
requires control on arbitrary matrices, not just rank-one products. Thus the
base-vertex identity suggests a completely bounded or amplified route, but it
does not by itself prove the desired order/operator-norm estimate.

## Schur Stress Test

The obstruction sidecar audit tested logarithmic Schur multipliers. These have
symbols with bounded pointwise entries but Schur-multiplier norm growing like
`log n`.

For such examples, the sampled norm of `d^1M_m` also grows logarithmically.
This is consistent with the desired residual estimate and explains why the
Schur examples are serious stress tests but not counterexamples.

## Interpretation

For `H_n(R)`, after the fixed-frame reductions, the sector-preserving Schur
residual is now controlled:

```text
||M_m|| <= 60 ||d^1M_m||_inj.
```

The remaining high-rank matrix problem is no longer this one-dimensional real
sector-preserving Schur multiplier. Combined with
`agent-B/notes/hermitian-scalar-sector-reconstruction-corollary.md` and
`agent-B/notes/complex-antilinear-peirce-residual-theorem.md`, the fixed-frame
sector-preserving residual is also controlled for `H_n(C)` after formal
off-sector leakage removal. The quaternionic internal residual is controlled
in `agent-B/notes/quaternionic-internal-peirce-residual-theorem.md`.
Off-sector leakage is globalized in
`agent-B/notes/off-sector-leakage-globalization-theorem.md`, and the assembled
matrix result is recorded in
`agent-B/notes/matrix-factor-exact-adjoint-splitting-theorem.md`.
