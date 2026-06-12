# w35_charge — PARTIAL: chart selection + deficit banked; ALL stress families collapse to ratio EXACTLY 1 in the min-max chart; THE open = (CHARGE) (codex, 2026-06-12)
# Brief: notes/briefs/w35_charge.md. Long form: experiments/out/w35_charge/proof.md.

VERDICT: PARTIAL. The exists-chart SF theorem did not close even at delta_0 = 1/4, but the
problem is now ONE displayed inequality.
- PROVED/BANKED: (1) the chart selection U* = argmin over exact max-volume ties of
  Phi(U) = max_s SF_s(U) is well-defined with theta = 1 (finitely many bases; minor-scan
  equivalence per w34_audit A7); (2) the deficit bound sum (B_sj)+(1-a_s) <= 2delta holds in
  ANY exact max-volume chart; (3) sufficient criterion: max_j E_s(j) <= K delta => SF_s <=
  K(1+delta_0) delta.
- EXACT STRESS CHECKS (all rational, every max-volume tie enumerated): transverse pair a=1/4
  (delta=1/5): best-tie max ratio = 1 (worst 5/4); dense pair k=7 (delta=6/17): best = 1
  (worst 17/8); staircase m=2,3 (delta=1/2!): best = 1 (worst = m). NOTE: the min-max chart
  achieves ratio EXACTLY 1 on every known bad instance EVEN AT delta = 1/2 — the exists-form
  may hold far beyond delta_0 = 1/4 with C ~ 1; no counterexample to Phi(U*) <= delta is known.
- THE NAMED OPEN — (CHARGE): for U* = argmin Phi and every s, there exist q_si >= 0 with
  sum_i q_si <= C(delta_0) such that sum_j (P_{u_s j})+ E_s(j) <= sum_i q_si nu_i(P).
  (CHARGE) => SF with the same C, theta = 1.
- THE PRECISE OBSTRUCTION: the tie-swap shear formula (S): swapping u_s for a bad row
  a(j) = e_s + w (w_s = 0, sum w = 0) gives a'_t(i) = a_t(i) - a_s(i) w_t — a swap removes
  the present bad mass but can SHEAR excess into other coordinates; min-max gives only local
  single-swap monotonicity, not a bounded charge. The w34_audit A3 path-tie family
  (ratios saturating ~2) is the warning: a recurrence/dual certificate is needed, not
  single-swap arguments. Calibration: P(PARTIAL survives audit) = 0.84; P(exists-chart
  theorem true at delta_0 = 1/4) = 0.63.
---
## Appendix: proof.md (verbatim)

# VERDICT: PARTIAL

I did not prove the requested EXISTS-chart signed-face estimate for all ranks,
even with the smaller cap

\[
\delta_0={1\over4}.
\]

That is the cap I would use for a completed proof: it includes the sharp
transverse endpoint \(a=1/2\), where \(\delta=1/4\), and stays below the
confirmed dense-pair obstruction at \(\delta=6/17\).  The proof still does not
close at this cap.

What is proved here is:

1. the exact max-volume tie-selection problem is well-defined with
   \(\theta=1\);
2. the known deficit term still gives the banked \(2\delta\) bound in any
   exact max-volume chart;
3. a clean sufficient max-excess criterion is recorded;
4. the requested stress families were recomputed exactly, and in every one the
   min-max max-volume tie chart has
   \[
   \max_s \mathrm{SF}_s \le \delta.
   \]

The missing step is the dimension-free dual-flow charging inequality for the
potential-minimizing max-volume tie chart, displayed in Section 5.

Calibration:

\[
P(\hbox{this PARTIAL verdict survives hostile audit})=0.84,\qquad
P(\hbox{the EXISTS-chart theorem is true for }\delta_0=1/4)=0.63.
\]

No `answer.md` was created.

## 1. Setup and Selected Chart

Use the audited Hognas-Mukherjea frame in the row-stochastic specialization:

