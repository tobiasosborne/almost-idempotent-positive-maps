**Verdict:** I did not find a refutation. The best exact adversarial shell I could reconstruct enters the non-exposed-pair region, but with `δ/H² ≈ 280`, not `o(H²)`.

**Explicit Exact Candidate**
Take `r=4`, `n=8`, `R=[I_4 | 0]`, and `P=ΛR` with

```text
Λ =
e0
e1
e2
e3
(-0.1,  0,    1.1, 0)
( 0,   -0.1,  1.1, 0)
(-0.064830487338, -0.016510216942, 0.918308748207, 0.163031956072)
(-0.171143734643, -0.125378004487, 1.277347847585, 0.019173891546)
```

**PROVED:** since the top block of `Λ` is `I_4`, `RΛ=I_4`, hence `P²=P`; all rows sum to `1`, so `P1=1`.

**NUMERICAL verification:** recomputing `τ` from this `P` gives

```text
δ = 0.29652173913034846
τ = 0.5445380970422073
ρ = 2.1781523881688294
κ = 0.13613452426055184
W = {0,1,3,7}
H = min dist₁(v_j,conv W) = 0.032535174789137915
δ/H² = 280.1239554776283
```

Rows `4,5` are distinct vertices and both fail exposedness (`m1=m2≈0.1063 < κ`). So this is a real exact “entered” shell, but it is the opposite of a refutation: the helpers enlarge `W`, and `H` collapses.

**Structural Wall**
**PROVED in canonical frames:** if the archetypes are realized rows, they enter `W`; then `conv W` contains the simplex and

```text
dist₁(row, conv W) <= dist₁(λ, Δ) = 2 neg(λ) <= 2δ.
```

So canonical/refined-barycentric attempts cannot give `δ=o(H²)`; they give the stronger linear obstruction `δ >= H/2`.

**SKETCH:** the non-realized-archetype escape also hits the same mechanism. To make a high vertex fail exposedness at honest `ρ=4√δ`, a helper must sit outside the `ρ`-ball and still keep affine height small. If the helper is exposed, it joins `W` and captures the pair. If it is hidden, the same requirement recurses. Numerically, every successful blocker shell either joins `W` or shrinks `H`; the d7 sweeps found entered examples only with huge ratios (`best ≈280`, often `10³+`).

**GUESS / proof-mining target:** the real wall is “helper exposure / hull-chase plus exact high-shell reinjection.” A rigorous refutation route would need a non-realized high shell where blockers do not enter `W` and exactness does not charge the displacement. I do not see such a route; that missing impossibility is essentially the FTI-2 projection-cost lemma itself.