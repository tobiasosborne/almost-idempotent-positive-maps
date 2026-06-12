# w33_sf_geom: PROVE the signed-face excess — geometry-first LP loop + the H-M 1.12 converse parametrization

You are a codex (gpt-5.5) PROVER. The classical campaign's entire global route
now rests on ONE finite-dimensional inequality (the signed-face excess). Wave 32
started the LP/extremal attack and was stopped early; its single banked finding
is your starting constraint: **the coefficient-only LP relaxation is ALREADY too
weak at delta=0 — geometry is load-bearing from round one.** Do not re-run the
coefficient-only relaxation.

Repo root: /home/tobias/Projects/almost-idempotent-positive-maps (readable).
Workdir (writable): /tmp/codex-sigma-wall/w33_sf_geom.
PROGRESS PROTOCOL: append one short line per stage to progress.md (eager flush).
ARTIFACT RULE: long-form proof to proof.md, NEVER answer.md. Save all code +
outputs in the workdir.
TOOLING: gurobi IS available (gurobi_cl on PATH; gurobipy 13.0.1 importable).
NO network. NO wolframscript. numpy/scipy/HiGHS available.

## THE TARGET (the signed-face excess, SF)
P real d x d, exactly idempotent (P^2 = P), row sums 1 (P1 = 1), row negative
mass nu_i := sum_j (-P_ij)_+ <= delta <= delta_0. u_1..u_k the max-volume
actual-row basis (rows p_j = sum_t a_t(j) p_{u_t}, |a_t(j)| <= 1,
sum_t a_t(j) = 1 — the audited L2 chart). Prove for each s:

  sum_j (P_{u_s j})_+ * E_s(j) <= C_sf * delta,
  E_s(j) := ( sum_{t != s} (-a_t(j))_+  -  (1 - a_s(j)) )_+ .

E_s(j) > 0 iff the foreign coefficients of j are net-negative beyond the
deficit; E_s vanishes on convex coefficient vectors; at delta = 0, E_s = 0
identically (H-M coefficients are convex). C_sf must be dimension-free
(independent of d and of the rank k); dependence on delta_0 is acceptable.

## READ FIRST (under agent-A/explorations/classical-portfolio/)
1. notes/briefs/w32_excess.md — the predecessor brief: ALL exact identities
   at your disposal are listed there as items (i)-(vii); re-verify and use them.
   The partial script experiments/out/w32_excess/lp_excess_audit.py is reusable
   scaffolding.
2. notes/swarm-answers/w31_tax.md — the split that isolated SF (deficit part
   sum_j (P_{u_s j})_+ (1 - a_s(j)) <= 2 delta is PROVED there); section 4 =
   the exact failed split (transverse-pair family a(j) = e_s ± a(e_t - e_r));
   section 5 = numerics conventions + where the excess lives.
3. notes/swarm-answers/w30_maxvol.md + w30_telescope.md — the conditional
   chain (SF => tax with C_mu = 2 + C_sf => representative displacement with
   C_D <= 2(1+2delta_0)(4+C_sf)) and the Cramer facts.
4. notes/swarm-answers/w25_hm112.md — the Hognas-Mukherjea Theorem 1.12
   autopsy WITH the loci table (line numbers into
   refs/hognas-mukherjea-2011/hognas-mukherjea-2011.txt). Byte-verify any
   quote you use with grep -nF against that .txt (FULL string, not substring).

## THE TWO MANDATED ATTACK UPGRADES (what w32 did not get to)

### A. Geometry-first LP loop (gurobi)
For fixed small rank k (2, 3, 4) and modest d: treat the FULL matrix P as the
variable, not just the coefficients. Constraints: P1 = 1; the max-volume chart
constraints |a_t(j)| <= 1; row negative masses <= delta; AND the idempotence
P^2 = P. Idempotence is quadratic — handle it by ONE of:
  (a) gurobi's nonconvex bilinear QCP (NonConvex=2) at small sizes — maximize
      the excess directly; or
  (b) parametrize exactly via the 1.12 converse (attack B below) so idempotence
      is structural, and optimize over the remaining FREE parameters; or
  (c) alternate-fix linearization (fix the basis rows' geometry, LP over the
      rest; then re-fit) with the violating configurations fed back as cuts.
If the max excess is O(delta) with a dimension-free-looking constant across k:
extract the dual/active-set certificate, rationalize, convert to a proof. If
it grows: extract the configuration and try to defeat or realize it.

### B. The 1.12 CONVERSE as an exact parametrization (the underused lever)
H-M Theorem 1.12 has a CONVERSE: any real matrix P with a partition
{T; B; C_1; ...; C_k} satisfying (1.1)-(1.4) is idempotent of rank k (locus:
lines ~2276-2277 and 2337 of the .txt; byte-verify). That converse is an EXACT
parametrization of ALL rank-k real idempotents. The campaign's perturbation is
"exactness FREE, only positivity perturbed": so write SF's left side as a
function on the exact parametrization data (representative rows, proportionality
factors gamma, B-coefficients), with the ONLY constraint being the delta-budget
on row negative masses. At delta = 0 the H-M coefficients are convex and SF = 0.
Question: prove first-order stability — the delta-budget bounds the total
(P_{u_s j})_+-weighted transverse total-variation excess linearly. Work out
EXACTLY how the row-negativity budget propagates through (1.1)-(1.4) to
constrain signed B-coefficients. If the parametrized problem is self-similar
in rank (the coefficient matrix A is itself near-idempotent — w32 brief item
(vii)), set up the induction on k honestly or name why it fails.

## KNOWN HARD FACTS your proof must respect (do NOT rediscover)
- The transverse-pair family carries tax/delta ~ 1 IN-CLUSTER (not leakage):
  cross-cluster leakage (<= 2delta/(1-eta), w27) cannot pay for it.
- HM 1.12's sum rules sum_j P_{u_s j} a_t(j) = delta_st are exact signed
  barycentre identities — they permit the cancellation; they do not bound
  total variation by themselves (w31 section 3).
- Max-volume gives |a_t(j)| <= 1 and determinant bounds on multi-row swaps,
  NOT a = O(delta) on transverse amplitudes (w31 section 4).
- LP rank-stress saw NO growth of tax/delta with k (w31 section 5) — the
  truth is plausibly C_sf <~ 1-ish; aim for clean, not optimal.

## DELIVERABLE (verdict-first; long form to proof.md)
VERDICT: SF PROVED (display math, explicit C_sf, honest dependence; restate the
conditional chain consequences in one paragraph) / LP-CERTIFICATE AT SMALL k
(+ the general-k gap stated precisely) / DIED-AT (the exact configuration the
geometry-included loop could not cut + whether it is realizable as an exact
idempotent) / COUNTEREXAMPLE (verified exact-rational). Calibrated
P(survives audit). Save all code + outputs + gurobi logs in the workdir.
