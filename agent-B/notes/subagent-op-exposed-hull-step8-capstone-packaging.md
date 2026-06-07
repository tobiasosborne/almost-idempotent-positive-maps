# Subagent Step 8: Closed-Bad-Class Capstone Packaging

Date: 2026-06-07.  Lane: Agent B sandbox.  Status: packaging note, not a
canonical proof shard.

## Scope

This note packages the closed-bad-class/high-face block for `op-exposed-hull`
into candidate `af`-sized contracts and a dependency DAG.  It does not claim
that the proof is complete.  The capstone remains blocked on the Step 4
interface, the Step 6 alpha/calibration problem, and Step 7.

Target normalization:

```text
P1=1,        P^2=P,        neg(p_i)<=delta,        tau=sqrt(delta),
q_i=p_i^+/(1+neg(p_i)),   rho=R tau,              kappa=k tau.
```

Let `R0` be a maximal `4rho`-separated subset of
`W_{rho,kappa}` and put `C=conv(R0)`.  A bad row means a row farther than a
chosen threshold `D tau` from `C`, with the usual `rho`-cluster enlargement
when vertex language is needed.

## Verdict

The capstone can be decomposed cleanly, but it is not ready for Agent A as a
closed proof.  The ready pieces are small and classical:

```text
positive-coordinate repair,
bad-kernel resolvent,
finite Markov lifetime extraction,
high-slice drift,
top-face exposure,
shadow edge,
finite shadow recurrence,
failed-exposedness Farkas circuit.
```

The load-bearing open pieces are:

```text
shadow-exit/interface lemma,
alpha-budget or calibrated-dual aggregation lemma,
separated-circuit negative-mass lower bound.
```

If these three are proved with constants at the stated scale, the
closed-bad-class augmentation lemma follows by a short contradiction
argument, and the global `op-exposed-hull` result follows from the existing
resolvent alternative and maximality of `R0`.

## Status Legend

```text
ready:     proof idea is local and ready for Agent A review/formal packaging.
conditional: proof-ready once its named hypothesis is supplied.
open:      plausible target, no complete proof yet.
blocked:   depends on at least one open target.
```

## Candidate Contracts

### C0. Positive-coordinate repair

Status: ready.

```text
lem-positive-coordinate-repair:
For a signed affine retraction with row negative mass <=delta, the repaired
probability rows q_i=p_i^+/(1+neg(p_i)) satisfy
  ||p_i - sum_j q_i(j)p_j||_1 <= 4 delta.
```

Deps: none beyond `P^2=P`, `P1=1`, and `neg(p_i)<=delta`.

Future `af` size: one workspace, expected below 6 nodes.

### C1. Bad-kernel resolvent

Status: ready.

```text
lem-bad-kernel-resolvent:
Assume C0.  Let B be a bad index set, G=B^c, T=q|_{B,B}, and suppose every
G-row is Gamma-close to a convex set C.  If rho(T)<1 and
L=||(I-T)^(-1)||_{inf->inf}, then every i in B satisfies
  dist_1(p_i,C) <= Gamma + 4 delta L.
```

Deps: C0, convexity of distance to a convex set, substochastic identity
`(I-T)^(-1)(1-T1)=1`.

Future `af` size: one workspace, expected below 10 nodes.

### C2. Long-lifetime quasi-closed measure

Status: ready after review.

```text
lem-long-lifetime-quasi-closed-measure:
For a finite substochastic block T with exit s=1-T1, either
  ||(I-T)^(-1)1||_infty <= L
or there is a probability mu on B such that
  mu s <= 1/L,        ||muT-mu||_1 <= 2/L.
```

Deps: finite geometric-series occupation measure.

Future `af` size: one workspace, expected below 8 nodes.

### C3. Distance separator

Status: ready.

```text
lem-bad-row-distance-separator:
If dist_1(p_i,C)>=H tau for a convex hull C, then there is an affine
functional phi with l_infty-dual norm <=1 such that
  phi(p_i) >= sup_C phi + H tau.
```

Deps: finite-dimensional l1/l_infty dual separation.  Canonical use should
either prove the finite separation lemma internally or cite a byte-verified
local source.

Future `af` size: split into separation lemma plus application if it grows
past 12 nodes.

### C4. High-slice drift bound

Status: ready in the two-scale form.

```text
lem-high-slice-drift-bound:
Assume C0 with error eps and let phi be L_phi-Lipschitz in l1.  If
M=max_j phi(p_j), h_i=M-phi(p_i), and H_gamma={j:h_j<=gamma}, then
  q_i(H_gamma^c) <= (h_i+L_phi eps)/gamma.
```

