VERDICT: CONFIRMED-WITH-CORRECTIONS

PROVED: For barycentric `λ` with `Σλ=1`, in abstract coordinate `l1`, `dist1(λ, Δ_c)=2 neg(λ)`. Lower bound: negative coordinates already cost `neg(λ)`, and the positive block has excess mass `neg(λ)`, costing another `neg(λ)`. Clipping negatives to zero and renormalizing positives attains it.

PROVED only in the identity canonical frame `R=[I_r|0]`: there the realized row is the coordinate vector `λ` (padded), so realized `l1` equals coordinate `l1`, and row negative mass equals `neg(λ)`. Since archetype vertices are assumed in `W`, `Δ_R⊂conv W`, hence
`H=dist_real(row,conv W) ≤ dist_real(row,Δ_R)=dist_coord(λ,Δ_c)=2 neg(row)`.
Thus `neg(row)≥H/2`, and therefore `δ≥H/2`.

Reconciliation: the recorded proof is the same Route A argument. Correction: its linear bound is valid only with the metric-identification assumption `R=[I_r|0]`. For a general realized affine simplex `Tλ=Σλ_a v_a`, the step `dist_real(Tλ,TΔ)=dist_coord(λ,Δ)` and `neg(Tλ)=neg(λ)` is unjustified. That would be a metric-transfer gap, not a constant issue.