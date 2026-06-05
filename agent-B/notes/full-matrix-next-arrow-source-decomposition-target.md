# Full Matrix Next-Arrow Source Decomposition Target

Date: 2026-06-05.

This note records the next target after
`agent-B/notes/diagonal-frame-matrix-next-arrow-walsh-target.md`. The fixed
diagonal-frame module controls 2-cochains restricted to `D x D`. The full
matrix adjoint next-arrow problem must also control cochains with off-diagonal
source arguments.

## Setup

Let

```text
J=H_n(F),        F in {R,C,H},
```

with a fixed diagonal Jordan frame. Write

```text
D=span{e_i},        E=direct_sum_{i<j} V_ij,
J=D direct_sum E.
```

For an adjoint 2-cochain

```text
theta:J x J -> J,
```

decompose the source variables as

```text
theta_DD = theta|_{D x D},
theta_DE = theta|_{D x E},
theta_EE = theta|_{E x E}.
```

The diagonal-frame Walsh theorem controls `theta_DD`:

```text
dist(theta_DD, im d^1_D) <= C||Jtheta|_{D,D}||.
```

This is a local commutative result. It does not control `theta_DE` or
`theta_EE`, and it does not solve compatibility across different frames.

## Why The Exact-Adjoint Proof Suggests This Decomposition

For an exact primitive `h` with `f=d^1h`, the fixed-frame exact-adjoint proof
used the same source split.

1. `D x D` fixed the diagonal gauge.
2. `D x E` gave the diagonal commutator equation

   ```text
   [L_a,h|_E]x = f(a,x)-h(a)o x,
   ```

   which controlled off-sector leakage by diagonal-sign spectral gaps.
3. `E x E` controlled the sector-preserving edge maps through Peirce products
   `V_ij x V_jk -> V_ik` and `V_ij x V_ij -> D`.

The approximate-cocycle next-arrow problem should be attacked in the same
order, but the objects are 2-cochains rather than primitives. Exact
coboundary inversion cannot be reused directly.

## Target 1: One Diagonal And One Off-Diagonal Source

After subtracting a controlled coboundary for `theta_DD`, the next local
problem is to control

```text
theta_DE(a,x),        a in D, x in E.
```

The expected mechanism is a cochain-level diagonal-sign spectral gap. In the
exact primitive proof, the operator

```text
R(T)=E_epsilon ad_epsilon^2(T)
```

had kernel equal to sector-preserving maps and spectrum

```text
1/2, 1, 3/2
```

on leakage maps. The next-arrow analogue should produce, from `Jtheta` with
one or two diagonal test variables, an operator-valued residual whose
off-sector part is inverted by the same polynomial

```text
q(t)=85/9 t - 40/3 t^2 + 44/9 t^3.
```

The technical requirement is a bounded projection formula for the
`D x E` residual, not merely pointwise control on each source edge `V_ij`.

## Target 2: Two Off-Diagonal Sources

The remaining source block is

```text
theta_EE(x,y),        x,y in E.
```

Here the exact-adjoint proof used the full Peirce multiplication table:

```text
V_ij o V_ij -> D,
V_ij o V_jk -> V_ik,
V_ij o V_kl = 0        for disjoint edges.
```

The next-arrow analogue must detect approximate sector-preserving curvature
directly at the 2-cochain level. The expected stress families are again
Schur-multiplier and connection-type tensors, but now one degree higher than
the exact primitive residuals.

Concrete subtargets:

```text
E x E -> D        square/diagonal components,
V_ij x V_jk -> V_ik        triangle components,
V_ij x V_kl -> J        disjoint-edge leakage.
```

The exact matching-reconstruction theorems suggest that triangle and matching
tests should be used in operator norm; pointwise coefficient curvature will
not be enough.

## What Would Close The Matrix Next-Arrow

A full fixed-frame matrix next-arrow theorem would provide a projection

```text
Pi_2:C^2(J,J)->im d^1
```

or an equivalent distance estimate

```text
dist(theta,im d^1) <= C||Jtheta||
```

for all adjoint 2-cochains on `H_n(F)`, uniformly in `n` and `F`.

The current known pieces are:

```text
D x D source block: closed by diagonal-frame Walsh theorem.
D x E source block: open cochain-level leakage target.
E x E source block: open Peirce curvature/matching target.
```

Naive averaging over all frames remains unavailable because random diagonal
pinching reconstructs traceless data with a rank-sized loss, as recorded in
`agent-B/notes/frame-covariance-and-global-matrix-obstacle.md`.
