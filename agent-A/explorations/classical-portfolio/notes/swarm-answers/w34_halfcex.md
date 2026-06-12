# w34_halfcex — MIXED: the half-delta staircase is REAL in the best-tie chart (ratio = m, exact, m=2..8) and COLLAPSES to 1 in every other tie; delta* = 1/2; C(delta) ~ 1/(1-2delta) conjectured (codex, 2026-06-12)
# Brief: notes/briefs/w34_halfcex.md. Long form: experiments/out/w34_halfcex/proof.md.
# Worker survived a full network outage mid-run (websocket retry loop) and delivered on reconnect.

VERDICT: MIXED / MAX-VOLUME TIE AMBIGUITY — the statement-level fork is now exact.
- CLOSED FORM (general m, structural): L rows e_0..e_{2m}, x_pm = e_0 pm (1/2) sum sigma_t e_t;
  B explicit (B_{r,t} = 1_{r=t} - sigma_r sigma_t/(2m), pair entries pm sigma_r/(2m));
  P_p = e_p and P_n = e_n EXACTLY (the signed rows are exact unit rows — the source of the ties);
  row neg masses: row 0 and signed rows 0, every foreign representative EXACTLY 1/2.
- CHART RECOMPUTATION (exact, m=2,3,5,8): the intended identity chart REMAINS max-volume with
  SF/delta = m; it is tied with 2m+2 charts omitting row 0 (replacing it by e_p/e_n) where the
  ratio is EXACTLY 1. So: FOR-ALL-ties SF is FALSE at delta_0 = 1/2 (rank-unbounded);
  EXISTS-tie SF is UNREFUTED by everything tested. P(best-tie blow-up survives audit) = 0.99.
- THRESHOLD MAP (exact instances, caps 0.300..0.500, m <= 12): best-tie envelope grows toward
  the cap-1/2 endpoint (5/3 @ 0.300, 4 @ 0.375, 10 @ 0.450, m in general @ 0.500);
  delta* = 1/2 is a SUPREMUM (not attained below); conjectured envelope C(delta) ~ 1/(1-2delta).
  For cap <= 0.3 the family stays in ~1..2.
- MECHANISM (for the wave-35 tie-break rule): tied charts swap row 0 OUT for the exact signed
  unit rows; then the big split-mass row is no longer a representative and the displayed excess
  is only delta. "Prefer signed/unit rows as representatives" is the candidate deterministic rule.
- WAVE-35 FORK (carried in HANDOFF): (1) does the w30 displacement reduction tolerate a CHOSEN
  max-volume basis (=> exists-form SF + tie-break rule = the proof target, expected C ~ 5/3..2
  at delta_0 <= 0.3)? (2) if the chain forces for-all ties, the staircase refutes dimension-free
  SF for delta_0 >= 1/2 and the envelope constrains everything below.
---
## Appendix: proof.md (verbatim)

# VERDICT: MIXED / MAX-VOLUME TIE AMBIGUITY

The half-delta staircase survives exact chart recomputation in the strongest
`exists a max-volume chart` sense, but not in an `all max-volume charts` sense.

At `delta=1/2`, the intended identity chart is itself an exact max-volume
actual-row basis and gives

\[
\mathrm{SF}/\delta=m.
\]

However, it is tied with `2m+2` other max-volume bases.  Those other bases omit
row `0` and give best displayed ratio `1`.  Therefore the outcome is not a
clean chart artifact and not an unqualified chart-confirmed theorem unless SF
specifies the tie rule.

Practical registry statement:

* If SF must hold for every max-volume basis, or if an arbitrary legal
  max-volume tie choice may be the intended identity chart, then SF is false at
  `delta_0=1/2`.
* If SF only requires existence of a favorable max-volume tie chart, this
  family does not refute it; the favorable charts collapse the ratio to `1`.

Calibration:

* `P(exact family and best-tie blow-up survive independent audit) = 0.99`.
* `P(SF as currently worded is tie-ambiguous at this family) = 0.95`.
* `P(all-max-volume-chart blow-up claim survives) = 0.05`.
* `P(exists-good-chart boundedness for this family survives) = 0.90`.

No `answer.md` was created.

## 1. Closed Form

