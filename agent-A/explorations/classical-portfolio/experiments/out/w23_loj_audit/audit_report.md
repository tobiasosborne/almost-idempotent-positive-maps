# VERDICT

J1': **HOLDS WITH REPAIR / CLARIFICATION.**  I did not find a support-addition or mixed-jet counterexample.  The repaired statement is credible as a fixed-base, fixed-`n`, closed-stratified local estimate
\[
  \operatorname{dist}_{chart}(z,M_{HM})^2 \le L(P_0)\,\delta(P(z)).
\]
The repair is not cosmetic: the local H-M locus must be the closure of the full finite profile union, and the promotable-zero list must include the induced transient-row entries created when a pure transient column is promoted into a block.  Constants and radius are genuinely profile-local.

J2': **BROKEN AS ASSEMBLED.**  I do not have a counterexample to the local linear law itself, but the claimed derivation of
\[
  H(P)\le(2+K_{vis}L)\delta(P)
\]
does not follow from the banked lemmas.  The invalid step is the line turning the endpoint Dini lemma plus visibility into the finite inequality
\[
  H(P(z))\le2\delta(P(z))+K_{vis}r(z)^2 .
\]
w19 gives only an upper Dini estimate at an H-M base.  w20/w21 give a two-scale fixed/final-profile visibility statement with target-scale hypotheses.  J1' gives \(r=O(\sqrt\delta)\), but not the much stronger visibility hypotheses \(\epsilon\le \tau/64\), \(\epsilon\le\eta\tau/64\), or uniform \(\mu,\eta\) along the nearest stratified H-M point.

Calibration: `P(J1' repaired statement survives) = 0.78`; `P(J2' assembly as written survives) = 0.18`; `P(local law is still true after a new finite visibility-remainder lemma) = 0.62`.

## Promotable/Rigid Zeros

At an H-M base with recurrent blocks \(C_s\), recurrent laws \(\pi_s\), transient set \(T\), and transient coefficients \(\alpha_i\):

- A transient state \(a\) is promotable into block \(s\) iff \(\alpha_a=e_s\).  Non-pure transient columns are rigid as recurrent support in a rank-`k` local profile.
- If \(a\in T_s^0\) is promoted into block \(s\), every row with block coefficient \(\alpha_{is}>0\) may acquire first-order mass in column \(a\).  This includes old recurrent rows in \(C_s\), promoted rows, and unpromoted transient rows mixed with block \(s\).  The proof note implies this through \(B_s\), but its bullet list should say it explicitly.
- An unpromoted transient row may open zero mixture coefficients: \(\gamma_{iq}\ge0\) for \(q\notin\operatorname{supp}\alpha_i\).
- For a pure transient state \(a\in T_s^0\), the two local choices are exclusive for that same row: promoted requires \(g_a=\sum_{q\ne s}\gamma_{aq}=0\); unpromoted requires \(b_{s,a}=B_{s,a}=0\).
- Old recurrent rows cannot acquire old off-block recurrent mass at zero first-order delta.  Such entries are rigid unless paid by linear negative active-zero mass.

Multi-entry simultaneous promotions are allowed independently: choose any subsets \(A_s\subseteq T_s^0\).  There is no new obstruction from promoting several pure transients in the same block; the incompatibility is the sum of the per-state products \(b_{s,a}g_a\).

## Exact Mixed-Jet Probe

I wrote `audit_probe.py` and saved `audit_probe_results.json` / `audit_probe_summary.txt`.

The key exact family is the smallest hostile corner:
\[
P_0=\begin{pmatrix}1&0&0\\0&1&0\\1&0&0\end{pmatrix}.
\]
For \(b,g\ge0\),
\[
P(b,g)=
\begin{pmatrix}
(1+bg)/(1+b)&-bg&b(1+bg)/(1+b)\\
0&1&0\\
(1-g)/(1+b)&g&b(1-g)/(1+b)
\end{pmatrix}
\]
is exactly row-stochastic and idempotent.  The \(b\)-axis is the support-promotion H-M branch, the \(g\)-axis is the transient-face-opening H-M branch, and together they force
\[
\delta(P(b,g))=bg.
\]

Selected results:

```text
balanced b=g=1e-3:      delta=1e-6,  dist2/delta=1.7495
b=t, g=t^2 at t=1e-3:  delta=1e-9,  dist2/delta=0.0017495
b=t^2, g=t at t=1e-3:  delta=1e-9,  dist2/delta=0.003495
b=g=t^2 at t=1e-3:     delta=1e-12, dist2/delta=1.75
```

