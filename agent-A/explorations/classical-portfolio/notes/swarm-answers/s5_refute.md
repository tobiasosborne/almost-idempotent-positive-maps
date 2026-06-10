VERDICT: PARTIAL. I constructed an exact-rational all-shallow optimal face, but it is a structural refutation of the “all-shallow faces cannot exist” claim, not a formal refutation of the stated `H - C_D δ/τ` DMF for arbitrary `C_D`. The obstruction is that this family has `H = O(δ)`, so for large `C_D` the DMF threshold becomes vacuous.

**Construction / Certificate**

Use `P = ΛR`, `RΛ = I`, with rows

```text
λ0=e0, λ1=e1, λ2=e2,
λ3=(-1/2000, 1/20, 1901/2000),
λ4=(-1/2000, 11/20, 901/2000).
```

The resulting exact rational `P` is:

```text
[4000001/4000000,  -399/8000000,  -3603/8000000,   1801/4000000,    199/4000000]
[      1/4000000, 8001601/8000000, -5603/8000000,   3801/4000000,  -1801/4000000]
[      1/4000000,  -2399/8000000, 7998397/8000000,  -199/4000000,   2199/4000000]
[  -1999/4000000,        1989/40000, 3801099/4000000,              0,        1/2000]
[  -1999/4000000,       21999/40000, 1800099/4000000,         1/2000,             0]
```

Exact checks: `P1=1`, `P^2=P`. Max negative mass is

```text
δ = 1841/1600000 ≈ 0.001150625
τ ≈ 0.03392086,  ρ≈0.13568346,  κ≈0.00848022.
```

Robust LP verification gives `W={0,1,2}`. Rows `3,4` are genuine distinct vertices and hidden. For `v=3`:

```text
H = dist1(p3, conv W) = 1/1000,
σ̃_v = P34 = 1/2000 > 0.
```

Canonical separator: `w=(-1,1,1,1,1)`, `s=1999999/2000000`, giving

```text
φ = (-2, 0, 0, 1/1000, 1/1000)
g = H - φ = (2001/1000, 1/1000, 1/1000, 0, 0).
```

The far set for `v=3` is `{0,1,4}`; row `4` is far and shallow:

```text
||p4-p3||1 = 2003/2000 > ρ,   g4 = 0 < H/2.
```

Optimal exposedness witness face: primal certificate

```text
h = (1, 1/100, 0, 0, 1/200),   Ph=h,
```

so `t* ≥ 1/200`. Dual certificate

```text
μ4=1,  α2=2001/200,  β0=1/200,  γ=11
```

satisfies `(♦)` and gives `t*≤1/200`. Thus `t*=1/200<κ`. Since the primal has strict far-row slack on rows `0,1`, complementarity forces every optimal dual to have `μ0=μ1=0`, hence `μ4=1`. Entire optimal face is shallow.

Failed templates:
- Canonical `bary_to_P`: always `σ̃=0`; RW witness lands on W.
- Near-coincident mutual pair: left-inverse columns blow up like `m/||a-b||`, making anchor negativity huge.
- Opposite-negative-anchor pair: hidden/σ̃>0 occurs, but the partner has `g≫H`; optimal μ returns to deep W rows.
- Same-height pair: succeeds structurally, but only on the budget line `H=O(δ)`.

**New Sub-Lemmas**

1. Exact two-cycle shallow-face lemma: the matrix above has `v=3` hidden, `σ̃_v>0`, and every optimal witness has `μ=δ_4`, with `g4=0`. Status: proved by exact primal/dual certificates.

2. Scaling observation: the same closed-form family with `h=m=ε`, fixed lateral separation, gives all-shallow optimal faces with `δ→0`, but `H/τ→0`. Status: algebraic/numeric; explains why formal `C_D δ/τ` DMF is not killed.

Calibration: `P(existential DMF true as formally stated) = 0.60`. `P(this structural counterexample survives audit) = 0.88`; `P(it is accepted as a full formal DMF refutation) = 0.20`.

Sharpest insight: all-shallow optimal faces are real once `σ̃>0`; the obstruction is not their existence. The real load-bearing distinction is scale: this construction lives in the `H=O(δ)` budget regime, where the `C_D δ/τ` slack can swallow the whole height. So any final DMF/Baake-Sumner stability statement must exclude shallow hidden webs only at height comparable to `τ`, not absolutely.