# op-exposed-hull hard-block delegation

Date: 2026-06-07.  Author: Agent B.  Status: exploration orchestration, not
a canonical proof shard.

## Scope

This file is the durable subagent roster for the hard block in the classical
route:

```text
closed-bad-class / high-face augmentation
```

All workers stay in:

```text
agent-B/**
docs/plans/**
```

Do not edit:

```text
definitions/**
argument/**
proofs/**
report/**
AGENTS.md
CLAUDE.md
HANDOFF.md
```

Every worker reports:

```text
Verdict; candidate contract; proof outline; gaps; constants; next handoff.
```

## Step 1: High-Slice Extraction

Deliverable:

```text
agent-B/notes/subagent-op-exposed-hull-step1-high-slice.md
```

Status: completed in exploration form.  Main output:

```text
q_i({phi <= M-gamma}) <= (h_i + L_phi eps)/gamma,
h_i=M-phi(p_i),        eps<=4delta.
```

For `gamma=G tau` and `h_i=O(delta)`, leakage below the high slice is
`O(tau)`.  This is a two-scale statement: an `O(delta)` top core maps into a
`G tau` high slice with `O(tau)` leakage.  A same-scale `tau` slice would only
give constant leakage.

## Step 2: Top-Face Exposure Test

Status: completed in proof-ready exploration form.  Main output:

```text
outside phi-drop >= M_phi kappa
  => e_u(rho)>=kappa,
M_phi<=2+4delta for l_infty-dual normalized phi.
```

Prompt:

```text
You are Agent B subagent for op-exposed-hull. Work ONLY in sandbox paths
agent-B/** and docs/plans/**. Do not edit canonical layers.

Task Step 2: Top-Face Exposure lemma.

Read:
- docs/plans/2026-06-07-op-exposed-hull-attack-plan.md
- docs/plans/2026-06-07-op-exposed-hull-hard-block-delegation.md
- agent-B/notes/subagent-op-exposed-hull-step1-high-slice.md
- agent-B/notes/subagent-op-exposed-hull-lp-dual.md

Deliverable:
agent-B/notes/subagent-op-exposed-hull-step2-top-face-exposure.md

Goal:
Prove the easy exposure test.  If u is separator-maximal and every row outside
the rho-ball around u has phi-drop at least kappa, then u is
(rho,kappa)-well-exposed.  Track the exact normalization needed to turn phi
into an exposedness witness h with h(u)=0 and 0<=h<=1 on rows.  State what
changes if phi is only l_infty-dual normalized or has oscillation >1.  End
with Verdict, candidate contract, proof outline, gaps, constants, next
handoff.
```

## Step 3: Shadow Edge

Prompt:

```text
You are Agent B subagent for op-exposed-hull. Work ONLY in sandbox paths
agent-B/** and docs/plans/**. Do not edit canonical layers.

Task Step 3: Shadow Edge lemma.

Read:
- docs/plans/2026-06-07-op-exposed-hull-attack-plan.md
- docs/plans/2026-06-07-op-exposed-hull-hard-block-delegation.md
- agent-B/notes/subagent-op-exposed-hull-step1-high-slice.md
- agent-B/notes/subagent-op-exposed-hull-lp-dual.md

Deliverable:
agent-B/notes/subagent-op-exposed-hull-step3-shadow-edge.md

Goal:
Assume a separator-maximal high bad vertex u is not (rho,kappa)-well-exposed.
Use the exposedness LP/minimax statement to extract a row or barycenter y
supported outside B_1(u,rho) with phi(y)>=phi(u)-O(kappa).  Determine whether
one can choose an actual row w with comparable height, and record losses.
Preserve badness: if u is A tau above conv R or conv W, quantify the remaining
margin for y/w.  End with Verdict, candidate contract, proof outline, gaps,
constants, next handoff.
```

## Step 4: Shadow Recurrence / Potential

Prompt:

```text
You are Agent B subagent for op-exposed-hull. Work ONLY in sandbox paths
agent-B/** and docs/plans/**. Do not edit canonical layers.

Task Step 4: Shadow Recurrence / Potential lemma.

Read:
- docs/plans/2026-06-07-op-exposed-hull-attack-plan.md
- docs/plans/2026-06-07-op-exposed-hull-hard-block-delegation.md
- agent-B/notes/subagent-op-exposed-hull-step1-high-slice.md
- agent-B/notes/subagent-op-exposed-hull-step3-shadow-edge.md if present
- agent-B/notes/subagent-op-exposed-hull-frameworks.md

Deliverable:
agent-B/notes/subagent-op-exposed-hull-step4-shadow-recurrence.md

Goal:
Formalize the Happynet-like no-escape alternative.  Repeated shadow edges
among high non-exposed vertices either create a Lyapunov drift that bounds
bad lifetime by O(1/tau), or produce a recurrent high bad component.  Make the
graph/state space precise: rows vs barycenters, rho-separated vertices vs
clusters, and how Step 1 closure is used.  End with Verdict, candidate
contract, proof outline, gaps, constants, next handoff.
```

