# op-exposed-hull Mission Control

Date: 2026-06-07.  Lane: Agent B exploration sandbox.  Do not treat this as a
canonical proof shard.

## Restart protocol

After compaction, read this file first, then:

1. `PRD.md`, `CLAUDE.md`, `HANDOFF.md`;
2. `argument/lemmas/op-exposed-hull.md`;
3. `agent-B/notes/simultaneous-skeleton-reduction.md`;
4. `agent-B/notes/exposed-circuit-cancellation.md`;
5. `agent-B/notes/cluster-representative-classical-stability.md`;
6. `agent-B/notes/robust-approximate-simplexity-reduction.md`;
7. latest files in `agent-B/experiments/op-exposed-hull/`.

Keep all exploration in `agent-B/**` or dated `docs/plans/**`.  Do not edit
`argument/`, `definitions/`, `proofs/`, or `report/` until a proof is ready for
Agent A review and the Recipe A/B pipeline.

## Target

Let `P` be an exact signed affine retraction:

```text
P1 = 1,        P^2 = P,        neg(p_i) <= delta
```

for every row `p_i`, and set `tau = sqrt(delta)`, `K = conv{p_i}`.  For
`rho = C tau`, `kappa = c tau`, let `W_{rho,kappa}` be the row vertices of `K`
whose exposedness modulus at scale `rho` is at least `kappa`.

The target `op-exposed-hull` is:

```text
dist_1(p_i, conv W_{rho,kappa}) <= C' tau
```

for every row, with universal constants.  The existing cluster-representative
theorem then gives a stochastic idempotent within `O(tau)`.

## Non-negotiable reductions already established

- Sequential pointwise deletion is not enough; it can accumulate.
- The proof must produce a simultaneous skeleton, global exposed hull, acyclic
  contraction certificate, or robust coordinate certificate.
- Generic convex geometry is insufficient.  The proof has to use both:
  `P^2=P`, i.e. every row is fixed by right multiplication by `P`, and
  `neg(p_i)<=delta`.
- The sharp scale is `tau=sqrt(delta)` by Hume's example.

## Workstreams

## Multisession orchestration update - 2026-06-07

`bd create` is currently blocked in this clone by missing `issue_prefix`
configuration, so this mission-control file is the durable task ledger until
beads is repaired.  Keep each subagent deliverable in a separate
`agent-B/notes/subagent-op-exposed-hull-*.md` file and put reproducible code
or data under `agent-B/experiments/op-exposed-hull/`.

Subagent roster:

- A: LP-dual analytic attack.  Active deliverable:
  `agent-B/notes/subagent-op-exposed-hull-lp-dual.md`.  Verdict:
  inconclusive; exact Farkas dual found; uncontrolled negative dual mass is
  the blocker.
- B: maximal-skeleton augmentation and no-accumulation certificates.  Active
  deliverable: `agent-B/notes/subagent-op-exposed-hull-skeleton.md`.
  Current target: positive-coordinate resolvent bound `||(I-T)^(-1)||<=C/tau`
  or an augmenting exposed vertex.
- C: robust-coordinate route with coefficient negative mass `O(delta)`.
  Active deliverable:
  `agent-B/notes/subagent-op-exposed-hull-robust-coordinates.md`.  Current
  data: `agent-B/experiments/op-exposed-hull/robust_coordinate_probe.*`.
  Hard target: upgrade a reconstruction kernel from representative Gram
  matrix `I+O(tau)` to `I+O(delta)` without introducing `O(tau)` negativity.
- D: computational falsification and dual-certificate mining by LP/MILP/CAS.
  Current code and outputs: `agent-B/experiments/op-exposed-hull/`, plus
  `subagent-op-exposed-hull-computational.md`,
  `subagent-op-exposed-hull-small-cases.md`, and
  `subagent-op-exposed-hull-stress-tests.md`.  No serious counterexample found;
  next targets are a joint feasibility model for LP-dual certificate A5 and a
  direct exact-retraction parameterization `P=A B`, `B A=I`, `P1=1`.
- E: deep literature search for near-idempotent stochastic matrices, affine
  retracts of simplices, polytope skeleton selection, and exposed-point
  stability.  Active deliverable:
  `agent-B/notes/op-exposed-hull-literature-scout-2026-06-07.md`.  Any source
  useful for canonical work must be proposed for local `refs/` acquisition and
  byte verification.
- F: formalization packaging once a proof skeleton survives A-D.
- H: alternative proof frameworks.  Active deliverable:
  `agent-B/notes/subagent-op-exposed-hull-frameworks.md`.  Best current stack:
  maximal exposed skeleton -> positive-coordinate Markov kernel -> resolvent
  alternative -> closed-bad-class augmentation -> LP/game/circuit contradiction.
  Central open lemma: a `c tau`-closed bad class under the repaired
  positive-coordinate kernel contains a new `(rho,kappa)`-well-exposed row
  vertex far from the current skeleton.
