# op-exposed-hull Mission Control

Date: 2026-06-07.  Lane: Agent B exploration sandbox.  Do not treat this as a
canonical proof shard.

## Restart protocol

After compaction, read this file first, then:

1. `PRD.md`, `CLAUDE.md`, `HANDOFF.md`;
2. `docs/plans/2026-06-07-op-exposed-hull-attack-plan.md`;
3. `argument/lemmas/op-exposed-hull.md`;
4. `agent-B/notes/simultaneous-skeleton-reduction.md`;
5. `agent-B/notes/exposed-circuit-cancellation.md`;
6. `agent-B/notes/cluster-representative-classical-stability.md`;
7. `agent-B/notes/robust-approximate-simplexity-reduction.md`;
8. latest files in `agent-B/experiments/op-exposed-hull/`.

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
- B: maximal-skeleton augmentation and no-accumulation certificates.
  Deliverables: `agent-B/notes/subagent-op-exposed-hull-skeleton.md` and
  `agent-B/notes/subagent-op-exposed-hull-bad-kernel.md`.  Current state:
  the resolvent half is proof-ready,
  `dist_1(p_i,conv R) <= Gamma + 4 delta ||(I-T)^(-1)||_{inf->inf}`.
  The remaining hard target is closed-bad-class/high-face augmentation.
- C: robust-coordinate route with coefficient negative mass `O(delta)`.
  Deliverables: `agent-B/notes/subagent-op-exposed-hull-robust-coordinates.md`
  and `agent-B/notes/subagent-op-exposed-hull-interpolation-upgrade.md`.
  Current target: construct one stochastic kernel `U` with row reconstruction
  `O(tau)` and representative interpolation row-l1 defect `O(delta)`.
- D: computational falsification and dual-certificate mining by LP/MILP/CAS.
  Current code and outputs: `agent-B/experiments/op-exposed-hull/`, plus
  `subagent-op-exposed-hull-computational.md`,
  `subagent-op-exposed-hull-small-cases.md`, and
  `subagent-op-exposed-hull-stress-tests.md`.  No serious counterexample found;
  `subagent-op-exposed-hull-direct-search.md` adds exact `P=A B`, `B A=I`,
  `P1=1` searches with no counterexample.  Next target: repaired-coordinate
  bad-kernel lifetime scoring on direct-search samples.
- D/n4: `subagent-op-exposed-hull-n4-circuit.md` sharply reduces the remaining
  `n=4`, rank-3, `2|2` circuit gap: normalized circuit coefficients either
  give all four vertex exposures, or a small coefficient collapses its vertex
  to the opposite edge at `O(sqrt(delta))`.
- D/LP-game: `agent-B/notes/subagent-op-exposed-hull-lp-game.md` starts the
  frozen joint-certificate miner.  Full unfrozen negation is bilinear/nonconvex;
  the frozen diagnostic augments Hume and reproduces only the large-negative-mass
  regular-polygon warning so far.
- E: deep literature search for near-idempotent stochastic matrices, affine
  retracts of simplices, polytope skeleton selection, and exposed-point
  stability.  Deliverables:
  `agent-B/notes/op-exposed-hull-literature-scout-2026-06-07.md` and
  `agent-B/notes/subagent-op-exposed-hull-literature.md`.  Verdict: no direct
  theorem found; useful sources are indirect and must be proposed for local
  `refs/` acquisition and byte verification before canonical use.
- F: formalization packaging once a proof skeleton survives A-D.
- H: alternative proof frameworks.  Active deliverable:
  `agent-B/notes/subagent-op-exposed-hull-frameworks.md`.  Verdict:
  strongest architecture is maximal exposed skeleton + positive-coordinate
  Markov resolvent + LP/game closed-class augmentation + oriented-circuit
  bookkeeping; pure convex geometry alone is not enough.
- I/P: closed-bad-class hard-block decomposition.  Active workers:
  step1 high-slice extraction, step2 top-face exposure, step3 shadow edge,
  step4 shadow recurrence, step5 circuit extraction, step6 circuit
  aggregation.  Queued until thread capacity frees: step7 separated-circuit
  negative-mass lower bound, step8 capstone packaging.  Durable decomposition:
  `docs/plans/2026-06-07-op-exposed-hull-attack-plan.md`.  Dispatch packets:
  `agent-B/notes/op-exposed-hull-hard-block-dispatch-packets.md`; expanded
  prompt roster:
  `docs/plans/2026-06-07-op-exposed-hull-hard-block-delegation.md`.
- Step1 high-slice extraction delivered:
  `agent-B/notes/subagent-op-exposed-hull-step1-high-slice.md`.  Verdict:
  proof-ready two-scale drift bound:
  `q_i({phi<=M-gamma}) <= (M-phi(p_i)+L_phi eps)/gamma`, `eps<=4delta`.
  This gives `O(tau)` leakage from an `O(delta)` top core into a
  `gamma~tau` high slice; same-scale rowwise closure is too strong.
