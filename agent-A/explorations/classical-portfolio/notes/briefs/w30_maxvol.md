# w30_maxvol: the displacement lemma via the max-volume structure

You are a codex (gpt-5.5) PROVER on the single named open statement of the
classical campaign: the representative displacement lemma. A sibling worker
(w30_telescope) attacks via iterated identities; you attack via WHAT
MAX-VOLUME FORBIDS. Different routes — go deep on yours.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w30_maxvol.
PROGRESS PROTOCOL: short line per stage to progress.md.
ARTIFACT RULE: long-form proof to proof.md, NEVER answer.md.

## THE TARGET
P exactly idempotent, P1 = 1, row negative mass <= delta <= delta_0;
u_1..u_m = the MAX-VOLUME actual-row basis (the audited L2 chart:
notes/swarm-answers/w26_cluster_audit.md + experiments/out/w26_cluster_audit/
audit_report.md — read the construction and the proof that it gives
coefficient bound A = 1: every row p_i = sum_t a_t(i) p_{u_t} with
|a_t(i)| <= 1, sum_t a_t(i) = 1; that is Cramer's rule + maximality). Prove
for each s:
  T(u_s) := sum_j (P_{u_s j})_+ * ||p_j - p_{u_s}||_1 <= C_D * delta.

## CONTEXT (read first)
1. notes/swarm-answers/w29_displacement.md + experiments/out/w29_displacement/
   proof.md — the FREE vector identity (signed displacement sum = 0; positive
   vector sum <= 2*delta*(1+2delta)); the GENERAL-ROW delta = 0 counterexample
   (READ IT CLOSELY: it shows a non-representative row with positive mass at
   large displacement in cancelling directions — understand exactly why such
   a row CANNOT be max-volume; that understanding IS the proof's seed);
   the numerics (T/delta <= 3.6).
2. notes/swarm-answers/w27_concentration.md — in-class concentration
   (G1 = eta + 2*delta) and the rank-2 saturating family (T = delta exactly —
   your C_D must accommodate it).
3. refs/hognas-mukherjea-2011/hognas-mukherjea-2011.txt ~:2245-2330 —
   Thm 1.12's sum rules (1.2)/(1.3) in case the coordinates help.

## THE ROUTE
1. Write the displacement in the A = 1 coordinates: p_j - p_{u_s} =
   sum_t (a_t(j) - delta_{ts}) p_{u_t}; so f(j) = ||p_j - p_{u_s}||_1 is
   controlled by the coefficient deviation ||a(j) - e_s||_1 times the basis
   geometry (and conversely — derive both directions; the basis rows' mutual
   l1 distances enter: define the basis gap/diameter explicitly).
2. The quantity T(u_s) becomes a statement about u_s's positive mass weighted
   by coefficient deviation: T <= sum_j (P_{u_s j})_+ ||a(j) - e_s||_1 * (basis
   scale). Now use the FREE identity IN COORDINATES: applying the coordinate
   map to sum_j P_{u_s j}(p_j - p_{u_s}) = 0 gives sum_j P_{u_s j} (a(j) - e_s)
   = 0 COMPONENTWISE (k scalar identities, no norms!) — each component's
   positive part is bounded by its negative part <= (coefficient bound 1) *
   nu_{u_s} <= delta. SUM OVER t: sum_t |sum_j P_{u_s j}(a_t(j) - delta_{ts})|
   <= 2*k*delta?? — careful: that introduces k. The scalar target needs
   sum_j (P)_+ sum_t |a_t(j) - delta_{ts}| — the sum-abs is INSIDE j but
   OUTSIDE t vs the identity's t-wise cancellation: the gap is now
   FINITE-DIMENSIONAL (k coefficients, each in [-1,1], summing to 1).
   Exploit: sum_t a_t(j) = 1 exactly => the deviations a(j) - e_s sum to 0 =>
   ||a(j) - e_s||_1 = 2 * (negative part of the deviation + ...) — relate the
   l1 deviation to the NEGATIVE coefficient mass and to (1 - a_s(j)); then
   u_s's positive-mass-weighted negative-coefficient mass may be controllable
   by the sum rules / a second application of idempotence at the COEFFICIENT
   level (the a-coordinates of an idempotent satisfy their own exact algebra:
   derive a(P x) in coordinates — the coefficient matrix is itself idempotent!
   a_t(j) = entries of an idempotent k x k system? — work it out: with
   p_j = sum a_t(j) p_{u_t}, applying P and idempotence gives exact relations
   among the a's; find them and use them the way the free identity was used).
3. MAXIMALITY as an inequality: max-volume means swapping u_s for any row j
   does not increase the basis volume — translate to |a_s(j)| <= 1 (known) AND
   sharper local statements (the volume ratio IS |a_s(j)| — Cramer; maximality
   over ALL rows including compositions?). Check whether maximality under
   P-averaging (u_s = sum_j P_{u_s j} p_j is a near-convex combination of
   rows — and a max-volume vertex being an average of others forces the
   average to concentrate on near-u_s rows! THIS is the geometric heart:
   a vertex of maximal volume cannot be a (1 + 2*delta)-almost-convex
   combination of points unless the combination concentrates near it —
   derive the quantitative version; the delta = 0 counterexample row is
   non-extremal precisely this way).
4. Numerics throughout (python3/numpy; the w29 audit script conventions);
   verify each candidate inequality on the saturator + split-block + certified
   + random samples. Track every k-dependence; the final C_D should be
   dimension-free — if k enters, say exactly where.

## DELIVERABLE (verdict-first; long form to proof.md)
VERDICT: LEMMA PROVED (display math, explicit C_D, honest dependence) /
DIED-AT (the exact gap + the minimal interface fact you'd request from the
telescoping route). Calibrated P(survives audit). Save code + outputs.
