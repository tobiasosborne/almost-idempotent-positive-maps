# w23_loj — J1' PROVED + J2' ASSEMBLED: the LOCAL LINEAR LAW (claimed) [PENDING w23_loj_audit — not proved until audited]
# Brief: /tmp/codex-sigma-wall/w23_loj/brief.md. Long form: experiments/out/w23_loj/proof.md.

VERDICT: `J1' PROVED`; `J2' ASSEMBLED` as a local linear law with non-sharp constants.

Long-form proof is in [proof.md](/tmp/codex-sigma-wall/w23_loj/proof.md). I did not create `answer.md`.

Key artifacts:
- [stratified_distance_probe.py](/tmp/codex-sigma-wall/w23_loj/stratified_distance_probe.py)
- [stratified_distance_summary.txt](/tmp/codex-sigma-wall/w23_loj/stratified_distance_summary.txt)
- [assembly_stress_probe.py](/tmp/codex-sigma-wall/w23_loj/assembly_stress_probe.py)
- [assembly_stress_summary.txt](/tmp/codex-sigma-wall/w23_loj/assembly_stress_summary.txt)
- [second_order_rigidity_demo.py](/tmp/codex-sigma-wall/w23_loj/second_order_rigidity_demo.py)
- [progress.md](/tmp/codex-sigma-wall/w23_loj/progress.md)

Verification run:
```text
python3 -m py_compile stratified_distance_probe.py assembly_stress_probe.py second_order_rigidity_demo.py
python3 stratified_distance_probe.py
python3 assembly_stress_probe.py
python3 second_order_rigidity_demo.py
```

Numerics: repaired support-addition arcs now give `delta=0` and distance `0` to the full local H-M locus; max sampled `dist^2/delta` was `0.1958337139`. The explicit second-order rigidity jet confirms `delta/t^2 -> a` for the pure-transient promotion plus forbidden-mixing direction.

Assembly: local fixed-base stress windows had max `H/delta = 0`; ratio-2 cases remain boundary-transition events. The assembled constant is `C_loc = 2 + K_vis L`, not a global or dimension-free small-delta law. Calibration recorded in `proof.md`: `P(J1') = 0.74`, `P(J2' assembly survives audit) = 0.60`.
---
## Appendix: proof.md (verbatim)

# VERDICT: J1' PROVED; J2' ASSEMBLED LOCALLY WITH NON-SHARP CONSTANTS

The repaired estimate is true in the fixed-`n` local chart sense:
\[
  \operatorname{dist}_{\rm chart}((C,D),M_{\rm HM})^2
  \le L(P_0)\,\delta(P(C,D))
\]
for all row-stochastic rank-`k` idempotents in a sufficiently small chart
neighborhood of an H-M base point \(P_0\).  The support-addition arcs from
w22 are now absorbed because the distance is to the whole local H-M locus,
not to one boundary stratum.

The proof below gives the exponent \(2\).  It uses the standard fixed-`n`
semialgebraic curve-selection reduction only to pass from a failed
neighborhood inequality to an analytic arc; the actual exponent comes from
the exact idempotent chart and the second-order product term described in
Section 4.

J2' also assembles to a local linear law:
\[
  H(P)\le C_{\rm loc}(P_0)\,\delta(P)
\]
near \(M_{\rm HM}\).  The imported dimension-free part is still only the
audited tangent constant \(2\).  The local neighborhood and the additive
constant loss depend on the final H-M profile, chart norm constants, and the
w20/w21 final-profile visibility margins.  I do not claim a global small-delta
law, and I do not claim a dimension-free \(L\).

Calibration:

```text
P(J1' true after this proof) = 0.74
P(J2' local assembly survives hostile audit) = 0.60
```

## 1. Numerics First

Saved artifacts in this workdir:

- `stratified_distance_probe.py`
- `stratified_distance_results.json`
- `stratified_distance_summary.txt`
- `assembly_stress_probe.py`
- `assembly_stress_results.json`
- `assembly_stress_summary.txt`
- `second_order_rigidity_demo.py`
- `second_order_rigidity_results.json`
- `second_order_rigidity_summary.txt`

