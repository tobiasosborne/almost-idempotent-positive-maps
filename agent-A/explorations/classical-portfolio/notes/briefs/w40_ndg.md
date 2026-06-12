# w40_ndg: cross-verify the (P1)/(SB*) repair, then close the near-degenerate horn (NDG)

You are a codex (gpt-5.5) VERIFIER + PROVER. The campaign's reduction was
refuted (your w38 predecessor's catch), then repaired by the opus family
(w39). Two jobs: (A) cross-verify the repair (2-family bar), (B) attack the
single residual display of the multi-row swap dichotomy — the near-degenerate
horn (NDG).

Repo root: /home/tobias/Projects/almost-idempotent-positive-maps (main).
Workdir (writable): /tmp/codex-sigma-wall/w40_ndg.
PROGRESS PROTOCOL: one short line per stage to progress.md.
ARTIFACT RULE: long form to proof.md, NEVER answer.md. sympy/HiGHS; gurobi
broken in sandbox.

## READ (under agent-A/explorations/classical-portfolio/)
1. notes/swarm-answers/w39_opus_repair.md + experiments/out/w39_opus_repair/
   (proof.md + scripts): (P1) E_s <= sigma_s + 2(-lambda_s)_+; S* := S+ + 2V;
   (SB*): U* in argmin_{theta=1/2} Phi => S*_s <= 3 delta; V = 0 at every
   tested argmin; the (DEF)-coupling argument that overshoot is not free.
2. notes/swarm-answers/w38_sb.md (the refutation this repairs), w37_opus.md
   (what stands: (R), (DEF), irreducibility), w36_audit.md (B6 theta=1/2),
   notes/briefs/w38_sb.md items B1-B2 (the multi-row swap dichotomy).
3. Reusable exact auditors: experiments/out/w37_opus/, w38_sb/, w36_charge/.

## PART A — VERIFY THE REPAIR (honest, line by line)
A1. (P1) as a pointwise inequality: prove it by hand from the definitions
    (case split on the sign of lambda); then re-verify numerically on the six
    families INDEPENDENTLY of the opus scripts.
A2. The "V = 0 at every tested argmin" claim: re-verify, and answer the
    question opus did not: is V = 0 at the argmin PROVABLE (does the
    selection always prefer charts without overshoot rows — e.g. because an
    overshoot row is itself swap-eligible at volume factor a_s > 1 > 1/2,
    so swapping it IN increases volume and is always permitted)? If yes,
    PROVE IT — then (SB*) collapses to (SB) at the argmin and the overshoot
    discussion ends. This looks plausibly EASY and high-value: an a_s(j) > 1
    row swapped into the basis at pivot s multiplies the volume by a_s > 1,
    so U* (within the theta = 1/2 class, anchored at Vol >= Vol_max/2)...
    careful: increasing volume never exits the class; minimality of Phi is
    the constraint, not volume. Work out what the swap does to Phi.
A3. The (DEF)-coupling no-free-overshoot argument: confirm or refute.

## PART B — THE NEAR-DEGENERATE HORN (NDG)
Setting: U in the theta = 1/2 class; s fixed; J = the set of rows carrying
the S*_s excess (positive beta_s mass, positive sigma_s + overshoot). The
dichotomy: EITHER some subset J' of J can be swapped into the basis keeping
Vol >= (1/2) Vol_max (then argmin-minimality versus that basis must be shown
to reduce S*_s — the volume-permitted horn), OR every such swap collapses the
volume — meaning the transverse coefficient block of J is near-degenerate.
(NDG): in the near-degenerate case, prove the carried excess is O(delta)
DIRECTLY. Intuition to make precise: near-dependent coefficient vectors with
positive beta_s weights and signed transverse parts force cancellations that
the row-negativity budget must pay for — the excess of a near-dependent
family lives in a lower-dimensional face where the (DEF)/sum-rule identities
close. Work rank 2 EXHAUSTIVELY first (k = 2, all configurations — this is a
planar problem; solve it completely, exact), then rank 3, then the general
pattern. If rank 2 already resists, say exactly why — that failure would
itself be decisive intelligence.
ALSO: the volume-permitted horn is NOT yet a theorem either (minimality gives
Phi(U*) <= Phi(V); you must compute Phi(V) after a multi-row swap — derive
the block/Schur multi-row generalization of the shear formula and bound the
sheared excess). If you can only close ONE horn, close rank 2 ENTIRELY (both
horns at k = 2) — a complete rank-2 theorem with explicit C would be the
first unconditional instance of the selected-chart bound and the template.

## MANDATORY EXACT CHECKS
The six families (transverse pair a=1/4, dense pair k=7, staircase m=2,3,
perturbed staircase m=5 eps=1/1000, no-center path k=6,8) for Part A; for
Part B rank-2: random + adversarial exact rank-2 instances (your own
generator; idempotents via the LB/BL=I converse).

## DELIVERABLE (verdict-first; long form to proof.md)
VERDICT per part: A = REPAIR CONFIRMED (+ V=0-at-argmin PROVED?) / REFUTED-
AT-<step>; B = NDG PROVED / RANK-2 THEOREM (both horns, explicit C) /
PARTIAL (exact missing display) / DIED-AT. Calibrated P's. Save everything.
