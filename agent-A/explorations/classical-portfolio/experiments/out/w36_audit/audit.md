# Hostile audit of w35_quantifier and w35_charge

## Verdict table

| item | verdict | P | one line |
|---|---:|---:|---|
| B1 constants chain | CONFIRMED, with minor threshold correction | 0.92 | `C_mu=C_sf+1+A`, `C_D=4(1+2delta_0)(C_sf+1+A)`, `L_eta`, and L4 substitution are right; the later `delta_sm` "equivalent" formula is only a conservative sufficient bound. |
| B2 routing caveat consistency | CONFIRMED | 0.94 | `w35_charge` uses the sign fact only in exact max-volume charts (`theta=1`), where it is valid; it does not cover `theta<1`. |
| B3 end-to-end chain | CONFIRMED AS CONDITIONAL | 0.86 | The registry SF contract implies the W-free `O(sqrt(delta))` theorem through the routed links, but several upstream notes are `DIED-AT` and are only being used conditionally. |
| B4 selection and stress checks | CONFIRMED | 0.99 | Re-run and independent actual-Gram enumeration reproduce best max-ratio exactly `1`; tie enumeration is exhaustive over all row bases. |
| B5 `(CHARGE)` formulation | CONFIRMED, but mostly tautological | 0.90 | `(CHARGE)` is sufficient for exact `theta=1` registry SF and uses one common `U_*`; as written it is essentially equivalent to the desired SF bound unless more structure is imposed on `q`. |
| B6 fresh eyes / perturbed staircase | CONFIRMED | 0.99 | There is an exact epsilon-perturbed staircase with unique exact max-volume bad chart and ratio `m-3epsilon`; the good charts re-enter exactly at `theta <= 1-epsilon`. |

## Artifacts and commands

I read the requested wave-35 notes and upstream notes under:

```text
/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/swarm-answers/
```

I copied `experiments/out/w35_charge/stress_checks.py` unchanged into the writable workdir because the source tree is read-only in this sandbox. Verification:

```text
python3 -m py_compile w35_charge/stress_checks.py
python3 w35_charge/stress_checks.py
python3 -m py_compile independent_minmax_check.py
python3 independent_minmax_check.py
```

Saved outputs:

```text
w35_charge/stress_checks.json
w35_charge/stress_checks_summary.txt
independent_minmax_check.py
independent_minmax_check.out
progress.md
audit.md
```

No `answer.md` was created.

## B1. Constants chain

Let `U={u_s}` be a selected actual-row basis and write

```text
p_j = sum_t a_t(j) r_t,     r_t = p_{u_t},
sum_t a_t(j)=1,             P a_t = a_t.
```

For a `theta`-quasi-max chart, Cramer gives `|a_t(j)| <= A=1/theta`. Put

```text
lambda_s(j)=1-a_s(j),
mu_s(j)=sum_{t != s} (-a_t(j))_+,
E_s(j)=(mu_s(j)-lambda_s(j))_+.
```

Assume the registry SF estimate in this selected chart:

```text
sum_j (P_{u_s j})_+ E_s(j) <= C_sf delta.
```

Since `P lambda_s = lambda_s` and `lambda_s(u_s)=0`,

```text
sum_j P_{u_s j} lambda_s(j)=0.
```

Also `|lambda_s(j)| <= 1+A`. Therefore

```text
sum_j (P_{u_s j})_+ lambda_s(j)
    = - sum_{P_{u_s j}<0} P_{u_s j} lambda_s(j)
    <= (1+A) delta.
```

Pointwise,

```text
mu_s <= (mu_s-lambda_s)_+ + lambda_s.
```

So the transverse tax obeys

```text
M_s := sum_j (P_{u_s j})_+ mu_s(j)
     <= (C_sf + 1 + A) delta.
```

Thus the advertised

```text
C_mu = C_sf + 1 + A
```

is correct.

The positive scalar deficit is also bounded. From the same signed identity,

```text
sum_j (P_{u_s j})_+ lambda_s(j)_+
 <= sum_j (P_{u_s j})_+ lambda_s(j)_- + (1+A) delta.
```

When `lambda_s(j)<0`, `E_s(j) >= -lambda_s(j)`, so

```text
sum_j (P_{u_s j})_+ lambda_s(j)_+ <= (C_sf+1+A) delta.
```

