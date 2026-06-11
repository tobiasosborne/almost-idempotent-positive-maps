# w26_cluster_audit: hostile audit of the rank-conditioned clustered chart (L2-partial)

You are a codex (gpt-5.5) HOSTILE AUDITOR. A prover claims the clustered-
conditioning chart with explicit constants: clustering scale eta = sqrt(delta),
proportionality error F = eta, coefficient bound A = R(1+R)^(k-1) with
R = 1 + 2*delta, k = rank(P). It kills the split-block 1/delta blow-up but is
rank-dependent. Break it, or confirm it with corrected constants. Cardinal
failure mode: a confident, plausible, WRONG claim.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w26_cluster_audit.
PROGRESS PROTOCOL: short line per stage to progress.md.
ARTIFACT RULE: long form to audit_report.md, NEVER answer.md.

## THE CLAIM
agent-A/explorations/classical-portfolio/notes/swarm-answers/w26_cluster.md
(full proof note appended; if unarchived: /tmp/codex-sigma-wall/w26_cluster/
proof.md + verify_cluster.py + cluster_results.json).

## CONTEXT
1. notes/swarm-answers/w25_hm112.md — the 1.12 bridge (the lemma chain L1-L4;
   the split-block obstruction family this must cure; analyze_hm112.py).
2. refs/hognas-mukherjea-2011/hognas-mukherjea-2011.txt ~:2245-2330 — Thm 1.12.
3. notes/swarm-answers/w21_recode_audit.md — the audited recoding lemma whose
   language (original removed/merged mass; one-shot final clustering) the
   chart should be compatible with; check consistency.
4. notes/swarm-answers/w16_quotient.md — the conjugation-smearing caveat
   (exact equality is not robust; eta-clustering is supposed to be the cure —
   verify the claimed chart is actually robust to S = I + O(eta') similarity
   smearing, or state the gap).

## AUDIT TASKS (derive-first)
1. RE-DERIVE the chart construction and each constant: why eta = sqrt(delta)
   (what breaks at eta ~ delta or eta ~ delta^{1/4}?); the proportionality
   error F; the coefficient bound A = R(1+R)^{k-1} — re-derive the recursion
   behind the (1+R)^{k-1} growth and check it is TIGHT or an artifact of the
   proof's ordering (a greedy/per-class argument often gives products that a
   global argument turns into sums — is there an easy improvement to
   polynomial-in-k or even constant? If you can IMPROVE the bound, that is a
   first-class outcome — derive it).
2. WELL-DEFINEDNESS: dependence on representative choice and on the clustering
   order (merge order can change the clusters at scale eta — does the chart's
   error budget cover re-clustering ambiguity?); behavior under the
   conjugation smearing of context item 4.
3. INDEPENDENT NUMERICS: re-implement the chart (your own code); verify on
   (i) the split-block family at eps in {1e-3, 1e-4, 1e-5} (claimed: max
   coefficient 1.0, distance 2*delta), (ii) the w19 leftcone family,
   (iii) the certified w16/w17 rational instances, (iv) ADVERSARIAL new
   families targeting the rank-dependence: chains of k nearly-proportional
   classes at pairwise scale ~eta designed to force the (1+R)^{k-1} cascade —
   does the bound saturate (the rank-dependence is REAL) or stay O(1) (the
   bound is loose)? This is the decisive experiment for the dimension-free
   question — design it carefully and report the measured growth in k.
4. L3 STATEMENT check: the proof note states L3 precisely — is it correctly
   posed given your findings (does it need A, and does A's k-dependence
   propagate into the final G(delta), making the global route rank-dependent —
   the parent project's known disease)? State what a dimension-free route
   would minimally require.

## DELIVERABLE (verdict-first; long form to audit_report.md)
VERDICT: HOLDS (constants confirmed; the k-growth measured: real vs loose) /
HOLDS WITH IMPROVEMENT (your better bound + proof) / BROKEN (the failing
family). Then the decisive k-growth experiment results, the well-definedness
assessment, the L3 propagation analysis, and calibrated P(verdict survives).
Do not soften.
