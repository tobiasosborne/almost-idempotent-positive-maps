# Exposed-Circuit Cancellation Lemma

This note extracts the proved part of the exposed-or-redundant classical
projection-stability route. It is a theorem-level lemma, not a conjectural
step.

The open part remains the exposed-or-redundant dichotomy in
`agent-B/notes/exposed-redundant-dichotomy-target.md`.

## Setup

Let `P` be an `n x n` real matrix with

```text
P1=1,        P^2=P.
```

Write `p_i` for the rows, viewed as signed probability vectors, and assume

```text
neg(p_i)=sum_j max(-p_i(j),0) <= delta
```

for every row. Let

```text
K=conv{p_i}.
```

For a signed probability `mu`, write `mu=mu^+-mu^-` and
`neg(mu)=||mu^-||_1`.

## One Well-Exposed Row Concentrates

Let `v` be a row of `P`. Suppose there are constants `rho,kappa>0` and an
affine function

```text
h:K->[0,1]
```

such that

```text
h(v)=0,
h(x)>=kappa        whenever ||x-v||_1>=rho.
```

Set

```text
U_v={j: ||p_j-v||_1<rho}.
```

Then there is a probability measure `pi_v` supported on `U_v` with

```text
||v-pi_v||_1 <= C(delta/kappa + delta).          (1)
```

### Proof

Since `P^2=P`, every row is fixed by right multiplication by `P`:

```text
vP=sum_j v_j p_j=v.
```

Applying the affine function `h` gives

```text
sum_j v_j h(p_j)=h(v)=0.
```

Decompose `v=v^+-v^-`. Because `0<=h<=1`,

```text
sum_j v^+_j h(p_j)
 = sum_j v^-_j h(p_j)
 <= neg(v)
 <= delta.
```

On `U_v^c`, the exposedness hypothesis gives `h(p_j)>=kappa`, hence

```text
v^+(U_v^c) <= delta/kappa.                       (2)
```

First dispose of the large-error case. Let

```text
b=v^+(U_v^c),        c=neg(v).
```

If `b+c>=1/4`, choose any probability measure supported on `U_v`; such a
measure exists because `v` itself is one of the rows, say `v=p_i`, and then
`i in U_v`. Since `||v||_1<=1+2delta`, the bound `(1)` is trivial after
increasing `C`.

Assume now that `b+c<1/4`. Then

```text
||v^+|_{U_v}||_1=1+c-b >= 3/4,
```

so we may define

```text
pi_v = v^+|_{U_v} / ||v^+|_{U_v}||_1.
```

The standard signed-measure truncation estimate gives

```text
||v-pi_v||_1
 <= 2(neg(v)+v^+(U_v^c))
 <= C(delta+delta/kappa).
```

This proves `(1)`.

## Exposed-Circuit Cancellation

Let `C_ec` be the universal constant implicit in the one-row estimate above.

Let `A` be a finite label set. Suppose rows `v_a` of `P`, indexed by
`a in A`, satisfy:

1. the row points are pairwise separated:

   ```text
   ||v_a-v_b||_1 >= 2rho        (a!=b);
   ```

2. each `v_a` has an exposing function `h_a:K->[0,1]` with

   ```text
   h_a(v_a)=0,
   h_a(x)>=kappa        whenever ||x-v_a||_1>=rho.
   ```

Then for every `a` there is a probability measure `pi_a` supported on

```text
U_a={j: ||p_j-v_a||_1<rho}
```

such that

```text
||v_a-pi_a||_1 <= C(delta/kappa+delta),          (3)
```

and the supports `U_a` are pairwise disjoint. Consequently, for all real
coefficients `c_a`,

```text
||sum_a c_a v_a||_1
 >= (1-C_ec(delta/kappa+delta)) sum_a |c_a|.     (4)
```

### Proof

The probability measures `pi_a` and estimate `(3)` follow from the one-row
lemma. If some index `j` belonged to both `U_a` and `U_b`, then

```text
||v_a-v_b||_1
 <= ||v_a-p_j||_1 + ||p_j-v_b||_1
 < 2rho,
```

contradicting the separation hypothesis. Thus the supports are disjoint.

Since the `pi_a` are probability measures on disjoint supports,

```text
||sum_a c_a pi_a||_1=sum_a |c_a|.
```

The triangle inequality and `(3)` give

```text
||sum_a c_a v_a||_1
 >= ||sum_a c_a pi_a||_1 - sum_a |c_a| ||v_a-pi_a||_1
 >= (1-C_ec(delta/kappa+delta)) sum_a |c_a|.
```

This proves `(4)`.

## Square-Root Corollary

Set `tau=sqrt(delta)`. If `kappa>=c tau`, then

```text
delta/kappa+delta <= C_c tau,
```

so `(4)` becomes

```text
||sum_a c_a v_a||_1
 >= (1-C_c tau) sum_a |c_a|.                    (5)
```

For sufficiently small `delta`, the rows `v_a` are therefore linearly
independent in the strongest possible `l1` sense. In particular, they cannot
participate in a nontrivial exact affine circuit

```text
sum_a c_a v_a=0,        sum_a c_a=0,
```

unless all `c_a=0`.

## Role In The Classical Program

This lemma proves that well-exposed, separated vertices cannot be the source
of a non-simplex row polytope at small defect. Therefore the remaining
non-simplex obstruction must come from vertices that are not well exposed at
scale `sqrt(delta)`.

The missing theorem is precisely the dichotomy:

```text
not well exposed  =>  O(sqrt(delta))-redundant/mergeable.
```

If that dichotomy is proved dimension-free, this cancellation lemma combines
with `agent-B/notes/robust-approximate-simplexity-reduction.md` to prove the
classical square-root projection-stability theorem.
