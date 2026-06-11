# w16_barrier: prove the barrier inequality — hidden => sigma_tilde <= C0*sqrt(delta)

You are a codex (gpt-5.5) PROVER. The campaign has just collapsed to its leanest
form: prove that a hidden top vertex cannot have sigma_tilde above C0*sqrt(delta).
If true with ANY universal C0 (and a workable H side-condition), the proved belt
(s8 branch + height collapse + corner machinery) finishes the kernel conjecture.
The measured record says the constant to beat is 1.52 >= delta/sigma_tilde^2,
i.e. C0 ~ 0.81 empirically; ANY universal C0 suffices.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w16_barrier.
PROGRESS PROTOCOL: append one short line per stage to
/tmp/codex-sigma-wall/w16_barrier/progress.md.

## READ FIRST (the order matters)
1. agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex — ALL
   definitions + the constraints ledger §5 (what any proof must respect; dead
   routes — do not rewalk them).
2. notes/swarm-answers/ (same exploration dir): w15_prover.md (the cloning
   obstruction — your proof must be CLONE-INVARIANT: sigma_tilde, hiddenness,
   delta all are, so the target itself is safe; but any intermediate path-product/
   atom-level quantity is NOT — use only clone-invariant quantities: masses,
   distances, functionals, quotient objects), w15_refuter.md (the measured
   obstruction per template: what stops sigma_tilde from crossing — hiddenness
   margin vs negative-mass budget), w15_sos.md (chain-local scalar certificates
   are DEAD: you MUST consume the hiddenness LP frame), w15_audit.md (the
   verified moduli: dist(p_i, conv{p_j: P_ij>0}) <= (2+4delta)*nu_i; the
   small-invisible-mass branch dist(p_v, C_W) <= 2(1+2delta)*max(sigma_tilde_v,
   nu_v)), w15_periodic.md + w15_periodic_audit.md (closed components are
   automatically aperiodic; finisher attachment needs closure + radius < r*).
3. notes/wave5-sigma-wall-parallel.md FINAL sections (the corner theorem:
   tau* = 2-sqrt(3), wall H/tau <= 2(2-sqrt(3)); the sigma-tilde height-collapse
   lemma: sigma_tilde <= s => H <= delta*Omega/(1-s); the s8 branch; t10/w12
   finishers; wave-10 meta-theorem "hiddenness IS the LP frame").

## TARGET
Exists universal delta_0, C0 (and if needed B): for every exactly idempotent
P (P^2 = P, P1 = 1) with row negative mass <= delta <= delta_0, every HIDDEN
top vertex v (multiplicity-correct convention) satisfies
  sigma_tilde_v <= C0 * sqrt(delta).
(If you need the height side-condition H > B*tau, prove the statement in the
form "hidden + H > B*tau => contradiction" — the H <= B*tau branch is already
covered by the proved belt; SAY explicitly which branch split you use.)

## METHOD HINTS (new ingredients this wave)
- Work CLONE-INVARIANTLY: quotient by coincident rows up front (identical rows
  carry identical deficits g and identical functional values).
- The hiddenness LP frame: v hidden means NO exposing functional separates p_v;
  dualize — hiddenness gives a convex combination of other rows representing
  p_v's exposure deficit. Combine with the audited row-reproduction modulus and
  the height-collapse lemma to force either sigma_tilde small or an exposure
  certificate (contradiction).
- The H-M surrogate carrier-mass bound (derived in w15_prover.md):
  sigma_tilde_v > tau and H > B*tau put mass >= (B/3-4)*tau into the shallow
  band off C_W. The w12 finisher (periodicity now free) exposes any CLOSED
  component with collapse radius < r* = 0.85*tau. The survivor class is thin
  components — but at the QUOTIENT level, thinness is constrained: a quotient
  class aggregates its fiber mass. Try: total shallow off-C_W mass
  >= (B/3-4)*tau must distribute over quotient components; bound the number of
  geometrically distinct shallow classes (the corner/near-coincidence machinery
  bounds how many distinct near-vertex directions fit) and force one class to
  carry mass >= some c*tau — then the aggregated (quotient) two-step mass
  P^2 = P returns it with a floor? Derive honestly; if the count of distinct
  classes cannot be bounded dimension-free, SAY SO — that is the died-at.
- Numerics allowed (python3/numpy in your workdir) to sanity-test intermediate
  inequalities before proving them.

## DELIVERABLE (verdict-first)
VERDICT: PROVED (full proof, display math, explicit universal constants, the
branch split stated) / PARTIAL (exactly what is proved + the gap) / DIED-AT
(the exact failed inequality in display math; why each natural repair fails;
whether the failure suggests a counterexample template for the numerical
decider). Calibrated P(barrier true), P(this route closes with more work).