Deps: C0.

Future `af` size: one workspace, expected below 6 nodes.

### C5. High-slice bad closure

Status: ready as a conditional corollary.

```text
lem-high-slice-bad-closure:
Under C4, if B has exit s_i=q_i(B^c), then
  q_i((B cap H_gamma)^c) <= s_i + (h_i+L_phi eps)/gamma.
In particular, rows in an O(delta) top core map outside a gamma~tau high slice
with O(tau) mass, provided their B-exit is O(tau).
```

Deps: C4.

Future `af` size: one workspace, expected below 6 nodes.

### C6. Top-face exposure

Status: ready.

```text
lem-top-face-exposure:
Let u be a row vertex maximizing an affine functional phi on all rows.  If
every row with ||p_i-u||_1>=rho has
  phi(u)-phi(p_i) >= Delta_phi,
then
  e_u(rho) >= Delta_phi/M_phi,
where M_phi=max_i(phi(u)-phi(p_i)).  If ||phi||_{l_infty-dual}<=1, then
M_phi<=2+4delta.
```

Deps: row diameter bound `diam_1(K)<=2+4delta`.

Future `af` size: one workspace, expected below 8 nodes.

### C7. Shadow edge

Status: ready, with the global-maximizer hypothesis.

```text
lem-shadow-edge:
Let u be a row vertex with phi(u)=max_i phi(p_i).  If e_u(rho)<kappa, then
there is a row index j with ||p_j-u||_1>=rho and
  phi(p_j) >= phi(u) - (2+4delta)kappa.
If phi(u)>=sup_C phi+H tau, then
  dist_1(p_j,C) >= (H-(2+4delta)k)tau.
```

Deps: C6, exposedness definition.  The row-vertex conversion is not included;
the recurrence must accept row-index or barycentric witnesses.

Future `af` size: one workspace, expected below 10 nodes.

### C8. Shadow recurrence

Status: ready as finite recurrence, conditional on high-supported witnesses.

```text
lem-shadow-recurrence:
Let H be finite and S>=0 be substochastic on H with row sums at least
1-eps_s.  Then there is a probability pi supported on a recurrent class of
the row-normalized chain such that
  ||piS-pi||_1 <= eps_s.
If also q_i(H^c)<=eps_q for all i in H, then
  pi q(H^c) <= eps_q.
```

Deps: finite stochastic recurrent class theorem.

Future `af` size: one workspace, expected below 10 nodes.

### C9. Shadow-exit interface

Status: open.

```text
lem-shadow-exit-gap:
For a high bad slice obtained from C3-C5, either failed-exposedness witnesses
can be chosen as a shadow kernel with H-leakage O(tau), or the repaired q-chain
has a Lyapunov drift/resolvent bound O(1/tau) and the bad rows are already
O(tau)-close to C.
```

Deps: C1-C8.  This is the first central blocker.

Future `af` size: should be split before formalization.  Suggested split:

```text
C9a: distributional closure/pruning from long lifetime and high slice;
C9b: witness-leakage alternative for failed-exposedness barycenters;
C9c: Lyapunov fallback implies the C1 resolvent hypothesis.
```

### C10. Failed-exposedness circuit

Status: ready.

```text
lem-failed-exposedness-circuit:
For a finite row set X, vertex v, and scale rho, if e_v(rho)<kappa, then
there exist mu in Delta({j:||x_j-v||_1>=rho}) and alpha,beta>=0 such that
  sum_j mu_j(x_j-v) = sum_i (beta_i-alpha_i)(x_i-v),
  sum_i beta_i < kappa,
with alpha supported on the zero face and beta supported on the top face of
an optimal exposing functional.
```

Deps: finite minimax plus LP strong duality/Farkas.  Agent A may want this
split into minimax, fixed-barycenter duality, and complementarity normal form.

Future `af` size: three small workspaces if avoiding a large black box.

### C11. Circuit aggregation with alpha budget

Status: conditional.

```text
lem-circuit-aggregation-with-alpha-budget:
Assume C0 and failed-exposedness circuits from C10 for b in a q-quasi-closed
high class B, averaged by a probability m.  If
  sum_b m_b |alpha^b|_1 <= M,
then there is a normalized affine circuit with beta mass <=kappa, q-flow
residual O(delta(1+M)+xi(1+M)), and separated witness mass >=1/(1+M).
```

Deps: C0, C10, quasi-closedness of `m`.

