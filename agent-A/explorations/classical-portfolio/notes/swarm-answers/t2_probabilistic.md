**1. VERDICT**

DIED-AT, with subroute (a) random exposer marked DIED-AT-BY-COLLAPSE.

The probabilistic coupling route gets a real new object, but dies at the carrier-to-blocker hitting probability:

\[
\boxed{
\theta_\mu
:= \sum_{b\in F_v}\mu_b\,(Q_vQ)_b
\ \stackrel{\text{needed}}{\ge}\ c\,\tau
}
\]

where \(Q\) is the positive Markovization of \(P\), \(F_v=\{b:\|p_b-p_v\|_1\ge\rho,\ g_b<\kappa\Omega_g\}\), and \(\mu\) is a far top-band blocker measure. What is actually available is only

\[
\big|(Q_vQ)(A)-Q_v(A)\big|\le 5\delta
\]

for every set \(A\). If \(Q_v(F_v)=0\), the probabilistic chain never sees the far blocker except at \(O(\delta)\) scale. Hiddenness gives a blocker exists; it does not give that the signed kernel feeds it.

**2. Native Probabilistic Post-Mortem**

Define row negative mass \(\nu_i=\sum_j P_{ij}^-\le\delta\) and the honest Markov kernel

\[
Q_{ij}=\frac{P_{ij}^+}{1+\nu_i}.
\]

For any \(f\) with \(\operatorname{osc}(f)\le1\),

\[
|(Q-P)f(i)|\le \nu_i\le\delta.
\]

Since \(P^2=P\), this gives approximate idempotence:

\[
\|(Q^2-Q)\|_{\mathrm{osc}\to\infty}\le 5\delta
\quad(\delta\le1/4).
\]

So the signed kernel becomes an almost-idempotent Markov chain. Starting at the hidden top vertex \(v\), the chain’s first step is almost entirely in the shallow non-\(W\) web:

\[
Q_v(\operatorname{conv}W)\le \frac{\delta\Omega_g}{H},
\qquad
Q_v\{g\ge\kappa\Omega_g\}\le \frac{\delta}{\kappa}=4\tau,
\]

hence

\[
Q_v(T_\kappa)\ge
1-\frac{\delta\Omega_g}{H}-4\tau,
\quad
T_\kappa:=\{p_j\notin\operatorname{conv}W,\ g_j<\kappa\Omega_g\}.
\]

Approximate idempotence then says the two-step chain also stays there:

\[
(Q_vQ)(T_\kappa)\ge
1-\frac{\delta\Omega_g}{H}-4\tau-5\delta.
\]

This proves a probabilistic formulation of the survivor: high hidden vertices generate an almost-closed shallow Markov web. At \(\delta=0\), Baake-Sumner kills this via the Markov idempotent normal form: recurrent blocks are closed with equal positive rows [equal-fin.tex](/home/tobias/Projects/almost-idempotent-positive-maps/refs/baake-sumner-2007.11433/equal-fin.tex:1060). But for \(\delta>0\), the coupling proof needs a quantitative return/minorization from that web to the far blocker set \(F_v\), and the current identities do not provide it.

Random exposer route collapsed as follows:

\[
\sup_{\mathcal D}\inf_{b\in F_v}
\mathbb E_{h\sim\mathcal D}\,[h(p_v)-h(p_b)]
=
\sup_h\inf_{\mu\in\Delta(F_v)}
\sum_b\mu_b[h(p_v)-h(p_b)].
\]

That is exactly the exposedness LP game. So route (a) is DIED-AT-BY-COLLAPSE under the anti-collapse rule.

**3. New Objects**

- Positive Markovization \(Q_{ij}=P_{ij}^+/(1+\nu_i)\).
- Approximate idempotence coupling: \(Q_i\) and \(Q_iQ\) can be coupled with failure probability \(\le5\delta\).
- Shallow quasi-stationary web \(T_\kappa\), carrying almost all of \(Q_v\) in the high branch.
- Missing probabilistic minorization \(\theta_\mu\ge c\tau\), the native coupling form of the open web-exclusion step.

**4. Calibration**

\[
P(\text{linear law true})=0.78.
\]

\[
P(\text{this DIED-AT diagnosis survives audit})=0.84.
\]

**5. What This Sees Beyond LP**

The probabilistic view separates two facts the LP frame blends together: the signed idempotent really does contain an almost-idempotent positive Markov chain, and a high hidden vertex really does generate an almost-closed shallow web. The blocker problem is not just “find a better exposing functional”; it is a missing hitting/minorization theorem saying that this quasi-stationary shallow web must probabilistically feed the far blocker that prevents exposure. Current LP duals see the blocker, while \(Q\)-coupling sees the recurrent web; the unsolved step is coupling those two objects.