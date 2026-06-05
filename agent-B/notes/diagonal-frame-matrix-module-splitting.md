# Diagonal Frame Matrix Module Splitting

Date: 2026-06-04.

This note refines the caveat in
`agent-B/notes/peirce-sector-norm-accumulation.md`.

The Peirce-sector inclusion

```text
direct_sum_{i<j}^{l_infty} R(E_ij+E_ji) -> H_n(R)
```

has norm at least `n-1`. Therefore a proof cannot simply pass through the max
sector norm and then include all sectors into the matrix operator norm.

However, this accumulation is not by itself an obstruction to the exact
coboundary problem for a diagonal frame. There is a dimension-free right
inverse for the restriction of the adjoint matrix module to the diagonal
subalgebra, obtained by a Rademacher/Schur-multiplier formula.

## Setup

Let `F` be `R`, `C`, or `H`, and let

```text
M = H_n(F)
```

with its usual operator norm. Let

```text
B = R^n
```

act by the diagonal Jordan action

```text
x . A = (D_x A + A D_x)/2,
```

where `D_x=diag(x_1,...,x_n)`. This is the restriction of the adjoint module of
`H_n(F)` to the diagonal Jordan frame.

For cochains use

```text
||h|| = sup_{||x||_infty<=1} ||h(x)||_op,
||f|| = sup_{||x||_infty,||y||_infty<=1} ||f(x,y)||_op.
```

The coboundary is

```text
(d^1 h)(x,y)=x.h(y)+y.h(x)-h(xy).
```

## Theorem

There is a linear right inverse

```text
S_n : im(d^1) -> C^1(B,M)
```

with

```text
d^1 S_n f = f,
||S_n f|| <= 11 ||f||.
```

The constant is independent of `n` and of `F in {R,C,H}`.

The numerical constant is not optimized.

## Proof

Let `E_diag:M->M` be the diagonal pinching and `E_off=I-E_diag`. The diagonal
pinching is contractive, and

```text
||E_off|| <= 2.
```

Both diagonal and off-diagonal subspaces are invariant under the `B`-action, so
we solve the two components separately.

### Diagonal Part

For the diagonal component `f_d=E_diag f`, define

```text
(S_d f)(x)_i = (f_d(x,e_i))_ii.
```

This is just the coordinate-evaluation splitting from
`commutative-scalar-module-splitting.md`. It satisfies

```text
d^1 S_d f = f_d,
||S_d f|| <= ||f_d|| <= ||f||.
```

### Off-Diagonal Normalization

Let

```text
f_o = E_off f.
```

Then `||f_o||<=2||f||`. Put

```text
m_0=f_o(1,1).
```

Since `f_o` is an exact coboundary, every primitive has value `m_0` at `1`.
Remove this unit value by setting

```text
k(x)=x.m_0=(D_x m_0+m_0D_x)/2,
g=f_o-d^1 k.
```

Then

```text
g(1,1)=0,        g(x,1)=0.
```

Also

```text
||m_0|| <= ||f_o|| <= 2||f||,
||k|| <= ||m_0||.
```

For `||x||_infty,||y||_infty<=1`, a direct calculation gives

```text
(d^1 k)(x,y)
  = (D_x m_0 D_y + D_y m_0 D_x)/2,
```

and therefore

```text
||d^1 k|| <= ||m_0|| <= 2||f||.
```

So

```text
||g|| <= ||f_o||+||d^1 k|| <= 4||f||.
```

### Rademacher Inversion On The Normalized Off-Diagonal Part

Let `epsilon=(epsilon_1,...,epsilon_n)` range over `{+-1}^n` with uniform
measure, and write `D_epsilon=diag(epsilon_i)`.

For normalized off-diagonal exact coboundaries `g`, define

```text
(S_o^0 g)(x)
  = E_epsilon [ D_epsilon g(x,epsilon) + g(x,epsilon) D_epsilon ].
```

This is off-diagonal because `g` is off-diagonal.

To see that this inverts `d^1`, inspect each off-diagonal Peirce entry. For the
`ij` entry the scalar action is

```text
l_ij(x)=(x_i+x_j)/2.
```

Let `g=d^1 h` and `h(1)=0`. Write the `ij` entry of `h` as

```text
h_ij(x)=sum_k t_k x_k.
```

Then `sum_k t_k=0`, and

```text
g_ij(x,epsilon)
 = l_ij(x) h_ij(epsilon)
   + l_ij(epsilon) h_ij(x)
   - h_ij(x epsilon).
```

Taking expectation after multiplying by `epsilon_i+epsilon_j` gives

```text
E[(epsilon_i+epsilon_j)g_ij(x,epsilon)]
 = h_ij(x)
   + l_ij(x)(t_i+t_j)
   - t_i x_i - t_j x_j.
```

Equivalently,

```text
E[(epsilon_i+epsilon_j)g_ij(x,epsilon)]
 = sum_{k notin {i,j}} t_k x_k
   + ((t_i+t_j)/2)(x_i+x_j).
```

This is the canonical representative obtained from `h_ij` by deleting the
antisymmetric kernel component `(t_i-t_j)(x_i-x_j)/2`. It has the same
coboundary as `h_ij`. The matrix formula above is exactly this entrywise
canonical representative. Hence

```text
d^1 S_o^0 g = g.
```

For the norm, each `D_epsilon` is unitary/orthogonal, so

```text
||D_epsilon A + A D_epsilon|| <= 2||A||.
```

Thus

```text
||S_o^0 g|| <= 2||g||.
```

### Combine

Define

```text
S_n f = S_d f + k + S_o^0 g.
```

Then

```text
d^1 S_n f = f_d + d^1 k + g = f_d + f_o = f.
```

The norm bound is

```text
||S_n f||
 <= ||S_d f|| + ||k|| + ||S_o^0 g||
 <= ||f|| + 2||f|| + 2*4||f||
 = 11||f||.
```

This proves the theorem.

## Projection Corollary

The formula for `S_n` is defined for every 2-cochain, not only for exact
coboundaries. Since the diagonal action is contractive,

```text
||d^1 h|| <= 3||h||.
```

Therefore

```text
Pi_n = d^1 S_n : C^2(B,M) -> C^2(B,M)
```

has

```text
||Pi_n|| <= 33.
```

Because `S_n` is a right inverse on `im(d^1)`, `Pi_n` is a projection onto
`im(d^1)`:

```text
Pi_n^2=Pi_n,        ran(Pi_n)=im(d^1).
```

This still does not solve approximate cocycles. It supplies a uniformly bounded
projection onto exact coboundaries for the fixed diagonal-frame complex; a
separate estimate is needed to show that an approximate Jordan 2-cocycle lies
close to this range.

## Consequences

1. The coherent matrix `11^T-I` shows that sectorwise inclusion has large norm,
   but it does not produce a lower bound for the exact coboundary inverse.
   Exact coboundaries contain enough coherence for the Rademacher formula to
   control the off-diagonal sum directly.
2. The diagonal-frame restriction of the adjoint `H_n(F)` module is not the
   high-rank obstruction.
3. The remaining matrix-family Layer-1 problem is genuinely noncommutative:
   one must control cochains for the full matrix Jordan algebra, not only for a
   fixed diagonal frame acting on its Peirce spaces.
