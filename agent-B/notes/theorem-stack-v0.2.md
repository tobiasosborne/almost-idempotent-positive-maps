# Theorem Stack v0.2

This is Agent B's current clean formulation after the null-ideal bridge and
decomposable-norm correction.

## Definition: Epsilon-JB Order-Unit Algebra

A finite-dimensional real order-unit space `(A,A_+,1)` with order-unit norm and
a commutative bilinear product `*` is an `epsilon`-JB order-unit algebra if:

1. `1*a=a` exactly.
2. `||a*b|| <= (1+epsilon)||a||||b||`.
3. `||a*a|| >= (1-epsilon)||a||^2`.
4. `a*a >= -epsilon ||a||^2 1`.
5. `||((a*a)*b)*a - (a*a)*(b*a)|| <= epsilon ||a||^3 ||b||`.

The order-unit structure is exact; only the product axioms are approximate.

## Theorem A: Abstract Stability

Desired Layer 1 theorem:

There are universal constants `epsilon0,C` such that every finite-dimensional
`epsilon`-JB order-unit algebra with `epsilon<epsilon0` is `C epsilon`-close to
a genuine finite-dimensional JB algebra.

For the positive-map application, the output should include order data strong
enough to produce positive maps. A norm-only near Jordan isomorphism is not
enough. The useful versions would output either:

- unital positive near-inverse maps between the approximate object and a
  genuine JB algebra; or
- a concrete nearby JC-subalgebra in the ambient `B(H)_sa`; or
- enough extra cone control to avoid the generic spin-factor
  positivity-rounding obstruction.

Agent A is currently leading this theorem.

## Theorem B: Algebraic Positive-Map Bridge

Let `Phi:B(H)_sa -> B(H)_sa` be unital positive with

```text
||Phi^2-Phi|| <= eta
```

in operator norm. For small `eta`, set

```text
P=theta(2Phi-I),        A=Im P,        a*b=P(a o b),
```

where `a o b=(ab+ba)/2`.

Then Agent B's candidate theorem is:

```text
(A,*,1,A_+ inherited from B(H)_sa) is an O(sqrt(eta))-JB order-unit algebra.
```

The proof has three parts:

1. Spectral calculus gives `P^2=P`, `P(1)=1`, `||P-Phi||=O(eta)`, and
   `||P||<=1+O(eta)`.
2. Jordan-Schwarz for `Phi` gives the first insertion estimate
   `||P(Px o b)-P(x o b)||<=C sqrt(eta)||x||||b||` for `b in A`.
3. Square holes `q_r=P(r^2)-r^2` are almost positive kernel elements; after a
   positivity shift, `||P(q_r^2)||<=C eta||r||^4`. Polarization gives
   hole-hole and hole-range estimates, closing the Jordan identity at
   `O(sqrt(eta))`.

Detailed proof: `agent-B/theory/theorem-B-algebraic-bridge.md`; exploratory
notes: `agent-B/notes/layer2-null-ideal-sqrt.md`.

This is the main new Agent B claim and should be peer-reviewed by Agent A.

## Theorem C: Conditional Factorization

Assume:

1. Theorem A holds with order/positivity output strong enough for maps.
2. The output avoids the black-box positivity-rounding obstruction, for example
   by giving concrete positive comparison maps or by proving near-positive
   projection stability for `P`.

Then for `Phi` as in Theorem B there should exist a finite-dimensional special
JB/JC algebra `J` and unital positive maps

```text
Delta:J -> B(H)_sa,
Upsilon:B(H)_sa -> J
```

such that

```text
||Delta Upsilon - Phi|| <= C sqrt(eta),
||Upsilon Delta - id_J|| <= C sqrt(eta),
```

with the expected approximate Jordan multiplicativity.

The target is special JB/JC, equivalently the self-adjoint part of a
finite-dimensional J*-algebra after complexification. It is not reversible in
general.

The unresolved point is exact positivity of `Delta,Upsilon`; see
`agent-B/notes/factorization-positivity-rounding.md`.

Important: a general dimension-free `O(epsilon)` theorem saying that every
unital `epsilon`-positive map into a finite-dimensional JB algebra is
`O(epsilon)`-close to a positive unital map is false. A spin-factor target gives
a lower bound `sqrt(epsilon)`. Therefore exact UP factor maps with the same
exponent must be constructed using the special structure of this problem, not a
generic rounding lemma.

Near-positive projection stability, if used instead, is also at best
square-root in general. Hume found a classical `l_infty^3` unital idempotent
family with positivity defect `delta=s^2` and distance
`2sqrt(delta)+O(delta)` from every stochastic idempotent. Thus projection
stability can plausibly recover the baseline `O(sqrt(eta))` factorization but
cannot yield `O(eta)` for arbitrary positive maps.

As of 2026-06-02, the projection-stability route is still conditional. The
commutative version is equivalent, up to constants, to the Markov perturbation
theorem

```text
Q row-stochastic, ||Q^2-Q||_{infty->infty} <= eps
  => dist(Q, stochastic idempotents) <= C sqrt(eps).
```

No proof or citation for this dimension-free theorem has been found. Exact UP
factorization should therefore remain conditional unless Layer 1 outputs
concrete positive comparison maps or this Markov/noncommutative
projection-stability theorem is proved.

## Decomposable Strengthening

The Kitaev-strength exponent `O(eta)` is not currently proven for arbitrary
positive maps. Agent A v0.4 and Agent B agree that it likely requires
dilation/two-hole structure.

Plausible stronger theorem:

If `Phi` admits an explicitly controlled decomposition

```text
Phi = Phi_0 + Psi_0 o tau,
```

with `Phi_0,Psi_0` completely positive and `tau` a transpose/anti-automorphic
coCP leg, then the bridge may improve to `O(eta)` by adapting Kitaev's two-hole
argument separately to the CP and coCP summands.

Do **not** state this as `||Phi||_dec=1` for the standard
Haagerup/Wittstock decomposable norm. The transpose on `M_n` is a unital
positive decomposable map with standard decomposable norm `n`.

For a unital CP+coCP decomposition, the component bound needed for estimates is
automatic:

```text
Phi_0(1)+Psi_0(1)=1,
||Phi_0||_cb, ||Psi_0||_cb <= 1.
```

The actual two-hole computation remains unwritten.

Additional caution: the naive universal/opposite doubling does not by itself
solve this. If `Phi=Cj` is a doubled factorization, the candidate lifted map
`F=jC` satisfies

```text
F^2-F=j((Phi-I)C),
```

which is not controlled by `||Phi^2-Phi||` without extra information on
`C(D)`. A commutative stochastic example in the exact doubled form has `Cj`
exactly idempotent but `||jCjC-jC||=1`; see
`agent-B/notes/decomposable-doubling-obstruction.md`.

There is a valid conditional version: if one can choose a dilation-compatible
model in which `F=jC` is UCP and `||F^2-F||_cb<=eta`, then Kitaev's theorem
applied to `F` restricts along the Jordan embedding and gives the desired
`O(eta)` bridge. See
`agent-B/notes/decomposable-dilation-compatible-theorem.md`.

## Exact Consistency

When `eta=0`, `P=Phi` is a unital positive projection. Effros-Stormer applies
exactly: `P(B(H)_sa)` is a JC algebra for `r*s=P(r o s)`.

The v0.2 theorem stack reduces to this exact result at `eta=0`.
