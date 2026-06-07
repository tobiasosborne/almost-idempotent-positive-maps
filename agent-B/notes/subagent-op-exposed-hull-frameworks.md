# Subagent H: Alternative Frameworks For `op-exposed-hull`

Date: 2026-06-07. Lane: Agent B exploration sandbox. Status: exploratory
strategy note, not a canonical proof shard.

## Restart Snapshot

Target:

```text
P1=1, P^2=P, neg(p_i)<=delta, tau=sqrt(delta), K=conv{p_i}.
```

For `rho=C0 tau` and `kappa=c0 tau`, let `W_{rho,kappa}` be the row vertices
whose exposedness modulus at scale `rho` is at least `kappa`.  Prove

```text
dist_1(p_i, conv W_{rho,kappa}) <= C tau
```

for every row.

Existing local reductions to keep in mind:

- `op-exposed-hull-mission-control.md`: global exposed hull implies the
  classical route.
- `subagent-op-exposed-hull-skeleton.md`: the clean maximal-skeleton target is
  a bad-kernel resolvent / closed-bad-class dichotomy.
- `subagent-op-exposed-hull-robust-coordinates.md`: robust coordinates are
  plausible, but blocked by an interpolation upgrade.
- `subagent-op-exposed-hull-lp-dual.md`: LP duals are explicit; failed
  exposedness gives small-positive-mass affine circuits but uncontrolled
  negative coefficients.
- `subagent-op-exposed-hull-stress-tests.md`: no counterexample found; dense
  polygon chains fail exact idempotency or have constant negative mass.

## Executive Verdict

The best current proof architecture is not pure convex geometry.  It is:

```text
maximal exposed skeleton
  + positive-coordinate Markov kernel from P^2=P
  + absorbing-chain resolvent
  + LP/game dual closed-class augmentation
  + oriented-circuit bookkeeping for the final contradiction.
```

The most promising next theorem is the **closed-bad-class augmentation lemma**:

```text
If a bad set B is O(tau)-closed under the repaired positive-coordinate kernel,
then B contains a new (rho,kappa)-well-exposed row vertex far from the current
skeleton.
```

If this lemma is false, the LP/game formulation below should produce the
counterexample.  If it is true, the existing resolvent certificate finishes the
global exposed-hull proof.

## Framework 1: Markov Recurrent-Class Theory

### Verdict

Primary route.  This framework exactly matches the good part of the skeleton
note: after repairing row signs, every bad row is almost a convex combination of
its positive-support successors.  The substochastic bad-to-bad block has a
fundamental matrix; either the expected bad lifetime is `O(1/tau)`, or a
nearly closed recurrent class appears.  That is the right non-accumulation
language.

### Translation

For each row, write

```text
a_i=neg(p_i),       q_i=p_i^+/(1+a_i).
```

Then `q_i` is stochastic and right-fixity gives

```text
||p_i - sum_j q_i(j) p_j||_1 <= C delta.        (PC)
```

Given a candidate exposed skeleton `R`, define bad rows

```text
B={i : dist_1(p_i,conv R)>A tau}
```

with `rho`-cluster enlargement.  Let `T=q|_{B x B}` and let
`s_i=q_i(B^c)`.

The exact absorbing-chain identity is

```text
N=(I-T)^(-1)=sum_{m>=0} T^m,
N s <= 1,
```

whenever the bad chain exits almost surely.  If

```text
||N||_{infty->infty} <= L,
```

then the skeleton note proves

```text
dist_1(p_i,conv R) <= Gamma + C L delta.
```

Thus `L <= C/tau` is enough.

### Lemma Chain

M1. Positive-coordinate reconstruction.

```text
For every i, q_i is stochastic and (PC) holds with universal C.
```

This is already essentially proved in the skeleton/LP notes.

M2. Bad fundamental-matrix certificate.

```text
If rows outside B are Gamma-close to conv R and
||(I-T)^(-1)||_{inf->inf} <= L, then all rows in B are
Gamma + C L delta-close to conv R.
```

This is the smallest formalisable lemma from this framework.

M3. Long lifetime implies quasi-stationary bad measure.

```text
If ||(I-T)^(-1)||_{inf->inf} > C/tau, then there is a probability mu on B
such that
  mu T >= (1-c tau) mu
or
  ||mu - mu T||_1 <= c tau
after a harmless normalization.
```

This is Perron-Frobenius / Collatz-Wielandt for the substochastic block.