For `v(j)=a(j)-e_s`,

```text
||v(j)||_1 = 2(mu_s(j)+lambda_s(j)_+)
```

even when `lambda_s` is signed. Since each pivot row has `||r_t||_1 <= R0=1+2delta_0`,

```text
D_s := sum_j (P_{u_s j})_+ ||p_j-r_s||_1
    <= 4 R0 (C_sf+1+A) delta.
```

Therefore

```text
C_D = 4(1+2delta_0)(C_sf+1+theta^{-1})
```

is correct. For exact max-volume (`theta=1`) the old sign `lambda_s>=0` gives the sharper but non-robust constant `2(1+2delta_0)(C_sf+4)`.

The `L_eta` line is also correct:

```text
L_eta := max_s sum_{j notin M_s} |P_{u_s j}|
       <= C_D delta/eta + delta.
```

The positive outside mass is Markov from `D_s`; the negative outside mass is at most the row negative mass `delta`.

The L4 substitution is correct:

```text
||P-Q||_{infty,1}
 <= eta + 12 L_eta + 24 delta
 <= eta + 12 C_D delta/eta + 36 delta.
```

Minor correction: the later small-regime condition in `w35_quantifier` is not equivalent as written. From `eta=sqrt(delta)` and `L_eta<=1/8`, the exact root condition is

```text
x^2 + C_D x <= 1/8,   x=sqrt(delta),
x <= (sqrt(C_D^2+1/2)-C_D)/2.
```

The note's `(sqrt(C_D^2+1/8)-C_D)^2` is a stricter sufficient bound, not an equivalent threshold. This does not harm the theorem, but the word "equivalently" is wrong.

## B2. Routing caveat consistency

`w35_charge` Section 2 uses

```text
0 <= 1-a_s(j) <= 2.
```

That is valid in every exact max-volume chart because exact maximality gives `|a_s(j)|<=1`. The selected chart `U_*` in `w35_charge` is an argmin over exact max-volume ties only, so the banked deficit bound is valid for every candidate in that argmin set.

There is no internal inconsistency for `theta=1`.

There is a real coverage gap for `theta<1`. In a `theta`-quasi chart, Cramer only gives `|a_s(j)|<=1/theta`, so `1-a_s(j)` can be negative. The exact banked deficit proof in `w35_charge` cannot be reused. The robust replacement is exactly the B1 derivation:

```text
C_mu = C_sf + 1 + theta^{-1}.
```

Documents together cover:

```text
w35_charge:
  theta = 1 exact max-volume selection U_*.
  Partial target mainly delta_0 = 1/4.
  If exact (CHARGE) is proved, it gives exact SF for U_*.

w35_quantifier:
  delta_0 <= 0.3, any fixed theta in (0,1].
  Conditional chain from a theta-quasi SF registry contract to W-free O(sqrt(delta)).

combined:
  exact theta=1 CHARGE + delta_0 <= 1/4 => global theorem by w35_quantifier.
  theta<1 theorem requires a separate theta-quasi SF/CHARGE contract.
```

So the final theorem must not claim that `w35_charge` proves the `theta<1` registry contract.

## B3. End-to-end composed theorem

A correct composed theorem is:

```text
Fix delta_0 <= 0.3 and theta in (0,1].
Let C_sf(delta_0,theta)<infty.
Assume that every finite row-stochastic idempotent P with
delta(P):=max_i sum_j (-P_ij)_+ <= delta_0
has an actual-row basis U={u_1,...,u_k} such that

  Vol(U) >= theta Vol_max(P)

and, in that one chart,

  max_s SF_s(U) <= C_sf(delta_0,theta) delta(P).

Then there is a nonnegative Hognas-Mukherjea stochastic idempotent Q with

  ||P-Q||_{infty,1} <= K(delta_0,theta,C_sf) sqrt(delta(P)).
```

More explicitly, with

```text
C_D = 4(1+2delta_0)(C_sf+1+theta^{-1}),
```

for any `eta <= theta/4` and `L_eta <= 1/8`,

```text
||P-Q||_{infty,1}
 <= eta + 12 C_D delta/eta + 36 delta.
```

For small `delta`, choose `eta=sqrt(delta)`. For larger `delta` inside the fixed cap, use the coarse fallback to a fixed rank-one stochastic idempotent; since `||P||_{infty,1} <= 1+2delta_0`, this only worsens the fixed constant.

