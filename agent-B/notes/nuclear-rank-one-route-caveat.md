# Nuclear Rank-One Route Caveat

Date: 2026-06-05.

This note explains the exact limitation of
`agent-B/notes/trace-zero-rank-one-matrix-primitive-estimate.md`. Rank-one
primitive maps are uniformly controlled, but extending this by decomposing an
arbitrary primitive into rank-one maps gives a nuclear/projective norm bound,
not the operator-norm bound needed for Layer 1.

## Setup

Let `J=H_n(F)`, `F in {R,C,H}`, and let `J_0={x:tr(x)=0}`. Consider
normalized rank-one primitives

```text
h(x)=phi(x)c,        phi(1)=0.
```

The rank-one estimate gives

```text
||h|| <= 2||d^1h||
```

on these primitive lines.

Now let a normalized primitive `T:J->J` be written as a finite sum

```text
T(x)=sum_alpha phi_alpha(x)c_alpha,        phi_alpha(1)=0.
```

The triangle inequality and the rank-one estimate only give a bound controlled
by the projective/nuclear size of this representation:

```text
||T|| <= sum_alpha ||phi_alpha||_* ||c_alpha||,
```

and similarly any attempt to invert `d^1T` term-by-term pays this sum.

Thus the rank-one result would imply a dimension-free full splitting only if
one could decompose the relevant primitives with nuclear norm uniformly
controlled by their operator norm. That assertion is false in high dimension.

## Identity On The Traceless Part Has Large Nuclear Norm

Equip `J_0` with the operator norm. The identity map

```text
Id_{J_0}:J_0->J_0
```

has operator norm `1`, but its nuclear norm grows at least linearly in
`dim J_0`.

Indeed, for any finite-dimensional Banach space `E`, the nuclear norm of
`Id_E` is at least `dim E`. This follows by duality with bounded operators:

```text
nu(Id_E)
 = sup { |tr(A)| : A in L(E), ||A||_{op->op}<=1 }.
```

Taking `A=Id_E` gives

```text
nu(Id_E) >= tr(Id_E)=dim E.
```

Applying this to `E=J_0`,

```text
nu(Id_{J_0}) >= dim J_0,
```

while

```text
||Id_{J_0}||_{op->op}=1.
```

For `H_n(F)`, `dim J_0` grows like `n^2` over `R` for `F=C,H` and like
`n^2/2` for `F=R`.

## Consequences

1. The rank-one primitive estimate is a real local control statement, but it
   cannot be summed naively over a nuclear decomposition to prove the desired
   dimension-free matrix splitting.
2. The remaining high-rank matrix problem is an operator-space/Banach-geometry
   question about coherent endomorphisms, not a pointwise rank-one question.
3. A successful proof must either:

```text
avoid rank-one nuclear decompositions, or
show that exact coboundary data imposes additional cancellation beyond
ordinary operator-norm control.
```

This caveat is consistent with the earlier frame-averaging rank loss: both
failures come from trying to reconstruct a global operator from many locally
controlled pieces while paying an additive/projective norm.
