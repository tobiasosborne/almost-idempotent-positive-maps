# w17_antecedent: can sigma_tilde > tau coexist with real height? (the decisive decider)

You are a codex (gpt-5.5) numerical decider. The sigma-barrier was just crossed
for the FIRST time (hidden v, sigma_tilde/tau = 1.63) — but at NEGLIGIBLE height
(H/tau = 0.016) and large delta (0.228). The entire campaign now turns on ONE
empirical question: can a hidden top vertex have sigma_tilde > tau AND
substantial height (H > 0.1*tau, ideally H ~ tau)? The record (67k+ instances,
six campaigns) contains ZERO such instances. Find one or map the obstruction.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w17_antecedent.
PROGRESS PROTOCOL: append one short line per stage to
/tmp/codex-sigma-wall/w17_antecedent/progress.md.

## READ FIRST
1. agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex — all
   definitions + §5 (the corner theorem CAP: the proved wall H/tau <=
   2(2-sqrt(3)) ~ 0.536 for the 2-family — your search lives BELOW that; the
   empirical linear law delta >~ H/2).
2. notes/swarm-answers/w16_nlopt.md (same exploration dir) + the instance files
   in experiments/out/w16_nlopt/ (w16_best_factorization.json: P = L B with
   B L = I, n = 7, k = 4 — your warm start) + the worker's method (active-set
   continuation at the rho threshold).
3. experiments/out/w15_refuter/w15_refuter_search.py — the independent verifier
   conventions (multiplicity-correct W, hiddenness LP, sigma_tilde, H).

## TASK
1. Build a rigorous verifier from the definitions (you may adapt the w15
   verifier). EVERY reported instance must pass it; never trust the optimizer's
   own penalty values.
2. HOMOTOPY/CONTINUATION from the w16 instance: maximize H/tau subject to
   (exactly idempotent P = L B, B L = I; v hidden — multiplicity-correct;
   sigma_tilde_v > tau). Use a path-following / penalty-annealing strategy:
   alternate (a) gradient steps increasing H, (b) projection back to the
   feasible set (hiddenness margin + sigma_tilde gate). Track the Pareto front
   (H/tau vs sigma_tilde/tau vs delta) at every accepted point; save it.
3. DIMENSIONS: stay at (7,4) first, then try (8,4), (9,4), (10,5), (12,6) —
   more room can buy height; also try DOUBLING constructions: direct sums /
   couplings of the w16 instance with a high-height corner-type instance (the
   corner family has H/tau = 0.536 but sigma_tilde = 0: can a coupling
   interpolate? — the natural refuter move the record never tested WITH a
   sigma_tilde > tau seed in hand).
4. Also run the reverse probe: at FIXED H/tau in {0.05, 0.1, 0.2}, maximize
   sigma_tilde/tau. Report the achieved frontier per H-level: this measures the
   TRADEOFF the conjectures live on.
5. DECISION-GRADE OUTPUT either way:
   - ANTECEDENT REALIZED (hidden, sigma_tilde > tau, H > 0.1*tau, delta <= 0.25,
     verified): save matrix + full certificate; this would (with the proved
     cloning construction) REFUTE the raw floor AND be the first genuine test
     object for the quotient floor — also compute its quotient carrier
     structure (coincident-row classes, quotient path products) and report
     whether the quotient floor holds ON IT.
   - NOT REALIZED: the quantified tradeoff frontier (max H/tau as a function of
     sigma_tilde/tau), where the continuation stalls (binding constraints,
     which rows' negative budgets saturate), and whether the stall matches the
     linear law delta >= H/2 or a sharper sigma_tilde-aware bound — fit the
     empirical boundary and CONJECTURE its closed form (that conjecture is the
     campaign's next proof target).
6. Save all scripts + the Pareto front JSON + best instances in your workdir.

## DELIVERABLE (verdict-first)
VERDICT: ANTECEDENT REALIZED (certificate + quotient-floor test result) /
NOT REALIZED (the frontier + the conjectured boundary law in display math).
Then calibrated P(the antecedent regime is empty), and the single most
informative next experiment.
