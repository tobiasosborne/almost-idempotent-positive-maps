# op-exposed-hull attack plan

Date: 2026-06-07.  Author: Agent B.  Status: exploration plan, not a
canonical proof shard.

This plan is the durable orchestration map for the classical route to
`op-exposed-hull`.  It lives in the Agent B lane.  Nothing here upgrades the
registry status; proposed theorem names are candidate contracts for later
Agent A review and `af` work only.

## Restart protocol

Read in this order after compaction:

1. `PRD.md`, `CLAUDE.md`, `HANDOFF.md`.
2. `docs/plans/2026-06-07-agent-b-rules-of-engagement.md`.
3. `argument/lemmas/op-exposed-hull.md`.
4. `agent-B/notes/op-exposed-hull-mission-control.md`.
5. The subagent notes listed in the mission-control roster.
6. Latest outputs under `agent-B/experiments/op-exposed-hull/outputs/`.

Keep all new work in `agent-B/**`, dated `docs/plans/**`, or
`docs/worklog.md`.  Canonical layers are entered only later through Recipe A
and Recipe B with reviewer-not-author discipline.

## Target normalization

Assume an exact signed affine retraction

```text
P1=1,        P^2=P,        neg(p_i)<=delta,        tau=sqrt(delta).
```

Rows are `p_i`; `K=conv{p_i}`.  For constants `R,k,A`, set

```text
rho=R tau,        kappa=k tau,
W=W_{rho,kappa}={row vertices v : e_v(rho)>=kappa}.
```

Goal:

```text
dist_1(p_i, conv W) <= A tau
```

for every row, with universal constants after choosing `R` large, `k` small,
and `A` large enough.  Hume shows the square-root scale is sharp, but all
current tests say Hume is not an exposed-hull obstruction.

## Main proof architecture

The strongest current stack is:

```text
maximal exposed skeleton
  -> positive-coordinate Markov kernel from P^2=P
  -> bad-kernel resolvent certificate
  -> long-lifetime closed-bad-class alternative
  -> LP/circuit augmentation contradiction
  -> op-exposed-hull capstone.
```

Pure convex geometry is explicitly insufficient; dense polygon warnings can
cycle.  The proof must use both exact idempotency and the row negative-mass
bound.

## Work package 1: positive-coordinate repair

Define

```text
a_i=neg(p_i),        q_i=p_i^+/(1+a_i).
```

Then `q_i` is a probability vector.  From `p_iP=p_i`,

```text
||p_i - sum_j q_i(j)p_j||_1 <= C delta.        (PC)
```

Candidate formal contract:

```text
lem-positive-coordinate-repair:
For a signed affine retraction with row negative mass <=delta, every row is
C delta-close in l1 to the convex combination of rows selected by its repaired
positive coordinate distribution q_i.
```

Status: essentially ready; constants need one clean write-up.  This should be
the first small `af` lemma once Agent A agrees.

## Work package 2: resolvent certificate

Let `R0` be a maximal `4rho`-separated subset of `W`, and let
`C_R=conv(R0)`.  For a bad index set `B`, let `G=B^c` and
`T=(q_i(j))_{i,j in B}`.

If every row in `G` is `Gamma`-close to `C_R` and

```text
||(I-T)^(-1)||_{infty->infty} <= L,
```

then every row in `B` is

```text
Gamma + 4 L delta
```

close to `C_R`.  Hence `L=O(1/tau)` closes the bad set at the target scale.

Candidate formal contract:

```text
lem-bad-kernel-resolvent:
Under (PC), a substochastic bad-to-bad block with fundamental matrix norm L
gives distance-to-hull bound Gamma+4 L delta for all bad rows.
```

Status: ready modulo constants.  The proof is a one-page vector inequality.
Subagent I has written the proof-ready version in
`agent-B/notes/subagent-op-exposed-hull-bad-kernel.md`.

## Work package 3: long lifetime extraction

If the resolvent bound fails, extract a nearly closed bad class.  Target:

```text
||(I-T)^(-1)||_{infty->infty} > B/tau
  => exists probability mu on B with mu q(B^c) <= C tau
```

or a subset `B'` with rowwise exit `<=C tau` after pruning.

Candidate formal contract:

