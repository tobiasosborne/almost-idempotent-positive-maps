**VERDICT: DIED-AT-BY-COLLAPSE.**

Native homotopy calculus gets to a clean slope target, but the first place where the path could create or destroy the bad hidden vertex is exactly an exposedness-LP wall.

For fixed rank,
\[
V_r=\{P:P^2=P,\ P{\bf1}={\bf1},\ \operatorname{rank}P=r\}
\]
has tangent space
\[
T_PV_r=\{X:XP+PX=X,\ X{\bf1}=0\}.
\]
For total negativity
\[
\mathcal N(P)=\sum_i \nu_i(P)=\sum_{i,j}(-P_{ij})_+,
\]
on a fixed sign cell,
\[
d\mathcal N_P(X)=-\sum_{P_{ij}<0}X_{ij}.
\]
So the projected gradient flow is well-defined piecewise:
\[
\dot P=-\Pi_{T_PV_r}Z,\qquad Z_{ij}=-{\bf1}_{P_{ij}<0},\qquad
\dot{\mathcal N}=-\|\Pi_{T_PV_r}Z\|^2.
\]

A positive-negativity stopping point satisfies the conormal KKT condition
\[
0\in \partial\mathcal N(P)+P^TY+YP^T-Y+a{\bf1}^T. \tag{KKT}
\]
This is the native “critical point” object. But it only sees the negative-entry sign pattern plus the projection variety. It does not see \(W\), the canonical separator, \(\widetilde\sigma_v\), or hidden height.

The needed transport lemma would be
\[
\boxed{\quad
\frac{d}{dt}H(P_t)\le C\Bigl(-\frac{d}{dt}\mathcal N(P_t)\Bigr)
\quad}
\]
away from harmless cell changes, integrated from a nonnegative Baake-Sumner endpoint back to \(P_0\). This would give \(H(P_0)\le C\mathcal N(P_0)\), hence the linear law.

The death point is the first exposedness wall:
\[
e_{w,t}(\rho_t)=\kappa_t,\qquad \rho_t=4\sqrt{\delta_t},\quad \kappa_t=\sqrt{\delta_t}/4.
\]
At that instant, controlling the jump or derivative of
\[
H_t=\operatorname{dist}_1(p_{v,t},\operatorname{conv}W_t)
\]
requires the canonical separator \(\phi\), deficit \(g=H-\phi(p)\), and an optimal failed-exposedness witness. That is exactly the LP-dual frame. The native homotopy variables cannot decide whether the emerging wall row becomes exposed, stays shallow, or forms the signed shallow web.

Worse, the known LP cleanup is already dead: pushing a shallow witness through \(P\) changes
\[
B\mapsto B_{\rm pushed}=\frac{B+N}{M_F},
\]
while optimality would require
\[
M_F\ge 1+\frac{N}{B},
\]
but \(M_F\le 1+N\) and \(B<\kappa<1\). Any negative leakage \(N>0\) breaks the transfer.

**New Objects**
- Negativity conormal condition `(KKT)` on \(V_r\).
- Open “linear transport slope” lemma \(dH\le C\,d\mathcal N\).
- Exposedness-wall event \(e_w(\rho)=\kappa\), the exact collapse point.
- Homotopy-critical diagnostic: native criticality is too weak unless supplemented by the same quantitative Baake-Sumner / exposedness modulus already identified in the swarm.

Calibration: \(P(\)linear law true\()=0.82\). \(P(\)this death certificate survives audit\()=0.78\).

What homotopy sees that the LP frame does not: it reframes the missing theorem as a global slope/retraction problem on the idempotent variety, not merely a static witness-support problem. That is useful: any successful proof must either build an \(O(\delta)\)-length retraction to the nonnegative locus or prove a slope inequality preventing \(H\) from increasing faster than negativity is removed. But at the decisive exposedness wall, the path method has no native invariant left and collapses back to the LP separator machinery.