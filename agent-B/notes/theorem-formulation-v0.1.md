# Theorem Formulation v0.1

This is Agent B's current proposed formulation after reading Agent A v0.2.

## Definitions

Work first on real self-adjoint parts.

An `epsilon`-JB order-unit algebra is a finite-dimensional real order-unit space `(A,A_+,1)` with order-unit norm and a commutative bilinear product `*` such that:

1. `1*a=a` exactly.
2. `||a*b|| <= (1+epsilon)||a||||b||`.
3. `||a*a|| >= (1-epsilon)||a||^2`.
4. `a*a >= -epsilon ||a||^2 1`.
5. `||((a*a)*b)*a - (a*a)*(b*a)|| <= epsilon ||a||^3 ||b||`.

This should be reviewed by Agent A. I currently prefer keeping both the norm-square lower bound and order positivity of squares because both are natural outputs of positive maps.

## Layer 1: Abstract Stability

Desired theorem:

There are universal constants `epsilon0,C` such that every finite-dimensional `epsilon`-JB order-unit algebra with `epsilon<epsilon0` is `C epsilon`-isomorphic, as an order-unit Jordan algebra, to a genuine finite-dimensional JB algebra.

For the positive-map application it is enough to prove the special/JC version. A full JB theorem including `H_3(O)` is welcome but not needed for the north star.

## Layer 2A: Conditional Positive-Map Bridge

Let `Phi:B(H)_sa -> B(H)_sa` be unital positive and `||Phi^2-Phi||<=eta`. Let `P=theta(2Phi-I)`, `A=Im P`, and `a*b=P(a o b)`.

Assume a contextual insertion estimate: there are `alpha>0` and universal `C` such that for each Jordan monomial context `C[ ]` of degree at most four needed to expand the Jordan identity,

```text
|| P(C[P(x)]) - P(C[x]) || <= C eta^alpha ||x|| prod ||inputs||.
```

Then `A` is an `O(eta^alpha)`-JB order-unit algebra.

Known from Agent B:

- the easy axioms hold with `O(eta)`;
- the first insertion context `C[x]=x o b`, `b in A`, holds with `alpha=1/2`;
- Agent B now has a candidate approximate Effros-Stormer null-ideal estimate
  for range-product holes, giving the full Jordan identity with `alpha=1/2`.
  See `agent-B/notes/layer2-null-ideal-sqrt.md`. This should be reviewed by
  Agent A before consensus.

## Layer 2B: Factorization

Assuming Layer 1 and Layer 2A, obtain a genuine finite-dimensional JB algebra `J` and an isomorphism

```text
v:J -> A
```

with distortion `O(eta^alpha)`.

The map

```text
Delta = inclusion_A_to_B(H) o v
```

is unital and approximately positive. The map

```text
tilde Upsilon = v^{-1} o P
```

is unital and approximately positive, and

```text
Delta tildeUpsilon = P = Phi + O(eta),
tildeUpsilon Delta = id_J.
```

Remaining rounding problem:

Turn approximately positive unital maps `Delta, tildeUpsilon` into genuinely positive unital maps with comparable norm error. In finite-dimensional order-unit spaces this should follow from cone perturbation if `v` is an approximate order isomorphism, but it must be written carefully.

Warning: this is not automatic dimension-free. A naive repair by adding a fixed faithful state can introduce constants depending on the smallest value of that state on normalized positive elements. The positive-map analog of Kitaev's UCP rounding is therefore a separate proof obligation.

Possible safer route: strengthen Layer 1 in the concrete setting so that it produces an actual concrete JC-subalgebra `J0 subset B(H)_sa` close to `A=Im P`. Then the trace-preserving conditional expectation onto `J0` is positive by VLW, and one can try to compare it directly with `P`/`Phi`. This would avoid abstract cone-rounding, but it is a stronger stability theorem.

Conclusion target:

```text
||Delta Upsilon - Phi|| <= O(eta^alpha) + O(eta)
||Upsilon Delta - id_J|| <= O(eta^alpha)
```

with approximate Jordan multiplicativity.

## Correct Target Class

The factorization target in the positive-map theorem should be a finite-dimensional special JB/JC algebra, equivalently the self-adjoint part of a finite-dimensional J*-algebra after complexification.

It should **not** be stated as reversible in general.

Decomposable factor maps should be a corollary only under an additional reversible/universally reversible hypothesis.

## Sharpened Conjecture

The natural Kitaev-strength bridge conjecture is that the contextual
insertion/null-ideal estimates hold with `alpha=1`.

Agent B's current candidate proof gives the unconditional positive-map bridge
with `alpha=1/2`. The earlier first-insertion-only proof was insufficient; the
new ingredient is the approximate null-ideal estimate for square holes
`P(r^2)-r^2`.

Agent A v0.4 correctly retracts the claim that `alpha=1` is automatic for
arbitrary unital positive maps. The plausible `alpha=1` theorem should be
stated under an explicitly controlled CP/coCP decomposition, not as
`||Phi||_dec=1` for the standard Haagerup/Wittstock decomposable norm. The
transpose has standard decomposable norm `n` on `M_n`, but any unital CP+coCP
decomposition has CP pieces with cb norms at most `1`.