M4. Quasi-stationary bad measure gives an almost-invariant convex point.

```text
y=sum_i mu_i p_i satisfies
dist_1(y, conv{p_j:j in B})=0 and
dist_1(yP, y) <= C tau + C delta.
```

Since all rows are exactly fixed by `P`, this should be sharpened to a
statement about signed coordinate leakage rather than point motion.  The useful
output is not `yP=y` but that the positive-coordinate mass has little exit.

M5. Closed bad class augmentation.

```text
If B is c tau-closed under q and every row in B is farther than A tau from
conv R, then some row vertex w in B satisfies e_w(rho)>=kappa.
```

This is the real open lemma.  Prove it with the LP/game or oriented-circuit
frameworks below.

### Failure Mode

Markov theory alone only says a long-lived closed class exists; it does not
explain why a closed class must have a well-exposed vertex.  Dense polygons are
exactly the convex-geometry warning.  The missing ingredient is that the kernel
is not arbitrary: it comes from signed idempotent rows with negative mass
`<=delta`.

### Literature Pointers

- Blackwell, "Idempotent Markoff chains", Annals of Mathematics 43 (1942),
  560-567.  Useful exact-idempotent background, not a perturbation theorem.
- Schwarz, "On the Structure of the Semigroup of Stochastic Matrices" (1964).
  Exact stochastic semigroup/idempotent structure.
- Standard absorbing-chain fundamental matrix: `N=(I-Q)^(-1)` records expected
  visits before absorption.  This is exactly the resolvent quantity in M2.

## Framework 2: Lyapunov / Drift

### Verdict

Primary route, equivalent to Framework 1 but more proof-friendly for constants.
Instead of bounding a matrix inverse directly, construct a height function on
bad rows with uniform positive drift to the good set.  This may be easier to
derive from separators.

### Translation

Need a function

```text
H:B -> [0,1/tau]
```

such that for each bad row

```text
H(i) >= 1 + sum_{j in B} q_i(j) H(j) - C
```

or, more simply,

```text
E_q[H(next)-H(i) | i] <= -c
```

until the chain exits.  Then optional stopping gives expected bad lifetime
`O(1/tau)`, which plugs into M2.

### Lemma Chain

L1. Separator height.

```text
For a row i far from conv R, choose an l_infty separator phi_i of
p_i from conv R and normalize h_i=max_B phi_i - phi_i.
```

This is local and not enough by itself.

L2. Common height or potential.

```text
There is a single affine functional phi separating all bad rows from conv R
up to O(tau), or else the bad set splits into smaller face-lattice classes.
```

If true, the drift proof is clean: failure of drift means a high plateau.

L3. Plateau augmentation.

```text
If a phi-high plateau is c tau-closed under q, then a maximal phi row in the
plateau is (rho,kappa)-well-exposed.
```

This is the same hard content as M5, but expressed as drift obstruction.

### Failure Mode

A single separator for one bad row may not control the whole bad set.  Multiple
separators can cycle.  Acyclicity without escape is too weak, because path
length can depend on the number of rows.

### Concrete Next Test

Use existing LP data to compute the value

```text
V(i)=dist_1(p_i,conv R)
```

and test whether

```text
V(i) <= C delta + sum_j q_i(j) V(j)
```

is nearly sharp on random exact signed idempotents.  If sharp cases have long
lifetime, inspect their maximizers for exposed vertices.

## Framework 3: LP / Farkas / Hoffman Error Bounds

### Verdict

Primary analytic certificate route.  Generic Hoffman bounds are not enough
because their constants depend on angles.  But the exact LP duals already found
the right obstruction.  The target should be a *structured* Hoffman theorem for
the joint system consisting of:

```text
P1=1, P^2=P, neg rows<=delta,
failed exposedness for all bad rows,
bad closedness under q,
row far from conv R.
```

### Known Dual Inputs

Failed exposedness at a vertex `v` gives a signed affine circuit

```text
sum_{j outside rho(v)} mu_j (p_j-v)
  = sum_i (beta_i-alpha_i)(p_i-v),
sum_i beta_i < kappa,
alpha_i,beta_i >= 0.
```

Distance from `v` to `conv W` gives a separator

```text
phi(v) >= sup_{w in W} phi(w) + A tau,
||phi||_infty <= 1.
```

The uncontrolled term is `sum alpha_i`.  Any successful Hoffman/Farkas proof
must use right-fixity and negative-mass bounds to control or eliminate this
negative side.

