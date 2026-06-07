# Step 3 - Shadow Edge Lemma

Date: 2026-06-07.  Lane: Agent B sandbox.  Status: exploratory, not a
canonical proof shard.

## Verdict

This step is proof-ready, with one explicit hypothesis: the chosen top row
`u` must be a genuine `phi`-maximizer over all rows, or equivalently a
maximizer over a height-defined bad set so that any higher row would also be
bad and hence included.

Under that hypothesis, non-exposedness gives a `rho`-separated row witness
with only `(diam_1 K) kappa` height loss.  Since

```text
diam_1(K) <= 2+4delta,
```

the loss is at most `(2+4delta)kappa`.

At row-index level the barycenter can be converted to a single row without
loss.  At row-vertex level it cannot be converted without potentially losing a
factor `1/rho`; recurrence should therefore accept row or barycentric shadow
witnesses, and postpone vertex extraction to the closed-class/circuit stage.

## Setup

Rows are `x_i=p_i`, `K=conv{x_i}`, `P1=1`, `P^2=P`, and
`neg(x_i)<=delta`.  Put

```text
tau=sqrt(delta),        rho=R tau,        kappa=k tau.
```

Let `C=conv(R0)` be the current exposed skeleton hull.  Let `phi` be an affine
functional whose linear part has `l_infty` norm at most `1`; constants are
irrelevant, so write

```text
s=sup_{z in C} phi(z).
```

For a row vertex `u`, define

```text
S_u(rho)={i : ||x_i-u||_1 >= rho}.
```

The exposedness gauge is

```text
e_u(rho)=sup_h min_{i in S_u(rho)} h(x_i),
```

where `h` ranges over affine functions on `aff(K)` with

```text
h(u)=0,        0<=h(x_i)<=1 for all rows i.
```

Let

```text
M=diam_1(K).
```

Since each row has total mass `1` and negative mass at most `delta`,

```text
||x_i||_1=1+2 neg(x_i) <= 1+2delta,
M <= 2+4delta.                                      (D)
```

## Candidate Contract

```text
lem-shadow-edge:
Let u be a row vertex with phi(u)=max_i phi(x_i).  If e_u(rho)<kappa, then
there exists a row index j with ||x_j-u||_1>=rho and

    phi(x_j) >= phi(u) - (2+4delta) kappa.

Moreover, if phi(u)>=s+H tau, then

    dist_1(x_j,C) >= (H-(2+4delta)k) tau.

In particular, for nested bad thresholds D_bad < H-(2+4delta)k, the shadow row
j is still D_bad-bad.
```

The same statement holds with a barycenter `y` supported on `S_u(rho)` in
place of `x_j`; the row witness is obtained by choosing a support row with
maximal `phi`.

## Proof Outline

Because `u` is a global `phi`-maximizer over rows,

```text
0 <= phi(u)-phi(x_i) <= M
```

for every row `i`.  Therefore

```text
h_phi(x) = (phi(u)-phi(x))/M
```

is an admissible exposedness test function: `h_phi(u)=0` and
`0<=h_phi(x_i)<=1`.

If `e_u(rho)<kappa`, then no admissible test function has gap `kappa` on all
rows outside the `rho`-ball.  Applying this to `h_phi` gives some
`j in S_u(rho)` with

```text
h_phi(x_j)<kappa.
```

Thus

```text
phi(x_j) > phi(u)-M kappa
          >= phi(u)-(2+4delta)kappa.
```

This proves the shadow edge.

For badness, assume `phi(u)>=s+H tau`.  Then

```text
phi(x_j) >= s + H tau - (2+4delta)kappa
          = s + (H-(2+4delta)k) tau.
```

Since the linear part of `phi` has `l_infty` norm at most `1`, for every
`z in C`,

```text
||x_j-z||_1 >= phi(x_j)-phi(z) >= phi(x_j)-s.
```

Taking the infimum over `z in C` gives

```text
dist_1(x_j,C) >= (H-(2+4delta)k) tau.
```

