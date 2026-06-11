# w21_recode: the mass-removed boundary-recoding lemma (the convergent blocker)

You are a codex (gpt-5.5) PROVER with numerics. Two independent workers have
converged on ONE missing object: a quantitative theory of recoding to boundary
H-M strata when tiny positive entries die along a variety arc. It is now the
single blocker for (a) the uniform two-scale visibility lemma, (b) the
second-order race's sharp cases, and plausibly (c) the local linear law by
strata induction.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w21_recode.
PROGRESS PROTOCOL: append one short line per stage to progress.md.
ARTIFACT RULE: long-form proof to proof.md, NEVER answer.md.

## READ FIRST
1. agent-A/explorations/classical-portfolio/notes/swarm-answers/w20_t1_audit.md
   — the audit that killed the naive recoding: dropping all entries below a
   threshold theta can move the recoded H-M point ~ n*theta away while its
   surviving min mass is only ~ theta (hypothesis violations by 62.7-314x).
   ITS PRESCRIPTION (your starting point): restate in terms of the TOTAL MASS
   REMOVED from each block, q_s = sum_{j in D_s} pi_s(j), not the threshold;
   recode degenerate transient faces (alpha_is -> 0) too. Also the repaired
   fixed-mass visibility lemma you may import (ambient: eps <= min{mu/8,
   tau/64, eta*tau/64, 1/64} with the LP support margin eta).
2. notes/swarm-answers/w21_second.md — the sharp second-order cases are
   exactly boundary recoding events: arcs whose H/delta -> 2 cross a tiny-
   entry scale; the clean fixed-base race is empty (max_local_ratio = 0).
3. notes/swarm-answers/w19_tangent.md (+ _audit) — the banked first-order
   lemma (dot-H+ <= 2 dot-delta, C = 2 dimension-free) available at EVERY H-M
   base point, including boundary-stratum points (verify the statement's
   applicability at the recoded base — it quantifies over all H-M points, so
   it applies; say so explicitly).
4. notes/swarm-answers/w18_variety.md — strata, dimensions, the exact chart.

## TARGET (the recoding lemma + the induction)
L1 (the lemma): let P_0 be an H-M point and let D = {(s,j) : pi_s(j) small}
be a set of low-mass recurrent coordinates with per-block removed masses
q_s = sum_{j in D_s} pi_s(j) (and similarly degenerate transient coefficients
alpha_is <= q'). Construct the RECODED H-M point P_0' on the boundary stratum
(remove D from the blocks, renormalize pi_s' = pi_s|_{C_s \ D_s} / (1 - q_s);
reassign the removed coordinates as transient rows with explicit mixtures —
choose the assignment that minimizes distance; degenerate transient faces
drop their vanishing coefficients). PROVE with explicit constants:
  max-row-l1 distance(P_0, P_0') <= A * (sum_s q_s + q'),
  mu(P_0') >= mu-bound in terms of the SURVIVING masses (not theta),
  |H(P) - H'(P)| and |delta-references| transform controllably, and the
  visibility margins of surviving recurrent vertices change by at most
  O(sum q_s + q') (use the ambient fixed-mass lemma's margin calculus).
The KEY DESIGN CHOICE the naive version got wrong: all bounds in terms of
REMOVED MASS, never the threshold or n * theta. Verify your constants against
the audit's 62.7-314x stress family (they must now PASS — re-run its numerics).
L2 (the two-scale assembly): combine L1 + the ambient fixed-mass lemma into
the REPAIRED uniform two-scale visibility statement: for ANY H-M base and any
arc, either the fixed-mass lemma applies directly, or recode (possibly
iteratively — each recoding strictly shrinks the support pattern, so <= n
steps) and apply it at the recoded base. State the resulting uniform radius
honestly (its dependence on the degeneration profile).
L3 (state precisely, attempt if time permits): the strata induction toward the
LOCAL linear law: induct on the support pattern; at each base the banked
first-order lemma + L2 control the non-boundary directions; boundary-crossing
arcs recode and recurse. Identify exactly what estimate (if any) is still
missing after L1+L2 — if none, assemble the local law (fixed n honest
dependence) — that would be the campaign landmark; do NOT overclaim: every
constant explicit, every step derived.

## NUMERICS
Re-run the w20_t1_audit stress family (experiments/out/w20_t1_audit/
independent_visibility_audit.py has the conventions) against YOUR recoded
bounds — the 62.7-314x violations must become passes. Then stress L1 with
mixed-rate degenerations (several q_s at different scales; simultaneous
alpha-face degenerations). Then test L3's induction numerically on the
w21_second sharp boundary events (experiments/out/w21_second/).

## DELIVERABLE (verdict-first; long form to proof.md)
VERDICT: L1+L2 PROVED (+ L3 status: ASSEMBLED / the one remaining estimate) /
L1 ONLY / DIED-AT (the exact failed bound). Constants explicit; the
removed-mass design verified against the audit's stress family. Calibrated
P(L1+L2 survive audit), P(L3 assembles the local law). Save code + outputs.
