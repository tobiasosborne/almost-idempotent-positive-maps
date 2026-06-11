# w15_prover: the path-product floor via the H-M signed-surrogate frame

You are a codex (gpt-5.5) PROVER. After 13 waves the entire classical campaign is
jammed at ONE inequality (the kernel). A fresh autopsy of the real delta=0 proof
(Hognas-Mukherjea) has just produced a new frame nobody has attacked with. Your job:
prove the floor, or die at a sharply-stated inequality.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w15_prover.
PROGRESS PROTOCOL: append one short line per stage to
/tmp/codex-sigma-wall/w15_prover/progress.md (stage name + status).

## READ FIRST (in this order)
1. agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex — the
   complete self-contained statement: all 7 definitions, Conjecture 1 (kernel),
   Conjecture 2 (path-product floor, the working form), the proved
   component-finisher bridge, and the evidence/constraints ledger (what any proof
   MUST respect; which routes are PROVED DEAD — do not rewalk them).
2. notes/swarm-answers/w14_autopsy.md (same dir as below): the H-M autopsy. Key
   output: the delta=0 proof's kernel/minimal-ideal mechanism is sign-rigid at the
   zero-sum-closure step, but its signed analogue is: visible exposed vertices play
   the recurrent classes; hidden top vertices generate a shallow positive carrier
   graph; a strongly connected positive component with enough path-product mass is
   the "approximate minimal ideal". EXACT idempotence is FREE (P^2 = P exactly; only
   positivity is perturbed, entries >= -delta) — exact row reproduction
   p_i = sum_j P_ij p_j is SIGN-ROBUST with modulus
   dist(p_i, conv{p_j : P_ij > 0}) <= (2+4*delta)*nu_i.
3. agent-A/explorations/classical-portfolio/notes/swarm-answers/: w13_chain_excl.md
   (the previous prover's died-at — start PAST it), w13_chain_refuter2.md and
   w12_chain_refuter.md (the refuters' quantified failure maps — these constrain
   what is true), w12_comp_finisher.md (the PROVED component finisher you may
   import as a black box, respecting its hypotheses).

## TARGET
Path-product floor (kernel-conjecture.tex Conjecture 2 — use its exact statement):
for the band component C of any hidden top vertex with sigma_tilde > tau,
  Pi_C >= tau - O(L*delta)   (or any floor Pi_C >= c*sqrt(delta) - C'*L*delta
strong enough to feed the component finisher). TRUE => thin-chain exclusion =>
linear law delta >= c*H => HLC => op-exposed-hull => op-classical.

## METHOD CONSTRAINTS
- The NEW angle is the H-M surrogate: run the minimal-ideal construction on the
  positive carrier graph, using EXACT idempotence at every step where H-M uses
  measure positivity, and convert each sign-rigid step via the autopsy's repair
  column. Iterate P^k = P (free!) to amplify path products along C before signed
  error accumulates — check whether k-step path products beat the O(L*delta) loss.
- Every step derived, no "standard facts" asserted; constants explicit and
  dimension-free (no n-dependence).
- You may write and RUN small numerical experiments in your workdir to test
  intermediate claims before proving them (python3; numpy available).
- If a step needs the component finisher, verify its hypotheses are satisfied.

## DELIVERABLE (verdict-first)
VERDICT: PROVED / PARTIAL (state exactly what is proved) / DIED-AT. If proved: the
full proof, every inequality in display math, explicit constants. If died-at: the
EXACT inequality that failed, in display math, plus why each natural repair fails.
Then calibrated P(the floor is true) and P(this route can close it with more work).
