# w20_t1_audit: hostile audit of the two-scale visibility lemma (T1)

You are a codex (gpt-5.5) HOSTILE AUDITOR. A prover claims T1: the two-scale
visibility lemma — the uniformity repair demanded by the previous audit of the
tangent-cone lemma. Break it if you can. Cardinal failure mode: a confident,
plausible, WRONG claim.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w20_t1_audit.
PROGRESS PROTOCOL: append one short line per stage to progress.md in your
workdir. ARTIFACT RULE: long-form output to audit_report.md, NEVER answer.md.

## THE CLAIM
agent-A/explorations/classical-portfolio/notes/swarm-answers/w20_curve.md —
the full proof note (T1 section): for H-M points with recurrent masses bounded
below by mu, an EXPLICIT visibility radius within which recurrent-cluster
vertices stay visible along variety arcs and newly-visible vertices only lower
H; the mu -> 0 case handled by RECODING to the boundary H-M stratum before
applying the same argument.

## CONTEXT
1. notes/swarm-answers/w19_tangent.md + w19_tangent_audit.md — the banked
   tangent-cone lemma and the audit that demanded T1 (incl. the concrete
   tiny-mass stress: H/t ~ 2 above a 1e-6 active-entry scale).
2. notes/swarm-answers/w18_variety.md — the chart + stratification.
3. report/kernel-conjecture.tex §5 — the recorded "naive compactness / W-jump"
   dead route: T1 is supposed to disarm it; assess whether it actually does.

## AUDIT TASKS (derive-first)
1. RE-DERIVE the visibility margin: at an H-M point, the exposing functional
   for a recurrent-cluster vertex pi_s has an explicit LP margin in terms of
   block masses — recompute it; check the claimed modulus of continuity along
   variety arcs (which norm? does the arc stay in the variety matter, or does
   the argument hold for ambient perturbations too — if ambient, say so, it
   strengthens the lemma).
2. THE RECODING STEP (mu -> 0): the proof recodes to the boundary stratum.
   Attack: is the recoding well-defined when SEVERAL masses degenerate at
   different rates? Does the two-scale split (above/below the active-entry
   scale) cover ALL degeneration patterns (e.g. a transient mixture weight
   alpha_is -> 0 simultaneously with a block mass)? Construct the nastiest
   degeneration you can and test the lemma on it numerically.
3. QUANTIFIERS: is the radius claim genuinely UNIFORM in the sense the
   curve-selection application needs (a radius depending only on stated,
   computable quantities)? List every constant's dependence (mu, k, t, n).
4. INDEPENDENT NUMERICS (python3/numpy/scipy): re-implement the visibility
   check; sweep the audit's stress family (active-entry scale 1e-6) plus your
   own degenerations; verify the claimed radius formula numerically (find the
   actual visibility-breaking radius vs the claimed lower bound — claimed must
   be <= actual everywhere).
5. THE W-JUMP QUESTION: does T1 as proved actually disarm the recorded
   compactness dead route (the visible set jumping in limits)? State precisely
   what compactness argument T1 now licenses and what it still does not.

## DELIVERABLE (verdict-first; long form to audit_report.md)
VERDICT: T1 HOLDS (constants confirmed/corrected, dependence list) / HOLDS
WITH REPAIR (the repaired statement) / BROKEN (the degeneration that kills it,
with numbers). Then the W-jump assessment, your numerics, and calibrated
P(verdict survives further audit). Do not soften.
