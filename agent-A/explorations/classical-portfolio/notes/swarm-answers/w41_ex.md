# w41_ex — FACTORIZATION VERIFIED (S* <= 2 Phi + 6 delta); (EX) at rank 3 HOLDS EMPIRICALLY with C0 = 1 exactly (codex, 2026-06-13)
# Brief: notes/briefs/w41_ex.md. Long form: experiments/out/w41_ex/proof.md.

VERDICT: FACTORIZATION VERIFIED with (a,b) = (2,6): for ANY theta-1/2 chart U and any s,
S*_s(U) <= 2 Phi_s(U) + 6 delta(P). Zero violations across 7573 valid charts / 2947
theta-half charts / 278 exact rank-3 records (220 random + 53 structured adversarial,
delta <= 1/4). (EX) at rank 3: HOLDS EMPIRICALLY, NOT PROVED — worst observed
min_U max_s Phi_s(U)/delta = EXACTLY 1 (transverse / no-center rank-3 families attain it).

CONSEQUENCE — THE CAMPAIGN'S OPEN PROBLEM IS NOW FORMALLY (EX):
  every row-stochastic idempotent P with delta(P) <= 1/4 has an actual-row basis U with
  Vol(U) >= (1/2) Vol_max such that max_s Phi_s(U) <= C0 * delta(P).
(EX) + factorization + argmin selection => the registry contract with C_sf = 2*C0 + 6
(empirical C0 = 1 => C_sf = 8) => (via w35_quantifier's chain, theta = 1/2, A = 2) the
global W-free O(sqrt(delta)) theorem => op-exposed-hull => op-classical.
STATUS LADDER: rank 2 PROVED (w40, C = 2); rank 3 empirical (this wave, C0 = 1, 278 exact
instances, adversarial windmill/staircase/near-degenerate searches all bounded); rank >= 3
proof OPEN — the two-horn swap dichotomy ((NDG) + volume-permitted) is the live mechanism.
PENDING 2-FAMILY: the factorization lemma is codex-only so far — opus cross-audit launched
(w42_factor_audit) before banking.
