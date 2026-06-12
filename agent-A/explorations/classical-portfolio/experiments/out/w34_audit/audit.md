# Hostile audit of wave-33 SF claims

Artifacts produced in this directory:

- `audit_compute.py`, `audit_compute.json`, `audit_compute_summary.txt`
- `fixed_support_lp_check.py`, `fixed_support_lp_check.out`
- `path_tail_fit.py`, `path_tail_fit.out`
- `hm_anchor_check.py`, `hm_anchor_check.out`
- `progress.md`

No `answer.md` was created.

## Verdict Table

| item | verdict | P(verdict correct) | one-line reason |
|---|---:|---:|---|
| A1 transverse-pair exact family | CONFIRMED, with tie caveat | 0.92 | `BL=I`, `P^2=P`, row sums, delta, and the intended-chart ratio `m(1+4a^2)` check exactly; other max-volume tie bases give different SF. |
| A2 duplicate-stacking invariance | CONFIRMED | 0.88 | Asymmetric fixed splits do not improve the ratio; exhaustive small-q LP and large-q row0-nonnegative LP hit the same single-pair constant. |
| A3 tie-chart path ratios and limit 2 | UNRESOLVED | 0.84 | k=10 and k=20 ratios reproduce, and tail fits favor saturation near 2, but the worker's evidence is not a proof against slower growth. |
| A4 fixed-support certificates | CONFIRMED | 0.90 | Symbolic active solutions give `1+4a^2` and `1+3a^2`; sign-chamber LP checks are tight at those constants. |
| A5 k=7 dense-pair instance | CONFIRMED | 0.96 | Exact rational recomputation gives delta `6/17`, SF `3/4`, ratio `17/8`; tie bases exist but have lower SF. |
| A6 orchestrator refutation of convexity estimate | CONFIRMED | 0.98 | `E_0` is convex and the k=7 instance satisfies the hypotheses; the proposed inequality has Jensen in the wrong direction. |
| A7 H-M `P=LB, BL=I` equivalence and anchors | CONFIRMED | 0.93 | The factorization is equivalent for rank-k idempotents with independent representative rows; OCR anchors and rank assumptions check out. |

## A1. Exact transverse-pair family

Independent script: `audit_compute.py`, section `A1_transverse_pair`.

For

```text
L = [e0, e1, e2, e0+a(e1-e2), e0-a(e1-e2)]
c = a/(1+4a^2)
B0 = (1-m,0,0,m/2,m/2)
B1 = (0,1-2ac,2ac,c,-c)
B2 = (0,2ac,1-2ac,-c,c)
```

Sympy verifies `B L = I`, all rows of `L` and `B` sum to 1, hence `P=L B` has `P^2=P` and `P 1=1`.

The intended chart `[0,1,2]` has

```text
SF = m a
delta = c = a/(1+4a^2)
SF/delta = m(1+4a^2)
```

For `a=1/100`, `m=99/100`, my exact sample gives:

```text
delta = 25/2501
SF = 99/10000
SF/delta = 247599/250000
claimed m(1+4a^2) = 247599/250000
```

Conditions the worker did not spell out cleanly: the displayed delta formula assumes `m/2 >= 2 a c`, and the intended max-volume minor is tied for max only in the relevant `a <= 1/2` regime. Outside that regime, the chart/negative-mass statement can change.

Tie caveat: the max-volume chart is not unique. Exact minors for the sample have max ties:

```text
[0,1,2], [1,2,3], [1,2,4]
```

The identity chart gives the worker's ratio. The two signed-row tie charts give ratio exactly `1` in the sample:

```text
[0,1,2]: pivot 0 SF=99/10000, SF/delta=247599/250000
[1,2,3]: pivot 3 SF=25/2501, SF/delta=1
[1,2,4]: pivot 4 SF=25/2501, SF/delta=1
```

So there is no algebra slip in the intended formula, but it is not a tie-invariant statement about every max-volume basis.

## A2. Duplicate-stacking invariance

Independent scripts: `audit_compute.py`, section `A2_duplicate_asymmetry`.

I tested q=5 duplicate supports with `a=0.01`, `m=0.99`, fixing row `B0` with asymmetric mass splits and then minimizing delta over all dual rows `B1,B2`.

```text
symmetric:              delta=0.009996001599360257, target=0.0099, ratio=0.990396
concentrated_one_copy:  delta=0.009996001599360363, target=0.0099, ratio=0.990396
skewed_geometric:       delta=0.009996001599360257, target=0.0099, ratio=0.990396
unbalanced 70/30 signs: delta=0.013954418232706918, target=0.0099, ratio=0.709453
```

Balanced asymmetric splitting across copies does not change the optimum. Deliberately unbalancing plus/minus mass forces negative basis entries in `B0` and makes the ratio worse.

I also ran full sign-chamber LPs for arbitrary `B0` signs for q=2,3,4 at the single-pair constant `C=1+4a^2=1.0004`:

```text
q2: margin=1.73e-18, ratio=1.0004
q3: margin=1.73e-18, ratio=1.0004
q4: margin=-0.0,     ratio=1.0004
```

