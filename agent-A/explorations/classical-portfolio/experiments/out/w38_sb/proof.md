# VERDICT: REDUCTION REFUTED-AT-A3

The Opus reduction is not valid as stated.  The algebraic reformulation (R) and
the deficit identity (DEF) are correct, but the claimed (SIG) step

\[
E_s(j)\le \sigma_s(j),\qquad
\mathrm{SF}_s\le S^+_s:=\sum_j(\beta_s(j))_+\sigma_s(j)
\]

is false in the \(\theta=1/2\) class.  The failure occurs even in the selected
argmin chart of the mandatory perturbed staircase \(m=5,\epsilon=10^{-3}\).
Therefore proving the displayed (SB) would not prove the stated SF/registry
contract unless an additional term controlling negative pivot deficit is added.

Calibration:

\[
P(\text{(R) and (DEF) audit})=0.995,\qquad
P(\text{A3 refutation is fatal to the Opus reduction})=0.99,\qquad
P(\text{standalone SB true})=\text{not evaluated after refutation}.
\]

Artifacts produced locally:

* `verify_reduction.py`, `verify_reduction.out`, `verify_reduction.json`
* `single_swap_check.py`, `single_swap_check.out`, `single_swap_check.json`
* `progress.md`

No `answer.md` was created.

## A1. Exact relation among \(\mu,\sigma,\lambda,E\)

For fixed \(s\), write

\[
\lambda_s(j)=1-a_s(j)=\sum_{t\ne s}a_t(j),
\]

\[
\mu_s(j)=\sum_{t\ne s}(-a_t(j))_+,\qquad
\sigma_s(j)=\sum_{t\ne s}(a_t(j))_+ .
\]

Since the off-pivot sum is positive mass minus negative mass,

\[
\lambda_s(j)=\sigma_s(j)-\mu_s(j),
\qquad
\mu_s(j)=\sigma_s(j)-\lambda_s(j).
\]

Hence the registry excess is exactly

\[
E_s(j)=(\mu_s(j)-\lambda_s(j))_+
      =(\sigma_s(j)-2\lambda_s(j))_+ .
\tag{R}
\]

This is valid with no sign assumption.  The sign cases are:

* if \(\lambda\ge\sigma/2\), then \(E=0\);
* if \(0\le\lambda<\sigma/2\), then \(E=\sigma-2\lambda\le\sigma\);
* if \(\lambda<0\), then \(E=\sigma+2|\lambda|>\sigma\) unless
  \(\lambda=0\).

Thus (R) is sign-robust, but \(E\le\sigma\) is not.  Exact max-volume
\(\theta=1\) gives \(a_s(j)\le1\), hence \(\lambda\ge0\).  The required
\(\theta=1/2\) class only gives \(a_s(j)\le2\), so \(\lambda\) may be negative.

The w35 quantifier chain needs a direct selected-chart SF bound:

\[
\mathrm{SF}_s=\sum_j(\beta_s(j))_+E_s(j)\le C_{\rm sf}\delta.
\]

From such a direct SF bound the transverse tax step still survives.  Pointwise

\[
\mu_s(j)\le E_s(j)+\lambda_s(j),
\]

and (DEF) gives

\[
\sum_j(\beta_s(j))_+\lambda_s(j)
=-\sum_{\beta_s(j)<0}\beta_s(j)\lambda_s(j)
\le (1+A)\delta,\qquad A=\theta^{-1}.
\]

Therefore

\[
M_s:=\sum_j(\beta_s(j))_+\mu_s(j)
\le (C_{\rm sf}+1+A)\delta.
\]

For \(\theta=1/2\), this is \(C_\mu=C_{\rm sf}+3\).  What does not survive is
substituting the Opus \(S^+\) display for the SF bound.

The correct pointwise fallback from (R) is only

\[
E_s(j)\le \sigma_s(j)+2(-\lambda_s(j))_+,
\]

so a valid sign-budget reduction would need to control

\[
S^+_s+2\sum_j(\beta_s(j))_+(-\lambda_s(j))_+,
\]

or control \(\mathrm{SF}_s\) directly.

## A2. The w35 correction is confirmed

The mandatory perturbed staircase \(m=5,\epsilon=1/1000\) has
\(\delta=1/2\).  In the selected \(\theta=1/2\) chart

\[
U_*=[1,2,3,4,5,6,7,8,9,10,11],
\]

look at representative index \(s=10\), pivot row \(u_s=11\), and column \(j=0\).
The exact verifier gives

\[
\beta_s(j)=\frac{999}{1000000},\qquad
\lambda_s(j)=-\frac1{999},
\]

