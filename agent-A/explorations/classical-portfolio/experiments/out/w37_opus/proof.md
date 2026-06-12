# VERDICT: PARTIAL (exact missing display in LaTeX below)

Independent second-family (Opus) attack on the SF/(CHARGE) lemma at
\(\delta_0=1/4\), \(\theta=1/2\) class. I did **not** close the lemma and I
found **no** selected-chart counterexample to the dimension-free contract. What
I add over w35/w36 is an independent reformulation that (i) localizes the entire
difficulty to a single scalar inequality in the *selected* chart, (ii) proves a
clean **\(C=3\) bound in that chart conditional on one harmonic sign-budget
inequality**, and (iii) pins, with exact arithmetic, *why the argmin selection
is irreducibly load-bearing* — the same wall as w36, now sharpened.

```
Calibration:
P(this PARTIAL verdict survives hostile audit)               = 0.88
P(the selected-chart SF bound is true at delta_0=1/4, C<=3)  = 0.66
P(the harmonic sign-budget (SB) below is provable)           = 0.30
P(C=1 for the selected chart)                                = 0.02  (refuted, w36)
P(a single-swap / pointwise argument can close it)           = 0.02  (refuted here)
```

All claims below are checked **exactly (sympy rationals)** on the mandatory
families (transverse pair \(a=1/4\); dense pair \(k=7\); staircase \(m=2,3\);
PERTURBED staircase \(m=5,\ \varepsilon=10^{-3}\)) and the genuine **no-center
path \(C\sim2\) family** rebuilt by HiGHS LP at \(k=6,\dots,40\). Scripts and
outputs are in this directory:
`harness.py`, `charge_lp.py`/`.json`, `nocenter_lp.py`, `nocenter_exact.py`.

---

## 0. Notation (matches the registry)

\(P=LB\), \(BL=I_k\). Rows of \(L\): coefficient vectors \(a(j)\in\mathbb R^k\),
\(\sum_t a_t(j)=1\). Rows of \(B\): representatives \(r_s=p_{u_s}\). Write
\(\beta_s(j):=B_{sj}=P_{u_sj}\). Harmonicity \(Pa_t=a_t\) is, dually,
\[
\sum_j \beta_s(j)\,a_t(j)=\delta_{st}\qquad(\text{all }s,t).
\tag{HARM}
\]
Row negativity \(\nu_i:=\sum_\ell(-P_{i\ell})_+\le\delta\); in particular
\(\nu_{u_s}=\sum_j(-\beta_s(j))_+\le\delta\), so \(\beta_s\) is a signed mass-1
measure with negative mass \(\le\delta\), positive mass \(1+\nu_{u_s}\le1+\delta\).
\[
\lambda_s(j)=1-a_s(j),\quad
\mu_s(j)=\sum_{t\ne s}(-a_t(j))_+,\quad
\sigma_s(j)=\sum_{t\ne s}(a_t(j))_+,\quad
E_s(j)=(\mu_s(j)-\lambda_s(j))_+ .
\]
\(\mathrm{SF}_s=\sum_j(\beta_s(j))_+E_s(j)\), \(\Phi=\max_s\mathrm{SF}_s\), and
\(U_*=\arg\min_{\mathcal M_\theta}\Phi\) over the \(\theta=1/2\) volume class
(Cramér gives \(|a_t(j)|\le 1/\theta=2\) there).

---

## 1. The excess reformulation (exact, independent of w35/w36)

Since \(\sum_t a_t(j)=1\), for every \(j\) and every \(s\):
\[
\sigma_s(j)=\mu_s(j)+\sum_{t\ne s}a_t(j)=\mu_s(j)+\lambda_s(j),
\qquad\text{i.e. } \mu_s(j)=\sigma_s(j)-\lambda_s(j).
\]
Therefore
\[
\boxed{\;E_s(j)=(\mu_s(j)-\lambda_s(j))_+=\bigl(\sigma_s(j)-2\lambda_s(j)\bigr)_+\;}
\tag{R}
\]
where \(\sigma_s(j)=\sum_{t\ne s}(a_t(j))_+\ge0\) is the **positive transverse
mass**. The excess is active **iff the positive off-pivot mass exceeds twice the
pivot deficit**, \(\sigma_s(j)>2(1-a_s(j))\). *(Verified exactly on all fast
families: `reformulation_ok=True`.)*

