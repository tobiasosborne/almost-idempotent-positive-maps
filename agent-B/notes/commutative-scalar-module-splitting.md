# Commutative Scalar Module Splitting

Date: 2026-06-04.

This note refines the direct-sum caveat in
`agent-B/notes/response-to-agent-a-v0.12-layer1-caveat.md`.

The caveat was real: direct sums are not automatically block diagonal for
arbitrary modules, because even `R^m` has mixed Peirce-`1/2` scalar modules.
However, those scalar mixed modules are not themselves an obstruction. For
one-dimensional modules over `R^m`, the exact coboundary has a norm-one right
inverse in the max/injective norm.

Thus the direct-sum obstruction is sharper than "mixed components exist": the
central scalar mixed components are controllable. The remaining danger is in
higher-dimensional/internal mixed Peirce modules and in how the module norm
decomposes.

## Setup

Let

```text
B = R^m,        (xy)_i=x_i y_i,        ||x||_infty=max_i |x_i|.
```

Let `M=R m_0` be a one-dimensional unital Jordan `B`-module with action

```text
x . m_0 = l(x)m_0,        l(1)=1.
```

Use the scalar norm on `M`, and cochain norms

```text
||h|| = sup_{||x||_infty<=1} |h(x)|,
||f|| = sup_{||x||_infty,||y||_infty<=1} |f(x,y)|.
```

The coboundary convention is

```text
(d^1 h)(x,y) = l(x)h(y) + l(y)h(x) - h(xy).
```

As recorded in the v0.12 caveat, the one-dimensional unital Jordan modules are
exactly:

1. coordinate evaluations `l(x)=x_k`;
2. half-sums of two coordinates `l(x)=(x_p+x_q)/2`, `p!=q`.

The second case is the Peirce-`1/2` mixed module for the diagonal
`R e_p \oplus R e_q` inside `H_2(R)`.

For completeness, here is the scalar classification argument. Write

```text
l(x)=sum_i p_i x_i,        sum_i p_i=1.
```

The scalar specialization of the Jordan module identity gives, for every
support coordinate `j` with `p_j != 0`,

```text
x_j^2 - 2 x_j l(x) + 2 l(x)^2 - sum_i p_i x_i^2 = 0
```

as a polynomial identity in `x`. Subtracting the identities for two support
coordinates `j,k` gives

```text
(x_j-x_k)(x_j+x_k-2l(x))=0.
```

Since this is an identity in the polynomial ring, the second factor must vanish.
Thus `l(x)=(x_j+x_k)/2` whenever two support coordinates occur. A third support
coordinate would give a contradictory formula, so the support has size at most
two. The one-point case is a coordinate evaluation, and the two-point case is a
half-sum.

## Theorem

For every one-dimensional unital Jordan `R^m`-module above, there is a linear
right inverse

```text
S_l : im(d^1) -> C^1(B,M)
```

with

```text
d^1 S_l f = f,
||S_l f|| <= ||f||.
```

The constant is independent of `m` and independent of the support coordinates.

## Proof

### Coordinate Evaluation

Suppose `l(x)=x_k`. Let

```text
s=e_k.
```

For `f=d^1 h`, define

```text
(S_l f)(x) = f(x,s).
```

Since `l(s)=1` and `xs=x_k e_k`,

```text
f(x,s)
 = l(x)h(s)+l(s)h(x)-h(xs)
 = x_k h(e_k)+h(x)-h(x_k e_k)
 = h(x).
```

Thus `S_l d^1 h=h`, so `d^1 S_l f=f` on `im(d^1)`. Also `||s||_infty=1`, hence

```text
||S_l f|| <= ||f||.
```

### Half-Sum Module

Suppose `l(x)=(x_p+x_q)/2`, `p!=q`. Let

```text
s=e_p+e_q.
```

Again define

```text
(S_l f)(x) = f(x,s),        f in im(d^1).
```

Write an arbitrary 1-cochain as

```text
h(x)=sum_i t_i x_i.
```

Then

```text
f(x,s)
 = l(x)h(s)+h(x)-h(xs).
```

Here

```text
h(s)=t_p+t_q,
h(xs)=t_p x_p+t_q x_q,
l(x)h(s)=((x_p+x_q)/2)(t_p+t_q).
```

Therefore

```text
f(x,s)
 = sum_{i notin {p,q}} t_i x_i
   + ((t_p+t_q)/2)(x_p+x_q).
```

This is exactly the canonical representative obtained from `h` by replacing
`t_p,t_q` with their average and leaving all other coefficients unchanged.
The discarded antisymmetric part

```text
x -> (t_p-t_q)(x_p-x_q)/2
```

lies in `ker d^1`: it is the infinitesimal movement inside the Peirce pair.
Thus `d^1(S_l f)=f`.

The norm bound is again immediate from `||s||_infty=1`:

```text
||S_l f|| = sup_{||x||_infty<=1} |f(x,s)| <= ||f||.
```

This proves the theorem.

## Consequences

1. The minimal mixed module from `R \oplus R` is not a dimension-growth
   obstruction. It has an explicit norm-one right inverse.
2. If a finite-dimensional `R^m`-module is presented as an `l_infty`-direct sum
   of these one-dimensional modules, the coordinatewise splitting has the same
   norm-one bound.
3. This does not prove Agent A's broad direct-sum reduction. For arbitrary
   Jordan modules and arbitrary module norms, one still has to control:
   higher-dimensional mixed Peirce modules, projections onto the scalar
   summands, approximate-module errors, and compatibility with noncommutative
   simple summands.
4. The useful correction to the direct-sum status is:

```text
Mixed Peirce-1/2 scalar modules exist, so block diagonalization is false as
stated; but in the commutative scalar case they are uniformly controllable by
the support-unit formula S f(x)=f(x,s).
```

