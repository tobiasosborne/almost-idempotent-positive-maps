# VERDICT: DIED-AT, WITH BOUNDED SEARCH EVIDENCE

I did not find a counterexample family to SF.  I also did not prove SF.
The useful output is a fairly sharp obstruction diagnosis for the advertised
transverse-pair conspiracy:

* In the exact transverse-pair family, and in duplicated copies of it, the
  signed-face excess is `Theta(delta)` with ratio tending to `1`, not growing.
* In graph-shaped stacks of many transverse pairs, the fixed intended chart
  again has `SF/delta ~= 0.99` at amplitude `0.01`, independent of the number
  of edges tested.
* Recomputing max-volume bases exposes determinant-one tie charts with larger
  ratios, but the largest structured family found is a path-basis tie whose
  ratio climbs toward `2`, not infinity.
* The w25 split-block `1/delta` coefficient blow-up does not survive the
  max-volume chart audit: the exact split-block instances have SF exactly `0`
  in the recomputed max-volume chart.
* Random small-delta idempotent conjugation searches did not beat `0.901`.

Calibration:

\[
P(\text{a transverse-stack counterexample exists}) \approx 0.04,\qquad
P(\text{some different small-delta SF counterexample exists}) \approx 0.12,
\qquad
P(\text{this DIED-AT diagnosis survives audit}) \approx 0.76.
\]

No `answer.md` was created.

## 1. H-M converse implementation

I used the Hognas-Mukherjea 1.12 converse in the `P = L B` form.  The rows of
`L` are coefficient vectors, the rows of `B` are the representative rows, and

\[
B L = I.
\]

Then

\[
P = L B,\qquad P^2 = L(BL)B = LB=P.
\]

If every row of `L` has coordinate sum `1`, then `P 1 = 1` follows from
`BL=I`.  This is the row-stochastic specialization of the theorem's converse.

I byte-checked the relevant theorem anchors:

```text
2246:Theorem 1.12. Let P be a d ... d idempotent matrix of rank k.
2276:Conversely any real matrix P with a partition ...
2337:Conversely, conditions (1.1)-(1.4) imply that P is idempotent.
```

The `gurobi_cl` and `gurobipy` optimizers were installed, but optimization was
blocked in this sandbox by a license HostID mismatch.  The saved failure is
`tiny_gurobi_test.out`, and the failed Python run is `sf_gurobi_failure.out`.
I therefore used SciPy HiGHS for the fixed-`L` LP searches.  In this
representation those searches are linear, not nonlinear: the idempotence has
already been enforced by `BL=I`.

## 2. Exact rational auditor

Script: `sf_exact.py`.

The auditor checks exactly, over rationals:

* `P^2=P`,
* `P1=1`,
* all row negative masses,
* rank and max-volume actual-row basis by exact Gram determinants,
* coefficients in the recomputed max-volume chart,
* SF for every representative row.

It produced:

```text
sf_exact_results.json
sf_exact_summary.txt
```

## 3. Exact transverse-pair family

For amplitude `a` and mass `m`, use coefficient rows

\[
e_0,\ e_1,\ e_2,\ e_0+a(e_1-e_2),\ e_0-a(e_1-e_2),
\]

and

\[
c={a\over 1+4a^2}.
\]

The representative rows are

\[
B_0=(1-m,0,0,m/2,m/2),
\]

\[
B_1=(0,1-2ac,2ac,c,-c),
\qquad
B_2=(0,2ac,1-2ac,-c,c).
\]

This gives an exact rational idempotent.  In the intended max-volume chart,

\[
\delta={a\over 1+4a^2},\qquad
\mathrm{SF}=ma,\qquad
{\mathrm{SF}\over \delta}=m(1+4a^2).
\]

With `m=99/100`, the exact runs gave:

```text
a=1/200: delta=50/10001, SF/delta=990099/1000000
a=1/100: delta=25/2501,  SF/delta=247599/250000
a=1/50:  delta=25/1252,  SF/delta=30987/31250
a=1/20:  delta=5/101,    SF/delta=9999/10000
```

So the ratio tends to `0.99` as `a -> 0`.  Taking `m -> 1` would make the
small-amplitude ratio tend to `1`, not infinity.

## 4. Duplicate-pair stacking fails

I duplicated the same transverse pair `q` times and split the row `B_0` mass
equally among the copies.  The dual rows `B_1,B_2` split their signed entries
among the copies too.  Exact max-volume recomputation keeps the ratio unchanged:

```text
q=2:  SF/delta=247599/250000
q=5:  SF/delta=247599/250000
q=10: SF/delta=247599/250000
q=25: SF/delta=247599/250000
```

This is the cleanest answer to the "shared negativity budget" attempt:
duplicates do share the same representative-row negative entry, but the row
`B_0` has fixed total positive mass.  Splitting that mass among more copies
does not increase total SF.

## 5. Split-block instability does not survive max-volume

The w25 split-block family has huge exact H-M coefficients in the too-fine
singleton chart.  The exact rational audit recomputed the max-volume basis
instead of trusting that chart.  For

```text
eps=1/100, 1/1000, 1/10000
```

the max-volume pivots were `[0,2]`, `max|a|=1`, and

```text
SF/delta=0
```

for all tested eps.  This rules out the direct `1/delta`-coefficient pumping
mechanism in the SF chart.

## 6. Fixed-L LP stacks

Script: `sf_lp_search.py`.

