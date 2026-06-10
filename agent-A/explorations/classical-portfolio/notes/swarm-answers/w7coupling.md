VERDICT: DIED-AT — same wall, now sharpened to the missing lower bound
`sum_{b in B} mu_b P_{v b} >= c tau` or equivalently
`sum_{b in B} mu_b sum_{j in A_v} lambda_j P^+_{j b} >= c tau`.

The mandated column route gives only the signed identity
```text
sum_{j in A_v} lambda_j P_{j b} = P_{v b} + O(delta/sigma_v)
```
for each blocker coordinate `b`. This is just the carrier shadow in column form. It proves: if `P_{v b}` is nontrivial, then v’s carrier system feeds blocker-site `b`. But neither C10-exchange nor the audited belt lower-bounds `P_{v b}` for a far top-band blocker. C10 controls height:
```text
sum_F mu_j g_j + sum_i alpha_i g_i = sum_i beta_i g_i <= kappa R,
```
but the uncontrolled `alpha` mass still carries all radius/column information. Pairing C10 with coordinate `b` or a sign vector again dies on the same uncontrolled high zero-face term.

New sub-lemmas:
1. Column-shadow lemma: v-carriers reproduce every column of `p_v` up to `O(delta/sigma_v)`.
2. Coupling reduction: carrier-blocker coupling follows from the aggregate pinning inequality `sum mu_b P_vb >= c tau`.
3. Obstruction: far/top-band/C10-low does not imply that pinning inequality from current inputs.

Calibration:
`P(coupling true) = 0.65` for an aggregate μ-weighted version, lower for “every blocker”.
`P(survives audit) = 0.25` without a mined LP dual; `0.70` if d10 finds a positive optimum and rational dual.

Single best next experiment: run the joint LP proposed by w6fin, but with objective minimizing the aggregate coupling
```text
M = sum_b mu_b sum_{j in A_v} lambda_j P^+_{j b}
```
under exact `P^2=P`, C10 witness constraints, `sigma_v >= 1/2`, and far top-band blocker constraints. If optimum `M=0`, the lemma is false as stated. If `M >= c tau`, extract that LP dual; that is the missing proof certificate.