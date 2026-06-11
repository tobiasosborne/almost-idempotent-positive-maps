# w21_recode_audit — HOLD WITH REPAIR: L1 banked; L2 only in final-profile one-shot form (codex hostile audit, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w21_recode_audit/brief.md. Long form: experiments/out/w21_recode_audit/audit_report.md.

VERDICT: **HOLD WITH REPAIR**.

I wrote the long-form audit to [audit_report.md](/tmp/codex-sigma-wall/w21_recode_audit/audit_report.md). I did not create `answer.md`.

Key result: L1 survives, including exact H-M idempotence and the `2(sum q_s + q')` removed-mass bound. L2 only survives in the repaired final-profile form. The literal stepwise “recode again and add errors” reading is broken; my explicit sequential family overcharges by `10.8x` at 12 drops.

Artifacts:
- [independent_recode_audit.py](/tmp/codex-sigma-wall/w21_recode_audit/independent_recode_audit.py)
- [independent_recode_summary.txt](/tmp/codex-sigma-wall/w21_recode_audit/independent_recode_summary.txt)
- [independent_recode_results.json](/tmp/codex-sigma-wall/w21_recode_audit/independent_recode_results.json)
- [progress.md](/tmp/codex-sigma-wall/w21_recode_audit/progress.md)

Verification passed:
`python3 -m py_compile independent_recode_audit.py`
`python3 independent_recode_audit.py`
---
## Appendix: audit_report.md (verbatim)

# VERDICT: HOLD WITH REPAIR