(R) is the clean object: it is sign-robust (no use of \(\lambda_s\ge0\), which
**fails** at \(\theta=1/2\) — trap (c)), and it exposes that the excess is a
*positive-mass* phenomenon offset by the deficit.

---

## 2. The harmonic deficit identity and the \(C=3\) reduction

Summing (HARM) over \(t\ne s\) and using \(\sum_{t\ne s}a_t(j)=\lambda_s(j)\):
\[
\sum_j\beta_s(j)\,\lambda_s(j)=\sum_{t\ne s}\sum_j\beta_s(j)a_t(j)
=\sum_{t\ne s}\delta_{st}=0 .
\tag{DEF}
\]
*(Verified exactly: `I1(deficit=0):True` on every family, including perturbed.)*

From (R), \(E_s(j)\le\sigma_s(j)\) pointwise, hence
\[
\mathrm{SF}_s\le S^+_s:=\sum_j(\beta_s(j))_+\sigma_s(j)
=\sum_{t\ne s}\sum_j(\beta_s(j))_+(a_t(j))_+ .
\tag{SIG}
\]
**Empirical law (the calibration target).** In the *selected* chart \(U_*\),
\[
S^+_s\le 3\,\delta\qquad\text{for every }s,
\tag{C3}
\]
holds **exactly** on every mandatory family (selected-chart value \(=2\delta\) on
all of them; \(\le3\delta\) is the envelope). On the genuine no-center path
family it is \(\frac{5}{2}\delta,\frac{8}{3}\delta,\dots\to3\delta\) (selected
chart). Combining (SIG)+(C3) gives the contract \(\mathrm{SF}_s\le3\delta\), i.e.
\(\Phi(U_*)\le 3\,\delta(P)\), a **dimension-free \(C(\delta_0)=3\)** — *if* (C3)
is proved.

So the **entire** open problem is now the single scalar display (C3) in the
selected chart. This is strictly cleaner than (CHARGE)/(TREE): it has no shear
tree, no per-generation product, and no charge weights to construct.

---

## 3. Why selection is irreducible (the sharpened wall)

(C3) is **false over the whole \(\theta=1/2\) class**; it holds only at the
argmin \(U_*\). Exact witness (perturbed staircase \(m=5,\varepsilon=10^{-3}\)):
the identity chart \([0,1,\dots,10]\) is in the \(\theta=1/2\) class and there
\(S^+_0=5.001\,\delta=m\,\delta\) — **growing with rank**. The selected chart
\([1,\dots,11]\) instead has \(S^+_s=2\delta\). (`nocenter`/`charge_lp` runs.)

Consequently **(C3) cannot follow from (HARM)+(DEF)+Cramér alone**; any proof
must invoke the argmin minimality of \(U_*\). This kills three tempting routes,
each **refuted here exactly**:

