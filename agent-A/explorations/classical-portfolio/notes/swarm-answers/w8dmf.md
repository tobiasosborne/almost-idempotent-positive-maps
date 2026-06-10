DIED-AT: the descent fails at hidden-vertex recursion. Nonvertex Krein–Milman descent is clean, and the δ=0 Baake–Sumner anchor is clean, but a hidden vertex’s “own witness” is not a positive convex decomposition of that vertex. Substituting it loses sign/mass control and gives no strictly decreasing invariant.

**Descent Formalization**
Let `E` be the deficit tolerance and set

`D_E = {i : g_i >= H - E}`, `T_E = {i : g_i < H - E}`.

Since every `w in W` has `phi(p_w) <= 0`, every W-row is deep: `g_w >= H`, hence `W subset D_E` for `E > 0`.

For a root hidden top vertex `v`, an all-shallow witness means `mu(T_E)=1` in the dual (♦) from [wave8-fable-closer.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave8-fable-closer.md:72).

The valid descent step is:

If `j in T_E` is nonvertex and admits
`p_j in conv{p_i : i in T_E cap F_v, i != j}`,
then replacing `mu_j p_j` by that convex combination preserves positivity, far-support, total `mu` mass, and the `g`-average. The face dimension drops, so this part terminates.

The invalid step is hidden vertices. For hidden `x`, its witness is

`sum mu^x_j p_j + sum alpha^x_k p_k = sum beta^x_k p_k + gamma_x p_x`.

Solving for `p_x` gives

`p_x = gamma_x^{-1}(sum mu^x_j p_j + sum alpha^x_k p_k - sum beta^x_k p_k)`.

That is signed. The `beta` term is negative, near rows can enter through `alpha`, and there is no preserved probability measure on far shallow rows. So recursion through hidden vertices is not Krein–Milman descent; it is a signed certificate substitution.

**δ=0 Anchor**
Baake–Sumner gives the exact Markov-idempotent normal form: a partition into zero-column/transient indices and recurrent blocks whose restrictions have equal positive rows [equal-fin.tex](/home/tobias/Projects/almost-idempotent-positive-maps/refs/baake-sumner-2007.11433/equal-fin.tex:1060). Thus transients descend to recurrent equal-input blocks, and recurrent block rows are the terminal exposed objects. This kills the web at δ=0.

But at δ>0, `B=P_TT` being approximately idempotent is not enough. It does not give a nearby nonnegative Markov idempotent with a stable Baake–Sumner partition, and it does not control the LP witness graph.

**Minimal Obstruction**
Two shallow hidden vertices `a,b` with optimal-witness edges

`a -> b`, `b -> a`

already defeat the proposed induction. Both are top-band vertices, neither is a nonvertex, neither is W, and each has an all-shallow witness supported on the other. Candidate decreasing quantities fail:

`face dimension`: already zero.  
`top-band vertex count`: stays `2`.  
`support size`: stays `1`.  
`unclassified mu-mass`: stays `1`.

Baake–Sumner says this exact object cannot occur at δ=0 unless the rows collapse into equal-input recurrent structure. The missing theorem is precisely a quantitative δ>0 version excluding this shallow hidden cycle.

**New Sub-Lemmas**
1. Far-band convex pruning: nonvertex descent is valid only when the decomposition stays inside `F_v cap T_E`; otherwise near rows enter `alpha` and dual normalization changes.
2. Hidden-witness substitution obstruction: (♦) cannot be used as a positive mass-preserving row decomposition because of the signed `- beta` term.
3. Closed shallow witness class criterion: DMF follows if every closed class in the shallow hidden-witness graph has universal escape mass to `D_E`; this is equivalent to the missing quantitative Baake–Sumner stability input.

Calibration: `P(DMF true as stated)` ≈ 0.55. `P(weakened “extreme/pruned witness” DMF true)` ≈ 0.70. `P(this descent failure survives audit)` ≈ 0.82. No files were changed.