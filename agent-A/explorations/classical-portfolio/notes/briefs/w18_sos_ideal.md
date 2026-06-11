# w18_sos_ideal: SOS / Positivstellensatz MODULO THE IDEAL of the idempotent variety

You are a codex (gpt-5.5) RESEARCH+COMPUTE worker in a 5-worker round whose
shared charge is: exploit the exact quadratic constraint P^2 = P to its fullest.
Your lens: polynomial optimization ON THE VARIETY — SOS modulo the ideal
I = <P^2 - P, P*1 - 1>, NOT scalar shadows and NOT stratum-by-stratum modules.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w18_sos_ideal.
PROGRESS PROTOCOL: append one short line per stage to
/tmp/codex-sigma-wall/w18_sos_ideal/progress.md.

## CONTEXT — what is ALREADY DEAD (do not repeat)
1. report/kernel-conjecture.tex (under agent-A/explorations/classical-portfolio/)
   — definitions + §5 ledger. The REAL target per the dossier: the LINEAR LAW
   delta >= c*H over exact signed stochastic idempotents.
2. notes/swarm-answers/ + the dossier (notes/wave5-sigma-wall-parallel.md):
   - t5 (wave-10 SOS) COLLAPSED: "quadratic module lacks any generator beyond
     C10-exchange on each stratum" — it worked on hiddenness STRATA, hit the
     LP-frame meta-finding. Read its answer in notes/swarm-answers/ if present.
   - w15_sos: the chain-local SCALAR shadow is FALSE (exact witnesses) — no
     proof can be chain-local.
   Your task is the formulation BOTH missed: global, matrix-level, with the
   FULL ideal of the variety in the quadratic module — idempotence supplies
   infinitely many polynomial identities (P^k = P; all minors' relations; trace
   identities tr P = k; the characteristic polynomial factors) that the dead
   attempts never injected.
3. The certified crossing instance (experiments/out/w16_cert_audit/
   w16_best_rational_instance.json): any candidate inequality MUST hold on it
   (hidden, sigma/tau = 1.63, H/tau = 0.016, delta = 0.228) — a cheap kill test.

## TASKS
1. FORMULATE the linear law as polynomial optimization on the real variety
   V = {P in R^{nxn} : P^2 = P, P1 = 1}: minimize delta - c*H ... but H and
   hiddenness are LP-defined (max-min) — handle via lifting (introduce the
   exposing functional variables and the witness weights as new variables with
   their KKT/complementarity polynomials — complementarity is ALSO quadratic!).
   Write the exact lifted polynomial system. The hiddenness complementarity
   conditions become part of the variety — this dodges the "hiddenness stratum"
   collapse by making the LP structure itself polynomial. Check: is the lifted
   formulation clone-invariant (does cloning lift)? Note where multiplicity-
   correctness enters and how to encode "distinct rows" semi-algebraically
   (products of ||p_i - p_j||^2 > 0 — or work on the quotient by clustering).
2. THEORY: what does idempotence buy in the quotient ring R[P]/I? Derive a
   GROEBNER-flavoured normal form for small (n,k): which monomials survive?
   (P's entries satisfy: every entry of P^2 - P = 0 — n^2 quadrics; the variety
   is smooth of known dimension — from w18_variety's lens — so the ideal is
   real radical: Positivstellensatz degrees may be LOW. State the expected
   degree bounds honestly as UNVERIFIED-LEAD where from memory.)
3. COMPUTE (python3, numpy/scipy/fractions; sympy IF installed — check; no
   network): for n = 3, k = 2 (the smallest case with hidden geometry?
   determine the smallest n,k where a hidden vertex can exist — check the
   record/instances): set up the degree-2 and degree-4 SOS-modulo-ideal LP/SDP
   for delta >= c*H restricted to V (eliminate variables via the corner
   parametrization from the variety structure: P = L B, B L = I_k reduces to a
   POLYNOMIAL map — the SOS then lives on (L,B)-space with the I_k relations!).
   Hand-roll a small SDP via scipy (or reduce to LP on a monomial sample +
   rational rounding as in w15_sos). Report feasibility/certificates per (n,k).
4. If a certificate appears at any small (n,k): rational-round and verify
   EXACTLY; if not: extract the dual witness and its geometric reading.

## DELIVERABLE (verdict-first)
VERDICT per attempted (n,k): CERTIFICATE / NO CERTIFICATE AT DEGREE d (dual
witness reading) / FORMULATION OBSTRUCTION (exactly what breaks). Then the
lifted polynomial formulation (display math), the theory write-up, UNVERIFIED-
LEAD list (precise statements + acquisition targets), and calibrated
P(SOS-on-the-variety can prove the linear law at fixed small n),
P(it can give the n-uniform statement). Save all code + outputs.
