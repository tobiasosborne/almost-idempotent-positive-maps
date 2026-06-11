# VERDICT: L1+L2 PROVED IN THE TWO-SCALE FORM; L3 NOT ASSEMBLED

L1 is proved below with explicit constants in removed mass.  The w20 stress
family now passes: the old ratios `eps/(mu_after/8)=62.7..313` are not the
right test after recoding.  The repaired tests are
`eps_recode <= 2*(removed recurrent mass + max removed transient face mass)`,
survivor-coordinate relative shift `<= q_s`, and transient-face coefficient
shift `<= 2*r_i`; all pass.

L2 is proved as the honest two-scale visibility assembly: after a finite
recoding chain, apply the fixed-mass ambient visibility lemma on the recoded
stratum, with the radius depending on the arc's degeneration profile
`(epsilon(t), delta(t), q_m, eta_m, Lambda_m, mu_m)`.  This is the strongest
statement justified by the imported w20 lemma; it is not a global radius
depending only on `n`.

L3 still has the w21 missing estimate:
\[
  \operatorname{dist}(J^m P,J^m\mathcal M)^2
  \le L(P_0)\,\delta_m(P)
\]
at the first non-H-M jet after all boundary rebasings.  The banked w19
first-order lemma applies at every recoded boundary H-M point, but it does not
supply this finite-jet projection estimate.

Numerical artifacts:

- `recode_removed_mass_checks.py`
- `recode_removed_mass_results.json`
- `recode_removed_mass_summary.txt`

Calibration:

- `P(L1+L2 survive audit) = 0.78`
- `P(L3 assembles the local linear law from the present ingredients) = 0.34`

## 1. H-M Data And Removed-Mass Notation

Let \(P_0\) be an H-M stochastic idempotent on \([n]\), with recurrent blocks
\(C_1,\ldots,C_k\), transient set \(T\), recurrent laws \(\pi_s\), and
transient coefficients \(\alpha_i\in\Delta_{k-1}\):
\[
  p_i^0=\pi_s\quad(i\in C_s),\qquad
  p_i^0=\sum_{s=1}^k \alpha_{is}\pi_s\quad(i\in T).
\]
The supports \(C_s\) are disjoint, \(\pi_s\) is positive on \(C_s\), and
transient columns are zero.

Choose recurrent coordinates \(D_s\subset C_s\) to remove and put
\[
  K_s=C_s\setminus D_s,\qquad
  q_s=\sum_{j\in D_s}\pi_s(j),\qquad
  q=\sum_s q_s .
\]
Assume \(K_s\ne\emptyset\).  The important parameter is \(q_s\), not the
threshold by which \(D_s\) was chosen.

For transient faces choose \(E_i\subset\{s:\alpha_{is}>0\}\), and put
\[
  r_i=\sum_{s\in E_i}\alpha_{is},\qquad
  r=\max_{i\in T} r_i,\qquad
  Q=q+r .
\]
Assume \(q_s<1\) and \(r_i<1\).  For the clean constants below one may impose
\(q_s,r_i\le1/2\), but the first two estimates are exact for all \(<1\).

## 2. The Recoded H-M Point

