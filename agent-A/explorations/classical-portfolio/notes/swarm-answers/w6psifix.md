PROVED (conditioned). This proves the corrected `F-ψ` input, not the harder top-band localization/HZF condition itself.

**Statement**
Let \(P1=1\), \(P^2=P\), row negative mass \(\le \delta\), \(\tau=\sqrt\delta\), \(\rho=4\tau\), \(\kappa=\tau/4\). Let \(W\) be the \((\rho,\kappa)\)-well-exposed row vertices and \(C=\operatorname{conv}W\). Pick a hidden top row vertex \(v\) with
\[
H=\operatorname{dist}_1(p_v,C)>0,\qquad p_v\notin W.
\]
Let \(\phi\) be the canonical top separator:
\[
\|\phi\|_{\ell^1{}^\ast}\le 1,\quad \sup_C\phi=0,\quad \phi(p_v)=H,
\]
and set \(g_i=H-\phi(p_i)\).

For \(S\subset\{1,\dots,n\}\), write \(s_i=p_i(S)\). Let
\[
\psi_i=s_i+\tfrac12\phi(p_i),
\]
let \(v''\) be a row vertex maximizing \(\psi\), and set
\[
Z=\max_i\psi_i-\min_i\psi_i>0.
\]
Assume \(s_{v''}\ge 1-\kappa\). Define the canonical high-danger band by
\[
\mathcal Z_{\mathrm{hi}}=\{i:\|p_i-p_{v''}\|_1\ge\rho,\ g_i\le g_{v''}+2\kappa Z\}.
\]
Condition: every row in \(\mathcal Z_{\mathrm{hi}}\) is \(S\)-full, i.e. \(s_i\ge1-\kappa\).

Then every \(\rho\)-far non-\(S\)-full row \(q\) satisfies
\[
\psi_{v''}-\psi_q\ge \kappa Z.
\]
Equivalently, every \(\rho\)-far blocker for \(h_\psi=(\psi_{v''}-\psi)/Z\) with \(h_\psi(q)<\kappa\) is \(S\)-full.

Also, if \(s_v\ge1-\sigma_v\), then
\[
g_{v''}\le 2\sigma_v+2\delta.
\]

**Proof**
Assume \(q\) is \(\rho\)-far from \(v''\), non-\(S\)-full, and \(\psi_{v''}-\psi_q<\kappa Z\). Since \(s_{v''}\ge1-\kappa>s_q\),
\[
s_{v''}-s_q>0.
\]
Thus
\[
\tfrac12(\phi(p_{v''})-\phi(p_q))
=(\psi_{v''}-\psi_q)-(s_{v''}-s_q)<\kappa Z.
\]
So \(\phi(p_q)>\phi(p_{v''})-2\kappa Z\), equivalently
\[
g_q<g_{v''}+2\kappa Z.
\]
Hence \(q\in\mathcal Z_{\mathrm{hi}}\), contradicting the conditioning. Therefore the gap is at least \(\kappa Z\).

For the height bound, maximality of \(v''\) gives
\[
s_{v''}+\tfrac12\phi(p_{v''})\ge s_v+\tfrac12H,
\]
so
\[
g_{v''}=H-\phi(p_{v''})\le2(s_{v''}-s_v).
\]
Because row negative mass is \(\le\delta\), \(s_{v''}\le1+\delta\), and \(s_v\ge1-\sigma_v\). Hence \(g_{v''}\le2\sigma_v+2\delta\).

**Counterexample Checks**
Wave-5 ψ counterexample: excluded. Its selected \(v''=p_1\) is already well-exposed: \(h(x)=1-x_1\) has \(h(p_1)=0\) and far-row values \(1\ge\kappa\). Also \(\phi=x_3\) is not canonical after computing \(W\), since \(p_3\in W\) and \(\phi(p_3)=1\), contradicting \(\sup_C\phi=0\).

Wave-5 ψ2 counterexample: excluded. The offending \(q=p_6\) is itself well-exposed by the recorded exposer, with far-row values \(\ge2/5\gg\kappa=1/16\), so \(q\in W\). Therefore the attacked \(\phi=-2x_4\) is not canonical after computing \(W\): \(\phi(q)=1/8>0\), impossible under \(\sup_C\phi=0\).

**Consumer Fit**
This suffices for the `F-ψ` consumer: “the \(\psi=x(S)+\lambda\phi\) max-selection forces an S-full \(\rho\)-far blocker for \(v''\), with \(g(v'')\le2\sigma_v+O(\delta)\)” from [fable-hlc-attack.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/fable-hlc-attack.md:479). It gives exactly that, with \(O(\delta)=2\delta\).

What remains open is proving the high-danger-band/S-full condition from exactness; that is essentially the top-band localization residual.

Calibration: \(P(\)variant true\()=0.99\). \(P(\)survives audit as the correct conditioned `F-ψ` replacement\()=0.82\).