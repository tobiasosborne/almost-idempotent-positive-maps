# Subagent E: op-exposed-hull Small Cases

Date: 2026-06-07. Lane: Agent B sandbox. Status: exploratory evidence and
candidate proof structure, not a canonical proof shard.

Command:

```bash
python3 agent-B/experiments/op-exposed-hull/small_cases_exact.py
```

Artifacts:

- `agent-B/experiments/op-exposed-hull/small_cases_exact.py`
- `agent-B/experiments/op-exposed-hull/small_cases_exact.json`
- `agent-B/experiments/op-exposed-hull/small_cases_exact.csv`
- `agent-B/experiments/op-exposed-hull/gurobi_exposedness_quad_t_1_10_v1.{lp,log,sol}`

Script SHA256:

```text
8aaf167f6fb14bca55f2979ec9e79f500d911149b81c084ec061924baf5a9df1
```

Tools: SymPy 1.14.0 and SciPy 1.11.4 were used. `gurobi_cl` 13.0.2 solved
the exported quadrilateral exposedness LP with objective
`0.99=1-(1/10)^2`. `wolframscript` is installed but not licensed, so Wolfram
was unavailable.

## Target And LP

For an exact signed affine retraction

```text
P1=1,        P^2=P,        neg(p_i)<=delta,        tau=sqrt(delta),
```

the exposed-hull target asks whether, for `rho=C tau` and `kappa=c tau`, every
row is `O(tau)`-close to `conv W`, where `W` is the set of row vertices with
`e_v(rho)>=kappa`.

The finite-row exposedness LP is:

```text
maximize t
subject to h(p_v)=0,
           0 <= h(p_i) <= 1 for every row,
           h(p_i) >= t for every outside row ||p_i-p_v||_1 >= rho,
```

with affine `h`. A separate LP computes `l1` distance to a hull.

## Exact Certificates

### Matrix rank <= 2

If `rank(P)<=2`, the row polytope is a point or segment. For `K=[a,b]`, set
`D=||a-b||_1`. The endpoint coordinate

```text
h((1-lambda)a+lambda b)=lambda
```

has `h>=rho/D` on all outside rows from `a`, and similarly at `b`. Since each
signed probability row has `||p_i||_1<=1+2delta`,

```text
D <= 2+4delta.
```

For `delta<=1/2`, `rho=C tau` implies

```text
e_a(rho), e_b(rho) >= C tau/4.
```

Thus both endpoints are in `W` for `kappa<=C tau/4`, and every row lies in
`conv W` exactly. Hull error: `0`.

### n=3

Every exact `3x3` case is covered:

- rank `1`: point;
- rank `2`: segment;
- rank `3`: `P=I`, the standard simplex.

The Hume sharp family is rank `2`. The script checks `t=1/10,1/20,1/50` with
`delta=t^2`, `rho=t`; both endpoint vertices are in `W`, and hull error is `0`.

### Simplex row polytopes

The segment estimate extends to simplex row polytopes. If `v` is a simplex
vertex and `lambda_v` its barycentric coordinate, then `h=1-lambda_v` vanishes
at `v`, lies in `[0,1]`, and satisfies

```text
||x-v||_1 <= D h(x),        D=max_a ||r^a-v||_1 <= 2+4delta.
```

So every simplex vertex is in `W` for `kappa<=C tau/4`, and the hull error is
`0`. This covers `n=4` rank `1`, rank `2`, rank `4`, and rank `3` cases whose
row polytope is not a genuine quadrilateral.

## Exact n=4 Quadrilateral Family

The first non-simplex small geometry is a corank-one `4x4` quadrilateral. For
`0<t<=1/4`, set

```text
v=(1-t^2, t^2, -1+t^2, -t^2),
u=(1, 0, -t^2/(1-t^2), 0),
P_t=I-u v^T.
```

SymPy verifies:

```text
sum_j v_j=0        =>        P_t 1=1,
v^T u=1            =>        P_t^2=P_t.
```

Explicitly,

```text
P_t =
[ t^2,  -t^2,              1-t^2,   t^2             ]
[ 0,     1,                0,       0               ]
[ t^2,   t^4/(1-t^2),      1-t^2,  -t^4/(1-t^2)     ]
[ 0,     0,                0,       1               ].
```

The row negative mass is `delta=t^2`. The affine circuit is

```text
(1-t^2)p_0 + t^2 p_1 = (1-t^2)p_2 + t^2 p_3.
```

For `0<t<=1/4`,

```text
||p_0-p_2||_1 = 2t^2/(1-t^2) < t,
```

while the other relevant distances exceed `t`. At `rho=t`, the outside sets
for `p_0` and `p_2` omit the close mate.

Affine value assignments satisfying the circuit relation:

```text
p_0:  (0, 1, 0, 1)                         gives e_{p_0}(t) >= 1
p_2:  (0, 1, 0, 1)                         gives e_{p_2}(t) >= 1
p_1:  (1, 0, 1-t^2, 1-t^2)                 gives e_{p_1}(t) >= 1-t^2
p_3:  (1-t^2, 1-t^2, 1, 0)                 gives e_{p_3}(t) >= 1-t^2
```

Hence all four vertices lie in `W_{t,kappa}` for any `kappa<=1-t^2`, and
`dist_1(p_i,conv W)=0` for every row.

LP/Gurobi checks:

```text
t=1/10:  min e/tau = 9.9     Gurobi objective for p_1 = 0.99
t=1/20:  min e/tau = 19.95
t=1/50:  min e/tau = 49.98
```

This is not a counterexample. It is a reference problem showing that a small
negative-mass quadrilateral can be much better exposed than the square-root
threshold.

## Remaining n=4 Gap

Every arbitrary rank-`3`, `n=4` case has the corank-one form

```text
P=I-u v^T,        sum_j v_j=0,        v^T u=1,
```

and affine dependence

```text
sum_i v_i p_i=0.
```

If the signs of `v` split as `1|3` or `3|1`, one row lies in the triangle of
the other three, so the simplex certificate applies. The only non-simplex case
is the `2|2` sign pattern.

Candidate formalisable lemma:

```text
For n=4, P=I-u v^T, neg(p_i)<=delta, and v having a 2|2 sign pattern,
either the quadrilateral is O(sqrt(delta))-close to a simplex/segment hull,
or all four vertices satisfy e_v(C sqrt(delta)) >= c sqrt(delta).
```

The likely input is the rank-one-defect inequality package from
`agent-B/notes/rank-one-classical-stability.md`: after normalising `v`, row
negative mass permits at most one positive-active and one negative-active
coordinate of `u`; inactive rows are `O(sqrt(delta))` perturbations of basis
rows.

## Handoff

Small dimensions do not suggest a counterexample to `op-exposed-hull`. They
suggest a proof mechanism: a non-simplex quadrilateral requires a balanced
affine circuit, and the signed-retraction negative-mass inequalities should
force either collapse to a simplex at `O(sqrt(delta))` scale or exposedness of
every remaining vertex.

Next concrete step: solve the general `n=4` corank-one `2|2` LP symbolically in
circuit coordinates and extract the inequality behind the explicit `P_t`
value assignments.
