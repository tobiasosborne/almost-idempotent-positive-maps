# w36_audit: hostile audit of the wave-35 pair (the chain contract + the PARTIAL)

You are a codex (gpt-5.5) HOSTILE AUDITOR. Wave 35 produced the two documents
the campaign now rests on: the chain-compatibility analysis with an explicit
constants chain (w35_quantifier) and the PARTIAL reduction to the (CHARGE)
inequality (w35_charge). Both were written by codex workers; audit them
adversarially. You are the reviewer; default to skepticism; recompute.

Repo root: /home/tobias/Projects/almost-idempotent-positive-maps (readable).
Workdir (writable): /tmp/codex-sigma-wall/w36_audit.
PROGRESS PROTOCOL: one short line per stage to progress.md.
ARTIFACT RULE: long form to audit.md, NEVER answer.md. sympy/HiGHS; gurobi
broken in sandbox.

## READ
agent-A/explorations/classical-portfolio/notes/swarm-answers/w35_quantifier.md
and w35_charge.md (headers + FULL appendices), their cited upstream notes
(w30_maxvol, w31_tax, w28_face, w27_concentration, w26_cluster_audit,
w34_audit, w34_halfcex), and experiments/out/w35_charge/stress_checks.py.

## ITEMS (verdict CONFIRMED / REFUTED / UNRESOLVED + calibrated P each)
B1. THE CONSTANTS CHAIN (w35_quantifier): re-derive C_mu = C_sf + 1 + A and
    C_D = 4(1+2delta_0)(C_sf+1+A) from the w30/w31 reductions with |a_t| <= A
    replacing |a_t| <= 1, line by line. Check the L_eta and L4 lines too.
    Any dropped term or wrong factor?
B2. THE ROUTING CAVEAT CONSISTENCY: w35_quantifier says the w27 scalar
    telescope needs the exact-max sign fact 0 <= 1-a_s <= 2 and must be
    routed around for theta < 1. But w35_charge's banked deficit bound
    (its section 2) ALSO uses that sign fact. Is the deficit bound still
    valid in the theta = 1 (exact max-volume tie) selection class that
    w35_charge actually uses? Is there an inconsistency if the final theorem
    wants theta < 1? State exactly which delta_0/theta combinations are
    covered by the two documents TOGETHER.
B3. THE CHAIN END-TO-END: take the registry contract (exists theta-quasi U
    with max_s SF_s <= C_sf delta) and verify it actually implies the global
    W-free O(sqrt(delta)) statement through the audited links, with the
    routing caveat respected. Write the composed theorem statement with all
    hypotheses explicit. Flag any link whose own audit status is weaker than
    'audited' (check the upstream notes' own status tags).
B4. w35_charge's SELECTION WELL-DEFINEDNESS + stress checks: re-run
    stress_checks.py; verify the min-max chart claims (best max-ratio
    EXACTLY 1 on all four families) independently; check the selection
    argmin is over ALL exact max-volume ties (the tie enumeration in the
    script — is it exhaustive or heuristic?).
B5. THE (CHARGE) FORMULATION: is (CHARGE) actually equivalent to / sufficient
    for the registry contract as claimed (q_si <= C(delta_0), nu_i <= delta
    => SF <= C delta — fine), and is anything LOST relative to what the
    chain needs (per-s vs max-s, the same U* for all s simultaneously)?
B6. FRESH EYES: anything else suspicious in either document. In particular:
    does the staircase-at-delta-1/2 "ratio exactly 1 in the min-max chart"
    claim secretly rely on the exact ties existing (P_p = e_p) — i.e., is
    there a PERTURBED staircase (epsilon-broken ties) where the theta = 1
    selection class collapses to the bad chart alone and Phi(U*) = m delta?
    If yes, the theta < 1 slack is NOT optional — quantify the minimal slack.

## DELIVERABLE (verdict-first; long form to audit.md)
Verdict table (item, verdict, P, one line), then evidence. B6's perturbed
staircase question is the highest-value item — answer it with an exact or
high-precision construction, not hand-waving.
