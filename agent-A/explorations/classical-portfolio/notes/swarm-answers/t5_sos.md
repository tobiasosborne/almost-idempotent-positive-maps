VERDICT: **DIED-AT-BY-COLLAPSE**

The SOS route can honestly formulate the problem only after stratifying the exposedness geometry. On each fixed stratum it collapses to the same exposedness-dual obstruction: the quadratic module has the C10 exchange and the block boundary identities, but no generator that turns a shallow optimal LP witness into either deep mass or approximate \(P\)-closure.

**Smallest Honest Semialgebraic Encoding**

Introduce \(\tau\ge0\), \(\delta=\tau^2\), \(\rho=4\tau\), \(\kappa=\tau/4\). For each fixed combinatorial stratum choose:

- sign patterns for row entries and \(\ell^1\) distances;
- far sets \(F_i=\{j:\|p_j-p_i\|_1\ge\rho\}\);
- row-vertex/nonvertex status;
- the exact exposed set \(W\);
- outside-\(C_W\) carrier set for \(\widetilde\sigma_v\).

The polynomial constraints are then:

\[
P\mathbf 1=\mathbf 1,\qquad P^2=P,\qquad
P_{ij}=P^+_{ij}-P^-_{ij},\quad P^\pm_{ij}\ge0,\quad
\sum_jP^-_{ij}\le\tau^2 .
\]

For \(w\in W\), include an exposedness certificate \(h^w\):

\[
0\le h^w(p_i)\le1,\qquad h^w(p_w)=0,\qquad
h^w(p_j)\ge\kappa\quad(j\in F_w).
\]

For a hidden row vertex \(x\notin W\), encode non-exposedness by the LP dual witness:

\[
\sum_{j\in F_x}\mu_jp_j+\sum_k\alpha_kp_k
=
\sum_k\beta_kp_k+(1+A-B)p_x,
\qquad
\sum_{j\in F_x}\mu_j=1,\quad A=\sum\alpha_k,\quad B=\sum\beta_k<\kappa .
\]

For the hidden top vertex \(v\), use the canonical separator/deficit:

\[
g_i=H-\phi(p_i),\qquad g_v=0,\qquad g_i\ge0,\qquad Pg=g,\qquad
\phi\le0\text{ on }C_W .
\]

This is honest but not small uniformly in \(n\): exact \(W\) is a union over exponentially many strata. If \(W\) is relaxed to a chosen subset, the encoding is unsound because \(H\) can be artificially inflated. The s5 exact \(5\times5\) all-shallow construction is the sanity check: shallow optimal witnesses with \(\widetilde\sigma_v>0\) are real at \(H=O(\delta)\), so the encoding must include the height condition, not ban shallowness outright.

**n=3 / n=4 Search**

For \(n=3\), the certificate is degenerate. The row polytope is a point, segment, or simplex. Every row vertex is \((\rho,\kappa)\)-exposed for small \(\delta\): along a segment/simplex barycentric exposer,

\[
h(p_j)\ge \frac{\rho}{2+4\delta}=\frac{4\tau}{2+4\delta}>\frac{\tau}{4}=\kappa .
\]

Thus \(W\) contains every row vertex and \(H=0\). This is a Farkas/SOS certificate before any serious use of \(P^2=P\).

For \(n=4\), after eliminating simplex strata, the only nontrivial case is a planar quadrilateral/hidden-pair stratum. Modulo \(P^2=P\), the degree-2 ansatz yields only the known exchange

\[
\sum_{j\in F_v}\mu_jg_j+\sum_i\alpha_i g_i
=
\sum_i\beta_i g_i
\le \kappa\Omega_g,
\]

and block identities such as

\[
A^2-A=-BC,\qquad A=P_{SS}.
\]

For a hidden pair \(S=\{a,b\}\), this gives the spectral tax

\[
2P_{ab}P_{ba}
\le
P_{aa}(1-P_{aa})+P_{bb}(1-P_{bb})+4\delta(1+\delta),
\]

which only kills direct large two-site carrying. It does not relate the LP witness measure \(\mu\) to the row-coefficient block \(P_{SS}\). The missing SOS generator would have to prove something like

\[
\mu\text{-closed shallow web}
\Longrightarrow
\sum_{x\in C}\pi_x P^+_{x,C^c}\ll1
\quad\text{or}\quad
\|P_{CC}^2-P_{CC}\|\ll1,
\]

but that is exactly the known quantitative Baake-Sumner / \(\mu\)-to-\(P\) closure gap.

**Death Point**

The attempted Positivstellensatz certificate would need

\[
\tau^2-cH\in I(P^2-P,P\mathbf1-\mathbf1,Pg-g,\ldots)
+\mathrm{QM}(\text{stratum inequalities}).
\]

After quotienting by the idempotence ideal, the only available height-pricing identity is

\[
\sum\mu g+\sum\alpha g\le \kappa\Omega_g .
\]

To get \(\tau^2\ge cH\), SOS still needs a lower bound

\[
m(H-E)\le \sum_j\mu_j g_j,
\]

or an approximate \(P\)-closed top-band block. That is precisely the exposedness-LP/DMF basin. Native SOS machinery could not create the missing generator; it merely made clear that it is absent from the current polynomial ideal.

**New Objects**

1. Exact-W semialgebraic stratum \(\mathcal S_{\mathfrak s}\).
2. \(n=3\) simplex-exposure certificate: \(H=0\).
3. Degree-2 quotient-collapse lemma: idempotence reduces to C10 exchange plus block boundary equations.
4. SOS missing-generator formulation: prove \(\mu\)-closure \(\Rightarrow P\)-closure, or no certificate pattern emerges.

Calibration: \(P(\text{linear law true})=0.74\).  
\(P(\text{this SOS post-mortem survives audit})=0.80\).

What SOS sees that the LP frame does not: the LP frame sees uncontrolled \(\alpha\)-mass; SOS sees that this is not just a bad choice of witness. It is a missing polynomial generator in the quadratic module after exact \(W\)-stratification. A proof needs a new semialgebraic certificate for signed quantitative Baake-Sumner stability, not another manipulation of the existing exposedness dual.