Use the block-sign version of the dense-pair family.  The odd/even description
in the prompt is a coordinate permutation of this convention.

Let

\[
k=2m+1,\qquad d=2m+3,\qquad p=k,\qquad n=k+1,
\]

and define

\[
\sigma_t=\begin{cases}
+1,&1\le t\le m,\\
-1,&m+1\le t\le 2m.
\end{cases}
\]

The support matrix `L` has rows

\[
e_0,\ldots,e_{2m},\qquad
x_+=e_0+\frac12\sum_{t=1}^{2m}\sigma_t e_t,\qquad
x_-=e_0-\frac12\sum_{t=1}^{2m}\sigma_t e_t.
\]

The closed-form left inverse `B` is:

\[
B_{0,p}=B_{0,n}=\frac12,\qquad B_{0,j}=0\quad(j\ne p,n),
\]

and, for `1 <= r <= 2m`,

\[
B_{r,0}=0,\qquad
B_{r,t}=\mathbf 1_{r=t}-{\sigma_r\sigma_t\over 2m}\quad(1\le t\le 2m),
\]

\[
B_{r,p}={\sigma_r\over 2m},\qquad
B_{r,n}=-{\sigma_r\over 2m}.
\]

Then `P = L B`.  The signed rows simplify exactly:

\[
P_p=e_p,\qquad P_n=e_n.
\]

The exact verification is structural:

\[
B L = I_k,\qquad P^2=L(BL)B=P,\qquad P{\bf 1}={\bf 1}.
\]

The row negative masses are:

* row `0`: `0`;
* every foreign representative row: `(m-1)/(2m)+1/(2m)=1/2`;
* rows `p,n`: `0`.

Thus the exact cap is `delta=1/2`.  The intended-chart SF is

\[
\mathrm{SF}=m\cdot {1\over2}\cdot
\left(B_{0,p}+B_{0,n}\right)=m/2,
\qquad
\mathrm{SF}/\delta=m.
\]

Saved exact checks:

* `closed_form_audit.json`
* `closed_form_audit.txt`
* `closed_form_neg_masses.txt`

The summary lines are:

```text
closed_form_m2_a1/2_cap1/2 ... delta=1/2 intended=2 recomp_best=2 recomp_worst=1 ties=7
closed_form_m3_a1/2_cap1/2 ... delta=1/2 intended=3 recomp_best=3 recomp_worst=1 ties=9
closed_form_m5_a1/2_cap1/2 ... delta=1/2 intended=5 recomp_best=5 recomp_worst=1 ties=13
closed_form_m8_a1/2_cap1/2 ... delta=1/2 intended=8 recomp_best=8 recomp_worst=1 ties=19
```

## 2. Chart Recompute

I reused the w33 exact-auditor convention:

* exact rational matrices;
* max-volume actual-row bases by exact row-volume comparison;
* recomputed coefficients in the selected actual-row chart;
* SF evaluated for every representative in every max-volume tie chart;
* report worst and best over ties.

For this `d=k+2` family, the two exact row dependencies are explicit:

\[
x_+-e_0-\frac12\sum_t\sigma_t e_t=0,\qquad
x_- -e_0+\frac12\sum_t\sigma_t e_t=0.
\]

Therefore max-volume comparison reduces to exact `2 x 2` minors of this
dependency matrix, equivalent to exact Gram determinants but much faster.

At `delta=1/2`, every audited `m` has exactly `2m+3` max-volume ties.  They are:

* the intended basis omitting `[p,n]`, with ratio `m`;
* every basis omitting `[0,j]` for one other row `j`, with ratio `1`.

Exact required audit:

```text
m=2: best=2, worst=1, ties=7,  volume^2=1/4
m=3: best=3, worst=1, ties=9,  volume^2=1/6
m=5: best=5, worst=1, ties=13, volume^2=1/10
m=8: best=8, worst=1, ties=19, volume^2=1/16
```

Saved outputs:

* `chart_recompute_audit.json`
* `chart_recompute_audit.txt`
* `chart_recompute_stdout.txt`

Mechanism: the recomputed max-volume search does not force row `0` out.  The
identity chart remains max-volume and displays the full row-0 excess.  But tied
charts can replace row `0` by one or both exact signed unit rows `P_p=e_p`,
`P_n=e_n`; then the row carrying the large split mass is no longer a
representative, and the remaining displayed excess is only `delta`.

