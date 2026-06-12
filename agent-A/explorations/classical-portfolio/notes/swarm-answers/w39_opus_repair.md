# w39_opus_repair — REPAIRED ONLY: (P1) exact pointwise fix; open = (SB*); overshoot NOT free; the near-degenerate horn (NDG) is the missing display (opus, 2026-06-13)
# Worker: Claude Opus (repair of w37_opus after the w38_sb refutation). Long form: experiments/out/w39_opus_repair/proof.md.

VERDICT: REPAIRED ONLY (open = (SB*)); overshoot bounded-by-selection, not for free.
- (P1) THE REPAIR (banked, sympy-exact at every (s,j) across all six families, whole
  theta = 1/2 class): E_s(j) <= sigma_s(j) + 2(-lambda_s(j))_+, hence SF_s <= S*_s :=
  S+_s + 2V_s. The refuted row is now correctly dominated (S+/d = 5001/1e6 < SF/d =
  5003/1e6 < S*/d = 5005/1e6).
- (SB*) THE CORRECTED OPEN DISPLAY: U* in argmin_{theta=1/2} Phi => S*_s <= 3 delta.
  ENVELOPE UNCHANGED: V_s = 0 at EVERY tested argmin chart (the repair costs zero
  envelope); S*/delta = 2 on the five core families, 5/2 -> 8/3 -> 3 on no-center.
- OVERSHOOT NOT SEPARATELY BOUNDABLE (task-2 answer NO): (DEF) couples D+_s - V_s =
  Dneg_s with |Dneg_s| <= 3 delta — one equation, two unknowns; at theta = 1/2 the
  positive deficit is O(1) from the box, not O(delta). Cleanly V_s <= M_s (transverse
  tax) but M_s/delta grows ~m off-argmin. So V is bounded by the SAME selection.
- (NDG) THE MISSING DISPLAY: in the multi-row swap dichotomy (volume-permitted swap =>
  minimality bites; else transverse block near-degenerate), the near-degenerate horn —
  "small transverse determinant => the carried excess is O(delta)" — is exactly what is
  not closed (worked at rank 2-3). Single-swap insufficiency re-confirmed.
- Wave-40 target: codex cross-verifies (P1)/(SB*) + attacks (NDG).