The grid over 1156 \((b,g)\) pairs had max matrix-Frobenius proxy `dist2/delta = 2.4291`, median `0.0915`, and exact idempotence/row-sum residuals below `4e-16`.  This is not the claimant's chart norm, but at this fixed base it is norm-equivalent and enough to detect exponent failure.  No third-order-flat transverse 2-jet showed up; unbalanced higher-order mixes make `dist2/delta` smaller, not larger.

## J1' Assessment

The support-addition refutation from w22 is fixed by measuring distance to the full local H-M union.  On exact H-M axes, `delta=0` and distance to the union is zero.  On the mixed axes, the forced negative term is the product \(bg\), and the distance to the union is controlled by \(\min(b^2,g^2)\le bg\).

The proof's product estimate is the right local mechanism:
\[
\operatorname{dist}(A,T M_{HM})^2 \lesssim \sum b_{s,a}g_a
\lesssim q_\delta(A).
\]
The report should present the induced transient-row promotable entries explicitly, and it should state that \(L\) and the radius are over the closed finite profile union after shrinking around a fixed base.  With that repair, I failed to break J1'.

## Broken J2' Step

The exact family above also exposes the assembly flaw.  Take the balanced mixed point \(b=g=t\) and choose the nearest promoted H-M branch as the base profile.  At `t=1e-3`:

```text
delta = 1e-6
dist2/delta = 1.7495
epsilon_inf,l1_to_branch /(mu/8) = 12.8179
epsilon_inf,l1_to_branch /(tau/64) = 128
```

These ratios are scale-stable; shrinking `t` does not make the w20 visibility hypotheses true.  Thus the proof cannot apply the fixed-mass visibility lemma at the nearest support-added H-M point.  This example has `H=0`, so it is not a law counterexample.  It is a concrete failure of the claimed inference from nearest-locus point plus visibility to a finite `K_vis r^2` remainder.

The integration reading is also invalid.  The straight segment in the w18 chart stays in the idempotent variety, but w19 is a Dini statement at H-M bases.  Interior segment points are not H-M bases, so one cannot integrate a pointwise H-M-base derivative bound along the segment.  To get the displayed J2' estimate, a new finite lemma is needed:
\[
H(P(z))\le2\delta(P(z))+K_{vis}\operatorname{dist}_{chart}(z,M_{HM})^2
\]
on a fixed final profile with the w20/w21 two-scale visibility hypotheses already verified.  That lemma is not in the banked chain.

## Constants/Neighborhoods

For J1', the dependence of \(L(P_0)\) is honest but local: chart norm equivalence, finite profile angles, active-zero coefficient conversion, and positive base entries/faces.  If a smallest positive recurrent mass or positive transient coefficient tends to zero, the valid radius can shrink to zero.

For J2', the constants are not honestly assembled.  \(K_{vis}\) cannot be taken uniformly over nearest H-M points in the support-added union without extra work, because promoted masses and LP margins can tend to zero at the lower stratum.  The w21 repair is final-profile one-shot only; it does not license stepwise recoding or a radius depending only on \(P_0,n\).  `C_loc = 2 + K_vis L` is therefore conditional on an unproved finite visibility-remainder lemma.

## Independent Numerics

Certified matrix recomputation with the report's visible-height definition:

```text
w16 rational: delta=0.2284002679, H=0.0075669067, H/delta=0.0331300
w17 main:     delta=0.2329335240, H=0.0483561470, H/delta=0.2075963
w17 robust:   delta=0.2345924911, H=0.0484359827, H/delta=0.2064686
```

These are well above the local/corner scale (`delta≈0.23`), so they do not test the claimed local H-M neighborhood.  They also do not violate `H<=2delta`.

For the previously audited w20/w21 stress artifacts:

```text
w20 local t<=mu max H/delta = 0
w20 transition max H/delta = 1.9999979798
w21 local fixed-base max H/delta = 0
w21 transition max H/delta = 2.0000000000
```

I count these as prior-audited scalar stress data, not as fresh matrix recomputation.  They support the same conclusion: ratio-2 behavior is a boundary/transition phenomenon, while the fixed-base local windows did not produce a counterexample.

## Bottom Line

J1' survives my attack after the promotable-zero list and local-constant statement are made explicit.  J2' does not survive as a proof: the assembled finite inequality is exactly the missing theorem, not a consequence of w19+w20+w21+J1'.