### Lemma Chain

H1. Joint infeasibility theorem.

```text
For constants R,k,A, the following finite system is infeasible for small delta:
  - signed idempotent row equations;
  - neg(p_i)<=delta;
  - a bad closed class B under q with exit <= c tau;
  - every row vertex in B has e_v(R tau)<k tau;
  - B is farther than A tau from the current exposed skeleton.
```

H2. Quantitative infeasibility margin.

```text
The infeasibility in H1 has a dual certificate whose coefficients are bounded
by universal constants or by O(1/tau), never by dimension.
```

H3. Structured Hoffman conversion.

```text
If the system is violated by O(delta), then one of:
  - a row is O(tau)-close to conv R;
  - a new exposed vertex exists;
  - neg(p_i)>delta for some i.
```

H4. Extract human-readable certificate.

```text
Dual multipliers reduce to either the Markov resolvent certificate M2 or the
closed-class augmentation lemma M5.
```

### Computational Plan

1. Build the A5 joint feasibility model for small `n` using exported LP files
   and `gurobi_cl` or SciPy HiGHS.
2. Fix a candidate skeleton `R` and a bad set `B`; impose affine coordinates
   rather than vertex enumeration where possible.
3. Search for feasible bad closed classes with `delta` small and
   `rho=R tau`, `kappa=k tau`.
4. If infeasible, export the dual certificate and simplify it into H1-H4.
5. If feasible, rationalize the instance with SymPy and save it as a
   counterexample candidate under `agent-B/experiments/op-exposed-hull/`.

### Literature Pointers

- Hoffman, "On approximate solutions of systems of linear inequalities"
  (1952), the original error-bound theorem.
- Robinson, perturbed linear-program solution-set bounds, Linear Algebra and
  Applications 6 (1973), useful for sensitivity but angle-dependent.
- Modern Hoffman-constant papers are useful for algorithms, but not directly
  canonical unless the structured constant is proved here.

## Framework 4: Game / Minimax / Approachability Duality

### Verdict

Primary computational-discovery route and possibly the cleanest exposition for
the closed-class lemma.  It packages the obstruction as a zero-sum game:
separator chooses a direction, the non-exposed row chooses a far outside
barycenter, and the Markov kernel chooses a positive-support successor.

### Game Form

Let the skeleton `R` be fixed.  Consider a bad row `v`.

Player S chooses a separator `phi` with `||phi||_infty<=1` and
`phi <= 0` on `conv R`.

Player E, witnessing non-exposedness of the current maximizer `u`, chooses
a probability measure on rows outside `B_rho(u)` such that

```text
phi(y) >= phi(u)-O(kappa).
```

Player M moves by the positive-coordinate kernel `q_u`.

The desired theorem says this game cannot stay in the bad region for expected
time greater than `O(1/tau)` unless it creates a well-exposed maximizer.

### Lemma Chain

G1. Separator propagation game.

```text
If dist(v,conv R)>A tau, then there is a separator phi.  If the phi-maximal
bad row u is not well-exposed, non-exposedness produces a rho-separated row
y with phi(y)>=phi(u)-O(kappa).
```

This is already in the LP-dual note.

G2. Strategy-to-kernel compatibility.

```text
If the game can keep phi-height within O(kappa) while moving rho-separatedly,
then the repaired positive-coordinate kernel has a bad closed class.
```

G3. Closed-class game contradiction.

```text
A closed class that admits a no-drop separator strategy has a row vertex with
exposedness >= kappa.
```

This is M5 again, but the minimax statement may make the proof shorter.

### Failure Mode

Blackwell approachability-style theorems control averages over time, while this
problem needs a one-step exposed vertex or an `O(1/tau)` resolvent.  The game
must keep the exact row-fixity identities visible; otherwise it degenerates
into generic convex geometry.

### Next Subagent Task

Write the finite zero-sum matrix game for a fixed candidate bad set:

```text
value(B,R)=inf_{exit/drift certificates} sup_{bad rows and separators}
           expected bad lifetime * delta + separator violation.
```

Then compare the dual variables with the A5 LP certificate.

## Framework 5: Oriented Matroids / Affine Circuits

### Verdict

Strong auxiliary framework, not a standalone proof.  It is the right language
for the final contradiction after the Markov/LP step produces many local
failed-exposedness circuits.  It also explains why small-dimensional examples
collapse to simplex or exposed quadrilateral cases.

### Translation

