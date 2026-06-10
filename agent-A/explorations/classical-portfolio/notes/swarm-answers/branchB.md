VERDICT: STUCK — available facts force near-top supplier mass, but not the needed high-blocker localization.

**Partial Proof**
Let `C = conv W`, `H = H_v = dist_1(p_v,C)`, and `D = diam_1(K) <= 2+4δ` (D0). Choose an `ell^1/ell^∞` distance dual `φ` with `||φ||∞ <= 1`, `sup_C φ = 0`, `φ(p_v)=H`. If `v` is also maximal for `φ` on the row set, set

```text
g_i = H - φ(p_i),      so g_v = 0,  0 <= g_i <= D,  and g = Pg.
```

Then the normalized candidate exposer is `h_i = g_i / D`. If every `ρ`-far row has `g_i >= κD`, then `h(v)=0`, `0<=h<=1`, and `h_i>=κ` for every far row, so `v` is exposed. This would prove Branch B whenever

```text
H >= κD = (τ/4)(2+4δ) = (1/2 + δ) τ
```

provided the top-slab blocker set is empty.

The audited g-budget F-GB gives, for every `ell>0`,

```text
P_v^+({g >= ell}) <= δD/ell.
```

Taking `ell = κD` gives

```text
P_v^+({g >= κD}) <= δ/κ = 4τ.
```

Thus, if `σ_v >= 1/2`,

```text
P_v^+({j != v : g_j < κD}) >= σ_v - 4τ >= 1/2 - 4τ.
```

This identifies the linear mechanism: large external mass forces suppliers into the top slab `g < κD`; once that slab contains no `ρ`-far blockers, the margin is at least `H/D`, reaching `κ` at the observed `H/τ ~ 1/2` wall.

**Precise Failure**
What is needed is the localization inequality

```text
T_far := {j : ||p_j-p_v||_1 >= ρ and g_j < κD} = empty.
```

What is available is only

```text
P_v^+(T_far union T_near) >= σ_v - 4τ,
```

with no control separating `T_far` from the `ρ`-near exempt rows. F-WR/F-BC do not close this when `σ_v` is order one: the external-mass cost is affordable. The C10 dual route hits the same wall: failure gives far mass `μ` and `α,β >= 0`, `sum β < κ`, but `α` is uncontrolled, so the high zero-face can absorb the certificate.

**Stress Test**
The d8 edge instance has `σ_v=0.5`, `δ=0.07175`, `H/τ=0.5357`, and cluster margin `0.9997κ`, still just hidden. The crude vertical threshold is `(κD)/τ=0.57175`, so any proof using only `H/D` misses the measured wall; it must exploit lateral cluster structure.

**Needed Sub-Lemmas**
1. Top-slab localization: under `σ_v>=1/2`, every `ρ`-far row has `g>=κD`. Status: open.
2. Equivalent C10 α-control: failed-exposedness certificates cannot place uncontrolled `α` on the high zero-face/top slab. Status: open.
3. A strengthened ψ-gap could imply this, but current F-ψ is explicitly conditional and still not enough as stated.

**Probabilities**
`P(claim B true)`: 0.78.  
`P(this stuck assessment survives adversarial audit)`: 0.85.