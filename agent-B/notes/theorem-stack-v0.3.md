# Theorem Stack v0.3

This is Agent B's current consensus candidate after:

- the `O(sqrt(eta))` algebraic bridge proof, verified by Agent A v0.5 and
  re-audited during the report review;
- the positivity-rounding obstruction;
- the classical projection-stability reduction;
- the decomposable doubled-route stress test.

Prefer this file over `theorem-stack-v0.2.md`.

## Definition: Epsilon-JB Order-Unit Algebra

A finite-dimensional real order-unit space `(A,A_+,1)` with order-unit norm and
a commutative bilinear product `*` is an `epsilon`-JB order-unit algebra if:

1. `1*a=a` exactly.
2. `||a*b|| <= (1+epsilon)||a||||b||`.
3. `||a*a|| >= (1-epsilon)||a||^2`.
4. `a*a >= -epsilon ||a||^2 1`.
5. `||((a*a)*b)*a - (a*a)*(b*a)|| <= epsilon ||a||^3 ||b||`.

The order-unit structure is exact; only the product axioms are approximate.

## Theorem 1: Abstract Algebraic Stability

Desired Layer 1 theorem:

There are universal constants `epsilon0,C` such that every finite-dimensional
`epsilon`-JB order-unit algebra with `epsilon<epsilon0` is `C epsilon`-close to
a genuine finite-dimensional JB algebra.

Status: open. Agent A's proposed cohomological error-reduction route still
needs a dimension-free bounded Jordan cohomology splitting, not just qualitative
`H^2=0`. See `agent-B/notes/layer1-agent-a-review-v0.1.md`.
A local literature check of Baak--Moslehian J*-homomorphism stability and
Chu--Russo/Penico cohomology is recorded at
`agent-B/notes/known-jstar-stability-literature-check.md`; it confirms that
these sources do not provide the required dimension-free epsilon-JB product
stability theorem.

For the positive-map factorization theorem, this algebraic version is not
enough by itself. A useful Layer 1 output must additionally provide at least
one of:

- positive near-inverse maps;
- a nearby concrete JC-subalgebra in the ambient `B(H)_sa`;
- a comparison theorem strong enough to pair with near-positive projection
  stability.

See `agent-B/notes/layer1-output-requirements.md`.

## Theorem 2: Algebraic Positive-Map Bridge

Let `H` be finite-dimensional and let `Phi:B(H)_sa -> B(H)_sa` be unital
positive with

```text
||Phi^2-Phi|| <= eta
```

in operator norm. For small `eta`, set

```text
P=theta(2Phi-I),        A=Im P,        a*b=P(a o b),
```

where `a o b=(ab+ba)/2`.

Then Agent B's theorem is:

```text
(A,*,1,A_+ inherited from B(H)_sa)
is an O(sqrt(eta))-JB order-unit algebra.
```

Status: proved internally at the `O(sqrt(eta))` scale. Detailed proof:
`agent-B/theory/theorem-B-algebraic-bridge.md`. Agent A reports a line-by-line
verification in `agent-a-findings` v0.5 §10. Agent B's report-review pass on
2026-06-02 found no local algebraic error in Section 6 of `report/`; it did
patch status/provenance and small-threshold wording around the theorem. The
spectral-idempotent estimate is proved directly by the Banach-algebra formula
`sgn(S)=S(S^2)^(-1/2)` for `S=2Phi-I`, after fixing a small universal
threshold `eta0`.

Proof ingredients:

1. Spectral calculus gives `P^2=P`, `P(1)=1`, `||P-Phi||=O(eta)`,
   `||P||<=1+O(eta)`, and `P` is `O(eta)`-positive.
2. Since `A=Im P` is a unital self-adjoint real subspace, the inherited cone
   `A cap B(H)_+` gives an exact Archimedean order-unit space and its
   order-unit norm is exactly the ambient operator norm.
3. Jordan-Schwarz for `Phi` gives first insertion:
   `||P(Px o b)-P(x o b)||<=C sqrt(eta)||x||||b||` for `b in A`.
4. Square holes `q_r=P(r^2)-r^2` are almost positive kernel elements. After a
   positivity shift, `||P(q_r^2)||<=C eta||r||^4`.
5. Polarization gives arbitrary product-hole bounds from the square-hole
   bounds; then Cauchy-Schwarz gives hole-hole and hole-range estimates, which
   close the Jordan identity at `O(sqrt(eta))`.

The proof now explicitly isolates the standard order estimates used in these
steps: Jordan-Schwarz for unital positive maps on self-adjoint elements,
Cauchy-Schwarz for positive functionals, positive-cone norm monotonicity, and
the state-supremum formula for self-adjoint norms. It also makes explicit the
self-adjoint order-perturbation rule
`||x-y||<=epsilon => x>=y-epsilon 1`, used in the square-hole lower bound. No
CP/cb input is used in the bridge proof.

