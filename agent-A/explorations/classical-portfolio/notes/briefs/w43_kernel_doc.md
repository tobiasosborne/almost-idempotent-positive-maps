# w43_kernel_doc: rewrite the kernel-conjecture document to the (EX) interface

You are a codex (gpt-5.5) TECHNICAL WRITER with full mathematical competence.
The campaign's open kernel has moved from the path-product floor (the version
in the existing document) to the existence statement (EX). Produce v2 of the
user-facing kernel document: fully self-contained, every definition from
scratch, honest statuses. This is the document a fresh expert mathematician
reads to attack the open problem cold.

Repo root: /home/tobias/Projects/almost-idempotent-positive-maps (READ ONLY —
do not modify the repo). Workdir (writable): /tmp/codex-sigma-wall/w43_kernel_doc.
Deliverable file: kernel-conjecture-v2.tex in the workdir. It MUST compile:
run `latexmk -pdf kernel-conjecture-v2.tex` in the workdir and fix all errors.
PROGRESS PROTOCOL: one short line per stage to progress.md.

## TEMPLATE AND SOURCES
- FORMAT template: report/kernel-conjecture.tex (the v1 — match its style:
  self-contained definitions section, the conjecture in a box, the conditional
  chain with per-link statuses, the evidence/constraints ledger, the dead-route
  ledger). Reuse its preamble.
- CONTENT: notes/swarm-answers/ under agent-A/explorations/classical-portfolio/
  — read w33_cex, w33_sf_geom, w34_audit, w34_halfcex, w35_quantifier,
  w35_charge, w36_audit, w36_charge, w37_opus, w38_sb, w39_opus_repair,
  w40_ndg, w41_ex, w42_factor_audit (headers carry the verdicts; appendices
  the proofs). The chain upstream of SF: w35_quantifier's contract + the v1
  document's outer chain (lem-classical-equiv etc. — keep v1's outer framing,
  replace the kernel core).

## REQUIRED CONTENT (sections)
1. The classical conjecture (op-classical) verbatim from v1's framing.
2. Definitions from scratch: row negative mass delta(P); actual-row bases;
   the theta-1/2 quasi-max-volume class (with WHY theta=1/2: the B6 perturbed
   staircase, stated as a theorem with the exact family); the chart
   coefficients; lambda, sigma, mu, E, beta, Phi, V, S+, S*.
3. **THE KERNEL — (EX)** in a box: every row-stochastic idempotent P with
   delta(P) <= 1/4 has an actual-row basis U, Vol(U) >= (1/2) Vol_max(P),
   with max_s Phi_s(U) <= C0 delta(P) for a universal C0. State the empirical
   value C0 = 1 (and what attains it).
4. The PROVED machinery (each with status PROVED + where): (P1); the
   factorization S*_s <= 2 Phi_s + 6 delta (2-family: codex proof + opus
   audit, constants tight, class-wide); the RANK-2 THEOREM (codex proof,
   second-family audit pending — say so honestly); the (DEF) identity; the
   irreducibility of selection (the three refuted shortcuts, with the exact
   witnesses cited); the B6 theta-necessity theorem.
5. The conditional chain: (EX) => registry SF contract (C_sf = 2 C0 + 6) =>
   [w35_quantifier constants, theta = 1/2, A = 2, the routing caveat] =>
   representative displacement => face/L4 => global W-free O(sqrt delta) =>
   op-exposed-hull => op-classical. Per-link status tags (which links are
   audited, which conditional, which DIED-AT-used-conditionally — copy the
   honest tags from w36_audit B3).
6. Evidence ledger: rank 2 proved; rank 3: 278 exact instances, 53
   adversarial, worst min-chart ratio exactly 1; the moderate-delta phase
   structure (ratio 1 for delta <= 0.3, blow-up at delta = 1/2 staircase);
   what any proof of (EX) must respect (the no-center path saturation ~2,
   the windmill attempts, the near-degenerate horn).
7. Dead-route ledger (one line each + pointer): coefficient-only LP (w32);
   universal C <= 2 (dense pairs); exists-EXACT-max-volume (B6); pointwise
   ME; sigma-only; single-swap monotonicity; convexity/Jensen route (w33
   sec-6 refutation); (SIG) without overshoot (w38).
8. The live mechanism for (EX): the two-horn multi-row swap dichotomy +
   (NDG), and the rank-2 max-diameter template; what fails at rank >= 3.

HONESTY RULES: every status tag must match the archived verdict; the rank-2
theorem's pending second-family pass MUST be flagged; calibrations quoted
where the workers gave them; no claim upgraded. Cite archive paths
(notes/swarm-answers/wNN_*.md) in footnotes/margin notes for every load-
bearing claim.

## DELIVERABLE
kernel-conjecture-v2.tex (compiling; ~8-14 pages) + the built PDF in the
workdir + progress.md. Final message: confirmation it compiles + a 5-line
table of contents.