Future `af` size: one conditional workspace, expected below 12 nodes if the
normalization is fixed in advance.

### C12. Alpha-budget or calibrated-dual lemma

Status: open.

```text
lem-alpha-budget-or-calibrated-dual:
In a q-quasi-closed high bad class where every high vertex fails
e_v(rho)>=kappa, the failed-exposedness witnesses can be chosen either with
averaged alpha mass M=O(1), or with a q-compatible calibration whose residual
is O(tau) and whose separated witness mass is at least a quantified theta.
```

Deps: C9-C11 plus LP/game dual mining.  This is the second central blocker.

Future `af` size: not ready.  It must be split after a proof mechanism is
found.

### C13. Separated-circuit negative-mass lower bound

Status: open; Step 7 now has a sanity artifact and refined target.

```text
lem-separated-circuit-negative-mass:
Let an exact signed affine retraction contain a normalized affine circuit
whose separated witness part has mass theta on pairs at l1-distance at least
rho, and whose residual is at most E.  Then
  max_i neg(p_i) >= c theta rho - C E
or, in the stronger mass-free form,
  max_i neg(p_i) >= c rho^2 - C E.
```

Deps: exact idempotency, row negative-mass algebra, and the normalization
output by C11/C12.  The `n=4` circuit note supports this shape only in the
corank-one `2|2` model; it is not a general proof.

Future `af` size: not ready.  First split should isolate the exact
normalization: constant witness mass versus witness mass `Omega(tau)`.
The weaker bound `theta rho^2` is useful only when `theta=Omega(1)`;
it does not close the route if Step 6 gives only `theta=Omega(tau)`.

### C14. Closed-bad-class augmentation

Status: blocked on C9, C12, C13.

```text
lem-closed-bad-class-augmentation:
Choose constants in the hierarchy below.  Let B be a bad row-vertex class
farther than D tau from C=conv(R0), enlarged by rho-clusters, and suppose B is
O(tau)-closed under q in the sense supplied by the long-lifetime alternative.
If R0 is a maximal 4rho-separated subset of W_{rho,kappa}, then B contains a
row vertex w with
  dist_1(w,C)>4rho        and        e_w(rho)>=kappa.
```

Proof skeleton once blockers close:

```text
separator from C3
-> high slice from C4-C5
-> either top vertex exposed by C6, or shadow witness by C7
-> recurrent high class by C8/C9
-> local circuits by C10
-> aggregated circuit by C11/C12
-> negative-mass contradiction by C13
-> therefore an augmenting exposed vertex exists.
```

Future `af` size: capstone should be one short workspace after C9/C12/C13 are
proved.  If it exceeds 12 nodes, split into "augmentation contradiction" and
"maximality contradiction".

### C15. Global exposed-hull capstone

Status: conditional on C14, otherwise ready.

```text
prop-op-exposed-hull-from-closed-bad-class:
Assume C14.  For a maximal 4rho-separated skeleton R0 in W_{rho,kappa}, every
row is O(tau)-close to conv(R0), hence to conv W_{rho,kappa}.
```

Deps: C1, C2, C14, maximality of `R0`.

Future `af` size: one workspace, expected below 8 nodes.

## Proposed DAG

```text
C0 positive-coordinate repair
  -> C1 bad-kernel resolvent
  -> C4 high-slice drift
  -> C11 circuit aggregation with alpha budget

C1 + C2 long-lifetime quasi-closed measure
  -> C9 shadow-exit interface
  -> C14 closed-bad-class augmentation
  -> C15 global exposed-hull capstone

C3 distance separator
  -> C4 high-slice drift
  -> C5 high-slice bad closure
  -> C9 shadow-exit interface

C6 top-face exposure
  -> C7 shadow edge
  -> C8 shadow recurrence
  -> C9 shadow-exit interface

C10 failed-exposedness circuit
  -> C11 circuit aggregation with alpha budget
  -> C12 alpha-budget or calibrated-dual lemma
  -> C13 separated-circuit negative-mass lower bound
  -> C14 closed-bad-class augmentation
```

Blocker cut:

```text
{C9, C12, C13} blocks C14.
C14 blocks C15.
```

## Constants

The constants must be chosen in this order, because later inequalities consume
earlier slack.

1. Fix the normalization of C13.  This supplies constants
   `c_circ`, `C_res`, and the required separated witness mass `theta`.
   If `theta` may be only `theta_0 tau`, C13 must have at least
   `theta rho` strength; `theta rho^2` is too weak.
