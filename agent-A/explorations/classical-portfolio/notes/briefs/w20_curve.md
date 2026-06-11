# w20_curve: from the audited tangent-cone lemma to the LOCAL linear law

You are a codex (gpt-5.5) PROVER with numerics. The campaign has just banked its
first audited new lemma: the first-order normal-cone inequality on the
idempotent variety. Your job: the upgrade to the LOCAL linear law near the
delta = 0 locus — including the audit's named missing piece.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w20_curve.
PROGRESS PROTOCOL: append one short line per stage to
/tmp/codex-sigma-wall/w20_curve/progress.md.
ARTIFACT RULE: write your long-form proof/verdict to proof.md in your workdir —
NEVER to answer.md (it gets overwritten by the capture mechanism).

## READ FIRST
1. agent-A/explorations/classical-portfolio/notes/swarm-answers/w19_tangent.md —
   the lemma + FULL proof note: dot-H+(A) <= 2 * dot-delta(A) at every H-M point
   P_0 and variety tangent A, C = 2 dimension-free.
2. notes/swarm-answers/ w19_tangent_audit answer (if archived as
   w19_tangent_audit.md) — the audit's repairs: (a) sharpness only for the
   FROZEN recurrent-hull derivative; (b) the pointwise Dini statement is fine
   but does NOT give a uniform local radius over tiny recurrent masses — an
   explicit TWO-SCALE VISIBILITY LEMMA is needed; (c) a finite-scale stress:
   H/t ~ 2 above a 1e-6 active-entry scale on a tiny-mass stratum (no Dini
   failure, but the uniformity danger made concrete).
3. notes/swarm-answers/w18_variety.md — the exact chart P(C,D) (diagonal
   deviations quadratic: P_EE - I = -CD + O(3), P_FF = DC + O(3)), the
   stratification, dimension counts.
4. report/kernel-conjecture.tex §5 — CRITICAL: "naive compactness to delta = 0"
   is a RECORDED DEAD ROUTE ("the visible set W jumps in limits"). Your curve-
   selection/compactness argument MUST explicitly handle the W-jump — the
   two-scale visibility lemma is presumably the cure; make the connection
   precise or report that it is not.

## TARGET (in increasing strength; deliver the strongest you can prove)
T1 (the two-scale visibility lemma — the audit's named gap): an explicit lemma
   giving, for every H-M point P_0 with recurrent masses bounded below by mu
   (and also the honest mu -> 0 version with the two scales separated), a
   RADIUS r(P_0) and constants such that along any variety arc from P_0 of
   length < r, the visible set's relevant part (the recurrent-cluster
   vertices) stays visible and new visible vertices only lower H — with
   r quantified (its dependence on mu, block count, n: state exactly).
T2 (local linear law, fixed n): there exist c(n), r(n) > 0 such that every
   exact row-stochastic idempotent P within variety-distance r(n) of the H-M
   locus satisfies H(P) <= c(n) * delta(P). Route: T1 + second-order control
   in the exact chart (the diagonal corrections are quadratic — bound the
   second-order height and negative-mass errors along the chart) + curve
   selection / stratum-boundary handling (strata meet; arcs may leave a
   stratum: handle by upper semicontinuity of the stratum data or by working
   in the closure with the boundary's own H-M structure).
T3 (state only, honestly): what survives dimension-free? The first-order
   constant 2 is dimension-free; track every place T1/T2 introduce n- or
   mu-dependence and list them — that list is the next campaign frontier.
   ALSO state the GLOBAL gap honestly: the local law covers a neighborhood of
   the H-M locus; the full small-delta linear law additionally needs every
   small-delta idempotent to BE in that neighborhood (the B-S normal-form
   distance question — do NOT claim it; it is the campaign's standing target).

## METHOD
- Derive T1 from the H-M structure: visibility of a recurrent-cluster vertex
  is an LP-margin statement; bound the margin's modulus of continuity along
  variety arcs (the exposing functional of pi_s at delta = 0 has an explicit
  margin in terms of block masses — compute it).
- For T2's second-order step, work in the exact chart: H and delta along
  P(tC, tD) have explicit expansions; the first-order term is the lemma; bound
  the second-order terms by ||(C,D)||^2 times explicit constants.
- NUMERICS (python3/numpy/scipy): stress T1's radius formula on the audit's
  tiny-mass stress stratum (active-entry scale 1e-6); verify T2 numerically on
  arcs that CROSS stratum boundaries; reuse
  experiments/out/w19_tangent/tangent_cone_decider.py conventions if helpful.

## DELIVERABLE (verdict-first; long form to proof.md, summary as final message)
VERDICT: T1+T2 PROVED (proofs in display math; r and c with explicit
dependence; the W-jump dead-route explicitly disarmed or not) / T1 ONLY /
DIED-AT (the exact failed estimate). Then the T3 honest dependence list + the
global-gap statement, numerics, and calibrated P(T2 as proved survives audit),
P(dimension-free upgrade reachable). Save code + outputs.
