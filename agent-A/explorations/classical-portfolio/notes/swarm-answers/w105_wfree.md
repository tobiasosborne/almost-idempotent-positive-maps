Note: `t4_extremal.md` and `t10_birkhoff.md` are not present under `notes/swarm-answers/`; their Wave 10 substance is in [wave5-sigma-wall-parallel.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave5-sigma-wall-parallel.md:703).

**Recommended Formulation**

Use Baake–Sumner normal-form distance. For an exact signed affine retraction
\[
P{\bf 1}={\bf 1},\qquad P^2=P,\qquad 
\nu(P):=\max_i\sum_j(-P_{ij})_+\le \delta,
\]
define
\[
D_{\mathrm{BS}}(P):=
\inf_{E\in\mathcal E_n}\|P-E\|_{\infty\to\infty},
\]
where \(\mathcal E_n=\{E\ge0,\ E{\bf 1}={\bf 1},\ E^2=E\}\), equivalently the Baake–Sumner normal-form idempotents:
\[
[n]=Z\dot\cup K_1\dot\cup\cdots\dot\cup K_r,\quad
E_i=
\begin{cases}
a^{(s)},&i\in K_s,\\
\sum_s\lambda_{is}a^{(s)},&i\in Z,
\end{cases}
\]
with \(a^{(s)}\in\Delta(K_s)\), \(\lambda_i\in\Delta_r\), and zero mass on \(Z\).

The W-free open core should be:
\[
\boxed{\quad D_{\mathrm{BS}}(P)\le C\sqrt{\nu(P)}\quad}
\]
with universal \(C,\delta_0\), independent of \(n\).

With the repo’s canonical notation, a full-distance \(C\delta\) statement is false: [ex-hume.md](/home/tobias/Projects/almost-idempotent-positive-maps/argument/lemmas/ex-hume.md:4) gives distance \(2\sqrt\delta+O(\delta)\). The observed linear law is about the old height \(H\), not full matrix distance.

**Equivalence/Losses**

Let the current W-form be:
\[
H_{\rho,\kappa}(P):=\max_i d_1(p_i,\operatorname{conv}W_{\rho,\kappa}(P))\le \gamma.
\]

1. Current W-form \(\Rightarrow D_{\mathrm{BS}}\):
By `thm-cluster`,
\[
D_{\mathrm{BS}}(P)\le C(\rho+\gamma+\delta/\kappa+\delta).
\]
Thus \(\rho,\gamma=O(\sqrt\delta)\), \(\kappa\gtrsim\sqrt\delta\) gives \(D_{\mathrm{BS}}(P)=O(\sqrt\delta)\).

2. \(D_{\mathrm{BS}}\Rightarrow\) current W-form:
Assume \(D_{\mathrm{BS}}(P)\le\varepsilon\), and take a nearest Baake–Sumner \(E\). For each recurrent block \(K_s\), choose a row-polytope vertex \(v_s\) minimizing
\[
\ell_s(x)=1-\sum_{j\in K_s}x_j.
\]
Then \(\|v_s-a^{(s)}\|_1\le 5\varepsilon\). If a row \(p_j\) satisfies \(\|p_j-v_s\|_1\ge\rho\), comparison with the exact row \(E_j=\sum_t\lambda_{jt}a^{(t)}\) gives
\[
\ell_s(p_j)-\ell_s(v_s)\ge \rho/2-5\varepsilon.
\]
So for \(\rho\ge20\varepsilon\), after normalizing \(\ell_s-\ell_s(v_s)\), \(v_s\) is \((\rho,\rho/8)\)-exposed. Also every row \(p_j\) is within
\[
\varepsilon+5\varepsilon=6\varepsilon
\]
of \(\operatorname{conv}\{v_s\}\). Hence
\[
H_{\rho,\rho/8}(P)\le6\varepsilon.
\]
So the W-form and Baake–Sumner distance are equivalent at the \(\sqrt\delta\) scale, with explicit constant loss.

**Candidate Audit**

(a) Normal-form distance: recommended, but with \(C\sqrt\delta\), not \(C\delta\). Makes Birkhoff natural because the finisher proves local equal-input collapse, exactly a local Baake–Sumner block.

(b) Equal-input defect: same object in coordinates. The partition search is not a hiddenness LP; it is the Baake–Sumner structural quantifier. This is the best working formulation.

(c) Spectral/\(\Gamma=P(g^2)-g^2\): W-free and useful, but not equivalent. Exact stochastic idempotents may have nonzero transient \(\Gamma\), so \(\Gamma\)-smallness is the wrong invariant unless it is augmented back into Baake–Sumner block data.

(d) Fixed-point geometry: one-way only. Normal-form distance controls the fixed simplex, but the fixed simplex alone loses the projection/row-coordinate data needed for transient proportionality.

**Why It Escapes**

The disappeared quantifier is: “choose a hidden vertex and an exposing/failed-exposing dual witness.” The new quantifier is only over exact Baake–Sumner partitions/idempotents. No normal cone of hiddenness appears.

\(P(\)equivalent to current W-form at the sharp \(\sqrt\delta\) scale\()\): **0.90**.  
\(P(\)strictly easier to attack than the hiddenness formulation\()\): **0.68**.