VERDICT: DIED-AT. Basicness gives only
\[
|\operatorname{supp}(\mu,\alpha,\beta)|\le d+1,\qquad d=\dim\operatorname{aff}\{p_i\},
\]
for an optimal BFS witness. A shallow hidden 2-cycle needs only two \(\mu\)-atoms, so the hoped-for contradiction would require
\[
2>d+1,
\]
which is false in every nontrivial affine dimension. Basicness does not kill the minimal obstruction.

Proof/post-mortem. The exposedness dual can be written in anchored form
\[
\sum_{j\in F}\mu_j(p_j-p_v)+\sum_k\alpha_k(p_k-p_v)-\sum_k\beta_k(p_k-p_v)=0,\qquad
\sum_{j\in F}\mu_j=1,
\]
with \(\mu,\alpha,\beta\ge0\), minimizing \(B=\sum\beta_k=t^*\). Hence an optimal basic feasible witness exists, and its total positive support is at most rank \(d+1\). Non-vertex shallow \(\mu\)-atoms can be pruned by replacing \(p_j\) with its convex decomposition inside \(F_v\cap T_E\), preserving \((♦)\), \(\sum\mu=1\), and \(B\). W-atoms are deep since \(g_w\ge H\). Thus any all-shallow basic witness reduces to hidden row vertices.

The route dies exactly there: the LP for \(v\) contains no constraints enforcing the separate witness equations for those hidden vertices. A basic witness may put all \(\mu\)-mass on one or two shallow hidden vertices and use \(\alpha,\beta\) to satisfy the signed identity. The failed recursion remains signed:
\[
p_x \text{ via its witness contains } -\sum_k\beta^{(x)}_k p_k,
\]
so substitution does not preserve a probability descent or a decreasing invariant.

New sub-lemmas.

1. Basic-witness support lemma: an optimal exposedness-dual BFS exists with total active \((\mu,\alpha,\beta)\)-support \(\le d+1\). Proved above.

2. Shallow non-vertex pruning: if a shallow \(\mu\)-atom lies in \(\operatorname{conv}(F_v\cap T_E)\), it can be replaced by atoms in a lower face without changing optimality. Status: proved under the stated in-band decomposition hypothesis.

3. Basic hidden-web reduction: failure of existential DMF for a basic witness implies a closed shallow hidden-vertex web after pruning W and non-vertices. Status: partial; closure still needs quantitative Baake-Sumner stability.

Calibration: \(P(\)existential DMF true\()\approx0.72\). \(P(\)this post-mortem survives audit\()\approx0.82\).

Sharpest structural insight: basicness is useful only as a cleanup device. It lets the optimal witness be made finite, sparse, and vertex-supported, but sparsity is the wrong scale: the obstruction is already a 2-cycle, and two atoms fit comfortably inside an LP basis. The missing theorem is not LP facial dimension counting; it is quantitative exclusion of shallow hidden closed classes.