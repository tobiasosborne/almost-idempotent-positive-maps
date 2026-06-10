**Verdict:** frame-transfer is still open. The new ASQ result closes the canonical-frame case, but the general case still needs a real structure theorem. The good news is that the obstruction is now very precise.

**1. Frame Route (A)**

**SKETCH/OBSTRUCTION.** Skinny frames are not the main problem.

If `f_1,...,f_r in conv W` and a row has affine coordinates

```text
p = sum_a lambda_a f_a,   sum lambda_a = 1,
m = neg(lambda),
```

then clipping the negative coordinates gives `x in conv{f_a} subset conv W` with

```text
||p-x||_1 <= diam_1({f_a}) * m <= (2+4delta)m.
```

So the useful direction of the canonical identity survives skinny frames:

```text
dist_1(p,conv W) <= O(1) * coordinate-negativity.
```

No lower frame width is needed.

The fatal missing piece is different:

```text
coordinate-negativity relative to the frame <= O(row-negativity)
```

or even `<= O(delta)`. That is false for arbitrary abstract frames: signed barycentric coordinates can be large while the realized row is nonnegative or already inside `conv W`. This is exactly the earlier “abstract signs cost nothing” obstruction.

So (A) reduces to a structure theorem:

```text
Good-frame theorem (OPEN):
There exist frame points in/near conv W such that every row’s negative affine coordinate
mass over that frame is controlled by its actual row negative mass.
```

That is essentially the frame-transfer inequality itself, not a consequence of current facts.

**2. Intrinsic Route (B)**

**PROVED leakage lemma, but not enough.** Let `C=conv W`, `h_i=dist_1(p_i,C)`, and `eps_i=neg(p_i)`. From exactness,

```text
p_i = p_i P = (1+eps_i) q_i - eps_i r_i,
q_i,r_i in K.
```

Hence

```text
||p_i-q_i||_1 <= diam(K) eps_i <= (2+4delta)delta.
```

Therefore if `h_i=H`,

```text
dist(q_i,C) >= H - O(delta).
```

So the positive part of row `i` must put almost all its mass on other high-distance rows. Quantitatively, positive mass leaking below height `H/2` is `O(delta/H)`.

This proves the recursion/leakage mechanism intrinsically. But iteration only gives a high path or a high cycle. It does not force contraction to `conv W`, because a positive high component could persist unless exactness plus non-exposedness rules it out. That is the remaining cost lemma.

**3. Fallback Deciding Configuration (C)**

The minimal standalone conjecture should be the exact skinny-pair completion problem:

```text
FTI-2:
Let P be exact, P1=1, P^2=P, max neg <= delta. Let A subset W and C=conv A.
Suppose v1,v2 are distinct row vertices with dist(vj,C) >= H, both fail
(4tau,tau/4)-exposedness, and admit mutual shadows

v1 = mu1 v2 + (1-mu1)L1 + e1,
v2 = mu2 v1 + (1-mu2)L2 + e2,

with Lj in C, ||ej||_1 <= 4tau, and mu1,mu2 -> 1.
Then max_i neg(p_i) >= a H^2.
```

A numerical decider should minimize `delta/H^2` over exact completions of this template, allowing arbitrary `Lambda,R`, not only canonical frames, while robustly recomputing `W`.

**4. No-Staircase Lemma**

Clean target:

```text
No-staircase-or-cost:
A shadow descent chain of distinct hidden vertices

v0 -> v1 -> ... -> vm,   m ~ H/rho,

with dist(vj,conv W) >= H - j rho and no same-shell shadow cycle, forces
max_i neg(p_i) >= a H^2.
```

The right proof shape is spectral. The positive high-row transition along an acyclic chain is nilpotent. But `P^2=P` must keep the height mode fixed. Therefore the negative part must re-inject height; the target inequality is that this requires norm excess `||P||_{∞→∞}-1 >= cH^2`, equivalently `delta >= aH^2`.

**5. Updated DAG**

- `lem-bary-dist-neg`: PROVED in canonical frame.
- `lem-archetypes-in-W`: PROVED in canonical frame.
- `lem-asq-frame`: PROVED, gives `H <= 2delta`.
- `lem-frame-clipping`: PROVED for any frame in `conv W`, but uses coordinate negativity.
- `lem-good-frame-transfer`: OPEN.
- `lem-intrinsic-leakage`: PROVED.
- `lem-skinny-pair-exact-cost / FTI-2`: OPEN, sharp deciding case.
- `lem-no-staircase-or-cost`: OPEN.
- `MCC`: conditional on `FTI-2` plus no-staircase.
- `op-exposed-hull`: conditional on MCC.

My current probabilities:

```text
P(op-exposed-hull true): 0.85
P(provable with this programme): 0.65
P(provable within ~2 more focused sessions): 0.40
```

The next best analytic target is `FTI-2`, preferably via the projection-norm formulation rather than more convex shadow algebra.