# w36_charge — PARTIAL: the open is now (TREE)/(DECAY), the shear-tree decay bound; the no-center path family pins C >= ~2 (codex, 2026-06-12)
# Brief: notes/briefs/w36_charge.md. Long form: experiments/out/w36_charge/proof.md.

VERDICT: PARTIAL. No proof of (CHARGE); no selected-chart counterexample either.
- ALL mandatory exact checks pass (transverse pair, dense pair, staircase, path-tie).
- NEW: the no-center path-tie VARIANT has selected-chart exact ratios 59999/40000 (k=6) and
  149999/90000 (k=8), float scan climbing toward 2 — so the selected-chart constant is NOT 1;
  the truth is C ~ 2 (the repeated-shear geometric cost).
- THE EXACT MISSING DISPLAYS: (DECAY) — a multi-swap estimate Phi(V) <= alpha Phi(U) + K delta
  with alpha < 1 (then Phi(U*) <= K delta/(1-alpha)); equivalently (TREE) — the shear-tree
  product-sum bound sum_r prod_{l<r} |a_{s_l}(i_{l+1}) w^(l)_{t_l}| <= C(delta_0).
- ORCHESTRATOR NOTE (the crux for the next prover): the naive per-generation branching mass is
  |a| * sum_t |w_t| <= 1*2 = 2 — DIVERGENT as a product bound. The decay must come from the
  delta-budget: mass-carrying shear paths should pay row negativity per generation (w27-style
  leakage) or a_s must decay along shear paths. The path family's saturation at 2 ~ geometric
  series with alpha = 1/2 is the shape to chase.
- CAVEAT (from w36_audit B6, which landed in parallel): this worker selected over exact ties
  (theta = 1); the final theorem needs the theta = 1/2 class. Its positive checks remain valid
  as exists-statements; (TREE) must be proven in the theta = 1/2 class.
---
## Appendix: proof.md (verbatim)

# VERDICT: PARTIAL

I did not prove (CHARGE) for the Phi-minimizing selected chart at
\(\delta_0=1/4\), and I did not find a selected-chart counterexample to the
dimension-free contract.

What changed relative to w35:

1. The requested w35 exact stress checks reproduce locally.
2. The w34 path-tie warning was separated into two cases:
   * with the central \(e_0\) row present, the Phi-minimizer selects that
     central chart and the ratio is below 1;
   * without the central row, the Phi-minimizer is forced onto the path and
     the selected ratio is already \(59999/40000\) at \(k=6\) and
     \(149999/90000\) at \(k=8\), with the float scan increasing toward 2.
3. Thus the selected-chart contract remains plausible, but sharp \(C=1\) is
   false for the natural no-center path variant and any proof must allow a
   path/shear constant near 2.

No `answer.md` was created.  Gurobi was not used.

Calibration:

\[
P(\text{this PARTIAL verdict survives audit})=0.86,
\quad
P(\text{CHARGE true at }\delta_0=1/4\text{ with some }C<4)=0.58,
\quad
P(C=1\text{ true for the selected chart})=0.02.
\]

## 1. Contract Used

The chart selector is the w35 selector:

\[
U_* \in \arg\min_{U\in\mathcal M}\Phi(U),\qquad
\Phi(U)=\max_s \mathrm{SF}_s(U),
\]

where \(\mathcal M\) is the finite set of exact max-volume actual-row bases.
I stayed with \(\theta=1\).  The chain can tolerate a quasi selector, but the
banked deficit estimate used here is exact-max-volume:

\[
0\le 1-a_s(j)\le 2.
\]

For a chart \(U\),

\[
\mathrm{SF}_s(U)=
\sum_j (P_{u_sj})_+
\left(
\sum_{t\ne s}(-a_t(j))_+-(1-a_s(j))
\right)_+ .
\]

The target remains:

