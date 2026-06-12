# w35_quantifier: which basis-quantifier does the chain need? (the statement-level fork, now decisive)

You are a codex (gpt-5.5) ANALYST/PROVER. The campaign's single open inequality
(signed-face excess, SF) was just shown to be TIE-AMBIGUOUS: an exact family
(the half-delta staircase, w34_halfcex) has SF/delta = m (rank-unbounded) in
one max-volume chart and EXACTLY 1 in 2m+2 tied max-volume charts. Whether the
campaign lives or dies at moderate delta_0 now depends on WHICH quantifier the
downstream chain actually needs. Settle it.

Repo root: /home/tobias/Projects/almost-idempotent-positive-maps (readable).
Workdir (writable): /tmp/codex-sigma-wall/w35_quantifier.
PROGRESS PROTOCOL: one short line per stage to progress.md.
ARTIFACT RULE: long form to proof.md, NEVER answer.md. gurobi BROKEN in
sandbox; sympy/HiGHS fine (you likely need no solver — this is proof analysis).

## READ (under agent-A/explorations/classical-portfolio/)
1. notes/swarm-answers/w30_maxvol.md — the FULL appendix: the reduction
   displacement <= f(tax) and exactly where "max-volume" is used (the Cramer
   bound |a_t(j)| <= 1 and what else?).
2. notes/swarm-answers/w28_face.md, w27_concentration.md, w26_cluster_audit.md
   — the downstream chain links (face estimate, in-class concentration,
   leakage) and their chart hypotheses.
3. notes/swarm-answers/w31_tax.md sec 1-2 (the tax split; deficit <= 2delta
   uses only sum rules + |a_s| <= 1).
4. notes/swarm-answers/w34_halfcex.md + w34_audit.md — the tie mechanism and
   the staircase.

## THE QUESTIONS (in order)
Q1. AUDIT THE CHAIN'S CHART HYPOTHESES: for each link (tax-split, displacement
    reduction, face estimate, concentration/leakage, L4 assembly), list
    EXACTLY which chart properties are used: |a_t(j)| <= 1? basis rows are
    actual rows? max-volume per se, or only its consequences? Does ANY link
    require the basis to be THE max-volume one, as opposed to A basis with
    bounded coefficients?
Q2. THE QUASI-MAX-VOLUME FIX (robustness to near-ties — IMPORTANT): exact ties
    are fragile (perturb the staircase epsilon and the favorable chart is no
    longer exactly max-volume). But any basis whose volume is within factor
    theta of maximal has |a_t(j)| <= 1/theta (Cramer). So the natural robust
    statement is: "there EXISTS an actual-row basis with volume >= theta *
    max-volume such that SF_chart <= C(delta_0, theta) * delta." Check: does
    every chain link tolerate |a_t| <= 1/theta with constants degrading only
    by theta-dependent factors? If yes, write the corrected end-to-end
    conditional statement (exists-quasi-max-basis SF => ... => global W-free
    O(sqrt(delta))) with the constant dependencies explicit.
Q3. THE TIE-BREAK RULE: for the staircase, the favorable charts replace row 0
    by the exact unit rows e_p, e_n. Formulate a deterministic chart-selection
    rule that (a) picks a quasi-max-volume basis, (b) provably collapses the
    staircase and the w33 dense-pair/transverse-pair excesses, (c) is
    well-defined for every P in the hypothesis class. Candidates to evaluate:
    "greedily prefer rows of minimal support / unit rows", "minimize SF over
    quasi-max bases" (is the minimum even the right object to feed the
    chain?), "maximize volume after projecting out near-duplicate directions".
Q4. VERDICT ON THE CONJECTURE'S SHAPE: given Q1-Q3, state the honest current
    status: (i) if the chain composes with exists-quasi-max SF: the open
    problem becomes that statement at delta_0 <= 0.3 — say so and restate it
    cleanly for the registry (one-line contract form); (ii) if some link
    genuinely needs the for-all/canonical chart: name the link and whether the
    staircase then kills the route at delta_0 >= 1/2 (and what survives below).

## DELIVERABLE (verdict-first; long form to proof.md)
VERDICT: CHAIN-COMPATIBLE (exists-form OK; corrected statement + constants) /
CHAIN-BLOCKED-AT-<link> (the precise chart property that fails + consequence) /
MIXED. Then: the registry-ready corrected SF contract (one line), the
tie-break rule assessment, calibrated P's per claim.
