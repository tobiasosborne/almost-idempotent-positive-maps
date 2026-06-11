# VERDICT: DIED-AT

I did not prove the transverse coefficient tax, and I did not find a
counterexample.  The strongest conclusion from this pass is a sharper diagnosis
of the remaining open piece:

\[
\boxed{
\sum_j (P_{u_sj})_+
\left(
\sum_{t\ne s}(-a_t(j))_+-(1-a_s(j))
\right)_+
\le C_{\rm sf}\delta .
}
\tag{SF}
\]

This is the signed-face core of the tax.  The already-bankable scalar deficit
identity gives

\[
\sum_j(P_{u_sj})_+(1-a_s(j))\le 2\delta,
\tag{1}
\]

so (SF) would imply the requested tax with

\[
C_\mu=2+C_{\rm sf}.
\]

I could not derive (SF) from Hognas-Mukherjea 1.12, the max-volume Cramer
bounds, the exact coefficient identities, or the w27 cluster leakage.  The
failed split is precise: the known tools control visible loss of the
\(s\)-coordinate and leakage to other clusters, but the numerically sharp
tax is carried by rows in the \(u_s\)-cluster with \(a_s(j)\simeq 1\) and
opposite foreign coefficients cancelling in pairs.

Calibration:

\[
P(\hbox{this DIED-AT diagnosis survives audit})=0.78,
\qquad
P(\hbox{the tax is true dimension-free})=0.62,
\qquad
P(\hbox{a small-\delta counterexample exists})=0.18.
\]

No `answer.md` was created.

## 1. Imported Setup

Assume

\[
P^2=P,\qquad P{\bf 1}={\bf 1},\qquad
\nu_i:=\sum_j(-P_{ij})_+\le\delta\le\delta_0 .
\]

Let \(r_t=p_{u_t}\) be the audited maximum-volume actual-row basis, and write

\[
p_j=\sum_{t=1}^k a_t(j)r_t,\qquad |a_t(j)|\le1,\qquad
\sum_t a_t(j)=1.
\]

The coordinate functions are fixed:

\[
Pa_t=a_t.
\]

For a fixed representative \(u_s\), put

\[
\lambda_s(j):=1-a_s(j),\qquad
\mu_s(j):=\sum_{t\ne s}(-a_t(j))_+.
\]

The target tax is

\[
M_s:=\sum_j(P_{u_sj})_+\mu_s(j)\le C_\mu\delta.
\tag{TAX}
\]

The w30 max-volume reduction remains valid: if (TAX) holds, then the
representative displacement lemma follows with

\[
C_D\le 2(1+2\delta_0)(2+C_\mu).
\]

The already-written consequence chain then gives the conditional face estimate,
conditional L4 assembly, and the global W-free \(O(\sqrt\delta)\) theorem.

## 2. What Is Proved

The \(s\)-coordinate deficit is controlled.  Since \(Pa_s=a_s\),

\[
0=\sum_jP_{u_sj}(1-a_s(j)).
\]

Also \(0\le1-a_s(j)\le2\), because \(|a_s(j)|\le1\).  Therefore

\[
\sum_j(P_{u_sj})_+(1-a_s(j))
\le
2\sum_j(-P_{u_sj})_+
\le2\delta.
\]

Thus the tax splits as

\[
M_s
\le
2\delta+
\sum_j(P_{u_sj})_+(\mu_s(j)-\lambda_s(j))_+.
\tag{2}
\]

The first term is done.  The second term is exactly the signed-face excess
(SF).  It is supported where the row has not visibly left the \(s\)-face:
\(a_s(j)\) can be close to \(1\), while foreign coordinates have matching
positive and negative parts.

The w27 cross-cluster leakage is also still valid:

\[
\sum_{j\in\cup_{t\ne s}M_t}(P_{u_sj})_+
\le {2\delta\over 1-\eta}.
\]

This controls positive mass from \(u_s\) into other pivot-balls.  It does not
control the signed-face excess inside \(M_s\), and the small-\(\delta\)
numerics show that this is where the tax sits.

## 3. HM 1.12 Does Not Add The Missing Inequality

In the row-stochastic specialization of Hognas-Mukherjea 1.12, exact
proportional classes collapse: if \(h,u_t\in C_t\), then

\[
p_h=\gamma(h,u_t)p_{u_t},\qquad p_h{\bf 1}=p_{u_t}{\bf 1}=1,
\]

so \(\gamma(h,u_t)=1\).

The theorem's sum rules become, with the usual coefficient functions,

\[
\sum_jP_{u_sj}a_t(j)=\delta_{st}.
\tag{3}
\]

For \(t=s\), (3) is the deficit estimate above.  For \(t\ne s\), it says only

\[
\sum_jP_{u_sj}a_t(j)=0.
\tag{4}
\]