This is precisely the tie ambiguity the w33 notes warned about.

## 3. Threshold Map

For the cap sweep I used the exact rational one-parameter extension

\[
B_{0,p}=B_{0,n}=1/2,\qquad
B_{r,t}=\mathbf 1_{r=t}-\sigma_r\sigma_t c,\qquad
B_{r,p}={\sigma_r c\over 2a},\qquad
B_{r,n}=-{\sigma_r c\over 2a}.
\]

For each cap `delta`, rank parameter `m`, and amplitude `a`, I used the largest
foreign-row value

\[
c={\delta\over m-1+1/(2a)}
\]

and accepted the instance when the signed rows also had negative mass at most
`delta`:

\[
m a\,|1-2mc|\le \delta.
\]

The amplitude was chosen by grid search with denominator `2400`; all accepted
instances were then audited exactly in the recomputed max-volume charts.

Dense sweep over caps `0.300,0.325,...,0.500` and all `m=2..12`:

```text
cap=0.300 max best-tie ratio=5/3      at m=2
cap=0.325 max best-tie ratio=279/130  at m=2
cap=0.350 max best-tie ratio=20/7     at m=2
cap=0.375 max best-tie ratio=4        at m=3
cap=0.400 max best-tie ratio=5        at m=4
cap=0.425 max best-tie ratio=100/17   at m=5
cap=0.450 max best-tie ratio=10       at m=9
cap=0.475 max best-tie ratio=240/19   at m=12
cap=0.500 max best-tie ratio=12       at m=12, and exactly m in general
```

The full table is in `threshold_cap_summary.txt`; exact records are in
`threshold_audit.json` and `threshold_audit.txt`.

Data versus conjecture:

* Data: best-tie ratio equals the intended-chart ratio for every audited cap and
  rank.  Worst-tie ratio is `1` on the `a=1/2` endpoint ties and approximately
  `1` on the lower-amplitude three-tie cases.
* Data: for cap `0.475`, all tested `m<=12` still allow `a=1/2`, so the ratio
  keeps growing on the tested range.
* Conjecture from the exact feasibility inequality: for every fixed
  `delta<1/2`, the best-tie ratio is bounded in `m`; at `delta=1/2`, it grows
  exactly like `m`.
* Threshold estimate:

\[
\delta_*=\sup\{\delta_0:\text{best-tie ratio bounded in }m\}=1/2,
\]

but `delta_*=1/2` is not included.

Near `1/2`, the endpoint `a=1/2` is feasible up to

\[
m\lesssim {2\delta\over 1-2\delta},
\]

and gives ratio `m/(2 delta)`.  This suggests the envelope

\[
C(\delta)\asymp {1\over 1-2\delta}
\]

as `delta -> 1/2-` for the best-tie interpretation.  The large-`m` small
amplitude plateau is lower, roughly square-root divergent, so the endpoint
window controls the observed envelope near `1/2`.

## 4. Small-Delta Support

For cap `0.300`, the recomputed best-tie ratios on `m=2..12` were between
`83/60 = 1.383...` and `5/3 = 1.666...`; the worst-tie ratios were at or very
near `1`.

Thus this family is consistent with an SF constant of order `1..2` for
`delta_0 <= 0.3`.  It does not support small-delta blow-up.

## 5. Artifacts

Code:

* `w34_halfcex_audit.py`

Outputs:

* `progress.md`
* `closed_form_audit.json`
* `closed_form_audit.txt`
* `closed_form_neg_masses.txt`
* `chart_recompute_audit.json`
* `chart_recompute_audit.txt`
* `chart_recompute_stdout.txt`
* `threshold_audit.json`
* `threshold_audit.txt`
* `threshold_cap_summary.txt`
* `threshold_stdout.txt`
* `final_checks.txt`

Verification commands run:

```text
python3 -m py_compile w34_halfcex_audit.py
python3 w34_halfcex_audit.py --mode chart > chart_recompute_stdout.txt
python3 w34_halfcex_audit.py --mode closed-form > closed_form_stdout.txt
python3 w34_halfcex_audit.py --mode threshold > threshold_stdout.txt
```

Gurobi was not used.
