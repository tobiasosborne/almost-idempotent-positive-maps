# w16_nlopt: end-to-end nonlinear decider on the barrier delta/sigma_tilde^2 < 1

You are a codex (gpt-5.5) numerical decider. The w15 refuter's quantified barrier:
across 1368 verified exactly-idempotent signed matrices (plus a 67k-instance prior
record), NO instance achieves a HIDDEN top vertex with sigma_tilde_v > tau =
sqrt(delta) (best: delta/sigma_tilde^2 = 1.52). Its named most-promising remaining
degree of freedom: END-TO-END nonlinear optimization over the factorization (L,B)
with a W-aware loss, instead of fixing B and LP-completing. Run that search to a
decision-grade verdict.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w16_nlopt.
PROGRESS PROTOCOL: append one short line per stage to
/tmp/codex-sigma-wall/w16_nlopt/progress.md.

## READ FIRST
1. agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex — ALL
   definitions (delta = row negative mass; tau = sqrt(delta); hidden top vertex;
   sigma_tilde; multiplicity-correct vertices; W).
2. agent-A/explorations/classical-portfolio/notes/swarm-answers/w15_refuter.md —
   the predecessor's templates, obstruction numbers, and verifier conventions.
3. agent-A/explorations/classical-portfolio/experiments/out/w15_refuter/ — its
   code (w15_refuter_search.py has a robust W/H/sigma/path-product VERIFIER —
   reuse or re-derive it) and its best instances (w15_best_*.json) as warm starts.

## TASK
1. Parametrize EXACTLY idempotent P = L B with B L = I_k (rank k), n moderate
   (n <= 12, k <= 4 first; then push if promising). Loss: maximize
   sigma_tilde_v / sqrt(delta) subject to v hidden (use a smooth W-aware penalty:
   exposedness margins of the would-be exposing functionals; the LP dual gives
   the hiddenness certificate — re-verify candidate optima EXACTLY with the
   rigorous verifier, never trust the penalty).
2. Use scipy.optimize (SLSQP / trust-constr / basinhopping; numpy/scipy only, no
   network). Multi-start: random + the warm starts + perturbations of the s5
   exact all-shallow construction if reachable. Track the Pareto front of
   (delta, sigma_tilde, H): report the best delta/sigma_tilde^2 PER (n,k) and
   overall, and whether H/tau can be pushed up simultaneously.
3. DECISION-GRADE OUTPUT either way:
   - If you cross the barrier (verified instance, delta <= 0.25, hidden v,
     sigma_tilde_v > sqrt(delta)): print + save the matrix and the full
     certificate (delta, H, sigma_tilde, tau, W, the hiddenness LP certificate).
     This would be the FIRST antecedent-realizing instance ever — triple-check
     hiddenness with the multiplicity-correct vertex convention.
   - If not: report the best achieved frontier, where the optimizer stalls
     (which constraint binds: hiddenness margin vs negative-mass budget), and
     whether the stall geometry matches the corner theorem's cap
     (H/tau <= 2(2-sqrt(3)) ~ 0.536). Quantify: best delta/sigma_tilde^2 per
     template family, gradient-norm at stall, and the active-set pattern.
4. Save all scripts + JSON results in your workdir.

## DELIVERABLE (verdict-first)
VERDICT: BARRIER CROSSED (the certificate) / NOT CROSSED (the stall analysis:
binding constraints, best frontier numbers, active sets). Then calibrated
P(the barrier inequality "hidden => sigma_tilde <= C0*sqrt(delta)" is TRUE),
and the single most informative next numerical experiment.