This theorem does not require `P` to be positive. `P` can fail positivity even
classically.

## Theorem 3: Conditional Exact UP Factorization

Assume near-positive projection stability at the sharp square-root scale:
every `delta`-positive unital idempotent `P:B(H)_sa -> B(H)_sa` with
`||P||<=1+delta` is `O(sqrt(delta))`-close to a unital positive idempotent.

Then for `Phi` as in Theorem 2 there exist a finite-dimensional special JB/JC
algebra `J` and unital positive maps

```text
Delta:J -> B(H)_sa,
Upsilon:B(H)_sa -> J
```

such that

```text
||Delta Upsilon - Phi|| <= C sqrt(eta),
Upsilon Delta = id_J,
Upsilon(Delta(x) o Delta(y)) = x*y        (x,y in J).
```

This implication is now written as a theorem-level proof in
`agent-B/theory/theorem-C-conditional-factorization.md`. It uses the spectral
estimate for `P=theta(2Phi-I)`, the assumed projection-stability theorem to
replace `P` by a positive idempotent `E`, and exact Effros-Stormer on `E`.
The proof now explicitly justifies the real-to-complex step: a unital positive
idempotent `E:B(H)_sa->B(H)_sa` extends complex-linearly to a unital positive
projection on `B(H)`, so Effros-Stormer applies and restricts back to the real
self-adjoint range with product `E(x o y)`. It also checks positivity of the
factor maps against the chosen cones: inclusion is positive for
`J_+=J cap B(H)_+`, and `E(V_+) subset J_+`.
The proof now also verifies cone compatibility: the JB positive cone of the
Effros-Stormer product equals the inherited cone `J cap B(H)_+`. One inclusion
uses `x*x=E(x o x)` and positivity of `E`; the other uses the unital JB
criterion `z>=0 iff || ||z||1-z ||<=||z||` together with the inherited Banach
norm.

If instead Theorem 1 is proved with a positivity-capable/concrete output, an
analogous exact factorization should follow by comparing `P` to the canonical
positive expectation onto the nearby concrete JC algebra. That route is not yet
formalized.

Status: the implication from near-positive projection stability is proved
conditionally; the projection-stability theorem itself remains open. Exact
factorization is not proved from algebraic stability alone.

Reason: generic dimension-free `O(epsilon)` positivity rounding is false for
finite-dimensional JB targets. A spin-factor example gives maps that are
`epsilon`-positive but at distance at least `sqrt(epsilon)` from every positive
unital map. See `agent-B/notes/factorization-positivity-rounding.md`.

The near-positive projection-stability route is also open. Its commutative
version is equivalent, up to constants, to:

```text
Q row-stochastic, ||Q^2-Q||_{infty->infty} <= eps
  => dist(Q, stochastic idempotents) <= C sqrt(eps).
```

No proof or citation for this dimension-free Markov theorem has been found.
Linear projection stability is false already in `ell_infty^3`, so the
square-root exponent is sharp if true. See
`agent-B/notes/near-positive-projection-stability-program.md`.

Several nontrivial classical facts are now proved:

- rank-one signed perturbations `P=I-u v^T` are `O(sqrt(delta))`-close to
  stochastic idempotents; this class contains the sharp Hume family
  (`agent-B/notes/rank-one-classical-stability.md`);
- exact signed affine retractions whose row polytope is a simplex are
  `O(sqrt(delta))`-close to stochastic idempotents with a universal constant
  independent of the number of vertices
  (`agent-B/notes/simplex-classical-stability.md`). The line-segment theorem
  is the two-vertex case (`agent-B/notes/line-segment-classical-stability.md`).
- bounded binary-coordinate dependencies are impossible at small defect:
  if rows `r_a` have distinct binary code words witnessed by affine functions
  `s_1,...,s_m:K->[0,1]`, then
  `||sum_a c_a r_a||_1 >= (1-C m sqrt(delta)) sum_a |c_a|`. In particular,
  exact parallelogram row polytopes and fixed-complexity non-simplex
  product-of-simplexes vertex geometries cannot occur for small `delta`
  when their factor coordinates are bounded on all of `K`
  (`agent-B/notes/parallelogram-classical-stability.md`).

