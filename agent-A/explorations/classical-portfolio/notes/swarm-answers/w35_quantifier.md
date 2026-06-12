# w35_quantifier — CHAIN-COMPATIBLE: the exists-quasi-max form composes end-to-end; registry contract written; one routing caveat (codex, 2026-06-12)
# Brief: notes/briefs/w35_quantifier.md. Long form: experiments/out/w35_quantifier/proof.md.

VERDICT: CHAIN-COMPATIBLE (P = 0.88). No load-bearing link needs for-all max-volume or a
canonical tie choice; one selected chart with bounded coefficients suffices.
- REGISTRY-READY CONTRACT: for delta_0 <= 0.3, theta in (0,1]: every row-stochastic idempotent
  P with delta(P) <= delta_0 has an actual-row basis U with Vol(U) >= theta Vol_max(P) such
  that max_s SF_s(U) <= C_sf(delta_0,theta) delta(P).
- CONSTANTS CHAIN (quasi, A = 1/theta): C_mu = C_sf + 1 + A; C_D = 4(1+2delta_0)(C_sf+1+A);
  L_eta <= C_D delta/eta + delta; L4: ||P-Q||_{infty,1} <= eta + 12 C_D delta/eta + 36 delta
  (eta <= theta/4, L_eta <= 1/8).
- ROUTING CAVEAT: w27's scalar cross-cluster telescope uses the exact-max sign fact
  0 <= 1-a_s <= 2, FALSE in quasi charts — route through SF -> tax -> displacement ->
  face/leakage instead. (AUDIT FLAG for w36: w35_charge's banked deficit bound also uses the
  sign fact — fine for theta = 1 exact-tie selection, needs care if theta < 1.)
