# w37_opus — PARTIAL: the open reduced to ONE scalar display (SB); selection proven irreducible; a w35 step CORRECTED at theta=1/2 (opus, 2026-06-12)
# Worker: Claude Opus (second family, independent line). Long form: experiments/out/w37_opus/proof.md (+ charge_lp.py, nocenter_lp.py, nocenter_exact.py, predecessor harness reused).

VERDICT: PARTIAL — SF/(CHARGE) not proved; no selected-chart counterexample; the open is now
the single display (SB), strictly cleaner than (TREE) (no shear tree, no charge weights).
- (R) SIGN-ROBUST REFORMULATION (banked): E_s(j) = (sigma_s(j) - 2 lambda_s(j))_+ with
  sigma_s = positive off-pivot coefficient mass — valid at theta = 1/2 where a_s can exceed 1.
- CORRECTION TO w35: the step SF_s <= M_s (w35_charge sec 2 / w31 form) is FALSE at
  theta = 1/2 (exact witness: perturbed staircase m=5 — when a_s > 1, E_s = mu_s + |lambda_s|
  > mu_s). The theta = 1/2 campaign must use (R)/(SIG). AUDIT FLAG: re-derive the
  w35_quantifier constants chain (C_mu = C_sf + 1 + A) against (R) in wave 38.
- (DEF) harmonic deficit identity: sum_j beta_s lambda_s = 0 exactly (all families).
- THE REDUCTION (banked): (SIG) E <= sigma gives SF_s <= S+_s := sum_j (beta_s)_+ sigma_s;
  S+_s <= 3 delta would give Phi(U*) <= 3 delta. Exact checks: S+ = 2 delta on every known
  family in the SELECTED chart; the genuine no-center C~2 family climbs 2.5 -> 2.95 delta.
- (SB) THE SINGLE OPEN DISPLAY: U* in argmin_{M_{1/2}} Phi => sum_j (beta_s(j))_+ sigma_s(j)
  <= 3 delta(P) for all s. Available handles: nu_i <= delta, (DEF), Cramer box |a_t| <= 2,
  and argmin minimality — which is PROVEN NOT OPTIONAL:
- IRREDUCIBILITY OF SELECTION (banked, exact witnesses): (SB) is FALSE over the full
  theta = 1/2 class (perturbed staircase identity chart: S+ -> m delta); pointwise (ME),
  sigma-only-without-selection, and single-swap-monotonicity are EACH refuted (best swap
  from U* gives Phi/delta = 1, no contraction).
- LP-dual probing reproduces S+ = 2 delta but returns only the tautological one-row charge
  (w36 B5's tautology) — the combinatorial selection constraints were not encoded.
- Calibration: P(verdict survives audit) = 0.88; P(selected-chart bound true at
  delta_0 = 1/4, C <= 3) = 0.66; P(SB provable) = 0.30.
