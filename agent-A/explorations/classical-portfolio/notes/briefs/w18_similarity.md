# w18_similarity: the cohomological route, revived — corner splitting + similarity orbit + Newton

You are a codex (gpt-5.5) RESEARCH+COMPUTE worker in a 5-worker round whose
shared charge is: exploit the exact quadratic constraint P^2 = P to its fullest.
Your lens: THE COHOMOLOGICAL/ERROR-REDUCTION ROUTE — never run in this lane
(verified: zero cohomology mentions in the classical-portfolio record; it lived
only in the parent project's Layer-1 programme). It is also the route the
wave-10 meta-finding ASKS for: it avoids hiddenness as a hypothesis entirely.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w18_similarity.
PROGRESS PROTOCOL: append one short line per stage to
/tmp/codex-sigma-wall/w18_similarity/progress.md.

## CONTEXT (read first)
1. report/kernel-conjecture.tex (under agent-A/explorations/classical-portfolio/)
   — definitions; the delta=0 anchor (H-M Thm 1.16 normal form: recurrent
   equal-input blocks + transient convex mixtures); §5 ledger. The target: the
   LINEAR LAW delta >= c*H — equivalently (audited W-free target, wave-10):
   every exact signed stochastic idempotent is O(delta)-close to the
   Baake-Sumner/H-M normal-form family.
2. The dossier (notes/wave5-sigma-wall-parallel.md): wave-10 table +
   meta-finding ("any proof must either live in the exposedness-LP frame —
   where the pushed-witness certificate blocks cleanup — or avoid hiddenness
   as a hypothesis"); wave-15/16 (clone-invariance mandatory; anti-splitting
   died-at; the certified sigma-crossing instance).
3. The certified exact rational instance:
   experiments/out/w16_cert_audit/w16_best_rational_instance.json — your
   mandatory test object.
4. notes/swarm-answers/w14_autopsy.md + w15_audit.md — which delta=0 proof
   steps are sign-rigid (your normal-form coordinates must not secretly assume
   them).

## THE ROUTE (develop it rigorously)
1. CORNER SPLITTING: fix a candidate base idempotent P_0 (an H-M normal form).
   Matrix space splits into the four Peirce corners of P_0:
   E_11 = P_0 M P_0, E_10 = P_0 M (1-P_0), E_01 = (1-P_0) M P_0,
   E_00 = (1-P_0) M (1-P_0). Linearize the variety {P^2 = P} at P_0: the
   tangent space is E_10 (+) E_01 (the "cohomological degrees of freedom"),
   while E_11 (+) E_00 deviations are QUADRATICALLY DETERMINED (the
   error-reduction direction). Derive the exact quadratic correction map and
   its norm bounds in the campaign's row-sum norm.
2. SIMILARITY: for idempotents with ||P - Q|| < 1 (suitable norm), the
   explicit similarity S = QP + (1-Q)(1-P) satisfies S P = Q S (derive it;
   bound ||S - I|| <= ||P - Q|| and the conditioning of S^{-1}). Consequence:
   the problem "is P within O(delta) of a stochastic idempotent" becomes a
   geometry-of-the-orbit problem: choose Q in the H-M family minimizing
   distance; P and Q are then SIMILAR, and the question is whether the
   similarity can be taken row-stochastic-compatible.
3. NEWTON/ERROR-REDUCTION with positivity projection: alternate (a) project
   the entrywise-negative part away (rounding toward the nonneg cone — this
   LEAVES the variety), (b) retract back to the variety via the corner-
   quadratic correction (this is where exactness of idempotence does ALL the
   work: the retraction is quadratically small — ||correction|| =
   O(||deviation||^2)). The hoped contraction: delta_{m+1} = O(delta_m^2)/gap.
   Identify the GAP quantity that controls the retraction (the separation of
   P's spectrum is FREE: spec = {0,1} exactly! What replaces the gap is the
   conditioning of the corner equations — make it precise: which campaign
   quantity is it? Is it clone-invariant? Is it where hidden vertices bite?).
   THE HONEST QUESTION: where does this loop FAIL for the certified crossing
   instance? Run it numerically (python3/numpy; the instance is rational) —
   does the iteration converge to an H-M point at distance O(delta), or does
   it stall/escape? Either outcome is decisive intelligence: convergence
   evidence FOR the linear law via a constructive route; stall = the precise
   geometric obstruction, in coordinates nobody has looked at.
4. WHY IT MIGHT EVADE THE DEAD ENDS (verify each claim against the record):
   no hiddenness hypothesis (evades the LP-frame collapse + pushed-witness);
   works at matrix level with masses (clone-invariance: check — does cloning
   commute with the corner splitting? the quotient instance has the same
   normal form); not chain-local (evades w15_sos falsity). The known risk:
   the t3 rank-complement death ("quantitative (delta,H,W)-complementation
   algebra") is ADJACENT — read its died-at and explain exactly how the
   corner-quadratic mechanism differs (the answer should be: t3 lacked the
   retraction's quadratic gain; verify by reading t3's answer in
   notes/swarm-answers/ if archived).

## DELIVERABLE (verdict-first)
VERDICT: ROUTE VIABLE (the precise lemma chain: corner-splitting lemma ->
retraction bound -> contraction -> linear law, each in display math, with the
identified gap quantity) / ROUTE BLOCKED (the exact obstruction + which corner
fails, with the numerical run on the certified instance as evidence). Then the
numerical results (iteration trace on the certified instance + 2-3 random
small instances), UNVERIFIED-LEAD list, and calibrated P(route yields a proved
contraction lemma in one wave), P(route proves the linear law eventually).
Save all code + traces.
