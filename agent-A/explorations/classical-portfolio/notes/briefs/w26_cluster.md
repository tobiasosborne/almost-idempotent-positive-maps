# w26_cluster: the clustered-conditioning lemma (L2 of the 1.12 bridge)

You are a codex (gpt-5.5) PROVER with numerics, on the single named missing
step of the campaign's best route to the GLOBAL statement.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w26_cluster.
PROGRESS PROTOCOL: short line per stage to progress.md.
ARTIFACT RULE: long-form proof to proof.md, NEVER answer.md.

## READ FIRST
1. agent-A/explorations/classical-portfolio/notes/swarm-answers/w25_hm112.md —
   the 1.12 bridge analysis: the candidate lemma chain (its "Candidate lemma
   chain" section: L1 stochastic 1.12 coordinates / L2 clustered conditioning /
   L3 signed concentration / L4 constructive projection), the split-block
   obstruction family (B coefficients ~ 1/delta when exact proportional classes
   split a limiting recurrent block; the MERGED point is 2*delta-close), and
   the numerics script experiments/out/w25_hm112/analyze_hm112.py.
2. refs/hognas-mukherjea-2011/hognas-mukherjea-2011.txt — Theorem 1.12
   (~:2245-2330): statement + proof (exact linear algebra; classes = maximal
   sets of mutually proportional rows; the sum rules (1.2)-(1.4)).
3. notes/swarm-answers/w21_recode.md + w21_recode_audit.md — the audited
   mass-removed recoding lemma (final-profile form): your merging step should
   speak its language (bounds in removed/merged ORIGINAL mass, one-shot to the
   final clustering — never iterate stepwise).
4. notes/swarm-answers/w19_tangent.md, w20_t1_audit.md — the banked lemmas the
   eventual assembly will use; OVERVIEW.md §3/§4.7/§4.9 for the map.

## TARGET — the clustered-conditioning lemma
Let P be exactly idempotent, P1 = 1, row negative mass <= delta (small). The
exact 1.12 partition uses EXACT row proportionality; the obstruction is that
near-proportional-but-distinct classes mis-split limiting blocks. PROVE a
clustering statement of the shape: there is a scale eta (state it — eta ~
C*delta? C*sqrt(delta)? derive what the split-block family forces) and a
clustering of the rows (merge 1.12 classes whose representative rows are
within eta in the right projective/l1 sense) such that, in the merged
coordinates:
 (a) every merged class has a representative row, and all rows of the class
     are within F(eta, delta) of proportional to it (quantify);
 (b) the B-coefficients in the merged coordinates are BOUNDED (|a_t(i)| <= A,
     sum_t a_t(i) = 1 exactly from P1 = 1 — derive), killing the 1/delta
     blow-up of the unmerged chart;
 (c) the exact sum rules (1.2)/(1.3) descend to the merged classes with error
     controlled by (eta, delta) — state the merged rules;
 (d) WELL-DEFINEDNESS: the clustering is canonical enough (independent of
     representative choices up to controlled error; if only a finite set of
     admissible clusterings exists, that is fine — say so; mind the
     conjugation-smearing caveat from w16_quotient: exact equality is not
     robust, your eta-clustering is exactly the cure if done right).
VERIFY against: (i) the split-block family (must now give bounded coefficients
+ a 2*delta-close merged H-M candidate); (ii) the w19 leftcone family (must
stay harmless); (iii) the certified w16/w17 rational instances (above-corner:
report what the merged chart gives there, no small-delta claim).
THEN (if L2 lands): state precisely what L3 (signed concentration: bounded
merged coordinates + sum rules + entries >= -delta => each merged class is
within G(delta) of an equal-input block and B-rows within G(delta) of convex
mixtures) needs, and attempt its first estimate. Do NOT claim the global
statement; the deliverable is L2 (+ L3 progress).

## DELIVERABLE (verdict-first; long form to proof.md)
VERDICT: L2 PROVED (statement + proof, display math, explicit eta/A/F and
their delta-dependence; the three verification families' numbers) / PARTIAL /
DIED-AT (the exact failed estimate + what the split-block geometry forces
instead). Calibrated P(L2 survives audit), P(L2+L3 reach the global
statement). Save code + outputs.
