# w19_tangent — TANGENT-CONE LEMMA PROVED (claimed): dot-H+ <= 2 * dot-delta, C = 2 dimension-free (codex, 2026-06-11) [pending w19_tangent_audit]
# Brief: /tmp/codex-sigma-wall/w19_tangent/brief.md. Artifacts: experiments/out/w19_tangent/ (incl. the FULL PROOF NOTE recovered_proof.md — recovered from the transcript after the -o capture overwrote the worker's answer.md; orchestration lesson logged).

VERDICT: LEMMA PROVED.

I saved the full proof and numerics here:

- [answer.md](/tmp/codex-sigma-wall/w19_tangent/answer.md)
- [tangent_cone_decider.py](/tmp/codex-sigma-wall/w19_tangent/tangent_cone_decider.py)
- [out_large/tangent_decider_summary.txt](/tmp/codex-sigma-wall/w19_tangent/out_large/tangent_decider_summary.txt)
- [progress.md](/tmp/codex-sigma-wall/w19_tangent/progress.md)

Main result:

\[
\dot H^+_{P_0}(A)\le 2\,\dot\delta_{P_0}(A)
\]

for every H-M normal-form point and tangent direction \(P_0A+AP_0=A,\ A\mathbf1=0\). The constant \(C=2\) is dimension-free and has no dependence on partition size or minimum recurrent-block mass. It is sharp for the recurrent-hull normal derivative; the actual visible-set height can be smaller when new row vertices become visible.

Numerics: the LP decider found no \(\dot\delta=0\) counterexample direction. Large run summary: `246` strata, `zero_budget_max = 0.0`, `counterexample_count = 0`, `budget1_max = 2.0`.

Verification: `python3 -m py_compile tangent_cone_decider.py` passed, and both decider runs completed with saved JSON/text outputs.

Remaining gap: this proves the first-order normal-cone lemma, not the full local law. The next step is the second-order/curve-selection upgrade through the exact idempotent chart and stratum-boundary handling. Calibration recorded in the note: \(P(\)local route works\()\approx0.74\), \(P(\)global all-strata-uniform version true\()\approx0.52\).
---
## THE FULL PROOF NOTE (recovered verbatim from the worker transcript)

# VERDICT: LEMMA PROVED

The first-order normal-cone form is true, with the dimension-free sharp
constant
\[
  C=2 .
\]
The proof is for the upper Dini derivative of the actual height along exact
\(C^1\) arcs in the row-stochastic idempotent variety.  Equivalently, it proves
the stronger frozen/recurrent-hull upper derivative; changes of the visible set
can only lower the first-order height, and recurrent-cluster visibility is
stable at the \(o(t)\) level needed below.

## Statement

