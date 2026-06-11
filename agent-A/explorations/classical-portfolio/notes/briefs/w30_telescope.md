# w30_telescope: the displacement lemma via the iterated identity (route R1)

You are a codex (gpt-5.5) PROVER on the single named open statement of the
classical campaign: the representative displacement lemma, max-volume form.
A sibling worker (w30_maxvol) attacks via the max-volume structure; you attack
via TELESCOPING. Different routes — do not hedge toward generality.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w30_telescope.
PROGRESS PROTOCOL: short line per stage to progress.md.
ARTIFACT RULE: long-form proof to proof.md, NEVER answer.md.

## THE TARGET
P exactly idempotent, P1 = 1, row negative mass <= delta <= delta_0. u = a
MAX-VOLUME representative row (the max-volume basis of the audited L2 chart —
read notes/swarm-answers/w26_cluster_audit.md + experiments/out/
w26_cluster_audit/audit_report.md for the exact property). Prove
  T(u) := sum_j (P_{uj})_+ * ||p_j - p_u||_1 <= C_D * delta.
KNOWN (read notes/swarm-answers/w29_displacement.md + its proof note in
experiments/out/w29_displacement/proof.md):
- The general-row version is FALSE at delta = 0 (its counterexample tells you
  what max-volume must exclude — read it).
- The FREE IDENTITY: sum_j P_{uj}(p_j - p_u) = 0 exactly; the positive-part
  VECTOR sum has norm <= 2*delta*(1+2*delta).
- Numerics: T/delta in [0.5, 3.6] over all tested instances (median 2.04).
- The Markov handoff to the face estimate is already written (w29 §9).

## THE ROUTE (develop seriously, with all the audited tools)
1. f(j) := ||p_j - p_u||_1. At every row j, the row-reproduction identity
   p_j = sum_l P_{jl} p_l gives (derive carefully, with the negative-mass
   error explicit): f(j) <= sum_l (P_{jl})_+ f(l) + 2*nu_j*(1 + ...) — an
   "almost-subharmonicity". Conversely the exact vector identity at j bounds
   the cancellation. Set T = sum_j (P_{uj})_+ f(j) and expand once through
   each j: T <= sum_j (P_{uj})_+ sum_l (P_{jl})_+ f(l) + 2*delta*(...).
   The double sum is the TWO-STEP positive kernel from u — and exact
   idempotence says the two-step SIGNED kernel from u equals the one-step:
   sum_j P_{uj} P_{jl} = P_{ul}. Decompose the positive two-step kernel as
   P_{ul} + (cross terms involving negative parts) and derive a
   self-improvement inequality T <= T + small?? — find where a CONTRACTION
   factor a < 1 can come from: candidates: (i) the mass that returns to
   near-u rows contributes f ~ 0 (use in-class concentration, w27: class rows
   are eta-close to u); (ii) the max-volume property bounds how much positive
   mass can sit on rows with LARGE f (sibling's territory — import only the
   audited A = 1 coordinate bound); (iii) iterate m steps (P^m = P free) and
   let the class mass dominate. A clean outcome is an inequality
   T <= a*T + b*delta + c*eta*M where M = off-cluster mass, combined with the
   Markov relation M <= T/eta — solve the two-by-two system; check the
   resulting constants against the measured T/delta <= 3.6 and the
   eta = sqrt(delta) scales.
2. Verify every intermediate inequality numerically BEFORE relying on it
   (python3/numpy; reuse experiments/out/w29_displacement/displacement_audit.py
   conventions; instances: the w27 rank-2 saturator, split-block, certified
   w16/w17, random small-delta variety samples).
3. If the contraction fails: identify the EXACT leak (which term refuses to be
   < 1) and whether the sibling's max-volume input would plug it — state the
   minimal max-volume fact you need as a precise conjecture (that becomes the
   interface between the two routes).

## DELIVERABLE (verdict-first; long form to proof.md)
VERDICT: LEMMA PROVED (display math, explicit C_D, dimension-dependence
honest, numerics consistent) / DIED-AT (the exact leak + the minimal
max-volume interface fact needed). Calibrated P(survives audit). Save code +
outputs.
