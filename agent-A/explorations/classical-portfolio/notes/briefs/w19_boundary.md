# w19_boundary: the boundary-product dichotomy on the quotient (wave-18 semigroup plan 2)

You are a codex (gpt-5.5) PROVER with numerics, attacking the campaign's
recorded frontier (anti-splitting) with wave-18's new exact identities.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w19_boundary.
PROGRESS PROTOCOL: append one short line per stage to
/tmp/codex-sigma-wall/w19_boundary/progress.md.

## READ FIRST
1. agent-A/explorations/classical-portfolio/notes/swarm-answers/w18_semigroup.md
   — Plan 2: the exact all-lengths boundary identity. For ANY band split
   P = [[B, E], [C', D']] (B = the shallow band block S_t), exact idempotence
   gives  B^m - B = - sum_{r=0}^{m-2} B^r E C'  for every m. Also Plan 3 (the
   trace tax tr B - tr B^2 = tr(E C')) as a supporting tool.
2. notes/swarm-answers/w16_barrier.md + w16_quotient.md — the anti-splitting
   died-at this must break: high hidden height forces aggregate shallow
   off-C_W mass >= (B/3-4)*tau, but no tool pins c*tau into ONE closed
   quotient component. The quotient machinery (Q stochastic idempotent,
   lumping lemma) is SECURED — build on it.
3. notes/swarm-answers/w15_periodic.md + w15_periodic_audit.md — closed
   components are automatically aperiodic (delta < 1/4); the leakage-tolerant
   versions of the constants.
4. report/kernel-conjecture.tex — definitions + conj:quotient-floor + §5.

## TARGET (the dichotomy)
On the quotient (classes of coincident rows; Q the quotient matrix — itself
exactly idempotent and stochastic-up-to-delta), for the shallow band S_t and
its quotient band block B: prove a quantitative dichotomy of the form —
EITHER some closed quotient component C in S_t has theta_C/path-product large
enough to attach the (audited, periodicity-free) w12 finisher (collapse radius
< r* = 0.85*tau), OR the boundary product sum_{r} B^r E C' has total mass
>= c''*tau, which must be CHARGED somewhere: derive where it lands (deep
rows? visible mass? v's own budget?) and what that forces (if it lands on
v's delta-budget: a bound H <= C*delta follows? derive the constants).
The identity holds for EVERY m simultaneously — optimize over m (the
m -> infinity limit of B^m exists trivially? careful: ||B|| <= 1 + 2*delta,
B^m does NOT converge a priori; but B^m - B is EXACTLY the boundary sum —
use m where (signed) B^m is controllable, e.g. m = 2: B^2 - B = -EC' is
already exact and the trace/row-sum versions of it are the sharpest small
identities available).
GUARDRAILS: every quantity must be clone-invariant (work on the quotient);
no chain-local scalar reasoning (w15_sos: the scalar shadow is false — your
dichotomy must consume the row-realization/band structure); respect the
certified instances (delta ~ 0.23, sigma/tau ~ 1.6, H/tau ~ 0.016-0.10:
plug your dichotomy into them numerically — which horn do they satisfy?).

## METHOD
1. Derive the exact m = 2 identities row-wise and trace-wise on the quotient;
   then the all-m family; bound the signed errors with the audited moduli.
2. The charging argument: where can sum B^r E C' mass live? Decompose E
   (band -> deep) and C' (deep -> band) against the deficit g (g = Pg exact:
   deep rows have g >= t — the conservation structure t6 died on, but t6
   lacked the boundary identity; combine them).
3. NUMERICS: implement the dichotomy quantities on (i) the certified w17
   antecedent instance (experiments/out/w17_antecedent/targeted_best/) and
   (ii) random H-M-perturbed instances; measure both horns; report which holds
   and with what margins. If BOTH horns fail somewhere: that instance is the
   sharpest counterexample geometry yet — save it.
4. If the dichotomy proves: state precisely what remains for the linear law /
   conj:quotient-floor (the second horn's charge bound is presumably the new
   lemma; the first horn is the finisher).

## DELIVERABLE (verdict-first)
VERDICT: DICHOTOMY PROVED (display math, explicit constants, the charging
destination identified) / PARTIAL (which horn is proved, the exact gap) /
DIED-AT (the failed inequality + the instance where both horns fail). Then
the numerical horn-measurements, and calibrated P(dichotomy true),
P(it closes anti-splitting). Save code + outputs.