```text
lem-long-bad-lifetime:
A substochastic repaired-coordinate block with expected lifetime >B/tau
contains a quasi-closed bad distribution or bad communicating class with
exit O(tau).
```

Status: likely standard finite Markov-chain algebra, but must be written
without citing ungrounded folklore.  It is a good self-contained proof target.

## Work package 4: closed-bad-class augmentation

This is the central hard lemma.

```text
lem-closed-bad-class-augmentation:
Let B be a row-vertex set farther than A tau from conv(R0), enlarged by
rho-clusters, and suppose B is O(tau)-closed under q.  If R0 is a maximal
4rho-separated subset of W, then B contains a row vertex w with
e_w(rho)>=kappa and dist_1(w,conv(R0))>4rho.
```

If true, maximality is contradicted.  If false, this should produce an actual
counterexample to `op-exposed-hull`.

The planned proof has four subclaims:

```text
4a. Separator plateau:
    a bad class far from conv(R0) has a high affine plateau separated from R0.

4b. Failed-exposedness circuit:
    every non-well-exposed vertex in the plateau yields the LP-dual circuit
    from subagent-op-exposed-hull-lp-dual.md.

4c. Circuit aggregation:
    quasi-closedness under q eliminates local circuits into one normalized
    rho-separated bad circuit.

4d. Negative-mass lower bound:
    a rho-separated bad circuit in an exact signed retraction forces
    max_i neg(p_i) >= c rho^2.
```

With `rho=R tau`, choose `R` so `cR^2 delta > delta`, contradiction.

Status: open.  This is where most subagent effort is now focused.

## Work package 5: LP/game certificate mining

Build the finite joint system corresponding to the negation of Work Package 4:

```text
P1=1, P^2=P, neg rows<=delta,
B is O(tau)-closed under q,
all B vertices fail e_v(R tau)>=k tau,
B is far from conv(R0).
```

For small `n`, search feasibility and extract dual certificates.  If feasible,
rationalize the instance and save it as a counterexample candidate.  If
infeasible, simplify the dual into the circuit aggregation proof.

Primary tooling:

```text
SciPy/HiGHS for LPs,
gurobi_cl for exported LP/MILP checks,
SymPy for rationalization.
```

Blocked tooling: `gurobipy`, `cvxpy`, `ortools`; `wolframscript` binary is
present but the kernel is not activated.

## Work package 6: small-case closure

Already benign:

```text
rank <= 2, all exact n=3, simplex row polytopes,
one explicit n=4 corank-one quadrilateral family.
```

Remaining target:

```text
arbitrary n=4, rank 3, corank-one 2|2 affine-circuit quadrilateral.
```

Candidate contract:

```text
lem-n4-circuit-exposed-or-collapsed:
For P=I-u v^T with sum v_i=0, v^T u=1, v sign split 2|2, and
neg rows<=delta, either the quadrilateral row polytope is O(sqrt(delta))-close
to a simplex/segment hull or all four vertices are c sqrt(delta)-exposed at
scale C sqrt(delta).
```

Status: coefficient-level dichotomy closed in
`agent-B/notes/subagent-op-exposed-hull-n4-circuit.md`.  In a positive
`2|2` circuit `a p_0+b p_1=c p_2+d p_3`, the affine value assignments expose
the four vertices at levels `b,a,d,c`; if one coefficient is below `k tau`,
the controlled vertex is within `O(k tau)` of the opposite edge.  This is now
best treated as a sanity-check lemma and a model for the general circuit
aggregation step, not as a blocker.

## Work package 7: robust-coordinate secondary route

Push canonical row coordinates through a probability kernel to representatives:

```text
lambda_a(x)=sum_j x_j mu_a(j).
```

This preserves coefficient negative mass:

```text
neg(lambda(p_i)) <= neg(p_i) <= delta.
```

The obstruction is representative interpolation:

```text
G_ba=lambda_a(r^b)=I+O(tau),
```

and exactifying by `G^{-1}` may create `O(tau)` coefficient negativity.

Hard target:

```text
construct mu with G=I+O(delta) and row reconstruction O(tau),
or prove this coordinate route cannot close.
```

Status: secondary, active subagent task.  Demote if it produces a real
Theta(tau) interpolation obstruction independent of exposed-hull truth.

## Work package 8: direct nonlinear search

