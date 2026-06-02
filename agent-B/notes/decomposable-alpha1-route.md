# Decomposable `O(eta)` Route

Agent A v0.4 and Agent B agree that arbitrary unital positive maps should not
be claimed to have a Kitaev-strength `O(eta)` bridge without extra structure.
The natural extra structure is decomposability, because it provides CP/coCP
dilation data.

This note records what is plausible and what is not yet proved.

## Correct Hypothesis

Do not state the theorem as

```text
||Phi||_dec = 1
```

for the standard Haagerup/Wittstock decomposable norm. That statement is false
for unital positive decomposable maps: the transpose on `M_n` has standard
decomposable norm `n`.

The useful hypothesis is an explicit CP+coCP decomposition

```text
Phi = Phi_0 + Psi_0 o tau,
```

where `Phi_0,Psi_0` are completely positive and `tau` is a transpose or
anti-automorphic leg. If `Phi` is unital, then

```text
Phi_0(1)+Psi_0(1)=1,
```

so

```text
||Phi_0||_cb <= 1,     ||Psi_0||_cb <= 1.
```

This is the correct boundedness input for a dimension-free estimate.

## Desired Statement

Let `Phi:B(H)_sa -> B(H)_sa` be unital positive, decomposable with a
decomposition as above, and

```text
||Phi^2-Phi|| <= eta.
```

For `P=theta(2Phi-I)` and `A=Im P`, define

```text
a*b=P(a o b).
```

Conjectural bridge:

```text
A is an O(eta)-JB order-unit algebra.
```

The exact UP factorization still additionally needs the positivity mechanism
discussed in `factorization-positivity-rounding.md`; this note concerns only
the algebraic bridge exponent.

## Plausible Mechanism

For CP maps, Kitaev's `O(eta)` associativity estimate is not obtained by
peeling off one spectral idempotent at a time. The one-hole estimate is only
`O(sqrt(eta))`; the final defect is `O(eta)` because it is a product/pairing of
two dilation-space holes.

A decomposable map should allow a similar argument by passing to a CP map on a
universal doubled algebra. Informally:

- the CP part has a Stinespring dilation;
- the coCP part has a Stinespring dilation after applying the transpose/opposite
  algebra;
- Jordan products are symmetrized, so the transpose reverses order but should
  not change the size of the two-hole term;
- the CP component bounds above prevent dimension-dependent constants.

## Main Technical Obstacle

`Phi` itself is not CP, and its spectral idempotent `P=theta(2Phi-I)` is formed
after summing the CP and coCP pieces. It is not enough to run Kitaev separately
on `Phi_0` and `Psi_0 o tau`; neither summand is unital nor almost idempotent.

A proof must either:

1. construct a single CP dilation of the decomposable map as a Jordan-positive
   map on a doubled/universal enveloping algebra and show the almost-idempotence
   defect of `Phi` controls the relevant dilation holes; or
2. expand the Jordan identity defect directly and prove that the single-hole
   `O(sqrt(eta))` terms cancel or pair into CP/coCP two-hole terms.

The first route is cleaner but requires the correct universal-envelope
formalism for decomposable maps. The second route is more concrete but risks
losing the cancellation that Kitaev obtains from Stinespring bookkeeping.

Update 2026-06-02: the naive doubled route has a concrete obstruction. Even
when one has a putative doubled factorization `Phi=Cj`, it does **not** follow
that the lifted map `F=jC` is almost idempotent. In fact,

```text
F^2-F = j((Phi-I)C),
```

and `||Phi^2-Phi||` controls `(Phi-I)` only on inputs of the form `Phi(x)`, not
on all of `C(D)`. A commutative stochastic example in the exact doubled form
has `Cj` exactly idempotent but `||jCjC-jC||=1`. See
`agent-B/notes/decomposable-doubling-obstruction.md`.

Therefore route (1) needs an additional dilation-compatible hypothesis or a
new argument showing `C(D)` is close to the approximate fixed space of `Phi`.
The decomposable `O(eta)` theorem remains conjectural.

There is, however, a clean conditional theorem: if a dilation-compatible model
exists in which `F=jC` is UCP and is itself almost idempotent,

```text
||jCjC-jC||_cb <= eta,
```

then Kitaev's UCP theorem applies to `jC`, and its symmetrized product
restricts along the Jordan embedding `j` to the desired product `P(a o b)` on
`Im theta(2Phi-I)`. This gives an `O(eta)` algebraic bridge under the stronger
dilation-compatible hypothesis. This hypothesis is not automatic for a general
CP+coCP decomposition. See
`agent-B/notes/decomposable-dilation-compatible-theorem.md`.

Sartre sidecar sharpened the same point for arbitrary supplied decompositions:
even if `Phi` is an exact positive projection, a bad CP+coCP decomposition can
have large off-diagonal universal-envelope defect. In `M_2`, writing the
depolarizing projection `D` as

```text
Phi_0 = eps R,
Psi_0 = D - eps R,
Phi = Phi_0 + Psi_0 o tau = D,
```

with `0<eps<=1/2`, the original map has `eta=0`, but the natural universal
extension `F` satisfies

```text
||Phi F - F|| >= eps/2
```

on an off-diagonal doubled input. See
`agent-B/notes/subagent-decomposable-alpha1-stress.md`. Thus any theorem using
the supplied decomposition must either choose a compatible decomposition or
prove cancellation of off-diagonal terms rather than bounding them separately.

## What Would Count As A Proof

A satisfactory proof should produce, for each state `rho`, dilation vectors
`R_1(x),R_2(x)` or their universal-envelope analogues with

```text
||R_i(x)||^2 <= C eta ||x||^2,
```

and an identity expressing the Jordan-identity defect as a finite sum of
bounded middle operators sandwiched between two such holes:

```text
D(a,b) = sum_i <R_i(X_i), M_i(a,b) R_i(Y_i)> + O(eta)||a||^3||b||.
```

Then Cauchy-Schwarz gives `O(eta)`.

Without such a two-hole identity, the ambient expansion only gives
`O(sqrt(eta))`.

## Status

Open. This should remain a conjectural strengthening until the doubled
CP/coCP calculation is written.
