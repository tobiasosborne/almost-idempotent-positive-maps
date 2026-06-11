# w18_semigroup: P^k = P for ALL k — semigroup, duality, and two-sided structure

You are a codex (gpt-5.5) RESEARCH worker in a 5-worker round whose shared
charge is: exploit the exact quadratic constraint P^2 = P to its fullest. Your
lens: the constraint is not one equation — it generates the FULL multiplicative
semigroup structure (P^k = P for all k >= 1), a two-sided (row AND column)
rigidity, and exact spectral data (spec(P) = {0,1}, P = its own Riesz
projection). The campaign has been almost entirely ROW-geometric; find what the
unused halves buy.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps (read-only).

## CONTEXT (read first)
1. agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex — the
   problem + §5 ledger (dead ends: LP-frame collapse + pushed-witness;
   clone-invariance mandatory; no chain-local certificates; anti-splitting
   died-at; the certified sigma-crossing at tiny height). Target: the LINEAR
   LAW delta >= c*H.
2. The dossier wave-10 table (notes/wave5-sigma-wall-parallel.md): t2
   probabilistic died at "signed coupling defect uncontrolled"; t6 discharging
   died at "conservation g = Pg yields no forbidden local configuration"; t7
   Lyapunov died. Your angles must differ from those death points — read them.
3. notes/swarm-answers/w14_autopsy.md — the sign-rigid vs sign-robust table of
   the delta=0 proof (your semigroup arguments must respect it).

## RESEARCH ANGLES (develop each; rank at the end)
1. TWO-SIDEDNESS: columns. P^T is idempotent too (not stochastic). The column
   space structure: left fixed vectors (invariant measures!) pi P = pi. The
   campaign's deficit g satisfies P g = g (right); what do LEFT fixed vectors
   give? At delta = 0 the left-fixed cone is spanned by the recurrent-class
   distributions pi_s — EXACTLY the visible vertices' rows. For signed P: the
   left fixed space has the same dimension k (exact!). Develop: a signed
   left-fixed vector basis -> candidate "recurrent classes" WITHOUT positivity;
   pair left and right structure (the k-dim left-fixed space vs the rows'
   affine geometry: rows p_i live in... derive: p_i = e_i^T P, and
   P = sum_s (right vectors)(left vectors)^T spectral form — rows are
   combinations of the k left-fixed vectors with coefficients from the right
   eigenstructure: THE ROWS LIVE IN A k-DIM AFFINE SPAN with coordinates given
   by the right 1-eigenspace! Exploit: H and dist(p_v, conv W) measured INSIDE
   this exact k-dim coordinate system — does hiddenness become a k-dimensional
   (n-free!) statement? This smells like the dimension-free reduction the
   anti-splitting step needs. Make it precise.).
2. TRACE + RANK: tr P = k exactly, an INTEGER. Trace is clone-invariant and
   basis-free. Negative diagonal entries are paid for by positive ones summing
   to an integer. Sign-pattern + trace identities for powers (tr P = tr P^2 =
   sum_{ij} P_ij P_ji): derive trace-based inequalities linking delta, the
   diagonal, and off-diagonal cancellation structure. (The dead positive-
   diagonal step of the delta=0 proof — w14 autopsy — may have a TRACE-
   AGGREGATED sign-robust replacement: per-component trace >= 1 - O(delta)?)
3. SIGNED ERGODIC/PATH CALCULUS: P^k = P means signed path sums of EVERY
   length agree exactly. The t2 death was an uncontrolled coupling defect for
   ONE step; with all k available, design telescoping/averaging identities
   where cancellations must conspire across all lengths simultaneously —
   derive at least one new exact identity the record does not have, and test
   what it forces on the certified instance's numbers (read them from
   notes/swarm-answers/w16_cert_audit.md — n=7, k=4, delta=0.228,
   sigma/tau=1.63, H/tau=0.016).
4. FUNCTIONAL CALCULUS / RESOLVENT: (zI - P)^{-1} = (z-1)^{-1} P +
   z^{-1}(I - P) EXACTLY — every resolvent bound is free. What perturbation /
   subspace-rotation statements (Davis-Kahan-style, but non-self-adjoint)
   follow for the pair (range P, ker P) vs a candidate nonneg idempotent's
   pair? Could the linear law be a SUBSPACE-ANGLE statement?
5. Anything further your lens generates — surprise us.

## DELIVERABLE (verdict-first)
TOP 3 ranked attack plans (first lemma in display math; dead-end-evasion check
incl. clone-invariance; what each buys), then the supporting derivations (hand
derivations — you cannot run code; arithmetic on the certified instance's
published numbers is fine), then UNVERIFIED-LEAD list (precise statements +
sources for acquisition), then calibrated P per plan and overall.
