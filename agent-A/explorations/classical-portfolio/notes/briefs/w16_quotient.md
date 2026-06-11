# w16_quotient: the clone-invariant (quotient) path-product floor — state it, secure the bridge, attack it

You are a codex (gpt-5.5) PROVER. The campaign's working conjecture (path-product
floor on the raw-index carrier graph) has just been hit by a cloning obstruction:
duplicate-index splitting preserves all row geometry and exact idempotence but
kills raw path products. The natural repair is the QUOTIENT form. Your job has
three stages: formulate, secure the bridge, then attack.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w16_quotient.
PROGRESS PROTOCOL: append one short line per stage to
/tmp/codex-sigma-wall/w16_quotient/progress.md.

## READ FIRST
1. report/kernel-conjecture.tex (under agent-A/explorations/classical-portfolio/)
   — all definitions (note def:vertex is ALREADY multiplicity-correct), the
   carrier graph + Pi_C definition (raw indices, ~lines 230-241), conj:floor,
   conj:kernel, the finisher paragraph, the constraints ledger (§5).
2. notes/swarm-answers/w15_prover.md — the cloning obstruction (read fully; your
   quotient form must provably neutralize exactly this).
3. notes/swarm-answers/w15_sos.md — chain-local certificates are DEAD: the scalar
   shadow is false; any proof must consume hiddenness/realization constraints.
4. notes/swarm-answers/w12_comp_finisher.md — the proved finisher you must
   re-attach; notes/swarm-answers/w15_periodic.md — the (audit-pending)
   periodicity exclusion; notes/swarm-answers/w15_audit.md — the tightened
   attachment hypotheses (closed component, radius < r* = 0.85*tau).
5. notes/swarm-answers/w13_chain_excl.md + w13_chain_refuter2.md — the prior
   stalemate's failure maps.

## STAGE 1 — FORMULATE (Conjecture 2')
Define the quotient carrier graph: nodes = geometric row classes [i] (exactly
coincident rows identified — same convention as def:vertex), edge weight
Q_{[i][j]} = sum_{b in [j]} P_{i,b} (well-defined? PROVE rows in one class give
the same aggregated weights — they are identical rows, so yes; write it).
Quotient path product Pi'_C over Q. State Conjecture 2': the floor for Q on the
quotient component. PROVE clone-invariance: for any duplicate-splitting P_hat,
the quotient objects of P_hat and P are isomorphic with equal Q (this kills the
w15 obstruction by construction). Also check: near-coincident (not exactly
coincident) rows — is exact-coincidence quotienting enough, or does a delta-
cloud of near-duplicates re-open the obstruction continuously? If yes, state
the eps-clustered variant and note its cost.

## STAGE 2 — SECURE THE BRIDGE (the finisher on the quotient)
The proved w12 finisher consumes raw path products / entry floors. Show identical
rows are stochastically lumpable: lumping commutes with the band block, the
Birkhoff-Hilbert projective contraction, and the radius bookkeeping
(2(1+delta)*eps/theta_C + 4*delta < r*), so the finisher applied to the quotient
component yields the SAME row-collapse conclusion for the original (rows in a
class are equal, so collapse on classes = collapse on indices). Derive it; this
is the load-bearing step that makes 2' a legitimate replacement target. If
anything fails, report exactly what.

## STAGE 3 — ATTACK Conjecture 2'
With cloning neutralized, attack the quotient floor. The H-M surrogate frame +
exact idempotence shortcut from w15_prover.md remain valid on the quotient
(P^k = P descends to Q-paths?). Aggregate-mass arguments that died at atom level
may live at class level: the row reproduction p_i = sum_j P_ij p_j aggregates to
classes with weights Q. Use hiddenness (the LP frame) — w15_sos proved you MUST.
You may run numerics (python3/numpy) in your workdir to test candidate
inequalities on small instances (build exactly-idempotent P = V W, W V = I).
If you die: state the EXACT failed inequality in display math + why each repair
fails + whether the quotient floor has its own obstruction in the same spirit
as cloning (e.g. near-duplicate clouds).

## DELIVERABLE (verdict-first)
VERDICT: 2' PROVED / BRIDGE SECURED + 2' OPEN (died-at, display math) /
2' ILL-POSED (its own obstruction — exhibit it). Then: the LaTeX-ready statement
of 2' + the lumping lemma, and calibrated P(2' is true), P(2' provable within
the campaign's frame). Explicit dimension-free constants everywhere.
