**Verdict**

The true minimal missing set is **one open localization/cost lemma**. The older opens `no-staircase`, `FTI-2`, `dual-localization`, `anchored-cycle cost`, `good-frame transfer`, and the `A2` stall repair are best treated as **faces of the same missing statement**, not independent blockers.

All statements below are for the small-`δ` regime used in the notes.

**Minimal DAG**

| Node | Contract | Status |
|---|---|---|
| D0 | `diam₁(K) ≤ 2+4δ`, `‖P‖∞→∞ = 1+2 max neg(row)` | **PROVED**; norm identity in [F1](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave1/F1-projection-norm.md:3). |
| L1 | If `dist₁(v,conv(rows\{v})) ≥ ρ`, then `v` is exposed with margin `≥ ρ/(2+4δ)`; near rows inside `ρ` are exempt. | **PROVED** in [A1](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave1/A1-lone-far-row.md:3). |
| L2 | A row at height `H=dist(row,conv W)` yields a hidden vertex at height `≥H`. | **PROVED** in [A2](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave1/A2-recursion-triple.md:3), also d4. |
| L2′ | A hidden vertex has a `ρ`-shadow: `dist(v,conv(rows\{v}))<ρ`. | **PROVED** by contrapositive of L1; see [d4](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/d4-codex-mcc-attempt.md:16). |
| A2-stall | The naive recursion gives a new hidden vertex. | **OPEN as stated**; expansion can reuse `v` through a nonvertex row, [A2](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave1/A2-recursion-triple.md:7). Redundant under HLC below. |
| L4 | Frame clipping: coordinate negative mass over a frame in `conv W` bounds distance to `conv W`. | **PROVED**, [A4](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave1/A4-clipping-and-leakage.md:3). |
| L5′ | At a global height maximizer, positive mass leaking below `H/2` is `≤ 2(2+4δ)δ/H` up to normalization. | **PROVED only at global maximizer**, [A4](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave1/A4-clipping-and-leakage.md:9). |
| L6 | Canonical identity-frame bound: `dist(row,conv W) ≤ 2 neg(row) ≤ 2δ`. | **PROVED only for `R=[I_r|0]`**, [A3](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave1/A3-canonical-frame-trio.md:5). Not transferable. |
| S1 | Two-shadow elimination gives `H ≤ (1+μ₁)ρ/(1−μ₁μ₂)`. | **PROVED algebra**, but **SKETCH/obstruction** that it is vacuous as `μ₁μ₂→1`, [A7](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave1/A7-skinny-vacuity.md:3). |
| S2 | Height-test/projection-norm route proves FTI-2. | **FALSE as route**; exact scalar algebra only gives the skinny relation, not norm excess, [F1](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave1/F1-projection-norm.md:41). |
| N1 | Acyclic high chain is nilpotent and must send positive mass to off-chain high rows. | **PROVED conditional algebra**, but does not bound that mass by `O(δ)`, [N1](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave1/N1-no-staircase.md:16). |
| HLC | High-shell localization/cost lemma below. | **OPEN**. This is the single missing node. |
| HCC/MCC | `max_i dist(row_i,conv W)=H ⇒ δ ≥ aH²`, unless `H=O(ρ)`. | **PROVED conditional on HLC**. |
| op-exposed-hull | Every row is within `C′τ` of `conv W`. | **PROVED conditional on HLC**. |

**Single Open Problem**

**High-shell localization/cost lemma (HLC).**  
There exist universal constants `δ₀,A,a>0` such that:

Let `P1=1`, `P²=P`, `max_i neg(p_i)≤δ≤δ₀`, `τ=√δ`, `ρ=4τ`, `κ=τ/4`. Let `W` be the `(ρ,κ)`-well-exposed row vertices, `C=conv W`, `h_i=dist₁(p_i,C)`, and `H=max_i h_i`.

If `H≥Aρ` and `δ<aH²`, then some row vertex `v` with `h(v)≥H/2` is `(ρ,κ)`-well-exposed.

Equivalently: a high hidden shell cannot be kept alive by near-coincident shadows, nonvertex reuse, off-chain high carriers, or a skinny two-lane staircase unless the matrix already pays `Ω(H²)` negative mass.

This one statement absorbs:

- `FTI-2`: skinny mutual-shadow pairs are the two-vertex high-shell case.
- `no-staircase`: acyclic chains are the nilpotent high-shell case.
- `A2` stall repair: reuse of `v` through a nonvertex row is a local high-shell localization failure.
- `good-frame transfer`: arbitrary-frame coordinate negativity is another formulation of the same hidden high zero-face obstruction.

**Conditional Assembly**

Assume HLC. Let `H=max_i dist₁(p_i,conv W)`.

If `H=0`, done. Otherwise L2 gives a row vertex at height `H`; since `W⊂conv W`, it is hidden. If `H<Aρ`, then

```text
H < Aρ = 4Aτ.
```

If `H≥Aρ`, HLC says either `δ≥aH²`, or there is a well-exposed row vertex at height `≥H/2`. The latter is impossible, because a well-exposed vertex is in `W⊂conv W` and has height `0`. Hence

```text
δ ≥ aH²,
so H ≤ τ / sqrt(a).
```

Therefore in all cases

```text
H ≤ C′ τ,
C′ = max(4A, 1/sqrt(a)).
```

Since `H` was the maximum over rows, every row is within `C′τ` of `conv W`. That is `op-exposed-hull`.

**Probabilities**

- HLC true: **0.65–0.75**. Numerics strongly support it, but F1/N1 show the obvious proof routes fail.
- HLC provable by the current localization programme: **0.40–0.50**.
- `op-exposed-hull` true as stated in the small-`δ` regime: **~0.80**.
- Needs weakening, e.g. extra `log(1/δ)`: **~0.20**. I would not build on the log-free rate as proved until HLC is settled.