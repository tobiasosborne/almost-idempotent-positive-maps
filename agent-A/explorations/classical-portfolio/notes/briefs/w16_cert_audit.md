# w16_cert_audit: independent certification of the claimed sigma-barrier crossing

You are a codex (gpt-5.5) INDEPENDENT VERIFIER. A numerical worker claims the
FIRST verified instance of a hidden top vertex with sigma_tilde > tau =
sqrt(delta) (it would correct the campaign's measured frontier). The campaign's
cardinal failure mode is a confident, plausible, WRONG claim — your job is to
certify or kill this instance with code the CLAIMANT DID NOT WRITE.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w16_cert_audit.
PROGRESS PROTOCOL: append one short line per stage to
/tmp/codex-sigma-wall/w16_cert_audit/progress.md.

## THE CLAIM (read agent-A/explorations/classical-portfolio/notes/swarm-answers/w16_nlopt.md)
Instance: agent-A/explorations/classical-portfolio/experiments/out/w16_nlopt/
w16_best_matrix.json (+ w16_best_factorization.json, w16_best_certificate.json).
Claimed: n = 7, k = 4, delta = 0.2284, sigma_tilde = 0.7769, tau = 0.4779,
sigma_tilde/tau = 1.626, W = {0,1,2,3}, hidden top vertex v = 4, H/tau = 0.0158,
exact idempotence to 2.2e-16.

## RULES
- Do NOT reuse the claimant's verification code (w16_nlopt_search.py /
  w15_verifier_reuse.py) except to read file formats. Write your OWN verifier
  from the DEFINITIONS in report/kernel-conjecture.tex (delta = row negative
  mass; tau = sqrt(delta); multiplicity-correct row vertices def:vertex; W =
  visible (exposed) vertices; hidden; sigma_tilde_v = positive mass of row v on
  columns whose rows lie strictly off C_W = conv W; H = height of the top
  vertex; the deficit g). Cross-check the prior independent implementation
  experiments/out/w15_refuter/w15_refuter_search.py ONLY as a convention
  reference if a definition is ambiguous — flag any convention ambiguity you hit.
- python3 + numpy/scipy available (HiGHS via scipy.optimize.linprog).

## TASKS
1. FLOATING CHECK: load the matrix; verify P^2 = P, P1 = 1, the claimed delta,
   the row-vertex structure (which rows coincide geometrically?), W via
   exposedness LPs (multiplicity-correct), hiddenness of v = 4 (no exposing
   functional: solve the separation LP both directions and report the optimal
   margins + dual certificates), sigma_tilde_v, H, tau. Report every number
   independently; compare to the claim.
2. EXACTNESS HARDENING: attempt to RATIONALIZE the factorization (L, B with
   B L = I): round to rationals (fractions module, continued-fraction
   convergents per entry; re-solve B L = I exactly if needed by adjusting one
   block) to produce an EXACTLY idempotent rational P_rat near the float one;
   re-verify ALL claims for P_rat with exact rational arithmetic (your own code;
   LPs may stay float but margins must be >> float error, report them). If
   rationalization fails, do an interval/perturbation analysis: bound how the
   certificate quantities move under ||P - P_exact|| <= eps_machine-scale
   perturbations, and state whether the float certificate is decision-grade.
3. CONTEXT CHECKS: (a) confirm H/tau ~ 0.016 — i.e. this does NOT enter the
   floor conjectures' antecedent (needs H > B*tau) nor contradict the recorded
   "no instance with sigma_tilde > tau AND H > 0.1*tau"; (b) check consistency
   with the proved sigma-height-collapse lemma and the corner constraints
   (any tension = a red flag for a definitional error somewhere — investigate);
   (c) delta = 0.228 is near the search cap: does the instance family survive
   at delta <= 0.1 (quick local continuation: rescale/perturb and re-verify, a
   few attempts suffice — this is a bonus, not the gate).
4. Also verify the SECOND saved instance (w16_scale_*.json) the same way
   (floating check only).

## DELIVERABLE (verdict-first)
VERDICT: CERTIFIED (float) / CERTIFIED (exact rational — give the rational
instance file path in your workdir) / BROKEN (the failing check, exactly,
with numbers). Then the full independent number table (yours vs claimed), the
hiddenness dual certificates, the perturbation analysis, the context-check
results, and calibrated P(the instance is genuine). Save your verifier +
any rational instance in your workdir.
