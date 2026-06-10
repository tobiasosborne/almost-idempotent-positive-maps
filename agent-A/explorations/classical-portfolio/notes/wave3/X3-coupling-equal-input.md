Status: X3 gives a real **conditional** equal-input lemma, but it does **not** close HLC unconditionally.

**PROVED: repaired kernel is approximately idempotent.**  
Let `ν_i=neg(p_i)` and `Q=(q_i)`. Then

```text
||q_i-p_i||_1 = 2ν_i ≤ 2δ
||P||_{∞→1} ≤ 1+2δ
||Q²-Q||_{∞→1} ≤ 6δ+4δ² ≤ 8δ     for small δ.
```

So `Q²≈Q` is true in row `ℓ¹`, not just after applying rows.

**PROVED: equal-input under a genuine mixing/localization hypothesis.**  
Let `B` be a high-shell block. Suppose for all `x∈B`,

```text
q_x(B^c) ≤ λ
```

and the one-step rows on `B` have Dobrushin overlap

```text
inf_{x,y∈B} Σ_{z∈B} min(q_x(z),q_y(z)) ≥ γ > 0.
```

Then for `x,y∈B`,

```text
||q_x-q_y||_1 ≤ (4λ + 2||Q²-Q||_{∞→1})/γ
              ≤ Cγ^{-1}(λ+δ).
```

Same proof works for `m`-step communication with `C m γ^{-1}(λ+δ)`. This recovers Baake-Sumner exactly when `δ=λ=0`: communicating rows in an idempotent stochastic class are identical.

**HIGH-SHELL consequence.**  
For the global height maximizer `i*`, L5′ gives

```text
q_i*(rows below H/2) ≤ C δ/H.
```

So if the communicating high block containing `i*` also has uniformly propagated leakage `λ=O(δ/H)` and a fixed Dobrushin gap, then

```text
||q_i-q_k||_1 = O(δ/H),  ||p_i-p_k||_1 = O(δ/H)
```

for all rows in that block. Since `H≥Aρ=4A√δ`,

```text
δ/H ≤ ρ/(16A),
```

so for large universal `A` the whole block is a single `ρ`-cluster. Internal block members are then exempt from each other’s exposer constraints.

**Assembly That Closes Conditionally**

If that `ρ`-cluster is isolated from all other high obstructions and from the lower hull in the L1 sense, L1 exposes a representative high row. That is definitionally impossible because exposed high vertices are in `W`, hence have height `0`. Therefore this branch forces `δ ≥ aH²`.

If it is not isolated, there is a `ρ`-connection downward or to off-chain high carriers. The acyclic part is exactly the N1 situation: nilpotence forces positive mass to off-chain high rows. X3 helps only if those off-chain carriers also form localized/mixing repaired-kernel blocks; then they collapse to `ρ`-clusters and the same exposure/downward-chain dichotomy repeats.

**What Remains Open**

The missing step is proving the required localization/mixing for every high obstruction. L5′ only controls low leakage from the top row, not arbitrary high helper rows. Mere directed “q-mass between neighborhoods” is not enough unless upgraded to a fixed-time Dobrushin/minorization statement. This is the same high zero-face/helper-shell gap recorded in [W2b](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave2/W2b-hull-chase.md:24) and [N1](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave1/N1-no-staircase.md:16).

So: **X3 proves a strong localized equal-input lemma; HLC still needs the theorem that every high hidden shell either satisfies that localization/mixing hypothesis or pays `Ω(H²)`.**