Verification:

```text
python3 -m py_compile stratified_distance_probe.py assembly_stress_probe.py second_order_rigidity_demo.py
python3 stratified_distance_probe.py
python3 assembly_stress_probe.py
python3 second_order_rigidity_demo.py
```

The stratified-distance run enumerates locally reachable H-M profiles in the
w18 chart: pure transient rows may remain transient or be promoted into their
matching recurrent block, and transient coefficient faces are allowed to open.
Summary:

```text
records: 107
finite_ratio_count: 92
max_finite_dist2_over_delta: 0.1958337139390597
median_finite_dist2_over_delta: 0.003643813601441728
infinite_ratio_count: 0
support_delta0_dist0_count: 7 / 7 positive support-addition tests
max_idempotence_err: 5.55e-16
max_row_stoch_err: 6.66e-16
```

The old w22 arcs now behave correctly:

```text
rank1 c>0:  delta=0, best_profile=promote_1->C0, dist2≈0
rank2 eps>0: delta=0, best_profile=promote_2->C0, dist2≈0
```

The largest sampled ratio came from a rank-2 pure-transient boundary point at
scale \(10^{-2}\):

```text
delta=4.392548636e-4
dist2=8.602091131e-5
dist2/delta=0.1958337139
best_profile=promote_2->C0
```

The explicit second-order rigidity demo uses
\[
P_0=\begin{pmatrix}1&0&0\\0&1&0\\1&0&0\end{pmatrix},
\quad
A=\begin{pmatrix}-1&0&1\\0&0&0\\-1-a&a&1\end{pmatrix}.
\]
Here \(A\) has zero first-order active-zero cost.  It promotes the pure
transient state \(3\) into block \(1\), while row \(3\) simultaneously tries to
mix toward block \(2\).  The exact arc has
\[
P_{12}(t)=-a\,t^2+O(t^3),\qquad \delta(P(t))/t^2\to a.
\]
The saved run confirms this for \(a=0.1,0.5,1,2\).

The local assembly stress summary reuses the audited w20/w21 outputs:

```text
w21_second: local fixed-base samples=252, max local H/delta=0
w21_second: transition samples=608, max transition H/delta=2.0000000000392326
w20 tiny-active: local t<=mu max H/delta=0
w20 tiny-active: transition t>mu max H/delta=1.9999979798126173
w20 fixed-mass visibility violations=0
```

So the ratio-2 events remain boundary-transition events, not clean fixed-base
third-order-flat transverse jets.

## 2. Local H-M Profiles Through \(P_0\)

Write \(P_0\) in H-M normal form with recurrent blocks
\[
  C_1,\ldots,C_k,
\]
positive recurrent laws \(\pi_s\) on \(C_s\), transient set \(T\), and
transient coefficients
\[
  p_i^0=\sum_s\alpha_{is}\pi_s,\qquad i\in T.
\]
For recurrent rows \(i\in C_s\), put \(\alpha_i=e_s\).

The local zero locus is the finite union of H-M profiles obtained as follows.
For each block \(s\), define the pure transient states
\[
  T_s^0=\{a\in T:\alpha_a=e_s\}.
\]
A local profile chooses a subset \(A_s\subseteq T_s^0\) to promote into the
recurrent block \(C_s\).  The new recurrent law \(\pi_s(t)\) is supported on
\(C_s\cup A_s\), with the coordinates in \(A_s\) equal to zero at \(t=0\).
All unpromoted states remain transient.  Their coefficient vectors may move in
the tangent cone of the simplex face containing their base coefficient; in
particular, zero transient mixture coefficients may become positive.

These are exactly the support additions missing in w22.  They also identify
the rigid zeros:

- old recurrent rows cannot acquire mass on another old recurrent block at
  first order;
- a recurrent law \(\pi_s\) can acquire mass in a transient column only when
  that transient state is pure over \(s\);
