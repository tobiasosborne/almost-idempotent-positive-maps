# Near-Positive Projection Stability Program

This is the cleanest remaining route to exact UP factor maps after the
algebraic bridge.

## Desired Theorem

There are universal constants `delta0,C` such that:

If `P:B(H)_sa -> B(H)_sa` is a unital idempotent linear map satisfying

```text
x>=0, ||x||<=1  =>  P(x) >= -delta 1,        delta<=delta0,
```

and perhaps also

```text
||P|| <= 1+C delta,
```

then there exists a unital positive idempotent

```text
E:B(H)_sa -> B(H)_sa
```

with

```text
||E-P|| <= C sqrt(delta).
```

The exponent `1/2` is sharp even in the classical `l_infty^3` case; linear
stability is false. For our application, `P=theta(2Phi-I)` has `delta=O(eta)`,
so this would match the algebraic `O(sqrt(eta))` bridge but cannot give a
Kitaev-strength `O(eta)` theorem for arbitrary positive maps.

## Why This Would Finish Factorization

If such `E` exists, exact Effros-Stormer gives a concrete JC algebra

```text
J=E(B(H)_sa)
```

with product `r*s=E(r o s)`. The maps

```text
Delta = inclusion_J_to_B(H)_sa,
Upsilon = E
```

are unital positive and

```text
||Delta Upsilon - Phi|| <= ||E-P|| + ||P-Phi||.
```

This bypasses:

- abstract positivity rounding, which is false at `O(epsilon)` in general;
- the need for Layer 1 to output concrete positive comparison maps;
- the cone perturbation constants that may depend on spin-factor dimension.

This implication is now written as a standalone conditional theorem in
`agent-B/theory/theorem-C-conditional-factorization.md`. Thus this program's
remaining task is the perturbative projection-stability estimate itself, not
the construction of the factor maps once a nearby positive idempotent is known.

## Known Non-Obstructions

Generic positivity-rounding failure does not refute this theorem. McClintock's
spin-factor counterexample gives approximately positive maps far from positive
maps, but it does not satisfy the idempotent/retraction constraint.

Pasteur checked the natural way to force that obstruction into an idempotent:
represent a spin factor `J` concretely, start from its positive trace projection
`E0`, and perturb by `K` with `K|_J=0`. The retraction condition saturates all
spin faces `p_a=(1+s_a)/2`; the hidden signed variation is then detected by
those faces, raising the positivity defect to the same scale as the distance to
`E0`. Thus the standard spin-factor obstruction does not produce an
instability example.

Classical stochastic searches also found no obstruction.

## Classical Subproblem

Prove first, at the sharp exponent:

If `P:l_infty^n -> l_infty^n` is unital idempotent and

```text
P([0,1]^n) subset [-delta,1+delta]^n,
```

then `P` is `C sqrt(delta)`-close in `l_infty -> l_infty` norm to a stochastic
idempotent.

Equivalent matrix language:

- rows of `P` are signed probability vectors with negative mass at most
  `delta`;
- `P^2=P`;
- find a row-stochastic idempotent `E` close to `P`.

The exact `delta=0` case is elementary: a unital norm-one projection on
`l_infty^n` is positive.

Hume found that no better power is possible. For

```text
v_s = (1, -1+s, -s),
u_s = (1-s+s^2, -s, 0)^T,
P_s = I-u_s v_s^T,
```

one has `P_s 1=1`, `P_s^2=P_s`, row negative mass `delta=s^2`, and distance
to the nearest stochastic idempotent

```text
2s-2s^2+2s^3 = 2 sqrt(delta)+O(delta).
```

See `agent-B/notes/subagent-classical-projection-stability.md`.

Thus the classical theorem, if true, must be a square-root theorem.

## Reduction To Markov Almost-Idempotents

Two sidecar checks reduced the classical theorem to a clean Markov-kernel
perturbation problem, but did not prove that problem.

Let `P` be a signed row-unital idempotent with row negative masses
`a_i<=delta`. For each row `mu_i`, set

```text
q_i = mu_i^+/(1+a_i).
```

The matrix `Q` with rows `q_i` is row-stochastic and

```text
||P-Q||_{infty->infty} <= 2 delta,
||Q^2-Q||_{infty->infty} <= 6 delta + 4 delta^2.
```

Therefore the desired classical projection-stability theorem follows from:

```text
Q row-stochastic, ||Q^2-Q||_{infty->infty} <= eps
  => dist(Q, stochastic idempotents) <= C sqrt(eps).
```

