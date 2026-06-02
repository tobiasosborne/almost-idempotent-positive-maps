# Decomposable Doubling Route: A Basic Obstruction

This note stress-tests the most tempting route to an `O(eta)` decomposable
bridge.

## Tempting Construction

Given an explicit CP+coCP decomposition

```text
Phi = Phi_0 + Psi_0 o tau,
```

one would like to pass to a doubled/opposite algebra `D=A oplus A^op`.
There is a Jordan/*-homomorphic embedding

```text
j:A -> D
```

and a CP map

```text
C:D -> A
```

such that

```text
Phi = C j.
```

The tempting move is to consider the CP map

```text
F = j C:D -> D
```

and apply Kitaev's UCP `O(eta)` theorem to `F`.

## The Problem

Almost-idempotence of `Phi=Cj` does not control almost-idempotence of `F=jC`.
Indeed

```text
F^2-F = j(CjC-C)=j((Phi-I)C).
```

The hypothesis `||Phi^2-Phi||` controls `(Phi-I)` only on `Ran(Phi)` (or on
inputs of the form `Phi(x)`), not on the larger set `C(D)`.

Thus the doubled CP route needs an additional argument proving

```text
||(Phi-I)C|| <= O(eta),
```

or some substitute two-hole identity. It does not follow formally from
`||Phi^2-Phi||<=eta`.

## Commutative Exact Counterexample To The Formal Implication

This obstruction already occurs for stochastic maps between commutative
C*-algebras, in the actual doubled form.

Let

```text
j: ell_infty^2 -> ell_infty^2 oplus ell_infty^2 = ell_infty^4,
j(x1,x2)=(x1,x2,x1,x2).
```

Let `C:ell_infty^4 -> ell_infty^2` be the row-stochastic map

```text
C =
[ 1/2   0     0     1/2
  0     1/2   1/2   0   ].
```

Then

```text
Phi=Cj =
[ 1/2  1/2
  1/2  1/2 ],
```

so `Phi^2=Phi` exactly.

But

```text
F=jC =
[ 1/2   0     0     1/2
  0     1/2   1/2   0
  1/2   0     0     1/2
  0     1/2   1/2   0 ],
```

and

```text
||F^2-F||_{infty->infty}=1.
```

So even exact idempotence of `Cj` does not imply approximate idempotence of
`jC` with any small bound.

## Consequence

The decomposable `O(eta)` theorem remains plausible, but it cannot be proved
by simply applying Kitaev's CP theorem to `jC` after the universal/opposite
doubling. A valid proof must add one of:

1. a stronger dilation-compatible hypothesis, such as
   `||jCjC-jC||=O(eta)`;
2. a proof that the specific decomposable channel data force
   `C(D)` to lie `O(eta)`-close to the approximate fixed space of `Phi`;
3. a direct CP/coCP two-hole identity for the Jordan defect that uses only
   `||Phi^2-Phi||`.

Without one of these, the `O(eta)` decomposable bridge should stay
conjectural.
