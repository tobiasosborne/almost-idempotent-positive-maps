# w37_tree: prove (TREE)/(DECAY) in the theta = 1/2 class — the last display

You are a codex (gpt-5.5) PROVER. Three provers have compressed the classical
campaign to one display: the shear-tree decay bound. The truth is now sharply
calibrated: the selected-chart constant is ~2 (no-center path family), the
decay shape is geometric (saturation 1 -> 2 like sum 2^{-r}), and the naive
product bound FAILS (per-generation branching mass |a| * sum|w_t| <= 2 — you
must find where the delta-budget pays for the branching).

Repo root: /home/tobias/Projects/almost-idempotent-positive-maps (readable).
Workdir (writable): /tmp/codex-sigma-wall/w37_tree.
PROGRESS PROTOCOL: one short line per stage to progress.md.
ARTIFACT RULE: long form to proof.md, NEVER answer.md. sympy/HiGHS; gurobi
broken in sandbox (write-not-run any nonconvex script).

## READ (under agent-A/explorations/classical-portfolio/notes/swarm-answers/)
1. w36_charge.md — FULL appendix: the (DECAY) and (TREE) displays, the
   no-center path family (your acid test), the shear formula (S), and the
   orchestrator's crux note in the header (branching mass 2 — divergent —
   the decay must be bought by the delta-budget).
2. w36_audit.md — B6: the perturbed staircase forces selection over the
   THETA = 1/2 class (volume >= Vol_max/2; coefficients |a_t| <= 2 there,
   NOT <= 1 — adjust every box bound). Your theorem must hold with the B6
   family (eps in (0, 1/2)) as a stress check.
3. w35_charge.md sections 1-3 (selection, deficit, sufficient criterion) and
   w35_quantifier.md (the chain contract you feed; theta = 1/2 cost A = 2).
4. Scripts to reuse: experiments/out/w36_charge/*.py (exact tie/selected-chart
   auditors, the path and no-center-path families).

## THE TARGET
delta_0 = 1/4 (0.3 if clean). Selection class: actual-row bases U with
Vol(U) >= (1/2) Vol_max(P). Selector: U* = argmin over the class of
Phi(U) = max_s SF_s(U) (lexicographic tie-break). Prove

  Phi(U*) <= C(delta_0) * delta(P),   C dimension-free.

Sufficient and preferred route: (DECAY) for the multi-swap operation —
there is a V in the class with Phi(V) <= alpha Phi(U) + K delta, alpha < 1
— applied at U* gives Phi(U*) <= K delta/(1-alpha). Equivalent: (TREE).

## WHERE THE DECAY MUST COME FROM (work these, in order)
T1. PAY-PER-GENERATION: when excess shears from representative s to
    coordinate t along a swap, the row i that carries the sheared mass has
    a_s(i) reduced (formula (S): a'_t(i) = a_t(i) - a_s(i) w_t). Track the
    DIAGONAL coefficient along a shear path: does each generation multiply
    the carried excess by a_s(i_l) <= 1 AND force the carrying rows to be
    progressively farther from the s-face? If the carried excess at
    generation r is supported on rows with a_s <= 2^{-r}-ish, the deficit
    bound (valid form in the theta = 1/2 class: 1 - a_s in [-1, 3] — NOT
    nonneg; rework it: sum_j (B_sj)_+ |1 - a_s(j)| needs its own bound,
    possibly via sum rules + |a| <= 2) kills the tail.
T2. LP-DUAL WITH SWAP CONSTRAINTS AT SMALL k: for the path and no-center
    path families k <= 8, solve max Phi(U*) subject to (BL = I, negativity,
    AND the finitely many swap-comparison constraints Phi(U*) <= Phi(V) for
    all V in the theta = 1/2 class) exactly; extract the dual multipliers on
    the swap constraints; their structure IS the charge assignment q. If the
    multipliers have a uniform pattern across k (geometric along the path),
    convert the pattern to a general proof.
T3. RESTRICTED FIRST VERSION: prove (TREE) for shear trees of depth <= 2
    with explicit constants, and identify exactly which configurations
    require depth >= 3 (do ANY known families? the path family is depth ~k —
    check whether its selected chart actually requires deep recursion or
    whether one global recentering suffices).

## MANDATORY STRESS CHECKS (exact rational; reuse the w36 auditors)
transverse pair a = 1/4; dense pair k = 7; staircase m = 2, 3; PERTURBED
staircase (B6: m = 5, eps = 1/1000 AND eps = 2/5); path-tie k = 6, 8;
no-center path k = 6, 8. Your claimed C must clear ALL of them in the
theta = 1/2 selected chart.

## DELIVERABLE (verdict-first; long form to proof.md)
VERDICT: PROVED (Phi(U*) <= C delta, theta = 1/2, full proof + all checks) /
PARTIAL (the exact missing display, strictly smaller than (TREE)) /
COUNTEREXAMPLE (an instance beating the theta = 1/2 selected chart) /
DIED-AT. Calibrated P's. Save everything.
