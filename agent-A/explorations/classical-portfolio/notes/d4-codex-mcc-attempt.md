I can’t honestly mark MCC as proved. I also do not see a refutation. The current state is: the recursion lemmas are provable, the numerics strongly support the cost, but the proof still needs one sharp projection-constant inequality.

**PROVED Reductions**

Assume the small-`delta` regime, say `delta <= 1`, so `diam_1(K) <= 2+4delta <= 6`. With `rho=4tau`, `kappa=tau/4`, the lone-far-row lemma gives margin at least

```text
rho / diam_1(K) >= 4tau/6 > tau/4.
```

So:

1. **Far row implies far hidden vertex.**  
If some row `p` has `dist_1(p,conv W) >= H`, write `p` as a convex combination of geometric vertices of `K`. Since distance to a convex set is convex, at least one vertex in that combination has distance `>= H` from `conv W`. It cannot lie in `W`, so it is hidden.

2. **Far hidden vertex has a near shadow.**  
If a hidden vertex `v` satisfied

```text
dist_1(v, conv(rows \ {v})) >= rho,
```

then it would be well-exposed by the lone-far-row lemma. Hence every far hidden vertex has

```text
dist_1(v, conv(rows \ {v})) < rho.
```

3. **Recursion with loss.**  
Choose `q in conv(rows \ {v})` with `||v-q||_1 < rho`. If `dist(v,conv W) >= H`, then

```text
dist(q,conv W) >= H-rho.
```

Expanding `q` into vertices gives another non-`W` vertex at distance `>= H-rho`.

This proves the recursion mechanism, but not yet a same-height finite cycle. An acyclic staircase can descend by `rho` per step, so “far row => cycle” still needs a no-staircase lemma.

**Where MCC Stops**

The C10 dual identity is not enough by itself:

```text
sum_i mu_i^j (p_i-v_j)
  = sum_i (beta_i^j - alpha_i^j)(p_i-v_j),
sum beta_i^j < tau/4.
```

The uncontrolled `alpha` mass can live on a high zero-face. That permits a raw local circuit, and raw circuits alone do not force negativity. The missing support lemma is:

```text
Dual localization lemma (OPEN):
For an H-far hidden vertex with H >> rho, one can choose the failed-exposedness dual so that,
up to O(rho/H) leakage, its mass is supported on the same far hidden shadow component; otherwise
max neg >= a H^2 already.
```

**The Actual Key Inequality**

The cleanest form is operator-theoretic. Since

```text
max_i ||p_i||_1 = 1 + 2 max_i neg(p_i),
```

we have

```text
||P||_{infty -> infinity} <= 1 + 2delta.
```

So MCC would follow from:

```text
Anchored-cycle projection constant (OPEN):
Any affine projection whose row geometry contains a height-H mutually-shadowing anchored cycle
has ||P||_{infty -> infinity} >= 1 + c H^2.
```

Then `1+2delta >= 1+cH^2`, hence `delta >= (c/2)H^2`.

This matches the envelope numerics exactly, but I do not have a proof.

**k=2**

Two vertices cannot shadow each other in isolation; other rows/anchors must participate. The simplest real test case is the anchored skinny quadrilateral:

```text
low anchor face W,
two high vertices v1,v2 at height H,
each near conv(the other high vertex + low/side rows),
both failing margin tau/4.
```

Symbolically proving that every exact retraction onto this quotient has projection norm `>= 1+cH^2` would likely prove the core MCC mechanism.

**Conditional DAG**

- `lem-isolated-row-exposes`: PROVED.
- `lem-far-row-gives-far-hidden-vertex`: PROVED.
- `lem-hidden-vertex-has-rho-shadow`: PROVED.
- `lem-recursion-or-staircase`: PROVED with `rho` loss.
- `lem-no-staircase-or-cost`: OPEN.
- `lem-dual-localization`: OPEN.
- `lem-anchored-cycle-projection-cost`: OPEN, numerically supported.
- `MCC`: conditional on the previous three.
- `op-exposed-hull`: conditional on MCC plus no-staircase extraction.

Final verdict: **MCC true: ~0.75. Provable by this route: ~0.45.** The next proof target is not another LP experiment; it is the anchored skinny-quadrilateral projection-norm lower bound.