\[
\mathrm{SF}_s(U_*)\le \sum_i q_{si}\nu_i(P),
\qquad q_{si}\ge0,\qquad \sum_iq_{si}\le C.
\tag{CHARGE}
\]

Since \(\nu_i(P)\le\delta(P)\), this implies
\(\Phi(U_*)\le C\delta(P)\).

## 2. Exact Checks Reproduced

Local artifacts:

* `stress_checks.py`
* `stress_checks.json`
* `stress_checks_summary.txt`

Commands:

```text
python3 -m py_compile stress_checks.py
python3 stress_checks.py
```

Output:

```text
transverse_pair_a1_4: delta=1/5 ties=3 best_basis=[1, 2, 3] best_max_ratio=1 worst_max_ratio=5/4 checks=BL:True P2:True rows:True
dense_pair_k7_a1_4: delta=6/17 ties=3 best_basis=[1, 2, 3, 4, 5, 6, 7] best_max_ratio=1 worst_max_ratio=17/8 checks=BL:True P2:True rows:True
staircase_m2_a1_2: delta=1/2 ties=7 best_basis=[1, 2, 3, 4, 5] best_max_ratio=1 worst_max_ratio=2 checks=BL:True P2:True rows:True
staircase_m3_a1_2: delta=1/2 ties=9 best_basis=[1, 2, 3, 4, 5, 6, 7] best_max_ratio=1 worst_max_ratio=3 checks=BL:True P2:True rows:True
```

These are exact rational checks.  They verify \(BL=I\), \(P^2=P\), row sums,
row negative masses, all exact max-volume ties, and every representative SF
value in each tied chart.

## 3. Path-Tie Family

Local artifacts:

* `path_tie_exact.py`
* `path_tie_exact.json`
* `path_tie_exact_summary.txt`
* `selected_family_scan.py`
* `selected_family_scan.json`
* `selected_family_scan_summary.txt`

The original w34 A3 support includes the central row \(e_0\).  Exact
rationalized k=6 and k=8 checks give:

```text
path_tie_k6_a1_100_mass99_100: delta=40/4001 ties=9 selected_basis=[0, 1, 2, 3, 4, 5] selected_ratio=396099/400000 audit_basis_ratio=207207/128000 worst_ratio=1036067/640000 checks=BL:True P2:True rows:True
path_tie_k8_a1_100_mass99_100: delta=300/30007 ties=13 selected_basis=[0, 1, 2, 3, 4, 5, 6, 7] selected_ratio=990231/1000000 audit_basis_ratio=20911279/12000000 worst_ratio=20911279/12000000 checks=BL:True P2:True rows:True
```

So the displayed A3 saturation is a nonselected tie when the central row is
available.

The no-center variant removes that escape chart.  The exact max-volume ties
are the bases consisting of all foreign unit rows plus one signed path row.
The determinant proof is the usual identity-row expansion: if \(c\) signed
rows are selected, expanding along the selected unit rows leaves the
\(c\times c\) signed-row minor on the omitted identity columns.  For
\(a=1/100\), determinant \(1\) occurs exactly when \(c=1\) and the omitted
identity column is \(0\); all \(c\ge2\) minors are smaller because the remaining
rows carry at least one factor \(a\).

Exact k=6 and k=8 no-center checks:

```text
path_no_center_k6_a1_100_mass1: delta=40/4001 ties=8 selected_basis=[0, 1, 2, 3, 4, 7] selected_ratio=59999/40000 audit_basis_ratio=59999/40000 worst_ratio=260017/160000 checks=BL:True P2:True rows:True
path_no_center_k8_a1_100_mass1: delta=300/30007 ties=12 selected_basis=[0, 1, 2, 3, 4, 5, 6, 11] selected_ratio=149999/90000 audit_basis_ratio=149999/90000 worst_ratio=210013/120000 checks=BL:True P2:True rows:True
```

The float scan continues:

