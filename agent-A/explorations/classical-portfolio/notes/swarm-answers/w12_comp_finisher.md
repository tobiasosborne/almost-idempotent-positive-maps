**VERDICT**
PARTIAL. The support-component finisher is proved with explicit constants for every primitive component whose positive path-products beat the signed/idempotence error. What survives is exactly the long-thin support class:

\[
\Pi_C \le E_L(\delta,\zeta)+{2(1+\delta)\varepsilon\over r_*-4\delta},
\]

where \(\Pi_C\) is the minimum best path-product across the component, \(L\) is directed diameter, \(r_*=0.85\tau\) for the audited F-ND consumer, and \(\tau=\sqrt\delta\). If edges have floor \(a\), this survivor is \(a^L \lesssim C\tau+O(L\delta)\). No dimension-free closure follows without ruling out those chains.

**Proof Sketch**
Use row \(\ell^1\) norm. In the d14 frame, positive leakage from the band is zero, so for \(B=P_{SS}=A-N\), \(A=B^+\), \(N=B^-\),

\[
\|N\|\le\delta,\qquad \|A\|\le1+\delta,\qquad \|B\|\le1+2\delta.
\]

Since \(P^2=P\) and \(P^+_{S,S^c}=0\),

\[
\zeta:=\|B^2-B\|\le \delta(1+2\delta).
\]

Normalize each positive component row: \(K_C=D^{-1}A_C\), \(D_{ii}=\sum_{j\in C}A_{ij}\in[1,1+\delta]\). Then

\[
\|K_C^2-K_C\|\le \varepsilon:=\zeta+6\delta+4\delta^2
\le 7\delta+6\delta^2.
\]

For a positive path \(\gamma:i\to j\) of length \(\ell\) and product \(\pi(\gamma)\),

\[
B_{ij}\ge
\pi(\gamma)
-\ell\delta(1+2\delta)^{\ell-1}
-\zeta\sum_{r=0}^{\ell-2}(1+2\delta)^r.
\]

Thus if

\[
\theta_C:=\min_{i,j\in C}\max_{\gamma:i\to j}
\left[
\pi(\gamma)-\ell(\gamma)\delta(1+2\delta)^{\ell(\gamma)-1}
-\zeta\sum_{r=0}^{\ell(\gamma)-2}(1+2\delta)^r
\right] >0,
\]

then every entry of \(A_C\) is at least \(\theta_C\), and every entry of \(K_C\) is at least

\[
\beta_C={\theta_C\over 1+\delta}.
\]

So the Hilbert diameter is finite:

\[
\Delta_C\le 2\log(1/\beta_C),\qquad
1-q_C\ge {2\beta_C\over1+\beta_C}.
\]

The t10 collapse lemma gives

\[
\operatorname{diam}_1\{K_{C,i}\}
\le {2\varepsilon\over1-q_C}
\le {2(1+\delta)\varepsilon\over \theta_C}.
\]

Returning to signed rows costs at most \(4\delta\):

\[
\operatorname{diam}_1\{p_i:i\in C\}
\le R_C:={2(1+\delta)\varepsilon\over\theta_C}+4\delta.
\]

If \(R_C<0.85\tau\), the audited F-ND / near-coincidence consumer forces the collapsed equal-input cluster into \(W\). If using only the original t10 exposure consumer, replace \(0.85\tau\) by \(\rho=4\tau\).

**Assembly**
Positive coupling between distinct \(B^+\)-components is zero by definition. The d14 cross-band leakage is only negative and already budgeted by \(\delta\), so it only enters the constants above. Therefore every band component either collapses-and-exposes, hence cannot be a hidden shallow survivor, or satisfies the displayed long-thin inequality.

Periodic components are not closed dimension-free by this argument. Cesaro averaging over a period/exponent \(M\) gives the same conclusion with a worse threshold \(O(M\varepsilon/\bar\Pi_C)\); without a bound on \(M\) and averaged path-product, they join the same residual class.

**New Sub-Lemmas**
1. Positive-normalized defect: \(\|K_C^2-K_C\|\le\zeta+6\delta+4\delta^2\).
2. Path-product shortcut: indirect positive paths force direct \(B^+\)-entries once product exceeds signed/idempotence error.
3. Component diameter bound: \(\Delta_C\le2\log((1+\delta)/\theta_C)\).
4. Collapse radius: \(R_C\le2(1+\delta)\varepsilon/\theta_C+4\delta\).
5. Assembly dichotomy: collapse-and-expose or long-thin residual.

\(P(\text{linear law})\approx0.78\).  
\(P(\text{this survives audit})\approx0.84\).

No files changed; the workspace is read-only, so I did not write this into `notes/`.