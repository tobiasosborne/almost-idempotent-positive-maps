# Audit Consensus 2026-06-04

This note records Agent B's current status after reading Agent A v0.11 and
three independent side audits.

## Layer 1

The abstract dimension-free stability theorem is still open:

```text
finite-dimensional epsilon-JB order-unit algebra
  => C epsilon-close to a genuine finite-dimensional JB algebra.
```

The exact missing lemma is not qualitative rigidity. It is a dimension-free
order-unit-norm Jordan cochain homotopy. One needs an explicit operator

```text
S:C^2_J(B,M)->C^1_J(B,M)
```

for every finite-dimensional JB algebra `B` and relevant Banach Jordan module
`M`, with

```text
d^1 S f=f,        ||S f|| <= K ||f||
```

for exact cocycles and universal `K`, independent of matrix rank, spin-factor
dimension, Albert summands, and number of direct summands. The same construction
must also control approximate cocycles and approximate module actions with only
`O(K epsilon)` loss.

Haar averaging over `Aut(B)` has norm one as a projection, but that alone is not
a right inverse to the Jordan coboundary. The inverse estimate on the
non-invariant cochain components is exactly where rank or dimension dependence
can enter. Agent A's Frobenius-norm numerics are useful evidence, but they do
not prove the needed order-unit/operator-norm estimate.

## Layer 2 And Factorization

The arbitrary unital-positive algebraic bridge remains proved internally at
`O(sqrt(eta))`:

```text
Phi unital positive, ||Phi^2-Phi|| <= eta
P=theta(2Phi-I), A=Im P, a*b=P(a o b)
  => A is an O(sqrt(eta))-JB order-unit algebra.
```

The conditional exact UP factorization theorem is also locally sound. Under the
near-positive projection-stability hypothesis, `P` is repaired to a positive
idempotent `E`; Effros-Stormer then gives the special JB/JC range
`J=E(B(H)_sa)` and the exact positive factor maps

```text
Delta = inclusion,        Upsilon = E.
```

Thus this route has a single unproved input: near-positive projection stability.
The sharp noncommutative target is:

```text
P^2=P, P(1)=1, ||P||<=1+delta, P(x)>=-delta 1 for 0<=x<=1
  => dist(P, positive unital idempotents) <= C sqrt(delta).
```

The sharp reduced commutative gap is the global exposed-hull lemma for exact
signed affine retractions. If `W_{rho,kappa}` is the set of row vertices exposed
at `rho=O(sqrt(delta))` with gap `kappa>=c sqrt(delta)`, prove every row is
`O(sqrt(delta))`-close to `conv W_{rho,kappa}`. The existing
cluster-representative theorem then gives an exact commutative positive/JB
factorization.

## Faithful-Invariant Sidequest

Agent A v0.11 and Agent B now agree on the corrected answer:

```text
faithful invariant state alone does not imply approximate ambient-product
closure with a dimension-free rate.
```

The valid quantitative statement is conditioned by the least density `mu` of the
invariant state:

```text
||a o b - P(a o b)|| <= C (eta/mu) ||a|| ||b||.
```

B's `3 x 3` stochastic family has faithful invariant states for every parameter
but `mu=Theta(eta)` and ambient square holes bounded below by a constant. Hence
the Effros-Stormer projected product remains necessary under the baseline
hypotheses.

Report provenance/status corrections to request from Agent A:

1. `prop:faithful-exact` should not be ledgered as purely original; it is
   supported by VLW faithful fixed-point/multiplicative-domain theory plus the
   inline proof.
2. `ex:no-faithful` should not cite the stale A-FIT sentence claiming a unique
   invariant state. The correct invariant face is `(t,1-t,0)`.
3. `thm:faithful-approx` should distinguish the exact-invariant subcase proved
   in B-FIT from the approximate-invariance extension proved in A-FIT/report.

No downgrade is needed for the report's Section 6 bridge theorem labels.

## Current Priority

Agent B's most useful next mathematical work is on the exact factorization
route: either prove the near-positive projection-stability theorem or disprove
it already in the commutative Markov/signed-idempotent model. The cleanest
current target is the global exposed-hull lemma; arbitrary convex polygon
intuition is not enough unless it is realized by an exact signed idempotent with
small row negative mass.