\[
P=LB,\qquad BL=I_k.
\]

The rows of \(L\) are the chart coefficients \(a(j)\), and the rows of \(B\)
are the representative rows \(p_{u_s}\).  For a representative \(u_s\),

\[
P_{u_s j}=B_{s j}.
\]

For an exact max-volume actual-row basis \(U=(u_1,\ldots,u_k)\), Cramer's rule
gives

\[
|a_t(j)|\le 1
\]

for every actual row \(j\) and every coordinate \(t\).  By w34_audit A7,
maximizing actual-row volume is equivalent to maximizing
\(|\det L_U|\), since

\[
\det(P_U P_U^T)=\det(L_U)^2\det(BB^T).
\]

There are finitely many actual-row bases.  Therefore the following chart
selection is well-defined and has \(\theta=1\):

\[
U_* \in
\arg\min_{U\in \mathcal M}
\Phi(U),\qquad
\Phi(U):=\max_{1\le s\le k}\mathrm{SF}_s(U),
\]

where \(\mathcal M\) is the set of exact max-volume bases and

\[
\mathrm{SF}_s(U)
:=
\sum_j (P_{u_sj})_+
\left(
\sum_{t\ne s}(-a_t(j))_+-(1-a_s(j))
\right)_+ .
\]

This proves the selection part only.  It does not prove
\(\Phi(U_*)=O(\delta)\).

## 2. Banked Deficit

For any exact max-volume chart, put

\[
\lambda_s(j)=1-a_s(j),\qquad
\mu_s(j)=\sum_{t\ne s}(-a_t(j))_+,
\qquad
E_s(j)=(\mu_s(j)-\lambda_s(j))_+ .
\]

The target is

\[
\sum_j (B_{sj})_+E_s(j)\le C\delta.
\tag{SF}
\]

The non-excess deficit term is already controlled.  Since \(Pa_s=a_s\),

\[
0=\sum_j B_{sj}(1-a_s(j)).
\]

The max-volume box gives \(0\le 1-a_s(j)\le2\).  Hence

\[
\sum_j (B_{sj})_+(1-a_s(j))
\le
2\sum_j(-B_{sj})_+
\le 2\delta .
\tag{D}
\]

This is exactly the w31 Section 2 deficit estimate.  It does not control (SF),
because \(E_s\) is supported on transverse signed-face rows where
\(\lambda_s\) can vanish.

## 3. A Sufficient Criterion

The row \(B_s\) has positive mass

\[
\sum_j(B_{sj})_+=1+\sum_j(-B_{sj})_+\le1+\delta.
\]

Therefore any chart satisfying the max-excess estimate

\[
\max_j E_s(j)\le K\delta
\tag{ME}
\]

for every \(s\) automatically satisfies

\[
\mathrm{SF}_s
\le
K(1+\delta_0)\delta .
\]

This is not the theorem: (ME) is stronger than necessary, and I did not prove
it for the potential-minimizing chart.  It is useful because it isolates the
right small-\(\delta\) obstruction.  The half-delta staircase shows that no
such estimate can survive at \(\delta_0=1/2\), while the audited threshold data
are consistent with such control below about \(0.3\).

## 4. Exact Stress Checks

I wrote `stress_checks.py`, which works over exact rationals.  For each family
it checks:

* \(BL=I\);
* \(P^2=P\);
* \(P{\bf1}={\bf1}\);
* exact row negative masses;
* all exact max-volume coefficient-minor ties;
* the SF value of every representative in every max-volume tie chart.

The chart selection used in the table is the finite min-max rule from Section
1.

Saved outputs:

* `stress_checks.py`
* `stress_checks.json`
* `stress_checks_summary.txt`

Verification run:

```text
python3 -m py_compile stress_checks.py
python3 stress_checks.py
```

Summary:

```text
transverse_pair_a1_4: delta=1/5 ties=3 best_basis=[1, 2, 3] best_max_ratio=1 worst_max_ratio=5/4 checks=BL:True P2:True rows:True
dense_pair_k7_a1_4: delta=6/17 ties=3 best_basis=[1, 2, 3, 4, 5, 6, 7] best_max_ratio=1 worst_max_ratio=17/8 checks=BL:True P2:True rows:True
staircase_m2_a1_2: delta=1/2 ties=7 best_basis=[1, 2, 3, 4, 5] best_max_ratio=1 worst_max_ratio=2 checks=BL:True P2:True rows:True
staircase_m3_a1_2: delta=1/2 ties=9 best_basis=[1, 2, 3, 4, 5, 6, 7] best_max_ratio=1 worst_max_ratio=3 checks=BL:True P2:True rows:True
```

The transverse pair at \(a=1/4\) is inside the chosen cap:

\[
\delta={1\over5}< {1\over4}.
\]

The dense \(k=7\) pair and the two staircase endpoints are outside the
\(\delta_0=1/4\) theorem range, but they are the requested stress tests.  They
confirm the same mechanism: the bad displayed ratio is a worst-tie artifact,
and a favorable max-volume tie chart collapses the max representative ratio to
exactly \(1\).

## 5. Where the Full Proof Fails

The natural attempt is to use the min-max chart \(U_*\).  If a bad row \(j\)
satisfies \(a_s(j)=1\), then replacing \(u_s\) by \(j\) is an exact
max-volume tie swap.  If

\[
a(j)=e_s+w,\qquad w_s=0,\qquad \sum_t w_t=0,
\]

then the new coordinates after the swap are

\[
a'_s(i)=a_s(i),\qquad
a'_t(i)=a_t(i)-a_s(i)w_t\quad(t\ne s).
\tag{S}
\]

In every audited bad family, such a swap moves the split-mass row out of the
representative role and the remaining SF is paid by actual row negativity.
This is exactly the w34_halfcex collapse mechanism.

The missing inequality is that this favorable behavior is forced in general.
The precise form I could not prove is the following dual-flow charging
statement:

\[
\boxed{
\text{For }U_* \in \arg\min_{\mathcal M}\Phi,\ \text{for every }s
\text{ there are }q_{s i}\ge0
\text{ with }
\sum_i q_{s i}\le C(\delta_0)
\text{ such that}
}
\]

\[
\boxed{
\sum_j (P_{u_sj})_+E_s(j)
\le
\sum_i q_{s i}\nu_i(P),
\qquad
\nu_i(P)=\sum_\ell(-P_{i\ell})_+ .
}
\tag{CHARGE}
\]

Since \(\nu_i(P)\le\delta\), (CHARGE) would prove (SF) with the same
dimension-free constant \(C(\delta_0)\) and \(\theta=1\).

The exact stress checks verify the consequence of (CHARGE), namely
\(\mathrm{SF}_s\le\delta\), on the transverse pair, dense pair, and staircase
charts above.  They do not supply a structural charge assignment.  I cannot
prove that assignment from the available identities:

\[
\sum_j B_{sj}a_t(j)=\delta_{st},
\qquad
Pa_t=a_t,
\qquad
|a_t(j)|\le1.
\]

The obstruction is the shear formula (S).  A tie swap can remove the present
representative's bad mass, but it can also shear the displayed excess into
other coordinates.  The finite min-max condition says only that this cannot
lower \(\Phi\); it does not by itself identify a bounded row-negative budget
that pays for the surviving sheared excess.  The path tie family from
w34_audit A3 is the warning sign: the ratios appear to saturate near \(2\),
but the proof would need a recurrence or dual certificate, not just local
single-swap monotonicity.

Thus the died-at wall is exactly (CHARGE).  Proving it for the selected
max-volume tie chart would complete the target for \(\delta_0=1/4\), and
probably for \(\delta_0=0.3\) with a larger envelope constant.
