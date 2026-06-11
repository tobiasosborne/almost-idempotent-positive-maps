# w19_tangent_audit: hostile audit of the tangent-cone lemma (dot-H+ <= 2 dot-delta)

You are a codex (gpt-5.5) HOSTILE AUDITOR. A prover claims the first genuinely
new proved lemma of the current campaign phase: the first-order normal-cone
form of the linear law, with a dimension-free sharp constant C = 2. If it
survives you, it gets banked and becomes the base of a curve-selection upgrade.
Break it if you can. The campaign's cardinal failure mode is a confident,
plausible, WRONG claim.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w19_tangent_audit.
PROGRESS PROTOCOL: append one short line per stage to
/tmp/codex-sigma-wall/w19_tangent_audit/progress.md.

## THE CLAIM (read in full)
agent-A/explorations/classical-portfolio/notes/swarm-answers/w19_tangent.md —
the statement, the FULL recovered proof note, and the decider summary.
Statement: for every H-M stochastic-idempotent normal form P_0 (recurrent
blocks C_1..C_k with laws pi_s, transient set T with mixtures alpha_i) and
every variety tangent A (P_0 A + A P_0 = A, A1 = 0), the upper Dini derivative
of the height along any exact C^1 arc P(t), P(0) = P_0, P'(0) = A satisfies
dot-H+ <= 2 * dot-delta, with dot-delta(A) = max_i sum_{j: P0_ij = 0} (-A_ij)_+,
and C = 2 independent of n, k, partition, mixtures, and minimal block mass.

## CONTEXT
1. report/kernel-conjecture.tex (under agent-A/explorations/classical-portfolio/)
   — H, W (multiplicity-correct), hidden, delta = row negative mass.
2. notes/swarm-answers/w18_variety.md — the variety structure the proof uses
   (tangent equations; the first-order normal cost formula — re-derive it too).
3. notes/swarm-answers/w19_leftcone.md — the adjacent lemma that was REFUTED
   by an exact n=4 family; check whether that family (or its tangent data)
   stresses THIS lemma.

## AUDIT TASKS (derive-first)
1. RE-DERIVE the tangent characterization at an H-M point: P_0 A + A P_0 = A,
   A1 = 0 — work out the block form of A against the H-M zero pattern
   (recurrent diagonal blocks, vanishing transient columns, off-diagonal
   recurrent blocks zero). Verify the proof's claimed structure of admissible
   first-order moves. Any error here voids everything.
2. RE-DERIVE the height derivative: H is a max-min over the visible hull. The
   proof works with a "frozen/recurrent-hull" upper derivative and claims
   (a) it bounds the true upper Dini derivative because visible-set changes
   only LOWER first-order height, and (b) recurrent-cluster visibility is
   stable at o(t). Attack both claims: construct arcs where a NEW vertex
   becomes visible at rate O(t) and check whether the true H derivative can
   exceed the frozen one; check the (rho,kappa)-visibility rescaling argument
   in the proof note. This semicontinuity step is the most likely soft spot.
3. RE-DERIVE the core inequality on the n = 3, k = 2 model (the proof has an
   explicit section) and CHECK THE CONSTANT: is 2 forced, or does the proof
   actually give 2 + O(something)? Where is sharpness attained (the proof says
   the recurrent-hull derivative is sharp at C = 2 — exhibit the optimizing
   direction and verify by hand).
4. INDEPENDENT NUMERICS: re-implement the decider YOURSELF (do not run the
   claimant's tangent_cone_decider.py except to compare formats): sample H-M
   strata (include EXTREME geometries the claimant may have under-sampled:
   tiny block masses pi_s with entries ~ 1e-6; many transients t >> k;
   k = 1; mixtures alpha on stratum boundaries — alpha with zero entries,
   i.e. transient rows on faces; n up to ~12), solve the same LP (max frozen
   dH subject to dot-delta <= 1, ||A||_inf <= 1, A tangent) and the dangerous
   cone (dot-delta = 0). Report your max C and any counterexample direction.
5. ARC-LEVEL spot check: take your worst LP direction A, integrate a short
   exact arc in the variety (use the corner chart / Newton retraction onto
   {P^2 = P}), and verify numerically that H(P(t))/t stays <= 2*dot-delta + o(1)
   — this tests the lemma BEYOND first order and the frozen-hull claim at once.
6. SCOPE check: the lemma quantifies over H-M base points. The intended
   application (curve selection from a hypothetical small-delta counterexample
   to the linear law) needs the arc to START at the H-M locus. State precisely
   what is still missing for the local linear law (the proof note has a
   "Remaining gap" — assess whether its description is honest and complete;
   in particular stratum-boundary base points and arcs not C^1 at 0).

## DELIVERABLE (verdict-first)
VERDICT: LEMMA HOLDS (constant confirmed or corrected; the semicontinuity step
verified) / LEMMA HOLDS WITH REPAIR (state the repaired statement + proof
sketch) / LEMMA BROKEN (the failing arc/direction with numbers). Then your
independent decider results (max C over your sampling, worst strata), the
arc-level spot check, the honest remaining-gap assessment, and calibrated
P(verdict survives further audit). Save all code + outputs. Do not soften.