Rows form an affine oriented matroid through their signed circuits:

```text
sum_i c_i p_i=0,       sum_i c_i=0.
```

Well-exposed separated representatives have no small circuit by
`exposed-circuit-cancellation.md`:

```text
||sum_a c_a r^a||_1 >= (1-C tau) sum_a |c_a|.
```

Thus any obstruction must live inside the non-well-exposed bad class and must
involve circuits whose positive side is almost supported in the bad class.

### Lemma Chain

O1. Circuit extraction from non-exposedness.

```text
For each non-well-exposed bad vertex v, extract a signed affine circuit C_v
whose positive part outside the rho-neighborhood has total mass 1 and whose
opposite positive coefficient mass is < kappa.
```

This is the LP-dual circuit lemma, rewritten oriented-matroid style.

O2. Circuit elimination along closed bad class.

```text
In a q-closed bad class with no exposed vertex, eliminate the local circuits
to obtain one affine circuit supported on rho-separated bad vertices with
positive side mass bounded below but signed-row negative mass only O(delta/tau).
```

O3. Negative-mass lower bound for separated bad circuits.

```text
Any rho-separated affine circuit inside rows of an exact signed retraction
forces max_i neg(p_i) >= c rho^2.
```

At `rho=C tau`, this becomes `>= c C^2 delta`.  Choosing constants may
contradict `neg<=delta`.

### Why This Is Plausible

Small-case exploration found exactly this pattern: quadrilateral circuits are
either collapsed at `O(tau)` scale or quantitatively exposed.  Dense polygon
circuits can evade pointwise deletion, but exact idempotency gives constant
negative mass or large idempotency defect.

### Failure Mode

General oriented-matroid theorems are qualitative and combinatorial.  They do
not see the quantitative `l1` norm, the row coordinate signs, or `P^2=P`.
Circuit elimination can blow up coefficients unless the Markov closed-class
or LP dual supplies normalization.

### Literature Pointers

- Oriented-matroid convexity and affine circuits are useful vocabulary.
- Ziegler/standard polytope references give face-lattice and normal-fan
  language, but not the quantitative estimate needed here.

## Framework 6: Barycentric Spanners

### Verdict

Secondary route and likely not enough.  Barycentric spanners guarantee bounded
linear coordinates for finite-dimensional convex bodies, but the bound normally
depends on dimension or on a spanner constant unrelated to `delta`.  The
robust-coordinate note shows the exact target is much stronger:

```text
coordinate negative mass <= O(delta), reconstruction error <= O(tau).
```

### Useful Part

Barycentric spanner algorithms can help choose a stable representative set and
diagnose coordinate blow-up.  They may also be useful for computing candidate
robust coordinates in the LP route.

### Lemma Chain If Revived

B1. Exposed skeleton is an almost-1-barycentric spanner.

```text
Separated well-exposed rows R satisfy
||sum_a c_a r^a||_1 >= (1-C tau) sum_a |c_a|.
```

This is already exposed-circuit cancellation.

B2. Rowwise reconstruction implies coordinate positivity improvement.

```text
If every row is O(tau)-close to conv R and R satisfies B1, then the
barycentric coordinates of the best affine projection have negative mass
O(delta), not merely O(tau).
```

This is exactly the robust-coordinate interpolation upgrade and is currently
open.

B3. Coordinate reduction.

```text
B1+B2 feed robust-approximate-simplexity-reduction and produce a stochastic
idempotent.
```

### Failure Mode

The robust-coordinate probe found regular polygons and thin rectangles with
constant coordinate negative mass in generic convex geometry.  Exact signed
retraction constraints may remove these examples, but barycentric spanners do
not encode those constraints automatically.

### Literature Pointer

Awerbuch-Kleinberg barycentric spanners are useful algorithmic vocabulary for
bounded-coordinate bases, but their generic guarantees are too weak for the
`O(delta)` negativity target.

## Framework 7: Helly / Caratheodory / Approximate Caratheodory

### Verdict

Mostly packaging, not a proof route.  These theorems reduce support size or
intersection witnesses, but they generally introduce dimension dependence or
ignore the row-fixity identities.  Approximate Caratheodory is dimension-free
in some Banach norms, but it approximates points already in a convex hull; it
does not identify the correct exposed hull.

### Possible Uses

C1. Support-size cleanup.

```text
After proving p_i is O(tau)-close to conv W, use approximate Caratheodory only
to replace a large convex combination by a small support combination if needed.
```

