# Layer 1 Quantitative Stability: Proof Obligations

This note sharpens the current status of Agent A's Layer 1 plan. It is not a
replacement for `agent-B/notes/layer1-agent-a-review-v0.1.md`; it specifies the
exact estimates that must be proved before the abstract epsilon-JB stability
theorem can be used in the positive-map factorization theorem.

## Current Target

The desired abstract theorem is:

```text
finite-dimensional epsilon-JB order-unit algebra
  => C epsilon-close to a genuine finite-dimensional JB algebra
```

with universal constants independent of dimension and of the number/type of
simple summands.

The proposed proof mirrors Kitaev's error reduction: if
`v:B -> A` is a `delta`-Jordan homomorphism from an exact JB algebra into an
epsilon-JB algebra, correct `v` by a bounded linear `h:B->A` so that the new
multiplicativity defect is `O(delta^2+epsilon)`.

## What Kitaev's Associative Step Actually Uses

Kitaev's `lem_approx` does not use only `H^2=0`. It uses a diagonal

```text
D = sum_j A_j tensor B_j
```

with two properties:

```text
X D = D X,        pi(D)=1,
sum_j ||A_j|| ||B_j|| = 1.
```

The last bound is the dimension-free part. It comes from the representation

```text
D = integral U^* tensor U dmu(U),
```

a probability average of norm-one elements. The correction

```text
w(X)=sum_j v(A_j) g(B_j,X)
```

is therefore bounded by `O(delta)` without any dimension factor. The
associative cocycle equation and the diagonal identities then give
`F_w=g+O(delta^2+epsilon)`.

## Jordan Replacement Needed

For the Jordan proof, it is not enough to cite `H^2(B,M)=0`. We need a
dimension-free homotopy formula in the order-unit norm. Concretely:

### Obligation 1: Explicit Homotopy

Produce an explicit linear operator

```text
S: C^2_J(B,M) -> C^1_J(B,M)
```

for every finite-dimensional JB algebra `B` and every unital Banach Jordan
`B`-module `M`, such that for exact Jordan 2-cocycles

```text
d^1 S f = f.
```

Here the module action and the Jordan coboundary must be the same ones used in
the perturbative proof.

### Obligation 2: Dimension-Free Norm

Prove

```text
||S f|| <= K ||f||
```

with universal `K`, where the cochain norms are the norms relevant to the
epsilon-JB theorem: order-unit/operator norms, not unnormalized trace/Hilbert
norms.

This is the main missing estimate. A Haar probability Reynolds operator has
norm `1`, but it is only an averaging projection on cochains. By itself it is
not a right inverse to `d^1`. The inverse on non-invariant isotypic components
requires a spectral-gap or separability-idempotent estimate; that estimate is
where dimension/rank dependence can enter.

### Obligation 3: Approximate-Cocycle Projection

The draft statement

```text
d^2 g = O(epsilon)  =>  g is O(epsilon)-close to an exact cocycle
```

also requires a bounded homotopy/projection for the cochain complex. It cannot
be used before Obligation 2 is proved. A valid proof can avoid naming an exact
cocycle by showing directly that

```text
d^1 S g = g + O(K epsilon)
```

for approximate cocycles.

### Obligation 4: Direct Sums

If

```text
B = direct_sum_k B_k,
```

the estimate must remain independent of the number of summands. This requires
an explicit blockwise decomposition of cochains:

- same-factor cocycles;
- cross-factor cocycles;
- central/idempotent movement terms.

The order-unit norm on a direct sum is a max norm, so a block-diagonal
construction should be possible, but cross-factor terms must be killed with
constants independent of the number of blocks.

### Obligation 5: Simple Factor Uniformity

Uniformity must be checked separately for the simple Euclidean JB factors:

- `H_n(R)`, `H_n(C)`, `H_n(H)` with `n` unbounded;
- spin factors `V_m` with `m` unbounded;
- the exceptional Albert factor `H_3(O)`.

The Albert factor is finite in type and should not create dimension growth.
The real tests are matrix rank and spin-factor dimension. A trace-form
Casimir whose Hilbert norm scales like dimension is not enough; it must be
renormalized into an order-unit-norm homotopy with universal bound.

### Obligation 6: Approximate Module Errors

In the application, `M=A` is not an exact `B`-module. The action

```text
a . m = v(a) * m
```

uses the approximate product of `A`. The proof must derive, from JB4 and the
`delta`-multiplicativity of `v`, the precise `O(epsilon+delta^2)` error in the
Jordan cocycle identity. This derivation cannot be hidden inside exact
cohomology notation.

## Positivity Output Is A Separate Requirement

Even after the algebraic Layer 1 theorem is proved, exact UP factorization does
not follow automatically. For the channel theorem, Layer 1 must also provide at
least one of:

- positive near-inverse comparison maps;
- a nearby concrete JC subalgebra of `B(H)_sa` with a canonical positive
  conditional expectation close to `P`;
- enough concrete comparison data to combine with near-positive projection
  stability.

The spin-factor positivity-rounding obstruction shows that an arbitrary
approximately positive algebraic isomorphism cannot be repaired linearly in
general.

## Current Assessment

The Layer 1 route is plausible but not proved. The right next deliverable is
not another qualitative cohomology citation; it is a concrete Jordan analogue
of Kitaev's norm-one diagonal calculation, or an incremental Peirce/frame
construction that avoids applying a global homotopy with dimension-dependent
constants.

## Literature Boundary Checked

`agent-B/notes/known-jstar-stability-literature-check.md` records a check of
Baak--Moslehian's *On the Stability of J*-Homomorphisms* and the relevant
Chu--Russo/Penico cohomology facts.

Conclusion: existing J*-homomorphism Hyers--Ulam--Rassias stability does not
prove Layer 1. It stabilizes maps between already exact J*-algebras under
global scaling-control hypotheses; it does not perturb an epsilon-JB product
on an order-unit space to an exact JB algebra. Chu--Russo/Penico supplies
qualitative `H^2=0`, but not the required dimension-free order-unit-norm
homotopy.
