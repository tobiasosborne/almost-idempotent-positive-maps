# w41_ex: verify the factorization S* <= a*Phi + b*delta, then decide (EX) at rank 3

You are a codex (gpt-5.5) PROVER/DECIDER. The rank-2 theorem just closed
(w40: every Phi-argmin chart has S* <= 2 delta, unconditional). Its proof
factorizes, and IF the factorization is right, the entire classical campaign
reduces to a pure existence statement (EX). Verify the factorization, then
decide (EX) at rank 3 — by construction or by counterexample.

Repo root: /home/tobias/Projects/almost-idempotent-positive-maps (main).
Workdir (writable): /tmp/codex-sigma-wall/w41_ex.
PROGRESS PROTOCOL: one short line per stage to progress.md.
ARTIFACT RULE: long form to proof.md, NEVER answer.md. sympy/HiGHS; gurobi
broken in sandbox (write-not-run nonconvex scripts).

## READ (under agent-A/explorations/classical-portfolio/)
1. notes/swarm-answers/w40_ndg.md — the rank-2 theorem + proof pattern + the
   ORCHESTRATOR ANALYSIS paragraph (the factorization sketch you must verify
   or refute: sigma <= E + 2 lambda_+; (-lambda)_+ <= E/2 on overshoot rows;
   Sum beta_+ lambda_+ <= 3 delta + Phi/2 via (DEF) + box) and
   experiments/out/w40_ndg/proof.md (full rank-2 proof).
2. notes/swarm-answers/w39_opus_repair.md ((P1), S*, (SB*)), w38_sb.md,
   w36_audit.md (B6: theta = 1/2). Reusable exact auditors in
   experiments/out/w37_opus/, w38_sb/, w40_ndg/.

## PART 1 — THE FACTORIZATION LEMMA (verify or refute, with exact constants)
Claim to check: for ANY basis U in the theta-1/2 class and any s,
  S*_s(U) <= a * Phi_s(U) + b * delta,   Phi_s := sum_j (beta_s)_+ E_s(j),
with dimension-free a, b (the sketch suggests a ~ 3, b ~ 6; get the true
constants). If TRUE: combined with the argmin selection, (EX) [exists U in
the class with max_s Phi_s <= C0 delta] implies the registry contract with
C_sf = a*C0 + b — state this composition precisely. If FALSE: exact witness
and what additional term is needed.

## PART 2 — (EX) AT RANK 3 (the decisive question)
(EX): every rank-3 row-stochastic idempotent with delta(P) <= delta_0 = 1/4
has an actual-row basis U, Vol(U) >= (1/2) Vol_max, with
max_s Phi_s(U) <= C0 * delta(P).
2a. CONSTRUCTION: find the rank-3 analog of the rank-2 max-diameter chart.
    Candidates to test exactly: (i) max-volume itself (KNOWN insufficient —
    the staircase has Phi = m*delta at max-volume... but that is at
    delta = 1/2; test at delta_0 = 1/4!); (ii) the "peeled" basis: choose
    rows greedily maximizing the MINIMUM coefficient (most-convex chart);
    (iii) the basis minimizing total negative coefficient mass
    sum_{j,t} (-a_t(j))_+ (an LP-friendly surrogate for Phi); (iv) the
    Phi-argmin itself via exhaustive enumeration at small d. For each
    candidate: exact values on rank-3 restrictions/analogs of all the stress
    families + your own adversarial instances.
2b. ADVERSARIAL SEARCH (the falsification side): maximize over rank-3
    idempotents (LB/BL=I converse, exact rationals) the quantity
    min over theta-1/2 charts U of max_s Phi_s(U) / delta(P).
    Structured guesses: rank-3 versions of the perturbed staircase; rows
    placed so EVERY large-volume triangle has some row outside it (a
    "windmill" configuration — three clusters arranged so any basis triangle
    leaves one cluster's rows with negative coefficients); near-degenerate
    triangles. If you find min-chart Phi / delta unbounded (growing along a
    family), (EX) IS FALSE AND THE CONJECTURE FALLS — verify exactly and
    triple-check the chart enumeration is exhaustive over the theta-1/2 class.
2c. If 2a yields a construction that works on everything: attempt the rank-3
    proof (the two-horn dichotomy now only needs to handle the constructed
    chart's failure modes). If both 2a-candidates fail and 2b finds no
    counterexample: report the sharpest instance and the exact obstruction.

## MANDATORY EXACT CHECKS
All six known families (restricted/adapted to rank 3 where applicable:
transverse pair IS rank-3; dense pair k=7 is rank-7 — skip or restrict;
staircase m=2 is rank-5 — build the rank-3 analog m=1 and say if degenerate)
+ at least 200 random + 20 adversarial exact rank-3 instances.

## DELIVERABLE (verdict-first; long form to proof.md)
VERDICT: FACTORIZATION VERIFIED/REFUTED (constants) x (EX)-RANK-3: PROVED
(construction + proof) / HOLDS-EMPIRICALLY (best construction, worst ratio,
the precise open) / FALSE (exact counterexample family). Calibrated P's.
Save everything.
