# Subagent: op-exposed-hull n=4 Circuit Gap

Date: 2026-06-07. Lane: Agent B sandbox. Status: exploratory proof skeleton,
not a canonical proof shard.

## Verdict

The requested n=4, rank-3, corank-one `2|2` small-case dichotomy is closed at
the coefficient level.

For any genuine `2|2` quadrilateral circuit, after normalizing the Radon
coefficients, either every coefficient that controls a vertex exposure is at
least `k sqrt(delta)`, in which case all four vertices are
`k sqrt(delta)`-exposed at every scale `rho`; or one coefficient is smaller
than `k sqrt(delta)`, in which case the corresponding vertex is within
`O(k sqrt(delta))` of the opposite edge, so the quadrilateral is
`O(sqrt(delta))`-close to a triangle/segment.

The full row-wise `u` inequalities are only needed here for the row-diameter
bound. Idempotency supplies the affine circuit.

## Parameterization

Let `P` be a `4 x 4` row-stochastic idempotent of rank `3`. Then `I-P` is a
rank-one idempotent, so

```text
P = I - u v^T,        sum_i v_i = 0,        v^T u = 1.
```

In the only genuine quadrilateral case, after permutation and rescaling,

```text
v = (a,b,-c,-d),        a,b,c,d > 0,        a+b=c+d=1.
```

Writing the rows as `p_i`, the rank-one defect gives

```text
v^T P = 0,
```

hence the normalized affine circuit

```text
a p_0 + b p_1 = c p_2 + d p_3.              (C)
```

Since all four coefficients are positive, nondegenerate rows form a
quadrilateral; degeneracies are already simplex/segment cases.

## Negative-Mass Inequalities

For row `i`,

```text
P_ij = delta_ij - u_i v_j.
```

Let `m_i = |v_i|` and `s_i = sign(v_i)`. The condition
`neg(P_i) <= delta` is exactly:

```text
if s_i u_i >= 0:
    |u_i|(1-m_i) + max(|u_i|m_i - 1, 0) <= delta,
if s_i u_i < 0:
    |u_i| <= delta.
```

In the displayed `2|2` coordinates this says:

```text
u_i aligned with v_i:      |u_i|(1-|v_i|)+max(|u_i||v_i|-1,0) <= delta,
u_i opposite sign to v_i:  |u_i| <= delta.
```

These imply the active-index facts from `rank-one-classical-stability.md`. For
this dichotomy the only quantitative consequence needed is the row-diameter
bound

```text
||p_i||_1 <= 1 + 2 delta,
diam_1{p_0,p_1,p_2,p_3} <= 2 + 4 delta.       (D)
```

## Exposing Values

An affine functional on the four rows is determined by its values
`y_i=h(p_i)`, subject only to the circuit relation

```text
a y_0 + b y_1 = c y_2 + d y_3.              (C_h)
```

The following value assignments satisfy `(C_h)` and lie in `[0,1]`:

```text
vertex p_0:  (0, 1, b, b)        gives e_{p_0}(rho) >= b,
vertex p_1:  (1, 0, a, a)        gives e_{p_1}(rho) >= a,
vertex p_2:  (d, d, 0, 1)        gives e_{p_2}(rho) >= d,
vertex p_3:  (c, c, 1, 0)        gives e_{p_3}(rho) >= c.
```

These lower bounds hold for every `rho`: if some row is closer than `rho`, it
is removed from the outside set and the certificate only becomes easier.

Thus, for `tau=sqrt(delta)` and `kappa=k tau`, if

```text
min(a,b,c,d) >= k tau,
```

then all four row vertices belong to `W_{rho,kappa}`, for any choice of
`rho`.

## Collapse Alternative

If a coefficient controlling a vertex exposure is small, the same circuit
places that vertex near the opposite edge. With `D=diam_1{p_i}`:

```text
b small:  dist_1(p_0, conv{p_2,p_3}) <= (b/a) D,
a small:  dist_1(p_1, conv{p_2,p_3}) <= (a/b) D,
d small:  dist_1(p_2, conv{p_0,p_1}) <= (d/c) D,
c small:  dist_1(p_3, conv{p_0,p_1}) <= (c/d) D.
```

For example, if `b < k tau` and `k tau <= 1/2`, then `a=1-b >= 1/2`, and by
`(D)`

```text
dist_1(p_0, conv{p_2,p_3})
  <= 2(2+4 delta) k tau.
```

For `delta <= 1/2`, this is at most `8 k tau`. The other three cases are
identical. If several coefficients are small, the quadrilateral collapses
further, potentially to a segment.

## Constants

A clean small-case package is:

```text
delta <= 1/2,
tau = sqrt(delta),
kappa = k tau with k <= 1/8.
```

Then exactly one of the following holds:

```text
all four vertices satisfy e_v(rho) >= kappa for every rho;
or
some vertex is within 8 k tau of the opposite edge.
```

Taking `k=1/8` gives collapse distance at most `tau`.

## Artifacts

Reproducible coefficient certificates:

```bash
python3 agent-B/experiments/op-exposed-hull/n4_circuit_analysis.py
```

Outputs:

```text
agent-B/experiments/op-exposed-hull/n4_circuit_analysis.py
agent-B/experiments/op-exposed-hull/n4_circuit_analysis.json
```

The script records the exposing values, lower bounds, and collapse bounds for
representative regimes, including the Hume-shaped `a=c=1-t^2`, `b=d=t^2` case.

## Failure Modes

This is a coefficient-level proof skeleton, not yet an `af` proof. The packaging
risk is wording the collapse branch. It proves closeness to the opposite edge;
Agent A should decide whether the canonical small-case lemma should state this
as:

```text
quadrilateral is O(tau)-close to a simplex hull,
```

or directly as the four displayed edge-distance alternatives.

Degenerate rows fall into the segment/simplex certificate from
`subagent-op-exposed-hull-small-cases.md`.

## Next Handoff

Package this as a short formal lemma:

```text
Given four rows satisfying a positive `2|2` affine circuit
a p_0+b p_1=c p_2+d p_3 with a+b=c+d=1 and row diameter D,
either all four vertices are min(a,b,c,d)-exposed, or the vertex controlled by
any coefficient eps is within eps/(1-eps) D of the opposite edge.
```

Then combine it with the corank-one parameterization above. This should retire
the n=4 circuit gap as an obstruction to `op-exposed-hull`.
