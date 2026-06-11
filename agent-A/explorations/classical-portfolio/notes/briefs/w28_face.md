# w28_face: the final estimate of the 1.12 bridge — representative off-cluster mass <= C*(eta + delta/eta)

You are a codex (gpt-5.5) PROVER with numerics. The campaign's route to the
GLOBAL statement now hangs on EXACTLY ONE estimate, in the signed
affine-face case. Prove it or exhibit the saturating family.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w28_face.
PROGRESS PROTOCOL: short line per stage to progress.md.
ARTIFACT RULE: long-form proof to proof.md, NEVER answer.md.

## THE STATE (read in order; all under agent-A/explorations/classical-portfolio/)
1. notes/swarm-answers/w27_concentration.md — THE TARGET in context: the full
   proof note has (a) in-class concentration PROVED (G1 = eta + 2*delta),
   (b) cross-cluster representative leakage PROVED (<= 2*delta/(1-eta)),
   (c) the rank-2 family refuting O(delta) (the true scale is sqrt(delta)),
   (d) the CONDITIONAL L4 ASSEMBLY: if the target below lands, the W-free
   O(sqrt(delta)) H-M distance follows in ||.||_{infty,1}. Read its exact
   definitions (M_s = the eta-pivot clusters, u_s = the max-volume
   representative rows, B_eta = the non-class rows).
2. notes/swarm-answers/w26_cluster_audit.md (+ experiments/out/
   w26_cluster_audit/audit_report.md) — the dimension-free L2 chart (A = 1,
   max-volume basis) whose notation the target uses.
3. notes/swarm-answers/w25_hm112.md + refs/hognas-mukherjea-2011/
   hognas-mukherjea-2011.txt ~:2245-2330 — Thm 1.12 and the exact sum rules
   (1.2)/(1.3) — the structural input.
4. Audited tools available: w19_tangent; w20_t1_audit; w21_recode(+audit);
   the row-reproduction modulus dist(p_i, conv{p_j: P_ij>0}) <= (2+4delta)nu_i
   (w15_audit); exact idempotence P^k = P; P1 = 1.

## TARGET
With eta = sqrt(delta) (but prove for general eta if natural):
  max_s sum_{j not in M_s} |P_{u_s j}| <= C * (eta + delta/eta),
i.e. each max-volume representative row's TOTAL mass outside its own cluster
is O(sqrt(delta)) — in the SIGNED AFFINE-FACE case (the w27 note identifies
exactly which configurations escape its proved cases: read its died-at
section carefully and start there).
KNOWN CONSTRAINTS your proof must respect:
- The w27 rank-2 family SATURATES the bound at sqrt(delta) (mass exactly
  sqrt(delta) on B_eta) — so C >= 1 and no better exponent exists; your proof
  must accommodate that family, not contradict it.
- Work dimension-free (no n-counts; telescope via normalization/sum rules);
  the L2 coefficient bound A = 1 is available.
- Exact idempotence applied to the representative row: u_s = u_s P = u_s P^m —
  the representative reproduces itself through ALL rows; combine with in-class
  concentration (the class rows are eta-close to u_s) and the sum rules to
  force off-cluster mass to either return (bounded by delta-budget terms) or
  sit on B_eta rows whose OWN coordinates are bounded (A = 1) — the
  delta/eta term should appear where a small divisor eta enters from
  near-proportionality; find the right telescoping.
- Numerics FIRST (python3/numpy): implement the quantity max_s sum |P_{u_s j}|
  off-cluster on (i) the w27 rank-2 saturating family, (ii) the split-block
  family, (iii) random small-delta variety samples, (iv) the certified
  w16/w17 instances — measure the ratio to (eta + delta/eta); confirm the
  conjectured shape before proving.
IF PROVED: run the w27 conditional L4 assembly END-TO-END (its proof note has
the construction): state the resulting GLOBAL theorem (the W-free
O(sqrt(delta)) H-M distance, ||.||_{infty,1}, explicit constants + delta_0)
and verify it numerically on all the families above. Do NOT overclaim beyond
what the assembly licenses.

## DELIVERABLE (verdict-first; long form to proof.md)
VERDICT: ESTIMATE PROVED (+ THE GLOBAL THEOREM assembled, explicit constants)
/ DIED-AT (the exact failed sub-estimate + the family that saturates/escapes)
/ COUNTEREXAMPLE (a family violating C*(eta + delta/eta) for every C — that
would re-route the campaign: report loudly). Calibrated P(survives audit).
Save code + outputs.