\[
\mu_s(j)=\frac{1667}{666},\qquad
\sigma_s(j)=\frac{4999}{1998},\qquad
E_s(j)=\frac{5003}{1998}.
\]

This row has

\[
\mathrm{SF}_s=\frac{5003}{2000000},
\qquad
M_s=\frac{5001}{2000000}.
\]

So \(\mathrm{SF}_s\le M_s\) is false by exactly \(1/1000000\).  This confirms
the Opus warning that the old \(SF\le M\) move is a \(\theta=1\)-only shortcut.

The downstream constants chain is not harmed if one assumes the direct registry
SF contract: as shown in A1, \(C_\mu=C_{\rm sf}+1+\theta^{-1}\).  But it is
not justified by \(S^+\le3\delta\) alone.

## A3. (DEF) is correct, but (SIG) is false

The harmonic deficit identity is correct:

\[
\sum_j\beta_s(j)\lambda_s(j)=0.
\tag{DEF}
\]

The verifier recomputed it exactly as zero for every selected representative in
the mandatory families it rebuilt:

* transverse pair \(a=1/4\);
* dense pair \(k=7\);
* staircase \(m=2,3\);
* perturbed staircase \(m=5,\epsilon=1/1000\).

The failed line is (SIG).  In the same selected perturbed chart and row as A2,
the exact row totals are

\[
\mathrm{SF}_s=\frac{5003}{2000000},
\qquad
S^+_s=\frac{5001}{2000000}.
\]

Thus

\[
\mathrm{SF}_s-S^+_s=\frac1{1000000}>0.
\]

At the pointwise term \(j=0\),

\[
E_s(j)-\sigma_s(j)=\frac{2}{999},
\]

with positive \(\beta_s(j)\).  The total row difference is partly offset by
other positive \(S^+\) terms with zero excess, but the row-level inequality
\(\mathrm{SF}_s\le S^+_s\) still fails.

Consequently the implication

\[
S^+_s\le3\delta\quad\Rightarrow\quad \mathrm{SF}_s\le3\delta
\]

has no proof from the displayed reduction.  In this concrete selected chart
both quantities are small, so this is not a counterexample to the final SF
bound.  It is a counterexample to the claimed reduction.

## A4. Irreducibility witness spot-checks

I spot-verified the single-swap obstruction exactly.  Starting from the selected
\(\theta=1/2\) chart, enumerate all legal one-row swaps that remain in the
\(\theta=1/2\) class:

```text
staircase_m3: star=[1, 2, 3, 4, 5, 6, 7] star_ratio=1
              swaps=14 best_swap_ratio=1 best_swap=[1, 2, 3, 4, 5, 6, 8]
perturbed_staircase_m5_eps1e-3:
              star=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] star_ratio=1
              swaps=17 best_swap_ratio=1 best_swap=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
```

So the single-swap route indeed provides no contraction on these witnesses.

The prior exact no-center checks read from w36 remain:

```text
path_no_center_k6_a1_100_mass1: delta=40/4001,
selected_ratio=59999/40000.

path_no_center_k8_a1_100_mass1: delta=300/30007,
selected_ratio=149999/90000.
```

The HiGHS float scan for the no-center path family climbs as previously
reported:

```text
k=6 selected=1.4999750000
k=8 selected=1.6666555556
k=10 selected=1.7499937500
k=12 selected=1.7999960000
k=20 selected=1.8888987654
k=40 selected=1.9473734071
```

These checks are consistent with the older calibration, but they do not repair
the (SIG) step.

## Part B status

I did not attempt to prove (SB) after A3, because the stated (SB)

\[
\sum_j(\beta_s(j))_+\sigma_s(j)\le3\delta
\]

does not imply the target SF bound in the \(\theta=1/2\) class.  The named gap
is therefore upstream of selection: the scalar display is missing the negative
deficit term created by \(a_s(j)>1\).

A corrected target would need one of the following forms:

\[
\sum_j(\beta_s(j))_+(\sigma_s(j)-2\lambda_s(j))_+\le C\delta,
\]

which is exactly the SF contract, or the more structured sufficient display

\[
\sum_j(\beta_s(j))_+\sigma_s(j)
+2\sum_j(\beta_s(j))_+(-\lambda_s(j))_+
\le C\delta.
\]

Only after adding that missing term would the argmin-selection problem be the
right remaining target.

Final verdict:

\[
\boxed{\text{REDUCTION REFUTED-AT-A3: (SIG) is false at }\theta=1/2.}
\]
