**VERDICT: NOT-REFUTED.** I did not find an exact-rational counterexample with `δ/H² < 3`. The sharpest reproduced near-failure is still the known wall instance:

`H = 287/2000 = 0.1435`, `δ = 287/4000 = 0.07175`, so  
`δ/H² = 1000/287 = 3.484320557...`.

For the canonical deficit in the reproduced edge instance, the top-band rows have `g_j = H`, `R = 2 + H = 4287/2000`, and

`(κR/H)^2 = 18378369/18368000`, so `κR/H = 1.000282...`.

That is the knife-edge: top-band exists, but only with the known `≈3.484 H²` negativity payment. It misses the requested `δ/H² < 3`.

**Failure Map**
1. **Belt-insufficiency scaling** `δ=ε², σ_v=√ε, ℓ=ε^{3/2}, H=ε`: satisfies the audited inequalities, but the exact `P²=P` realizations I could build/optimize collapse to the wall. The financing row height becomes pinned at `g=H`, forcing `δ/H²≈3.48`.

2. **Optimized financed-wiggle/MRP family**: I reimplemented the Gurobi alternating LP with SciPy because local Gurobi license failed. Scanning `σ_v`, `k_groups`, `ell`, and `d` found no `δ/H²<3`; best structured top-band entry in my grid was `δ/H²≈3.571`, while the refined known cell is `3.484`.

3. **Multi-group financing**: extra groups duplicate the same blocker geometry. They spread dual mass but do not lower the wall; the one-mode constraint still decides the margin.

4. **Canonical simplex/barycentric frame**: killed harder. With `R=[I|0]`, `conv W` contains the archetype simplex, so `dist(row, conv W) <= 2 neg(row)`; this gives a linear cost, far stronger than the desired quadratic evasion. Coincident-row tricks are invalidated by `d3_vertexfix.py`.

5. **Recursive/staircase/shell idea**: dies by the X1 exactness obstruction. A nonconstant hidden mode inside a skinny shell forces `diam₁ >= 2`, so the next financier cannot remain both `ρ`-local and low-g; reciprocal carriers either expose or pay cost.

6. **Unstructured random exact projections**: 1,220 random `P=ΛR`, `RΛ=I` projections gave only 16 hidden/top-band cases; best was terrible, `δ/H²≈176`.

**Calibrated P(top-band localization true):** `0.83`. Not proved, but after this pass I’d raise it slightly: the only surviving route to refutation needs a genuinely new arbitrary-frame dual-localization escape, not another sampled financed shell.

**Sharpest Structural Insight**
The belt lets the financier be a free low-g far row. Exactness does not. `RΛ=I` turns that financier into a biorthogonal carrier, and its canonical height is forced up to the wall. To beat `δ/H² < 3`, a counterexample needs a far row with `g` substantially below `H`; every attempt to make that row hidden recursively creates the same reciprocal-carrier obstruction.