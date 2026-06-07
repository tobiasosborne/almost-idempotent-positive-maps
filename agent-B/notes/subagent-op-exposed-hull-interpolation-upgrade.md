# Subagent: Interpolation Upgrade For `op-exposed-hull`

Date: 2026-06-07.  Lane: Agent B sandbox.  This is exploratory evidence, not
a canonical proof shard.

## Verdict

Keep the robust-coordinate route active, but narrow it to one precise LP-style
interpolation lemma.

The naive proof really is blocked: a representative interpolation matrix
`G=I+O(tau)` is not enough, because exactifying by `G^{-1}` can create
`O(tau)` coordinate negative mass.  However, the blocker does not look like a
real obstruction to `op-exposed-hull`.  An optimized stochastic push-forward
kernel achieves row-`l1` interpolation defect `O(delta)` on the sharp Hume
family, the exact rank-three quadrilateral family, and small-defect exact
similarity-conjugated projections.

So this route should not be demoted yet.  It should be treated as a certificate
extraction route parallel to the bad-kernel/resolvent route.

## Formal Obstruction

Let `R={r^1,...,r^m}` be selected representatives and let `U` be a stochastic
kernel from row labels to representatives:

```text
U_{j,a} >= 0,        sum_a U_{j,a}=1.
```

Push canonical row coordinates through `U`:

```text
lambda_a(x)=sum_j x_j U_{j,a}.
```

This gives the good part for free.  For every signed coordinate vector `x`,
stochasticity implies

```text
neg(xU) <= neg(x).
```

Hence for actual rows,

```text
neg(lambda(p_i)) <= neg(p_i) <= delta.
```

If every label row has a stochastic representative reconstruction

```text
||p_j - sum_a U_{j,a} r^a||_1 <= gamma,
```

then every row reconstructs with

```text
||p_i - sum_a lambda_a(p_i)r^a||_1
 <= (1+2delta) gamma.
```

The catch is interpolation on representatives.  Define

```text
G_{b,a}=lambda_a(r^b)=sum_j r^b_j U_{j,a}.
```

The robust simplexity reduction needs exact interpolation.  If `G` is
invertible, exactify by

```text
lambda'(x)=lambda(x) G^{-1}.
```

For dimension-free control the relevant smallness is not entrywise
`max_{b,a}|G_{b,a}-delta_{ba}|`; it is the row-operator quantity

```text
eps_G = max_b sum_a |G_{b,a}-delta_{ba}|.
```

If `eps_G<1/2`, then `||G^{-1}-I||_{infty->1} <= C eps_G`, and exactification
raises coordinate negative mass by at most `C eps_G`.  Therefore the coordinate
route needs

```text
eps_G = O(delta).
```

An `O(tau)` interpolation defect loses the target rate.  In the two-rep toy
case

```text
G = [[1-alpha, alpha],
     [alpha, 1-alpha]],
```

with `alpha ~ tau`, the inverse has negative off-diagonal entries of size
`~alpha`, so even exactifying probability coordinates can create `Theta(tau)`
negative coefficients.

## Attempted Upgrade

There is one easy exact case:

```text
if p_j = sum_a U_{j,a} r^a exactly for all row labels j
and the representatives are affinely independent, then G=I.
```

Indeed, for a representative row,

```text
r^b = r^b P
    = sum_j r^b_j p_j
    = sum_a G_{b,a} r^a.
```

Since the row sums of `G_b` are `1`, affine independence forces `G_b=e_b`.

With only `gamma=O(tau)` reconstruction error, this argument gives only
`eps_G=O(tau)` after using exposed-circuit conditioning.  The missing upgrade
is not a local exposedness estimate.  One-row exposed concentration bounds
positive leakage by

```text
delta/kappa = O(tau),
```

which is sharp at the square-root scale.  To get `O(delta)`, the kernel must
use global correction/cancellation, not only cluster assignment.

The sharpened target is:

```text
Interpolation-upgrade LP lemma.
Given a maximal square-root-exposed skeleton R with
dist_1(p_i, conv R) <= C tau for all rows, there exists a stochastic kernel U
such that
  ||p_i - sum_a U_{i,a}r^a||_1 <= C tau       for all i,
  max_b sum_a |sum_j r^b_j U_{j,a}-delta_{ba}| <= C delta.
```

This lemma would close the robust-coordinate route after exactifying by
`G^{-1}`.

## Numerical LP Probe

I added:

```bash
python3 agent-B/experiments/op-exposed-hull/interpolation_upgrade_probe.py
```

Output:

```text
agent-B/experiments/op-exposed-hull/interpolation_upgrade_probe.json
```

Script SHA256:

```text
d7b0c050b2e6f438ef63500a665947daa9e6e03fd3646de5d8b6523563138137
```

The LP variables are a stochastic kernel `U`, reconstruction slacks, and
absolute-value slacks for the rows of `G-I`.  Objective:

```text
minimize max_b sum_a |G_{b,a}-delta_{ba}|
```

subject to row reconstruction within `gamma`.  I used `gamma=4 tau` unless the
best simplex hull error was larger.

Results:

```text
Hume s=0.2,0.1,0.05,0.02,0.01:
  reps=[1,2], objective=0, exact row reconstruction.

Quadrilateral t=0.2,0.1,0.05,0.02,0.01:
  reps=[0,1,3], objective/delta -> 2,
  best simplex hull error ~ 2 delta.

Similarity n=6 rank=3 seed=20260607:
  target delta 1e-2,1e-3,1e-4,
  objective/delta ~ 0.78 to 0.79.
```

This is evidence against a `Theta(tau)` obstruction for the optimized kernel.
It also corrects the earlier weaker probe: entrywise control was not the right
quantity; the row-`l1` interpolation defect still scales like `O(delta)` in
these tests.

## Constants

The target hierarchy should be:

```text
tau = sqrt(delta),
rho = C_rho tau,
kappa = c_kappa tau,
gamma <= C_gamma tau,
eps_G <= C_G delta.
```

For exactification it is enough to require, after shrinking `delta_0`,

```text
eps_G <= 1/4.
```

Then

```text
neg(lambda'(p_i)) <= C(delta + eps_G) = O(delta),
reconstruction error <= C(gamma + eps_G) = O(tau).
```

## Failure Modes

1. Cluster assignment alone gives only `delta/kappa=O(tau)` representative
   leakage.  That is not enough.
2. Entrywise `O(delta)` control of `G-I` is not dimension-free; use row-`l1`
   or an equivalent operator bound.
3. Exactifying a merely `O(tau)` matrix can introduce `O(tau)` negative
   coordinate mass.
4. Rowwise distance to `conv R` is not a kernel.  The proof must select one
   stochastic kernel satisfying reconstruction and interpolation constraints
   simultaneously.
5. The interpolation LP may be equivalent to the closed-bad-class/resolvent
   obstruction; a failed LP dual should be fed back to that route, not treated
   as separate evidence against the theorem.

## Next Handoff

1. Extract the Farkas dual of the interpolation-upgrade LP.  The expected dual
   obstruction is a signed circuit plus a row of `G-I` that cannot be corrected
   without violating stochastic reconstruction.
2. Add a stress search that fixes `delta`, representatives, and a lower bound
   `eps_G >> delta`, then asks whether the exact-retraction equations can be
   satisfied.  If feasible, export the rationalized matrix.
3. Try to prove the LP lemma using the bad-kernel dichotomy: either the
   interpolation correction exits to the good skeleton within `O(1/tau)` steps,
   or a closed bad class contains a new well-exposed representative.
4. If Agent A wants a formalizable sublemma, start with the exact case:
   exact stochastic reconstruction by affinely independent representatives
   implies `G=I` by `P^2=P`.