Let \(P_0\) be an H-M stochastic idempotent with recurrent blocks
\(C_1,\ldots,C_k\), transient set \(T\), block laws \(\pi_s\) supported
positively on \(C_s\), and transient mixtures
\[
  p_i=\sum_{s=1}^k \alpha_{is}\pi_s,\qquad i\in T .
\]
For \(i\in C_s\), write \(\alpha_i=e_s\).  Let \(A\) be tangent to the
row-stochastic idempotent variety:
\[
  P_0A+AP_0=A,\qquad A\mathbf 1=0 .
\]
Define
\[
  \dot\delta_{P_0}(A)
  :=\max_i\sum_{j:P_{0,ij}=0}(-A_{ij})_+ .
\]
For any exact \(C^1\) arc \(P(t)\) with \(P(0)=P_0\), \(P'(0)=A\), define
\[
  \dot H^+_{P_0}(A)
  :=\limsup_{t\downarrow0}\frac{H(P(t))-H(P_0)}{t}
  =\limsup_{t\downarrow0}\frac{H(P(t))}{t}.
\]
Then
\[
  \boxed{\dot H^+_{P_0}(A)\le 2\,\dot\delta_{P_0}(A).}
\]
The constant is independent of \(n,k\), the partition, the transient mixtures,
and the minimum mass in the \(\pi_s\)'s.

## The \(n=3,k=2\) Model

In H-M form,
\[
P_0=
\begin{pmatrix}
1&0&0\\
0&1&0\\
a&b&0
\end{pmatrix}
=I-e_3(-a,-b,1),
\qquad a+b=1 ,
\]
which is \(P=I-uv^T\) with \(u=e_3\), \(v=(-a,-b,1)^T\),
\(v^Tu=1\), and \(v^T\mathbf1=0\).

Solving \(P_0A+AP_0=A\), \(A\mathbf1=0\), gives
\[
A_1=x(-a,-b,1),\qquad
A_2=y(-a,-b,1),
\]
and, with \(\theta=ax+by\),
\[
A_3=(r,-r-\theta,\theta).
\]
If \(a,b>0\), the transient row is in the relative interior of the visible
segment, so the first-order height is zero:
\[
  \dot H^+_{P_0}(A)=0 .
\]
If \(a=1,b=0\), row \(3\) sits on the first visible vertex.  The outward
coefficient toward the missing second block is
\[
  \gamma_2=A_{32}= -r-x ,
\]
so
\[
  \dot H^+_{P_0}(A)\le 2(-\gamma_2)_+
  =2(r+x)_+ .
\]
But the active zeros in row \(3\) are columns \(2,3\), hence
\[
  \dot\delta_{P_0}(A)\ge (-A_{32})_+=(r+x)_+ .
\]
Thus \(\dot H^+\le2\dot\delta\).  The case \(a=0,b=1\) is symmetric.
The endpoint examples attain the recurrent-hull upper derivative \(2\dot\delta\);
the actual height may be smaller because the lifted endpoint row can itself
become visible.

## General H-M Proof

For a row vector \(x\), define its block coefficient after applying \(P_0\):
\[
  \Gamma_s(x)
  :=\sum_{j\in C_s}x_j+\sum_{\ell\in T}x_\ell\alpha_{\ell s},
  \qquad
  xP_0=\sum_s\Gamma_s(x)\pi_s .
\]
Let
\[
  B_s:=\sum_{r\in C_s}\pi_s(r)A_r .
\]
Since \(\pi_sP_0=\pi_s\), averaging the tangent equation over block \(C_s\)
gives
\[
  B_sP_0=0 .
\]
For any row \(i\), with \(\alpha_i=e_s\) on recurrent rows and the H-M mixture
on transient rows, the row-wise tangent equation is therefore
\[
  A_i=\sum_s\alpha_{is}B_s+\sum_s\Gamma_s(A_i)\pi_s .
\tag{1}
\]
Let \(S_i=\{s:\alpha_{is}>0\}\).  The first term in (1) is an admissible
first-order motion of the recurrent hull at the base point \(p_i\).  The
second term is a coefficient displacement in the simplex spanned by the
\(\pi_s\)'s.  Because the supports \(C_s\) are disjoint and each \(\pi_s\) has
total mass \(1\),
\[
  \left\|\sum_s c_s\pi_s\right\|_1=\sum_s|c_s|.
\]
The tangent cone to the face \(\operatorname{conv}\{\pi_s:s\in S_i\}\) consists
of coefficient vectors \(\mu\) with
\[
  \sum_s\mu_s=0,\qquad \mu_q\ge0\quad(q\notin S_i).
\]
Hence the row's first-order distance to the recurrent hull is
\[
  D_i(A)
  =2\sum_{q\notin S_i}(-\Gamma_q(A_i))_+ .
\tag{2}
\]
This is the elementary \(\ell^1\) distance from a zero-sum coefficient vector
to a simplex face tangent cone: zero the forbidden negative coefficients and
rebalance the same total mass inside the face.

It remains to compare the forbidden coefficient mass with active-zero
negative mass.  For \(q\notin S_i\), the columns \(C_q\) are active zeros in
row \(i\), and every transient column is also an active zero.  Moreover
\[
  \Gamma_q(A_i)
  =\sum_{j:P_{0,ij}=0} w_{jq}A_{ij},
\]
where
\[
  w_{jq}=
  \begin{cases}
  1, & j\in C_q,\\
  \alpha_{jq}, & j\in T,\\
  0, & \text{otherwise}.
  \end{cases}
\]
For each active column \(j\),
\[
  \sum_{q\notin S_i}w_{jq}\le1 .
\]
Therefore, by subadditivity of negative part,
\[
\begin{aligned}
  \sum_{q\notin S_i}(-\Gamma_q(A_i))_+
  &\le
  \sum_{q\notin S_i}\sum_{j:P_{0,ij}=0}w_{jq}(-A_{ij})_+\\
  &\le
  \sum_{j:P_{0,ij}=0}(-A_{ij})_+\\
  &\le \dot\delta_{P_0}(A).
\end{aligned}
\tag{3}
\]
Combining (2) and (3) gives
\[
  D_i(A)\le2\dot\delta_{P_0}(A)
  \qquad\text{for every row }i .
\]
Taking the maximum over rows gives
\[
  \dot H^+_{P_0}(A)\le\max_iD_i(A)\le2\dot\delta_{P_0}(A).
\]

The visible-set point is as follows.  Along any exact \(C^1\) arc through
\(P_0\), the recurrent clusters remain separated from one another by
\(\ell^1\)-distance \(2+O(t)\), while each cluster has diameter \(O(t)\).
Row vertices in those clusters that matter to first order are
\((\rho,\kappa)\)-visible after the standard local exposing rescaling; vertices
that fail visibility lie \(o(t)\) inside the recurrent-cluster hull.  Additional
visible vertices can only enlarge the visible hull.  Thus the actual upper
Dini derivative of \(H\) is bounded by the recurrent-hull derivative
\(\max_iD_i(A)\) used above.

## Numerical Decider

Artifacts:

- `tangent_cone_decider.py`
- `out/tangent_decider_summary.json`
- `out/tangent_decider_summary.txt`
- `out_large/tangent_decider_summary.json`
- `out_large/tangent_decider_summary.txt`

The LP decider samples H-M strata, solves the exact tangent equations, and
maximizes the recurrent-hull upper derivative \(D(A)\) under
\(\dot\delta(A)\le1\), \(\|A\|_\infty\le1\).  It separately checks the dangerous
cone \(\dot\delta(A)=0\).

Large run:

```text
samples_total: 246
zero_budget_max: 0.0
counterexample_count: 0
budget1_min: 0.0
budget1_median: 0.0
budget1_mean: 0.975609756097561
