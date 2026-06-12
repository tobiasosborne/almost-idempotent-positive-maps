# w36_charge: prove (CHARGE) — the last named inequality of the classical campaign

You are a codex (gpt-5.5) PROVER. The entire route to the classical conjecture
is now reduced to ONE inequality for ONE selected chart. Wave 35 proved
everything around it: the chain composes with the exists-chart form
(w35_quantifier, constants explicit), the chart selection is well-defined, the
deficit is banked, and EVERY known adversarial instance — transverse pair,
dense pair, half-delta staircase even at delta = 1/2 — has ratio EXACTLY 1 in
the selected chart. Prove the inequality, or find the instance that beats the
selected chart.

Repo root: /home/tobias/Projects/almost-idempotent-positive-maps (readable).
Workdir (writable): /tmp/codex-sigma-wall/w36_charge.
PROGRESS PROTOCOL: one short line per stage to progress.md.
ARTIFACT RULE: long form to proof.md, NEVER answer.md. sympy/HiGHS available;
gurobi BROKEN in this sandbox (write any nonconvex script for the orchestrator
to run outside, do not run it here).

## READ FIRST (under agent-A/explorations/classical-portfolio/)
1. notes/swarm-answers/w35_charge.md — FULL appendix: the setup, the selection
   U* = argmin over exact max-volume ties of Phi(U) = max_s SF_s(U), the
   banked deficit, the boxed (CHARGE) statement, and section 5 (the shear
   formula (S) — the exact obstruction). Reuse its exact stress-check script
   experiments/out/w35_charge/stress_checks.py.
2. notes/swarm-answers/w35_quantifier.md — the chain contract you are feeding
   (theta-quasi allowed: if your proof needs theta < 1 slack in the selection
   class, TAKE IT — the chain tolerates it with A = 1/theta).
3. notes/swarm-answers/w34_audit.md — A2 (duplicate dual-flow mechanism),
   A3 (the path-tie family: ratios saturate ~2 — your proof must handle it),
   A4 (tight small-support certificates).
4. notes/swarm-answers/w34_halfcex.md — the collapse mechanism (swap exact
   unit rows in; the split-mass row leaves the representative role).

## THE TARGET
delta_0 = 1/4 (or up to 0.3 if clean). For U* the Phi-minimizing basis (over
exact max-volume ties, or over a theta-quasi-max class of your choice):

  (CHARGE)  for every s:  SF_s(U*) <= sum_i q_si nu_i(P),
            q_si >= 0,  sum_i q_si <= C(delta_0)  dimension-free.

Equivalent acceptable form: Phi(U*) <= C(delta_0) * delta directly, any
dimension-free C. The stress data supports C = 1 at theta = 1 — but do NOT
chase the sharp constant; chase CLOSURE.

## ATTACK ROUTES (in suggested order; deviate freely)
R1. MULTI-SWAP DESCENT WITH A DECAYING POTENTIAL: single swaps can shear
    excess (formula (S)); but the shear coefficient is a_s(i) * w_t with
    |w_t| <= 2 and the sheared excess lands on rows with SMALLER a_s. Look
    for a weighted potential (e.g. sum_s SF_s weighted by powers of the
    diagonal coefficients, or Phi plus epsilon * total excess) that STRICTLY
    decreases along a terminating swap sequence unless SF <= C delta. The
    path-tie family's geometric-looking saturation (1 -> 2) suggests a
    contraction factor ~1/2 per swap generation: try to prove the sheared
    excess after a swap is at most half the removed excess + O(delta).
R2. LP DUALITY ON THE SELECTED CHART: for FIXED support pattern, SF_s max
    subject to (BL = I, row negativity, minimality of Phi at U* expressed as
    finitely many swap-comparison inequalities Phi(U*) <= Phi(U) for adjacent
    ties U) is an LP. The swap-comparison constraints are exactly what w35
    lacked. Extract the dual at small supports (k = 3, 4, the path family
    k <= 8) with the swap constraints INCLUDED; if the dual certificates have
    uniform structure, generalize.
R3. DIRECT (ME): max_j E_s(j) <= K delta in U* for delta_0 <= 1/4. A row with
    huge excess and a_s(j) = 1 is swap-eligible at equal volume; minimality
    of Phi at U* + the deficit identity in the swapped chart may bound its
    excess directly. This is the shortest plausible path — try it FIRST at
    rank 2-3 to see the mechanism, then general.
R4. If all fail: produce the exact configuration where the Phi-minimizing
    chart still carries SF > C delta for every C (i.e. beat the SELECTED
    chart, not a fixed chart) — that would be a genuine counterexample to the
    registry contract. Verify exact-rationally with the w35 auditor.

## MANDATORY CHECKS
Whatever you prove, verify exact-rationally on: transverse pair (a = 1/4),
dense pair k = 7, staircase m = 2, 3 (reuse stress_checks.py), AND the
w34_audit path-tie family at k = 6, 8 (the saturation case — if your C < 2,
this family is the first thing that breaks you; handle it explicitly).

## DELIVERABLE (verdict-first; long form to proof.md)
VERDICT: CHARGE PROVED (statement, C, theta, delta_0, full proof, all checks)
/ PARTIAL (exact missing step in display math) / COUNTEREXAMPLE-TO-CONTRACT
(exact instance beating the selected chart) / DIED-AT. Calibrated P's. Save
all code + outputs; nonconvex gurobi scripts saved-not-run.
