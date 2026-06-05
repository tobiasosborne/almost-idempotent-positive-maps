# Commutative Scalar Cocycle Projection Theorem

Date: 2026-06-05.

This note proves the approximate-cocycle projection estimate for all scalar
irreducible modules over `R^m`: coordinate modules and Peirce `1/2` half-sum
modules. This is the first nontrivial positive case of the Layer 1
next-arrow target after the exact-adjoint benchmark.

## Setup

Let

```text
B=R^m,        ||x||=||x||_infty,
```

with coordinatewise product. Let `M=R` be a one-dimensional unital Jordan
module. Thus either

```text
l(x)=x_k
```

or

```text
l(x)=(x_p+x_q)/2,        p != q.
```

The module action is `x.m=l(x)m`. For a symmetric scalar 2-cochain
`theta:B x B -> R`, define the support-unit splitting

```text
(S theta)(x)=theta(x,s),        Pi theta=d^1S theta,
```

where

```text
s=e_k                    in the coordinate case,
s=e_p+e_q                in the half-sum case.
```

The coboundary is

```text
(d^1h)(x,y)=l(x)h(y)+l(y)h(x)-h(xy).
```

Define the two-variable linearized Jordan defect

```text
J_theta(a,b)
 = theta(a^2,ab) + l(a^2)theta(a,b) + l(ab)theta(a,a)
   - theta(a^2b,a) - l(a)theta(a^2,b) - l(a)l(b)theta(a,a).
```

This is the coefficient of the first-order perturbation in the Jordan identity
for the split square-zero extension `B direct_sum M`.

Use norms

```text
||theta|| = sup_{||x||,||y||<=1}|theta(x,y)|,
||Jtheta|| = sup_{||a||,||b||<=1}|Jtheta(a,b)|.
```

## Theorem

For every scalar irreducible module over `R^m`,

```text
dist(theta,im d^1) <= 12 ||Jtheta||.
```

The constant is independent of `m` and of the support coordinates.

## Coordinate Module

The coordinate case is proved in
`agent-B/notes/commutative-coordinate-cocycle-projection.md`, with the sharper
constant `2`.

Briefly, for `r=theta-Pi theta`, the residual depends only on the coordinates
away from the support coordinate:

```text
r(x,y)=R(u,v).
```

For sign vectors `sigma,tau`, the three tests with support coordinate
`alpha=0,1,-1` recover

```text
R(sigma,tau)
 = (1/2)Jr((sigma,1),(tau,0))
   +(1/2)Jr((sigma,-1),(tau,0))
   - Jr((sigma,0),(tau,0)).
```

Since the bilinear norm on `l_infty` is attained at sign vectors,

```text
||theta-Pi theta|| <= 2||Jtheta||.
```

## Half-Sum Module

Assume now

```text
l(x)=(x_1+x_2)/2.
```

Write

```text
s=e_1+e_2,        u=e_1-e_2,
```

and let `x_0` denote the tail of `x` outside `{1,2}`. Put

```text
R=theta-Pi theta.
```

Since `Pi theta` is a coboundary,

```text
J_R=J_theta.
```

Direct expansion of the support-unit projection gives the residual form

```text
R(x,y)
 = A Delta_x Delta_y
   + B(x_1 y_1 - x_2 y_2)
   + Delta_x U(y_0) + Delta_y U(x_0)
   + W(x_0,y_0),
```

where

```text
Delta_x=x_1-x_2,
```

`A,B` are scalars, `U` is a linear functional on the tail, and `W` is a
symmetric bilinear form on the tail.

These coefficients are recovered from finite defect evaluations:

```text
A = (1/4)J_theta(u,u),
B = (1/2)J_theta(u,s),
U(z) = (1/2)J_theta(u,z),
```

and, for tail-supported `z`,

```text
W(z,z)
 = J_theta(u+z,u) - J_theta(u,u) - 2J_theta(u,z).
```

For general tail vectors, real polarization gives

```text
W(x_0,y_0)=Q((x_0+y_0)/2)-Q((x_0-y_0)/2),
```

where

```text
Q(z)=J_theta(u+z,u)-J_theta(u,u)-2J_theta(u,z).
```

All vectors appearing in these evaluations have sup norm at most `1` when the
tail variables do. Therefore, with `M=||Jtheta||`,

```text
|A| <= M/4,
|B| <= M/2,
||U|| <= M/2,
sup_{||z||<=1}|W(z,z)| <= 4M,
||W|| <= 8M.
```

For `||x||,||y||<=1`,

```text
|Delta_x|, |Delta_y| <= 2,
|x_1y_1-x_2y_2| <= 2.
```

Thus

```text
||R|| <= 4|A|+2|B|+4||U||+||W||
      <= 12M.
```

Since `Pi theta in im d^1`, this proves

```text
dist(theta,im d^1) <= 12||Jtheta||.
```

## Vector-Valued Max Sums

The same estimate holds for `l_infty`-max sums of scalar irreducibles with
arbitrary Banach multiplicity spaces:

```text
M = direct_sum_alpha^infty E_alpha.
```

Apply the scalar theorem after pairing each `E_alpha` with an arbitrary
norm-one functional in `E_alpha^*`, and use the support-unit projection
coordinatewise. The constant remains `12`.

For an arbitrary module norm, the estimate is multiplied by the same sector
decomposition complementability constant `K_dec` used in
`agent-B/notes/commutative-scalar-module-splitting.md`.

## Consequence

For exact commutative modules over `R^m` whose sector decomposition is
uniformly complemented, approximate scalar Jordan 2-cocycles are
dimension-free close to exact coboundaries. This closes the commutative scalar
next-arrow test, including the intrinsic Peirce `1/2` mixed modules.

The remaining Layer 1 next-arrow problem is therefore noncommutative:
matrix/spin/internal modules and robustness under approximate module actions.
