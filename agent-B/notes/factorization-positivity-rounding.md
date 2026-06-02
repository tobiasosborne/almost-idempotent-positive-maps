# Factorization And Positivity Rounding

Layer 2 now has a candidate bridge from an almost-idempotent unital positive
map to an `O(sqrt(eta))` epsilon-JB order-unit algebra. This does not by
itself prove the full Kitaev-style factorization by genuinely positive maps.

## Setup After The Bridge

Let `Phi:B(H)_sa -> B(H)_sa` be unital positive and
`||Phi^2-Phi||<=eta`. Let

```text
P=theta(2Phi-I),        A=Im P,        a*b=P(a o b).
```

The bridge gives `A` as an `epsilon`-JB order-unit algebra with

```text
epsilon = O(sqrt(eta)).
```

Assume Layer 1 gives a finite-dimensional genuine JB algebra `J` and a unital
near-Jordan/order isomorphism

```text
v:J -> A
```

with distortion `O(epsilon)`.

The obvious factor maps are

```text
Delta_0 = inclusion_A_to_B(H) o v,
Upsilon_0 = v^{-1} o P.
```

Then

```text
Delta_0 Upsilon_0 = P = Phi + O(eta),
Upsilon_0 Delta_0 = id_J.
```

The issue is positivity:

- `Delta_0` is positive only if `v` is an actual positive/order map into the
  inherited cone of `A`.
- `Upsilon_0` is generally only approximately positive because `P` is not
  positive, only `O(eta)`-positive.

## Why The Naive Repair Is Not Enough

If a unital linear map `T:E -> J` satisfies

```text
x>=0, ||x||<=1  =>  T(x) >= -epsilon 1_J,
```

one might try

```text
T'(x) = (T(x)+epsilon phi(x)1_J)/(1+epsilon)
```

for a state `phi` on `E`. This is positive only if

```text
phi(x) >= c ||x||
```

for all positive `x`, with dimension-free `c`. Such a state does not exist on
`B(H)` or on `l_infty^n`: rank-one/minimal positive elements defeat it.

Thus positivity-rounding cannot be treated as a harmless scalar shift.

## Possible Ways To State Layer 1 To Avoid Half The Problem

The abstract stability theorem should produce more than a near multiplicative
norm isomorphism. For the positive-map theorem we should ask for one of:

1. A unital positive Jordan embedding `v:J -> A subset B(H)_sa` whose inverse
   is approximately positive on `A`.
2. A pair of unital positive maps `v:J -> A` and `w:A -> J` with
   `vw=id+O(epsilon)`, `wv=id+O(epsilon)`, and approximate Jordan
   multiplicativity.
3. In the strongest concrete version, a nearby concrete JC-subalgebra
   `J0 subset B(H)_sa` and a unital positive identification of `J` with `J0`.

Option 3 would make `Delta` positive for free, but does not automatically make
`Upsilon` positive or close to `P`.

## The Remaining Rounding Problem

The tempting missing statement would be a dimension-free repair theorem:

```text
Approximate-positive unital map  T:E -> J
=> nearby positive unital map T_+:E -> J.
```

Here `E` is usually `B(H)_sa` and `J` is finite-dimensional special JB/JC.
The desired bound would be

```text
||T-T_+|| <= C epsilon
```

with universal `C`.

This statement is false in this generality. A sidecar counterexample uses
spin-factor targets. For `J=R oplus R^m` with cone

```text
J_+ = {(s,v): s >= ||v||_2}
```

and `epsilon=1/(2m)`, define a unital map
`T:ell_infty^{2m}->J` on atoms by

```text
delta_{j,+} -> (epsilon,  2 epsilon e_j),
delta_{j,-} -> (epsilon, -2 epsilon e_j).
```

Then `T` is `epsilon`-positive on positive contractions, but every positive
unital map is at distance at least `sqrt(epsilon)` from `T`. Composing with the
diagonal conditional expectation gives the same obstruction for domain
`B(C^{2m})_sa`.

Thus a black-box positivity repair may force at least a square-root loss, and
cannot preserve the algebraic bridge exponent in full generality. See
`agent-B/notes/subagent-positivity-rounding.md`.

One useful reformulation: for unital maps between operator systems, exact
positivity is equivalent to contractivity; see Blecher-Read
`agent-B/references/blecher-read-2019/contractive-projections-real-positive.tex`
around Lemma 4.1, which recalls that a unital linear contraction on an operator
system is positive. Approximate positivity implies approximate contractivity,
since for `||x||<=1` we have
`0<=1+-x<=2` and hence

```text
-(1+O(epsilon))1 <= T(x) <= (1+O(epsilon))1.
```

Thus `||T||<=1+O(epsilon)`. The missing step can therefore also be phrased as:

```text
unital (1+epsilon)-contraction => nearby unital contraction/positive map.
```

This reformulation is helpful for diagnosis but not enough for a positive
result. The spin-factor counterexample shows that even the special JB geometry
does not give a dimension-free `O(epsilon)` repair for arbitrary approximately
positive unital maps.

## Alternative Route

Concrete Layer 1 output would make use of the following exact fact from the
positive-map paper: every finite-dimensional concrete J*-algebra
`J subset L(H)` has a unique trace-preserving conditional expectation
`E:L(H)->J`, and `E` is positive (`paper.tex` around lines 702-726).

Thus, if Layer 1 can produce a concrete `J0 subset B(H)_sa` close to
`A=Im P`, then positivity of `Delta` and a candidate positive `Upsilon` become
available from this canonical expectation. The remaining estimate is then
geometric:

```text
close(A,J0)  =>  ||E_{J0}-P|| small.
```

This is a different problem from arbitrary positivity rounding and may avoid
the spin-factor counterexample because `E_{J0}` is tied to an actual nearby
subalgebra.

The near-positive projection stability conjecture would bypass the problem even
more directly:

If the idempotent `P` is `O(eta)`-close to a unital positive idempotent `E`,
then exact Effros-Stormer gives a genuine JC range and the factorization can use
`E` directly.

This remains conjectural, but it is conceptually cleaner than repairing
arbitrary approximately positive maps after abstract stability.

## Current Recommendation

State the main factorization theorem conditionally until the positivity issue is
settled:

1. The algebraic bridge: unconditional candidate theorem with exponent
   `1/2`, producing an `O(sqrt(eta))` epsilon-JB algebra.
2. The factorization theorem with the same exponent requires either
   - positivity built into the Layer 1 output,
   - a concrete Layer 1 output plus an additional comparison argument,
   - near-positive projection stability, or
   - extra hypotheses excluding the spin-factor negative-variation
     obstruction.
3. If one uses only a black-box approximate-positive repair, expect at least a
   possible square-root loss: algebraic `epsilon=O(sqrt(eta))` may degrade to
   no better than `O(eta^(1/4))`.

Do not claim exact UP factor maps from Layer 1 alone.