2. Choose `R` large enough that the lower bound beats the allowed negative
   mass:

```text
c_circ R^2 >= 10                       for the mass-free rho^2 form,
c_circ theta_0 R >= 10                 for the theta rho form.
```

   after allowing the residual terms from C11/C12.
3. Choose `k>0` small enough that all shadow/exposedness losses are lower
   order:

```text
(2+4delta_0)k << 1,        k << R,        C_res k << c_circ theta R^2.
```

4. Choose high-slice constants `G,A0` so the Step 1 leakage budget is small:

```text
gamma=G tau,        alpha=A0 delta,
((A0+4)/G) tau <= eps_q tau,
eps_q << k.
```

5. Choose the lifetime cutoff `L0=A_life/tau`.  The resolvent cost is

```text
4 delta L0 = 4 A_life tau.
```

6. Choose the badness height `D` last, much larger than the geometric and
   resolvent constants:

```text
D >> A_life + R + G + 1,        D >= 100R.
```

   This ensures shadow rows remain bad after the `(2+4delta)k tau` loss and
   augmenting vertices remain farther than `4rho` from the old skeleton.
7. Choose `delta_0` last so all scale assumptions hold:

```text
0<delta<=delta_0,        tau=sqrt(delta),
D tau << 1,             R tau << 1,
2+4delta <= 3.
```

This hierarchy is schematic until C13 fixes the exact residual form.  The only
non-negotiable qualitative order is:

```text
D >> A_life + R + G >> R >> 1 >> k,eps_q,eps_s,
```

with `R` large enough for the `rho^2=R^2 delta` contradiction.

## Blocking Lemmas

### B1. Shadow-exit/interface lemma

Current issue: Step 1 gives rowwise `O(tau)` closure only for an `O(delta)`
top core with rowwise bad-exit control.  Long lifetime naturally gives a
distributional quasi-closed measure, and Step 3 naturally gives barycentric
shadow witnesses.  These need to be coupled.

Acceptable outputs:

```text
rowwise high class H with q_i(H^c)=O(tau) and shadow witnesses leaking O(tau);
or a Lyapunov drift that returns to C1 with lifetime O(1/tau).
```

### B2. Alpha-budget/calibrated-dual lemma

Current issue: Step 5 controls the top-face `beta` mass but not the zero-face
`alpha` mass.  Step 6 shows raw q-quasi-closedness does not control alpha.

Acceptable outputs:

```text
averaged alpha mass M=O(1);
or M=O(1/tau) plus a Step 7 lower bound that tolerates witness mass Omega(tau);
or a calibrated witness selection where alpha is q-controlled.
```

### B3. Separated-circuit negative-mass lower bound

Current issue: Step 7 delivered sanity checks and a refined target, but not a
proof.  The n=4 circuit note verifies the right coefficient geometry in the
smallest non-simplex model, while the transient-row stochastic example shows
that nonvertex affine circuits must be excluded.

Acceptable output:

```text
max_i neg(p_i) >= c theta rho^2 - C E
```

for constant witness mass, or preferably

```text
max_i neg(p_i) >= c theta rho - C E
```

when Step 6 supplies only `theta=Omega(tau)`.  The dependence on witness mass
`theta` and aggregation residual `E` must be explicit.

## Agent A Handoff Criteria

The following items are ready for Agent A review as isolated candidate
workspaces, provided Agent A agrees with the statements:

```text
C0 positive-coordinate repair;
C1 bad-kernel resolvent;
C2 long-lifetime quasi-closed measure;
C4 high-slice drift bound;
C5 high-slice bad closure;
C6 top-face exposure;
C7 shadow edge;
C8 shadow recurrence;
C10 failed-exposedness circuit, possibly split into LP-duality sublemmas.
```

The closed-bad-class lemma itself is not ready for formalization until all of
the following are true:

```text
1. C9 is proved or replaced by a sharper interface statement.
2. C12 is proved, or C11 is supplied with a verified alpha budget.
3. C13 is proved with constants compatible with the C11/C12 residual.
4. The constant hierarchy above is instantiated numerically or symbolically.
5. Known stress families, especially Hume products and dense polygon warnings,
   do not violate the chosen constants.
6. Any external separation/LP-duality theorem used canonically has a local
   refs plan, or is proved directly inside the future workspace.
```

Only after those criteria are met should Agent B propose a canonical
`argument/lemmas/` split through Recipe A.  Until then, `op-exposed-hull`
remains open, and this note is the restart map for the next attack on the
hard block.
