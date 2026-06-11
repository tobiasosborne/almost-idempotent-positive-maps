# w27_concentration: L3 — the support-concentration estimate (the last lemma of the 1.12 bridge)

You are a codex (gpt-5.5) PROVER with numerics, on the single remaining lemma
of the campaign's best route to the GLOBAL statement (every small-delta exact
stochastic idempotent is near the H-M family).
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w27_concentration.
PROGRESS PROTOCOL: short line per stage to progress.md.
ARTIFACT RULE: long-form proof to proof.md, NEVER answer.md.

## THE CHAIN SO FAR (read in order; all under agent-A/explorations/classical-portfolio/)
1. notes/swarm-answers/w25_hm112.md — the 1.12 bridge: L1 (Thm 1.12 stochastic
   coordinates — exact: classes of proportional rows C_s, B-rows as
   combinations, sum rules (1.2) in-class = 1 / (1.3) cross-class = 0; source
   refs/hognas-mukherjea-2011/hognas-mukherjea-2011.txt ~:2245-2330), L3's
   original statement, L4 (constructive projection).
2. notes/swarm-answers/w26_cluster.md — L2: the eta-clustered chart,
   eta = sqrt(delta), proportionality error F = eta.
3. notes/swarm-answers/w26_cluster_audit.md — L2 UPGRADED: with a MAXIMUM-
   VOLUME actual-row basis the coefficient bound is A = 1, Lambda <= 1,
   E <= R*eta, DIMENSION-FREE (the audit's audit_report has the construction —
   read experiments/out/w26_cluster_audit/audit_report.md fully and import its
   exact statements/notation).
4. Background tools (audited, import freely): w19_tangent (dot-H+ <= 2
   dot-delta at H-M points), w20_t1_audit (ambient fixed-mass visibility),
   w21_recode(+audit) (mass-removed recoding, final-profile form),
   w14_autopsy/w15_audit (the sign-robust row-reproduction modulus
   dist(p_i, conv{p_j : P_ij > 0}) <= (2+4delta)*nu_i).

## TARGET — L3 (then assemble L4 if it lands)
Setting: P exactly idempotent, P1 = 1, row negative mass <= delta <= delta_0;
the L2 chart with the max-volume row basis: merged classes (eta-pivot
clusters) U_1..U_m with representative rows r_1..r_m (actual rows, max-volume
choice), every row p_i = sum_t a_t(i) r_t with |a_t(i)| <= 1 and
sum_t a_t(i) = 1; the exact 1.12 sum rules in merged form (from w26 +
audit_report).
PROVE (dimension-free moduli; explicit constants):
 (a) IN-CLASS CONCENTRATION: each merged class's rows are within G1(delta) of
     a COMMON probability row (the "equal-input" candidate) — i.e. the
     proportionality factors are 1 + O(delta) and the common row is
     near-nonnegative. Tools: rows in a class are eta-proportional (L2) AND
     each row has negative mass <= delta AND row sums 1 — derive the forcing.
 (b) SUPPORT CONCENTRATION (the heart): the representative rows' mass
     concentrates on "their own" support up to G2(delta): cross-class positive
     mass + the B-rows' deviation from CONVEX mixtures are O(delta)-small.
     Tools: the EXACT sum rules (1.2)/(1.3) — at delta = 0 they are the
     sign-rigid zero-sum closures; with |a| <= 1 (L2!) and entries >= -delta,
     check whether cancellation can still hide large terms: the sum rules are
     now over BOUNDED coefficients, so each negative contribution is bounded
     by delta * (number of terms?) — the danger is n-dependence via the number
     of terms; use the row-reproduction modulus and the masses' normalization
     to telescope instead of counting terms. If an n-dependent count is
     genuinely forced somewhere, SAY SO precisely — that residual IS the
     answer then.
 (c) L4 ASSEMBLY (if (a)+(b) land): construct the H-M point (normalize class
     representatives to the common probability rows; clip B-coefficients to
     the simplex; zero the cross-class mass) and bound ||P - P_HM|| row-wise
     by G(delta) — state which norm and the explicit G. This would be the
     GLOBAL W-free statement at whatever delta_0/G you honestly get — the
     campaign landmark. Do NOT overclaim: every constant explicit; if G is
     O(sqrt(delta)) rather than O(delta), that is still the audited W-free
     target (B-S distance <= C*sqrt) — say which you get. Cross-check the
     ex-hume refutation (full-distance O(delta) is FALSE — your G must respect
     it; locate where your bound degrades to sqrt or how hidden height enters).
VERIFY numerically on: the split-block family, the w19 leftcone family, the
certified w16/w17 instances (above-corner — report, no small-delta claim),
and random small-delta samples ON the variety (use the corner chart or
P = LB constructions).

## DELIVERABLE (verdict-first; long form to proof.md)
VERDICT: L3+L4 PROVED (the global statement, explicit G + norm + delta_0;
ex-hume-consistent) / L3 ONLY / DIED-AT (the exact failed estimate — esp. if
an n-dependent term-count is forced: exhibit the family that saturates it).
Calibrated P(survives audit), P(the global statement as obtained feeds
op-exposed-hull/op-classical). Save code + outputs.