- Step2 top-face exposure and Step3 shadow edge delivered:
  `agent-B/notes/subagent-op-exposed-hull-step2-top-face-exposure.md` and
  `agent-B/notes/subagent-op-exposed-hull-step3-shadow-edge.md`.  Verdict:
  deterministic/proof-ready, provided the top row is a global separator
  maximizer or higher rows are also included in the bad/high set.
- Step4 shadow recurrence delivered:
  `agent-B/notes/subagent-op-exposed-hull-step4-shadow-recurrence.md`.
  Verdict: finite recurrence lemma is clean; open interface is choosing shadow
  witnesses with high-slice leakage `O(tau)` or proving a q-Lyapunov drift.
- Step5 failed-exposedness circuit extraction delivered:
  `agent-B/notes/subagent-op-exposed-hull-step5-circuit-extraction.md`.
  Verdict: LP/Farkas circuit is proof-ready; uncontrolled lower-face
  `alpha` mass is load-bearing.
- Step6 circuit aggregation delivered:
  `agent-B/notes/subagent-op-exposed-hull-step6-circuit-aggregation.md`.
  Verdict: aggregation works conditionally with an averaged alpha budget or a
  calibrated q-compatible dual; raw quasi-closedness controls q-flow but not
  the failed-exposedness lower-face alpha mass.
- Step7 separated-circuit lower bound delivered as a sanity/refinement note:
  `agent-B/notes/subagent-op-exposed-hull-step7-circuit-lower-bound.md`, with
  reproducible checks in
  `agent-B/experiments/op-exposed-hull/step7_circuit_sanity.py`.  Verdict:
  raw affine-circuit lower bound is false because of stochastic transient-row
  circuits; the viable target must be reduced/vertex or Step-5 anchored.  If
  Step6 gives only `theta=Omega(tau)` witness mass, Step7 needs at least a
  `theta*rho` lower bound, not merely `theta*rho^2`.
- Step8 capstone packaging delivered:
  `agent-B/notes/subagent-op-exposed-hull-step8-capstone-packaging.md`.
  Verdict: candidate DAG is clean; the blocker cut is C9 shadow-exit
  interface, C12 alpha-budget/calibrated-dual, and C13 separated-circuit
  lower bound.  Focused subplans for these three blockers are in
  `docs/plans/2026-06-07-op-exposed-hull-blocker-subplans.md`.
- C9 campaign checkpointed: six tracks covered high-core pruning,
  shadow-witness leakage, Lyapunov fallback, Markov coupling,
  repaired-coordinate computational scoring, and frozen LP/counterexample
  modeling.  Deliverables are
  `agent-B/notes/subagent-op-exposed-hull-c9*.md` plus sandbox experiment
  outputs.  The original C9 dichotomy is not proved; the surviving interface is
  pi-coupled q/shadow closure with the same occupation law, or a route to C12.
- C9-A high-core pruning delivered:
  `agent-B/notes/subagent-op-exposed-hull-c9a-high-core-pruning.md`.  Verdict:
  an `O(delta)` high core maps into an `O(tau)` high slice with `O(tau)`
  leakage if the occupation law returns enough mass to the high core; the
  naive "small high core implies Lyapunov fallback" shortcut is false.
- C9-B shadow leakage delivered:
  `agent-B/notes/subagent-op-exposed-hull-c9b-shadow-leakage.md`.  Verdict:
  Step 3 gives only `O(k/G)` leakage for arbitrary shadow witnesses.  Need
  q-compatible/minimum-leakage witnesses, or failure becomes a C12 calibrated
  dual obstruction.
- C9-C Lyapunov fallback delivered:
  `agent-B/notes/subagent-op-exposed-hull-c9c-lyapunov-fallback.md`.  Verdict:
  the finite Markov resolvent lemmas are proof-ready once real q-drift or
  rowwise exit lower bounds are supplied.
- C9-D Markov coupling delivered:
  `agent-B/notes/subagent-op-exposed-hull-c9d-markov-coupling.md`.  Verdict:
  distributional quasi-closure does not imply rowwise closure in pure finite
  Markov theory; Step 6 should use a `pi`-coupled q/shadow interface, ideally
  with `pi=m` from the bad-kernel quasi-stationary measure.
- C9-E computational scoring delivered:
  `agent-B/notes/subagent-op-exposed-hull-c9e-computational-scoring.md`, with
  `score_c9_repaired.py` and `outputs/c9_repaired_score_*_20260607.*`.
  Verdict: no C9 failure found in 4473 scored direct-sample reports; top
  threats had nonempty bad sets but `bad_lifetime=1` and zero shadow-leakage
  proxy.
- C9-F frozen LP/counterexample model checkpointed before worker shutdown:
  `agent-B/notes/subagent-op-exposed-hull-c9f-counterexample-lp.md`, with
  `agent-B/experiments/op-exposed-hull/c9_frozen_lp.py` and `outputs/c9f_*.json`.
  Verdict from the recorded diagnostic: no small-`delta` C9 failure found;
  Hume/direct examples stop by exposed augmentation or no bad class.  The
  regular 12-gon realizes the frozen failure pattern only at large negative
  mass `delta ~= 0.205`.

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
