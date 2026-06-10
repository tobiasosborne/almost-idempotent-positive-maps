**Verdict**

I cannot honestly mark HULL-CHASE proved in the general skinny regime. The evidence supports it strongly, and it is proved in the canonical simplex frame, but the proposed “top of far-support becomes exposed” step still has a real gap: it needs a dual-localization/no-high-off-support lemma that is not implied by L1, L5', or the F1 near-coincidence identity.

**What Is Proved**

PROVED: skinny mutual shadow gives near-coincidence. From the F1 identity,
`1 - μ1μ2 <= O(ρ/H)`, so the mutually-shadowing partner sits within `ρ + O(ρ/H)` of the first vertex. This means the partner is exempt from the exposer constraint once it lies in the `ρ`-ball.

PROVED: if a candidate top row `w` has a separator gap `>= κ diam₁(K)` from every row outside its `ρ`-ball, then `w` is `(ρ,κ)`-well-exposed. This is just L1 with the exemption: normalize the separating affine functional into `[0,1]`.

PROVED: L5' only controls leakage from a global height maximizer to low rows:
positive mass below `H/2` is `O(δ/H)`. It does not control positive mass to other high rows, and it does not control high rows that are not in the top row’s positive support.

**Where The Proposed Proof Fails**

The missing implication is:

```text
top of the C10 far support
  => every rho-far row from that top is low, or already in the near cluster
```

That implication is not proved. The C10 dual can have its controlled mass on one far support while the row set contains other high, rho-far helper/carrier rows on the same high zero-face. Those rows obstruct the exposer for the top row, but L5' does not see them because they are high, not low. The near-coincidence exemption only removes the skinny partner, not an entire high helper ring or a two-lane high shell.

So the exact failing configuration for the proof route is:

```text
low anchors A subset W at height 0
skinny hidden pair v1,v2 at height H, with ||v1-v2||1 < rho
C10 far supports that shadow v1,v2 mostly through the partner/near cluster
additional high carrier rows u_j at height H - O(tau)
with ||u_j - top||1 >= rho
and little/no P-positive mass from top to low rows
```

In this configuration, L5' is satisfied, the skinny pair is near-coincident, but the candidate top row is not forced to be exposed because the `u_j` are rho-far high obstructions. This is the same obstruction recorded locally as `dual-localization` / high zero-face mass, e.g. [R1-recursion-repair.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave1/R1-recursion-repair.md:1), [N1-no-staircase.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave1/N1-no-staircase.md:1), and [F1-projection-norm.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave1/F1-projection-norm.md:1).

**What Remains True**

PROVED in the canonical frame: `dist₁(row, conv W) <= 2 neg(row) <= 2δ`, hence `δ >= H/2`, so HULL-CHASE is stronger than needed there.

NUMERICAL: helper-ring searches enter the both-failing skinny region only with hull collapse; best recorded entered case has `δ/H² ≈ 280`, not a refutation.

SKETCH/GUESS: the conjectured hull-chase mechanism is probably true, but proving it needs one of these missing lemmas:

```text
dual-localization:
rho-far high obstructions to the top helper must either enter W
or force max-row-neg >= c H^2.

no-high-shell:
an exact high helper shell cannot keep all helpers non-exposed
while preserving H >> tau.
```

So the loop to `op-exposed-hull` cannot be closed from the currently proved inputs. The precise blocker is high, rho-far off-support helper rows; L5' controls low leakage, not those rows.