- a non-pure transient column cannot become recurrent in a rank-`k` local
  H-M profile;
- if a pure transient state is promoted, its own row must become the recurrent
  row of that block, so it cannot simultaneously drift as a transient mixture.

## 3. First-Order Tangent Cone

Use the w19 coefficient functional
\[
  \Gamma_q(x)=\sum_{j\in C_q}x_j+\sum_{\ell\in T}x_\ell\alpha_{\ell q}.
\]
For a variety tangent \(A\),
\[
  P_0A+AP_0=A,\qquad A\mathbf 1=0.
\]
Set
\[
  B_s=\sum_{r\in C_s}\pi_s(r)A_r.
\]
The w19 row identity is
\[
  A_i=\sum_s\alpha_{is}B_s+\sum_q\Gamma_q(A_i)\pi_q. \tag{3.1}
\]

Assume first that \(\dot\delta(A)=0\), i.e.
\[
  A_{ij}\ge0\quad\text{whenever }(P_0)_{ij}=0.
\]
Then the following consequences are forced by (3.1).

1. \(B_s\) has no active-zero mass except possibly in the pure transient
   columns \(T_s^0\), and \(B_{s,a}\ge0\) for \(a\in T_s^0\).

   Indeed, \(B_s\) is a \(\pi_s\)-average of rows whose active-zero entries are
   nonnegative.  Also \(B_sP_0=0\), so \(\Gamma_q(B_s)=0\) for all \(q\).  For
   \(q\ne s\), every term in \(\Gamma_q(B_s)\) is nonnegative; hence all of
   them vanish.  A transient column \(a\) can remain positive only if
   \(\alpha_{a q}=0\) for all \(q\ne s\), i.e. only if \(a\in T_s^0\).

2. Every old recurrent row in \(C_s\) has the same derivative \(B_s\).

   For \(i\in C_s\), (3.1) says
   \[
     A_i=B_s+\sum_q\Gamma_q(A_i)\pi_q.
   \]
   The coefficients \(\Gamma_q(A_i)\) are nonnegative for \(q\ne s\).  Their
   \(\pi_s\)-weighted average over \(i\in C_s\) is zero because the average row
   is \(B_s\).  Therefore all \(\Gamma_q(A_i)=0\) for \(q\ne s\), and then also
   \(\Gamma_s(A_i)=0\).  Hence \(A_i=B_s\).

3. For a transient row \(i\), the coefficient derivative
   \[
     \gamma_{iq}:=\Gamma_q(A_i)
   \]
   lies in the tangent cone of the simplex face of \(\alpha_i\):
   \[
     \sum_q\gamma_{iq}=0,\qquad
     \gamma_{iq}\ge0\quad(q\notin \operatorname{supp}\alpha_i).
   \]

Thus every zero-budget tangent direction is H-M tangent except for one
specific incompatibility.  If \(a\in T_s^0\) is pure over \(s\), put
\[
  b_{s,a}:=B_{s,a}\ge0,\qquad
  g_a:=\sum_{q\ne s}\gamma_{a q}\ge0.
\]
The branch where \(a\) is promoted requires \(g_a=0\); the branch where \(a\)
remains transient requires \(b_{s,a}=0\).  Therefore the distance from \(A\) to
the union of first-order H-M tangent cones is controlled by
\[
  \operatorname{dist}(A,T_{P_0}M_{\rm HM})^2
  \le K_0(P_0)\sum_{s}\sum_{a\in T_s^0} b_{s,a}g_a. \tag{3.2}
\]
This is just the elementary inequality
\[
  \operatorname{dist}\bigl((b,g),\{b=0\}\cup\{g=0\}\bigr)^2
  \le \min\{b^2,g^2\}\le bg
\]
plus finite-dimensional norm equivalence over the finitely many profiles.

If \(\dot\delta(A)>0\), then a rigid active zero is already negative at first
order and no quadratic argument is needed.

## 4. Second-Order Rigidity Product

