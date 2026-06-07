# Subagent: Step 2 Top-Face Exposure Test

Date: 2026-06-07.  Lane: Agent B sandbox.  Status: exploratory lemma note,
not a canonical proof shard.

## Verdict

This step is proved as a deterministic convex lemma.  It does not use
`P^2=P`, repaired coordinates, or quasi-closedness.  Its only job is to turn a
global separator gap around a top row vertex into the project definition of a
`(rho,kappa)`-exposed vertex.

The important normalization point is:

```text
raw l_infty/l1 separator gap gamma
  -> exposedness threshold gamma / (2+4 delta)
```

when the affine functional has linear part of `l_infty` norm at most `1`.
Equivalently, if the gap is measured as a fraction of the actual oscillation of
the affine functional on the row polytope, no `2+4 delta` loss is needed.

One hypothesis is essential: the chosen row `u` must be a global maximum of the
affine functional on the whole row set, not merely a maximum inside a selected
bad subset.  If some nearby row has larger affine value, the function
`phi(u)-phi` is negative there and cannot be the required exposing function
`h:K->[0,1]` with `h(u)=0`.

## Setup

Let the rows be signed probability vectors `p_i` with

```text
sum_l p_i(l)=1,       neg(p_i)<=delta.
```

Then

```text
||p_i||_1 = 1 + 2 neg(p_i) <= 1+2 delta,
diam_1({p_i}) <= 2+4 delta.                  (D)
```

Let `K=conv{p_i}`.  Let `u=p_a` be a row vertex.  Let

```text
phi(x)=<g,x>+b
```

be affine on the ambient row space, and suppose

```text
||g||_infty <= Lambda,
phi(u)=max_i phi(p_i).                       (TOP)
```

The top condition implies `phi(u)=max_K phi`, since `K` is the convex hull of
the rows.

## Lemma A: raw l_infty-normalized gap

Assume `Lambda>0` and that every row outside the `l1` `rho`-ball around `u`
satisfies

```text
phi(u)-phi(p_i) >= gamma
whenever ||p_i-u||_1 >= rho.                 (G)
```

Then `u` is `(rho, gamma/(Lambda(2+4 delta)))`-exposed.

In particular, for the distance-dual normalization `||g||_infty<=1`,

```text
e_u(rho) >= gamma/(2+4 delta).
```

If also `delta<=1/4`, then `2+4 delta<=3`, so

```text
e_u(rho) >= gamma/3.
```

For the usual small-defect regime `delta<=1/16`, the sharper denominator is
`2+4 delta<=9/4`, but the constant `3` is cleaner and safer.

## Proof

By `(TOP)` and `(D)`, for every row `p_i`,

```text
0 <= phi(u)-phi(p_i)
   = <g,u-p_i>
  <= Lambda ||u-p_i||_1
  <= Lambda(2+4 delta).
```

Define

```text
h(x) = (phi(u)-phi(x)) / (Lambda(2+4 delta)).
```

Then `h` is affine, `h(u)=0`, and `0<=h(p_i)<=1` for every row.  Since `K` is
the convex hull of the rows, `0<=h<=1` on all of `K`.

For every row with `||p_i-u||_1>=rho`, assumption `(G)` gives

```text
h(p_i) >= gamma/(Lambda(2+4 delta)).
```

This is exactly the definition of a `(rho,kappa)`-exposed row vertex with
`kappa=gamma/(Lambda(2+4 delta))`.

If there are no rows outside the `rho`-ball, the lower-bound condition is
vacuous; the same `h` works, and the exposedness constraint has no outside row
to test.  The canonical modulus convention for an empty minimum should be fixed
before formalization, but the existence-form definition is harmless.

## Lemma B: oscillation-normalized gap

Let

```text
Omega = max_i phi(p_i) - min_i phi(p_i).
```

If `Omega>0`, `(TOP)` holds, and every outside row satisfies

```text
phi(u)-phi(p_i) >= kappa Omega
whenever ||p_i-u||_1 >= rho,
```

then `u` is `(rho,kappa)`-exposed.

Proof: use

```text
h(x) = (phi(u)-phi(x))/Omega.
```

This is the same argument with the exact row oscillation replacing the coarse
diameter bound.  This version is best for conceptual statements; Lemma A is
best for constants coming from the `l_infty` distance dual.

## Candidate contract

```text
lem-top-face-exposure-test:
Let X={p_i} be signed probability rows with neg(p_i)<=delta and let
K=conv X.  Let u in X be a row vertex.  If an affine functional
phi(x)=<g,x>+b satisfies ||g||_infty<=1, phi(u)=max_X phi, and
phi(u)-phi(p_i)>=gamma for every row with ||p_i-u||_1>=rho, then u is
(rho,gamma/(2+4delta))-exposed.  Consequently, for delta<=1/4, a raw gap
gamma>=3 kappa implies u is (rho,kappa)-exposed.
```

This is af-sized: row diameter, affine normalization, definition unfolding.

## What feeds Step 3

The useful output for the shadow-edge step is the contrapositive.

Suppose `||g||_infty<=1`, `phi(u)=max_X phi`, and `u` is not
`(rho,kappa)`-exposed.  Then there must exist a row `p_j` with

```text
||p_j-u||_1 >= rho,
phi(u)-phi(p_j) < (2+4 delta) kappa.          (shadow row)
```

For `delta<=1/4`, this is the simpler bound

```text
phi(p_j) > phi(u) - 3 kappa.
```

Thus a non-exposed global top vertex produces a `rho`-separated row that is
still high in the same separator direction.  This is exactly the deterministic
input needed for Step 3.  Step 3 must then prove that this shadow row or a
barycentric witness remains in the bad/high region; that part uses the
separator margin from `conv(R0)` and the constant hierarchy `D >> k`.

## Constants

Use the following translation table.

```text
raw gap gamma, ||g||_infty<=1:
  exposed threshold = gamma/(2+4delta)

target exposed threshold kappa_exp:
  require raw gap gamma >= (2+4delta) kappa_exp

small-defect safe version delta<=1/4:
  require raw gap gamma >= 3 kappa_exp

oscillation-normalized gap:
  require gap >= kappa_exp * osc_X(phi)
```

In the global route, if `kappa_exp=k tau`, the Step 3 shadow row has height
drop `<(2+4delta)k tau`, safely `<3k tau` for `delta<=1/4`.

## Failure modes

1. If `u` is only maximal in a bad subset, the lemma can fail: higher rows
   outside that subset make `phi(u)-phi` negative, so the exposing function is
   not `[0,1]`-valued.
2. If a higher row lies within the `rho`-cluster of `u`, the outside-gap
   condition alone is still insufficient for exposing `u`; choose a global top
   row in the cluster or add a separate local tie-breaking lemma.
3. The lemma proves exposure of a row vertex.  If the separator maximum is
   attained at a non-vertex row, pass first to a row vertex in the same top
   face.
4. This step does not prove that the shadow row is bad, quasi-closed, or
   recurrent.  Those are Step 3 and Step 4 obligations.

## Next handoff

Step 3 should use the contrapositive with the raw-drop bound
`(2+4delta)kappa`.  A clean Step 3 contract should say:

```text
If a global separator-top bad vertex u is not (rho,kappa)-exposed, then there
is a row p_j with ||p_j-u||_1>=rho and phi(p_j)>phi(u)-(2+4delta)kappa.
Under the bad-hull separator margin, p_j remains in the high bad slice.
```

The first sentence is exactly this Step 2 lemma.  The second sentence is the
new work for Step 3.
