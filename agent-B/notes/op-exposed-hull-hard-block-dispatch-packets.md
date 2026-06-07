# op-exposed-hull Hard-Block Dispatch Packets

Date: 2026-06-07. Lane: Agent B exploration sandbox. Status: orchestration
artifact, not a canonical proof shard.

Use these packets to launch or resume focused workers on the eight pieces of
the closed-bad-class/high-face blocker.  Every worker stays in `agent-B/**`
and `docs/plans/**`, and must not edit canonical layers.

Common required reading for every worker:

```text
docs/plans/2026-06-07-op-exposed-hull-attack-plan.md
agent-B/notes/subagent-op-exposed-hull-lp-dual.md
agent-B/notes/subagent-op-exposed-hull-bad-kernel.md
agent-B/notes/subagent-op-exposed-hull-frameworks.md
```

Every deliverable ends with:

```text
Verdict; candidate contract if any; proof/gaps; constants; failure modes;
next handoff.
```

## Step 1: High-Slice Extraction

Deliverable:

```text
agent-B/notes/subagent-op-exposed-hull-step1-high-slice.md
```

Goal: prove or refute the Markov-drift statement that long bad lifetime plus a
separator `phi` produces a high slice which remains `O(tau)`-closed under the
repaired kernel `q`.  Quantify leakage from a row with height defect `a tau`
to rows lower by `gamma tau`.

## Step 2: Top-Face Exposure Test

Deliverable:

```text
agent-B/notes/subagent-op-exposed-hull-step2-top-face-exposure.md
```

Goal: isolate the easy exposure lemma.  If a separator-maximal bad vertex has
a `rho`-outside set all at affine gap at least `kappa`, prove it is
`(rho,kappa)`-well-exposed after normalizing the affine functional to `[0,1]`.

## Step 3: Shadow Edge

Deliverable:

```text
agent-B/notes/subagent-op-exposed-hull-step3-shadow-edge.md
```

Goal: from failure of Step 2, extract a `rho`-separated high bad row or
barycenter.  Use the LP-dual failed-exposedness witness and track whether the
witness can be forced to remain in the bad/high slice.

## Step 4: Shadow Recurrence / Potential

Deliverable:

```text
agent-B/notes/subagent-op-exposed-hull-step4-shadow-recurrence.md
```

Goal: turn repeated shadow edges into either a Lyapunov drift to the good set
or a recurrent high bad component.  This is the Happynet-like no-cycle step;
look for a potential using separator height, bad-kernel lifetime, or LP game
value.

## Step 5: Failed-Exposedness Circuit Extraction

Deliverable:

```text
agent-B/notes/subagent-op-exposed-hull-step5-circuit-extraction.md
```

Goal: make the Farkas circuit completely proof-ready, including
complementarity.  Record not only
`sum beta_i < kappa`, but also where `alpha` and `beta` can be supported for
chosen optimal witnesses.

## Step 6: Circuit Aggregation

Deliverable:

```text
agent-B/notes/subagent-op-exposed-hull-step6-circuit-aggregation.md
```

Goal: average/eliminate local circuits over a q-quasi-closed bad class.  Try
both `m`-average and q-flow balance normalizations.  The current delivered
verdict is conditional: aggregation needs an alpha-budget or a calibrated
q-compatible dual.

## Step 7: Separated Circuit Lower Bound

Deliverable:

```text
agent-B/notes/subagent-op-exposed-hull-step7-circuit-lower-bound.md
```

Goal: prove or refute that a normalized `rho`-separated bad circuit in an
exact signed affine retraction forces

```text
max_i neg(p_i) >= c rho^2.
```

Also test the weaker Step 6 output: can the lower bound tolerate separated
witness mass only `Omega(tau)` rather than a constant fraction?

## Step 8: Capstone Packaging

Deliverable:

```text
agent-B/notes/subagent-op-exposed-hull-step8-capstone-packaging.md
```

Goal: assemble Steps 1-7 into af-sized candidate contracts and a dependency
DAG.  Explicitly mark which statements are proof-ready, which need Agent A
review, and which remain open blockers.  Do not touch `argument/`.