L1 survives hostile audit.  The recoded point is an exact H-M stochastic
idempotent, the rowwise bound
\[
\|P_0-P_0'\|_{\infty,1}\le 2\left(\sum_s q_s+q'\right)
\]
is correct with \(q'=\max_i r_i\) for the max-row norm, and the w20 stress
family no longer violates the repaired removed-mass accounting.

L2 is not valid as a literal "iterate and add the step errors" argument.  That
version is the old trap at one higher level: relative removed masses measured
after each renormalization can sum to \(O(n)\) while the final original removed
mass is \(O(1)\).  L2 holds only in the repaired form: choose the final boundary
profile, measure all removed recurrent and transient-face mass in the original
profile (or equivalently collapse the chain), recompute \(\mu_m,\eta_m,\Lambda_m\),
and apply the fixed-mass visibility lemma once on that final recoded stratum.
No radius depending only on \(n\) or a threshold is justified.

Independent artifacts written in this workdir:

- `independent_recode_audit.py`
- `independent_recode_results.json`
- `independent_recode_summary.txt`
- `progress.md`

Verification:

```text
python3 -m py_compile independent_recode_audit.py
python3 independent_recode_audit.py
```

Both completed after one syntax patch during development.

## L1 Re-Derivation

Let the original H-M point have recurrent blocks \(C_s\), recurrent laws
\(\pi_s\), transient rows \(\sum_s\alpha_{is}\pi_s\), removed recurrent sets
\(D_s\), survivors \(K_s=C_s\setminus D_s\), and
\[
q_s=\sum_{j\in D_s}\pi_s(j).
\]
For transient face drops \(E_i\), put
\[
r_i=\sum_{s\in E_i}\alpha_{is}.
\]
The construction requires \(K_s\ne\emptyset\), \(q_s<1\), and \(r_i<1\).  If
one wants the perturbative "small relative shift" reading, one needs \(q_s\)
and \(r_i\) small; the exact algebra itself only needs strict inequality.

The recoding is
\[
\pi_s'=\frac{\pi_s|_{K_s}}{1-q_s}.
\]
The new recurrent blocks are \(K_s\).  Removed recurrent rows \(j\in D_s\) are
new transient rows with coefficient \(e_s\).  Old transient rows get
\[
\alpha'_{is}=0\quad(s\in E_i),\qquad
\alpha'_{is}=\frac{\alpha_{is}}{1-r_i}\quad(s\notin E_i).
\]

This is exactly H-M.  Every row is a convex mixture of the recoded recurrent
laws; all new transient columns \(T\cup\bigcup_sD_s\) are zero; and
\(\pi_s'P'=\pi_s'\) because \(\pi_s'\) is supported only on rows in \(K_s\),
all equal to \(\pi_s'\).  Hence every transient mixture also satisfies
\(p_i'P'=p_i'\), so \(P'^2=P'\) exactly.

Row distances:

- Recurrent row in block \(s\), including a removed row now made transient:
  \[
  \|\pi_s-\pi_s'\|_1=2q_s.
  \]
- Old transient row:
  \[
  \left\|\sum_s\alpha_{is}(\pi_s-\pi_s')\right\|_1
  =2\sum_s\alpha_{is}q_s\le 2\sum_s q_s.
  \]
  The coefficient face move has exact size
  \[
  \|\alpha_i-\alpha_i'\|_1=2r_i,
  \]
  and because the recoded recurrent supports are disjoint this is the same
  row movement after the recurrent laws are fixed.  Thus
  \[
  \|p_i^0-p_i'\|_1\le 2\sum_s q_s+2r_i.
  \]

Taking the max over rows gives the advertised constant \(A=2\), provided
\(q'\) is the max dropped transient-face mass \(q'=\max_i r_i\).  If \(q'\) is
instead the total over all transient rows, the bound remains true but is
unnecessarily weaker.

The survivor mass statement is also correct:
\[
\mu(P_0')=\min_{s,j\in K_s}\frac{\pi_s(j)}{1-q_s}
\ge \min_{s,j\in K_s}\pi_s(j).
\]
The relative coordinate shift is exactly \(q_s\) only when measured against
the recoded coordinate:
\[
\frac{|\pi_s'(j)-\pi_s(j)|}{\pi_s'(j)}=q_s.
\]
Measured against the original coordinate it is \(q_s/(1-q_s)\), which blows up
as \(q_s\to1\).  The near-total-removal numerical case below confirms this is
a range issue, not an exactness failure.

## L2 And Compounding

The fixed-profile L2 inequalities in the claimed note are the right shape:
\[
\varepsilon_m(t)\le
\min\{\mu_m/8,\bar\tau_m(t)/64,\eta_m\bar\tau_m(t)/64,1/64\}
\]
plus transfer conditions involving
\[
e_m(t)=2Q_m+L_m\|P(t)-P_0\|_{\infty,1}.
\]
The dependencies on \(\mu_m,\eta_m,\Lambda_m,Q_m\), and the target scale
\(\bar\tau_m(t)\) are real.

The dangerous part is the sentence "recode again."  If a block is recoded
sequentially and the step masses are measured after renormalization, then
\[
Q_{\rm final}^{\rm orig}=1-\prod_\ell(1-q_\ell^{\rm step}),
\]
not \(\sum_\ell q_\ell^{\rm step}\).  The one-shot final-profile distance is
\[
2Q_{\rm final}^{\rm orig},
\]
while a triangle bound using \(\sum_\ell q_\ell^{\rm step}\) can be \(O(n)\)
larger.  My explicit chain used block masses
\[
0.9,\ 0.09,\ 0.009,\ldots,\ 0.1^m
\]
and removed one coordinate per step.  For 12 drops the final original removed
mass is essentially \(1\), but the stepwise relative charges sum to
`10.8000035755`, giving a chain/direct overcharge of `10.8000036`.

So the repaired L2 statement must say this explicitly:

1. Select the final support/face profile \(m=(D_s,E_i)\).
2. Compute \(q_s,r_i,Q_m\) relative to the original base for that profile, or
   collapse any sequential chain using \(1-\prod(1-q_\ell)\).
3. Apply the one-shot recoding map and the fixed-mass lemma on \(P_m\).
4. Recompute or separately lower-bound \(\eta_m\), and keep the \(\Lambda_m\)
   margin-loss term.

The same warning applies to transient face drops.  Sequentially dropping face
mass after renormalization is not the same accounting as original face mass;
collapse the final kept face before charging the error.  It also avoids
multiplying the row-map Lipschitz constants across repeated face transports.

Stopping is finite for a fixed finite support profile.  For real-analytic or
Puiseux degeneration profiles, finite leading-order comparisons make the
eventual profile well-defined after choosing the scale regime.  Without such
regularity, the statement is false as a universal claim: the exact H-M arc
\[
P(t)=
\begin{pmatrix}
1&0&0\\
0&1&0\\
\alpha(t)&1-\alpha(t)&0
\end{pmatrix},
\qquad
\alpha(t)=t(2+\sin(1/t)),
\]
with \(\alpha(0)=0\), is convergent and exact H-M for \(t>0\), but
\(\alpha(t)/t\) crosses the threshold \(2\) infinitely often.  My sampled
probe saw `119` threshold crossings.  This is not analytic at zero, so it does
not refute the analytic-arc version; it refutes any unstated
regularity-free "every degeneration profile stabilizes" reading.

## Independent Numerics

Summary from `independent_recode_summary.txt`:

```text
cases checked: 60
failed removed-mass/exactness cases: 0
worst eps/(2Q): 1.00000000001
worst survivor shift relative to old mass: 499999.000013
```

The `1.00000000001` is roundoff at an equality case; the pass/fail check used
tolerance and found no violation.

w20 stress family:

```text
w20_stress_4_1e-05:  q=3.96e-05  r=5e-06  eps=7.92e-05   2Q=8.92e-05  eps/(2Q)=0.887892377  old eps/(mu/8)=62.7301891
w20_stress_8_1e-05:  q=7.92e-05  r=5e-06  eps=0.0001584  2Q=0.0001684 eps/(2Q)=0.940617577  old eps/(mu/8)=125.45541
w20_stress_20_1e-05: q=0.000198  r=5e-06  eps=0.000396   2Q=0.000406  eps/(2Q)=0.975369458  old eps/(mu/8)=313.601261
w20_stress_20_0.0001:q=0.00198   r=5e-05  eps=0.00396    2Q=0.00406   eps/(2Q)=0.975369458  old eps/(mu/8)=313.042313
```

Edge cases:

```text
explicit_two_block:          q_total=0.19     r=0.21  eps/(2Q)=0.66325     passes=True
multi_block_simultaneous:    q_total=0.69     r=0.3   eps/(2Q)=0.449494949 passes=True
near_total_block_removal:    q_total=0.999998 r=0     eps/(2Q)=1           passes=True
transient_only_faces:        q_total=0        r=0.001 eps/(2Q)=1           passes=True
```

The near-total-removal case has `mu_after=1`, new-relative survivor shift
`0.999998`, and old-relative survivor shift `499999.000013`.  This confirms
the exact mass-floor claim but also shows why a small-\(q_s\) hypothesis is
needed for perturbative use.

Mixed and random cases:

```text
claimant mixed-rate reimplementation: cases=12 failures=0 worst eps/(2Q)=0.957530678
random hostile cases:                cases=40 failures=0 worst eps/(2Q)=1
recurrent transport: l1 violations=0 delta violations=0 worst_l1_ratio=1
```

Sequential compounding trap:

```text
steps=2:  direct_removed=0.99           sum_step_q=1.8          chain/direct=1.81818182
steps=4:  direct_removed=0.9999         sum_step_q=3.6          chain/direct=3.60036004
steps=8:  direct_removed=0.99999999     sum_step_q=7.20000000036 chain/direct=7.20000007
steps=12: direct_removed=0.999999999999 sum_step_q=10.8000035755 chain/direct=10.8000036
```

w21_second boundary records:

```text
records=172 local=252 max_local=0.0 transition=608 max_transition=2.0000000000392326 sharp_ge_1p9=49
sharp ratio=2.00000000004 stratum=random_014 t=1e-05  min_entry=3.51e-07 t/min=28.4664  visible=5 vertices=6
sharp ratio=2.00000000001 stratum=random_014 t=3e-05  min_entry=3.51e-07 t/min=85.3991  visible=5 vertices=6
sharp ratio=2               stratum=random_011 t=3e-05 min_entry=4.44e-07 t/min=67.4924  visible=3 vertices=4
sharp ratio=2               stratum=random_014 t=0.0001 min_entry=3.51e-07 t/min=284.664 visible=5 vertices=6
sharp ratio=2               stratum=random_011 t=0.0003 min_entry=4.44e-07 t/min=674.924 visible=3 vertices=4
```

These are finite-scale boundary events, not fixed-base local second-order
violations.  L1+repaired L2 explain why the old stress mechanism is not a
counterexample, but they do not prove the finite-jet local law.

## L3 Assessment

With L1 and repaired L2 in hand, the remaining statement is still the finite
jet normal projection estimate.  A precise form is:

\[
\operatorname{dist}\bigl(J^mP,J^m\mathcal M_{\rm HM}\bigr)^2
\le L(P_m)\,\delta_m(P)
\]

after all lower-order H-M rebasings and boundary recodings have been performed.
Equivalently, at the first genuinely non-H-M jet, the visible-hull height
coefficient must be bounded by the first negative active-entry coefficient
with a constant depending on the fixed recoded base.

The w19 first-order lemma applies at every recoded H-M base, but it only
handles the first nonzero normal term.  It does not supply finite determinacy
through dangerous jets where the first-order normal cost vanishes.

The w20 arc-scale issue for \(\tau(t)=\sqrt{\delta(P(t))}\) is not eliminated
by L1/L2.  The fixed-mass lemma still contains the target-scale hypotheses
\(\varepsilon\le\tau/64\) and \(\varepsilon\le\eta\tau/64\).  To turn those
into an interval in \(t\), one still needs a lower scale estimate for
\(\tau(t)\).  The missing L3 projection/delta coefficient estimate would
provide that; until then, it remains an open dependency, not a solved
consequence of recoding.

## Calibration

My calibrated probability that this verdict survives further hostile audit:

```text
P(HOLD WITH REPAIR verdict survives) = 0.76
P(L1 exact constants survive)        = 0.91
P(repaired fixed-profile L2 survives)= 0.74
P(L3 assembles from current material) = 0.32
```

Bottom line: L1 is solid.  L2 is usable only as a fixed-final-profile,
two-scale recoding statement with explicit \(Q_m,\eta_m,\Lambda_m,\tau(t)\)
dependencies.  The naive sequential iteration reading is broken by an explicit
compounding family.
