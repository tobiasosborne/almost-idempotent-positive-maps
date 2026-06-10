**VERDICT: DIED-AT-BY-COLLAPSE.**

The extremal/KKT route reaches a clean native stationarity formula, but the moment the proof enforces “`v` remains hidden, hence not in `W`,” the normal cone is exactly the exposedness-LP dual cone. At that point the strategy has collapsed into the prior LP basin.

Native setup: on the rank-fixed unital idempotent manifold,
\[
T_P\mathcal I=\{\Delta:\Delta P+P\Delta=\Delta,\ \Delta{\bf 1}=0\}.
\]
Equivalently, locally \(\Delta=[A,P]\) with the unital constraint \((I-P)A{\bf 1}=0\). For a fixed hidden vertex \(v\), fixed \(W\), and fixed separator \(g\) with \(Pg=g,\ g_v=0\), the height derivative is
\[
dH_P(\Delta)=-(\Delta g)_v .
\]
In particular, the native diagonal/range-potential variations
\[
\Delta_f=[D_f,P],\qquad f=Pf,
\]
give
\[
dH_P(\Delta_f)=P(fg)_v .
\]
This is the variational object the manifold geometry naturally exposes.

The KKT condition for maximizing \(H-C\delta\), while keeping \(v\) hidden, has the form
\[
-e_v g^\top
\in
C\,\partial\delta(P)
+\lambda\,\partial t_v(P)
+N_{\{P^2=P,\ P1=1\}}(P)
+\text{chamber walls}.
\]
The death point is
\[
\partial t_v(P)
=
\operatorname{cone}\Bigl\{
(\mu,\alpha,\beta):
\sum_{j\in F_v}\mu_j(p_j-p_v)
+\sum_i\alpha_i(p_i-p_v)
-\sum_i\beta_i(p_i-p_v)=0,\ 
\sum_i\beta_i=t_v
\Bigr\}.
\]
That is exactly the exposedness-dual witness frame. To proceed, KKT would need a separation inequality saying some idempotent tangent direction improves height or lowers active negativity while staying inside this hiddenness cone. Written out, that is the already-open carrier/blocker or signed Baake-Sumner stability statement, not a consequence of KKT.

**Post-mortem.** Ignoring the \(t_v\le\kappa\) chamber constraint, the manifold has plenty of height-increasing directions. Enforcing hiddenness introduces the LP dual certificate. The obstruction becomes the same shallow signed web: the variation must prove that the LP blocker receives enough carrier mass, or that the top-band block is approximately closed. That is precisely where `s3_block.md` dies: the available leakage estimate has an unavoidable \(g_i/(\kappa R)\) term.

**New objects/sublemmas.**

1. Idempotent tangent chart:
\[
\Delta P+P\Delta=\Delta,\quad \Delta1=0.
\]

2. Separator-gradient identity:
\[
dH(\Delta)=-(\Delta g)_v.
\]

3. Range-potential commutator test:
\[
\Delta_f=[D_f,P],\ f=Pf,\qquad dH(\Delta_f)=P(fg)_v.
\]
This is useful diagnostically, but the canonical \(f=g\) specialization is the known dead kernel-energy route.

4. Collapse certificate: the hiddenness KKT multiplier is exactly an exposedness-dual witness \((\mu,\alpha,\beta)\), so this strategy cannot stay native past the chamber constraint.

Calibration: \(P(\)linear law true\()\approx 0.78\). \(P(\)this post-mortem survives audit\()\approx 0.82\). \(P(\)pure KKT proves the law without a new signed Baake-Sumner/tangent-web theorem\()\approx 0.12\).

What this strategy sees that the LP frame cannot: the idempotent geometry says the true first-order directions are off-diagonal image/kernel motions, not arbitrary row moves. The LP frame sees only a static certificate. KKT shows why that distinction still does not close the proof: the hidden-vertex chamber converts the variational normal cone back into the same exposedness-dual cone, so the missing ingredient is a genuine tangent-scale signed Baake-Sumner stability theorem, not sharper stationarity bookkeeping.