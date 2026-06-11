# w16_quotient — Conjecture 2' stated; BRIDGE SECURED; clone-invariance PROVED; died at anti-splitting (codex, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w16_quotient/brief.md

VERDICT: **BRIDGE SECURED + 2' OPEN**. Exact quotienting kills the w15 exact-clone obstruction, and the w12 finisher reattaches to closed quotient components. I did not prove the quotient floor: the attack dies at converting aggregate shallow/quotient path mass into a dimension-free best-path product. Progress logged in [progress.md](/tmp/codex-sigma-wall/w16_quotient/progress.md).

**Conjecture 2'**
```latex
Let \(i\sim j\) iff \(p_i=p_j\) as row vectors, and write
\(\alpha=[i]\).  For row classes \(\alpha,\beta\), define
\[
Q_{\alpha\beta}:=\sum_{b\in\beta}P_{ib}\qquad(i\in\alpha).
\]
This is well-defined because \(i,i'\in\alpha\) means \(P_{ib}=P_{i'b}\)
for every column \(b\).

For \(S'_t=\{\alpha:g_\alpha<t\}\), put a directed quotient carrier edge
\(\alpha\to\beta\) when \(Q_{\alpha\beta}>0\), and for a closed strongly
connected quotient component \(\mathcal C\subset S'_t\) define
\[
\Pi'_{\mathcal C}:=
\min_{\alpha,\beta\in\mathcal C}
\max_{\gamma:\alpha\to\beta\ {\rm in}\ \mathcal C}
\prod_{(u,w)\in\gamma}Q_{uw}.
\]

Conjecture \(2'\).  There exist universal constants
\(\delta_0,B,c,C'<\infty\) such that, if \(\delta(P)\le\delta_0\), \(v\) is
a hidden top vertex, \(\widetilde\sigma_v>\tau=\sqrt\delta\), and
\(H>B\tau\), then for some \(t\in[\kappa\Omega/2,\kappa\Omega]\), every
closed quotient carrier component \(\mathcal C\subset S'_t\) carrying
positive \(Q^+\)-mass from \([v]\) satisfies
\[
\Pi'_{\mathcal C}\ge c\,\tau-C' L(\mathcal C)\delta .
\]
```

Finisher-calibrated form: the bridge actually consumes
\[
\theta_{\mathcal C}:=
\min_{\alpha,\beta}\max_{\gamma:\alpha\to\beta}
\left[
\prod Q_e
-\ell(\gamma)\delta(1+2\delta)^{\ell(\gamma)-1}
-\zeta\sum_{r=0}^{\ell(\gamma)-2}(1+2\delta)^r
\right]
\]
with
\[
4\delta+\frac{2(1+\delta)\varepsilon}{\theta_{\mathcal C}}
<r_*=0.85\tau,\qquad
\varepsilon=\zeta+6\delta+4\delta^2.
\]
For example, if \(\delta_0\le10^{-4}\), then \(\theta_{\mathcal C}\ge20\tau\)
gives \(R_{\mathcal C}<0.85\tau\) dimension-free.

**Clone Invariance**
For a duplicate split
\[
\widehat P_{ab}=\alpha_bP_{\pi(a),\pi(b)},\qquad
\sum_{b\in\pi^{-1}(r)}\alpha_b=1,
\]
the quotient classes of \(\widehat P\) are canonically the original row
classes, and
\[
\widehat Q_{[a][c]}
=\sum_{\pi(b)\in[c]}\alpha_bP_{\pi(a),\pi(b)}
=\sum_{r\in[\pi(c)]}P_{\pi(a),r}
=Q_{[\pi(a)][\pi(c)]}.
\]
So quotient objects are isomorphic and have identical quotient weights. This neutralizes the exact w15 cloning obstruction.

Near-duplicate caveat: exact quotienting is not robust. If \(S\mathbf 1=\mathbf 1\) and \(P_\eta=S\widehat P S^{-1}\) with \(S=I+O(\eta)\), then \(P_\eta^2=P_\eta\), \(P_\eta\mathbf1=\mathbf1\), and duplicate rows can be split into an \(\eta\)-cloud while path weights remain \(O(1/M)+O(\eta)\). Thus a robust replacement should cluster rows at scale \(\eta_{\rm cl}\); the cost is
\[
\zeta\mapsto \zeta+O(\eta_{\rm cl}),\qquad
R_{\mathcal C}\mapsto
4\delta+O(\eta_{\rm cl})
+\frac{2(1+\delta)(\varepsilon+O(\eta_{\rm cl}))}{\theta_{\mathcal C}}.
\]
At the intended \(\theta_{\mathcal C}\asymp\tau\), this requires
\(\eta_{\rm cl}\lesssim \tau\theta_{\mathcal C}\asymp\delta\).

**Lumping Lemma**
```latex
Lemma.  The quotient \(Q\) satisfies
\[
Q\mathbf1=\mathbf1,\qquad Q^2=Q,\qquad \delta(Q)\le\delta(P).
\]
Moreover \(g_\alpha=g_i\) is \(Q\)-harmonic:
\[
g_\alpha=\sum_\beta Q_{\alpha\beta}g_\beta.
\]
If \(S_t\) is class-saturated and \(B=P_{S_tS_t}\), \(B'=Q_{S'_tS'_t}\),
then \(B'\) is the lumping of \(B\), positive band closure descends, and
\[
\|(B')^2-B'\|_{\infty\to\infty}\le \|B^2-B\|_{\infty\to\infty}.
\]
For a closed quotient positive component \(\mathcal C\), the w12 proof
applied to \(Q_{\mathcal C\mathcal C}\) gives
\[
\operatorname{diam}_1\{p_\alpha:\alpha\in\mathcal C\}
\le
4\delta+\frac{2(1+\delta)\varepsilon}{\theta_{\mathcal C}}.
\]
Since every original index in a class has row \(p_\alpha\), collapse on
classes is exactly collapse on the original indices.
```

**Died At**
The quotient H-M surrogate works:
\[
(Q^+)_{[v]}(S_t^c)\le \frac{\delta\Omega}{t},
\qquad
\widetilde\sigma'_{[v]}\ge \widetilde\sigma_v-\delta,
\]
so for \(t=\kappa\Omega\) and \(H>B\tau\),
\[
(Q^+)_{[v]}(S_t\setminus C_W)
\ge \left(\frac B3-5\right)\tau
\]
for small \(\delta\). Also \(Q^k=Q\), and
\[
Q_{\alpha\beta}\ge ((Q^+)^k)_{\alpha\beta}
-\big((1+2\delta)^k-(1+\delta)^k\big).
\]

The failed inequality is exactly
\[
\boxed{
\Pi'_{\mathcal C}
=
\min_{\alpha,\beta}
\max_{\gamma:\alpha\to\beta}
\prod_{e\in\gamma}Q_e
\ \ge\ c\tau-C'L\delta .
}
\]
Current identities control aggregate path sums, not a best individual path product. Total mass can still split over many nearly coincident quotient classes; scalar chain shadows remain false unless hiddenness/realization gives a new anti-splitting principle.

Calibrated probabilities:  
\[
P(2'\text{ true as exact quotient})\approx0.48,\qquad
P(2'\text{ provable in current campaign frame})\approx0.22.
\]
For the \(\eta_{\rm cl}\lesssim\delta\) clustered quotient variant, I would raise those to roughly \(0.66\) and \(0.38\).