- H: alternative proof frameworks.  Active deliverable:
  `agent-B/notes/subagent-op-exposed-hull-frameworks.md`.  Verdict:
  strongest architecture is maximal exposed skeleton + positive-coordinate
  Markov resolvent + LP/game closed-class augmentation + oriented-circuit
  bookkeeping; pure convex geometry alone is not enough.

### A. LP-dual proof of global exposed hull

Goal: write the contrapositive

```text
dist_1(v, conv W) > A tau  =>  e_v(rho) >= c tau
```

as a finite-dimensional LP/Farkas statement.  Identify the exact dual witness
for failure and combine it with right-fixity

```text
v = sum_j v_j p_j
```

to force either a new exposed vertex or a reconstruction by `conv W`.

Deliverables:
- normalized primal and dual LPs;
- lemma candidates with constants;
- a proof or a minimal obstruction instance.

### B. Maximal-skeleton augmentation

Goal: take a maximal separated set `R` of well-exposed vertices and prove every
row is close to `conv R`, or find a rule that augments `R` by a new well-exposed
representative.

Deliverables:
- a one-shot augmentation lemma;
- an acyclic/contraction certificate if augmentation is iterative;
- comparison to regular polygon and Hume stress tests.

Current refinement: naive augmentation is too weak.  The useful dichotomy is a
**bad-kernel resolvent / closed-bad-class** alternative.  Repair each signed row
by

```text
q_i = p_i^+ / ||p_i^+||_1 .
```

Then right-fixity gives

```text
||p_i - sum_j q_i(j) p_j||_1 <= C delta.
```

For a bad set `B` far from `conv R`, let `T=(q_i(j))_{i,j in B}`.  If

```text
||(I-T)^(-1)||_{infty->infty} <= C/tau,
```

then bad rows reconstruct from the good hull with total error
`O(delta/tau)=O(tau)`.  So the hard alternative is: if the bad kernel is nearly
closed for longer than `1/tau`, then the closed bad class must contain a new
`(rho,kappa)`-well-exposed vertex, contradicting maximality of `R`.

### C. Robust-coordinate route

Goal: construct affine coordinates on selected representatives with coefficient
negative mass `O(delta)` and reconstruction error `O(tau)`, then invoke the
robust approximate-simplexity reduction.

Deliverables:
- coordinate construction;
- bound on coordinate negative mass;
- failure examples if coordinate negativity is only `O(tau)`.

Current refinement: pushing canonical row coordinates through a probability
kernel to representatives gives coefficient negative mass `<=delta` for free,
but only an approximate representative interpolation matrix

```text
G = I + O(tau).
```

Exactifying by `G^{-1}` appears to introduce `O(tau)` coefficient negativity,
which is too large.  The hard subtarget is an **interpolation upgrade**:
construct the reconstruction kernel with `G=I+O(delta)` while keeping
row-reconstruction error `O(tau)`, or prove that this route cannot close.

### D. Computational search and falsification

Goal: use LP/MILP/nonlinear optimization to either find counterexamples to the
global exposed-hull statement or infer the correct hidden certificate.

Tasks:
- exact small-`n` enumeration of idempotent signed affine retractions;
- optimize worst-case distance to `conv W`;
- compute exposedness moduli by LP;
- stress Hume products, regular polygons with retraction constraints, random
  rank-`r` projections, and high-vertex polytopes;
- export reproducible JSON/CSV with code hashes.

### E. Literature search

Goal: find external tools for near-idempotent stochastic matrices, affine
retractions of simplices, Markov chain perturbation to idempotents, convex
geometry of exposed points, approximate retracts, and polytope skeleton
selection.

Every useful source must be proposed for local `refs/` acquisition before it can
support canonical claims.

### F. Formalization packaging

Goal: once A-D produce a plausible proof, split it into small contracts suitable
for Agent A formalization and `af`.

Likely contracts:
- LP dual witness for non-exposed vertex.
- Right-fixity converts witness into mass concentration or reconstruction.
- Maximal well-exposed skeleton reconstructs all rows.
- `op-exposed-hull` capstone.

## Current orchestration snapshot

Spawned subagents should report into this mission-control thread with:

```text
Verdict: proof / counterexample / inconclusive
Artifacts: paths changed or scripts run
Constants: explicit parameter choices
Failure modes: what broke
Next handoff: the next most concrete task
```

Do not rely on memory-only results.  Numerical evidence needs commands, seeds,
and output artifacts under `agent-B/experiments/op-exposed-hull/`.
