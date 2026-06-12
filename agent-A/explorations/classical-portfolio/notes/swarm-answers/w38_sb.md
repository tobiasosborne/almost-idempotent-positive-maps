# w38_sb — REDUCTION REFUTED-AT-A3: (SIG) is FALSE at theta=1/2; (SB) must carry the overshoot term (codex, 2026-06-13)
# Brief: notes/briefs/w38_sb.md. Long form: experiments/out/w38_sb/proof.md.

VERDICT: REDUCTION REFUTED-AT-A3 (Part B not attempted — target was unsound as stated).
- (R) CONFIRMED correct. But (SIG) "E_s <= sigma_s" is FALSE at theta = 1/2: on overshoot
  rows (a_s > 1, lambda_s < 0), E_s = sigma_s + 2|lambda_s| > sigma_s.
- EXACT WITNESS (perturbed staircase m=5, eps=1/1000, SELECTED chart): lambda = -1/999,
  SF_s = 5003/2000000 > S+_s = 5001/2000000 (gap 1/1000000). Small but structural —
  proving (SB) as stated would NOT imply the registry contract.
- CORRECTED TARGET (SB'): sum_j (beta_s)_+ [ sigma_s(j) + 2(-lambda_s(j))_+ ] <= C delta
  at the argmin chart — i.e. (SB) plus the negative-deficit (overshoot) term.
- ORCHESTRATOR NOTE: the overshoot term may be separately boundable — (DEF) gives
  sum beta_+ lambda = sum (-beta)_+ lambda, so sum beta_+ (-lambda)_+ = sum beta_+ lambda_+
  - sum (-beta)_+ lambda; with |lambda| <= 3 (theta=1/2 box) the second piece is <= 3 delta;
  the first is the positive deficit, which at theta=1/2 is NOT yet banked. Repair task sent
  back to the original (opus) author; the multi-row swap dichotomy (w38 brief B1-B2) is
  untouched and remains the live mechanism for whichever corrected display stands.
- The w37_opus harvest header carries a dated correction pointer to this refutation.