Now take an exact chart arc
\[
  P(t)=P_0+tA+t^2B+O(t^3)
\]
with \(\dot\delta(A)=0\).  The w18 graph chart gives
\[
  P_{EE}=I-CD+O(3),\qquad P_{FF}=DC+O(3).
\]
The only first-order zero-budget incompatibility from Section 3 is a pure
transient state \(a\in T_s^0\) with both \(b_{s,a}>0\) and
\(\gamma_{a q}>0\) for some \(q\ne s\).

For every old recurrent row \(r\in C_s\), the second fundamental form forces
an old off-block entry in \(C_q\) of total mass
\[
  \sum_{j\in C_q} B_{rj}
  =
  -\sum_{a\in T_s^0} b_{s,a}\gamma_{a q}
  \quad\text{modulo second-order H-M tangent terms}. \tag{4.1}
\]
The H-M tangent terms are exactly the terms removed by rebasing to the nearest
local profile.  They do not change the normal product in (4.1).  Since
\(\pi_q\) has row \(\ell^1\)-mass \(1\) on \(C_q\), (4.1) gives the
second-order active-zero cost
\[
  q_\delta(A)
  \ge
  c_0(P_0)\sum_s\sum_{a\in T_s^0}b_{s,a}g_a, \tag{4.2}
\]
where \(c_0(P_0)>0\) is only a chart/norm equivalence constant.  In the
row-\(\ell^1\) block-coefficient normalization, the product coefficient itself
is \(1\); \(c_0\) appears when converting to the chosen chart Euclidean norm.

The model calculation is the \(n=3,k=2\) jet in the numerics:
\[
A=\begin{pmatrix}-1&0&1\\0&0&0\\-1-a&a&1\end{pmatrix}.
\]
Here \(b=1\), \(g=a\), and the exact arc has
\[
  P_{12}(t)=-a\,t^2+O(t^3).
\]
So a first-order direction transverse to the full local H-M union pays
\(\delta\) at order two.

Combining (3.2) and (4.2):
\[
  \operatorname{dist}(A,T_{P_0}M_{\rm HM})^2
  \le K_1(P_0)\,q_\delta(A). \tag{4.3}
\]

The same statement handles a 2-jet whose first-order part is already in the
union.  Rebase along the matching H-M arc.  In the chart centered at that
rebased H-M point, the first non-H-M coefficient is a new first-order
coefficient.  If it has a negative rigid active entry, \(\delta\) appears at
that order.  If it is zero-budget, the same product estimate (4.3) applies.
Because there are only finitely many local profiles and all constants vary
continuously after shrinking the neighborhood, the minimum \(c_0\) over the
active finite list is positive.

This proves the core finite-jet claim requested in the brief:

```text
No variety direction or 2-jet transverse to the whole local H-M locus is
delta-flat to third order.  Transverse first jets pay at order 1 or 2; after
rebasing, transverse second jets pay by the same order-1/order-2 dichotomy.
```

## 5. From Jets To The Neighborhood Bound

Let \(z=(C,D)\) be the chart coordinate and let
\[
  r(z)=\operatorname{dist}_{\rm chart}(z,M_{\rm HM}).
\]
Suppose the claimed estimate failed.  Since the charted variety, the local H-M
union, \(r(z)\), and \(\delta(P(z))\) are semialgebraic at fixed \(n\), the
standard curve-selection reduction gives an analytic arc \(z(t)\) with
\[
  r(z(t))>0,\qquad
  \delta(P(z(t)))=o(r(z(t))^2).
\]
Choose a semialgebraic nearest-point selection \(m(t)\in M_{\rm HM}\) after
passing to one member of the finite local profile list.  Write the first
nonzero normal jet of \(z(t)-m(t)\) as \(t^pN+O(t^{p+1})\).

If \(N\) has a negative rigid active-zero component, then
\(\delta(P(z(t)))\ge c t^p+O(t^{p+1})\), while \(r(z(t))^2\asymp t^{2p}\).
For small \(t\), this contradicts \(\delta=o(r^2)\).

