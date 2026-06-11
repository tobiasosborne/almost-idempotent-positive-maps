# w22_jet: the last estimate — the finite-jet normal projection bound

You are a codex (gpt-5.5) PROVER with numerics. The campaign's audited lemma
chain for the LOCAL linear law is complete except for ONE estimate. Prove it
(or exhibit the degeneration that defeats it). If you prove it, ASSEMBLE the
local law from the banked chain — that is the campaign landmark.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w22_jet.
PROGRESS PROTOCOL: short line per stage to progress.md.
ARTIFACT RULE: long-form proof to proof.md, NEVER answer.md.

## THE BANKED CHAIN (read these; all audited — import freely, cite by name)
1. notes/swarm-answers/w19_tangent.md (+ _audit): TANGENT-CONE LEMMA —
   dot-H+ <= 2 dot-delta at every H-M point and variety tangent, C = 2
   dimension-free (sharp for the frozen recurrent-hull derivative).
   (Under agent-A/explorations/classical-portfolio/.)
2. notes/swarm-answers/w20_t1_audit.md: AMBIENT FIXED-MASS VISIBILITY —
   recurrent vertices with LP support margin eta stay visible for
   eps <= min{mu/8, tau/64, eta*tau/64, 1/64} (max-row-l1, ambient).
3. notes/swarm-answers/w21_recode.md + w21_recode_audit.md: L1 RECODING —
   exact boundary H-M recode with ||P0 - P0'|| <= 2(sum_s q_s + max_i r_i),
   bounds in ORIGINAL removed mass; L2 (REPAIRED form ONLY): one-shot recode
   to the FINAL boundary profile + fixed-mass lemma once — never iterate
   stepwise (that overcharges O(n)).
4. notes/swarm-answers/w21_second.md: the fixed-base second-order race is
   EMPTY (max_local_ratio = 0 in the clean window) — i.e. at a fixed base,
   dangerous-cone arcs (dot-delta = 0, frozen D = 0) appear to have q_H = 0
   as well; the sharp H/delta = 2 cases are boundary-crossing events that
   the recoding now handles.
5. notes/swarm-answers/w18_variety.md: the exact chart P(C,D) — diagonal
   deviations P_EE - I = -CD + O(3), P_FF = DC + O(3); strata dimensions.
6. notes/swarm-answers/w20_curve.md: the original T2 failure statement —
   H <= 2*delta + O(||(C,D)||^2) needs ||(C,D)_{perp M}||^2 <= L * delta,
   perp-M = normal to the H-M stratum within the variety. Also the w20_t1
   audit's flagged arc-scale issue: a lower estimate for tau(t) = sqrt(delta(t))
   along the arc (from the first nonzero term of delta) — handle or subsume it.

## TARGET
J1 (the jet bound): at any H-M base P_0 (allow boundary strata — by the L2
final-profile convention you may assume the base is already the final recoded
profile), in the exact chart, prove: there exist L (state its dependence —
on the stratum data mu, eta, block count; fixed n acceptable; track
dimension-freeness) and a neighborhood such that every variety point P(C,D)
in it satisfies
  ||(C,D)_{perp M}||^2 <= L * delta(P(C,D)),
where perp-M is the normal complement of the H-M stratum's tangent inside the
variety tangent space at P_0. STRATEGY HINTS:
- Decompose (C,D) = (stratum-tangent) + (linear-cost normal) + (dangerous
  normal). On linear-cost directions, delta >= c * ||component|| - O(||..||^2)
  by the first-order normal cost (derive c from the active-zero structure —
  is it the minimal surviving block mass? state it). Squaring gives the bound
  there.
- On the DANGEROUS normal cone (dot-delta = 0): w21_second's empirical fact
  (fixed-base ratio 0) suggests these directions, at second order, either
  (i) stay in the nonneg cone (then they are tangent to a LARGER nonneg
  family — but the H-M locus is exactly the delta = 0 locus on the variety:
  prove that a direction with delta vanishing to second order along the arc
  is stratum-tangent to second order — i.e. the delta = 0 locus is "second-
  order rigid": its tangent cone equals the stratum tangent), or (ii) pay
  delta at second order with a computable positive quadratic form q_delta —
  then L on that cone is 1/lambda_min(q_delta) (state lambda_min's
  dependence). The dichotomy (i)/(ii) IS the content — prove it via the
  exact chart algebra: compute delta(P(tC, tD)) to second order explicitly
  at active zeros (the first-order term vanishes on the dangerous cone by
  definition; the second-order term comes from the chart's quadratic
  diagonal corrections -CD, DC — compute its sign/positivity structure).
J2 (the assembly): if J1 holds, assemble the LOCAL LINEAR LAW: every exact
row-stochastic idempotent P in a (stated) neighborhood of the H-M locus
satisfies H(P) <= C_loc * delta(P), with C_loc explicit (the numerics say
C_loc = 2 sharp — aim for 2 + o(1) but state what you get honestly). Use:
final-profile recode (L2) -> fixed-mass visibility -> tangent-cone lemma along
a connecting arc + J1 to kill the quadratic error. EVERY step explicit; the
W-jump dead route must be explicitly disarmed by the visibility lemma at the
recoded base. State the neighborhood's dependence honestly (this is the
LOCAL law; the global small-delta law additionally needs the B-S normal-form
distance question — do NOT claim it).
J3 (honest list): every n-, mu-, eta-, profile-dependence in J1+J2; what
would be needed for dimension-freeness.

## NUMERICS (first)
In the exact chart at sampled bases (include boundary strata + tiny-mass
profiles): sample variety points near P_0, compute ||(C,D)_{perp M}||^2 /
delta — measure L empirically and find where it is largest (which directions/
strata). Then test J2's assembled inequality H <= C_loc * delta on the same
samples + the w21_second boundary events + the w20 stress family.

## DELIVERABLE (verdict-first; long form to proof.md)
VERDICT: J1+J2 PROVED (the LOCAL LINEAR LAW, explicit constants + neighborhood
+ dependence list) / J1 ONLY / DIED-AT (the exact failed estimate; if the
dangerous-cone dichotomy fails, the explicit direction — a second-order-flat
delta direction NOT stratum-tangent would be a major discovery: report it
loudly). Calibrated P(J1 true), P(J2 survives audit). Save code + outputs.
