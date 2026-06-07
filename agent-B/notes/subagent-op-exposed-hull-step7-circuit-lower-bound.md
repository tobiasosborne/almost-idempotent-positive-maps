# Subagent Step 7: Separated-Circuit Negative-Mass Lower Bound

Date: 2026-06-07.  Lane: Agent B sandbox.  Status: exploratory, not a
canonical proof shard.

## Verdict

The raw Step 7 statement is false:

```text
any rho-separated affine circuit in an exact signed affine retraction
  -> max row negative mass >= c rho^2.
```

A stochastic idempotent can have transient rows that form separated affine
circuits with zero negative mass.  Therefore Step 7 must be restricted to the
kind of circuit produced by Steps 5-6: a reduced row-vertex or one-sided
failed-exposedness circuit, with quantified separated witness mass and an
aggregation residual.

The useful target remains plausible, but it is open.  There are three possible
strengths:

```text
strong:  neg >= c rho^2 - C E,
medium:  neg >= c theta rho - C E,
weak:    neg >= c theta rho^2 - C E.
```

Here `theta` is the separated witness mass and `E` is the residual from Step
6.  The weak form only closes the global route when `theta=Omega(1)`.  If Step
6 gives only `theta=Omega(tau)`, the route needs at least the medium form, or
the strong form.

## Sanity Artifacts

Created:

```text
agent-B/experiments/op-exposed-hull/step7_circuit_sanity.py
agent-B/experiments/op-exposed-hull/step7_circuit_sanity.json
```

Re-run command:

```text
python3 agent-B/experiments/op-exposed-hull/step7_circuit_sanity.py
```

The script records two warnings.

First, the stochastic idempotent

```text
p_0=(1,0,0),        p_1=(0,1,0),        p_2=(1/2,1/2,0)
```

has exact circuit

```text
p_2 = (p_0+p_1)/2
```

with pairwise distances `1,1,2` and zero negative mass.  The circuit uses a
non-vertex transient row, so it is harmless for exposed-hull, but it refutes
any lower bound that does not exclude nonvertex redundancy.

Second, the exact `n=4` corank-one Hume-shape family has negative mass
`delta=t^2` and circuit coefficients `1-t^2,t^2,1-t^2,t^2`.  The small
coefficient is accompanied by a vertex-pair collapse much smaller than
`tau=t`; hence it does not violate a rho-separated vertex-circuit lower bound.

## Setup For A Correct Lemma

Rows are `x_i=p_i`, with

```text
P1=1,        P^2=P,        neg(p_i)<=delta.
```

A Step-6 aggregate should supply a signed affine relation of the form

```text
sum_a lambda_a x_a - sum_b mu_b x_b = r,
sum_a lambda_a = sum_b mu_b = 1,
lambda,mu >=0,        ||r||_1 <= E.
```

It should also supply a separated witness condition.  Possible versions:

```text
constant-mass:
  lambda({a : dist_1(x_a, conv{x_b}) >= rho}) >= theta;

paired:
  there is a coupling pi_ab with marginals lambda,mu and
  pi({(a,b):||x_a-x_b||_1>=rho}) >= theta;

basepoint:
  average of rows outside B_1(v,rho) is balanced against lower-face terms
  anchored at v.
```

The lower bound must say which version it uses.  The paired/basepoint versions
are closer to the failed-exposedness circuits from Step 5.

## Necessary Hypotheses

The sanity example shows at least one of the following is necessary:

```text
1. support rows are row vertices of K;
2. the circuit is reduced/minimal in the row polytope;
3. transient rows already in the current convex hull are removed before
   applying the lower bound;
4. the one-sided Step-5 anchor/basepoint structure is retained.
```

Pure affine dependence is not enough.

The lower bound also needs a residual term.  Step 6 may output only an
approximate aggregate because positive-coordinate repair contributes
`O(delta(1+M))` and quasi-closedness contributes `O(xi(1+M))`.

## Candidate Contracts