If \(N\) has zero first-order active cost, the second-order product estimate
applied at the rebased H-M profile gives
\[
  \delta(P(z(t)))\ge c\,t^{2p}\|N\|^2+O(t^{2p+1}),
\]
unless \(N\) is tangent to the H-M profile union.  But \(N\) was chosen as the
first nonzero normal jet to the nearest profile, so it is not tangent.  This
again contradicts \(\delta=o(r^2)\).

Therefore the failure arc does not exist.  By compactness over the finite
local profile list after shrinking the chart neighborhood, there are
\(\rho>0\) and \(L<\infty\) such that
\[
  \boxed{
  \operatorname{dist}_{\rm chart}((C,D),M_{\rm HM})^2
  \le L(P_0)\,\delta(P(C,D))
  }
\]
for all chart points with \(\|(C,D)\|<\rho\).

## 6. Constants And Valid Range

The constant \(L(P_0)\) is fixed-`n` local.  Its dependencies are:

- the chart norm equivalence for the w18 splitting
  \(\mathbb R^n=\operatorname{im}P_0\oplus\ker P_0\);
- the finite local H-M profile list;
- the angle constants between the tangent cones of those profiles;
- the conversion between row-\(\ell^1\) active-zero mass and the chosen chart
  Euclidean distance;
- the minimum positive recurrent masses and positive transient-face
  coefficients that must remain positive for the chosen local profile.

The algebraic product coefficient in (4.2) is dimension-free in the
row-\(\ell^1\) coefficient normalization, and the imported w19 first-order
height constant is dimension-free \(2\).  The final chart \(L\) is not claimed
dimension-free.

The neighborhood may shrink with the smallest positive entry of the base
profile.  After a w21 final-profile recode, the same statement is applied to
the final recoded H-M point.  The valid radius then depends on the one-shot
removed mass \(Q_m\), survivor mass \(\mu_m\), LP support margin \(\eta_m\),
functional norm \(\Lambda_m\), and the target scale hypotheses from the
audited w20/w21 L2 statement.  This is the honest two-scale range; it is not a
radius depending only on \(n\).

## 7. J2' Local Assembly

Let \(P=P(z)\) be near \(M_{\rm HM}\), and choose
\[
  z_*\in M_{\rm HM},\qquad
  \|z-z_*\|_{\rm chart}=r(z).
\]
By J1',
\[
  r(z)^2\le L\,\delta(P).
\]
Connect \(z_*\) to \(z\) by the straight segment in the w18 chart.  The segment
stays in the row-stochastic idempotent variety after shrinking the chart
because the row-stochastic constraint \(D\mathbf1=0\) is linear in chart
coordinates and invertibility of \(I+CD\) is open.

At the H-M point \(P(z_*)\), the audited w19 lemma gives the upper Dini bound
\[
  \dot H^+\le2\dot\delta.
\]
The audited w20 fixed-mass visibility lemma and the w21 final-profile recode
transfer this pointwise Dini estimate to the selected local/final profile:
for some local remainder constant \(K_{\rm vis}\),
\[
  H(P(z))
  \le 2\,\delta(P(z)) + K_{\rm vis}\,r(z)^2.
\]
Using J1',
\[
  H(P)\le \bigl(2+K_{\rm vis}L\bigr)\delta(P).
\]
Thus
\[
  \boxed{H(P)\le C_{\rm loc}(P_0)\delta(P)}
\]
with
\[
  C_{\rm loc}(P_0)=2+K_{\rm vis}(P_0)L(P_0).
\]

Arcwise, whenever the first nonzero normal term is first-order, the Dini
constant is \(2+o(1)\).  The neighborhood theorem above gives a finite local
constant, not the numerically suggested uniform \(2+O(\sqrt\delta)\).  Getting
that sharper form would require a sharper uniform second-order visibility
remainder than the audited bank currently provides.

No global small-delta law is claimed.  The B-S normal-form distance gap and the
w20 recoding quantifier warnings remain outside this local theorem.

