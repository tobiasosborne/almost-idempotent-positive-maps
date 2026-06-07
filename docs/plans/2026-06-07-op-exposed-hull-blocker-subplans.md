# op-exposed-hull blocker subplans

Date: 2026-06-07.  Author: Agent B.  Status: exploration plan, not a
canonical proof shard.

This decomposes the current blocker cut for the classical `op-exposed-hull`
route:

```text
C9   shadow-exit/interface lemma
C12  alpha-budget or calibrated-dual aggregation lemma
C13  separated-circuit negative-mass lower bound
```

These are the remaining open mathematical interfaces before the
closed-bad-class augmentation capstone can be assembled.

## C9: Shadow-Exit Interface

Target:

```text
lem-shadow-exit-gap:
For a high bad slice, either failed-exposedness witnesses can be chosen as a
shadow kernel with H-leakage O(tau), or the repaired q-chain has a
Lyapunov/resolvent bound O(1/tau).
```

### Plan

Connect two notions of recurrence:

```text
q-recurrence from P^2=P and positive-coordinate repair
shadow recurrence from failed-exposedness witnesses.
```

The failure mode is that failed-exposedness gives a high-average barycenter,
not rowwise mass in the selected high slice.  C9 must either upgrade that
witness to a high-supported shadow kernel, or show the leakage creates drift
which triggers the bad-kernel resolvent.

### Substeps

1. **Two-scale high core.**  Define

   ```text
   H0={i : M-phi(p_i)<=c0 delta},        H1={i : M-phi(p_i)<=G tau}.
   ```

   Use `q_i(H1^c) <= (h_i+4delta)/G tau` to prove `H0` maps into `H1` with
   `O(tau)` leakage.

2. **Prune distributional closure.**  From a quasi-stationary bad measure,
   extract support with both

   ```text
   q_i(B^c)<=O(tau),        M-phi(p_i)<=O(delta).
   ```

   If pruning loses too much mass, convert that loss into a Lyapunov drift.

3. **Shadow witness leakage dichotomy.**  For non-exposed top row `u`, prove
   either the Step 3 witness has `O(tau)` mass outside `H1`, or the mass below
   `H1` gives separator-height drift under `q`.

4. **Build the shadow kernel.**  Choose witnesses `sigma_u` with

   ```text
   sigma_u(H1^c)<=O(tau),
   sigma_u({j:||p_j-p_u||_1>=rho})=1.
   ```

5. **Lyapunov fallback.**  If the preceding substeps fail, construct a
   potential satisfying

   ```text
   E_q[V(next)] <= V(i)-c tau
   ```

   until exit, hence `||(I-T)^(-1)||=O(1/tau)`.

### Experiments

Add repaired-coordinate scoring to direct `A,B` samples:

```text
compute q_i;
choose separator/high slices H0,H1;
measure q-exit, shadow-witness leakage, and bad lifetime.
```

## C12: Alpha-Budget Or Calibrated-Dual Lemma

Target:

```text
lem-alpha-budget-or-calibrated-dual:
In a q-quasi-closed high bad class, failed-exposedness witnesses can be chosen
with averaged alpha mass M=O(1), or with q-compatible calibration whose
residual is O(tau) and whose separated witness mass is quantified.
```

### Plan

Step 5 gives `Y_b + A_b = B_b`, with `A_b` in a zero-face cone and
`|B_b|<kappa`.  Step 6 shows naive averaging is blocked by

```text
M=sum_b m_b |alpha^b|_1.
```

C12 must bound `M`, choose witnesses whose `alpha` sides align with q-flow,
or prove large `alpha` creates a lower-face circuit which is sent to C13.

### Substeps

1. **Gauge-fix the dual.**  Among optimal failed-exposedness duals, add a
   secondary objective minimizing weighted `|alpha|_1`.

2. **Track complementarity supports.**  Use:

   ```text
   alpha on h_b=0,        beta on h_b=1,        mu on h_b=e_b.
   ```

3. **Lower-face null-circuit alternative.**  If `M` is large, extract a
   lower-face affine null circuit and route it either to C13 or to q-leakage.

4. **q-calibrated aggregation.**  Try to choose weights/witnesses with

   ```text
   sum_b omega_b nu^b_j ~= omega_j(1+A_j-B_j)
   ```

   on the recurrent bad class.

5. **Conditional aggregation interface.**  Formalize:

   ```text
   M<=C or M<=C/tau
   -> witness mass theta>=1/(1+M),
      residual E=O((delta+xi)(1+M)).
   ```

### Experiments

Extend `lp_game_certificate.py` to minimize alpha mass subject to
failed-exposedness optimality.  Classify examples by whether `M=O(1)`,
`O(1/tau)`, or apparently unbounded.

## C13: Separated-Circuit Negative-Mass Lower Bound

Target:

```text
lem-separated-circuit-negative-mass:
For the reduced/one-sided aggregate circuit output by C12, with separated
witness mass theta and residual E,
  max_i neg(p_i) >= c theta rho - C E.
```

The raw statement for arbitrary affine circuits is false: stochastic
idempotents can have transient non-vertex circuits with zero negative mass.
C13 must use reduced row-vertex or one-sided failed-exposedness structure.

### Substeps

