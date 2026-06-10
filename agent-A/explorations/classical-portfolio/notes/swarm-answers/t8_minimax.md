**VERDICT: DIED-AT-BY-COLLAPSE.**

The minimax/meta-game route does not prove the linear law. Its native failure is that the adversary’s exact-instance space is not convex, and the proposed “lifted game on certificates” either becomes a trivial probability simplex over exact instances or collapses back to the fixed-instance exposedness LP dual frame.

For fixed \(n\), the exact row-stochastic idempotents already fail convexity:

\[
P^0=\begin{pmatrix}1&0\\0&1\end{pmatrix},\quad
P^1=\begin{pmatrix}1&0\\1&0\end{pmatrix},\quad
\bar P=\frac12(P^0+P^1)=\begin{pmatrix}1&0\\1/2&1/2\end{pmatrix},
\]

but

\[
\bar P^2-\bar P=
\begin{pmatrix}0&0\\1/4&-1/4\end{pmatrix}\ne0.
\]

So Sion/von Neumann cannot be applied to exact instances. If instead one averages lifted certificates,

\[
\bar P=\int P_\omega\,d\nu,\qquad \bar g=\int g_\omega\,d\nu,
\]

then the identities needed by the campaign do not descend:

\[
\bar P\bar g-\bar g
=
\iint P_\omega g_{\omega'}\,d\nu(\omega)d\nu(\omega')
-\int P_\omega g_\omega\,d\nu(\omega),
\]

with uncontrolled cross terms. Carrying the whole measure \(\nu\) avoids this, but then the adversary’s extreme mixed strategies are just Dirac masses at worst exact instances. That gives no reduction to corner-family extrema.

The only remaining convex game is the fixed-instance exposedness game

\[
t^*(v)=\max_h\min_{j\in F_v} \operatorname{margin}_h(j),
\]

whose minimax dual is exactly the old failed-exposedness witness \((\mu,\alpha,\beta)\). At that point the route has collapsed into the forbidden LP basin. The known death certificate applies:

\[
B_{\mathrm{pushed}}=\frac{B+N}{M_F},\qquad
B_{\mathrm{pushed}}\le B
\iff
M_F\ge 1+\frac NB,
\]

but \(M_F\le1+N\), \(B<\kappa<1\), and any \(N>0\) makes this impossible.

**New Objects / Sub-Lemmas**

1. Exact-idempotent nonconvexity lemma: mixtures of exact idempotents need not be idempotent, even at \(\delta=0\).
2. Lifted-certificate cross-term obstruction: averaged \((P,g)\) generally loses \(g=Pg\).
3. Dirac adversary lemma: a mixed adversary over exact instances gives no nontrivial extremal-instance reduction unless additional moment constraints are imposed.
4. Missing theorem made explicit:

\[
x\in \operatorname{Ext}\overline{\operatorname{co}}(\mathcal C_{\mathrm{bad}})
\Longrightarrow H(x)\le C\delta(x),
\]

but this is essentially the desired linear law, not a consequence of minimax.

**Calibration**

\(P(\)linear law true\()\): 0.76, driven by d13 and the absence of verified high webs.

\(P(\)this minimax death certificate survives audit\()\): 0.84.

\(P(\)this minimax route can be repaired without a new signed quantitative Baake-Sumner stability theorem\()\): 0.08.

What minimax sees that the LP frame does not: the real obstruction is not just an optimal-witness support problem. It is the absence of a legitimate convex adversary space compatible with \(P^2=P\), \(g=Pg\), and the jumping \(W\)-geometry. Any useful “meta-dual” must first prove a rounding/stability theorem from convexified or tangent certificates back to exact signed idempotents; without that, minimax either says nothing or re-enters the exposedness LP dual frame.