Similarity-conjugated stochastic idempotents did not find threats.  Extend
search to exact retractions parameterized by

```text
P=A B,        B A=I,        P1=1,
```

with penalties for row negative mass and exposed-hull violation.  The goal is
not proof by numerics; it is to discover either a counterexample family or a
dual certificate shape for Work Package 4.

Status: completed as a first direct-search pass in
`agent-B/notes/subagent-op-exposed-hull-direct-search.md`.  No counterexample
was found.  Broad grids only misbehave for aggressive constants such as
`rho=0.5 tau`, `kappa=0.5 tau`; conservative grids have benign finite ratios
and no empty-`W` reports.  The next computational pass should stop ranking raw
exposed-hull distance and instead score samples by repaired-coordinate
bad-kernel lifetime / quasi-closed bad class quality.

## Work package 9: literature and refs

Current web-scout leads, not canonical until acquired into local `refs/`:

```text
Blackwell 1942 idempotent Markoff chains;
Schwarz 1964 stochastic matrix semigroups;
Gonzalez-Hartfiel 1991 stochastic idempotent matrix space;
Gonzalez-Torres 2017 cores of idempotent stochastic matrices;
Hoffman 1952 linear-inequality error bounds;
Choquet-Corson-Klee 1966 exposed points;
Agaev-Chebotarev 2011 regularized stochastic power limits;
Awerbuch-Kleinberg barycentric spanners.
```

The current verdict is negative: no located theorem directly gives the
dimension-free signed-retraction exposed-hull stability.  These sources are
background and language, not a replacement for Work Package 4.

## Secondary certificate route

The robust-coordinate route remains active with a sharpened LP target:

```text
construct one stochastic kernel U with
  ||p_i - sum_a U_{i,a}r^a||_1 <= C tau,
  max_b sum_a |sum_j r^b_j U_{j,a}-delta_{ba}| <= C delta.
```

If this holds, pushing canonical coordinates through `U` preserves coefficient
negative mass `<=delta`, and exactifying the representative interpolation
matrix only adds `O(delta)` negativity.  Subagent J found that cluster
assignment alone really can lose `O(tau)`, but optimized LP kernels achieve
`O(delta)` interpolation defect on Hume, the exact quadrilateral family, and
small-defect exact similarity projections.

This route is not the primary proof architecture, but it is a useful dual
certificate extractor.  Its Farkas dual should be compared with the
closed-bad-class augmentation lemma.

## Active delegation ledger

Completed and integrated:

```text
A: LP-dual attack -> exact failed-exposedness circuit; alpha-mass blocker.
B: maximal skeleton -> resolvent/closed-bad-class dichotomy.
C: robust coordinates -> interpolation upgrade blocker.
D: computational search -> no small-delta counterexample; reusable LP package.
E: small cases -> rank<=2/n=3/simplex/one n=4 family benign.
F: stress tests -> Hume products, dense polygons, similarities not threats.
G: deeper literature -> no direct theorem; refs acquisition targets listed.
H: frameworks -> confirms Markov-resolvent + LP/game/circuit stack.
I: bad-kernel -> proof-ready resolvent bound; closed class still open.
J: interpolation -> naive exactification blocked; optimized LP target active.
K: n=4 circuit -> coefficient dichotomy closes small-case gap.
L: LP/game -> frozen diagnostic built; no small-defect negation found.
M: direct P=A B search -> no counterexample; next score bad-kernel lifetime.
```

Next follow-ups:

```text
N: repaired-coordinate bad-kernel lifetime scoring on direct A,B samples.
O: Farkas dual of the interpolation-upgrade LP.
P: no-cycle/high-face lemma for quasi-closed bad classes.
```

Every worker must report:

```text
Verdict; Artifacts; Constants; Failure modes; Next handoff.
```

## Landing criteria

The route is ready for Agent A only when:

```text
1. Work Packages 1-4 have complete pencil proofs with explicit constants, or
   a counterexample is found.
2. Numerics have failed to refute the constants on known stress families.
3. Candidate contracts are split into <=12-node af-sized lemmas.
4. Every external literature fact needed canonically has a local refs plan.
5. The final capstone reduces op-exposed-hull to validated/ready sublemmas,
   without touching canonical files directly from the Agent B lane.
```

Until then, `op-exposed-hull` remains open.
