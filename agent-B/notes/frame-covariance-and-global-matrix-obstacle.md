# Frame Covariance And The Global Matrix Obstacle

Date: 2026-06-04.

This note follows `agent-B/notes/diagonal-frame-matrix-module-splitting.md`.
The fixed diagonal-frame splitting is not an artifact of the standard basis:
it transports to every Jordan frame with the same constants. However, this
does not yet solve the full `H_n(F)` cochain problem. The obstruction is not
frame covariance; it is the loss incurred when one tries to reconstruct a
global noncommutative cochain from diagonal-frame restrictions.

## Setup

Let

```text
J = H_n(F),        F in {R,C,H},
M = J
```

with the adjoint Jordan module structure and the order-unit/operator norm.
Let `B_0` be the standard diagonal algebra. For a Jordan frame
`E=(p_1,...,p_n)`, write

```text
B_E = span_R{p_1,...,p_n}.
```

Every such `B_E` is the image of `B_0` under an isometric Jordan automorphism
`alpha` of `J`. The norm on `B_E` is the spectral max norm, transported from
`l_infty^n`.

For a 1-cochain `h:B_E->M` and a 2-cochain `f:B_E x B_E->M`, use

```text
(d_E^1 h)(x,y)=x o h(y)+y o h(x)-h(xy).
```

## Frame-Covariance Theorem

For every Jordan frame `E`, there is a linear right inverse

```text
S_E : im(d_E^1) -> C^1(B_E,M)
```

such that

```text
d_E^1 S_E f = f,
||S_E f|| <= 11 ||f||.
```

The constant is independent of `n`, `F`, and the frame.

Moreover, the corresponding projection

```text
Pi_E=d_E^1 S_E
```

onto `im(d_E^1)` satisfies

```text
||Pi_E|| <= 33.
```

## Proof

Choose an isometric Jordan automorphism `alpha:J->J` with
`alpha(B_0)=B_E`. For a 2-cochain `f` on `B_E`, define its pullback to `B_0`
by

```text
(alpha^# f)(x,y)=alpha^{-1} f(alpha x, alpha y).
```

For a 1-cochain `h`, define `alpha^# h` analogously. Because `alpha` is a
Jordan automorphism and an order-unit isometry,

```text
||alpha^# f||=||f||,
alpha^#(d_E^1 h)=d_0^1(alpha^# h).
```

Write `alpha_*` for the inverse operation on cochains, i.e. push-forward by
`alpha`.

Let `S_0` be the fixed diagonal-frame splitting from
`diagonal-frame-matrix-module-splitting.md`, and set

```text
(S_E f)(alpha x)=alpha( S_0(alpha^# f)(x) ),        x in B_0.
```

Then

```text
d_E^1 S_E f
 = alpha_* d_0^1 S_0 alpha^# f
 = alpha_* alpha^# f
 = f
```

for `f in im(d_E^1)`, and

```text
||S_E f||=||S_0(alpha^# f)|| <= 11||alpha^# f||=11||f||.
```

The projection estimate follows exactly as in the fixed-frame case, since
`||d_E^1 h||<=3||h||` for the contractive adjoint action.

This proves frame covariance.

The construction is also independent of the obvious frame normalizer choices:
permuting the diagonal coordinates or conjugating by diagonal unitary entries
commutes with diagonal pinching and with the Rademacher formula, since real
sign matrices `D_epsilon` are carried to real sign matrices and the
Rademacher measure is invariant.

## What This Does Not Prove

The theorem gives uniform control of

```text
f | (B_E x B_E)
```

for each fixed frame `E`. A full matrix cochain is a bilinear map on

```text
J x J,
```

including noncommuting pairs. Framewise control does not automatically glue to
a linear global right inverse

```text
S:C^2(J,J)->C^1(J,J)
```

for three reasons.

1. A generic pair `(a,b)` is not contained in one associative diagonal frame.
   Simultaneous diagonalization only applies to commuting pairs.
2. Choosing a frame for a single element is nonlinear and nonunique when
   eigenvalues collide. Therefore defining `(Sf)(a)` from an arbitrary frame
   containing `a` does not give a linear map in `a`.
3. Even for exact coboundaries, each frame splitting recovers a canonical
   primitive only modulo the framewise kernel of `d^1`. These derivation/gauge
   choices must be compatible across overlapping frames; the fixed-frame
   theorem gives no such compatibility.

Thus the remaining `H_n(F)` Layer-1 problem is not Peirce-sector inversion
inside a chosen frame. It is a genuinely noncommutative compatibility and
order-norm problem.

## Naive Frame Averaging Loses Rank

There is an especially tempting globalization attempt: compress an element to
random frames, apply the frame-local construction, and average back. The
linear reconstruction step already has a rank-sized loss.

Let `E_0:J->B_0` be the trace-preserving diagonal pinching and let `G=Aut(J)`.
Define

```text
A(z)=int_G alpha E_0 alpha^{-1}(z) d alpha.
```

This is an `Aut(J)`-equivariant contraction. Decompose

```text
J = R1 \oplus J_0,
J_0={z: tr(z)=0}.
```

On `R1`, `A` is the identity. On `J_0`, irreducibility gives

```text
A|J_0 = lambda I.
```

Taking the trace of this operator on `J_0` computes `lambda`:

```text
lambda
 = dim(B_0 cap J_0) / dim(J_0)
 = (n-1)/(dim_R H_n(F)-1).
```

Consequently,

```text
lambda =
  2/(n+2)       for F=R,
  1/(n+1)       for F=C,
  1/(2n+1)      for F=H.
```

Recovering the traceless part of an element from this averaged diagonal
compression therefore requires amplification by `1/lambda`, which is linear in
the rank.

This does not rule out a more subtle global cochain homotopy. It does rule out
the straightforward "average the fixed-frame splitting over all frames and
reconstruct by random diagonal pinching" strategy as a dimension-free proof.
For example, applying such a pinching-average reconstruction to the exact
coboundary `d^1(id_J)` would return the 1-cochain

```text
z -> tr(z)1/n + lambda (z-tr(z)1/n)
```

rather than `id_J` modulo a derivation, so `d^1` is not recovered unless one
amplifies the traceless part by `1/lambda`.

## Conclusion

The fixed-frame Rademacher formula is a genuine local building block and is
fully frame-covariant. The next matrix-family target must be stronger:

```text
construct a dimension-free order-norm homotopy for the full noncommutative
Jordan cochain complex of H_n(F), or find an incremental construction that
never reconstructs global traceless information from random diagonal frames.
```

The rank-sized factor above is the concrete warning sign for global averaging
routes.