For a fixed coefficient matrix `L`, the LP chooses arbitrary geometry `B`
subject only to

\[
B L=I,\qquad \nu_i(P)\le \delta,\qquad P=LB.
\]

Thus this is a geometry-free test of whether the transverse coordinates can be
realized with less negativity by making representative rows nearly degenerate.

I tested paths, cycles, stars, complete graphs, and duplicate stacks with
amplitude `a=0.01` and `B_0` mass `0.99` on the signed rows.  In the intended
chart all fixed-mass graph stacks were essentially flat:

```text
single k=3:  SF/delta=0.990396
path k=10:   SF/delta=0.990223
cycle k=10:  SF/delta=0.990198
star k=10:   SF/delta=0.990223
duplicate q=25: SF/delta=0.990396
```

I also ran row-0-nonnegative max-SF LP checks under a cap on the common
negative mass.  At the minimum feasible cap the optimum always gave
`SF/cap ~= 1`; increasing the cap just decreases `SF/cap` because the same
balanced signed pair already uses the available row-0 mass.

Representative lines:

```text
single k=3 cap=min:     SF/cap=1.0003
duplicate q=5 cap=min:  SF/cap=1.0003
cycle k=5 cap=min:      SF/cap=1.0001
complete k=5 cap=min:   SF/cap=1.00017
cycle k=8 cap=min:      SF/cap=1.0001
```

## 7. Max-volume tie charts

Script: `sf_tie_scan.py`.

Because max-volume bases are not always unique, I scanned all coefficient
minors with maximal determinant for the smaller graph cases.  This found a
real tie-basis effect: selecting one signed row as a representative can raise
the displayed SF ratio.  The effect still looks bounded.

Best scanned ratios:

```text
path k=4:      1.24757
path k=5:      1.49510
path k=6:      1.61885
path k=8:      1.74261
cycle k=8:     1.70728
complete k=6:  1.59420
duplicate q=25: 1.00000
```

For the path pattern, I evaluated the observed best tie basis directly through
rank `20`:

```text
path k=10: ratio=1.80445598
path k=12: ratio=1.84158513
path k=15: ratio=1.87587324
path k=20: ratio=1.90759158
```

This strongly suggests a limiting constant `2`, not growth.

## 8. Random small-delta search

Script: `sf_random_search.py`.

I generated nonnegative stochastic idempotents and conjugated them by random
row-sum-preserving similarities, binary-searching to target small row-negative
mass.  For each sample I recomputed the max-volume chart and evaluated SF.

Saved outputs:

```text
sf_random_results.json
sf_random_summary.txt
```

Summary:

```text
samples=240 good=240
best=0.901039
median=0.189689
p90=0.482976
p99=0.705014
```

This did not find any hidden high-ratio small-delta instance.

## 9. Candidate obstruction lemma

The finite-dimensional obstruction suggested by all searches is:

**Candidate transverse-flow lemma.**  Let `L` consist of a max-volume chart with
representatives `e_0,...,e_{k-1}` and signed-face atoms

\[
e_0+x_j,\qquad \sum_{t\ne0} x_{j,t}=0,\qquad \|x_j\|_\infty\le a,
\]

with all `k x k` minors of `L` bounded by `1` in absolute value.  Let `B` be
any real left inverse, `BL=I`, and put `P=LB`.  If every row of `P` has negative
mass at most `delta`, then for the intended chart

\[
\sum_j (B_{0j})_+ E_0(j) \le (1+O(a))\delta.
\]

For determinant-one max-volume tie charts generated by replacing `e_0` with a
single signed-face atom, the corresponding bound should be

\[
\mathrm{SF}\le (2+O(a))\delta.
\]

In graph language, the signed-face atoms are edges and `BL=I` is a dual-flow
constraint.  A positive row-0 circulation on signed atoms must be balanced by
opposite signs in the foreign dual rows.  Duplicating edges can split this dual
flow, but cannot increase the row-0 mass; graph stacks move the same unit of
flow through more coordinates, and the max negative row remains at the same
scale as the total signed-face excess.

This is not a proof of SF, because I did not extract a rational LP dual
certificate for the general atom set and did not handle arbitrary max-volume
coefficient configurations.  It is, however, the precise wall hit by the
refutation attempt: every tested way of making many transverse pairs share the
same negativity budget reduces to a bounded dual-flow problem.

## 10. Artifacts

Code and outputs saved in this workdir:

```text
progress.md
proof.md
sf_exact.py
sf_exact_results.json
sf_exact_summary.txt
sf_lp_search.py
sf_lp_results.json
sf_lp_summary.txt
sf_tie_scan.py
sf_tie_scan_results.json
sf_tie_scan_summary.txt
sf_random_search.py
sf_random_results.json
sf_random_summary.txt
path_pattern_growth.txt
tiny_gurobi_test.lp
tiny_gurobi_test.out
sf_gurobi_search.py
sf_gurobi_failure.out
tax_audit_existing_stdout.txt
```

Verification commands run successfully:

```text
python3 -m py_compile sf_exact.py
python3 sf_exact.py
python3 -m py_compile sf_lp_search.py
python3 sf_lp_search.py
python3 -m py_compile sf_tie_scan.py
python3 sf_tie_scan.py
python3 -m py_compile sf_random_search.py
python3 sf_random_search.py --samples 240
```

`sf_gurobi_search.py` compiled, but Gurobi optimization itself did not run due
to the saved HostID license mismatch.