Upstream status audit:

```text
w26_cluster_audit: HOLDS WITH IMPROVEMENT.
w27_concentration: DIED-AT; only in-class, cross-cluster, and conditional L4 are banked.
w28_face: DIED-AT; representative displacement was missing there.
w30_maxvol: DIED-AT; it reduced displacement to transverse tax.
w31_tax: DIED-AT; it reduced tax to signed-face excess.
w34_audit: core tie computations confirmed; A3 path limit unresolved.
w34_halfcex: MIXED; exact tie ambiguity and threshold conjecture.
w35_charge: PARTIAL; exact theta=1 CHARGE not proved.
```

This is why B3 is confirmed only as a conditional chain. The registry SF contract supplies exactly the missing estimates from w31/w30/w28/w27; without that contract, the upstream notes do not prove the global theorem.

## B4. Selection well-definedness and stress checks

The re-run of the copied `stress_checks.py` produced:

```text
transverse_pair_a1_4: delta=1/5 ties=3 best_basis=[1, 2, 3] best_max_ratio=1 worst_max_ratio=5/4 checks=BL:True P2:True rows:True
dense_pair_k7_a1_4: delta=6/17 ties=3 best_basis=[1, 2, 3, 4, 5, 6, 7] best_max_ratio=1 worst_max_ratio=17/8 checks=BL:True P2:True rows:True
staircase_m2_a1_2: delta=1/2 ties=7 best_basis=[1, 2, 3, 4, 5] best_max_ratio=1 worst_max_ratio=2 checks=BL:True P2:True rows:True
staircase_m3_a1_2: delta=1/2 ties=9 best_basis=[1, 2, 3, 4, 5, 6, 7] best_max_ratio=1 worst_max_ratio=3 checks=BL:True P2:True rows:True
```

The independent verifier used actual-row Gram determinants `det(P_U P_U^T)`, not coefficient minors, and recomputed coordinates from actual rows:

```text
transverse_pair_a1_4: delta=1/5 ties=3 best_basis=[1, 2, 3] best_ratio=1 worst_ratio=5/4
dense_pair_k7_a1_4: delta=6/17 ties=3 best_basis=[1, 2, 3, 4, 5, 6, 7] best_ratio=1 worst_ratio=17/8
staircase_m2: delta=1/2 ties=7 best_basis=[1, 2, 3, 4, 5] best_ratio=1 worst_ratio=2
staircase_m3: delta=1/2 ties=9 best_basis=[1, 2, 3, 4, 5, 6, 7] best_ratio=1 worst_ratio=3
```

The tie enumeration in `stress_checks.py` is exhaustive for these finite instances:

```python
for basis in itertools.combinations(range(L.rows), k):
    det = L[list(basis), :].det()
```

It scans all `k`-row subsets, discards singular bases, and collects all bases whose exact determinant equals the maximum. This is not heuristic. The coefficient-minor scan is valid by `w34_audit` A7; the independent actual-Gram scan confirms it.

## B5. `(CHARGE)` formulation

`(CHARGE)` says that for the selected exact max-volume chart `U_*`, for every `s`,

```text
sum_j (P_{u_s j})_+ E_s(j) <= sum_i q_{s i} nu_i(P),
sum_i q_{s i} <= C(delta_0),    q_{s i} >= 0.
```

Since every `nu_i(P) <= delta(P)`, this gives

```text
SF_s(U_*) <= C(delta_0) delta(P)
```

for every `s`, hence

```text
max_s SF_s(U_*) <= C(delta_0) delta(P).
```

No per-`s` chart switch is hidden: `U_*` is fixed first, and the statement quantifies over every representative `s` in that same chart. This is sufficient for the exact `theta=1` registry contract.

Nothing is lost relative to the exact chain except quasi robustness: `(CHARGE)` as written is a `theta=1` exact-max statement and does not imply the `theta<1` registry contract.

Suspicious point: with no support, locality, or construction rule imposed on `q`, `(CHARGE)` is almost just a restatement of the SF bound. If `delta>0` and some row attains `nu_i=delta`, then any already-known bound `SF_s<=C delta` gives `(CHARGE)` by placing all charge on that row. Thus `(CHARGE)` is not a genuine reduction unless future work adds structural restrictions on the charge assignment.

