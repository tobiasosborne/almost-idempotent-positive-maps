# w18_variety: the semi-algebraic / differential geometry of the idempotent variety

You are a codex (gpt-5.5) RESEARCH worker in a 5-worker round whose shared charge
is: the campaign has NOT yet exploited the exact quadratic constraint P^2 = P to
its fullest — reformulations so far retreat to weaker convex-hull information.
Your lens: the VARIETY STRUCTURE.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps (read-only).

## CONTEXT (read in this order)
1. agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex — the
   full problem (definitions; Conjecture 1 = kernel; the multiplicity-correct
   quotient floor; §5 ledger incl. the wave-15/16 constraints: clone-invariance
   mandatory, no chain-local certificates, the certified sigma-gate crossing at
   tiny height; the REAL proof target per the dossier: the LINEAR LAW delta >= c*H).
2. notes/wave5-sigma-wall-parallel.md — the WAVE 10 strategy-kind table (search
   "WAVE 10") + META-FINDING ("hiddenness IS the LP frame": any proof must either
   live in the exposedness-LP frame, where the pushed-witness certificate blocks
   cleanup, or avoid hiddenness as a hypothesis); the FINAL STATE + wave 15/16
   sections (anti-splitting died-at; cloning).
3. experiments/out/w16_cert_audit/w16_best_rational_instance.json — the certified
   exact instance (hidden v, sigma/tau = 1.63, H/tau = 0.016): a concrete test
   object on the variety.

## YOUR RESEARCH QUESTIONS
1. STRUCTURE: the set {P : P^2 = P, P1 = 1, rank P = k} — describe it exactly:
   the GL_n similarity orbit structure, smooth manifold/homogeneous-space
   structure, dimension, tangent space at P (corner blocks: T_P = P X (I-P)
   (+) (I-P) Y P), the row-stochastic slice, the explicit corner/Riccati
   parametrization around a base idempotent P_0 (P = P_0 + corners + the
   quadratically-determined diagonal deviation). Derive everything you state
   (no citations-as-proof: derivations or clearly-flagged UNVERIFIED-LEAD).
2. THE CONSTRAINTS ON THE VARIETY: the campaign's objects — delta (row negative
   mass), the nonneg stochastic idempotents (the H-M normal forms = the
   delta = 0 locus), hidden vertices, H — how do they sit on/along the variety?
   Is the delta = 0 locus a nice subvariety (stratified by partition data)? What
   is its normal geometry inside the idempotent variety — i.e. how fast must
   delta grow as you move away along the variety? (THE LINEAR LAW delta >= c*H
   is exactly a statement of this kind! H is a function on the variety vanishing
   on... what? Make this precise.)
3. ATTACK PLANS: produce your TOP 3 concrete attack plans exploiting the variety
   structure, each with: the precise first lemma to prove (display math), why it
   evades the recorded dead ends (LP-frame collapse, anti-splitting,
   clone-invariance — note: similarity/cloning acts ON the variety; quotienting
   = a group action?; a variety-intrinsic argument may be automatically
   clone-invariant — check!), and what it would feed (linear law / quotient
   floor / kernel directly).
4. Sanity-check your geometric claims symbolically on small cases (you may NOT
   run code — derive by hand for n = 2, 3, rank 1, 2) and against the certified
   instance's data where possible.

## DELIVERABLE (verdict-first)
A ranked list: TOP 3 attack plans (first-lemma statements in display math,
dead-end-evasion table, what each buys), then the structural write-up backing
them, then UNVERIFIED-LEAD list (any literature fact you used from memory —
precise statement + where to acquire it; the repo's grounding rule: nothing
binds until byte-matched in refs/). Calibrated P(at least one plan reaches a
new proved lemma within one wave) and P per plan.
