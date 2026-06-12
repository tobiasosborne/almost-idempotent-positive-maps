# w34_audit: hostile audit of the wave-33 verdicts (cex + sf_geom) AND the orchestrator's interventions

You are a codex (gpt-5.5) HOSTILE AUDITOR. Two wave-33 workers and the
orchestrator (a Claude-family model) have made load-bearing claims about the
signed-face excess (SF). Audit ALL of them adversarially — including the
orchestrator's own refutation of a worker claim (reviewer must differ from
author; you are the reviewer for everything below). Default to skepticism;
verify computationally where possible.

Repo root: /home/tobias/Projects/almost-idempotent-positive-maps (readable).
Workdir (writable): /tmp/codex-sigma-wall/w34_audit.
PROGRESS PROTOCOL: one short line per stage to progress.md.
ARTIFACT RULE: long form to audit.md, NEVER answer.md. Save all code+outputs.
TOOLING: SciPy/HiGHS + sympy exact rationals. gurobi is BROKEN in this sandbox.

## CONTEXT
SF: P real dxd, P^2=P, P1=1, row neg mass <= delta; u_1..u_k max-volume
actual-row basis, p_j = sum_t a_t(j) p_{u_t}, |a_t(j)|<=1, sum_t a_t(j)=1;
claim: sum_j (P_{u_s j})_+ (sum_{t!=s}(-a_t(j))_+ - (1-a_s(j)))_+ <= C*delta.
Read: agent-A/explorations/classical-portfolio/notes/swarm-answers/w33_cex.md
and w33_sf_geom.md (verdict headers + full appendices), and
experiments/out/w33_cex/, experiments/out/w33_sf_geom/ (all scripts/outputs).

## ITEMS TO AUDIT (verdict per item: CONFIRMED / REFUTED / UNRESOLVED, with
calibrated P and your evidence)
A1. w33_cex's exact transverse-pair family (its sec 3): re-derive
    independently in sympy; check BL=I, P^2=P, row sums, nu, the recomputed
    max-volume chart, SF, and the claimed SF/delta = m(1+4a^2)... (their
    formula: ratio = m(1+4a^2) with their m = mass parameter, NOT rank). Any
    algebra slip?
A2. w33_cex's duplicate-stacking invariance claim ("splitting B_0's fixed
    positive mass among q copies cannot raise SF") — is the LP/exact evidence
    airtight, or does it depend on a symmetry assumption about how the dual
    rows split? Try an ASYMMETRIC split adversarially.
A3. w33_cex's tie-chart path family ratios (sec 7: 1.25 -> 1.91, k=4..20,
    "suggests limit 2"): re-run/spot-check k=10 and k=20; is the limit-2 claim
    sound, or could it keep growing (log k)? Fit honestly.
A4. w33_sf_geom's fixed-support certificates (sec 4): ratio formulas 1+4a^2
    (k=3 pair) and 1+3a^2 (k=4): derive ANALYTICALLY from the LP optimality
    conditions (small enough to do by hand/sympy). Confirm or correct.
A5. w33_sf_geom's k=7 dense-pair instance (delta=6/17, SF=3/4, ratio=17/8):
    independent exact re-verification INCLUDING max-volume chart recomputation
    with tie scan (the saved dense_pair_k7_verify.txt claims max minor 1 —
    check whether OTHER bases also attain minor 1 and whether SF differs in a
    tie basis).
A6. THE ORCHESTRATOR'S REFUTATION (header of w33_sf_geom.md): the worker's
    sec-6 "convexity estimate" sum_j (B_sj)_+ F(L_j) <= nu_{u_s} max_j F(L_j)
    was declared FALSE via the worker's own k=7 instance (B_0 >= 0 so
    nu_{u_0} = 0, LHS = 3/4; and with global delta in place of nu: 9/34 <
    3/4). Check: is E_0 really convex with E_0(e_0) = 0? Is the instance
    really feasible for the estimate's hypotheses? Is there a CHARITABLE
    reading of the worker's estimate (e.g. different nu, or an additional
    hypothesis) under which it is true and useful? If the refutation stands,
    say so; if a repaired version survives, STATE IT — a correct version
    would be a proof ingredient.
A7. CROSS-CUTTING: both w33 workers used the H-M 1.12 converse in the
    factored form P = LB, BL = I. Confirm this equivalence carefully ONCE
    (rank conditions! L full column rank, B full row rank — where is that
    needed, can it fail for the constructed instances?) and byte-check the
    H-M anchors they cite (refs/hognas-mukherjea-2011/*.txt; note the OCR
    glyph issues flagged in w33_sf_geom sec 1).

## DELIVERABLE (verdict-first; long form to audit.md)
A table: item, verdict, P(your verdict correct), one-line reason. Then the
detailed evidence per item. Flag anything ELSE suspicious you noticed beyond
A1-A7 (you are encouraged to find NEW problems).
