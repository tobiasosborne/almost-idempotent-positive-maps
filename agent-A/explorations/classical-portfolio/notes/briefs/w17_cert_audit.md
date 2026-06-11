# w17_cert_audit: certify or kill the claimed ANTECEDENT-REALIZING instance

You are a codex (gpt-5.5) INDEPENDENT VERIFIER. A numerical worker claims the
first instance EVER realizing the floor conjectures' antecedent: hidden top
vertex with sigma_tilde > tau AND H > 0.1*tau. If certified this falsifies a
ledger item of the campaign record and (via the proved cloning construction)
refutes the raw-index floor at delta0 >= 0.233. The hiddenness margin is
RAZOR-THIN (t*/kappa = 0.99988) — that margin is your primary target.
The campaign's cardinal failure mode is a confident, plausible, WRONG claim.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w17_cert_audit.
PROGRESS PROTOCOL: append one short line per stage to
/tmp/codex-sigma-wall/w17_cert_audit/progress.md.

## THE CLAIM
Read agent-A/explorations/classical-portfolio/notes/swarm-answers/w17_antecedent.md
(if absent: /tmp/codex-sigma-wall/w17_antecedent/answer.md + verdict.md).
Instances (n = 10, k = 5, hidden v = 5):
- MAIN: /tmp/codex-sigma-wall/w17_antecedent/targeted_best/
  fine_best_certificate.json + fine_best_factorization.json —
  delta = 0.23293, H/tau = 0.10019, sigma/tau = 1.5467, t*/kappa = 0.99988.
- ROBUST companion: /tmp/codex-sigma-wall/w17_antecedent/targeted_robust/
  robust_certificate.json (+ factorization nearby) — H/tau = 0.10000,
  sigma/tau = 1.5521, t*/kappa = 0.99777.
(If the orchestrator has archived these under agent-A/explorations/
classical-portfolio/experiments/out/w17_antecedent/, prefer that copy.)

## RULES
Write your OWN verifier from the definitions in
agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex
(delta = row negative mass; tau = sqrt(delta); multiplicity-correct row
vertices; W = exposed; hidden; sigma_tilde; H; deficit g). Do NOT reuse the
claimant's w17_decider.py except to read formats. python3 + numpy/scipy.

## TASKS
1. FLOAT CHECK both instances: P^2 = P, P1 = 1, delta, all-rows-distinct,
   W (exposedness LPs with reported margins), hiddenness of v (BOTH directions:
   the separation LP and its dual; report t*, kappa, the active sets), sigma_tilde,
   H, tau. Compare every number to the claim.
2. THE MARGIN QUESTION (decisive): t*/kappa = 0.99988 means v is hidden by
   1.2e-4 relative. Quantify the sensitivity: how much entrywise perturbation
   flips v to exposed? If that radius is < 1e-9 the float certificate is NOT
   decision-grade — say so plainly. Then attempt EXACT RATIONAL hardening
   (continued-fraction rationalization of the factorization with exact
   B L = I; re-verify hiddenness with EXACT rational LP if feasible — fractions
   + a small exact pivot/simplex you write yourself, n = 10 is tractable for
   vertex-by-vertex checks; otherwise float LP with interval error analysis and
   an explicit statement of the certified margin). The deliverable must state:
   does an EXACT instance with hidden v, sigma > tau, H > 0.1*tau EXIST — yes,
   no, or undecidable-at-float-precision. The ROBUST companion (margin 2.2e-3)
   may certify where the main one fails — try it second but report both.
3. CONTEXT: (a) delta = 0.233 is ABOVE the corner scale delta* = (2-sqrt3)^2 ~
   0.0718 — confirm; state clearly that the small-delta regime is untouched.
   (b) linear law check: H <= ~2*delta on these instances? (c) Compute the
   quotient carrier structure + Pi for the main quotient component and check
   the claimant's Pi/tau ~ 2.5e-4 (the quotient-floor test object claim).
   (d) Re-run YOUR verifier on a few of the claimant's reported Pareto-front
   points (w17_final_pareto_front.json) to assess systematic bias.
4. If certified: produce the rational (or interval-certified) instance file in
   your workdir + a one-paragraph statement of exactly what record item is
   falsified and at what delta.

## DELIVERABLE (verdict-first)
VERDICT: CERTIFIED EXACT / CERTIFIED FLOAT-ONLY (with stated margin) / BROKEN
(the failing check + numbers) — separately for MAIN and ROBUST. Then the
independent number table, the sensitivity analysis, the context checks, and
calibrated P(an exact antecedent-realizing instance exists at delta <= 0.25).
Save verifier + any hardened instance in your workdir.
