# Spin Normalized Cocycle Projection Theorem

Date: 2026-06-05.

This note proves the normalized spin-factor next-arrow estimate. It is the
first noncommutative positive case of the Layer 1 approximate-cocycle
projection target.

## Setup

Let

```text
V=R1 direct_sum H
```

be a real spin factor with product

```text
(alpha 1+x)(beta 1+y)
 = (alpha beta+<x,y>)1 + alpha y + beta x.
```

Use the Euclidean-injective cochain norms. The order-unit norms are uniformly
equivalent to these norms in spin factors, as recorded in
`agent-B/notes/adjoint-spin-splitting-theorem.md`.

In the unital error-reduction setting, the first-order product perturbation is
normalized:

```text
theta(1,z)=0.
```

Thus for `x,y in H` write

```text
theta(x,y)=c(x,y)1 + D(x,y),
```

where `c` is a symmetric scalar bilinear form and
`D:H x H -> H` is symmetric bilinear.

## Scalar Part

The scalar part is always an exact coboundary. If `A=A^*` is defined by

```text
2<x,Ay>=c(x,y),
```

then the 1-cochain

```text
h_A(1)=0,        h_A(x)=Ax
```

satisfies

```text
(d^1h_A)(x,y)=c(x,y)1.
```

Moreover `||A|| <= (1/2)||c||`, so this correction is dimension-free.

The normalized spin next-arrow problem is therefore entirely in the vector
part `D`.

## Vector Coboundary Subspace

For `u in H`, let

```text
h_u(1)=0,        h_u(x)=<u,x>1.
```

Then

```text
(d^1h_u)(x,y)=<u,y>x+<u,x>y.
```

Thus the vector coboundary subspace is

```text
D_u(x,y)=<u,y>x+<u,x>y.
```

The normalized vector projection target is:

```text
inf_u ||D-D_u||_inj <= C ||J_D||.
```

## Linearized Jordan Defect

Use the two-variable linearized Jordan identity from Agent A's cochain setup.
For pure vectors `a,b in H`, using

```text
a^2=||a||^2 1,        a b=<a,b>1,
```

and `theta(1,.)=0`, the scalar part drops out and the vector part gives

```text
J_D(a,b)
 = <a,b>D(a,a) - <b,D(a,a)>a.
```

Indeed the terms

```text
theta(a^2,ab),
theta(a^2b,a),
L_{a^2}theta(a,b),
L_a theta(a^2,b)
```

either vanish by normalization or cancel, while

```text
L_{ab}theta(a,a)=<a,b>D(a,a),
L_aL_b theta(a,a)=<b,D(a,a)>a.
```

For `||a||=1`, taking the supremum over `||b||<=1` gives

```text
sup_{||b||<=1} ||J_D(a,b)||
 = ||P_{a^\perp}D(a,a)||.
```

Therefore

```text
||J_D|| = sup_{||a||=1} ||P_{a^\perp}D(a,a)||.
```

## Hilbert-Space Stability Lemma

The normalized spin next-arrow estimate now follows from the following
dimension-free lemma.

Let `D:H x H -> H` be symmetric bilinear and set `Q(x)=D(x,x)`. Does there
Then there exists `u in H` such that

```text
||D-D_u||_inj
 <= (2 sqrt(2)+2) sup_{||x||=1} ||P_{x^\perp}Q(x)||.
```

### Proof

Let

```text
T=sup_{||x||=1} ||P_{x^\perp}Q(x)||.
```

The case `dim H=1` is exact, since every symmetric bilinear `D` is of the
form `D_u`. Assume `dim H>=2`.

For unit `x`, define

```text
phi(x)=<Q(x),x>.
```

Let `x,y` be orthonormal. Put

```text
a=<D(x,y),x>,        b=<D(x,y),y>,
q_xy=<Q(x),y>,       q_yx=<Q(y),x>.
```

The bound defining `T` gives `|q_xy|,|q_yx|<=T`. Since

```text
(x+y)/sqrt(2)        and        (x-y)/sqrt(2)
```

are orthonormal, the same bound applied to these two unit vectors gives

```text
|<Q((x+y)/sqrt(2)),(x-y)/sqrt(2)>| <= T,
|<Q((x-y)/sqrt(2)),(x+y)/sqrt(2)>| <= T.
```

Expanding these two inequalities and adding/subtracting gives

```text
|2b-phi(x)| <= (2 sqrt(2)+1)T,
|2a-phi(y)| <= (2 sqrt(2)+1)T.
```

Therefore, for every unit `x` and every unit `y perpendicular x`,

```text
|<D(x,y),y>-phi(x)/2| <= (sqrt(2)+1/2)T.
```

Define the trace functional

```text
c(x)=Tr(y -> D(x,y)).
```

This is linear in `x`. Choose an orthonormal basis

```text
e_1=x,        e_2,...,e_n perpendicular x.
```

Then

```text
c(x)=phi(x)+sum_{i=2}^n <D(x,e_i),e_i>
    = ((n+1)/2)phi(x)+err_x,
```

with

```text
|err_x| <= (n-1)(sqrt(2)+1/2)T.
```

Let `u in H` be the Riesz vector for the linear functional `c/(n+1)`:

```text
<u,x>=c(x)/(n+1).
```

Then, for every unit `x`,

```text
|phi(x)-2<u,x>| <= (2 sqrt(2)+1)T.
```

Consequently

```text
||Q(x)-2<u,x>x||
 <= |phi(x)-2<u,x>| + ||P_{x^\perp}Q(x)||
 <= (2 sqrt(2)+2)T.
```

For `E=D-D_u`, this says

```text
||E(x,x)|| <= (2 sqrt(2)+2)T ||x||^2
```

for all `x`, by homogeneity. Polarization gives, for unit `x,y`,

```text
E(x,y)=1/4(E(x+y,x+y)-E(x-y,x-y)).
```

Since

```text
||x+y||^2+||x-y||^2=4,
```

we get

```text
||E(x,y)|| <= (2 sqrt(2)+2)T.
```

This proves the lemma.

## Theorem

For every normalized spin adjoint 2-cochain `theta` with `theta(1,z)=0`,

```text
dist(theta,im d^1) <= (2 sqrt(2)+2)||Jtheta||.
```

The constant is in Euclidean-injective cochain norm; in order-unit spin norm
it changes only by the fixed spin norm-comparison constant.

## Proof

The scalar part is an exact coboundary by the scalar correction above. For the
vector part, the linearized defect formula gives

```text
||J_D||=sup_{||a||=1}||P_{a^\perp}D(a,a)||.
```

The Hilbert-space lemma produces `u` with

```text
||D-D_u|| <= (2 sqrt(2)+2)||J_D||.
```

Since `D_u=d^1h_u`, this proves the displayed distance estimate.

## Consequence

Normalized spin-factor approximate 2-cocycles are dimension-free close to
exact coboundaries:

```text
dist(theta,im d^1) <= C ||Jtheta||.
```

Thus spin factors are not a next-arrow obstruction in the normalized adjoint
sector. Remaining noncommutative next-arrow work lies in non-spin matrix and
internal Peirce configurations, and in robustness under approximate module
actions.
