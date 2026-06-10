**Verdict: no honest proof of FTI-2 yet.** The exact-completion dual route reduces to the known open frame-transfer / dual-localization inequality; it does not close from the current facts.

**PROVED pieces**

For a rank-`r` exact projection, write
```text
P = ΛR,      RΛ = I_r,      Λ1 = 1,      R1 = 1.
```
Then minimizing `max_i neg((ΛR)_i)` with fixed template constraints is an LP only after fixing `Λ` or `R`. The block duals certify one affine slice, not the global bilinear problem over all `(Λ,R)`.

In the canonical frame `R=[I_r|0]`, the proof works:
```text
dist_1(λ, Δ) = 2 neg(λ)
```
so if the archetypes lie in `W`,
```text
dist_1(p_i, conv W) <= 2 neg(p_i) <= 2δ.
```
Thus `δ >= H/2`, hence certainly `δ >= H^2/64` in the exposedness window. This is the audited canonical-frame result.

For a general frame `f_a in conv W`, clipping gives only
```text
dist_1(p, conv W) <= (2+4δ) neg(λ),
```
where `λ` are affine coordinates over the frame. The missing step is
```text
neg(λ) <= C · row-negativity.
```
That is false for arbitrary frames: abstract coordinate signs can be large while the realized row has little or no negative mass.

**Minimal Dual Obstruction**

A global dual certificate would need to prove a uniform structured-Hoffman inequality:
```text
template height H + P=ΛR, RΛ=I
    => max_i neg((ΛR)_i) >= a H^2
```
with `a>0` independent of `n`, `r`, and the chosen affine factorization.

The two-shadow algebra alone cannot supply it. Eliminating the mutual shadows gives
```text
v1 = Lbar + Ebar,      Lbar in C,
Ebar = (μ1 e2 + e1)/(1 - μ1 μ2),
```
so
```text
H <= ||Ebar||_1 <= (1+μ1)ρ / (1 - μ1 μ2).
```
In the skinny regime `μ1, μ2 -> 1`, this is vacuous. Since `ρ=4√δ`, it gives no lower bound `δ >= aH²`.

So the exact missing certificate is:

```text
Dual-localization / frame-transfer:
In every exact completion of the skinny-pair template, the high shadow residual cannot be
hidden in a collapsed affine frame; exactness must force either
  max_i neg(p_i) >= aH²
or a canonical-frame-like coordinate-negativity bound.
```

Equivalently, the obstruction is the uncontrolled high zero-face / frame-collapse direction. The existing block LP duals show idempotence is numerically load-bearing, but they do not produce a uniform all-`(Λ,R)` dual certificate.

So the deliverable is: **FTI-2 remains OPEN; the minimal obstruction is precisely the missing global dual-localization inequality above.**