Equation (4) is a signed barycentre identity.  It permits the positive part of
row \(u_s\) to split between \(a_t>0\) and \(a_t<0\) signed-face rows, with
the two contributions cancelling before any absolute values are taken.  That is
exactly the tax.  HM 1.12 identifies the right coordinates, but its exact sum
rules are not a quantitative total-variation bound.

## 4. Exact Failed Split

The tempting argument is:

1. Use (4) to say the positive \(a_t<0\) mass must be matched by positive
   \(a_t>0\) mass.
2. Interpret the \(a_t>0\) rows as leaning toward cluster \(t\).
3. Pay for them with the w27 cross-cluster leakage bound.

Step 2 is false at the needed scale.  Rows can have

\[
a_s(j)=1,\qquad
\sum_{t\ne s}a_t(j)=0,\qquad
\sum_{t\ne s}|a_t(j)|>0.
\tag{5}
\]

Such rows are in the \(s\)-face in the scalar coordinate \(a_s\), and for small
amplitude they lie in the \(M_s\) pivot-ball.  They need not be in any foreign
cluster.  The transverse-pair family is the model:

\[
a(3)=e_s+a(e_t-e_r),\qquad
a(4)=e_s-a(e_t-e_r).
\]

The representative row \(u_s\) can put positive mass on both rows.  The
foreign coordinate identities cancel exactly, while the tax sees the total
variation.

Max-volume alone also does not remove (5).  Single-row replacement gives only
\(|a_s(j)|\le1\).  Multi-row replacement bounds determinants, e.g. the
two-row signed pair gives \(2a\le1\) in the rank-three toy model, but not
\(a=O(\delta)\).

Thus the failed split is not cross-cluster leakage.  It is in-cluster
signed-face variation after the scalar deficit \(\lambda_s\) is removed.

## 5. Numerical Audit

Artifacts in this workdir:

- `tax_audit.py`
- `tax_audit_results.json`
- `tax_audit_summary.txt`
- `lp_rank_stress.py`
- `lp_rank_stress_results.json`
- `lp_rank_stress_summary.txt`
- `progress.md`
- `proof.md`

Verification:

```text
python3 -m py_compile tax_audit.py
python3 tax_audit.py
python3 -m py_compile lp_rank_stress.py
python3 lp_rank_stress.py
```

All completed cleanly.

Key `tax_audit_summary.txt` lines:

```text
rank2_leakage_delta_1e-05: tax/delta ~ 0
split_block_eps_1e-05:     tax/delta ~ 0
transverse_pair_a_0.01:    tax/delta=0.990396, own/delta=0.990396
transverse_pair_a_0.02:    tax/delta=0.991584, own/delta=0.991584
transverse_pair_a_0.05:    tax/delta=0.999900, own/delta=0.999900
random_conjugated_1e-4:    tax/delta=0.743569, own/delta=0.743569
w17_robust_rational:      tax/delta=0.0928222
```

The requested rank-2 leakage and split-block checks carry no tax in the
max-volume chart.  The transverse-pair family carries essentially all tax in
the own cluster, not in foreign clusters or \(B_\eta\), for small amplitude.
The random small-\(\delta\) conjugations show the same pattern.

The larger random coordinate projections sometimes place tax in \(B_\eta\), but
those samples are not in the small-\(\delta\) corner.  They did not produce a
counterexample; their worst recorded tax ratios stayed below \(1\).

The LP rank-growth stress fixed determinant-bounded coordinate rows with many
transverse signed pairs and minimized the row-negativity budget needed to carry
prescribed \(u_s\)-mass on them.  The ratios did not grow with rank:

```text
k=3  a=0.05 tax/delta=0.999900
k=6  a=0.05 tax/delta=0.994950
k=10 a=0.05 tax/delta=0.994950
k=4  a=0.2  tax/delta=1.108800
k=10 a=0.2  tax/delta=1.069200
```

This supports the tax rather than refuting it, but it is not a proof.

## 6. Minimal Further Fact

The minimal further fact is (SF), repeated here:

\[
\sum_j (P_{u_sj})_+
\left(
\sum_{t\ne s}(-a_t(j))_+-(1-a_s(j))
\right)_+
\le C_{\rm sf}\delta.
\]

Equivalently: after paying for visible loss of the \(s\)-coordinate, positive
representative mass cannot sit on signed-face rows with large transverse
positive/negative coefficient variation except at \(O(\delta)\) total cost.

If this lands, then

\[
M_s\le(2+C_{\rm sf})\delta,
\]

so the original tax holds with \(C_\mu=2+C_{\rm sf}\), and the w30 consequence
chain gives

\[
C_D\le2(1+2\delta_0)(4+C_{\rm sf}).
\]

Without (SF) or an equivalent in-face coercivity lemma, the current tools stop
at signed cancellation and do not prove the tax.