Define
\[
  \pi_s'={\pi_s|_{K_s}\over 1-q_s}.
\]
The new recurrent blocks are \(K_s\).  The new transient set is
\[
  T'=T\cup\bigcup_s D_s .
\]
For a removed recurrent coordinate \(j\in D_s\), set its new transient
coefficient to \(e_s\).  For an old transient row \(i\in T\), set
\[
  \alpha'_{is}=
  \begin{cases}
    0,&s\in E_i,\\
    \alpha_{is}/(1-r_i),&s\notin E_i .
  \end{cases}
\]
Then
\[
  p_i'=\pi_s'\quad(i\in K_s),\qquad
  p_j'=\pi_s'\quad(j\in D_s),\qquad
  p_i'=\sum_s\alpha'_{is}\pi_s'\quad(i\in T).
\]
This is again an H-M stochastic idempotent: the recurrent rows are block laws,
the transient rows are convex mixtures of them, and all transient columns
\(T'\) are zero.

The assignment \(j\in D_s\mapsto e_s\) is distance-minimizing.  For any mixture
\(\sum_r\beta_r\pi_r'\),
\[
\begin{aligned}
 \left\|\pi_s-\sum_r\beta_r\pi_r'\right\|_1
 &= q_s+\left|1-q_s-\beta_s\right|+\sum_{r\ne s}\beta_r\\
 &\ge 2q_s,
\end{aligned}
\]
and equality is attained by \(\beta=e_s\).  This assignment also leaves the
block coefficient functional \(\Gamma_s\) unchanged on the removed coordinate:
before recoding \(j\in C_s\) had weight \(1\), and after recoding the transient
row \(j\) has coefficient \(e_s\), again weight \(1\).

## 3. L1 Constants

### 3.1 Base Distance

For one recurrent law,
\[
  \|\pi_s-\pi_s'\|_1
  =q_s+\sum_{j\in K_s}\left({\pi_s(j)\over1-q_s}-\pi_s(j)\right)
  =2q_s .
\]
Thus every old recurrent row in block \(s\), including rows moved into
transient status, moves by exactly \(2q_s\).

For an old transient row, first recode the recurrent laws and then recode its
coefficient face.  The recurrent-law part moves by
\[
  \left\|\sum_s\alpha_{is}(\pi_s-\pi_s')\right\|_1
  \le \sum_s\alpha_{is}\,2q_s
  \le 2q .
\]
The coefficient face move has exact simplex \(\ell^1\)-size
\[
  \|\alpha_i-\alpha_i'\|_1=2r_i,
\]
and because the \(\pi_s'\)'s have disjoint supports, this is also the row
\(\ell^1\)-movement caused by the coefficient recoding.  Therefore
\[
  \|p_i^0-p_i'\|_1\le2q+2r_i\le2Q .
\]
Taking the maximum over all rows gives the L1 distance estimate
\[
  \boxed{\|P_0-P_0'\|_{\infty,1}\le 2Q.}
\]
So the requested constant can be taken as
\[
  \boxed{A=2.}
\]

### 3.2 Survivor Mass

Let
\[
  \mu_{\rm surv}=\min_{s}\min_{j\in K_s}\pi_s(j).
\]
The recoded recurrent mass floor is
\[
  \mu(P_0')=\min_s\min_{j\in K_s}{\pi_s(j)\over1-q_s}
  \ge \mu_{\rm surv}.
\]
Moreover, for every survivor \(j\in K_s\),
\[
  \pi_s'(j)-\pi_s(j)
  ={q_s\over1-q_s}\pi_s(j)
  =q_s\,\pi_s'(j).
\]
Thus the survivor-coordinate relative shift is exactly \(q_s\).  This is the
repair that the w20 audit demanded: even if the total dropped mass is
\(n\theta\), the small surviving coordinate is only changed by the relative
factor \(q_s\), not by \(n\theta/\theta\).  In particular \(q_s\le1/8\) implies
that every survivor coordinate is distorted by at most one eighth of its
recoded mass.

### 3.3 Recurrent Transport And Delta

For a row \(x\in\mathbb R^n\), define the recurrent transport \(R_Dx\) by
removing the coordinates in \(D_s\) and redistributing their signed total mass
inside \(K_s\) according to \(\pi_s'\):
\[
  (R_Dx)_j=
  \begin{cases}
    0,&j\in D_s,\\
    x_j+\pi_s'(j)\sum_{\ell\in D_s}x_\ell,&j\in K_s,\\
    x_j,&j\in T .
  \end{cases}
\]
This preserves row sums and sends \(\pi_s\) to \(\pi_s'\).  It is
nonexpansive in row \(\ell^1\):
\[
  \|R_Dx-R_Dy\|_1\le\|x-y\|_1.
\]
Indeed, in each block,
\[
  \|(x-y)_K+\pi_s'\sum_D(x-y)\|_1
  \le \|(x-y)_K\|_1+\|(x-y)_D\|_1.
\]
It also does not increase negative mass:
\[
  \delta(R_D P)\le \delta(P).
\]
Per block, the negative part after transport is bounded by the old negative
part on \(K_s\) plus \((-\sum_{D_s}x_j)_+\), and the latter is bounded by the
old negative part on \(D_s\).

If \(P\) is \(\varepsilon\)-close to \(P_0\) in max-row \(\ell^1\), then
\[
  \|R_D P-R_D P_0\|_{\infty,1}\le\varepsilon.
\]
The reverse delta comparison loses only the mass scale being erased:
\[
  \delta(P)\le \delta(R_D P)+q+\varepsilon .
\]
The term \(q\) is unavoidable: positive mass in removed columns can cancel
negative survivor mass after transport.

### 3.4 Transient Face Transport

For a transient row \(i\), after recurrent transport define
\[
  \Gamma_s'(x)=\sum_{j\in K_s}x_j+\sum_{\ell\in T'}x_\ell\alpha'_{\ell s}.
\]
Let \(\beta_i\) be the kept coefficient distribution
\(\beta_{is}=\alpha_{is}/(1-r_i)\) on \(s\notin E_i\), zero on \(E_i\).  The
face transport is
\[
  F_i x
  =
  x-\sum_{s\in E_i}\Gamma_s'(x)\pi_s'
   +\left(\sum_{s\in E_i}\Gamma_s'(x)\right)\sum_u\beta_{iu}\pi_u'.
\]
It sends the recurrently recoded base row
\(\sum_s\alpha_{is}\pi_s'\) to \(\sum_s\alpha'_{is}\pi_s'\).

The perturbation amplification is explicit:
\[
  \|F_i x-F_i y\|_1
  \le (1+2|E_i|)\|x-y\|_1
  \le (1+2k)\|x-y\|_1.
\]
Hence the full rowwise recoding map \({\mathcal R}\) satisfies
\[
  \|{\mathcal R}(P)-P_0'\|_{\infty,1}
  \le (1+2k)\|P-P_0\|_{\infty,1}.
\]
At the base itself, the face move is already included in the sharper
\(\|P_0-P_0'\|_{\infty,1}\le2Q\).

### 3.5 Reference Heights

Let
\[
  h_{\mathcal C}(P)=
  \max_i\operatorname{dist}_1(p_i,\operatorname{conv}\{\pi_s\}_{s=1}^k)
\]
and define \(h_{\mathcal C'}\) similarly with \(\pi_s'\).  Since each
\(\pi_s\) is within \(2q_s\) of \(\pi_s'\), the two recurrent hulls have
Hausdorff \(\ell^1\)-distance at most \(2\max_s q_s\le2q\).  Therefore
\[
  |h_{\mathcal C}(P)-h_{\mathcal C'}(P)|\le2q .
\]
With full row recoding,
\[
  |h_{\mathcal C}(P)-h_{\mathcal C'}({\mathcal R}P)|
  \le 2q + \|P-{\mathcal R}P\|_{\infty,1}.
\]
For \(P=P_0\) this is at most \(4q+2r\); for
\(\|P-P_0\|_{\infty,1}\le\varepsilon\), it is at most
\[
  4q+2r+(2+2k)\varepsilon .
\]
This is the controlled transformation of the H-reference.  The actual
visible-hull height \(H\) is then controlled by the same estimate once the
surviving recurrent vertices have been transferred as visible vertices; that
transfer is the margin statement next.

### 3.6 Visibility Margins

Let \(X=\{x_a\}\) and \(X'=\{x_a'\}\) be matched row sets with
\(\max_a\|x_a-x_a'\|_1\le e\).  Suppose an affine support function
\(\ell(x)=u\cdot x+b\) exposes a vertex \(v\) in \(X\), is normalized by
\(\ell(v)=0\), \(0\le\ell(x_a)\le1\), and satisfies
\(\ell(x_b)\ge\eta\) on the rows \(b\) where the shifted block exposer is
negative.  Put
\[
  \Lambda=\|u\|_\infty .
\]
Then the recentered function
\[
  \ell'(x)=\ell(x)-\ell(v')
\]
satisfies, on the matched negative rows,
\[
  \ell'(x_b')\ge\eta-2\Lambda e.
\]
The normalization bounds change by at most \(2\Lambda e\).  After the harmless
rescaling used in the w20 ambient lemma, the support margin is therefore at
least
\[
  \boxed{\eta'\ge \eta-4\Lambda e.}
\]
For the recoding above one may take \(e=2Q\) at the base, or
\[
  e\le 2Q+(1+2k)\varepsilon
\]
when matching a nearby target to the fully recoded target.

The dependence on \(\Lambda\) is not cosmetic.  A support margin normalized
only on a nearly affine-dependent finite row set need not be Lipschitz with a
dimension-only constant.  Thus \(\Lambda\), or equivalently the recomputed LP
margin at the recoded base, belongs in the honest degeneration profile.

## 4. L2: Two-Scale Visibility Assembly

The imported fixed-mass ambient lemma says:

If \(P_*\) is an H-M point, \(P\) is within
\(\varepsilon_*\) in max-row \(\ell^1\), \(\tau=\sqrt{\delta(P)}\), and a
recurrent-cluster vertex has LP support margin \(\eta_*>0\), then that vertex
is visible whenever
\[
  \varepsilon_*
  \le
  \min\left\{
    {\mu(P_*)\over8},\ {\tau\over64},\
    {\eta_*\tau\over64},\ {1\over64}
  \right\}.
\]

The recoding lemma gives the boundary version as follows.  For a recoding
profile \(m=(D_s,E_i)\), let \(P_m\) be the recoded H-M base and
\({\mathcal R}_m\) the rowwise recurrent/face transport.  The ambient proof is
scale-parametric: the symbol \(\tau\) enters only through the visibility
thresholds \(\rho=4\tau\), \(\kappa=\tau/4\), and the displayed smallness
conditions.  Thus one may use the recoded scale
\(\sqrt{\delta({\mathcal R}_mP(t))}\) for recoded height, or the original scale
\(\sqrt{\delta(P(t))}\) when transferring a certificate back to the original
rows.  Write the chosen scale as \(\bar\tau_m(t)\).  Put
\[
  L_m=1+2k,\qquad
  \varepsilon_m(t)=L_m\|P(t)-P_0\|_{\infty,1},
\]
\[
  \mu_m=\min_{s,j\in K_s}{\pi_s(j)\over1-q_s},\qquad
  \eta_m=\eta_{\rm LP}(P_m),
\]
where \(\eta_{\rm LP}(P_m)\) is either recomputed on the recoded row set or
bounded below by \(\eta-8\Lambda Q_m\) from the previous section.
Then the fixed-mass lemma applies on the recoded stratum whenever
\[
  \boxed{
  \varepsilon_m(t)
  \le
  \min\left\{
    {\mu_m\over8},\ {\bar\tau_m(t)\over64},\
    {\eta_m\bar\tau_m(t)\over64},\ {1\over64}
  \right\}.}
\]
The visible vertices transfer back to the original rows with the margin loss
from Section 3.6.  Let
\[
  e_m(t)=2Q_m+L_m\|P(t)-P_0\|_{\infty,1}.
\]
A sufficient transfer condition, including slack for the far-row threshold
\(\rho=4\bar\tau_m(t)\), is
\[
  e_m(t)\le{\bar\tau_m(t)\over256},
  \qquad
  4\Lambda_m e_m(t)\le {\eta_m\bar\tau_m(t)\over128}.
\]
Under these displayed inequalities the surviving recurrent vertices of the
recoded boundary stratum are visible in the original target, and the reference
height changes by the explicit bounds in Section 3.5.

This is the repaired uniform two-scale statement.  It is uniform over a fixed
recoding profile.  If the profile still contains small survivor masses or
small transient coefficients, recode again.  Each recurrent recoding removes
at least one recurrent coordinate from a block or each face recoding removes
at least one transient coefficient from a row face.  Hence the support pattern
strictly decreases, and there are at most
\[
  n+\#\{(i,s):i\in T,\ \alpha_{is}>0\}\le n+n k\le n+n^2
\]
elementary drops.  If only recurrent support is counted, the bound is \(n\).

For an analytic arc \(P(t)\), the honest radius is therefore
\[
  r_m=\sup\left\{r>0:
  \text{the two boxed fixed-mass inequalities and the transfer inequality hold
  for }0<t<r\right\}.
\]
It depends on the degeneration profile through
\[
  \mu_m,\quad \eta_m,\quad \Lambda_m,\quad Q_m,\quad
  \|P(t)-P_0\|_{\infty,1},\quad
  \bar\tau_m(t).
\]
There is no valid radius depending only on \(n\) or on a threshold
\(\theta\).  This is exactly the quantifier correction from the w20 audit.

## 5. Why The W20 Stress Family Now Passes

The old stress cases drop \(n_{\rm small}\) masses just below a threshold
\(\theta\), leaving one survivor just above \(\theta\).  The old invalid test
compared the recoding distance to \(\mu(P_0')/8\), producing failures
`62.7..313`.

The repaired quantities are:
\[
  \|P_0-P_0'\|_{\infty,1}=2q_s,\qquad
  {|\pi_s'(j)-\pi_s(j)|\over \pi_s'(j)}=q_s,
\]
and, for the transient face coefficient \(\alpha=\theta/2\),
\[
  \|\alpha-\alpha'\|_1=2\alpha .
\]
The saved run gives:

```text
w20_stress_4_1e-05:  q=3.96e-05   eps/(2Q)=0.887892  old ratio=62.7302   passes=True/True/True
w20_stress_8_1e-05:  q=7.92e-05   eps/(2Q)=0.940618  old ratio=125.455   passes=True/True/True
w20_stress_20_1e-05: q=0.000198   eps/(2Q)=0.975369  old ratio=313.601   passes=True/True/True
w20_stress_20_0.0001:q=0.00198    eps/(2Q)=0.975369  old ratio=313.042   passes=True/True/True
```

The mixed-rate tests also pass:

```text
cases: 12
nonexpansive_failures: 0
delta_nonincrease_failures: 0
worst eps/(2Q): 0.925227
```

## 6. L3 Status

The w19 tangent lemma is available at every H-M point:
\[
  \dot H^+\le2\dot\delta .
\]
It quantifies over all H-M points, so it applies to every recoded boundary
base \(P_m\), not only to interior strata.

The strata-induction plan is therefore:

1. Fix a support stratum.  If an arc has a nonzero first normal term, w19 gives
   the sharp first-order bound \(2\).
2. If small recurrent masses or transient coefficients are crossed before the
   target scale, use L1+L2 to recode to the boundary stratum and continue.
3. Since support decreases, boundary recoding terminates.

The remaining obstruction is not L1 or L2.  It is the dangerous-jet case from
w21_second: after every first-order normal cost vanishes, one needs a
finite-jet normal projection estimate showing that the first non-H-M jet pays
delta at the same order.  In formula, one needs a fixed-base constant
\(L(P_m)\) such that, after all H-M rebasings through lower order,
\[
  q_H\le L(P_m) q_\delta .
\]
The w21 numerics still support the expected picture.  In the saved
`second_order_full_records.json` filter:

```text
with_local_samples: 252
max_local_ratio: 0.0
with_transition_samples: 608
max_transition_ratio: 2.0000000000392326
sharp_transition_count_ratio_ge_1p9: 49
```

The sharp ratio-2 samples all occur in the boundary window, with
`t/min_positive_entry` from about `28` to `2250` in the top cases.  This is
exactly the recoding regime handled by L1+L2, but it does not prove the
finite-jet projection estimate needed to assemble the full local linear law.

So the local law remains:

```text
L3 status: one remaining estimate, the finite-jet normal projection bound.
```
