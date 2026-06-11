# w23_loj_audit: hostile audit of J1' (stratified bound) + J2' (the assembled LOCAL LINEAR LAW)

You are a codex (gpt-5.5) HOSTILE AUDITOR on the campaign's landmark candidate:
the stratified distance-to-locus bound and the assembled local linear law
H <= C_loc * delta near the H-M locus. Nothing is "proved" until you fail to
break it. Cardinal failure mode: a confident, plausible, WRONG claim.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w23_loj_audit.
PROGRESS PROTOCOL: short line per stage to progress.md.
ARTIFACT RULE: long form to audit_report.md, NEVER answer.md.

## THE CLAIM
agent-A/explorations/classical-portfolio/notes/swarm-answers/w23_loj.md (the
full proof note appended; if not yet archived read
/tmp/codex-sigma-wall/w23_loj/proof.md). Claims:
- J1': dist_chart((C,D), M_HM)^2 <= L * delta(P(C,D)) near any H-M base,
  M_HM = the local delta = 0 locus (union of strata incl. support additions).
- J2': the LOCAL LINEAR LAW H <= C_loc * delta with C_loc = 2 + K_vis * L
  (fixed n; explicit neighborhood).

## CONTEXT (the banked chain + the refutation history)
1. notes/swarm-answers/w22_jet.md — the support-addition refutation of the
   fixed-stratum version (the repaired J1' must give dist = 0 on those arcs).
2. notes/swarm-answers/w19_tangent.md + _audit, w20_t1_audit.md,
   w21_recode.md + _audit — the audited chain J2' assembles
   (tangent-cone lemma; ambient fixed-mass visibility with its eps condition;
   L1 recode; L2 final-profile one-shot ONLY — stepwise iteration is BROKEN).
3. notes/swarm-answers/w21_second.md — fixed-base ratio-0 empirics.
4. notes/swarm-answers/w18_variety.md — charts/strata.

## AUDIT TASKS (derive-first; the assembly is the likely soft spot)
1. J1' TANGENT-CONE CHARACTERIZATION: re-derive which zero entries of an H-M
   normal form are PROMOTABLE (support addition stays exactly H-M) vs RIGID
   (off-diagonal recurrent blocks; transient columns). The union-of-strata
   tangent cone must be exactly characterized — any missed promotable pattern
   makes J1' falsely strong (a missed stratum = an arc with delta = 0 counted
   as transverse). Enumerate systematically for small (n,k) and cross-check
   the proof's list; run the w22 support-addition family + YOUR OWN new
   promotion patterns (multi-entry simultaneous promotions; promotions
   interacting with transient faces) through their distance computation.
2. J1' SECOND-ORDER RIGIDITY: re-derive the transverse second-order delta-form
   positivity in the exact chart. Attack: directions mixing a promotable
   first-order part with a rigid second-order part (the 2-jet subtlety);
   does the proof handle jets whose first order lies IN the union but whose
   second-order correction is transverse? Construct the nastiest mixed 2-jet
   and test delta's vanishing order numerically (a third-order-flat
   transverse 2-jet kills J1' — search hard).
3. J1' CONSTANT/NEIGHBORHOOD: is L's claimed dependence honest (what happens
   as the base profile's smallest positive entry -> 0 — does the neighborhood
   shrink compatibly with the L2 final-profile composition or is there a
   circular dependence: the recode needs the neighborhood, the neighborhood
   needs the recoded profile)?
4. J2' ASSEMBLY (scrutinize line by line): (a) the nearest-locus-point +
   connecting-arc construction — the tangent-cone lemma is stated AT H-M base
   points along exact C^1 arcs: is it applied in the right direction (from
   the locus point toward P), and is the arc INSIDE the variety with
   controlled length? (b) the visibility lemma's eps-condition — verified at
   the right base with the right margins (eta at the recoded profile)?
   (c) the height comparison: H is compared between P and the locus point —
   the locus point has H = 0; the increment along the arc uses dot-H+ <= 2
   dot-delta PLUS the quadratic error controlled by J1' — check the
   integration step (the lemma is a derivative bound at the BASE; along the
   arc the base changes — does the proof integrate a pointwise bound it only
   has at one endpoint? THIS is the classic flaw — look hard); (d) constants:
   re-derive C_loc = 2 + K_vis*L and the claimed neighborhood.
5. INDEPENDENT NUMERICS: re-implement the distance probe (your own stratum
   enumeration); measure dist^2/delta on adversarial samples (near stratum
   corners where several promotions interact); test the assembled law
   H <= C_loc*delta on the w20/w21 stress families and the w17 certified
   instances (above-corner: OUTSIDE the neighborhood presumably — confirm the
   proof does not accidentally claim them).

## DELIVERABLE (verdict-first; long form to audit_report.md)
VERDICT separately for J1' and J2': HOLDS / HOLDS WITH REPAIR (statement) /
BROKEN (explicit jet/arc/step, with numbers). Then the independent numerics,
the constant re-derivations, the neighborhood-dependence assessment, and
calibrated P(each verdict survives further audit). Do not soften.
