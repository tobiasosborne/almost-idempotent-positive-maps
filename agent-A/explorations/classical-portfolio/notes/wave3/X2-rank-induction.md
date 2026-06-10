**Verdict:** no proof from rank induction as stated. The precise obstruction is that the only exact Schur-type compression either preserves rank or loses all control of `neg ≤ δ`. So X2 reduces to the already-open frame-transfer / dual-localization lemma, not to the proved lower-rank cases.

**PROVED obstruction.** Block
```text
P = [ A  B
      C  D ].
```
If `I-D` is invertible, the stochastic complement
```text
Q = A + B(I-D)^(-1)C
```
is again row-stochastic and idempotent. But it does **not** lower rank:
```text
rank(Q) = rank(P).
```
This follows from the Schur complement of `I-P`: since `rank(I-P)=n-rank(P)` and `I-D` is invertible, `rank(I-Q)=|S|-rank(P)`. Thus any exact nonsingular elimination keeps all fixed modes. To actually drop rank, the eliminated block must be singular or one must quotient by a fixed subspace, exactly where conditioning/positivity control is missing.

Worse, negativity can blow up arbitrarily. Let
```text
q = (epsilon + delta, -delta, 1 - epsilon),
P = 1 q^T,
S = {1,2}.
```
Then `P1=1`, `P²=P`, and `max neg(row)=delta`. The Schur complement onto `S` is the rank-one idempotent with row
```text
((epsilon + delta)/epsilon, -delta/epsilon),
```
so its negative mass is `delta/epsilon`. Taking `epsilon << 1` gives unbounded loss even from an exact idempotent with arbitrarily small original negativity. This is not an HLC counterexample, but it kills the proposed compression step unless an additional uniform conditioning lemma is proved.

**What this means for X2.**

If the high shell misses an archetype direction, one can choose barycentric coordinates on its smaller affine span and get a canonical lower-rank exact idempotent. But the new `δ` is coordinate-negativity, not row-negativity. Bounding it by the original `δ` is exactly the open good-frame / frame-transfer inequality noted in [F2-completion-LP.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave1/F2-completion-LP.md:1).

If the high shell spans everything, dimension alone does not force exposure. It can still be a full-dimensional high carrier shell where every candidate vertex is `ρ`-shadowed by other high rows. Current tools control low leakage, not high off-support carriers; this is the same obstruction recorded in [W2b-hull-chase.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave2/W2b-hull-chase.md:1).

**Partial reduction.** Rank induction would work if one proves a one-shot split lemma:

```text
A high hidden shell contained in a proper affine factor either
  pays max neg >= c H^2,
or admits a rank-lower exact/near-exact compressed system with
  neg' <= O(delta), H' >= cH, rho' <= C rho,
and well-exposed vertices lift back.
```

But that split lemma is essentially HLC/dual-localization itself. So the deliverable is a precise obstruction, not a proof: Schur exactness is available, rank drop plus `neg` control is the missing theorem.