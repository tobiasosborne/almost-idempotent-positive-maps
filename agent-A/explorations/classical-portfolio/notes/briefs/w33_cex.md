# w33_cex: REFUTE the signed-face excess — realize the transverse-pair conspiracy via the H-M 1.12 converse

You are a codex (gpt-5.5) REFUTER. Your prover twin is attacking the same
inequality from the proof side; your job is to BREAK it. The campaign's entire
global route rests on the signed-face excess (SF) below; the live refutation
window is real (prior prover calibration: P(small-delta counterexample) = 0.18).

Repo root: /home/tobias/Projects/almost-idempotent-positive-maps (readable).
Workdir (writable): /tmp/codex-sigma-wall/w33_cex.
PROGRESS PROTOCOL: append one short line per stage to progress.md (eager flush).
ARTIFACT RULE: long-form construction/obstruction analysis to proof.md, NEVER
answer.md. Save all code + outputs in the workdir.
TOOLING: gurobi available (gurobi_cl + gurobipy 13.0.1). NO network. NO
wolframscript. numpy/scipy/sympy (exact rationals!) available.

## THE TARGET TO BREAK (the signed-face excess, SF)
P real d x d, P^2 = P exactly, P1 = 1, row negative mass nu_i <= delta;
u_1..u_k the max-volume actual-row basis, p_j = sum_t a_t(j) p_{u_t},
|a_t(j)| <= 1, sum_t a_t(j) = 1. SF claims for each s:

  sum_j (P_{u_s j})_+ * ( sum_{t != s} (-a_t(j))_+ - (1 - a_s(j)) )_+
    <= C_sf * delta   with C_sf dimension-free.

A counterexample = a FAMILY (P_n, delta_n) with the excess / delta_n -> infinity
(or even just provably > any fixed constant), with the chart constraints honored
(max-volume basis recomputed per instance — do not assume your intended basis
is the max-volume one; VERIFY or re-derive the chart).

## THE CONSTRUCTION MACHINERY (use this — it is the underused lever)
Hognas-Mukherjea Theorem 1.12 CONVERSE (refs/hognas-mukherjea-2011/
hognas-mukherjea-2011.txt, lines ~2246-2277, 2337; byte-verify with grep -nF):
any real matrix with a partition {T; B; C_1..C_k} satisfying (1.1)-(1.4) is
idempotent of rank k. So you can BUILD exact idempotents to order: pick k
representative rows, attach proportional classes, then add B-rows whose
coefficient vectors you choose freely subject to (1.1)-(1.4) — e.g. the
transverse-pair family a(j) = e_s + a(e_t - e_r), a(j') = e_s - a(e_t - e_r).
Then normalize to P1 = 1 and COMPUTE: row negative masses (the delta you paid),
the max-volume chart, and the SF excess. Exact rationals (sympy / fractions).

## READ FIRST (under agent-A/explorations/classical-portfolio/)
1. notes/swarm-answers/w31_tax.md — section 4 (the exact failed split = your
   blueprint: rows with a_s(j) = 1, sum_{t!=s} a_t(j) = 0, sum |a_t(j)| > 0),
   section 5 (numerics: transverse pairs at amplitude a carry tax/delta ~ 1;
   ratios did NOT grow with rank in the LP stress — your job is to find the
   mechanism that stacks).
2. notes/briefs/w32_excess.md — the exact identities (i)-(vii) any instance
   must satisfy; w32's banked finding: coefficient-only constraints DON'T pin
   the geometry — exploit that freedom.
3. notes/swarm-answers/w29_displacement.md — the delta=0 counterexample to the
   GENERAL-ROW version (the trick that worked once: non-representative rows
   absorbing the violation). Ask: can a variant dodge max-volume?
4. notes/swarm-answers/w25_hm112.md — the 1.12 loci table + the split-block
   instability (exact classes splitting => coefficients of size 1/delta — a
   potential amplification mechanism if it survives inside the max-volume
   chart).

## THE CENTRAL QUESTION YOUR SEARCH MUST ANSWER
Why does each transverse pair seem to cost Theta(delta) of negativity budget
per Theta(delta) of excess? Find the configuration where MANY pairs share the
SAME negativity budget (overlapping supports, telescoping signs, the w25
split-block 1/delta-coefficient mechanism, near-degenerate bases pumping the
chart), or PROVE the per-pair cost is unavoidable — a sharp obstruction lemma
("each unit of excess consumes a unit of negative mass that no other unit can
reuse") would be a major step toward PROVING SF; state it precisely if you find
it. Either outcome is a win. Use gurobi (including NonConvex=2 bilinear at
small sizes) to SEARCH: maximize excess/delta over exact idempotents at small
(k, d), then study the maximizers' structure and scale.

## DELIVERABLE (verdict-first; long form to proof.md)
VERDICT: COUNTEREXAMPLE (exact-rational family + a verification script that
checks P^2=P exactly, P1=1, nu_i <= delta, recomputes the max-volume chart,
and evaluates excess/delta; growth demonstrated) / BOUNDED (best instances
found, excess/delta plateau value, + the precise obstruction that blocks
stacking, stated as a candidate lemma) / DIED-AT (what you tried, the exact
wall). Calibrated P(survives audit). Save all code + outputs in the workdir.
