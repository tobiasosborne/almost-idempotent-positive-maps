# w42_factor_audit — FACTORIZATION CONFIRMED (a=2, b=6, tight); composition clean; 2-FAMILY BAR MET (opus, 2026-06-13)
# Worker: Claude Opus (hostile auditor, != w41 author). Long form: experiments/out/w42_factor_audit/audit.md.

VERDICT: FACTORIZATION CONFIRMED, constants (2,6) TIGHT. P(correct) = 0.99 (both lemma and
composition).
- Line-by-line re-derivation reproduces every step: pointwise g <= E + 2 lambda_+
  (exhaustive sign split, equality on overshoot rows); (DEF) decomposition Dpos = V + Dneg;
  V <= Phi/2; Dneg <= 3 delta (via the lambda <= 3 box edge — the right one).
- The w38 cautionary check PASSES: the +2|lambda| overshoot term that refuted (SIG) is
  exactly what this proof carries; the old witness satisfies the factorization.
- NO hidden delta <= 1/4 dependence: only mass <= delta and lambda <= 3 used; verified on
  instances with delta up to 3. (delta_0 <= 1/4 is needed only by (EX) downstream.)
- Composition C_sf = 2*C0 + 6 clean (universal-in-s; no quantifier slip). ~700 exact
  instances + all named families + adversarial overshoot/windmill: 0 violations.
- BANKING STATUS after this wave: factorization = 2-family DONE (codex proof + opus audit).
  Rank-2 theorem (w40) = codex-only — still needs its opus pass before banking. (EX) = the
  open kernel, untouched.
