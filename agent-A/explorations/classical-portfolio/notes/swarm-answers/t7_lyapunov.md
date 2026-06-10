**VERDICT: DIED-AT**

Not DIED-AT-BY-COLLAPSE. I did not enter the exposedness-LP dual basin; the failure is native to the Lyapunov route.

Define the positive-part Markov kernel
\[
\nu_i=\sum_j(P_{ij})_-,\qquad K_{ij}=\frac{(P_{ij})_+}{1+\nu_i}.
\]
Then \(K\) is row-stochastic and exact idempotence of \(P\) gives the useful perturbative lemma
\[
\|K_i-P_i\|_1\le 2\delta,\qquad
\|K_iK-K_i\|_1\le (6+4\delta)\delta\le 7\delta
\quad(\delta\le1/4).
\]
So the signed web has a real internal Markov dynamics whose one-step Lyapunov drift is forced to be only \(O(\delta)\).

For a dangerous top vertex \(v\), set
\[
S=\{i:\ p_i\notin \operatorname{conv}W,\ g_i\le H/4\}.
\]
Since \(g_v=0\), \(g=Pg\), and \(0\le g\le R\le 2+4\delta\),
\[
K_v(S^c)\le P_v^+\{g>H/4\}\le \frac{4\delta R}{H}.
\]
Thus if \(H\gg\sqrt\delta\), the positive dynamics from \(v\) is almost trapped in the shallow hidden web.

The Lyapunov I tried is relative entropy or Hellinger entropy for the restricted carrier dynamics on \(S\):
\[
\Phi_\pi(\lambda)=D(\lambda\|\pi)
\quad\text{or}\quad
\Phi_\pi(\lambda)=H^2(\lambda,\pi),
\]
where \(\pi\) is stationary for an internal recurrent class. Markov data processing gives monotone decrease. Exactness gives near-conservation through \(\|K_vK-K_v\|_1=O(\delta)\). To close HLC, the missing inequality would have to be

\[
\boxed{
K_v(S^c)+\|K_vK-K_v\|_1 \ge c_0 H
}
\tag{Lyap-exit}
\]

or equivalently an entropy coercivity bound
\[
\boxed{
\Phi_\pi(K_v)-\Phi_\pi(K_vK)\ge c_1 H-C_1\delta.
}
\tag{Entropy-coercion}
\]

If (Lyap-exit) held, then
\[
c_0H\le 7\delta+\frac{4\delta R}{H},
\]
so for \(H\ge B\sqrt\delta\) and \(B\) large enough depending only on \(c_0\), contradiction. This would prove the stated no-high-shallow-web form.

It dies because I cannot prove (Lyap-exit). Entropy only sees internal mixing. A coherent almost-closed shallow class can have nearly stationary carrier rows, hence essentially zero entropy dissipation, while sitting at height \(H\) from \(\operatorname{conv}W\). Baake-Sumner’s \(\delta=0\) classification rules out the exact closed Markov version by forcing recurrent blocks to have equal positive rows [equal-fin.tex](/home/tobias/Projects/almost-idempotent-positive-maps/refs/baake-sumner-2007.11433/equal-fin.tex:1062), but the needed quantitative anchored version is precisely the open shallow-web stability theorem.

**New objects / lemmas**

1. Positive carrier kernel \(K=P^+/(1+\nu)\).
2. Positive-kernel defect lemma: \(\|K^2-K\|_{\infty\to\infty}\le7\delta\).
3. Conditional Lyapunov-exit criterion: (Lyap-exit) implies the high-shallow-web exclusion with explicit constants.
4. Death point: entropy coercion cannot be derived from Markov contraction alone; it needs quantitative Baake-Sumner anchoring.

Calibration: \(P(\text{linear law true})=0.72\). \(P(\text{this post-mortem survives audit})=0.80\). \(P(\text{Lyap-exit as stated is provable without extra geometry})=0.25\).

What this strategy sees that the LP frame cannot: it isolates the signed error cleanly as \(O(\delta)\) after passing to \(K\). The obstruction is therefore not “bad dual witness cleanup”; it is an almost-stationary hidden Markov class whose entropy has no reason to decrease unless one proves an anchored exit/coercivity theorem.