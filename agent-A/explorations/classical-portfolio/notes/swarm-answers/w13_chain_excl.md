**DIED-AT** the missing path-product lower bound.

I did not prove thin-chain exclusion. The strongest derivation I can honestly get is a recursive high-web reduction: every shallow node in the component is itself far from `conv W` and has large geometric `σ̃`, but the exact identities still do not force a dimension-free lower bound on the component path product `Π_C`.

The needed but unproved inequality is essentially

\[
\Pi_C \gtrsim \tau - O(L\delta)
\]

or any substitute strong enough to contradict the Wave-12 survivor

\[
\Pi_C \le E_L(\delta,\zeta)+{2(1+\delta)\varepsilon\over r_*-4\delta},
\qquad r_*=0.85\tau .
\]

Wave 12 proves the finisher for components beating this floor; see [w12_comp_finisher.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/swarm-answers/w12_comp_finisher.md:1). The remaining class is exactly long-thin support components.

**What I Can Prove**

Let \(S=\{g\le r_*\}\), with positive band closure \(P^+_{S,S^c}=0\), and let \(C\) be a \(B^+\)-component in \(S\). If \(i\in C\), then

\[
\operatorname{dist}_1(p_i,C_W)\ge H-g_i\ge H-r_* .
\]

Using the banked height cap rowwise,

\[
\operatorname{dist}_1(p_i,C_W)
 \le 2(1+2\delta)\max(\widetilde\sigma_i,\nu_i),
\]

so if

\[
H-r_* > 2(1+2\delta)\tau ,
\]

then every node in the component has \(\widetilde\sigma_i>\tau\). Thus the web recurses: the chain is not made of harmless shallow rows; every node is itself a high hidden web node.

Also, from \(g=Pg\),

\[
P_i^+\{g\ge H\}
\le {g_i+\nu_i\Omega_g\over H}
\le {r_*+\delta(2+4\delta)\over H}.
\]

So for \(H=B\tau\),

\[
P_i^+\{g\ge H\}\le {0.85\over B}+O(\tau/B).
\]

This is the expected closure fact: high shallow chain nodes send almost no positive mass to \(W\)-deep rows when \(B\) is large. It supports the component-finisher setup, but it does not collapse the chain.

**Where The Proof Dies**

Exactness only prices a thin edge locally. In a one-edge/self-loop schematic row identity,

\[
p_i=(1-a)p_i+a p_{i+1}+\text{signed correction},
\]

the correction only needs to absorb

\[
a\,\|p_{i+1}-p_i\|_1 \lesssim \delta .
\]

Thus a thin chain can evade all current inequalities at the formal scale

\[
a=\tau,\qquad \|p_{i+1}-p_i\|_1\asymp\tau,\qquad
a\|p_{i+1}-p_i\|_1\asymp\delta,
\]

while its path product over \(L\) links is

\[
\Pi_C\sim a^L=\tau^L\ll \tau .
\]

This is not an exact construction. It is the obstruction: current identities charge each link by a per-row \(\delta\)-budget, but the finisher needs a multiplicative path-product lower bound. The \(L\)-dependence does not cancel.

The banked geometry exclusions do not close this gap. They kill direct two-site order-one mutual carrying, disjoint order-one two-ball cycles, and non-skinny payment patterns, but the report still marks the skinny spread-mass regime open; see [08-residual-dmf.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/sections/08-residual-dmf.tex:129).

The refuter also failed to build an exact thin-chain instance: affine-line templates create shortcuts, private coordinates blow the negative budget, and skip-edge suppression costs order \(\varepsilon^2\); see [w12_chain_refuter.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/swarm-answers/w12_chain_refuter.md:31). That is evidence for truth, not a proof.

**Verdict**

Thin-chain exclusion remains the kernel open statement, exactly as the Wave-12 state records in [wave5-sigma-wall-parallel.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave5-sigma-wall-parallel.md:863).

\(P(\text{thin-chain exclusion true}) \approx 0.68\).  
\(P(\text{this died-at diagnosis survives audit}) \approx 0.86\).

No full chain assembled, because the exclusion is not proved.