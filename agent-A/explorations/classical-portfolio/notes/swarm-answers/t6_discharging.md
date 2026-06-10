**VERDICT: DIED-AT**

The discharging route gets a clean native invariant, but it does not force a forbidden local configuration.

Let
\[
N_i=\sum_j P^-_{ij}\le \delta,\qquad K_{ij}=\frac{P^+_{ij}}{1+N_i}.
\]
This is the positive-carrier Markov kernel. Since \(g=Pg\),
\[
(Kg)_i-g_i
=\frac{\sum_j P^-_{ij}(g_j-g_i)}{1+N_i},
\qquad |(Kg)_i-g_i|\le \delta\Omega_g.
\]
So \(g\) is an \(O(\delta)\)-harmonic charge for the carrier graph. Hence for \(L>0\),
\[
K_i\{g\ge L\}\le \frac{g_i+\delta\Omega_g}{L}. \tag{1}
\]

For the top vertex \(v\), \(g_v=0\), so if \(H>B\tau\),
\[
K_v\{g\ge aH\}\le \frac{\delta\Omega_g}{aH}=O(\tau/B).
\]
This recovers the shallow-recursion picture: carriers of \(v\), and then carriers of sufficiently shallow carriers, are mostly shallow on average.

**Death point.** To turn this into discharging, one needs a closed shallow carrier class or a local unavoidable sink. The needed estimate is
\[
\sum_{i\in C}\pi_i K_i(C^c)\ll 1
\quad\text{for some shallow recurrent carrier set }C,
\tag{2}
\]
or a pointwise version \(\sup_{i\in C}P_i^+(C^c)=O(\delta/H)\). But (1) only gives
\[
K_i\{g\ge L\}\le \frac{g_i+\delta\Omega_g}{L},
\]
which is order one for boundary shallow rows with \(g_i\sim L\). This is exactly the s3 leakage wall in discharging language.

The witness digraph does not repair it. Averaging a closed witness class cancels the \(\mu\)-transport charge and leaves only the LP slack:
\[
\sum_x\pi_x\sum_k \alpha_k^x(g_k-g_x)
=
\sum_x\pi_x\sum_k \beta_k^x(g_k-g_x),
\]
so that branch collapses to the known exposedness-dual frame.

**New objects / sublemmas**

1. Positive-carrier kernel \(K=P^+/(1+N_i)\).
2. Carrier harmonicity:
\[
|(Kg)_i-g_i|\le \delta\Omega_g.
\]
3. Band leakage:
\[
K_i\{g\ge L\}\le (g_i+\delta\Omega_g)/L.
\]
4. Native missing lemma: quantitative shallow carrier closure (2).

Calibration: \(P(\)linear law true\()\approx 0.78\). \(P(\)this discharging proof survives audit\()\approx 0.18\); \(P(\)the death certificate survives audit\()\approx 0.84\).

What discharging sees that LP does not: the obstruction is not primarily dual optimality; it is that \(g\) is an approximate harmonic function on the positive-carrier graph. A high shallow web is a near-zero-charge recurrent structure. LP witnesses describe blockers, but carrier discharging identifies the missing theorem as quantitative closure/stability of that positive-carrier recurrent class.