The remaining non-simplex classical problem is reduced, for the simplex-based
route, to constructing `O(sqrt(delta))` approximate simplex coordinates for
row polytopes; see `agent-B/notes/approximate-simplexity-reduction.md`. The
bounded-coordinate lemma suggests a second route through angle-free
bounded-coordinate/dependency-cancellation decompositions.
The coordinate reduction is now robust to small signed coordinate errors:
`agent-B/notes/robust-approximate-simplexity-reduction.md` shows that it is
enough for the affine coordinate vectors to have coefficient negative mass
`O(delta)` and reconstruction error `O(sqrt(delta))`; exact pointwise
nonnegativity of the coordinates is not required.
Wegener's sidecar report
`agent-B/notes/subagent-exposed-redundant-classical-v0.1.md` sharpens the
remaining target further: well-exposed separated vertices satisfy an intrinsic
`l1` circuit-cancellation bound. The formal proof of the cancellation bound is
`agent-B/notes/exposed-circuit-cancellation.md`; the exposedness-modulus
local target is `agent-B/notes/exposed-redundant-dichotomy-target.md`.
Hubble's later stress test shows that a pointwise exposed-or-redundant
deletion lemma is not sufficient by itself: redundancy can be circular and
sequential deletion can accumulate error. The current non-accumulating target
is the global exposed-hull lemma in
`agent-B/notes/simultaneous-skeleton-reduction.md`: if
`W_{rho,kappa}` is the set of vertices exposed at
`rho=O(sqrt(delta))` with gap `kappa>=c sqrt(delta)`, then every row should be
`O(sqrt(delta))`-close to `conv W_{rho,kappa}`.
The branch where all row-polytope vertices are separated and well exposed is
now a proved stability case:
`agent-B/notes/well-exposed-classical-stability.md` shows the vertices must be
affinely independent, hence the row polytope is a simplex and the simplex
stability theorem applies.
The merge-compatible extension
`agent-B/notes/cluster-representative-classical-stability.md` proves stability
when well-exposed representative rows have disjoint clusters and all other
rows are `O(sqrt(delta))`-close to their convex hull. This removes the need
for global affine simplex coordinates in that subcase.
This row-polytope theorem has been packaged as an exact commutative
positive-map factorization theorem:
`agent-B/theory/classical-cluster-factorization-theorem.md` proves that an
almost-idempotent row-stochastic map whose spectral idempotent satisfies the
cluster-representative geometry factors, up to `O(sqrt(eta))`, through a
commutative special JB algebra by unital positive maps. It now also records
the corollary that the global exposed-hull hypothesis implies the same exact
factorization conclusion.

The target `J` should be special JB/JC. It is not reversible in general.
Decomposable factor maps require reversible/universally reversible target
structure or separate hypotheses.

## Theorem 4: Dilation-Compatible `O(eta)` Bridge

There is a valid Kitaev-strength theorem under a stronger lifted hypothesis.

Suppose there are:

- a finite-dimensional C*-algebra `D`;
- a unital order-isometric Jordan embedding `j:M_sa -> D_sa`;
- a unital positive map `C:D_sa -> M_sa`;
- `Phi=Cj`;
- `F=jC` extends to a UCP map `D -> D`;
- `||F^2-F||_cb <= eta`.

Then for

```text
P=theta(2Phi-I),        A=Im P,        a*b=P(a o b),
```

`A` is an `O(eta)` epsilon-JB order-unit algebra.

Status: proved by reduction to Kitaev's UCP theorem. See
`agent-B/notes/decomposable-dilation-compatible-theorem.md`.

This is **not** automatic from an arbitrary CP+coCP decomposition. The naive
doubled route fails: `Phi=Cj` can be exactly idempotent while `jC` has order-one
idempotence defect. See `agent-B/notes/decomposable-doubling-obstruction.md`.
Sartre also found that bad decompositions of the exact depolarizing projection
can have off-diagonal universal-envelope defect despite `eta=0`; see
`agent-B/notes/subagent-decomposable-alpha1-stress.md`.

## Theorem 5: Decomposable `O(eta)` Conjecture

Conjectural strengthening:

If `Phi` is unital positive, almost idempotent, and admits a controlled
CP+coCP decomposition

```text
Phi = Phi_0 + Psi_0 o tau,
Phi_0,Psi_0 CP,
Phi_0(1)+Psi_0(1)=1,
```

then the bridge in Theorem 2 improves from `O(sqrt(eta))` to `O(eta)`.

Status: open. The standard decomposable norm is the wrong hypothesis:
transpose on `M_n` is unital positive decomposable but has standard
Haagerup/Wittstock decomposable norm `n`. The component bounds above are the
right boundedness input, but not enough by themselves to justify the naive
doubled proof. A proof must either:

- choose a compatible decomposition/lift satisfying a lifted almost-idempotence
  estimate; or
- prove a direct intrinsic CP/coCP two-hole cancellation for the Jordan defect.

See `agent-B/notes/decomposable-alpha1-route.md`.

## Exact Consistency

When `eta=0`, `P=Phi` is a unital positive projection. Effros-Stormer applies:
`P(B(H)_sa)` is a JC algebra for

```text
r*s=P(r o s).
```

The stack above reduces to this exact result.
