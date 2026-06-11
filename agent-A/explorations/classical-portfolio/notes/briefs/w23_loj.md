# w23_loj: the stratified distance-to-locus bound (the repaired last estimate)

You are a codex (gpt-5.5) PROVER with numerics. The fixed-stratum jet bound was
refuted by support-addition arcs (harmless for the law: H = 0 along them). The
repaired — and now correctly posed — last estimate before the local linear law:
the stratified error bound against the WHOLE local delta = 0 locus.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w23_loj.
PROGRESS PROTOCOL: short line per stage to progress.md.
ARTIFACT RULE: long-form proof to proof.md, NEVER answer.md.

## READ FIRST
1. agent-A/explorations/classical-portfolio/notes/swarm-answers/w22_jet.md —
   the refutation of the fixed-stratum version (support-addition arcs: delta=0
   to all orders, jets transverse to ONE stratum but inside the LOCUS) and the
   repair menu (option 3 = your target).
2. notes/swarm-answers/w18_variety.md — the exact chart P(C,D); the H-M locus
   as a finite union of strata by support pattern (partition data + zero
   patterns), each a smooth semialgebraic set through the base.
3. notes/swarm-answers/w21_second.md — the fixed-base dangerous-cone race is
   empirically EMPTY (clean-window ratio 0) — consistent with your target:
   transverse directions pay delta at order <= 2.
4. The banked chain (import freely): w19_tangent(+_audit) — dot-H+ <= 2
   dot-delta, C = 2; w20_t1_audit — ambient fixed-mass visibility;
   w21_recode(+_audit) — L1 exact boundary recode + L2 final-profile one-shot.
5. notes/swarm-answers/w18_quadlit.md lead #1 (Luo-Pang error bounds) — at
   fixed n, SOME Lojasiewicz exponent for dist(., M_HM) vs delta exists by
   semialgebraicity (you may use this as a flagged UNVERIFIED-LEAD for
   existence; the CONTENT you must derive is the exponent 2 and the constant
   structure).

## TARGET
J1' (the stratified bound): at any H-M base point P_0, with M_HM = the local
delta = 0 locus of the row-stochastic idempotent variety near P_0 (= the
finite union of H-M strata through P_0, including all support-addition
strata), prove: there exist a neighborhood and L (dependence: fixed n honest;
track what is dimension-free) with
  dist_chart((C,D), M_HM)^2 <= L * delta(P(C,D))
for variety points P(C,D) in the neighborhood. EQUIVALENT CORE CLAIM (prove
this form): no variety direction (or 2-jet) TRANSVERSE to M_HM has delta flat
to third order — i.e. transverse to the full locus, delta vanishes to order at
most 2. STRATEGY:
- Characterize T(M_HM) at P_0: the union (not sum!) of the strata tangent
  cones — tangent directions = (stratum moves) + (support additions at
  currently-zero entries that preserve the H-M block structure: entries that
  can become positive while staying exactly stochastic-idempotent — derive
  WHICH zero entries those are from the H-M normal form: within-block
  patterns, transient mixings; vs RIGID zeros: off-diagonal recurrent-block
  entries and transient columns, whose activation forces delta > 0 or leaves
  the locus).
- For a direction A transverse to the union: decompose against the active-zero
  structure; first-order cost dot-delta(A) > 0 unless A only activates
  "harmless-looking" zeros — for those, compute delta to SECOND order in the
  exact chart (the quadratic diagonal corrections -CD, DC) and prove the
  second-order delta-form is positive-definite transverse to the locus (this
  is the second-order rigidity claim; w21_second's empirical ratio-0 supports
  it). Handle 2-jets whose first order is IN the union but whose second-order
  correction is transverse (the curve-selection subtlety) — a finite-jet
  argument or explicit chart computation.
- VALID RANGE: state the neighborhood honestly (it may shrink with the
  smallest positive entry of the base profile — that is acceptable AFTER the
  L2 final-profile recode; say how the two compose).
J2' (assembly; attempt if J1' lands): H <= C_loc * delta near the H-M locus:
recode to the final profile (L2), pick the NEAREST locus point (J1' gives
dist <= sqrt(L*delta)), connect with a short arc, apply the tangent-cone
lemma + the visibility lemma; the quadratic height error is now controlled by
dist^2 <= L*delta. Aim for C_loc = 2 + O(sqrt(delta)) per the numerics; state
what you actually get. Do NOT claim the global small-delta law (the B-S
normal-form distance gap stands).

## NUMERICS (first)
In the chart at sampled bases (boundary strata included): sample variety
points, compute dist((C,D), M_HM) by minimizing over ALL local strata (
including support additions — enumerate the locally-reachable support
patterns), measure dist^2/delta — its sup is your empirical L; find the
saturating directions. Re-test the w22 support-addition arcs (they must now
give dist = 0). Then test the assembled H <= C_loc*delta on the w21/w20
stress families.

## DELIVERABLE (verdict-first; long form to proof.md)
VERDICT: J1' PROVED (+ J2' ASSEMBLED: the LOCAL LINEAR LAW, explicit
constants/neighborhood/dependence) / J1' ONLY / DIED-AT (the exact failed
estimate; a third-order-flat transverse 2-jet would be a major discovery —
report loudly with the explicit jet). Calibrated P(J1' true), P(assembly
survives audit). Save code + outputs.