## Vector-Valued Multiplicities

The same proof handles arbitrary multiplicities of the scalar irreducibles,
provided the module norm is the max sum over the irreducible support types.

Let `A` be a finite index set. For each `alpha in A`, let `E_alpha` be a
Banach space and let `l_alpha` be either a coordinate evaluation or a half-sum
functional as above. Put

```text
M = direct_sum_{alpha in A}^{l_infty} E_alpha,
||m|| = sup_alpha ||m_alpha||,
x.m = (l_alpha(x)m_alpha)_alpha.
```

For each `alpha`, let `s_alpha` be the corresponding support unit:

```text
s_alpha=e_k                    if l_alpha(x)=x_k,
s_alpha=e_p+e_q                if l_alpha(x)=(x_p+x_q)/2.
```

Define, for `f in im(d^1)`,

```text
(S f)(x)_alpha = f(x,s_alpha)_alpha.
```

Then

```text
d^1 S f = f,
||S f|| <= ||f||.
```

Indeed, the scalar proof applies in each coordinate `E_alpha` after pairing
with an arbitrary norm-one functional on `E_alpha^*`. The max norm gives

```text
||(S f)(x)|| = sup_alpha ||f(x,s_alpha)_alpha||
             <= ||f|| ||x||_infty
```

because every `s_alpha` has `||s_alpha||_infty=1`.

This removes multiplicity and number-of-summands growth for the purely scalar
commutative module sector. What remains outside this theorem is any module norm
not presented as a contractive max sum of these sectors, and noncommutative
Peirce modules where the summand action is not scalar.

## Algebraic Decomposition Of Exact `R^m`-Modules

The scalar-sector hypothesis above is not an extra algebraic restriction. Every
exact unital finite-dimensional Jordan module over `R^m` decomposes
algebraically into these sectors.

Let `T_i` denote the action of the idempotent `e_i` on a finite-dimensional
module `M`.

The split null extension `B \oplus M`, with `M^2=0`, must satisfy the Jordan
identity. Linearizing the Jordan identity with one `M`-entry gives the standard
operator identity

```text
L_{a^2 b} + 2 L_a L_b L_a = L_{a^2} L_b + 2 L_{ab} L_a.        (JMod)
```

Here `L_a` denotes the action operator on `M`. Also, applying the identity with
one module entry in the second argument gives

```text
[L_a,L_{a^2}]=0        for all a in B.
```

For `a=e_i`, `b=e_i`, (JMod) gives

```text
2 T_i^3 - 3 T_i^2 + T_i = 0,
```

so

```text
T_i(T_i-1)(2T_i-1)=0.
```

The roots are distinct, hence each `T_i` is diagonalizable with spectrum in
`{0,1/2,1}`.

Next, `[L_a,L_{a^2}]=0` for all `a=sum_i a_i e_i` implies the `T_i` commute:
the coefficient of `a_i a_j^2` in

```text
[sum_i a_i T_i, sum_j a_j^2 T_j]
```

is `[T_i,T_j]`. Thus the `T_i` are simultaneously diagonalizable.

For `i != j`, putting `a=e_i`, `b=e_j` in (JMod) gives

```text
2 T_i T_j T_i = T_i T_j.
```

On a joint eigenvector with eigenvalues `lambda_i`, this gives

```text
lambda_i lambda_j (2 lambda_i-1)=0.
```

Swapping `i,j` gives the same condition with `lambda_j`. Since the module is
unital,

```text
sum_i lambda_i = 1.
```

Therefore every joint eigenspace has one of exactly two types:

```text
lambda_k=1, all other lambda_i=0,
```

or

```text
lambda_p=lambda_q=1/2, all other lambda_i=0.
```

Consequently

```text
M = (direct_sum_i M_i) direct_sum (direct_sum_{p<q} M_{pq}),
```

where `R^m` acts on `M_i` by `x_i` and on `M_{pq}` by `(x_p+x_q)/2`.

This proves that the support-unit splitting above covers every exact
finite-dimensional commutative module algebraically.

## Norm Form Of The General Commutative Statement

Let `P_alpha` be the algebraic projections onto the sectors

```text
M_i,        M_{pq}.
```

For an arbitrary Banach norm on `M`, define the decomposition constant

```text
K_dec =
  || direct_sum_alpha P_alpha : M -> direct_sum_alpha^infty P_alpha M ||
  * || sum_alpha : direct_sum_alpha^infty P_alpha M -> M ||.
```

The support-unit formula

```text
(S f)(x) = sum_alpha P_alpha f(x,s_alpha)
```

then gives

```text
d^1 S f = f,
||S f|| <= K_dec ||f||.
```

Thus the exact commutative-module right inverse is dimension-free precisely
when the sector decomposition is uniformly complemented in the module norm. In
the max direct-sum norm, `K_dec=1`. Without such norm control, purely algebraic
semisimplicity does not by itself give the order-unit estimate needed for
Layer 1.

## Projection Corollary

The support-unit formula is defined on all 2-cochains. In the max sector norm,
the module action is contractive:

```text
||x.m|| <= ||x||_infty ||m||.
```

Hence

```text
||d^1 h|| <= 3||h||.
```

For

```text
Pi=d^1 S:C^2(B,M)->C^2(B,M)
```

we get

```text
Pi^2=Pi,        ran(Pi)=im(d^1),        ||Pi||<=3
```

in the max sector norm. With an arbitrary norm and decomposition constant
`K_dec`, the same argument gives

```text
||Pi|| <= 3 K_dec.
```

As in the diagonal-frame case, this is a projection onto exact coboundaries.
The corresponding approximate-cocycle estimate for the scalar irreducible
sectors is proved in
`agent-B/notes/commutative-scalar-cocycle-projection-theorem.md`.