## B6. Fresh eyes and perturbed staircase

The endpoint staircase collapse in `w35_charge` relies on exact max-volume ties. A tiny row-sum-preserving coefficient perturbation breaks those ties and makes the exact `theta=1` selection choose only the bad identity chart.

Here is an exact rational family.

Let `m>=2`, `k=2m+1`, and let

```text
sigma_t = +1 for 1<=t<=m,
sigma_t = -1 for m<t<=2m.
```

Fix rational `epsilon` with

```text
0 < epsilon < m/(2m+1).
```

This smallness condition keeps the identity basis uniquely maximal and also makes the displayed bad excess positive. Put

```text
h = 1-epsilon,
d = epsilon/(2m).
```

Define `L` with rows

```text
e_0, e_1, ..., e_{2m},
x_+ = h e_0 + sum_{t=1}^{2m} (d + sigma_t/2) e_t,
x_- = h e_0 + sum_{t=1}^{2m} (d - sigma_t/2) e_t.
```

Every row of `L` sums to `1`. Let the last two columns be `p,n`. Define `B` by

```text
B_{0,0}=epsilon,
B_{0,t}=-d                    for 1<=t<=2m,
B_{0,p}=B_{0,n}=1/2,

B_{r,t}=1_{r=t} - sigma_r sigma_t/(2m)     for 1<=r,t<=2m,
B_{r,p}= sigma_r/(2m),
B_{r,n}=-sigma_r/(2m),
B_{r,0}=0.
```

Then exact algebra gives

```text
B L = I,
P := L B is idempotent,
P 1 = 1.
```

The row negative masses are:

```text
row 0: epsilon,
foreign representative rows: 1/2,
signed rows x_+, x_-: epsilon/2.
```

So

```text
delta(P)=1/2.
```

Max-volume under the displayed epsilon condition:

```text
Vol(identity coefficient basis) = 1.
Every non-identity basis has volume <= 1-epsilon.
There are 2m+2 bases at volume exactly 1-epsilon.
```

Therefore the exact max-volume class at `theta=1` is a singleton: the identity chart.

In the identity chart, the bad representative is `s=0`. For each signed row,

```text
lambda_0 = 1-h = epsilon,
mu_0 = m(1/2-d) = m/2 - epsilon/2,
E_0 = mu_0-lambda_0 = m/2 - 3epsilon/2.
```

The positive `B_0` mass on `x_+` and `x_-` is `1/2+1/2=1`, hence

```text
Phi(U_identity) = SF_0 = m/2 - 3epsilon/2
Phi(U_identity)/delta = m - 3epsilon.
```

Thus, for `delta_0=1/2`, exact `theta=1` exists-max-volume SF is false with unbounded rank: choose `m` larger than any proposed constant and `epsilon` small.

The formerly favorable charts are not gone; they are near-ties. The `2m+2` bases at volume ratio `1-epsilon` have

```text
max_s SF_s/delta = 1.
```

Therefore the minimal quasi slack for this perturbation is exact:

```text
theta <= 1-epsilon   includes the good charts and gives ratio 1,
theta > 1-epsilon    excludes them and leaves only the bad exact chart near the top.
```

Concrete independent check for `m=5`, `epsilon=1/1000`:

```text
perturbed_staircase_m5_eps1e-3_exact:
  delta=1/2
  exact max-volume ties=1
  best_ratio=worst_ratio=4997/1000

theta >= 999/1000:
  count=13
  best_ratio=1
  best_vol_ratio=999/1000
```

This refutes the broad endpoint optimism in `w35_charge` ("no counterexample to Phi(U*) <= delta is known" at `delta=1/2`) for exact `theta=1`. It does not refute the small-cap `delta_0<=0.3` campaign; the construction sits exactly at `delta=1/2`, and the older threshold data still suggest bounded envelopes below `1/2`.

But it does prove that `theta<1` slack is not optional if the endpoint or perturbative robustness is part of the intended theorem.

Other suspicious points:

1. The `delta_sm` formula in `w35_quantifier` is conservative, not equivalent.
2. `(CHARGE)` needs structural constraints on `q` to be more than a repackaged SF inequality.
3. The exact max-volume selector is discontinuous at the staircase endpoint: arbitrarily small `epsilon` changes the exact tie class from many low-SF charts to a singleton high-SF chart.