* **Pointwise (ME).** \(\max_j E_s(j)\le C'\delta\) is FALSE: staircase \(m=3\)
  has \(E=6\delta\), perturbed \(m=5\) has \(E=10\delta=2m\delta\) (one row, with
  compensating \(\beta_s\sim\delta/m\)). The bound is a *summed* cancellation,
  never pointwise.
* **\(\sigma\)-relaxation without selection.** §2's \(E\le\sigma\) is exactly
  tight in the path family but loses the deficit subtraction that the selection
  exploits; over the full class \(S^+_s\to m\delta\) (above). Dead end unless
  paired with the argmin.
* **Single-swap monotonicity.** From \(U_*\), the best in-class swap of the
  active pivot gives new \(\Phi/\delta=1\) (staircase \(m=3\), perturbed
  \(m=5\)) — **no contraction**. The selected chart sits *at* the floor
  \(\Phi\approx\delta\); single-swap stationarity certifies "cannot go lower",
  not "is low". This is trap (a) made exact, and it rules out angle (ii)'s
  one-swap variational inequality on its own.

---

## 4. The exact missing display (the reduced open)

What remains, in LaTeX, is the **harmonic sign-budget** at the argmin chart:

\[
\boxed{\;
\text{(SB)}\qquad
U_*\in\arg\min_{\mathcal M_{1/2}}\Phi
\;\Longrightarrow\;
\sum_j(\beta_s(j))_+\,\sigma_s(j)\;\le\;3\,\delta(P)\quad\forall s,
\;}
\]
equivalently, using (HARM) per coordinate \(t\ne s\)
\(\bigl(S^+_{s,t}-T_{s,t}=\sum_j(\beta_s)_-a_t(j)\), with
\(T_{s,t}=\sum_j(\beta_s)_+(-a_t)_+\bigr)\),
\[
\sum_{t\ne s}\Bigl[\,T_{s,t}+\textstyle\sum_j(\beta_s(j))_-\,a_t(j)\,\Bigr]\le 3\,\delta ,
\]
where the only available global handles are: row-budget
\(\nu_i\le\delta\); the deficit identity (DEF); the Cramér box \(|a_t(j)|\le2\);
and the **argmin minimality of \(U_*\) over \(\mathcal M_{1/2}\)** — which §3
proves is *not optional*. The honest gap is identical in spirit to w36's
(DECAY)/(TREE), but recast as a single positive-mass inequality with the
selection as the only nonlinear ingredient; the shear tree has been replaced by
the requirement that the argmin certificate beat the rank-growing identity
chart.

I was not able to convert the argmin minimality into (SB). LP-dual probing of
small selected instances (angle iii) reproduced \(S^+=2\delta\) but the dual
weights it returns are the trivial "all charge on one saturated row"
assignment (w36/B5's tautology), giving no generalizable pattern without
encoding the combinatorial selection constraints, which I did not complete.

---

## 5. What is banked vs. open

**Banked (exact, audit-ready):**
1. (R) \(E_s(j)=(\sigma_s(j)-2\lambda_s(j))_+\) — sign-robust at \(\theta=1/2\).
2. (DEF) \(\sum_j\beta_s\lambda_s=0\) — the harmonic deficit identity.
3. The reduction **(SIG)+(SB) \(\Rightarrow\) \(\Phi(U_*)\le3\delta\)**: the
   lemma now needs only the single scalar display (SB), no charge weights.
4. The **irreducibility of selection**: (SB) is false over the full class
   (perturbed staircase, \(S^+\to m\delta\)); pointwise, \(\sigma\)-only, and
   single-swap routes are each refuted by exact witnesses.
5. Note \(\mathrm{SF}_s\le M_s\) (w35 §2) is **FALSE at \(\theta=1/2\)**
   (perturbed \(m=5\)): when \(a_s>1\), \(E_s=\mu_s+|\lambda_s|>\mu_s\). Use (R)
   / (SIG) instead — this corrects a \(\theta=1\)-only step for the theta=1/2
   campaign.

**Open:** (SB) — the harmonic sign-budget at the argmin chart. Proving it gives
\(C(\delta_0)=3\) (calibration true value \(\approx2\); the slack is the
\(E\le\sigma\) relaxation in (SIG), recoverable to \(2\) only with the deficit
subtraction, which again needs the selection).

## 6. Verdict

\[
\boxed{\text{PARTIAL: SF/(CHARGE) not proved; no selected-chart counterexample.
The open is reduced to the single display (SB), with selection proven irreducible.}}
\]