## Step 5: Failed-Exposedness Circuit Extraction

Prompt:

```text
You are Agent B subagent for op-exposed-hull. Work ONLY in sandbox paths
agent-B/** and docs/plans/**. Do not edit canonical layers.

Task Step 5: Failed-Exposedness Circuit Extraction.

Read:
- docs/plans/2026-06-07-op-exposed-hull-attack-plan.md
- agent-B/notes/subagent-op-exposed-hull-lp-dual.md
- agent-B/notes/subagent-op-exposed-hull-step2-top-face-exposure.md if present
- agent-B/notes/subagent-op-exposed-hull-step3-shadow-edge.md if present

Deliverable:
agent-B/notes/subagent-op-exposed-hull-step5-circuit-extraction.md

Goal:
Package the LP-dual derivation as an af-sized lemma.  From e_v(rho)<kappa,
produce mu on rows outside B_1(v,rho) and alpha,beta>=0 with
sum beta_i<kappa and
sum_{j outside rho} mu_j(p_j-v)=sum_i(beta_i-alpha_i)(p_i-v).
Normalize the circuit and isolate the uncontrolled alpha-mass.  End with
Verdict, candidate contract, proof outline, gaps, constants, next handoff.
```

## Step 6: Circuit Aggregation

Prompt:

```text
You are Agent B subagent for op-exposed-hull. Work ONLY in sandbox paths
agent-B/** and docs/plans/**. Do not edit canonical layers.

Task Step 6: Circuit Aggregation.

Read:
- docs/plans/2026-06-07-op-exposed-hull-attack-plan.md
- docs/plans/2026-06-07-op-exposed-hull-hard-block-delegation.md
- agent-B/notes/subagent-op-exposed-hull-step1-high-slice.md
- agent-B/notes/subagent-op-exposed-hull-step5-circuit-extraction.md if present
- agent-B/notes/subagent-op-exposed-hull-n4-circuit.md

Deliverable:
agent-B/notes/subagent-op-exposed-hull-step6-circuit-aggregation.md

Goal:
Average local failed-exposedness circuits over a q-quasi-closed recurrent high
bad component.  Find a way to cancel or dominate the uncontrolled alpha-mass
using q-closedness and positive-coordinate reconstruction.  Compare the
general mechanism with the n=4 2|2 circuit coefficient dichotomy.  End with
Verdict, candidate contract, proof outline, gaps, constants, next handoff.
```

## Step 7: Separated-Circuit Negative-Mass Lower Bound

Prompt:

```text
You are Agent B subagent for op-exposed-hull. Work ONLY in sandbox paths
agent-B/** and docs/plans/**. Do not edit canonical layers.

Task Step 7: Separated-Circuit Negative-Mass Lower Bound.

Read:
- docs/plans/2026-06-07-op-exposed-hull-attack-plan.md
- agent-B/notes/subagent-op-exposed-hull-step6-circuit-aggregation.md if present
- agent-B/notes/subagent-op-exposed-hull-n4-circuit.md
- agent-B/notes/subagent-op-exposed-hull-small-cases.md

Deliverable:
agent-B/notes/subagent-op-exposed-hull-step7-circuit-lower-bound.md

Goal:
Prove or refute the target lower bound: a normalized affine circuit supported
on rho-separated rows in an exact signed affine retraction forces
max_i neg(p_i) >= c rho^2, under whatever additional hypotheses Step 6
actually supplies.  Identify necessary normalization precisely; test against
Hume and n=4 circuits.  End with Verdict, candidate contract, proof outline,
gaps, constants, next handoff.
```

## Step 8: Capstone Packaging

Prompt:

```text
You are Agent B subagent for op-exposed-hull. Work ONLY in sandbox paths
agent-B/** and docs/plans/**. Do not edit canonical layers.

Task Step 8: Closed-Bad-Class Capstone Packaging.

Read:
- docs/plans/2026-06-07-op-exposed-hull-attack-plan.md
- docs/plans/2026-06-07-op-exposed-hull-hard-block-delegation.md
- all agent-B/notes/subagent-op-exposed-hull-step*.md
- agent-B/notes/subagent-op-exposed-hull-bad-kernel.md

Deliverable:
agent-B/notes/subagent-op-exposed-hull-step8-capstone.md

Goal:
Assemble Steps 1-7 into the closed-bad-class augmentation lemma.  Split the
result into af-sized candidate contracts, name exact dependencies, expose any
remaining gaps, and state constants in a hierarchy D >> R >> 1 >> k.  Do not
upgrade canonical status.  End with Verdict, dependency DAG, candidate
contracts, gaps, constants, next handoff to Agent A.
```
