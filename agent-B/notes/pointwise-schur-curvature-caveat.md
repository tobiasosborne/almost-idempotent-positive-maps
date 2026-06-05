# Pointwise Schur Curvature Caveat

Date: 2026-06-05.

This note records a proof-route obstruction inside the residual matrix
benchmark. It is not a counterexample to dimension-free exact-adjoint
splitting. It shows that pointwise bounds on edge symbols and triangle
curvatures cannot control the residual Schur/connection operator norm.

## Complex Skew-Connection Test

Work in

```text
J=H_N(C),        N=2n,
```

with the standard frame. Split the index set into two copies

```text
L={1,...,n},        R={bar 1,...,bar n}.
```

The frame-stabilizer gauge acts on off-diagonal entries by phases of the form

```text
alpha_i-alpha_j.
```

Let `sigma_pq=sign(p-q)` be the triangular sign symbol on `L x R`. Define a
skew connection symbol `beta` by

```text
beta_{p,bar q}=sigma_pq,
beta_{bar q,p}=-sigma_pq,
beta_{ij}=0        otherwise.
```

The corresponding Hermitian Schur symbol is

```text
m_ij=i beta_ij.
```

It maps Hermitian matrices to Hermitian matrices because
`m_ji=conj(m_ij)`. Its pointwise size is bounded:

```text
|m_ij| <= 1.
```

For every triangle of distinct indices,

```text
partial m(i,j,k)=m_ij+m_jk-m_ik
```

also satisfies

```text
|partial m(i,j,k)| <= 3.
```

Thus all edge weights and all pointwise triangle curvatures are uniformly
bounded.

## Schur Norm Still Grows

The corresponding Hermitian Schur multiplier has norm growing like the norm of
the triangular sign multiplier on `M_n(C)`.

Indeed, for an arbitrary `n x n` matrix `A`, form the Hermitian block matrix

```text
X_A = [ 0   A  ]
      [ A*  0  ].
```

Then

```text
||X_A||=||A||,
```

and applying the above skew connection multiplier gives the Hermitian block
matrix with off-diagonal block

```text
i (sigma o A).
```

Thus its Hermitian operator norm is exactly `||sigma o A||`. The sign
multiplier has logarithmic norm because, up to diagonal/off-diagonal
projections of universal norm, the lower triangular projection is obtained
from the identity and the sign multiplier by

```text
T_lower,off = (I_off + sigma)/2.
```

The main triangular projection has norm growing logarithmically with `n`; this
is the classical theorem of Kwapien and Pelczynski, "The main triangle
projection in matrix spaces and its applications", Studia Mathematica 34
(1970), 43-67. EuDML record:

```text
https://eudml.org/doc/217431
```

Therefore this Hermitian skew connection multiplier cannot be controlled
dimension-freely by only the pointwise quantities

```text
sup_ij |m_ij|,        sup_{i,j,k} |partial m(i,j,k)|.
```

## Consequence For The Residual Target

The residual fixed-frame matrix problem cannot be solved by:

1. bounding every edge map `S_ij` pointwise;
2. bounding every triangle curvature coefficient pointwise; and then
3. summing over Peirce sectors.

Such an argument would incorrectly prove a dimension-free bound for the
triangular sign multiplier.

The only plausible target is the full bilinear operator norm of the Jordan
defect

```text
Def(S)(x,y)=x o S(y)+S(x) o y-S(x o y).
```

The obstruction audit remains consistent with this: logarithmic Schur
multipliers are serious stress tests, but their full Jordan defects appear to
have logarithmic norm as well. The caveat here only rules out pointwise
curvature proofs.