Conversely, applying spectral functional calculus to an almost-idempotent
stochastic `Q` gives a signed idempotent `P=theta(2Q-I)` with negative mass
`O(||Q^2-Q||)`. Thus the two formulations are equivalent up to universal
constants.

No primary-source perturbation theorem of this form has been found. Exact
classification/geometry sources include Blackwell's "Idempotent Markoff
chains" and later idempotent Markov-chain classification work; Heisenberg also
flagged Douglas's exact contractive-projection theorem for `L^1` and
Gonzalez-Torres's geometric study of cores of stochastic idempotents. These do
not supply the needed dimension-free `sqrt(eps)` perturbative estimate.

The Cesaro limit of `Q` is not the right idempotent in general: a slow two-state
chain is close to the identity idempotent but can be far from its limiting
rank-one ergodic projection. Any proof must choose metastable classes at scale
`sqrt(eps)`.

## Possible Proof Strategy

1. Use `delta`-positivity to show every row/state functional of `P` is close in
   total variation to a genuine probability measure.
2. Use idempotency to show the repaired probabilities are almost invariant for
   the repaired Markov kernel.
3. Convert the resulting almost-idempotent stochastic matrix to an idempotent
   stochastic matrix by Markov-chain perturbation. Hume's example shows this
   step necessarily loses a square root near boundary strata.
4. Lift the argument from commutative faces to matrix state spaces using
   exposed faces of the positive cone and Effros-Stormer support projections.

The difficult step is keeping constants dimension-free in steps 3 and 4.

## Exposed-Face Leakage Lemma

One new dimension-free ingredient is recorded at
`agent-B/notes/classical-affine-face-lemmas.md`.

For a row-stochastic `Q` with

```text
eps = ||Q^2-Q||_{infty->infty},
```

let `q_i` be its rows. If `phi` is any `1`-Lipschitz affine functional on the
simplex and `m=max_j phi(q_j)`, then

```text
sum_j q_i(j)(m-phi(q_j)) <= m-phi(q_i)+eps.
```

Thus a row in an `alpha`-exposed slice sends all but
`(alpha+eps)/gamma` of its mass into the `gamma`-exposed slice. With
`gamma=sqrt(eps)`, exposed faces are almost closed at the sharp square-root
scale. This explains the boundary scale but does not yet give the missing
dimension-free recursive rounding to a stochastic idempotent.

## Possible Noncommutative Route

Use the algebraic bridge already proved:

- `A=Im P` is an `O(sqrt(delta))` approximate JB algebra.
- If Layer 1 gives a nearby concrete JC algebra `J0 subset B(H)_sa`, let
  `E0` be the trace-preserving conditional expectation onto `J0`.
- Prove `||E0-P||` from the fact that both maps are idempotents with close
  ranges and both are nearly contractive/positive.

This may be easier than proving projection stability from scratch, but it
depends on a concrete Layer 1 theorem.

## Current Status

Open at exponent `1/2`. Linear stability is false even classically. The
standard spin-factor positivity-rounding obstruction does not directly apply to
idempotents.

The best current reduction is:

```text
near-positive signed idempotents at sqrt(delta)
  <=> almost-idempotent stochastic matrices at sqrt(eps).
```

Semialgebraic/local error bounds give no obvious dimension-free constant. A
fresh sidecar checked a multi-escape variant of Hume's boundary example and did
not find a dimension-growth obstruction, but this is evidence rather than a
proof.

Latest route refinement: `agent-B/notes/robust-approximate-simplexity-reduction.md`
shows that the simplex-coordinate reduction only needs coordinate vectors with
coefficient negative mass `O(delta)`, not exact pointwise positivity. Wegener's
sidecar report `agent-B/notes/subagent-exposed-redundant-classical-v0.1.md`
then reformulates the remaining non-simplex task as an
exposed-or-redundant vertex dichotomy. Well-exposed separated vertices obey an
`l1` circuit-cancellation estimate; the theorem-level proof is in
`agent-B/notes/exposed-circuit-cancellation.md`. The missing part is to prove
that every non-well-exposed vertex is
`O(sqrt(delta))`-redundant/mergeable.
The formal exposedness modulus and LP-dual target are recorded at
`agent-B/notes/exposed-redundant-dichotomy-target.md`.
The fully well-exposed separated case is now closed:
`agent-B/notes/well-exposed-classical-stability.md` proves that if all
vertices of the row polytope are separated and well exposed at the
square-root scale, then the vertices are affinely independent, the row
polytope is a simplex, and the simplex stability theorem gives a nearby
stochastic idempotent.
The merge-compatible version is
`agent-B/notes/cluster-representative-classical-stability.md`: if
well-exposed representative rows have disjoint clusters and every non-cluster
row is `O(sqrt(delta))`-close to the convex hull of the representatives, then
a stochastic idempotent is constructed directly. This avoids global affine
coordinate functions and prevents accumulation over merged vertices.