## Minimax/Barycenter Form

The LP-dual note gives

```text
e_u(rho)=min_{mu in Delta(S_u(rho))} G_u(y_mu),
y_mu=sum_{i in S_u(rho)} mu_i x_i,
G_u(y)=sup_h h(y),
```

with the same admissible class of `h`.  If `e_u(rho)<kappa`, choose `mu` with
`G_u(y_mu)<kappa`.  Since `h_phi` is one admissible `h`,

```text
h_phi(y_mu)<kappa,
phi(y_mu)>phi(u)-M kappa.
```

Because `y_mu` is an average of rows in `S_u(rho)`, at least one support row
`j` satisfies

```text
phi(x_j) >= phi(y_mu) > phi(u)-M kappa,
```

and this `j` is still in `S_u(rho)`.  Thus the barycenter and row-index
versions are equivalent for Step 3.

The barycenter is still the right object for the later circuit stage: it is the
object that appears in the Farkas certificate for failed exposedness, with
small positive dual mass.

## Why Not Force A Row Vertex Here?

If the row witness `x_j` is not a vertex of `K`, a vertex decomposition

```text
x_j=sum_a lambda_a v_a
```

does give at least one vertex with `phi(v_a)>=phi(x_j)`, hence still high and
bad.  It also gives at least one vertex far from `u`, because the `l_1` ball
around `u` is convex.

It does not give one vertex that is both far from `u` and high with
`O(kappa)` loss.  Quantitatively, if `||x_j-u||_1>=rho`, then one can only
force a vertex at distance at least `rho/2` with height deficit bounded by
roughly

```text
2 M^2 kappa / rho.
```

With `rho=R tau` and `kappa=k tau`, this is `O(k/R)`, not `O(tau)`.  That loss
is too large for the high-bad recurrence.  The recurrence should therefore run
on row indices or barycentric shadow witnesses; vertex extraction belongs to
the later aggregation/lower-bound step.

## Constants

Universal height loss:

```text
M kappa <= (2+4delta) kappa.
```

For `delta<=1/16`, this is at most

```text
(9/4) kappa.
```

For the common coarse regime `delta<=1/4`, it is at most

```text
3 kappa.
```

To keep the shadow row above a badness threshold `D_bad tau`, choose the top
height `H tau` with

```text
H >= D_bad + (2+4delta)k.
```

This is the precise meaning of "still bad when D >> k".  If the same symbol
`D` is used for both top height and badness threshold, Step 3 only preserves a
slightly lower threshold:

```text
D tau  ->  (D-(2+4delta)k) tau.
```

So the recurrence package should use nested height levels or reserve a margin.

## Failure Modes

1. If `u` is only maximal inside an arbitrary subset, `h_phi` may be negative
   on rows outside that subset and is not an admissible exposedness test.  The
   lemma must be applied to a true global `phi`-maximizer, or to a
   height-defined bad set where every higher row is automatically included.
2. The row witness may be an interior row of `K`.  Converting immediately to a
   row vertex can lose `1/rho`, which is fatal at square-root scale.
3. Step 3 creates propagation, not contradiction.  A flat high component can
   still cycle; that is exactly the Step 4 recurrence/potential problem.
4. Equality at `e_u(rho)=kappa` is a boundary issue.  Formal statements should
   use either `e_u(rho)<kappa` or an `eta`-slack version.

## Next Handoff To Recurrence

Step 4 should take as input a directed shadow relation on high row indices:

```text
u -> j
iff
||x_j-u||_1>=rho
and
phi(x_j) >= phi(u) - M kappa.
```

Together with Step 1 high-slice quasi-closedness, recurrence must show that
iterating this relation either:

```text
1. loses enough height to give a Lyapunov/short-lifetime bound, or
2. traps a recurrent high bad component carrying the failed-exposedness
   circuits needed for aggregation.
```

Step 3 supplies the local outgoing edge from every non-well-exposed
separator-maximal row.  It deliberately does not attempt the no-cycle
contradiction.
