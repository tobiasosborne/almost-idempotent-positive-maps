# Subagent A - LP-dual attack on op-exposed-hull

Date: 2026-06-07.  Lane: Agent B exploration sandbox.  Status: scratch note,
not a canonical proof.

## Verdict

Inconclusive.  The LP duals are clean.  The obstruction is also clear: failed
exposedness gives a signed affine circuit with small positive mass, but the
dual leaves large negative coefficients uncontrolled.  A proof still needs a
dimension-free way to combine those circuits with `P^2=P` and
`neg(p_i)<=delta`.

## Normalization

Rows are `x_i=p_i`, with `P1=1`, `P^2=P`, `neg(x_i)<=delta`, and
`tau=sqrt(delta)`.  Let `K=conv{x_i}`.  For a row vertex `v=x_a`, set
`S_v(rho)={i : ||x_i-v||_1>=rho}` and
`H_v={h affine on aff(K) : h(v)=0, 0<=h(x_i)<=1 for all i}`.  Then
`e_v(rho)=max_{h in H_v} min_{i in S_v(rho)} h(x_i)`.  For `rho=R tau` and
`kappa=k tau`, let `W=W_{rho,kappa}` be the vertices with
`e_w(rho)>=kappa`.  The target is `dist_1(x_i,conv W)<=A tau`.

## LP 1: exposedness

Primal: maximize `t` over affine `h` with `h(v)=0`, `0<=h(x_i)<=1` for all
rows, and `h(x_i)>=t` for `i in S_v(rho)`.

Finite minimax gives

```text
e_v(rho)=min_{mu in Delta(S_v)} G_v(y_mu),
y_mu=sum_{i in S_v} mu_i x_i,
G_v(y)=sup_{h in H_v} h(y).
```

Write `z_i=x_i-v`, `z_y=y-v`.  The LP for `G_v(y)` is to maximize
`ell(z_y)` subject to `0<=ell(z_i)<=1`.  Farkas dual:

```text
minimize    sum_i beta_i
variables   alpha_i,beta_i >= 0
subject to  z_y = sum_i (beta_i-alpha_i) z_i.
```

Hence `e_v(rho)<kappa` iff there are `mu in Delta(S_v)` and
`alpha,beta>=0` such that

```text
sum_i beta_i < kappa,
sum_{j in S_v} mu_j (x_j-v)
  = sum_i (beta_i-alpha_i)(x_i-v).          (E-dual)
```

This is the first useful output: non-exposedness is a small-positive-mass
signed row-difference circuit.

## LP 2: distance to the exposed hull

Primal distance to `conv W`: minimize `sum_l r_l` subject to `lambda_w>=0`,
`sum_w lambda_w=1`, `r_l>=0`, and
`-r_l <= v_l - sum_w lambda_w w_l <= r_l`.  Dual separator:

```text
d_W(v)=max phi(v)-s
subject to ||phi||_infty<=1,        phi(w)<=s for w in W.
```

Thus `d_W(v)>A tau` yields a `phi` with

```text
phi(v) >= sup_{w in W} phi(w) + A tau.     (D-dual)
```

Constants may be added to `phi`, since all rows have coordinate sum `1`.

## Combined attempt

Assume `d_W(v)>A tau`.  Let `phi` be a separator and choose a row vertex `u`
maximizing `phi` over all rows.  Then `u notin W`.  Define
`h_u(x)=(phi(u)-phi(x))/2`.  Because `||phi||_infty<=1`, `h_u in H_u`.
Since `u notin W`, minimax gives `y in conv{x_i : ||x_i-u||_1>=rho}` with

```text
h_u(y)<kappa,        phi(y)>phi(u)-2kappa.       (1)
```

If `A>4k`, then `y` remains separated from `conv W` in the same direction:

```text
phi(y) > sup_W phi + (A-2k)tau.
```

So at least one row outside the `rho`-cluster of `u` is still far from
`conv W` in the separator direction.  This creates a high-value separated
edge, not a contradiction.  The missing ingredient is a no-cycle or
contraction principle for these high non-exposed rows.

## Input from `P^2=P`

Right-fixity gives `v = vP = sum_j v_j x_j`.  With `v=v^+-v^-` and
`c=neg(v)<=delta`,

```text
v=(1+c)q_vP-c r_vP,
q_v=v^+/(1+c),        r_v=v^-/c.
```

Since every row has `l1` norm at most `1+2delta`,

```text
dist_1(v, conv{x_j : v_j>0}) <= C delta.         (2)
```

This is the main non-convex-geometry fact: each row is very close to the hull
of its positive-support successors.  It does not yet imply closeness to
`conv W`.

## Candidate lemmas

A1, dual circuit lemma - derived above: `e_v(rho)<kappa` gives `(E-dual)` with
`beta` mass `<kappa`.

A2, separator propagation - derived above: `d_W(v)>A tau` and `A>4k` give a
separator-high row outside a `rho`-neighborhood of a separator-maximal
non-exposed row.

A3, closed-component exposed vertex - unproved: every closed positive-support
component contains `w` with `e_w(R tau)>=k tau`, or the component is
`O(tau)`-close to `conv W`.

A4, no small-positive-mass non-exposed cycle - unproved: the circuits
`(E-dual)` around a separator-high cycle contradict `neg(p_i)<=delta` when
`R` is large and `k` is small.

A5, global LP certificate - unproved: the joint system `(D-dual)` + failed
exposedness duals for all rows with height `> sup_W phi+4k tau` + `P^2=P` +
`neg rows<=delta` is infeasible.

## Constants to test

Current hierarchy:

```text
rho=R tau,        kappa=k tau,        A>=16k+8,        R>=8A.
```

Only `A>4k` is used above.  The `R>>A` gap is reserved for a future no-cycle
argument.

## Failure modes

1. Local LP duality reconstructs by other non-exposed rows, not by `conv W`.
2. `sum beta_i` is controlled, but `sum alpha_i` is not.
3. Separator propagation can cycle along a flat high face.
4. Right-fixity gives positive-support reconstruction, but positive-support
   components might contain no presently known well-exposed vertex.
5. A pure LP proof ignoring coordinate signs is too weak; this is exactly the
   regular-polygon warning.

## Next handoff

Build the joint feasibility LP/MILP for A5 at small `n`, searching for
`P1=1`, `P^2=P`, `neg rows<=delta`, some row far from `conv W`, and all
separator-high rows failing exposedness.

If infeasible certificates appear, extract dual multipliers and compare them
with A3/A4.  If feasible examples appear, export them under
`agent-B/experiments/op-exposed-hull/`.
