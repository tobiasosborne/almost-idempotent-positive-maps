VERDICT: PARTIAL. The direct/closed 2-block case is excluded with explicit constants, but the requested full ρ-separated σ̃-large 2-cycle is not proved. It dies at the same quantitative Baake-Sumner stability gap already identified in the notes.

**What I can prove**

1. **Direct two-site exclusion.** If `P_ab >= c` and `P_ba >= c`, then from `(P²)_{aa}=P_aa`,

```text
P_aa = P_aa² + P_ab P_ba + Σ_{k≠a,b} P_ak P_ka.
```

The negative part of the remainder is at most `2δ(1+δ)`, using row negative mass `≤δ`. Hence

```text
c² <= P_aa - P_aa² + 2δ(1+δ) <= 1/4 + 2δ(1+δ).
```

So direct mutual carrying with coefficient `> 1/2 + O(δ)` is impossible.

2. **Disjoint closed ball version.** Let `A,B` be disjoint carrier balls around `a,b`. If `a` sends positive mass `m` into `B`, `b` sends positive mass `n` into `A`, every row of `B` is within `r` of `p_b`, and `a` has only `ε` positive leakage into `A`, then exactness gives

```text
ε >= mn - mr - O(δ).
```

For `m,n >= c`, `r <= ρ = 4τ`, and `ε <= c²/4`, this contradicts small `δ`. Thus a genuinely closed, disjoint, order-one two-block cycle cannot exist.

3. **Non-skinny mutual shadows already pay.** If the mutual-shadow weights satisfy `μν <= 1-θ`, the standard elimination gives `H <= 2ρ/θ`, hence `δ = ρ²/16 >= (θ²/64)H²`. Only the skinny regime `μν = 1-O(ρ/H)` survives.

**Where the full proof dies**

The actual obstruction is not a direct `{a,b}` block. It can spread mass across the other vertex’s ρ-ball, and the current lemmas do not force that ball to be coefficient-closed or to return mass with a uniform minorization. F-WR needs a self-indexed common-pattern web with side conditions; F-ND only kills near-delta self-mass; F-ψ is explicitly conditional. This matches the local notes: wave5 identifies the irreducible obstruction as the shallow hidden 2-cycle, and wave8 says the missing input is quantitative Baake-Sumner stability for the top-band block.

At `δ=0`, Baake-Sumner kills it: recurrent Markov idempotent classes have equal positive rows, so separated recurrent vertices cannot mutually carry. For `δ>0`, the missing theorem is a perturbative version with no spectral gap.

**New sub-lemmas**

- Direct two-site coefficient exclusion: `P_ab,P_ba >= c` implies `c² <= 1/4 + 2δ(1+δ)`.
- Disjoint two-ball return exclusion: `ε >= mn - mr - O(δ)`.
- Non-skinny mutual-shadow payment: `μν <= 1-θ => δ >= (θ²/64)H²`.

**Probabilities**

`P(2-cycle exclusion true) ≈ 0.70`.

`P(the partial sub-lemmas above survive audit) ≈ 0.85`.

`P(a full proof follows from the currently banked tools without a new quantitative Baake-Sumner/top-band stability lemma) ≈ 0.20`.