C2. LP dual compression.

```text
Any separating witness or failed-exposedness barycenter can be represented with
small support for computational search in fixed small examples.
```

C3. Helly certificate for infeasibility.

```text
If the A5 joint system is infeasible, Helly gives a finite subsystem witness.
```

This does not give dimension-free constants by itself, but it can make
computer-mined certificates human-readable.

### Failure Mode

The open theorem is dimension-free in the number of rows and affine dimension.
Generic Helly/Caratheodory bounds scale with dimension.  Dimension-free
approximate versions lose the exact exposedness and sign structure.

## Framework 8: Face Lattices / Normal Fans

### Verdict

Useful local organization, not a standalone proof.  A closed bad class should
live on a face or high plateau of a separator.  Face-lattice language can turn
"not well exposed" into "the normal cone is too thin at scale rho", but it
does not explain why signed idempotency forbids a long necklace of thin normal
cones.

### Lemma Chain

F1. Separator face reduction.

```text
Given p_i far from conv R, choose a separator phi and let F be the high face
or high plateau of K above sup_R phi + A tau/2.
```

F2. High-face inheritance.

```text
If q_i is c tau-closed in bad rows, then the q-successors of a phi-maximal row
remain in the high face up to O(tau).
```

F3. Face-local augmentation.

```text
Inside a minimal closed high face F, either diam(F)<=rho and a vertex of F is
well exposed, or F contains a smaller bad face closed under q.
```

F4. Termination by drift, not by face count.

```text
The descent through faces must come with exit probability >= c tau, otherwise
face count can depend on n.
```

### Failure Mode

A pure face-lattice descent can take many steps.  It must be tied to the
Markov resolvent or Lyapunov drift to avoid dimension dependence.

## Framework 9: Pure Convex Geometry / Exposed-Redundant Dichotomy

### Verdict

Dead as a standalone route.  It remains useful as a source of local lemmas but
cannot handle accumulation.

### Reason

Regular polygons show that pointwise redundancy can be circular: each vertex
is close to the hull of nearby vertices, yet no simultaneous exposed skeleton
is produced by sequential deletion.  These polygons are not counterexamples to
the signed-retraction theorem, but they disprove the logic of pure pointwise
convex deletion.

### Salvage

Use pure convex geometry only after inserting one of:

```text
resolvent bound,
Lyapunov drift,
structured LP certificate,
or signed affine-circuit lower bound.
```

## Framework 10: Exact Stochastic Idempotent Semigroup / Core Geometry

### Verdict

Background and endpoint checking.  The exact positive idempotent structure is
well understood: rows collapse onto recurrent classes with fixed stationary
rows, and transient rows are convex combinations of recurrent rows.  This is
precisely what the cluster-representative theorem constructs.

### Use

S1. Endpoint normal form.

```text
Any stochastic idempotent E has recurrent row classes with rows pi_a and every
other row in conv{pi_a}.
```

S2. Compare candidate construction.

```text
The output of cluster-representative-classical-stability has exactly this
normal form.
```

S3. Perturbative warning.

```text
Existing semigroup/core literature describes exact stochastic idempotents, but
does not appear to provide dimension-free signed perturbation bounds.
```

### Literature Pointers

- Gonzalez-Torres, "A geometric study of cores of idempotent stochastic
  matrices", Linear Algebra and its Applications 527 (2017), 87-127.
- Schwarz (1964) and Blackwell (1942), exact stochastic/idempotent structure.
- Agaev-Chebotarev regularized power limits may be useful for exact endpoints
  of a nearby stochastic matrix, but no direct `O(sqrt(delta))` perturbation
  theorem was found.

## Consolidated Proof Plan

The frameworks above point to one concrete proof stack.

### Stage 1: Maximal Skeleton Setup

Choose `R` maximal `4rho`-separated in `W_{rho,kappa}`.  Let

```text
C_R=conv R,
B={row vertices p_i : dist_1(p_i,C_R)>A tau},
```

enlarged by `rho`-clusters so that rows near bad rows are also tracked.

Goal:

```text
B is empty.
```

### Stage 2: Positive-Coordinate Kernel

For every row define `q_i=p_i^+/(1+neg(p_i))`.  Prove (or import from existing
notes):

```text
||p_i - sum_j q_i(j)p_j||_1 <= C delta.
```

### Stage 3: Resolvent Alternative

Let `T=q|_{B x B}`.

If

