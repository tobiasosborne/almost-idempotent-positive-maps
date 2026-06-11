# w21_recode_audit: hostile audit of the mass-removed recoding lemma (L1+L2)

You are a codex (gpt-5.5) HOSTILE AUDITOR. A prover claims the convergent-
blocker lemma: mass-removed boundary recoding (L1) + the repaired uniform
two-scale visibility assembly (L2). A previous naive version was killed by an
audit (62.7-313x violations); this one claims to pass that exact stress family.
Break it. Cardinal failure mode: a confident, plausible, WRONG claim.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w21_recode_audit.
PROGRESS PROTOCOL: short line per stage to progress.md.
ARTIFACT RULE: long form to audit_report.md, NEVER answer.md.

## THE CLAIM
agent-A/explorations/classical-portfolio/notes/swarm-answers/w21_recode.md
(full proof note appended) — key claims:
- L1: recoded boundary H-M point P0' with ||P0 - P0'||_{infty,1} <= 2(sum_s q_s + q')
  (q_s = removed mass per block, q' = dropped transient-face mass); survivor
  mass mu(P0') >= min surviving original mass; survivor relative coordinate
  shift exactly q_s; transient face-drop row shift = 2 r_i.
- L2: iterate (<= n steps, support pattern strictly shrinks) + the ambient
  fixed-mass visibility lemma (notes/swarm-answers/w20_t1_audit.md — the
  REPAIRED version with margin eta and eps <= min{mu/8, tau/64, eta*tau/64,
  1/64}) => a uniform two-scale visibility statement.
- The w19 first-order lemma applies at every recoded base (it quantifies over
  all H-M points).

## CONTEXT
1. notes/swarm-answers/w20_t1_audit.md — the audit that killed the naive
   version + its stress family (experiments/out/w20_t1_audit/
   independent_visibility_audit.py) — the claimant says the removed-mass
   bounds now pass it; INDEPENDENTLY verify (your own implementation).
2. notes/swarm-answers/w21_second.md — the boundary events this should resolve.
3. notes/swarm-answers/w19_tangent.md + w19_tangent_audit.md — the banked lemma.
4. notes/swarm-answers/w18_variety.md — strata/charts.

## AUDIT TASKS (derive-first)
1. RE-DERIVE L1's constants: the recoding construction (renormalize pi_s' =
   pi_s|survivors / (1 - q_s); reassign removed coordinates as transient rows;
   drop degenerate faces). Check: (a) is P0' actually an EXACT H-M idempotent
   (verify the reassigned transient mixtures' row sums and the zero-pattern —
   construct small explicit examples and verify P'^2 = P' exactly); (b) the
   distance bound 2(sum q_s + q') — derive it row class by row class (recurrent
   survivors, removed coordinates, transient rows whose mixtures reference
   renormalized blocks — the alpha_is pi_s -> alpha_is pi_s' shifts compound:
   does the TRANSIENT row shift really stay <= 2(sum q_s + q') when MANY blocks
   lose mass simultaneously?); (c) mu(P0') — is "min surviving original mass"
   right, or does renormalization by 1/(1-q_s) matter at higher q_s? State the
   valid q_s range.
2. THE ITERATION (L2): each recoding step's errors COMPOUND — sum over <= n
   steps: is the total still controlled by the TOTAL removed mass (telescoping)
   or can it blow up by a factor n (the naive trap reborn one level up)?
   Derive the compounded bound explicitly. Also: the iteration's stopping
   condition (when does the fixed-mass lemma apply at the current base?) — is
   it well-defined for EVERY degeneration profile, or can an arc oscillate
   (mass leaving and re-entering blocks) so no finite recoding stabilizes?
   Construct the nastiest oscillating arc you can.
3. INDEPENDENT NUMERICS: re-implement the removed-mass checks YOURSELF; run
   (a) the original w20 stress family, (b) the claimant's 12 mixed-rate cases
   + your own (multi-block simultaneous, near-total-block-removal q_s -> 1,
   transient-only degenerations), (c) the w21_second sharp boundary events
   (experiments/out/w21_second/) — does L2's recoded visibility actually
   resolve them (the transition ratio 2.0000000000392 cases)?
4. L3 ASSESSMENT: with L1+L2 in hand, restate precisely what the remaining
   finite-jet normal projection bound says and whether the strata induction
   has any OTHER unstated gap (e.g. the arc-scale estimate for tau(t) from
   the w20 audit — is it subsumed, still open, or newly relevant?).

## DELIVERABLE (verdict-first; long form to audit_report.md)
VERDICT: L1+L2 HOLD (constants confirmed/corrected + valid ranges) / HOLD
WITH REPAIR (the repaired statements) / BROKEN (the compounding/oscillation/
exactness failure with explicit example). Then your independent numerics
tables, the L3 gap restatement, and calibrated P(verdict survives further
audit). Do not soften.