Strong version:

```text
lem-separated-vertex-circuit-lower-bound-strong:
Let rows of an exact signed affine retraction have negative mass <=delta.
Assume there is a reduced affine circuit among row vertices with a separated
witness component at l1-scale rho and residual E.  Then
  delta >= c rho^2 - C E.
```

Medium version:

```text
lem-separated-vertex-circuit-lower-bound-medium:
Under the same hypotheses, but with separated witness mass theta,
  delta >= c theta rho - C E.
```

Weak version:

```text
lem-separated-vertex-circuit-lower-bound-weak:
Under the same hypotheses,
  delta >= c theta rho^2 - C E.
```

The weak version is not enough if Step 6 only gives `theta=Omega(tau)`, because
then `theta rho^2=O(R^2 tau^3)` cannot beat `delta=tau^2` with fixed
constants.  The medium version would suffice:

```text
theta=Omega(tau),        rho=R tau
  -> theta rho = Omega(R tau^2),
```

so choosing `R` large can contradict `delta=tau^2`.

## Possible Proof Mechanisms

### 1. Vertex-minor / oriented-matroid route

For stochastic idempotents, row vertices are affinely independent after
removing transient convex rows.  A reduced vertex circuit should therefore
force a signed minor that vanishes in the stochastic case but is perturbed by
negative entries.  The target is a quantitative contrapositive:

```text
small row negative mass
  -> every reduced vertex circuit has either small separation or tiny witness
     coefficient.
```

This matches the `n=4` circuit note: small coefficients force geometric
collapse.

### 2. Positive-coordinate support route

For each row,

```text
x_i = sum_j q_i(j)x_j + e_i,        ||e_i||_1<=4delta.
```

If a circuit is reduced and all its separated witness mass stays in a
q-closed high class, applying this reconstruction to the anchored side should
make a convex self-reconstruction of a separated vertex.  The error is
`O(delta)` per use.  A lower bound would compare this error to either
`theta rho` or `rho^2`, depending on the circuit normalization.

This route is promising because it uses the same data as Step 6, but it has
not yet been made rigorous.

### 3. LP infeasibility route

Freeze the combinatorics of a reduced separated circuit and impose

```text
P1=1,        P^2=P,        neg rows<=delta,
aggregate circuit with witness mass theta and residual E.
```

Then minimize `delta` with SciPy/Gurobi on small instances.  If infeasible
certificates appear, extract their dual shape and compare to the oriented
minor route.  This is the recommended computational follow-up.

## Constants

The global route needs one of:

```text
strong:  c R^2 > 10,
medium:  c theta_coeff R > 10   when theta >= theta_coeff tau,
weak:    c theta0 R^2 > 10      only if theta >= theta0 > 0.
```

Residuals must satisfy

```text
C E <= (1/10) * lower-bound main term.
```

This is why Step 6's alpha budget is coupled to Step 7.  If Step 6 has
`M=O(1/tau)`, its normalized witness mass may be only `Omega(tau)` and its
residual budget must still be `O(delta)` or smaller after normalization.

## Failure Modes

1. Nonvertex transient circuits give zero negative mass.
2. A lower bound with factor `theta rho^2` is too weak for
   `theta=Omega(tau)`.
3. Large Step-6 `alpha` mass can make the separated witness fraction vanish.
4. Approximate residuals can swamp the lower bound unless their dependence on
   `M` is explicit.
5. Dense polygon warnings show that pure convex geometry cannot prove the
   claim; exact idempotency and row sign constraints must enter.

## Next Handoff

The next worker should attack the medium lower bound first:

```text
delta >= c theta rho - C E
```

for reduced row-vertex or anchored Step-5 circuits.  It is strong enough for a
Step-6 witness mass `theta=Omega(tau)` and is less ambitious than the
mass-free `rho^2` bound.

The LP/game worker should build a frozen feasibility model for this exact
medium statement and search for small rational counterexamples before anyone
tries to formalize it.