```text
k=10 selected=1.7499937500
k=12 selected=1.7999960000
k=20 selected=1.8888987654
k=40 selected=1.9473734071
```

This does not beat the selected-chart contract, but it is the first real
calibration that \(C\) must be near 2.  Any attempted proof of \(C=1\), or any
single-swap proof that loses the path shear, is false.

## 4. Half-Staircase At The Actual Cap

For the w34 half-staircase threshold family, I also checked the selected value
at \(\delta_0=1/4\), \(m=2,\ldots,12\).  The selected chart stays at or below
1, while nonselected ties reach \(4/3\) at \(m=2\).

Representative lines:

```text
m=2 a=1/6 delta=1/4 selected=1 max_tie=4/3
m=6 a=21/400 delta=1/4 selected=7623/7625 max_tie=63/50
m=10 a=1/32 delta=1/4 selected=1 max_tie=5/4
m=12 a=31/1200 delta=1/4 selected=4681/4705 max_tie=31/25
```

Thus the half-staircase still does not threaten the selected contract at the
requested cap.

## 5. Missing Step

The remaining gap is not selection, exact arithmetic, or the deficit bank.  It
is the following shear-decay/dual-flow lemma.

Let \(U\) be an exact max-volume chart and suppose
\(\mathrm{SF}_s(U)=\Phi(U)\).  A row \(j\) with \(a_s(j)=1\) can replace
\(u_s\).  Writing

\[
a(j)=e_s+w,\qquad w_s=0,\qquad \sum_t w_t=0,
\]

the swap sends

\[
a'_s(i)=a_s(i),\qquad
a'_t(i)=a_t(i)-a_s(i)w_t \quad(t\ne s).
\tag{S}
\]

What is needed is a uniform decay statement:

\[
\boxed{
\text{For every exact max-volume chart }U\text{ and active }s,
\text{ either }\mathrm{SF}_s(U)\le K\delta
\text{ or there is an exact max-volume chart }V
\text{ with }
\Phi(V)\le \alpha\,\mathrm{SF}_s(U)+K\delta
}
\tag{DECAY}
\]

for constants \(K<\infty\) and \(\alpha<1\) depending only on
\(\delta_0\).  Then applying (DECAY) to \(U_*\) would give

\[
\Phi(U_*)\le \Phi(V)\le \alpha\Phi(U_*)+K\delta,
\qquad
\Phi(U_*)\le {K\over 1-\alpha}\delta.
\]

The no-center path family shows why (DECAY) must be a multi-swap or dual-flow
statement rather than a one-swap estimate: shear can move the excess down a
path and only decays after repeated recentering.  The observed limiting
constant near 2 is exactly this repeated-shear cost.

Equivalently, in charging form, the missing bound is:

\[
\boxed{
\sum_j (P_{u_sj})_+E_s^U(j)
\le
\sum_i q_{si}\nu_i(P),
\qquad
\sum_i q_{si}\le C,
}
\]

where the \(q_{si}\) must be generated by the shear tree induced by (S).  I can
verify this on the mandatory families, but I do not have the dimension-free
tree bound:

\[
\sum_{\text{swap generations }r}
\prod_{\ell<r}\bigl|a_{s_\ell}(i_{\ell+1})\,w^{(\ell)}_{t_\ell}\bigr|
\le C(\delta_0).
\tag{TREE}
\]

This is the exact missing display.  Proving (TREE), or an LP-dual certificate
that implies it, would close (CHARGE).  Without it, the path family blocks a
valid proof.

## 6. Verdict

No selected-chart counterexample to the dimension-free contract was found.
The mandatory exact checks pass.  The no-center path family confirms the
expected saturation near 2 and rules out the sharp \(C=1\) hope.  The proof
still dies at the multi-swap shear-decay/dual-flow lemma (DECAY)/(TREE).

Final status:

\[
\boxed{\text{PARTIAL: CHARGE not proved; no counterexample-to-contract found.}}
\]