1. **Normalize admissible circuits.**  Define the accepted inputs exactly:

   ```text
   reduced row-vertex circuit; or anchored Step-5/C12 circuit;
   residual ||r||_1<=E;
   witness mass theta at l1-distance >=rho.
   ```

2. **Remove transient redundancy.**  Delete rows already in the convex hull of
   the opposite side while preserving `theta`, `rho`, and `E` up to constants.

3. **Radon/oriented-minor reduction.**  Extract a small reduced subcircuit.
   The `n=4` `2|2` circuit dichotomy is the base model.

4. **Positive-coordinate contradiction.**  Apply

   ```text
   p_i=sum_j q_i(j)p_j+e_i,        ||e_i||_1<=4delta
   ```

   to force `theta rho` movement that small negative mass cannot absorb.

5. **Prove the medium bound.**  Target first:

   ```text
   delta >= c theta rho - C E.
   ```

   This is the minimum strength needed if C12 gives only `theta=Omega(tau)`.

6. **LP infeasibility mining.**  Build fixed-combinatorics models imposing
   `P1=1`, `P^2=P`, `neg rows<=delta`, and the admissible circuit.  Minimize
   `delta`; extract dual certificates or counterexamples.

## Cross-Block Integration

The three blockers interact through:

```text
xi      q-closure/stationarity error from C9,
M       alpha mass or calibration cost from C12,
theta   separated witness mass output by C12 and consumed by C13,
E       residual from aggregation, roughly O((delta+xi)(1+M)).
```

The route closes if:

```text
xi <= c tau,
M <= C/tau,
theta >= c tau,
E <= c' delta,
delta >= c theta rho - C E contradicts delta=tau^2 by choosing rho=R tau.
```

Best next swarm:

```text
1. C9 repaired-kernel lifetime scorer on direct A,B samples.
2. C12 alpha-minimizing LP dual optimizer.
3. C13 medium-bound LP infeasibility miner.
4. C13 analytic reduced-circuit/Radon proof attempt.
5. C12 lower-face null-circuit leakage proof attempt.
```

## Active C9 Campaign

Launched and checkpointed 2026-06-07.  All workers stayed in the Agent B
sandbox.  The campaign did not prove the original C9 dichotomy; it sharpened
the remaining interface.

```text
C9-A high-core pruning
  -> agent-B/notes/subagent-op-exposed-hull-c9a-high-core-pruning.md
  Task: from quasi-stationary bad measure and height h=M-phi, prove pruning
  to rows with q-exit O(tau) and height O(delta), or produce drift.
  Status: delivered.  A normalized O(delta) high core maps into an O(tau)
  high slice with O(tau) leakage, provided the occupation law returns enough
  mass to that core.  The naive fallback "small high core implies drift" is
  false without a return-mass hypothesis.

C9-B shadow-witness leakage
  -> agent-B/notes/subagent-op-exposed-hull-c9b-shadow-leakage.md
  Task: upgrade failed-exposedness high-average witnesses to H1-supported
  shadow kernels, or show leakage below H1 creates q-drift.
  Status: delivered.  Step 3 alone gives shadow leakage O(k/G), not O(tau).
  Arbitrary failed-exposedness witnesses are not tied to repaired q-rows; the
  corrected split is minimum-leakage/q-compatible witness versus a C12
  calibrated-dual obstruction.

C9-C Lyapunov fallback
  -> agent-B/notes/subagent-op-exposed-hull-c9c-lyapunov-fallback.md
  Task: formalize height/resolvent potentials proving lifetime O(1/tau)
  whenever C9 concentration fails.
  Status: delivered.  The finite Markov resolvent lemmas are proof-ready once
  a genuine q-drift or rowwise exit lower bound is supplied.

C9-D Markov coupling
  -> agent-B/notes/subagent-op-exposed-hull-c9d-markov-coupling.md
  Task: bridge distributional quasi-closure to rowwise or pi-coupled closure
  suitable for Step 6.
  Status: delivered.  Distributional q-quasi-closure does not imply rowwise
  closure in pure Markov theory.  Step 6 should instead keep a common
  q-closed and shadow-stationary averaging law pi, preferably pi=m.

C9-E computational scoring
  -> agent-B/notes/subagent-op-exposed-hull-c9e-computational-scoring.md
  Task: score direct A,B samples by q-lifetime, high-slice exit, and shadow
  leakage; hunt small-delta C9 failures.
  Status: delivered.  No C9 failure found in 4473 scored direct-sample
  reports; nonempty bad sets exited immediately in the top threats, and
  Step-3 shadow leakage proxy was zero.

C9-F frozen LP/counterexample model
  -> agent-B/notes/subagent-op-exposed-hull-c9f-counterexample-lp.md
  Task: build a frozen-row/fixed-combinatorics feasibility model for failure
  of C9 and mine dual certificates or candidate counterexamples.
  Status: checkpointed before worker shutdown.  The recorded diagnostic found
  no small-delta C9 failure; regular 12-gon gives only a large-delta
  calibration warning.
```

Campaign integration target now:

```text
Either prove a pi-coupled C9 interface:
  pi q(H^c) <= O(tau),
  ||pi S-pi||_1 <= O(tau),
  pi(1-S1) <= O(tau),
with pi=m from the bad-kernel occupation law,
or prove that failure of such q-compatible witness selection produces the
C12 alpha-budget/calibrated-dual obstruction.
```
