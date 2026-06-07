# Subagent Step 2: Top-Face Exposure Test

Date: 2026-06-07. Lane: Agent B sandbox. Status: proof-ready exploratory
lemma, not a canonical proof shard.

## Verdict

The top-face exposure test is easy and proof-ready.  The only bookkeeping is
normalization: a separator `phi` whose oscillation on the row set is `M_phi`
gives exposedness gap equal to the outside `phi`-drop divided by `M_phi`.

In the usual `l_infty`-dual separator normalization,

```text
M_phi <= diam_1(K) <= 2+4delta.
```

Thus an outside `phi`-drop of `(2+4delta)kappa` proves
`e_u(rho)>=kappa`.  If `phi` is already normalized to take values in an
interval of length at most `1`, an outside drop of `kappa` is enough.

## Setup

Rows are `x_i=p_i`, with

```text
P1=1,        P^2=P,        neg(p_i)<=delta.
```

Let `K=conv{x_i}`.  For a row vertex `u=x_a` and scale `rho`, set

```text
S_u(rho)={i : ||x_i-u||_1 >= rho}.
```

The exposedness modulus is

```text
e_u(rho)=sup_h min_{i in S_u(rho)} h(x_i),
```

where `h` ranges over affine functions with

```text
h(u)=0,        0<=h(x_i)<=1        for all rows i.
```

Let `phi` be an affine functional and assume `u` is `phi`-maximal on all rows:

```text
phi(u)=max_i phi(x_i).
```

Define the row oscillation below `u`:

```text
M_phi=max_i (phi(u)-phi(x_i)).
```

## Candidate Contract

```text
lem-top-face-exposure:
Let u be a row vertex maximizing an affine functional phi on the row set.
Assume M_phi>0 and that every row outside the rho-ball around u satisfies

  phi(u)-phi(x_i) >= Delta_phi.

Then

  e_u(rho) >= Delta_phi/M_phi.

In particular, if the linear part of phi has l_infty norm <=1, then
M_phi<=2+4delta and

  Delta_phi >= (2+4delta)kappa
    => e_u(rho)>=kappa.
```

If `M_phi=0`, then all rows have the same `phi` value and the hypothesis can
hold only with `Delta_phi=0`; the lemma is vacuous.

## Proof

Since `u` maximizes `phi`, every row satisfies

```text
0 <= phi(u)-phi(x_i) <= M_phi.
```

For `M_phi>0`, define

```text
h(x)=(phi(u)-phi(x))/M_phi.
```

Then `h` is affine on `aff(K)`, `h(u)=0`, and `0<=h(x_i)<=1` for every row.
For every `i in S_u(rho)`,

```text
h(x_i) >= Delta_phi/M_phi.
```

Therefore this single admissible `h` witnesses

```text
e_u(rho)>=Delta_phi/M_phi.
```

If the linear part of `phi` has `l_infty` norm at most `1`, then

```text
|phi(x_i)-phi(x_j)| <= ||x_i-x_j||_1.
```

Each row has `l1` norm

```text
||x_i||_1=1+2neg(x_i)<=1+2delta,
```

so

```text
diam_1(K)<=2+4delta,
M_phi<=2+4delta.
```

This gives the stated quantitative corollary.

## Constants

For `delta<=1/16`,

```text
2+4delta <= 9/4.
```

For `delta<=1/4`,

```text
2+4delta <= 3.
```

Thus Step 3's height-loss constant and Step 2's exposure-normalization
constant are the same row-diameter factor.

## Failure Modes

1. If `u` is not a true maximizer over all rows under consideration, the
   normalized `h` may be negative on a higher row and is not admissible.
2. If `phi` is only a distance separator from `conv R0`, its oscillation is
   controlled by row diameter, not by `1`; the outside gap must be scaled by
   `2+4delta`.
3. The lemma proves exposedness only for a top vertex with a genuine gap to
   all outside-`rho` rows.  If there is a high outside row, Step 3 supplies the
   shadow edge instead.

## Next Handoff

Step 3 should use the contrapositive with the normalized test

```text
h=(phi(u)-phi)/M_phi
```

to obtain a row or barycenter outside the `rho`-ball with height loss at most
`M_phi kappa <= (2+4delta)kappa`.
