# Complex Skew-Connection Residual

Date: 2026-06-05.

This note records the exact fixed-frame formula for the skew sector-preserving
residual in

```text
J=H_n(C).
```

It complements `agent-B/notes/sector-preserving-schur-residual.md`, which
handles the real scalar edge-symbol part. The complex skew part has a gauge:
diagonal frame-stabilizer derivations.

## Setup

For an ordered pair `i != j`, write

```text
X_ij(z)=z E_ij + conj(z) E_ji        (z in C).
```

The off-diagonal Peirce space `V_ij` is identified with `C` by
`z -> X_ij(z)`.

Let `beta_ij` be real and skew-symmetric:

```text
beta_ji=-beta_ij,        beta_ii=0.
```

Define the skew sector-preserving operator

```text
K_beta X_ij(z)=X_ij(i beta_ij z),        K_beta(e_i)=0.
```

This is real-linear and maps Hermitian matrices to Hermitian matrices.

## Gauge Directions

Let

```text
A=i diag(alpha_1,...,alpha_n)
```

be a diagonal skew-Hermitian matrix. The Jordan derivation

```text
delta_A(x)=[A,x]
```

acts on `V_ij` by

```text
delta_A X_ij(z)=X_ij(i(alpha_i-alpha_j)z).
```

Thus

```text
beta_ij=alpha_i-alpha_j
```

is pure gauge. The residual connection problem must control `beta` modulo
these additive coboundaries.

## Curvature Formula

For distinct `i,j,k`,

```text
X_ij(z) o X_jk(w) = (1/2) X_ik(zw).
```

Therefore, with `f=d^1K_beta`,

```text
f(X_ij(z),X_jk(w))
 = (i/2)(beta_ij+beta_jk-beta_ik) X_ik(zw).
```

Equivalently, the curvature is the triangle defect

```text
curv beta(i,j,k)=beta_ij+beta_jk-beta_ik.
```

Pure gauges have zero curvature.

For a single edge, the square term does not see the skew part:

```text
f(X_ij(z),X_ij(z))=0.
```

This is the exact reason the complex skew sector is different from the real
scalar sector, where edge square terms detect `m_ij` pointwise.

## Residual Target And Status

The complex skew residual asks for a dimension-free estimate of the form

```text
dist(K_beta, Der_diag)_{Schur}
  <= C ||d^1 K_beta||_{bilinear inj},
```

where `Der_diag` consists of the gauge symbols

```text
beta_ij=alpha_i-alpha_j.
```

This is a noncommutative complete-graph connection estimate in Schur
multiplier norm. Pointwise curvature control is not enough:
`agent-B/notes/pointwise-schur-curvature-caveat.md` records the triangular
sign symbol `beta_ij=sign(i-j)`, whose pointwise curvature is bounded while
the Schur multiplier norm grows logarithmically.

The full bilinear norm of `d^1K_beta`, not only
`sup |curv beta(i,j,k)|`, is the correct object. This estimate is now proved
by the matching-slice and random matching reconstruction arguments in
`agent-B/notes/matching-slice-schur-detection.md`,
`agent-B/notes/pure-skew-matching-reconstruction-theorem.md`, and the combined
scalar Hermitian corollary
`agent-B/notes/hermitian-scalar-sector-reconstruction-corollary.md`.

Thus the one-dimensional diagonal-skew connection sector is no longer an open
high-rank obstruction. Combined with
`agent-B/notes/complex-antilinear-peirce-residual-theorem.md`, the
fixed-frame sector-preserving edge-map residual for `H_n(C)` is controlled
after formal off-sector leakage removal. The remaining complex matrix work is
the coherent globalization of off-sector leakage.
