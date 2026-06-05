# Fixed-Frame Peirce Matrix Reduction

Date: 2026-06-05.

This note sharpens the high-rank exact-adjoint matrix benchmark. It does not
solve the benchmark. It records a dimension-free fixed-frame pointwise
reduction for one possible source of trouble: leakage from one off-diagonal
Peirce sector into all other sectors.

The residual problem is a genuinely sector-preserving Schur-multiplier and
frame-stabilizer connection problem, together with the still-required
operator-norm globalization of the pointwise leakage formula.

## Setup

Let

```text
J=H_n(F),        F in {R,C,H},
```

with the standard Jordan frame `e_1,...,e_n`. Write

```text
D=span{e_i},
V_ij=e_i J e_j + e_j J e_i        (i<j)
```

for the diagonal algebra and the off-diagonal Peirce spaces. For `a in D`,
write

```text
l_ij(a)=(a_i+a_j)/2,
```

so that `a o x=l_ij(a)x` for `x in V_ij`.

Let `h:J->J` be a normalized adjoint primitive,

```text
h(1)=0,        f=d^1h,
```

where

```text
f(a,b)=a o h(b)+h(a) o b-h(a o b).
```

All norms below are order-unit/operator norms and injective cochain norms.

## Diagonal Gauge

Restrict `f` to `D x D`. The diagonal-frame splitting from
`agent-B/notes/diagonal-frame-matrix-module-splitting.md` gives a canonical
primitive `s_D:D->J` with

```text
d^1 s_D=f|_{D x D},        ||s_D||<=11||f||.
```

The difference `h|_D-s_D` is in the kernel of the diagonal-frame coboundary.
Entrywise, its `ij` Peirce component is a multiple of

```text
a_i-a_j.
```

Hence it is the restriction to `D` of a derivation of `J`. After subtracting
that derivation, we may assume

```text
||h|_D|| <= 11||f||.
```

This normalization is harmless because derivations are exactly the kernel
directions for the adjoint coboundary.

## Off-Sector Leakage

Fix an edge `ij` and `x in V_ij`. Put

```text
A=h(x).
```

For `a in D`,

```text
f(a,x)=a o h(x)+h(a) o x-h(a o x),
```

and since `a o x=l_ij(a)x`,

```text
(L_a-l_ij(a)I)A = f(a,x)-h(a) o x.        (1)
```

Thus the right side is bounded by

```text
||f|| ||a|| ||x|| + ||h|_D|| ||a|| ||x||
 <= 12||f|| ||a|| ||x||.
```

Let `epsilon in {+-1}^n` and let `D_epsilon` be the corresponding diagonal
symmetry. Define

```text
M_epsilon = L_epsilon-l_ij(epsilon)I.
```

Then `||M_epsilon||<=2`. Average the second application of this operator:

```text
R_ij A = E_epsilon M_epsilon^2 A.
```

On Peirce components, `R_ij` is diagonal. Its eigenvalue is:

```text
0      on V_ij,
1/2    on components sharing exactly one of i,j, and on e_i,e_j,
1      on off-diagonal V_kl disjoint from {i,j},
3/2    on diagonal e_k with k notin {i,j}.
```

Therefore `R_ij` is invertible on the complement of `V_ij` with a universal
inverse. One explicit inverse on these eigenvalues is the polynomial

```text
q(t)= (85/9)t - (40/3)t^2 + (44/9)t^3,
```

which satisfies

```text
q(1/2)=2,        q(1)=1,        q(3/2)=2/3.
```

Consequently

```text
(I-P_ij)A = q(R_ij) R_ij A,
```

where `P_ij` is the Peirce projection onto `V_ij`. Combining this identity with
(1) gives a dimension-free pointwise estimate

```text
||(I-P_ij)h(x)|| <= C ||f|| ||x||
```

for an absolute constant `C`.

Indeed, (1) bounds `M_epsilon A` uniformly. Since `||M_epsilon||<=2`,
`||R_ij A||<=24||f||||x||`; and `q(R_ij)` has a universal operator-norm bound
because it is a fixed polynomial in the operator `R_ij`, with
`||R_ij||<=4`. The value of `C` from this argument is crude but independent of
`n` and of `F`.

This is a single-source-sector estimate. It does not by itself say that the
linear map collecting all off-sector leakage from all `V_ij` has
dimension-free operator norm. That summation/globalization problem is another
place where Schur-multiplier growth can hide.

## Sector-Preserving Residual

After the diagonal gauge and the single-edge off-sector leakage estimate, the
pointwise residual is the sector-preserving edge map

```text
S_ij:V_ij -> V_ij,        S_ij x = P_ij h(x).
```

The quadratic evaluation

```text
f(x,x)=2x o h(x)-h(x o x)
```

controls the symmetric part of `S_ij` pointwise, because

```text
x o S_ij x
```

is the Peirce inner product on `V_ij` times `(e_i+e_j)/2`. For `F=R`, this
already controls each scalar edge coefficient pointwise.

Pointwise edge control is still not an operator-norm splitting. A
sector-preserving map on the real off-diagonal part is a Schur multiplier, and
bounded scalar entries do not give a dimension-free bound as an operator on
`H_n(F)` with the operator norm. The full bilinear defect

```text
x o T(y)+T(x) o y-T(x o y)
```

on products of different Peirce sectors must be used.

For `F=C,H`, the skew part of each `S_ij` is also not controlled by
`f(x,x)`. This skew part is exactly the infinitesimal action of the stabilizer
of the chosen frame on a single edge. The remaining compatibility condition is
a complete-graph connection problem: triple products

```text
V_ij x V_jk -> V_ik
```

measure the curvature.

This sector-preserving problem has now been controlled by the subsequent
Schur/matching notes:

- `agent-B/notes/real-symmetric-matching-reconstruction-theorem.md`;
- `agent-B/notes/hermitian-scalar-sector-reconstruction-corollary.md`;
- `agent-B/notes/complex-antilinear-peirce-residual-theorem.md`;
- `agent-B/notes/quaternionic-internal-peirce-residual-theorem.md`.

Thus, after formal removal of off-sector leakage, the fixed-frame
sector-preserving edge-map residual is controlled for `F=R,C,H` modulo the
diagonal frame-stabilizer derivations.

## Reduced High-Rank Target Status

A dimension-free exact-adjoint splitting for `H_n(F)` follows once the
pointwise leakage formula above is globalized in operator norm.

That globalization is now proved in
`agent-B/notes/off-sector-leakage-globalization-theorem.md`. It treats
`h|_E:E->J` as a single operator and uses the averaged squared commutator with
diagonal signs,

```text
R(T)=E_epsilon ad_epsilon^2(T),
```

whose kernel is exactly the sector-preserving maps and whose nonzero
off-sector eigenvalues are `1/2,1,3/2`. The polynomial inverse on those
eigenvalues controls the full leakage operator.

After subtracting:

1. the unit multiplication primitive from
   `agent-B/notes/unit-normalized-adjoint-reduction.md`;
2. the diagonal-frame derivation above;
3. the globally controlled off-sector leakage operator;

the sector-preserving edge operator `S=(S_ij)` is controlled by the
Schur/matching theorems listed above. The assembled matrix-factor statement is
recorded in
`agent-B/notes/matrix-factor-exact-adjoint-splitting-theorem.md`.
