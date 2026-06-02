# Sidecar: Classical sqrt near-positive projection stability

## Target

Wanted theorem:

Let `P: ell_infty^n -> ell_infty^n` be real, unital, and idempotent.  In
matrix language the rows of `P` have sum `1` and `P^2=P`.  Assume each row
`mu_i` has negative mass

```text
neg(mu_i) = sum_j max(-mu_i(j),0) <= delta.
```

Then there should be a row-stochastic idempotent `E` with

```text
||P-E||_{inf->inf} = max_i ||P_i-E_i||_1 <= C sqrt(delta)
```

with universal `C`.  Hume's `3 x 3` family in
`agent-B/notes/subagent-classical-projection-stability.md` shows the exponent
`1/2` is sharp.

## What I could prove

I did not prove the theorem.  I did prove a clean reduction to an equivalent
Markov-kernel perturbation statement, with explicit constants.

### Reduction to stochastic almost-idempotents

For each signed row `mu_i` of `P`, write

```text
a_i = neg(mu_i) <= delta,
q_i = mu_i^+ / (1+a_i).
```

Then `q_i` is a probability vector and

```text
||mu_i-q_i||_1 = 2 a_i <= 2 delta.
```

Let `Q` be the row-stochastic matrix with rows `q_i`.  Since

```text
||P||_{inf->inf} <= 1+2 delta,
||Q-P||_{inf->inf} <= 2 delta,
||Q||_{inf->inf}=1,
```

and `P^2=P`, we get

```text
Q^2-Q = (Q-P)Q + P(Q-P) - (Q-P),
```

hence

```text
||Q^2-Q||_{inf->inf}
  <= 2 delta + (1+2 delta) 2 delta + 2 delta
  = 6 delta + 4 delta^2.
```

Therefore the desired theorem follows from the following Markov theorem.

### Markov sqrt stability theorem sufficient for the target

There are universal constants `eta0,C_M` such that if `Q` is an `n x n`
row-stochastic matrix and

```text
||Q^2-Q||_{inf->inf} <= eta <= eta0,
```

then there is a row-stochastic idempotent `E` with

```text
||Q-E||_{inf->inf} <= C_M sqrt(eta).
```

Indeed, for `delta <= 1`,

```text
||P-E|| <= ||P-Q|| + ||Q-E||
        <= 2 delta + C_M sqrt(6 delta + 4 delta^2)
        <= (2 + sqrt(10) C_M) sqrt(delta).
```

Thus any dimension-free proof of this Markov theorem proves the desired
near-positive idempotent theorem.

## Converse reduction

The two formulations are also essentially equivalent.

Assume the near-positive idempotent theorem.  Let `Q` be row-stochastic and
`eta`-idempotent.  In the Banach algebra of matrices with operator norm
`ell_infty -> ell_infty`, functional calculus for

```text
theta(2Q-I)
```

gives a real unital idempotent `P` with

```text
||P-Q||_{inf->inf} <= K eta
```

for `eta < 1/4`, with universal `K` from the standard spectral separation
estimate.  Since `Q` is stochastic, each row of `P` has negative mass at most
`K eta / 2`.  Applying the near-positive theorem to `P` gives a stochastic
idempotent `E` with

```text
||Q-E|| <= K eta + C sqrt(K eta / 2) = O(sqrt(eta)).
```

So proving the original theorem is equivalent, up to constants, to proving
dimension-free sqrt stability of almost-idempotent stochastic matrices.

## Literature search result

I found exact structural/classification sources, but not the needed
quantitative perturbation theorem.

- Blackwell, "Idempotent Markoff chains", Annals of Mathematics 43(3), 1942,
  pp. 560-567.  The online abstract explicitly studies kernels satisfying
  `P_2(x,E)=P(x,E)`, i.e. idempotent Markov kernels.
- Kim, "Two classification theorems of states of Markov chains", Journal of
  Applied Probability 7(2), 1970, pp. 490-496, says it reproves the standard
  recurrent/transient classification and the corresponding classification for
  idempotent Markov chains due to Doob.
- Kitaev's local source
  `agent-B/references/kitaev-2405.02434/approximate_algebras.tex` notes that
  for eta-idempotent UCP maps the positive idempotent approximation problem at
  dimension-free scale is open, even though his algebraic/factorization theorem
  gives a different `O(eta)` output.

I did not locate a theorem of the form

```text
dist(Q, {stochastic idempotents}) <= C sqrt(||Q^2-Q||)
```

in Markov-chain perturbation literature.  Search terms checked included
`nearly idempotent stochastic matrix`, `almost idempotent stochastic matrix`,
`Q^2-Q idempotent stochastic`, `idempotent Markov chains`, and near-contractive
projection variants for `C(K)`/`ell_infty`.

## Proof-route diagnosis

The reduction above is tight enough for the project, but the Markov theorem is
not immediate from standard ergodic projection.  For example, if

```text
Q = [[1-a,a],[a,1-a]]
```

with small `a`, then `||Q^2-Q||=O(a)`, while the Cesaro limit has both rows
`(1/2,1/2)` and is distance `O(1)` from `Q`.  The correct nearby idempotent is
the identity.  Thus a proof must choose metastable classes, not the actual
ergodic projection of `Q`.

The exact idempotent classification suggests the right construction should
cluster rows/classes at scale `sqrt(eta)`: states connected only by leakage
`O(eta)` must be split, while states whose rows are indistinguishable at the
`sqrt(eta)` scale should be collapsed into a recurrent class.  Hume's example
is exactly the boundary case where a new class separates at first order while
the stochastic/idempotency defect is second order.

## Current status

No proof of the sharp theorem was obtained in this sidecar.  The strongest
usable deliverable is the equivalence:

```text
near-positive idempotent sqrt stability
  <=> almost-idempotent stochastic matrix sqrt stability
```

with explicit constants in the forward reduction.  This is a clean target for
Agent B: prove the Markov theorem above, or find it in the literature.
