**Verdict:** I cannot honestly mark FTI-2 proved by the projection-norm route. The exact k=2-with-anchors algebra closes to a sharp obstruction: it only forces the skinny relation `1 - μ1 μ2 = O(ρ/H)`, not `‖P‖∞→∞ ≥ 1 + cH²`.

**PROVED: norm reduction.** Let `Δ = max_i neg(p_i)`. Since rows sum to `1`,

```text
‖P‖∞→∞ = max_i ‖p_i‖₁ = 1 + 2Δ.
```

So FTI-2 would follow from `‖P‖∞→∞ ≥ 1 + cH²`.

**PROVED: exact k=2 scalar algebra.** Let `a,b` index `v1,v2`. For any test vector `x`, define

```text
Y1 = <v1,x>,  Y2 = <v2,x>,
Z1 = <L1,x>,  Z2 = <L2,x>,
rj = <ej,x>.
```

Then

```text
Y1 = μ1 Y2 + (1-μ1) Z1 + r1
Y2 = μ2 Y1 + (1-μ2) Z2 + r2
```

and `|rj| ≤ ρ‖x‖∞`. Also, because rows are left-fixed by `P`, `ej P = ej`, so applying `P²=P` to `y=Px` gives the same equations, not a stronger norm term.

Eliminating `Y2` gives

```text
Y1 = Zbar + (μ1 r2 + r1)/(1 - μ1 μ2),
Zbar ∈ conv{Z1,Z2}.
```

Thus any common height test with gap `s = Y1 - Zbar` satisfies

```text
(1 - μ1 μ2) s ≤ (1 + μ1) ρ ‖x‖∞.        (*)
```

**The failing inequality.** To get projection norm excess, one would need the positive margin

```text
(1 - μ1 μ2) s - (1 + μ1)ρ  ≳  H²
```

for some coordinate-bounded height/separator with `s ≳ H` up to constants. But in the skinny regime `μ1,μ2 → 1`, the left side can be non-positive. Equation `(*)` is then just the known vacuous bound: the residuals are amplified by `1/(1-μ1μ2)`.

So the natural height/exposer candidates do not prove norm excess. If `h:K→[0,1]`, then `Px` takes row values in `[0,1]`, so it cannot witness `‖P‖∞→∞>1`. A raw `ℓ∞` separator gives a gap, but not an absolute overshoot outside `[-1,1]`.

This matches the existing local status: FTI-2 is listed as open in [d6](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/d6-codex-frame-transfer.md:73), the projection constant is explicitly open in [d4](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/d4-codex-mcc-attempt.md:76), and the known gap is the skinny `μ→1` degeneracy in [DELIVERABLE2](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/experiments/DELIVERABLE2_asq_proof.md:42). Numerics still support FTI-2: the d7 tradeoff run found entered cases only with `δ/H²` huge, minimum about `280`, not a refutation [out](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/experiments/out/d7_tradeoff.json:505).

What would close it is a genuine dual-localization/projection statement: either prove the above positive margin despite `μ→1`, or prove that when it fails the helper/shadow rows enter `W` and collapse `H`. Current evidence supports that, but I do not have a proof from the projection-norm algebra alone.