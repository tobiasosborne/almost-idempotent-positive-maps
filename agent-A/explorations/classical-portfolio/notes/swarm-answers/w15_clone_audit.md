# w15_clone_audit — OBSTRUCTION REAL BUT CONDITIONAL (codex hostile audit, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w15_clone_audit/brief.md

VERDICT: OBSTRUCTION REAL BUT CONDITIONAL.

The index-cloning construction survives the hostile checks. It preserves the exact signed-idempotent data and all row geometry, while driving the raw-index path product to `0`. But it is not yet an unconditional counterexample to Conjecture 2, because no antecedent-realizing seed is in the record: the campaign record says `67,000+` verified instances and none with `\widetilde\sigma_v>\tau` and `H>0.1\tau` [kernel-conjecture.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex:273). A clone of a non-qualifying instance still does not qualify.

So the precise status is: if any non-vacuous seed satisfying the high-hidden antecedent exists, the raw-index path-product floor is false as written. Otherwise the floor may be vacuously true.

**Audit Checks**

Let `T:\mathbb R^n -> \mathbb R^{\hat n}` be `(Tx)_b=\alpha_b x_{\pi(b)}` with `sum_{b in pi^{-1}(j)} alpha_b=1`.

Algebra:
\[
\sum_b \widehat P_{ab}
=\sum_j P_{\pi(a)j}=1.
\]
\[
(\widehat P^2)_{ab}
=\sum_c \alpha_cP_{\pi(a)\pi(c)}\alpha_bP_{\pi(c)\pi(b)}
=\alpha_b(P^2)_{\pi(a)\pi(b)}
=\widehat P_{ab}.
\]
\[
\sum_b \max\{-\widehat P_{ab},0\}
=\sum_j \max\{-P_{\pi(a)j},0\},
\]
so `delta(P_hat)=delta(P)`.

Geometry:
\[
\|Tx-Ty\|_1=\sum_b\alpha_b|x_{\pi(b)}-y_{\pi(b)}|=\|x-y\|_1.
\]
Rows are exactly `\hat p_a=T p_{\pi(a)}`. Coincident clones are exactly coincident row points, so the multiplicity-correct vertex definition [kernel-conjecture.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex:84) does not rescue the raw graph.

Exposers lift and descend. If `h(x)=lambda.x+b`, define
\[
\widehat h(y)=h(Ry),\qquad (Ry)_j=\sum_{b\in\pi^{-1}(j)}y_b.
\]
Then `||R||_{1->1}<=1`, so the same margins hold. Conversely, `\widehat h\circ T` has coefficients `sum_b alpha_b \widehat\lambda_b` per old fiber, still `\ell^\infty`-bounded by `1`. Hence exposedness, hiddenness, `W`, `H`, and row-vertex status are invariant.

For the canonical separator, take `\widehat\varphi=\varphi\circ R`; then
\[
\widehat g_a=H-\widehat\varphi(\widehat p_a)=g_{\pi(a)},\qquad
\widehat P\widehat g=\widehat g.
\]
Also
\[
\widehat{\widetilde\sigma}_{\hat v}
=\sum_b \max\{\widehat P_{\hat v b},0\}\mathbf 1_{\dist(\widehat p_b,\widehat C_W)>0}
=\widetilde\sigma_v.
\]
Thus `tau`, `S_t`, and the high-hidden antecedent are preserved.

Target letter:
For an old carrier SCC `C`, the full preimage `\widehat C=pi^{-1}(C)` lies in `\widehat S_t` and is strongly connected. If old directed diameter is `L`, then clone diameter is at most `L` for different old vertices and at most `2L` between two clones of the same old vertex, or `1` if there is a self-loop. This is independent of `M`.

With equal splitting inside `C`, every positive edge in `\widehat C` has weight at most `(1+\delta)/M`. For two distinct clones of the same old node, every directed path between them has length at least one and all edges are divided by `M`, hence
\[
\widehat\Pi_{\widehat C}\le {1+\delta\over M}
\]
for large `M`. No path can avoid the divided edge, because paths are required to stay inside the cloned component.

**Repair**

The quotient repair is the right replacement for this obstruction. Define row classes by exact equality `p_i=p_j`, and set
\[
\overline P_{[i],[j]}:=\sum_{b\in[j]}P_{ib}.
\]
For the cloning construction this gives exactly the original edge weights:
\[
\sum_{b\in\pi^{-1}(j)}\widehat P_{ab}
=P_{\pi(a)j}.
\]
So the quotient path product is clone-invariant.

What is inherited: stochastic lumpability, row sums, idempotence, harmonicity of `g`, and the Birkhoff finisher for pure clone fibers.

What must be re-proved: the w12 finisher for arbitrary coincident-row quotients, especially that quotient collapse/exposure lifts back to the original row geometry when there can be internal signed cancellation inside a duplicate row class.

Recommended replacement:

```latex
\begin{conjecture}[Multiplicity-correct path-product floor]\label{conj:quotient-floor}
Let \(i\sim j\) mean \(p_i=p_j\) as vectors, and for classes set
\[
\overline P_{[i],[j]}:=\sum_{b\in[j]}P_{ib}.
\]
For \(S_t=\{i:g_i<t\}\), let \(\overline{\mathcal G}_t\) be the directed graph on
classes \([i]\subset S_t\) with edge \([i]\to[j]\) when
\(\overline P_{[i],[j]}>0\). For a strongly connected component
\(\overline{\mathcal C}\), define \(\overline\Pi_{\overline{\mathcal C}}\)
by the same min--max path-product formula using the edge weights
\(\overline P\).

There are universal \(\delta_0,B,c,C'\) such that, for
\(\delta\le\delta_0\), if \(v\) is a hidden top vertex with
\(\widetilde\sigma_v>\tau\) and \(H>B\tau\), then for some
\(t\in[\kappa\Omega/2,\kappa\Omega]\), every quotient carrier component
\(\overline{\mathcal C}\) of \(S_t\) carrying positive \(\overline P\)-mass
from \([v]\) satisfies
\[
\overline\Pi_{\overline{\mathcal C}}
\ge c\tau-C'\overline L\,\delta .
\]
\end{conjecture}
```

Coherence with `w15_sos`: consistent. The scalar shadow is false but not a matrix refutation; cloning shows the raw atom-level floor is not a multiplicity-invariant matrix target.

Calibrated `P(this verdict survives further audit) = 0.88`.