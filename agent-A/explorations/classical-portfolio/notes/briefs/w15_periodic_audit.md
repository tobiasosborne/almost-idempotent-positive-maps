# w15_periodic_audit: hostile audit of the periodicity-exclusion patch

You are a codex (gpt-5.5) HOSTILE AUDITOR. A prover claims the w12 component
finisher's declared primitivity gap is VACUOUS: exact idempotence excludes
nontrivial periodicity of closed positive components. Your job: break the proof.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps (read-only).

## READ
1. agent-A/explorations/classical-portfolio/notes/swarm-answers/w15_periodic.md —
   the patch under audit (statement + the periodic-exclusion proof).
2. notes/swarm-answers/w12_comp_finisher.md (same dir) — the PROVED finisher whose
   hypotheses the patch claims to inherit. CHECK THE DEFINITIONS MATCH: the patch
   assumes "positive mass from rows of C stays in C" (closure, d_i >= 1) and
   strong connectivity — is that exactly w12's component notion? Any drift between
   "w12 positive component" there and here voids the patch.
3. notes/swarm-answers/w12_chain_refuter.md — refuter #2's periodic template and
   dichotomy; does the patch's last paragraph correctly account for it?
4. report/kernel-conjecture.tex (same exploration dir) — definitions; the open-
   caveats item near lines 261-264 mentions periodic components — would this patch
   discharge it as stated?

## AUDIT TASKS (derive-first)
1. RE-DERIVE the central contradiction from scratch: period d >= 2 with cyclic
   classes C_0..C_{d-1}, positive edges only C_r -> C_{r+1}; fix i in C_r,
   T = C_{r+2 mod d}. Claimed: sum_{j in T} (A^2)_{ij} >= d_i >= 1 while
   sum_{j in T} (B^2)_{ij} <= zeta (since B_{iT} <= 0 and ||B^2 - B|| <= zeta),
   and the bridge sum_{j in T}(B^2)_{ij} >= 1 - 2*delta*(1+delta). CHECK THE
   BRIDGE CAREFULLY: B^2 = (A-N)^2 = A^2 - AN - NA + N^2 — does the claimed bound
   drop the N^2 term? Recompute the exact constant and the exact delta threshold
   at which the contradiction holds (the patch claims delta < 1/4 suffices via
   1 <= 3*delta + 4*delta^2 — verify; note 3*(1/4) + 4*(1/16) = 1 exactly, so
   check strictness and whether the true constant is worse).
2. EDGE CASES: d = 2 makes T = C_r itself (C_{r+2 mod 2} = C_r) — does the
   argument still work when T is i's own class (B_{iT} <= 0 may FAIL: B_{ii} can
   be positive)? If d = 2 breaks, the patch must handle it separately — find
   whether period-2 closed components are excluded by a repaired argument or are
   a REAL surviving case.
3. NORMS: the patch uses ||N|| <= delta, ||A|| <= 1+delta, zeta <= delta(1+2delta)
   — which norm (row-sum / l1->l1)? Are these the campaign's conventions
   (kernel-conjecture.tex: delta = row negative mass)? Do the matrix-product
   bounds used hold in that norm restricted to the block S?
4. The patched finisher display (R_C, E_L, the Pi_C upper bound in the
   "otherwise" branch): re-derive or flag as unsupported-as-stated.
5. The closure hypothesis: w12 components in the live campaign — is
   P^+_{S,S^c} = 0 exact closure realistic, or does the campaign only have
   APPROXIMATE closure (small positive leakage)? If approximate: does the
   exclusion proof tolerate leakage eta_leak (recompute the contradiction with
   d_i >= 1 - eta_leak)? State the tolerance.

## DELIVERABLE (verdict-first)
VERDICT: PATCH HOLDS (possibly with corrected constants — state them) /
PATCH HOLDS EXCEPT d=2 (state the surviving case precisely) / PATCH BROKEN
(exhibit the gap or a counterexample sketch). Every re-derived inequality in
display math, exact constants. Then calibrated P(your verdict survives a further
audit). Do not soften; finding errors is success.
