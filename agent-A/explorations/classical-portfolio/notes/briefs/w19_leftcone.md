# w19_leftcone: the quasi-positive left-fixed-cone extreme-point lemma (wave-18 semigroup plan 1)

You are a codex (gpt-5.5) PROVER with numerics. Wave-18's semigroup lens
produced a clone-invariant, hiddenness-free reduction: rows of an exact
idempotent live in the k-dim left fixed space. Prove its key lemma.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w19_leftcone.
PROGRESS PROTOCOL: append one short line per stage to
/tmp/codex-sigma-wall/w19_leftcone/progress.md.

## READ FIRST
1. agent-A/explorations/classical-portfolio/notes/swarm-answers/w18_semigroup.md
   — the fixed-space duality plan: P = sum_s u_s l_s^T (biorthogonal fixed
   bases), every row p_i = sum_s u_s(i) l_s^T; {g : Pg = g} is dual to the
   row affine geometry; the proposed lemma (its "Unverified Leads" item 1).
2. report/kernel-conjecture.tex — definitions (visible/hidden, H, sigma_tilde,
   delta = row negative mass, tau = sqrt(delta)).
3. notes/swarm-answers/w14_autopsy.md + w15_audit.md — at delta = 0 the left
   fixed cone is spanned by the recurrent-class distributions pi_s (= the
   visible rows); the audited sign-robust moduli you may use.
4. The certified instances (notes/swarm-answers/w16_cert_audit.md,
   w17_antecedent.md + experiments/out/w16_cert_audit/
   w16_best_rational_instance.json) — mandatory consistency checks.

## TARGET (the lemma; sharpen the statement as needed)
Let P be exactly idempotent, row-stochastic up to row negative mass <= delta.
Consider the left-fixed affine slice
  K_C = { l : l P = l, l 1 = 1, neg(l) <= C*delta }
(neg = total negative part). Prove: there exist universal constants (or
constants with explicitly-stated dependence) such that every EXTREME point of
K_C is within O(delta) (l1) of the row set {p_i} — ideally of a VISIBLE row.
Subgoals:
(a) delta = 0 case from the H-M structure: extreme points of the left-fixed
    probability slice = the recurrent-class rows pi_s. Derive it (do not cite).
(b) Perturbative case: exact idempotence gives l = l P = l P^m for all m —
    the all-lengths averaging is YOUR tool (this is where the constraint
    bites; the w18_semigroup boundary identities may help).
(c) The duality payoff: show how the lemma feeds the campaign — e.g. every
    row p_i is a combination of k left-fixed vectors; if all extreme points of
    K_C are near visible rows, what does that force for a hidden row with
    large sigma_tilde? Derive the implication chain toward H <= C'*delta or
    the kernel statement; state precisely what additional lemma (if any) the
    chain needs.
(d) CLONE-INVARIANCE check (should be automatic — left-fixed vectors aggregate
    over duplicate columns; verify).

## METHOD
Derive everything; numerics allowed (python3/numpy/scipy) to test the lemma on
(i) random H-M points + small perturbations ON the variety (use the corner
chart from notes/swarm-answers/w18_variety.md), (ii) the certified rational
instance (compute its left-fixed space, the K_C extreme points via LP
vertex enumeration at n = 7 — tractable; CHECK: are they near visible rows
even though sigma_tilde/tau = 1.63? The lemma predicts yes — if NO, the lemma
is false as stated: report the corrected version the data suggests).

## DELIVERABLE (verdict-first)
VERDICT: LEMMA PROVED (proof, display math, explicit constants + dependence) /
FALSE AS STATED (the counterexample from data + the corrected statement) /
PARTIAL (the delta = 0 case + what blocks the perturbation). Then the
implication-chain analysis (c), the numerical tables, and calibrated
P(lemma true), P(chain reaches the linear law). Save code + outputs.
