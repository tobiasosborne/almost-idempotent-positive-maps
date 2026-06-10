Verdict: **HLC is not proved by this pass.** X1 does identify the exact wall, but the full arbitrary-frame obstruction is still the known dual-localization/frame-transfer gap.

**PROVED wall, single-mode exact completion.**  
For a formal skinny shell on one affine mode,
\[
p_i=q+t_i r,
\]
exactness forces
\[
q\cdot t=0,\quad r\cdot 1=0,\quad r\cdot t=1.
\]
Thus, with \(\Delta t=\max t-\min t\),
\[
1=r\cdot(t-c1)\le \|r\|_1\Delta t/2,
\]
so
\[
\operatorname{diam}_1\{p_i\}=\Delta t\|r\|_1\ge 2.
\]
Therefore the W2c shadow-only idea cannot be completed as an exact idempotent while keeping a nonconstant high mode inside a sub-\(\rho\) skinny cluster. Since \(\rho=4\sqrt\delta\ll 1\), exactness must introduce reciprocal carriers outside the skinny cluster.

**PROVED interpretation of `RΛ=I`.**  
The completion condition is the biorthogonality
\[
\sum_i R_{a i}\Lambda_{i b}=\delta_{ab}.
\]
So the archetype rows \(R_a\) are signed measures on the row-index set, dual to the abstract coordinate functions \(\phi_b(i)=\Lambda_{ib}\). A high shell where the \(\phi_b\)’s are almost constant cannot supply this pairing internally; the missing dual mass has to appear as reciprocal carriers.

**SKETCH obstruction inequality, not yet proved generally.**  
The right named target is:

\[
\textbf{Biorthogonal high-shell cost:}
\]
if a high shell \(S=\{h_i\ge H/2\}\) is exact-completed with \(P=\Lambda R,\ R\Lambda=I\), all high row vertices are hidden, and \(\delta<aH^2\), then the reciprocal carriers forced by \(R\Lambda=I\) cannot all remain hidden inside an \(O(\rho)\)-shadow system. Hence either a high carrier is \((\rho,\kappa)\)-well-exposed, or
\[
\max_i \operatorname{neg}((\Lambda R)_i)\ge aH^2.
\]

This is **PROVED** in the canonical frame (`R=[I_r|0]`), where `dist(row,conv W) <= 2 neg(row)`, hence \(\delta\ge H/2\). It is also **PROVED** for the rank-one/single-mode wall above. It is **OPEN** for arbitrary collapsed frames because abstract coordinate negativity can be hidden by \(R\); converting the biorthogonal carrier mass into actual row negativity is exactly the frame-transfer / dual-localization gap noted in [F2-completion-LP.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave1/F2-completion-LP.md:1).

So X1 sharpens HLC to the right inequality, but I cannot honestly mark the target proved.