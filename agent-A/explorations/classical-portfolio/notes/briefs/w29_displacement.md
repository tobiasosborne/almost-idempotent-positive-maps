# w29_displacement: the representative displacement lemma — the bridge's last reduction

You are a codex (gpt-5.5) PROVER with numerics. The campaign's route to the
GLOBAL theorem now reduces to ONE clean lemma about a single row of an exact
idempotent. Prove it or find the conspiring family.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps.
Workdir (writable): /tmp/codex-sigma-wall/w29_displacement.
PROGRESS PROTOCOL: short line per stage to progress.md.
ARTIFACT RULE: long-form proof to proof.md, NEVER answer.md.

## THE LEMMA (the target)
P exactly idempotent, P1 = 1, row negative mass <= delta <= delta_0. For a row
u (in application: a max-volume cluster representative, but state the lemma
for general u if it holds generally):
  sum_j (P_{uj})_+ * ||p_j - p_u||_1  <=  C_D * delta,
with C_D universal (dimension-free). I.e. the transport cost of u's positive
successor mass is O(delta).

## THE FREE IDENTITY (start here — orchestrator-derived, verify it first)
Idempotence gives sum_j P_{uj} p_j = (P^2)_{u.} = p_u, and row sums give
sum_j P_{uj} = 1; hence the SIGNED displacement sum vanishes EXACTLY:
  sum_j P_{uj} (p_j - p_u) = 0,
so  || sum_j (P_{uj})_+ (p_j - p_u) ||_1 = || sum_j (P_{uj})_- (p_j - p_u) ||_1
    <= nu_u * max_j ||p_j - p_u||_1 <= delta * (2 + 4*delta).
The VECTOR version is therefore free at O(delta). The lemma is the SCALAR
(no-cancellation) version: positive mass cannot sit at large displacement in
mutually-cancelling directions beyond O(delta) total transport. Your job is to
exclude the conspiracy.

## ATTACK ROUTES (try in this order; combine freely)
R1. ITERATED/LOCALIZED IDENTITY: the same identity holds AT EVERY ROW j
    (p_j's own positive successors). Set f(j) = ||p_j - p_u||_1. From
    p_j = sum_l P_{jl} p_l: f satisfies an exact "harmonicity-like" relation
    with O(nu_j * diam) signed error. The quantity T = sum_j (P_{uj})_+ f(j)
    is then constrained by a one-step expansion: expand f(j) through j's own
    successors, use P^2 = P at u (the two-step positive mass through
    intermediate rows returns to u's distribution exactly), and look for a
    telescoping/self-improvement inequality T <= a*T + b*delta with a < 1.
R2. FUNCTIONAL SPLIT: f(j) = ||p_j - p_u||_1 = sup over sign-vectors phi of
    <phi, p_j - p_u>. For FIXED phi, sum_j (P_{uj})_+ <phi, p_j - p_u> <=
    2*delta*(1+2delta) by the free identity. The scalar sum is the sup INSIDE
    the sum; the gap is the phi-variation across j. Group rows by their
    optimal phi (epsilon-net of directions is n-dependent — avoid; instead
    use the structure: p_j - p_u directions live in the k-dim row space with
    A = 1 coordinates (the audited L2 chart, w26_cluster_audit) — a k-dim
    net?! k enters logarithmically or linearly? — check whether the L2
    coordinates make the sup effectively low-dimensional and whether
    dimension-freeness survives; if you get C_D(k), say so honestly).
R3. SECOND-MOMENT / CAUCHY-SCHWARZ with the exact two-step identity:
    sum_j (P_{uj})_+ f(j)^2 vs (sum (P_{uj})_+ f(j))^2 — the rank-2 saturator
    has mass sqrt(delta) at displacement sqrt(delta): first moment delta,
    second moment delta^{3/2} — measure both numerically to guess the true
    extremal profile, then prove the matching inequality.
R4. If all fail: search for a CONSPIRING family — positive mass m at
    displacement d in cancelling directions with m*d >> delta while
    m*(vector sum) stays <= 2*delta; the constraint is that the cancelling
    directions must themselves be realized by rows of an EXACT idempotent
    with small negative mass — build it with the P = L*B, B*L = I machinery
    (experiments/out/ has many generators). A genuine counterexample
    re-routes the campaign: report loudly.

## VERIFY on: the w27 rank-2 saturating family (scalar sum = delta exactly —
your C_D must accommodate it), the split-block family, the certified w16/w17
instances, random small-delta variety samples. Code + measured C_D
distribution in your workdir. If the lemma lands: hand the result to the w28
Markov step explicitly (one paragraph: the face estimate follows with
C = C_D), and state the resulting conditional chain status; do NOT assemble
the global theorem yourself (the next worker audits first).

## DELIVERABLE (verdict-first; long form to proof.md)
VERDICT: LEMMA PROVED (display math, explicit C_D, dimension-dependence
honest) / DIED-AT (the exact failed step per route R1-R3) / COUNTEREXAMPLE
(the family + verified numbers). Calibrated P(survives audit). Save code +
outputs.