The cleanest formulation now is as affine retraction stability of the simplex:

```text
exact affine retraction P of R^n,
P(Delta_n) subset O(delta)-neighborhood of Delta_n
  => P is O(sqrt(delta))-close to an affine retraction of Delta_n.
```

See `agent-B/notes/markov-affine-retraction-formulation.md`.

## Proven Special Case: Rank-One Signed Idempotents

The sharp square-root theorem is proved for rank-one perturbations

```text
P = I - u v^T,        sum_j v_j=0,        v^T u=1.
```

After normalizing the positive and negative masses of `v` to both equal `1`,
the row negative-mass condition implies

```text
u_i(1-v_i^+) <= delta        if u_i>0,
(-u_i)(1-v_i^-) <= delta     if u_i<0.
```

Thus, above the threshold `sqrt(delta)`, there is at most one positive active
row and at most one negative active row. Rounding the inactive rows to identity
rows and the active coordinates to the corresponding transient or two-state
recurrent stochastic idempotent gives

```text
dist(P, stochastic idempotents) <= C sqrt(delta).
```

This includes Hume's sharp `3 x 3` family. See
`agent-B/notes/rank-one-classical-stability.md`.

## Proven Special Case: Simplex Row Polytope

The sharp square-root theorem is also proved for exact signed affine
retractions whose row polytope is a simplex, with a universal constant
independent of the number of vertices; see
`agent-B/notes/simplex-classical-stability.md`.

Let the simplex vertices be rows `r^1,...,r^m`, and write

```text
p_i=sum_a lambda_a(i) r^a,
lambda_a(i)>=0,        sum_a lambda_a(i)=1.
```

Idempotency at vertex `r^a` gives

```text
sum_j r^a_j lambda_b(j)=delta_ab,
```

and therefore

```text
sum_j r^a_j (1-lambda_a(j))=0.
```

Since `neg(r^a)<=delta`, the positive mass of `r^a` is concentrated on its
near-vertex slice `{lambda_a>=1-sqrt(delta)}`. These slices are disjoint.
Normalizing the positive restrictions of the vertices to their own slices gives
recurrent distributions `pi_a`; rounding rows already in a near-vertex slice
to `pi_a` and keeping all other rows as barycentric mixtures of the `pi_a`
gives a stochastic idempotent within `C sqrt(delta)`.

The line-segment theorem in
`agent-B/notes/line-segment-classical-stability.md` is the `m=2` case. The
general non-simplex row-polytope case remains open because there are no global
affine barycentric coordinates attached to all vertices.

## Approximate Simplexity Reduction

The remaining non-simplex problem is isolated in
`agent-B/notes/approximate-simplexity-reduction.md`.

Suppose the rows admit `gamma`-approximate simplex coordinates: selected row
vectors `r^a` and affine functions `lambda_a` such that

```text
0<=lambda_a(p_i)<=1,        sum_a lambda_a(p_i)=1,
lambda_a(r^a)=1,
||p_i-sum_a lambda_a(p_i)r^a||_1 <= gamma.
```

Then the same vertex-concentration argument as in the simplex proof gives a
stochastic idempotent `E` with

```text
||P-E||_{infty->infty} <= C (sqrt(delta)+gamma).
```

Therefore the full classical theorem would follow from an
`O(sqrt(delta))` approximate-simplexity lemma for row polytopes of
near-positive signed affine retractions. The exposed-face leakage lemma gives
local near-vertex candidates, but the unresolved issue is constructing a
global affine partition of unity without dimension, facet-angle, or
stratum-count losses.

Fermat's non-simplex probe reached the same obstruction from the exposed-face
side; see `agent-B/notes/subagent-non-simplex-classical-probe-v0.1.md`. For a
single exposed face, exact idempotency gives dimension-free leakage. But
localizing a non-simplex vertex requires intersecting several exposed slacks,
which introduces either a facet-count union bound or an inverse
angle/altitude loss. Moreover, macroscopic affine dependencies, such as a
parallelogram relation `r^1+r^3=r^2+r^4`, cannot be rounded by assigning every
vertex a disjoint recurrent class. A successful proof therefore needs an
angle-free approximate-simplexity/cancellation lemma: any macroscopic
non-simplex affine dependence must force negative mass larger than `O(delta)`,
or else the dependent vertices must be mergeable at `O(sqrt(delta))` scale.