For larger q I ran a row0-signed-nonnegative LP:

```text
q5:  target=0.010000000000000002, delta=0.009996001599360257, ratio=1.0004
q10: target=0.010000000000000002, delta=0.009996001599360257, ratio=1.0004
q25: target=0.01,                 delta=0.009996001599360257, ratio=1.0004
```

The exact reason is simple: duplicate coefficient rows are identical, and `BL=I` only sees aggregate plus-minus mass. A balanced split can be moved among duplicate columns with the dual flow moved with it. SF depends on total positive signed mass, not how that mass is distributed among identical copies.

## A3. Tie-chart path family

Independent scripts: `audit_compute.py`, section `A3_path_tie_growth`, and `path_tail_fit.py`.

I reproduced the spot checks:

```text
k=10 ratio=1.8044559844
k=20 ratio=1.9075915833
```

Extended direct pattern checks:

```text
k=4  ratio=1.2475742500
k=5  ratio=1.4950986667
k=6  ratio=1.6188046875
k=8  ratio=1.7426065833
k=10 ratio=1.8044559844
k=12 ratio=1.8415851300
k=15 ratio=1.8758732426
k=20 ratio=1.9075915833
k=30 ratio=1.9370655140
k=40 ratio=1.9510162417
```

Tail fits from `path_tail_fit.out`:

```text
cutoff k>=10: free L=2.00245, forced-2 rmse=0.00268, log pred100=2.05802
cutoff k>=12: free L=1.99935, forced-2 rmse=0.00148, log pred100=2.04053
cutoff k>=20: free L=1.99478, forced-2 rmse=0.00146, log pred100=2.01060
```

This is strong numerical evidence for saturation around 2. It is not a proof. The worker's "strongly suggesting limit 2" is acceptable as a heuristic summary, but not as a load-bearing mathematical claim. A logarithmic curve is a worse fit on the tail, but it is not excluded by the worker's finite data alone.

## A4. Fixed-support certificate formulas

Independent scripts: `audit_compute.py`, section `A4_fixed_support_formulas`; `fixed_support_lp_check.py`.

For the k=3 signed pair, the active solution is the transverse-pair construction with `m=1`:

```text
c = a/(1+4a^2)
target = a
delta = a/(1+4a^2)
ratio = 1+4a^2
```

Sympy verifies `BL=I` and `P^2=P`, with active row negative masses:

```text
0, c, c, c, c
```

For the k=4 cycle/all-pairs support on foreign coordinates 1,2,3, orient the three edges `(1,2),(2,3),(3,1)`. Put `B0=1/6` on each of the six signed atoms. For a foreign row, put `+c,-c` on each incident signed pair according to incidence, with

```text
c = a/(2(1+3a^2))
delta = 2c = a/(1+3a^2)
target = a
ratio = 1+3a^2
```

The basis entries are `1-4ac` on the diagonal and `2ac` on the other two foreign basis columns. Sympy verifies `BL=I`, `P^2=P`, and active row negative masses `delta` for all nine nonzero rows, under the same small-amplitude sign chamber (`0<a<=1/2`).

Sign-chamber LP tightness checks:

```text
pair a=0.2:  C=1.16, margin_at_C=-0.0, ratio=1.16
pair a=0.5:  C=2.00, margin_at_C=-0.0, ratio=2.00
cycle a=0.2: C=1.12, margin_at_C=4.16e-17, ratio=1.12
cycle a=0.5: C=1.75, margin_at_C=2.50e-16, ratio=1.75
```

At `C-1e-4`, the LP margin becomes positive in each case, so these constants are tight for the audited supports.

## A5. Dense-pair k=7 instance

Independent exact construction: `audit_compute.py`, section `A5_A6_dense_pair_and_convexity`.

For `k=7`, `a=1/4`, with

```text
x+ = e0 + (1/4)(e1+e2+e3-e4-e5-e6)
x- = e0 - (1/4)(e1+e2+e3-e4-e5-e6)
```

I reconstructed the exact rational `B` from the worker's description. Checks:

```text
BL=I: true
P^2=P: true
row sums: all 1
row negative masses: 0, then eight copies of 6/17
delta = 6/17
identity-chart SF = 3/4
identity-chart ratio = 17/8
```

Max-volume ties exist:

```text
[0,1,2,3,4,5,6]
[1,2,3,4,5,6,7]
[1,2,3,4,5,6,8]
```

The identity chart is the high-SF chart. The two signed-row tie bases are lower:

```text
identity basis: pivot 0 SF=3/4, ratio=17/8
x+ tie basis:  pivot 7 SF=6/17, ratio=1; pivots 4,5,6 SF=3/17, ratio=1/2
x- tie basis:  pivot 8 SF=6/17, ratio=1; pivots 1,2,3 SF=3/17, ratio=1/2
```

Thus the saved dense-pair verification is correct, and no hidden tie basis raises the ratio above `17/8`. But the ratio is chart-sensitive: choosing a different max-volume tie basis can make the displayed SF much smaller.

## A6. Orchestrator refutation of the convexity estimate

