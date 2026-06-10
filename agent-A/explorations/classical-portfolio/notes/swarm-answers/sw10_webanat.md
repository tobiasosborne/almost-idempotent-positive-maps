VERDICT: PARTIAL - no contradiction from the current lemma stock. The survivor is a very constrained skinny, shallow, non-W web; the attempted contradiction dies exactly at “barycenter close to `p_v` does not imply carrierwise close/exposed.”

**Proof / Post-Mortem**
Let `C=conv W`, `eps = δR/H <= 0.1`, and `ν_v <= δ`.

The wave-9 height collapse gives:
\[
M_C(v):=\sum_{p_k\in C}P^+_{vk}\le \delta R/H=\varepsilon,
\]
hence
\[
\widetilde\sigma_v=1+\nu_v-M_C(v)\ge 1+\nu_v-\varepsilon\ge 0.9.
\]
Also, since `g=Pg`, `g_v=0`, and `g>=0`,
\[
\sum_k P^+_{vk}g_k=\sum_k P^-_{vk}g_k\le \nu_v R\le \delta R=\varepsilon H.
\]
So almost all positive outside-`C` mass is top-band:
\[
\mathbb E_{P^+_{v,\mathrm{out}}} g \le \frac{\delta R}{\widetilde\sigma_v}\le \frac{\varepsilon}{1-\varepsilon}H.
\]

The positive-carrier shadow is real but weaker than the tempting contradiction. For off-site positive mass `σ_off`,
\[
q_v=\frac1{\sigma_{\rm off}}\sum_{k\ne v}P^+_{vk}p_k,\qquad
\|q_v-p_v\|_1\le (2+4\delta)\nu_v/\sigma_{\rm off}.
\]
This is an average shadow only. If `σ_off` is order one, the barycenter is `O(δ)` from `p_v`; if `σ̃≈1` is mostly self/duplicates, it only says little about distinct carriers. The contradiction would need a uniform facial modulus:
\[
\operatorname{dist}_1\!\left(p_v,\operatorname{conv}(S\setminus B_r(p_v))\right)\ge cr,
\]
or equivalently a quantitative exposedness margin. But `v` is hidden, and skinny pairs are exactly where this modulus degenerates.

Surviving web blueprint:

- `v` has at most `eps` positive mass on `C`; its positive mass is almost entirely outside `C` and at `g=O(δR)`.
- Exact duplicate/self mass does not make `v` non-vertex. The multiplicity-correct convention treats coincident rows as one geometric vertex. If that point is exposed it joins `W`; if hidden, it still needs geometrically distinct blockers or shadows.
- Any shallow carrier `x` with `g_x <= ηH` satisfies the same recursion:
\[
\sum_{p_k\in C}P^+_{xk}\le (g_x+\delta R)/H\le \eta+\varepsilon.
\]
So shallow carriers also finance themselves mostly from non-W shallow rows.
- F-ND excludes near-delta shallow carriers:
\[
o_x\ge \min\left\{t_0,\frac{H-g_x-5\delta}{3}\right\}.
\]
Thus every genuine shallow web node must have nontrivial off-own-site spread.
- Nonvertices do not end the web: by affine `g`, a nonvertex top-band row descends to top-band row vertices except for `O(g_x/H)` mass on `W`.
- Direct two-site cycles are capped:
\[
P_{ab},P_{ba}\ge c\quad\Rightarrow\quad c^2\le \frac14+2\delta(1+\delta).
\]
So an order-one mutual pair cannot be two direct coefficients near 1.
- Disjoint order-one two-ball cycles are excluded by the wave-9 return-mass bound; the survivor must be skinny and spread across partner balls.
- Non-skinny shadow cycles pay:
\[
\mu\nu\le 1-\theta\quad\Rightarrow\quad \delta\ge \theta^2H^2/64.
\]
So in the small `δ/H^2` regime, any closed shallow class must have `μν=1-o(1)`.
- X1/F-WR kills closed common-pattern skinny shells unless they collapse to coincident rows or export reciprocal carrier mass. Hence the survivor is not a clean finite two-cycle; it is a skinny, spread-mass, top-band hidden-vertex web with external reciprocal support.

**New Sub-Lemmas**
1. Sigma-web balance: proved above. `M_C(v)<=δR/H`, `σ̃_v>=1+ν_v-δR/H`, and positive `g`-budget `<=δR`.

2. Corrected carrier shadow: proved above. It is barycentric, with scale `(2+4δ)ν/σ_off`; it is not a carrierwise clustering lemma.

3. Shallow recursion: proved. If `g_x<=ηH`, then positive mass from `x` into `C` is `<=η+δR/H`.

4. Multiplicity convention consequence: proved from the robust vertex test. Exact duplicates are one geometric vertex; duplicate mass cannot certify non-vertex status.

5. Missing lemma, open: uniform facial/exposedness modulus for hidden top-band webs. This is exactly where the contradiction dies.

**Probabilities**
`P(existential DMF true) = 0.62`.

`P(this structural blueprint survives audit) = 0.78`.

**Sharpest Structural Insight**
The phrase “`σ̃≈1 web`” is slightly misleading unless self/duplicates are separated from distinct off-site carriers. Wave 9 proves almost all positive mass is outside `conv W` and shallow, but the sharp shadow only controls a barycenter. The only surviving obstruction is therefore not “many carriers visibly clustered at `v`”; it is a hidden facial-angle failure: top-band non-W rows can average back near `v` while avoiding `W`, unless quantitative Baake-Sumner or a new facial modulus forces that average to expose or collapse.