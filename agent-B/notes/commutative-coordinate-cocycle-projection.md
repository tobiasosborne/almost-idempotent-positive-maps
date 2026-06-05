# Commutative Coordinate Cocycle Projection

Date: 2026-06-05.

This note proves the next-arrow estimate for one tractable Layer 1 model:
coordinate modules over `R^m`. It is a first positive test of the target

```text
dist(theta, im d^1) <= C ||d^2 theta||
```

after the exact-adjoint benchmark.

It does not cover the half-sum Peirce `1/2` modules, noncommutative factors,
or approximate module-action errors.

## Setup

Let

```text
B=R^m,        ||x||=||x||_infty,
```

with coordinatewise product. Let `M=R` be the coordinate module at `k`:

```text
x.m = x_k m.
```

Let `theta:B x B -> R` be a symmetric bilinear 2-cochain, with norm

```text
||theta|| = sup_{||x||,||y||<=1} |theta(x,y)|.
```

Write the coordinate `k` of `x` as `alpha=x_k`, and write `u` for the
remaining coordinates. Let

```text
s=e_k.
```

Define the support-unit projection from
`agent-B/notes/commutative-scalar-module-splitting.md`:

```text
(S theta)(x)=theta(x,s),        Pi theta=d^1S theta.
```

Set

```text
r=theta-Pi theta.
```

Then `Pi theta in im d^1`, so

```text
dist(theta,im d^1) <= ||r||.
```

## Residual Form

For the coordinate module,

```text
(d^1h)(x,y)=x_k h(y)+y_k h(x)-h(xy).
```

A direct calculation gives

```text
r(x,s)=0,
```

and `r` depends only on the coordinates away from `k`. Thus there is a
symmetric bilinear form `R` on `R^{m-1}` such that

```text
r(x,y)=R(u,v),
```

where `u=x|_{i != k}` and `v=y|_{i != k}`.

## Linearized Jordan Defect

For a symmetric 2-cochain `g`, define the two-variable linearized Jordan
defect

```text
Jg(a,b)
 = g(a^2,ab) + a_k^2 g(a,b) + (ab)_k g(a,a)
   - g(a^2b,a) - a_k g(a^2,b) - a_k b_k g(a,a).
```

This is exactly the coefficient of `t` in the Jordan identity defect for the
split square-zero extension with product

```text
(x,\lambda)*(y,\mu)
 = (xy, x_k mu+y_k lambda+t g(x,y)).
```

Because every coboundary has zero linearized defect,

```text
Jr=Jtheta.
```

For `a=(u,alpha)` and `b=(v,beta)`, the terms involving `beta` cancel for the
coordinate residual `r`, and the formula becomes

```text
Jr((u,alpha),(v,beta))
 = R(u^2,uv)-R(u^2v,u)
   + alpha^2 R(u,v)-alpha R(u^2,v).
```

Here products on `u,v` are coordinatewise.

## Theorem

For coordinate modules over `R^m`,

```text
dist(theta,im d^1) <= 2||Jtheta||,
```

where

```text
||Jtheta||=sup_{||a||,||b||<=1}|Jtheta(a,b)|.
```

The constant is independent of `m`.

## Proof

Since `r` is symmetric bilinear on `R^{m-1}` with the sup norm, its norm is
attained at sign vectors:

```text
||r||=sup_{sigma,tau in {+-1}^{m-1}} |R(sigma,tau)|.
```

Fix such `sigma,tau`. Put `u=sigma`, `v=tau`, and choose the support
coordinate `alpha=0`. Since `u^2` is the all-ones vector,

```text
Jr((sigma,0),(tau,0))
 = R(1,sigma tau)-R(tau,sigma).
```

Because `R` is symmetric and `sigma_i^2=1`, this is

```text
Jr((sigma,0),(tau,0))=R(1,sigma tau)-R(sigma,tau).
```

Choosing `alpha=1` gives

```text
Jr((sigma,1),(tau,0))=R(1,sigma tau)-R(1,tau).
```

Choosing instead `alpha=-1` gives

```text
Jr((sigma,-1),(tau,0))=R(1,sigma tau)+R(1,tau).
```

Averaging the `alpha=1` and `alpha=-1` identities and subtracting the
`alpha=0` identity,

```text
R(sigma,tau)
 = (1/2)Jr((sigma,1),(tau,0))
   +(1/2)Jr((sigma,-1),(tau,0))
   - Jr((sigma,0),(tau,0)).
```

The test vectors have sup norm `1`, so

```text
|R(sigma,tau)| <= 2||Jr||=2||Jtheta||.
```

Taking the supremum over sign vectors proves

```text
||r|| <= 2||Jtheta||.
```

Since `Pi theta` is an exact coboundary, this proves the theorem.

## Consequence

The coordinate sectors of the commutative `R^m` module decomposition have a
dimension-free approximate-cocycle projection estimate. The remaining
commutative scalar test is the half-sum module

```text
l(x)=(x_p+x_q)/2,
```

which is the Peirce `1/2` sector intrinsic to direct sums and matrix diagonal
frames.
