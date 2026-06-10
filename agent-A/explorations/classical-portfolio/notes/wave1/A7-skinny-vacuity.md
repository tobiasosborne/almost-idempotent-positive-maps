VERDICT: CONFIRMED

PROVED: Eliminating `v2` gives  
`(1−μ1μ2)v1 = μ1(1−μ2)L2 + (1−μ1)L1 + μ1e2 + e1`.  
After division, the `L1,L2` coefficients are nonnegative and sum to `1`, so their part lies in `conv W`. Hence  
`H1 := dist1(v1,conv W) ≤ ||μ1e2+e1||1/(1−μ1μ2) ≤ (1+μ1)ρ/(1−μ1μ2)`.  
Symmetrically, `H2 ≤ (1+μ2)ρ/(1−μ1μ2)`.

SKETCH: This bound gives no `O(ρ)` height control in the skinny regime. In a purely affine model with `conv W={0}`, points at fixed height `H`, and `μ=1−ρ/H`, the residual `(1−μ)H` is `ρ`; small perturbations make a distinct skinny pair. Thus convex shadow equations alone allow fixed height while `μ1μ2→1`. A useful cap must use extra structure beyond the two convex decompositions.

Reconciliation: the recorded proof has exactly this elimination and constant, with `H1 ≤ (1+μ1)ρ/(1−μ1μ2)`, and identifies the same failure: mutual-shadow weights approach `1`, so the denominator collapses. No correction to the displayed constant. Caveat: the “cannot cap height” part is a convex-geometric obstruction/sketch, not an existence theorem for every exact stochastic idempotent `P`; the recorded proof also says the missing ingredient is precisely an exactness/`P²=P` dual-localization lemma.