- TIE-BREAK: minimize max_s SF_s over theta-quasi-max bases + lexicographic — collapses all
  audited bad instances (= w35_charge's U*). Greedy unit-row (P=0.30) and projected-volume
  (P=0.25) rules NOT registry-ready.
- FOR-ALL READING: killed at delta_0 >= 1/2 by the staircase (P = 0.99); below 1/2 the
  envelope ~ 1/(1-2delta_0) constrains but does not kill.
- P(exists-quasi SF true for delta_0 <= 0.3) = 0.60.
---
## Appendix: proof.md (verbatim)

# VERDICT: CHAIN-COMPATIBLE

The downstream chain does not need SF in every max-volume chart, nor does it
need a canonical max-volume chart. It needs one selected actual-row chart whose
coordinate constants are bounded and whose representative rows satisfy the SF
bound. Thus the right quantifier is exists, and the robust near-tie version is
exists theta-quasi-max-volume basis.

There is one routing caveat. The original w27 scalar cross-cluster telescope
uses the exact max-volume sign fact `0 <= 1-a_s <= 2`. For theta-quasi charts
this sign fact is false. The quasi-max route should therefore pass through
SF -> tax -> representative displacement -> face/leakage, not through the
standalone scalar cross-cluster estimate. With that routing, constants degrade
only through theta-dependent factors.

Registry-ready contract:

For every `delta0 <= 0.3` and `theta in (0,1]`, there is a finite
`C_sf(delta0,theta)` such that every row-stochastic idempotent `P` with
`delta(P) <= delta0` has an actual-row basis `U` with
`Vol(U) >= theta Vol_max(P)` and, in the coordinates of `U`,
`max_s sum_j (P_{u_s j})_+ (mu_s(j) - (1-a_s(j)))_+ <= C_sf(delta0,theta) delta(P)`.

Here `mu_s(j)=sum_{t != s} (-a_t(j))_+` and
`p_j=sum_t a_t(j) p_{u_t}`.

## Source Audit

I used the requested notes:

* `w30_maxvol.md`: reduces representative displacement to the transverse tax.
* `w31_tax.md`: splits the tax into scalar deficit plus signed-face excess.
* `w28_face.md`: reduces the face/leakage estimate to representative displacement.
* `w27_concentration.md`: gives in-class concentration, cross-cluster leakage,
  and conditional L4 assembly.
* `w26_cluster_audit.md`: supplies the corrected max-volume chart constants.
* `w34_halfcex.md` and `w34_audit.md`: exhibit the tie ambiguity and favorable
  signed/unit-row tie charts.
* I also checked the relevant w33 tie examples to assess deterministic rules.

## Q1. Chart Hypotheses By Link

Common chart data:

Let `U={u_1,...,u_k}` be an actual-row basis, `r_s=p_{u_s}`, and

```text
p_j = sum_s a_s(j) r_s.
```

The useful algebraic facts are:

* actual rows: each `r_s` is a row of `P`, hence `||r_s||_1 <= R := 1+2 delta`;
* affine coordinates: `sum_s a_s(j)=1`;
* fixed coordinates: `P a_s = a_s`;
* coefficient bound: for max-volume, `|a_s(j)| <= 1`; for theta-quasi,
  `|a_s(j)| <= A := 1/theta`;
* coordinate norm/separation: max-volume gives coordinate functional norm
  `<=1` and pivot separation `>=1`; theta-quasi gives norm `<=A` and separation
  `>=1/A=theta`.

Tax split.

The exact max-volume version uses `|a_s| <= 1` in the strong form
`0 <= lambda_s(j) := 1-a_s(j) <= 2`. Together with `P a_s=a_s`, this gives

```text
sum_j (P_{u_s j})_+ lambda_s(j) <= 2 delta.
```

Then

```text
M_s := sum_j (P_{u_s j})_+ mu_s(j)
    <= 2 delta + SF_s.
```

This link does not use max-volume as a selector. It uses only actual-row
coordinates, fixedness, row negativity, and the coefficient bound consequence.

Displacement reduction.

For `v(j)=a(j)-e_s`,

```text
||p_j-r_s||_1 <= R ||v(j)||_1.
```

In the exact max-volume chart, `||v(j)||_1=2(lambda_s(j)+mu_s(j))`, because
`lambda_s >= 0`. Thus the displacement bound uses:

* actual rows and row norm `R`;
* affine coordinate sum;
* the scalar deficit estimate;
* the transverse tax.

Again, no canonical max-volume property is used after the constants are in hand.

Face estimate.

The w28 face step uses the representative displacement estimate

```text
D_s := sum_j (P_{u_s j})_+ ||p_j-r_s||_1 <= C_D delta.
```

Then rows outside `M_s={j: ||p_j-r_s||_1 <= eta}` receive positive mass at most
`C_D delta/eta`, and negative mass at most `delta`. This step uses the chosen
pivot rows and row negativity. It does not use max-volume directly.

Concentration and leakage.

In-class concentration uses only:

* actual pivot rows;
* `||r_s - r_s^+/(1+nu_{u_s})||_1 <= 2 delta`;
* membership `||p_i-r_s||_1 <= eta`.

So rows in `M_s` satisfy `||p_i - \hat r_s||_1 <= eta+2 delta`.

Disjointness of clusters uses pivot separation. Exact max-volume gives
separation `>=1`, so `eta <= 1/4` is safe. Theta-quasi gives separation
`>=theta`, so one must take `eta < theta/2`, for instance `eta <= theta/4`.

The original w27 scalar cross-cluster leakage estimate uses the exact
max-volume sign fact `lambda_s >= 0` globally. This is not robust under
theta-quasi replacement. The compatible quasi route instead obtains leakage
from the face estimate above.

L4 assembly.

The conditional L4 construction uses:

* disjoint pivot-ball clusters;
* representative leakage `L=max_s sum_{j notin M_s}|P_{u_s j}|`;
* in-class concentration `eta+2 delta`;
* coefficient coordinates summing to one;
* row negativity to bound the negative coefficient mass after clipping.

It does not require the basis to be "the" max-volume basis. It only needs the
selected basis to have the listed properties and `L <= 1/8`.

Conclusion for Q1: no load-bearing link requires a for-all max-volume statement
or a canonical tie choice. A single good selected basis is enough.

## Q2. Theta-Quasi-Max Robustness

Let `U` be an actual-row basis with

```text
Vol(U) >= theta Vol_max(P),        0 < theta <= 1,
```

and put `A=1/theta`.

By Cramer's rule, replacing one pivot row by any actual row gives

```text
|a_s(j)| <= A.
```

The w26 rank-gap argument then gives coordinate functional norm `<=A` and pivot
separation `>=1/A=theta`: for `W_s=span{r_t:t != s}`, some row has distance at
least one from `W_s`; since its `s`-coordinate is at most `A`, this forces
`dist(r_s,W_s) >= 1/A`.

Assume the robust SF hypothesis in this selected chart:

```text
SF_s := sum_j (P_{u_s j})_+ (mu_s(j)-lambda_s(j))_+
     <= C_sf delta,

lambda_s(j)=1-a_s(j),
mu_s(j)=sum_{t != s}(-a_t(j))_+.
```

The sign of `lambda_s` is no longer fixed. Nevertheless the SF term charges the
overshoot rows where `a_s>1`, and the chain survives.

First, pointwise,

```text
mu_s(j) <= (mu_s(j)-lambda_s(j))_+ + lambda_s(j).
```

Also `sum_j P_{u_s j} lambda_s(j)=0` and
`|lambda_s(j)| <= 1+A`, so

```text
sum_j (P_{u_s j})_+ lambda_s(j) <= (1+A) delta.
```

Therefore the transverse tax obeys

```text
M_s := sum_j (P_{u_s j})_+ mu_s(j)
    <= (C_sf + 1 + A) delta.                  (1)
```

Second, the positive scalar deficit is also controlled. From the same identity,

```text
sum_j (P_{u_s j})_+ lambda_s(j)_+
 <= sum_j (P_{u_s j})_+ lambda_s(j)_- + (1+A) delta.
```

Whenever `lambda_s(j)<0`, the SF integrand is at least `-lambda_s(j)`. Hence

```text
sum_j (P_{u_s j})_+ lambda_s(j)_+
 <= (C_sf + 1 + A) delta.                    (2)
```

For general signed `lambda_s`,

```text
||a(j)-e_s||_1 = 2( mu_s(j) + lambda_s(j)_+ ).
```

Combining (1) and (2), and using `||r_t||_1 <= R0 := 1+2 delta0`, gives the
representative displacement bound

```text
D_s := sum_j (P_{u_s j})_+ ||p_j-r_s||_1
    <= 4 R0 (C_sf + 1 + A) delta.            (3)
```

Thus one may take

```text
C_D(delta0,theta) = 4(1+2 delta0)(C_sf(delta0,theta)+1+theta^{-1}).
```

For theta=1, the exact max-volume sign `lambda_s>=0` gives the sharper old
constant

```text
C_D <= 2(1+2 delta0)(C_sf+4),
```

but (3) is the robust uniform formula.

Face/leakage follows for any `eta <= theta/4`:

```text
L_eta := max_s sum_{j notin M_s}|P_{u_s j}|
      <= C_D delta/eta + delta.              (4)
```

The conditional L4 assembly then gives, whenever `L_eta <= 1/8`,

```text
||P-Q||_{infty,1}
 <= eta + 12 L_eta + 24 delta
 <= eta + 12 C_D delta/eta + 36 delta.       (5)
```

Taking `eta=sqrt(delta)` is valid in the small regime
`sqrt(delta) <= theta/4`; then

```text
||P-Q||_{infty,1}
 <= (1 + 12 C_D + 36 sqrt(delta0)) sqrt(delta),
```

provided `C_D sqrt(delta)+delta <= 1/8`. Equivalently, it is enough that

```text
delta <= delta_sm :=
min( theta^2/16,
     (sqrt(C_D^2+1/8)-C_D)^2 ).
```

For larger `delta` inside a fixed cap, the usual coarse fallback to any fixed
rank-one stochastic idempotent gives a finite `O_{delta0,theta,C_sf}(sqrt(delta))`
constant. The constructive cluster/H-M estimate is the meaningful small-delta
part and is exactly (5).

Thus the end-to-end conditional statement is:

```text
exists theta-quasi-max SF with constant C_sf(delta0,theta)
  => transverse tax with C_mu = C_sf+1+theta^{-1}
  => representative displacement with C_D as in (3)
  => face/leakage L_eta <= C_D delta/eta + delta
  => conditional L4 H-M approximation
     ||P-Q||_{infty,1} <= eta+12 C_D delta/eta+36 delta
  => W-free O_{delta0,theta,C_sf}(sqrt(delta)).
```

## Q3. Deterministic Tie-Break Rule

The rule that is both deterministic and aligned with the chain is:

```text
Given theta, let B_theta(P) be the finite set of actual-row bases U with
Vol(U) >= theta Vol_max(P).  For each U compute
Phi(U)=max_s SF_s(U).  Choose a basis minimizing Phi(U), with a fixed
lexicographic tie-break.
```

This is well-defined for every finite `P` of rank `k`. It picks a
theta-quasi-max-volume basis by construction. It also collapses the known bad
tie examples:

* half-delta staircase: the favorable tied bases replacing row 0 by the exact
  signed/unit rows have ratio exactly 1, so the minimum is at most 1;
* w33 transverse-pair tie examples: the signed-row tie bases have ratio exactly
  1 in the audited samples;
* w33 dense-pair `k=7`: the identity chart has ratio `17/8`, while the signed
  row tie charts have ratio 1, so the minimum selects the low-SF chart or an
  equally good one.

This minimum is the right object for the exists-form chain. Once the minimizing
chart is selected, all later estimates are performed in that chart. No later
step asks how the chart was found.

Assessment of the proposed alternatives:

* Greedily prefer minimal support / unit rows: works for the half-delta
  staircase if exact unit rows are present, but it is not a theorem. In the
  dense-pair example the bad row 0 has very small support in the actual row,
  while the favorable signed rows have broader signed support. A minimal-support
  rule can therefore select the bad chart.
* Minimize SF over theta-quasi-max bases: registry-ready, deterministic after
  lexicographic tie-break, collapses the audited examples, and feeds the chain.
  Its drawback is that it is variational rather than structural, but that is
  exactly the exists quantifier.
* Maximize volume after projecting out near-duplicate directions: not yet a
  well-defined invariant rule. It depends on thresholds and a projection metric,
  and there is no proof that it reduces SF in the dense-pair or staircase
  families.

Recommended chart selector for the campaign: the min-SF theta-quasi-max
selector above.

## Q4. Status Of The Conjecture Shape

The honest current status is:

1. The chain composes with exists-quasi-max SF. The open problem is now the
   registry contract stated at the top, especially for `delta0 <= 0.3`.
2. No audited link genuinely needs a for-all or canonical max-volume chart.
3. If a future formulation insists on every max-volume chart, or on an arbitrary
   lexicographic max-volume chart that may pick the identity chart, then the
   half-delta staircase kills dimension-free SF at `delta0 >= 1/2`: at the
   endpoint it has `SF/delta=m` in one legal max-volume chart.
4. Below `1/2`, the staircase does not kill the route. Its audited envelope is
   consistent with growth like `1/(1-2 delta0)` as `delta0 -> 1/2-`, and for
   `delta0 <= 0.3` the tested ratios stay around `1` to `5/3`.

## Calibrations

* `P(chain only needs an exists selected chart, not for-all max-volume) = 0.88`.
* `P(theta-quasi robustness constants above survive audit) = 0.78`.
* `P(min-SF theta-quasi selector is the correct registry tie-break) = 0.86`.
* `P(greedy minimal-support/unit-row selector works in full generality) = 0.30`.
* `P(projected-volume tie-break becomes a clean theorem without new structure) = 0.25`.
* `P(exists-quasi SF is true for delta0 <= 0.3) = 0.60`.
* `P(for-all max-volume SF is false at delta0 >= 1/2 by the half-delta staircase) = 0.99`.

No `answer.md` was created.
