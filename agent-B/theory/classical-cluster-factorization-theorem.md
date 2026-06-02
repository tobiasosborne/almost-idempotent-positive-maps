# Classical Cluster Factorization Theorem

This note packages the latest classical projection-stability special case as
an exact positive/JB factorization theorem for commutative channels.

It is a genuine theorem under an explicit row-polytope geometry hypothesis on
the spectral idempotent. It is not the full dimension-free Markov theorem.

## Setup And Convention

Let `Q` be an `n x n` row-stochastic matrix, acting on `ell_infty^n` by

```text
(Tf)(i)=sum_j Q_{ij} f(j).
```

The operator norm `ell_infty -> ell_infty` is the maximum row `l1` norm, and

```text
||Q^2-Q||_{infty->infty}
```

is the maximum `l1` distance between the one-step and two-step row laws.

## Cluster Geometry Hypothesis

Let

```text
eta = ||Q^2-Q||_{infty->infty}
```

and define the spectral idempotent

```text
P=theta(2Q-I).
```

Write `p_i` for the rows of `P`.

Assume that the rows of `P` satisfy the cluster-representative hypotheses of
`agent-B/notes/cluster-representative-classical-stability.md` with

```text
delta=C eta,
rho <= C0 sqrt(eta),
gamma <= C0 sqrt(eta),
kappa >= c0 sqrt(eta),
```

where `delta` is the row negative-mass bound for `P`.

Concretely, this means there are representative row vertices

```text
r^1,...,r^m
```

which are pairwise separated at scale `rho`, well exposed with gap `kappa`
outside their `rho`-clusters, and every non-cluster row is within `gamma` of
the convex hull of the representatives.

## Theorem

There are constants `eta0,C` depending only on `C0,c0` such that, if
`eta<=eta0` and the cluster geometry hypothesis holds, then there exist:

- a finite-dimensional commutative special JB algebra `J`;
- unital positive maps

```text
Delta:J -> ell_infty^n,        Upsilon:ell_infty^n -> J
```

such that

```text
||Delta Upsilon - Q||_{infty->infty} <= C sqrt(eta),
Upsilon Delta = id_J,
Upsilon(Delta x . Delta y)=x*y        (x,y in J).
```

Here `.` is pointwise multiplication on `ell_infty^n`, and `*` is the JB
product of `J`.

## Proof

First record the spectral reduction. Set `S=2Q-I`. Since `Q` is
row-stochastic,

```text
||Q||_{infty->infty}=1,        Q1=1.
```

Moreover

```text
S^2-I=4(Q^2-Q),
```

so for `eta0` small the Banach-algebra formula

```text
sgn(S)=S(S^2)^(-1/2),        P=(I+sgn(S))/2
```

gives

```text
P^2=P,        P1=1,        ||P-Q||_{infty->infty}<=C eta.
```

Thus every row `p_i` has total mass `1`. Since the corresponding row `q_i` of
`Q` is a probability vector and

```text
||p_i-q_i||_1 <= C eta,
```

the negative mass of every `p_i` is at most `C eta`. This is the `delta=C eta`
used in the cluster geometry hypothesis.

Apply
`agent-B/notes/cluster-representative-classical-stability.md` to `P`. It gives
a row-stochastic idempotent matrix `E` with

```text
||E-P||_{infty->infty}
 <= C(rho+gamma+delta/kappa+delta)
 <= C sqrt(eta).
```

Therefore

```text
||E-Q||_{infty->infty}
 <= ||E-P||_{infty->infty}+||P-Q||_{infty->infty}
 <= C sqrt(eta).
```

Now set

```text
J=E(ell_infty^n).
```

Because `E` is a unital positive idempotent on the commutative C*-algebra
`ell_infty^n`, the exact Effros-Stormer/Choi-Effros construction gives `J` a
finite-dimensional commutative special JB product

```text
x*y=E(x.y),        x,y in J,
```

with positive cone equal to the inherited cone

```text
J_+=J cap (ell_infty^n)_+.
```

Define

```text
Delta:J -> ell_infty^n,        Delta(x)=x,
Upsilon:ell_infty^n -> J,      Upsilon(f)=E(f).
```

Both maps are unital and positive. Also

```text
Upsilon Delta=id_J,
Delta Upsilon=E,
```

so

```text
||Delta Upsilon-Q||_{infty->infty}=||E-Q||_{infty->infty}
 <= C sqrt(eta).
```

Finally, for `x,y in J`,

```text
Upsilon(Delta x . Delta y)
 = E(x.y)
 = x*y
```

by definition of the product. This proves the theorem.

## Corollary: Global Exposed-Hull Hypothesis

The cluster geometry hypothesis may be replaced by the global exposed-hull
hypothesis from `agent-B/notes/simultaneous-skeleton-reduction.md`.

Let `P=theta(2Q-I)` and let `K=conv{p_i}` be its row polytope. For a row
vertex `v`, define `e_v(rho)` as in
`agent-B/notes/exposed-redundant-dichotomy-target.md`, and set

```text
W_{rho,kappa}={row vertices v : e_v(rho)>=kappa}.
```

Assume that for some constants `C0,c0`,

```text
rho<=C0 sqrt(eta),        kappa>=c0 sqrt(eta),
```

and every row satisfies

```text
dist_1(p_i, conv W_{rho,kappa})<=C0 sqrt(eta).
```

Then the same exact positive/JB factorization conclusion holds.

Indeed, choose a maximal `4rho`-separated subset

```text
R={r^1,...,r^m} subset W_{rho,kappa}.
```

Every point of `conv W_{rho,kappa}` is within `4rho` of `conv R`, and each
representative remains exposed with gap `kappa` outside its `2rho`-cluster.
Thus `R` satisfies the cluster-representative hypotheses with cluster radius
`2rho` and reconstruction error `C sqrt(eta)`. The theorem applies.

## Role In The Main Program

This theorem is the commutative exact-factorization analog of theorem C under
a checkable geometric hypothesis on the spectral idempotent. It shows that
the classical cluster-representative work is not merely row-polytope geometry:
it already gives exact positive factor maps through a commutative special JB
algebra for a nontrivial class of almost-idempotent positive maps.

The full commutative projection-stability theorem would remove the cluster
geometry hypothesis. By the corollary, it is enough to prove the global
exposed-hull lemma for nearly positive signed affine retractions.
