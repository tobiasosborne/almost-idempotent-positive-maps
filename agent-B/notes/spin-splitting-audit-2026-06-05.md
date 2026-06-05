# Spin Splitting Audit

Date: 2026-06-05.

Scope: audit Agent A's `agent-A/theory/02-spin-splitting.md`.

Follow-up: the adjoint spin target identified in this audit is now proved in
`agent-B/notes/adjoint-spin-splitting-theorem.md`, with
`||S_H||_{Fop->Fop} <= 2` for exact adjoint coboundaries. The module and
approximate-cocycle caveats below still apply to the full Layer-1 ER lemma.

## Verdict

The spin note contains a useful and correct reduction:

```text
V_n = R 1 \oplus R^n,
|| (t,v) ||_ou = |t| + ||v||_2,
|| (t,v) ||_2 = (t^2+||v||_2^2)^{1/2}.
```

Therefore

```text
||x||_2 <= ||x||_ou <= sqrt(2)||x||_2
```

uniformly in `n`. Propagating this through one- and two-cochain injective norms
does give

```text
||S||_{ou->ou} <= 2 sqrt(2) ||S||_{Fop->Fop}
```

for spin factors, where `Fop` means Euclidean-injective norm on the cochain
slots. This is a good reduction: a dimension-free Euclidean-injective right
inverse for the adjoint spin cochain complex would imply a dimension-free
order-unit right inverse.

However, the note overstates what has been proved. The remaining
`Fop -> Fop` estimate is not automatic from the Hilbert/Frobenius
pseudoinverse, from bounded rank, or from small `O(n)` multiplicities. It still
requires an explicit injective-norm computation.

## 1. Element Norm Equivalence Is Not The Whole Cochain Story

The statement that the operator-norm obstruction is "exactly" the
`sqrt(rank)` element-norm conversion is too strong.

At the cochain level there are at least three separate norm conversions:

1. output element norm;
2. input-slot element norms;
3. Hilbert/HS tensor norm versus injective multilinear norm.

A bilinear form can have injective norm `1` and Hilbert-Schmidt norm growing
with dimension; the basic example is

```text
(x,y) -> <x,y>
```

on `R^n`, whose injective norm is `1` while its Hilbert-Schmidt tensor norm is
`sqrt(n)`. Thus a bounded singular-value estimate for `d^1` in HS norm does not
imply a bounded `Fop -> Fop` right inverse, even in the spin family. Agent A
does flag this later in the note, but the headline "whole story" claim should
be narrowed to the element-norm comparison only.

## 2. The Proposed Rank-Balance Lemma Has The Wrong Force

For the matrix families `H_n(F)`, a Hilbert/Frobenius bound gives, schematically,

```text
||h(a)||_2 <= C ||a||_2 <= C sqrt(n) ||a||_ou
```

for an order-unit input `a`. To turn this into an order-unit output bound, one
needs control of `||h(a)||_ou` itself. The displayed condition in Agent A's note,

```text
||h(a)||_2 <= K ||h(a)||_ou,
```

is a low-effective-rank condition. It does not reduce the upper bound on
`||h(a)||_ou`; since `||h(a)||_ou <= ||h(a)||_2` is already automatic, low
effective rank can still leave `||h(a)||_ou` as large as the Hilbert bound.

The condition that would actually remove a `sqrt(n)` loss from a Hilbert-bound
argument is closer to a high-spread estimate

```text
||h(a)||_ou <= K n^{-1/2} ||h(a)||_2
```

on the relevant outputs, or else a direct order-unit estimate bypassing the
Hilbert norm entirely. The current "rank-balance" formulation mixes low-rank
and spread behavior and should be rewritten before being used as a target.

## 3. `O(n)` Multiplicity Control Is Not An Injective-Norm Bound

The representation-theoretic setup for spin is promising:

```text
V_n = 1 \oplus W,        Aut(V_n)=O(n),
ker d^1 = Der(V_n)=Lambda^2(W).
```

After averaging, one may choose an `O(n)`-equivariant splitting. Schur's lemma
then reduces the Hilbert-space problem to maps between finite-dimensional
multiplicity spaces.

But this does not by itself bound the Banach cochain norm. The irreducible
summands inherit injective norms from their realization inside tensor powers of
`W`, and these Banach norms can have dimension-dependent geometry. The
projection/inclusion constants for pieces such as

```text
Sym^2_0(W),        Sym^3_0(W),        hook (2,1)
```

must be estimated as multilinear maps, not only as orthogonal Hilbert
projections. Small multiplicity says the matrix algebra on multiplicity spaces
is small; it does not say the surrounding injective tensor norms are uniformly
equivalent to the Hilbert norms.

Therefore the spin proof still needs the explicit `O(n)` tensor-contraction
calculation:

```text
S_n : im(d^1) subset C^2(V_n,V_n) -> C^1(V_n,V_n),
d^1 S_n f = f,
||S_n||_{Fop->Fop} <= K.
```

The constants must be checked for each scalar/vector/traceless/hook component
in the injective norm. Numerical flatness of the pseudoinverse is useful
evidence, but not a substitute for this estimate.

## 4. Module Caveat

The spin note appears to work with the adjoint module `M=V_n`. That is a valid
and valuable benchmark. It is not the full error-reduction lemma needed for
Layer 1, which requires the relevant `B`-module arising from the approximate
codomain `A` and must handle direct sums and mixed Peirce-`1/2` components.

Thus a theorem for adjoint spin factors should be labelled:

```text
dimension-free adjoint spin right inverse
```

not a proof of the general `ER-norm` obligation.

## The Useful Next Target

I recommend preserving Agent A's spin route but restating it as:

> For the adjoint spin factor `V_n`, prove an explicit `O(n)`-equivariant
> right inverse to `d^1` with uniformly bounded Euclidean-injective cochain
> norm.

This is concrete and worth doing. The proof should not rely on HS singular
values or finite multiplicity alone; it must compute the actual
injective-norm bounds of the equivariant tensor contractions.
