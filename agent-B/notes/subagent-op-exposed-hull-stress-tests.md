# Subagent F: op-exposed-hull Stress Tests

Date: 2026-06-07.  Lane: Agent B sandbox.  Status: exploratory evidence, not a
canonical proof shard.

## Target

For an exact signed affine retraction `P` with

```text
P1=1,        P^2=P,        neg(p_i)<=delta,        tau=sqrt(delta),
```

the open target `op-exposed-hull` asks whether, for universal constants
`rho=A tau` and `kappa=c tau`, every row is `O(tau)` from the convex hull of
the row vertices with exposedness modulus at least `kappa`.

## Reproducible Artifacts

Main command:

```bash
python3 agent-B/experiments/op-exposed-hull/stress_test_families.py
```

Artifact hashes:
`stress_test_families.py` `7cbe9ea3c201978764600d298972a3c0fe19ee0580061a6ce76c017b7b5e2331`;
`stress_test_families.json` `706309b0bb8941c983e00912dc616f1ec5415648f9aa9e83ce2757a2fad42c29`;
`stress_test_families.csv` `00a5cc801347b463b95cbaa467d5b43defa0b3c3bc3a2a369c24a33157638969`.

SciPy HiGHS LPs compute row vertices, exposedness moduli, and `l1` distance to
`conv W`.  `gurobi_cl` is installed, but `gurobipy`/`cvxpy` are absent;
WolframScript is installed but not activated.  SymPy sanity check:

```text
local cyclic stencil high-frequency idempotency defect -> 2,
negative mass 1/cos(2pi/m)-1 = 2pi^2/m^2 + O(m^-4).
```

## 1. Hume And Hume Products

```text
P_s = I - u_s v_s^T,
v_s=(1,-1+s,-s),
u_s=(1-s+s^2,-s,0)^T.
```

The tensor power `P_s^{\otimes k}` is again an exact row-unital idempotent.
The row negative mass is

```text
delta_k = ((1+2s^2)^k - 1)/2 = k s^2 + O(k^2 s^4).
```

Numerics at `rho=4tau`, `kappa=0.1tau`:
```text
hume_s=0.02                         delta=0.0004       vertices=2   W=2   maxdist/tau=0
hume_tensor_power=2_s=0.02           delta=0.00080032   vertices=4   W=4   maxdist/tau=0
hume_tensor_power=3_s=0.02           delta=0.00120096   vertices=8   W=8   maxdist/tau=0
hume_direct_sum_copies=6_s=0.05      delta=0.0025      vertices=12  W=12  maxdist/tau=0
```

Verdict: sharp but not a counterexample.  Naive product rounding can
accumulate, but the tensor-product vertex rows remain well exposed for small
`c`, and every row is already in their hull.

Constants caveat: `outputs/hume_product_s003_p2.json` shows artificial failure
if one demands `kappa=tau` at very small `rho`; then only the most exposed
vertex survives.  The open contract allows a sufficiently small universal `c`.

## 2. Dense Regular Polygons

Exact first-harmonic affine projection:

```text
P_ij = (1 + 2 cos(2pi(i-j)/m))/m.
```

This is exact but has negative mass bounded away from zero:
```text
m=7   delta=0.229125
m=11  delta=0.223401
m=21  delta=0.213876
m=41  delta=0.218363
```

Local neighbor stencil:

```text
x_i = (x_{i-1}+x_{i+1})/(2 cos theta)
      + (1 - 1/cos theta) * center,      theta=2pi/m.
```

After distributing the center coefficient uniformly, negative mass is small
but exact idempotency is badly false:
```text
m=11  delta=0.154393   ||P^2-P||_{inf->inf}=2.70367
m=21  delta=0.0420649  ||P^2-P||_{inf->inf}=2.17639
m=41  delta=0.0112801  ||P^2-P||_{inf->inf}=2.04596
```

Verdict: dense polygons are a real warning against sequential pointwise
deletion, but exact retraction constraints block them.  The exact projection
has constant negative mass; the small-negative local chain has order-one
idempotency defect.

## 3. Cyclic Redundancy Chains

The cyclic chain is the local polygon false alarm: every vertex borrows from
neighbors with `O(m^-2)` negative mass, so pointwise redundancy can form a
long cycle.  But the Fourier multipliers are

```text
mu_l = cos(l theta)/cos(theta),
```

not `0` or `1`.  High-frequency modes give

```text
mu^2 - mu -> 2.
```

Verdict: cyclic redundancy breaks non-accumulating deletion logic, not
`op-exposed-hull` under exact `P^2=P`.

## 4. High-Dimensional Affine Circuits

Hypercube first-order affine projection:

```text
lambda_s(t)=2^{-d}(1+s.t),        s,t in {+-1}^d.
```

This gives exact row-unital idempotents with cube-like affine circuits, but
the negative mass is not small:

```text
d=2  delta=0.25
d=3  delta=0.25
d=4  delta=0.4375
d=5  delta=0.4375
```

The robust-coordinate probe agrees: best simplex-coordinate negative mass is
`>=1/3` for regular polygons from `m=6` onward and `1` for thin rectangles.

Verdict: fixed-complexity circuits are already covered by the
`prop-parallelogram` direction; these explicit high-dimensional circuits have
constant negative mass and do not threaten a small-`delta` theorem.

## 5. Random Exact Signed Similarities

```text
P = S^{-1} E S,        S1=1,
```

where `E` is a stochastic idempotent and `S` is a small random row-sum
preserving similarity.  This preserves `P1=1` and `P^2=P` exactly while
introducing signed rows.

Sweep: 20 cases with `n in {8,12}`, rank `3` or `4`, amplitudes `0.005`,
`0.02`, `0.05`.  At `rho=4tau`, `kappa=0.1tau`, worst observed case:

```text
random_similarity_n=12_rank=4_eps=0.05_seed=234
delta=0.188449, vertices=9, W=8, maxdist/tau=0.0395292.
```

Most random exact projections had `W` equal to all vertices and `maxdist/tau=0`.
Separate existing random projections in
`random_n4_r2_metrics.json`, `random_n5_r2_metrics.json`, and
`random_n5_r3_metrics.json` also found no positive ratio at the tested scale.

Verdict: random exact signed idempotents near stochastic ones look benign.
They are useful regression tests for constants but not counterexamples.

## Overall Verdict

No serious counterexample candidate was found.

The strongest false alarms are now understood:

- Hume products preserve the sharp square-root boundary but keep the relevant
  vertices exposed for small enough `kappa/tau`.
- Dense polygons and cyclic chains expose why sequential deletion can fail,
  but exact idempotency forces either constant negative mass or order-one
  idempotency defect.
- Explicit affine circuits such as cubes have constant negative mass; small
  `delta` seems to force collapse toward simplex-like or well-exposed
  skeleton geometry.

The remaining blocker is therefore not an evident family.  It is the analytic
lemma: exact `P^2=P` plus `neg<=delta` must convert non-well-exposed vertices
into a one-shot `O(tau)` reconstruction from the already well-exposed hull.
The stress tests support focusing on the LP-dual/maximal-skeleton proof rather
than hunting for product or polygon counterexamples.
