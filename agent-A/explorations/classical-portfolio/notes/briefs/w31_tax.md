# w31_tax: the transverse coefficient tax — the campaign's single named open

You are a codex (gpt-5.5) PROVER. TWO independent provers reduced the entire
classical campaign's best route to ONE inequality, with matching constants.
Prove the tax, or find the conspiring family.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w31_tax.
PROGRESS PROTOCOL: short line per stage to progress.md.
ARTIFACT RULE: long-form proof to proof.md, NEVER answer.md.

## THE TAX (the target)
P exactly idempotent, P1 = 1, row negative mass <= delta <= delta_0;
u_1..u_m the max-volume actual-row basis (audited L2 chart: every row
p_j = sum_t a_t(j) p_{u_t}, |a_t(j)| <= 1, sum_t a_t(j) = 1). Prove, for
each s:
  sum_j (P_{u_s j})_+ * sum_{t != s} (-a_t(j))_+  <=  C_mu * delta,
C_mu universal (dimension-free if possible; honest dependence otherwise).
In words: the rows that the representative u_s feeds positively cannot carry
much negative coefficient mass in foreign directions.
CONSEQUENCE CHAIN (already written, do not redo): tax => displacement lemma
(C_D <= 2(1+2delta_0)(2+C_mu), w30 proof notes) => face estimate (Markov,
w29 §9) => conditional L4 assembly (w27) => the GLOBAL W-free O(sqrt(delta))
theorem.

## READ (both reductions + the tools)
1. notes/swarm-answers/w30_telescope.md + w30_maxvol.md (under
   agent-A/explorations/classical-portfolio/) — the two independent
   reductions and their proof notes (experiments/out/w30_*/proof.md): how the
   tax arises in each; the exact coefficient identity a*P^+ = P_{u.} + a*P^-
   + b*P^+ - b*P^- from the telescope note; the Cramer/maximality facts from
   the maxvol note.
2. notes/swarm-answers/w26_cluster_audit.md (+ its audit_report) — the
   max-volume basis construction and A = 1.
3. notes/swarm-answers/w27_concentration.md — in-class concentration
   (G1 = eta + 2*delta) and the proved cross-cluster leakage <= 2delta/(1-eta).
4. notes/swarm-answers/w25_hm112.md + refs/hognas-mukherjea-2011/
   hognas-mukherjea-2011.txt ~:2245-2330 — Thm 1.12's EXACT sum rules
   (1.2)/(1.3): at delta = 0 they force coefficient convexity; the tax is
   their quantitative shadow — this is the most promising structural input:
   derive the coefficient-level consequences of (1.2)/(1.3) for OUR P
   (P1 = 1) and the max-volume basis, then bound the tax from them plus the
   delta-budget.
5. The free identity (w29): sum_j P_{uj}(a(j) - e_s) = 0 COMPONENTWISE — the
   t-component: sum_j P_{u_s j} a_t(j) = a_t(u_s P) = a_t(u_s) = delta_{ts}
   EXACTLY (idempotence at coefficient level!). So for t != s:
   sum_j P_{u_s j} a_t(j) = 0 EXACTLY — the signed sum of foreign
   coefficients vanishes. The tax asks: can the positive-mass-weighted
   NEGATIVE parts be large while the signed sum vanishes? The conspiracy
   needs matching positive a_t(j) mass on u_s's positive support — and
   a_t(j) > 0 with |a| <= 1 ... find what limits it (positive foreign
   coefficients on u_s's support mean those rows lean toward u_t: combine
   with in-class concentration at cluster t? a row positively fed by u_s but
   leaning toward u_t is exactly the cross-cluster leakage ALREADY BOUNDED by
   2delta/(1-eta) in w27?? — check whether the tax follows by combining the
   exact componentwise identity + the w27 leakage bound + a splitting of j's
   by cluster membership. Derive carefully; this looks closable — but beware:
   a_t(j) > 0 does not imply j is in cluster t (coefficients vs distance);
   quantify the gap via the basis geometry (A = 1 both ways?).)
6. NUMERICS FIRST (python3/numpy; conventions from
   experiments/out/w30_maxvol/maxvol_displacement_audit.py): measure the tax
   ratio (tax/delta) on the rank-2 saturator, split-block, certified w16/w17,
   random small-delta samples; find which rows carry it (cluster members vs
   B_eta rows) — that tells you which splitting to prove.

## DELIVERABLE (verdict-first; long form to proof.md)
VERDICT: TAX PROVED (display math, explicit C_mu, honest dependence; the
consequence chain stated as conditional corollaries) / DIED-AT (the exact
failed split + the minimal further fact) / COUNTEREXAMPLE (the conspiring
family with verified numbers — report loudly). Calibrated P(survives audit).
Save code + outputs.
