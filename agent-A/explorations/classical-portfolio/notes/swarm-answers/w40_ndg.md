# w40_ndg — RANK-2 THEOREM (both horns, C = 2, unconditional) + repair confirmed + V=0-at-argmin refuted literally (codex, 2026-06-13)
# Brief: notes/briefs/w40_ndg.md. Long form: experiments/out/w40_ndg/proof.md.

VERDICTS: A = REPAIR CONFIRMED ((P1) proved by sign split + exact-checked independently;
(DEF)-coupling confirmed; literal V=0 at argmin REFUTED — perturbed staircase argmin has
V/delta = 1/500000, tiny but nonzero). B = **RANK-2 THEOREM** (P = 0.94):
  rank(P) = 2 => EVERY theta-half Phi-argmin has Phi(U*) = 0, V_s = 0, S*_s <= 2 delta.
  THE FIRST UNCONDITIONAL INSTANCE of the selected-chart bound.
- THE PROOF PATTERN (the template): (1) EXISTENCE: the max-diameter basis has all
  coefficients in [0,1] => Phi = 0 achievable => every argmin has Phi = 0; (2) Phi = 0 on
  positive-beta rows => lambda >= 0 => V = 0; (3) (DEF) + neg-beta mass <= delta +
  lambda_+ <= 2 (box) => S* <= 2 delta. Holds for EVERY argmin, no tie-break needed.
- ORCHESTRATOR ANALYSIS (UNVERIFIED — w41 must check): the proof FACTORIZES. Steps (2)-(3)
  generalize to any rank: from Phi(U) <= C0 delta one gets (sketch: sigma <= E + 2 lambda_+;
  (-lambda)_+ <= E/2; Sum beta_+ lambda_+ <= Sum (-beta)_+ lambda + Phi/2 <= 3 delta + Phi/2
  via (DEF) + box) S*_s <= ~3 Phi + 6 delta. SO THE WHOLE CAMPAIGN REDUCES TO (EX):
  *exists* an actual-row theta-1/2 chart with Phi <= C0 delta — the pure existence
  statement, with ALL the S*/V/deficit bookkeeping now banked. Rank 2: (EX) free
  (max-diameter). Rank >= 3: (EX) is THE open; the two-horn swap dichotomy is its live
  mechanism; every numerical instance ever tested satisfies it with C0 ~ 1.
- Wave-41 target: verify the factorization (S* <= aPhi + b delta, exact constants), then
  (EX) at rank 3 — analog of max-diameter (chart construction), or the decisive numeric:
  adversarially MINIMIZE min-chart Phi/delta over rank-3 idempotents (if some instance has
  min-Phi >> delta, (EX) is false and the conjecture falls).
