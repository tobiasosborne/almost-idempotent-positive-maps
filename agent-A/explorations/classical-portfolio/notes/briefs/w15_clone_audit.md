# w15_clone_audit: hostile audit of the CLONING OBSTRUCTION to the path-product floor

You are a codex (gpt-5.5) HOSTILE AUDITOR. A prover claims Conjecture 2 (the
path-product floor) is FALSE-OR-VACUOUS as written, via an index-cloning
construction. If correct this redirects the campaign. Break it if you can.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps (read-only).

## READ
1. agent-A/explorations/classical-portfolio/notes/swarm-answers/w15_prover.md —
   the claim under audit (the cloning construction is at the end).
2. report/kernel-conjecture.tex (same exploration dir) — the EXACT statements:
   def:vertex (multiplicity-correct row vertices, ~line 84), the carrier-graph +
   path-product definitions (~lines 230-241), Conjecture conj:floor (~243-255),
   the finisher paragraph after it, and Conjecture conj:kernel.
3. notes/swarm-answers/w12_comp_finisher.md — the proved finisher (for task 4).
4. notes/swarm-answers/w15_sos.md — the independent scalar-shadow falsity result
   (for coherence cross-check in your overall verdict).

## THE CLAIM
Split index r into M duplicates: surjection pi, fiber weights alpha_b > 0 summing
to 1 per fiber, P_hat_{ab} = alpha_b * P_{pi(a),pi(b)}. Claimed: P_hat 1 = 1,
P_hat^2 = P_hat, delta unchanged, row geometry (vertices, W, H, g, sigma_tilde,
exposedness, hiddenness) unchanged as an l1-isometry on row differences; but
splitting a carrier component C into M equal fibers leaves it strongly connected
with bounded diameter while Pi_hat_C <= (1+delta)/M -> 0, violating
Pi_C >= c*tau - C'*L*delta for large M.

## AUDIT TASKS (derive-first; every check explicit)
1. ALGEBRA: re-derive P_hat^2 = P_hat, row sums, delta(P_hat) = delta(P).
2. GEOMETRY: the rows of P_hat live on a DIFFERENT column index set (split
   columns). Verify carefully that the campaign's functionals are invariant:
   the row points p_hat_a as measures, the l1 distances between rows, the
   exposing functional phi (does an exposing functional on the original lift to
   one on the split space with the same margins?), H, the deficit g (harmonicity
   g = P_hat g with the SAME values on fibers?), sigma_tilde_v, tau = sqrt(delta),
   hidden/visible status (multiplicity-correct def:vertex — coincident duplicate
   rows count once: do the clones coincide EXACTLY as points?). Any functional
   that changes voids the refutation — check each.
3. THE TARGET'S LETTER: conj:floor says "every carrier-graph component C of S_t
   that carries positive mass of v". Verify the cloned component still qualifies:
   clones are in S_t (g values preserved?), the fiber edges keep it strongly
   connected, its directed diameter L_hat is bounded independent of M (compute
   it: does a path between two clones of the same old node need extra steps?),
   and v's positive mass into it is preserved. Then verify Pi_hat_C <= (1+delta)/M
   — note the path product is min over pairs of MAX over paths of the edge
   product: could a clever path avoid small cloned edges? (Every edge INTO any
   clone of r is divided; but edges between non-cloned nodes are untouched —
   does the min over pairs i,j force passing through clones? Take i,j themselves
   clones of r.)
4. REPAIR CHECK: define the QUOTIENT carrier graph (merge exactly-coincident
   duplicate rows; aggregate edge mass: edge weight from class [i] to class [j]
   = sum over b in [j] of P_{i,b}). (a) Is the quotient floor immune to cloning
   (prove: aggregated weights are invariant)? (b) Does the PROVED w12 finisher
   tolerate the quotient — identical rows lump (stochastic lumpability); does
   the Birkhoff-Hilbert contraction + the radius bookkeeping commute with
   lumping duplicate rows? State precisely what must be re-proved vs inherited.
5. VACUITY ANGLE: the prover also says P(floor true as written) ~ 0.30 "mostly
   via possible vacuity of the high-hidden antecedent" — i.e. maybe NO instance
   has sigma_tilde_v > tau AND H > B*tau at all (then conj:floor is vacuously
   TRUE and the cloning instance must FIRST realize the antecedent — does it?
   The clone of a non-qualifying instance does not qualify either!). Resolve
   this cleanly: does the obstruction need an antecedent-realizing seed
   instance, and does one exist in the record (check the dossier/empirics:
   67k+ instances, none in the open regime)? If no seed exists, the cloning
   argument shows CONDITIONAL non-provability rather than falsity — say which.

## DELIVERABLE (verdict-first)
VERDICT: OBSTRUCTION REAL — FLOOR REFUTED AS WRITTEN (+ does the quotient repair
restore a well-posed target?) / OBSTRUCTION REAL BUT CONDITIONAL (needs a seed;
floor possibly vacuous — state the precise logical status) / OBSTRUCTION BROKEN
(the failing check, display math). Then: the corrected statement you recommend
the campaign adopt (LaTeX, ready to paste), and calibrated P(your verdict
survives further audit). Do not soften.
