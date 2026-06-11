# w19_tangent: PROVE the tangent-cone form of the linear law (wave-18 plan 1)

You are a codex (gpt-5.5) PROVER with numerics. The wave-18 research round
identified the campaign's cleanest-ever target: the linear law as a first-order
normal-cone inequality on the idempotent variety. Prove it (or find the
analytic-arc counterexample direction).
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w19_tangent.
PROGRESS PROTOCOL: append one short line per stage to
/tmp/codex-sigma-wall/w19_tangent/progress.md.

## READ FIRST
1. agent-A/explorations/classical-portfolio/notes/swarm-answers/w18_variety.md
   — the full program: the variety I^1_{n,k}, tangent space PA + AP = A (pure
   corners, D1 = 0), the exact chart P(C,D), the H-M stratification, the
   first-order normal cost delta(P_0 + tA) = t * max_i sum_{j: P0_ij = 0}
   (-A_ij)_+ + O(t^2), and the n=3,k=2 model P = I - u v^T.
2. report/kernel-conjecture.tex (same exploration dir) — definitions (H, W,
   hidden, multiplicity-correct vertices; delta = row negative mass) + §5.
3. notes/swarm-answers/w18_similarity.md — why naive Newton failed (first-order
   diagonal displacement): your lemma is the correct infinitesimal form.
4. notes/swarm-answers/w17_antecedent.md + w16_cert_audit.md — the certified
   near-tangent instances (your inequality must be CONSISTENT with them: high
   sigma_tilde at H/tau ~ 0.016 means directions with large invisible mass and
   tiny dH exist — they do NOT violate dH <= C*ddelta; check).

## TARGET (state it precisely first — this is part of the work)
At every H-M normal-form point P_0 (every partition stratum, including
transient rows) and every tangent direction A (P_0 A + A P_0 = A, A1 = 0):
  dH(A) <= C * ddelta(A),
where ddelta(A) = max_i sum_{j: P0_ij = 0} (-A_ij)_+ (the first-order negative
mass) and dH(A) is the first-order growth of the height functional H along
P_0 + tA. SUBTLETIES you must handle honestly:
(a) H is a max-min over the visible hull — define its directional derivative
    (Danskin-type; the visible set W can change along the arc: handle the
    semicontinuity, or prove the inequality for the lim sup derivative);
(b) at delta = 0, H = 0 and the visible set is the recurrent rows — the
    inequality says: any tangent direction lifting a row out of the visible
    hull must create first-order negative mass at the active zeros. The
    H-M zero pattern (transient columns vanish; off-diagonal recurrent blocks
    vanish) is exactly the active-set structure — USE IT;
(c) C must be uniform over the stratum (dimension-free if possible; if C
    depends on the partition data or the minimal recurrent-block mass, SAY SO
    — that is the honest analogue of the spectral-floor caveats).

## METHOD
1. START AT n = 3, k = 2 (P = I - u v^T, v^T u = 1, v^T 1 = 0): compute
   everything explicitly; prove the inequality there with an explicit C.
2. RANK 1 + general k block structure: the recurrent-block tangent directions
   vs the transient mixing directions — decompose the tangent space along the
   H-M zero pattern; per-block the problem should reduce to a rank-one
   perturbation computation.
3. NUMERICAL TANGENT-CONE DECIDER (python3/numpy/scipy): sample H-M points
   P_0 (random partitions, random pi_s, random transient mixtures) and solve
   the LP/QP: maximize dH(A) subject to ddelta(A) <= 1, A in T_{P_0},
   ||A|| <= 1. If the max blows up on some stratum: that direction is the
   counterexample seed — report it precisely (it would be the leading term of
   the curve-selection arc). If bounded: the measured C per stratum is your
   conjectured constant. RUN THIS FIRST — it tells you which side to prove.
4. If the first-order statement holds: state what second-order/curve-selection
   step remains to conclude the local linear law H <= C*delta near the stratum
   (do not claim the full law without it — the variety has corners where
   strata meet; flag the stratum-boundary issue).

## DELIVERABLE (verdict-first)
VERDICT: LEMMA PROVED (statement + proof in display math; explicit C and its
stratum-dependence; the n=3 case fully explicit) / COUNTEREXAMPLE DIRECTION
(the tangent A, the stratum, the numbers — and what arc it seeds) / PARTIAL.
Then the decider results (measured C distribution over sampled strata), the
remaining gap to the local linear law, and calibrated P(local linear law
provable this route), P(global = all-strata-uniform version true).
Save all code + outputs.
