# w21_second: the second-order tangent-cone problem (the T2 gap)

You are a codex (gpt-5.5) PROVER with numerics. The campaign's banked
first-order lemma (dot-H+ <= 2 dot-delta, C = 2 dimension-free, audited) fails
to close the LOCAL linear law because of ONE named estimate. Your job is that
estimate — equivalently, the second-order tangent-cone problem on the
dangerous cone.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w21_second.
PROGRESS PROTOCOL: append one short line per stage to progress.md.
ARTIFACT RULE: long-form proof to proof.md, NEVER answer.md.

## READ FIRST
1. agent-A/explorations/classical-portfolio/notes/swarm-answers/w20_curve.md —
   T1 (proved two-scale visibility) + the EXACT T2 failure:
   H <= 2*delta + O(||(C,D)||^2) does not close without
   ||(C,D)_{perp M}||^2 <= L_n * delta(P(C,D))   (the quadratic normal bound),
   where perp-M = normal to the H-M stratum WITHIN the idempotent variety.
   Also its numerics: worst stable LOCAL ratio H/delta = 2.000000000013 — the
   local law empirically holds with constant exactly 2.
2. notes/swarm-answers/w19_tangent.md + w19_tangent_audit.md — the banked
   lemma; NOTE the audit fact: ALL dangerous-cone directions (dot-delta = 0)
   have frozen first-order height D = 0. So on the dangerous cone BOTH H and
   delta are second-order: the race restarts one order down.
3. notes/swarm-answers/w18_variety.md — the exact chart P(C,D): diagonal
   deviations are -CD and DC + O(3); use it for all second-order expansions.

## THE PROBLEM (decompose it cleanly first)
Decompose a variety tangent A at an H-M point P_0 into:
(i) stratum-tangent directions (moves along the H-M family: re-base, harmless);
(ii) normal directions with LINEAR delta-cost (dot-delta > 0): the first-order
     lemma handles these;
(iii) the DANGEROUS CONE: dot-delta(A) = 0 but A not stratum-tangent — these
     are directions that increase entries at active zeros POSITIVELY or move
     within the nonneg cone's faces while leaving the H-M locus. For arcs with
     leading direction here, expand IN THE EXACT CHART to second order:
     delta(P(tA + ...)) = t^2 * q_delta(A) + O(t^3),
     H(P(tA + ...))     = t^2 * q_H(A) + O(t^3) (first-order H vanishes —
     audited fact). PROVE the second-order tangent-cone inequality:
       q_H(A) <= C_2 * q_delta(A)
     for an explicit C_2 (dimension-free if possible — track it), OR exhibit
     a dangerous-cone direction with q_delta = 0 < q_H (that would be a
     genuine local-law counterexample seed — decisive either way!).
     CAREFUL: q_delta(A) can vanish identically on directions whose second-
     order displacement also stays in the nonneg cone — iterate: such arcs may
     re-enter case (i)/(ii) at second order (the H-M locus is itself curved).
     Handle the iteration honestly (a finite jet argument or a Lojasiewicz-
     style finite-determinacy claim — if you need finite determinacy as an
     external fact, flag it as UNVERIFIED-LEAD).
THEN assemble: T1 (proved) + first-order lemma (banked) + your second-order
lemma => the LOCAL linear law H <= C*delta near the H-M locus (fixed n
acceptable; state every n/mu-dependence). State the assembly precisely; if a
gap remains between the jet-level inequality and the neighborhood statement,
name it.

## NUMERICS (do this FIRST — it tells you which side to prove)
Implement the dangerous-cone second-order decider: at sampled H-M points,
parametrize dangerous-cone directions (LP: dot-delta = 0, A tangent, A not
stratum-tangent), integrate exact short arcs in the chart (with the quadratic
correction), and measure the ratio H(t)/delta(t) as t -> 0. The w20 numerics
already suggest sup = 2 exactly — confirm on YOUR sampling (include the
tiny-mass stress family and stratum-boundary base points) and find where the
ratio is attained (which directions saturate? the same recurrent-hull
geometry as first order?).

## DELIVERABLE (verdict-first; long form to proof.md)
VERDICT: SECOND-ORDER LEMMA PROVED (+ the assembled LOCAL LINEAR LAW with
explicit constants and dependence) / COUNTEREXAMPLE DIRECTION (the seed, with
arc numerics) / DIED-AT (the exact failed estimate + the iteration depth where
it fails). Then the decider results, the honest assembly/dependence statement,
UNVERIFIED-LEAD list, and calibrated P(local law true with C = 2),
P(this route proves it). Save code + outputs.