The worker's proposed estimate was:

```text
sum_j (B_sj)_+ F(L_j) <= nu_{u_s} max_j F(L_j)
```

For SF, `F=E_s`, where

```text
E_s(x) = max(sum_{t!=s} (-x_t)_+ - (1-x_s), 0).
```

This function is convex: `sum max(-x_t,0) + x_s - 1` is convex, and the max of that convex function with 0 is convex. Also `E_0(e0)=0`.

In the exact k=7 dense-pair instance:

```text
B0 = (0,0,0,0,0,0,0,1/2,1/2)
nu(P row 0) = 0
E0 values = 0 on basis rows, 3/4 on x+,x-
LHS = 3/4
delta * max E0 = (6/17)(3/4) = 9/34
```

So the proposed estimate fails both with row negativity `nu_{u_0}=0` and with global delta substituted. The instance satisfies the estimate's natural hypotheses: `BL=I`, `P=LB`, row sums, max-volume chart, and full-row negativity constraints.

Charitable repair: replacing `nu_{u_s}` by total positive mass of `B_s` gives the trivial true bound

```text
sum_j (B_sj)_+ F(L_j) <= (sum_j (B_sj)_+) max F.
```

For the dense pair this reads `3/4 <= 3/4`. It is not useful for proving SF because it does not charge full-row negativity. Any useful repair needs an additional hypothesis forcing positive `F`-mass in `B_s` to be balanced by negative coefficients or by full-row negative mass. That is exactly what the dense-pair instance violates. The orchestrator's refutation stands.

## A7. H-M factorization and anchors

Independent anchor check: `hm_anchor_check.py`, `hm_anchor_check.out`.

The cited OCR lines exist:

```text
2246:Theorem 1.12. Let P be a d \x03 d idempotent matrix of rank k. Then there is a
2276:    Conversely any real matrix P with a partition fT; B; C1 ; C2 ; : : : Ck g such that
2277:(i), (ii), (iii), and (iv) hold is idempotent of rank k.
2337:   Conversely, conditions (1.1)-(1.4) imply that P is idempotent.
```

The OCR caveats are real: line 2246 contains a control glyph for the multiplication sign in `d x d`, and line 2337 contains a UTF-8 en dash between `(1.1)` and `(1.4)`. Exact ASCII quotes from older notes are therefore not byte-identical.

Equivalence used by both workers:

If `P` is a rank-k idempotent and `u_1,...,u_k` are independent representative rows, write each row as

```text
p_i = L_i B
```

where `B` is the k-by-d matrix of representative rows and `L_i` is the coefficient row. For representative rows, `L_{u_s}=e_s`. Then `P=LB`. Idempotence gives, for row `u_s`,

```text
p_{u_s} P = p_{u_s}
sum_i P_{u_s i} L_i B = e_s B
```

Since the rows of `B` are independent, `B L = I`.

Conversely, if `P=L B` and `B L=I`, then

```text
P^2 = L B L B = L B = P.
```

Rank conditions: `BL=I_k` already forces `L` to have full column rank k and `B` to have full row rank k, so `rank(P)=k`. In the constructed instances, this is immediate because the first k rows of `L` are the identity. If one only had `P=LB` without `BL=I` or without full rank, the converse would fail; that is not the situation in the audited constructions.

Row-stochastic specialization: because every row of `L` sums to 1, `L 1_k = 1_d`. From `BL=I`, `B 1_d = B L 1_k = 1_k`; hence `P 1_d = L B 1_d = L 1_k = 1_d`. The cex LP script did not explicitly impose row sums on `B`, but `BL=I` plus row-sum-one `L` implies them.

Max-volume equivalence: for any k-row set `U`,

```text
P_U = L_U B
det(P_U P_U^T) = det(L_U)^2 det(B B^T),
```

since `B` has full row rank. Thus scanning coefficient minors of `L` is equivalent to scanning actual-row volumes of `P`. This validates the determinant scans used in the audited examples.

## Additional Suspicious Points

1. The prompt's experiment paths omit the `agent-A/explorations/classical-portfolio/` prefix. The artifacts are present, but not at `repo_root/experiments/out/...`.

2. Tie bases are under-emphasized in both wave-33 writeups. In A1 they change the transverse-pair ratio from the displayed `m(1+4a^2)` to `1` for the sample. In A5 they lower the dense-pair ratio from `17/8` to `1`. Neither breaks the boundedness conclusions, but any theorem statement must specify whether it is for every max-volume tie, some selected tie, or a deterministic tie-break.

3. The A1 formula should be read with its sign-chamber assumptions. If `m` is too small relative to `a`, or if `a>1/2`, the stated delta/max-volume chart conclusions can change.

4. The A3 "limit 2" language is too strong as evidence. The data through k=40 favors it strongly, especially on the tail, but it remains a conjectural pattern unless a recurrence/dual certificate is extracted.

5. The convexity route in w33_sf_geom is not just missing a constant; it is directionally wrong. Convexity gives lower Jensen control at `e_s`, not an upper bound on positive mass away from `e_s`.
