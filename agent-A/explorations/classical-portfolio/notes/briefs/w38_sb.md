# w38_sb: verify the opus reduction, then prove (SB) — the harmonic sign-budget at the argmin chart

You are a codex (gpt-5.5) PROVER and second-family VERIFIER. An independent
Claude-Opus prover (w37_opus) reduced the classical campaign's last lemma to a
single scalar display (SB), strictly cleaner than the earlier (TREE)/(CHARGE)
forms: no shear tree, no charge weights, the selection as the only nonlinear
ingredient. Your job: (A) independently verify the reduction (2-family
done-bar), then (B) prove (SB) — the named gap is encoding the argmin
selection constraints, which BOTH prior attempts left undone.

Repo root: /home/tobias/Projects/almost-idempotent-positive-maps (readable;
branch main). Workdir (writable): /tmp/codex-sigma-wall/w38_sb.
PROGRESS PROTOCOL: one short line per stage to progress.md.
ARTIFACT RULE: long form to proof.md, NEVER answer.md. sympy/HiGHS; gurobi
broken in sandbox.

## READ (under agent-A/explorations/classical-portfolio/)
1. notes/swarm-answers/w37_opus.md + experiments/out/w37_opus/proof.md (the
   reduction: (R), (DEF), (SIG), (SB), the irreducibility witnesses) and its
   scripts (charge_lp.py, nocenter_lp.py, nocenter_exact.py, harness.py).
2. notes/swarm-answers/w36_charge.md ((TREE) and the no-center path family),
   w36_audit.md (B6: theta = 1/2 mandatory; B5: tautological-charge warning).
3. experiments/out/w35_charge/stress_checks.py + w36_charge auditors (exact
   tie enumeration / selected-chart evaluation conventions).

## PART A — VERIFY THE OPUS REDUCTION (do this first, honestly)
A1. (R): E_s(j) = (sigma_s(j) - 2 lambda_s(j))_+ where sigma_s = positive
    off-pivot coefficient mass. Re-derive from the definitions; confirm it
    equals the registry E_s = (mu_s - lambda_s)_+ ... or does it? Work out
    the exact relation (mu vs sigma, lambda sign cases at theta = 1/2) and
    state which form the CHAIN (w35_quantifier contract) actually needs.
A2. The claimed w35 CORRECTION: SF_s <= M_s false at theta = 1/2 (witness:
    perturbed staircase m = 5, rows with a_s > 1). Verify the witness
    exactly. If confirmed, check whether the w35_quantifier constants chain
    (C_mu = C_sf + 1 + A) survives under (R) — recompute the one affected
    step or flag precisely what changes.
A3. (DEF) sum_j beta_s lambda_s = 0 and the (SIG) reduction SF_s <= S+_s and
    [S+_s <= 3 delta => Phi(U*) <= 3 delta]. Verify line by line.
A4. The irreducibility witnesses (SB false over the full class; ME, sigma-only,
    single-swap refuted). Spot-verify at least the single-swap one exactly.

## PART B — PROVE (SB) (the real target)
(SB): U* in argmin over the theta = 1/2 class of Phi(U) = max_s SF_s(U)
implies sum_j (beta_s(j))_+ sigma_s(j) <= 3 delta(P) for all s.
Handles: nu_i <= delta; (DEF); Cramer box |a_t(j)| <= 2; argmin minimality.

THE NAMED GAP (both families hit it): converting argmin minimality into a
usable inequality. Attack it head-on:
B1. ENCODE THE SELECTION COMBINATORIALLY: minimality means Phi(U*) <= Phi(V)
    for EVERY basis V in the theta = 1/2 class — not just adjacent swaps.
    For the known hard families, the certificate basis V that beats the bad
    chart is a MULTI-ROW swap (all signed rows in at once). So: derive the
    comparison inequality Phi(U*) <= Phi(V) for the SPECIFIC family of
    candidate bases V = (U* with the entire positive-mass support of row s's
    excess swapped in, when volume permits). Compute Phi(V) for such V in
    terms of U*'s data (the multi-row generalization of the shear formula —
    derive it; block Cramer/Schur complement on the swap set). If
    Phi(V) <= (something) + C' delta whenever S+_s(U*) is large, minimality
    forces S+_s(U*) small. This is the structured version of what single
    swaps cannot see.
B2. VOLUME-PERMITTING: the swap set above must keep Vol(V) >= (1/2) Vol_max.
    The bad configurations have excess carried by rows with LARGE transverse
    coefficients — exactly the rows whose swap-in changes volume by the
    determinant of the transverse block. Show: either the swap set has
    volume factor >= 1/2 (swap allowed => minimality bites), or the
    transverse block has small determinant => the coefficient vectors are
    near-dependent => their excess is bounded by O(delta) directly (a
    near-degenerate analysis — make precise). THIS DICHOTOMY is my best
    guess at the missing mechanism; work it at rank 2-3 first.
B3. LP WITH SELECTION CONSTRAINTS: redo the small-instance LP duals but ADD
    the comparison constraints from B1's structured family (finitely many
    per instance). If the duals stop being tautological, extract the pattern.
B4. Fallbacks if (SB) resists: prove it for delta_0 smaller; or prove
    S+_s <= C delta + (1/2) S+_max (self-improving form); or produce the
    exact sub-display that remains.

## MANDATORY EXACT CHECKS
transverse pair a=1/4; dense pair k=7; staircase m=2,3; perturbed staircase
m=5 eps=1/1000; no-center path k=6,8 (S+ climbs 2.5 -> 2.95 delta there —
your bound must clear 3 or explain the margin).

## DELIVERABLE (verdict-first; long form to proof.md)
VERDICT: REDUCTION VERIFIED + SB PROVED / REDUCTION VERIFIED + PARTIAL (exact
missing display) / REDUCTION REFUTED-AT-<step> (exact error) / DIED-AT.
Calibrated P's per part. Save all code + outputs.
