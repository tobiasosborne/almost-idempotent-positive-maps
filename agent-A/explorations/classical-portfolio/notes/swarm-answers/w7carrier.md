VERDICT: DIED-AT, same wall, sharpened.

The column route gives one useful identity but not the theorem. For direct carrier mass `m = P_vf > 0`, idempotence in column `f` gives

```text
P_vf = Σ_k P_vk P_kf.
```

Splitting `A = {k : P_vk > 0}` and `N = {k : P_vk < 0}`,

```text
Σ_{k in A} P_vk P_kf^+ >= P_vf - Σ_{k in N} P_vk^- P_kf^-
                           >= m - δ^2.
```

So positive carrier mass from `v` does propagate into positive feed toward `f`, but only in proportion to the actual overlap mass `m`. The hypothesis says “positive”, not “quantitatively nontrivial”. If `m` is tiny, the inequality contains no `H`, no `σ_v`, and cannot force `g_f >= κ R_osc` or `δ >= c H^2`.

The d9 “height = margin” law is explained by exposedness-LP complementarity: a binding far blocker satisfies `h(f)=t*` because its far-row constraint is active. I do not see an `RΛ = I` identity that upgrades this active-constraint equality into the required lower bound `t* >= κ`.

New sub-lemmas:

1. Column-carrier propagation: proved as above. Direct carrier mass forces second-generation positive feed from `v`’s positive carrier system, up to `δ^2`.

2. Gauge warning: any argument comparing raw rows of `Λ` is not invariant under `Λ -> ΛS`, `R -> S^{-1}R`. The invariant consequences reduce to row exactness `g=Pg` and column exactness `P^2=P`; the row side is the known no-gain lemma.

3. Binding height identity: proved, but LP-only. If `f` has nonzero blocker dual in the exposedness LP, then `h(f)=t*`. This matches d9 but does not force the wall.

Calibration: `P(correct quantitative reciprocal-carrier lemma true) ≈ 0.72`; `P(literal positive-mass form true) ≈ 0.40`; `P(this died-at diagnosis survives audit) ≈ 0.86`.

Single most informative next experiment: run the joint LP/alternating certificate search with an explicit carrier-overlap parameter

```text
θ_f = Σ_{k in A_v} (P_vk / σ_v) P_kf^+
```

and minimize `δ/H^2` while sweeping a lower bound `θ_f >= θ0`. If the wall `3.48` appears only for `θ0 = Ω(1)`, the missing theorem is exactly a quantitative carrier-overlap lower bound, not qualitative “positive mass”.