```text
||(I-T)^(-1)||_{inf->inf} <= C/tau,
```

then all bad rows are `O(tau)` from `C_R`, contradiction.

So assume the opposite.  Extract a quasi-closed probability measure or closed
bad subclass `B0`:

```text
q_i(B0) >= 1-c tau
```

in the averaged or pointwise sense needed by the next stage.

### Stage 4: Closed-Class Augmentation

Prove:

```text
If B0 is c tau-closed under q and all its vertices are farther than A tau
from C_R, then B0 contains a row vertex w with e_w(rho)>=kappa.
```

Since `w` is far from `R`, this contradicts maximality of `R`.

This is the central open lemma.

### Stage 5: Prove Stage 4 By LP/Game + Circuits

Assume no vertex in `B0` is well exposed.  For each bad vertex extract the
failed-exposedness circuit.  Combine these circuits using the quasi-stationary
measure from Stage 3.  Show that either:

```text
positive circuit mass leaks outside B0 by >= c tau,
```

contradicting closedness, or:

```text
there is an affine circuit among rho-separated bad rows whose signed
idempotent realization forces neg(p_i)>delta.
```

This is where oriented-matroid bookkeeping and Hoffman/Farkas certificates
should meet.

## Subagent Delegation Plan

H1-Markov:

```text
Write a self-contained proof of M2 and M3 with explicit constants, including
the pointwise/averaged conversion from large resolvent to a quasi-closed bad
subclass.
```

H2-ClosedClass-LP:

```text
Build the joint A5 feasibility LP for fixed small n,B,R and mine dual
certificates for the closed-class augmentation lemma.
```

H3-Circuit:

```text
Starting from failed-exposedness circuits and a quasi-stationary bad measure,
derive a normalized global affine circuit.  Test whether negative-mass lower
bound O(rho^2) is true.
```

H4-Drift:

```text
Try to construct a Lyapunov height from separator plateaus.  Either prove
expected bad lifetime O(1/tau) or identify the exact plateau obstruction.
```

H5-SmallCases:

```text
Finish n=4 corank-one 2|2 quadrilateral symbolics.  Extract the inequality
that says collapse-to-simplex or all vertices exposed.
```

H6-RobustCoordinate:

```text
Implement the Candidate 3 coordinate LP.  Decide whether exact interpolation
with coefficient negative mass O(delta) is feasible in all mined examples.
```

H7-Lit:

```text
Acquire and locally cache Blackwell, Schwarz, Gonzalez-Torres, Hoffman,
Robinson, and Awerbuch-Kleinberg if any are used beyond scouting.  Search
specifically for perturbation theorems for stochastic idempotents, polyhedral
Markov projections, and finite-chain fundamental-matrix stability.
```

## Current Best Bet

The fastest path to a rigorous proof is:

```text
M2 + M3  ->  closed bad subclass
closed bad subclass + LP circuit averaging  ->  new exposed vertex
maximality  ->  B empty
cluster-representative theorem  ->  stochastic idempotent
```

The biggest risk is Stage 4.  If the closed-class augmentation lemma fails,
the counterexample should already appear as a small rational A5 feasible model
or as a long-lived exact signed idempotent generated by the computational
search.  Existing Hume, polygon, cube, random-similarity, and small-case tests
do not show such a counterexample.

## Web-Scout Notes

These are not canonical sources.  Any final citation must be pulled into
`refs/` and byte-checked.

- Blackwell, "Idempotent Markoff chains", Annals of Mathematics 43 (1942),
  560-567, DOI `10.2307/1968811`.
- Schwarz, "On the Structure of the Semigroup of Stochastic Matrices",
  Magyar Tud. Akad. Mat. Kutato Int. Kozl. 9 (1964), 297-311.
- Gonzalez-Torres, "A geometric study of cores of idempotent stochastic
  matrices", Linear Algebra and its Applications 527 (2017), 87-127,
  DOI `10.1016/j.laa.2017.03.032`.
- Agaev-Chebotarev, "The Projection Method for Reaching Consensus and the
  Regularized Power Limit of a Stochastic Matrix", arXiv:1109.3948.
- Hoffman, "On approximate solutions of systems of linear inequalities",
  Journal of Research of the National Bureau of Standards 49 (1952), 263-265.
- Awerbuch-Kleinberg, "Online linear optimization and adaptive routing",
  Journal of Computer and System Sciences 74 (2008), 97-114, for barycentric
  spanner vocabulary.
