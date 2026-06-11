# w15_prover — H-M surrogate attack: DIED-AT + THE CLONING OBSTRUCTION (codex, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w15_prover/brief.md. Orchestrator verified the cloning idempotence algebra independently.

VERDICT: DIED-AT.

The H-M signed-surrogate gives shallow positive carrier mass, but it does not give the required index-level path-product floor. The exact failure is that path products are not invariant under multiplicity splitting, while all geometric hypotheses are.

What I can prove:

Let \(A=P^+\), \(N=P^-\), and \(\nu_i=\sum_j N_{ij}\le\delta\). Since \(Pg=g\),

\[
\sum_j A_{ij}g_j
=
g_i+\sum_j N_{ij}g_j .
\]

For the hidden top vertex \(v\), \(g_v=0\), hence

\[
\sum_j A_{vj}g_j\le \delta\Omega .
\]

Thus for \(S_t=\{g<t\}\),

\[
A_v(S_t^c)\le \frac{\delta\Omega}{t}.
\]

At \(t=\kappa\Omega=\tau\Omega/4\),

\[
A_v(S_t\setminus C_W)\ge \widetilde\sigma_v-4\tau .
\]

Using the proved small-\(\widetilde\sigma\) height cap, if \(H>B\tau\) then

\[
\widetilde\sigma_v\ge \frac{H}{2(1+2\delta)}
>
\frac{B}{2(1+2\delta)}\tau,
\]

so, for \(\delta\le 1/4\),

\[
A_v(S_t\setminus C_W)
\ge
\left(\frac{B}{3}-4\right)\tau .
\]

So the H-M surrogate really does generate shallow positive carrier mass when \(B\) is large.

The exact idempotence shortcut also works. Expanding \(P^k=(A-N)^k=P\),

\[
P_{ij}
\ge
(A^k)_{ij}
-
\eta_k,
\qquad
\eta_k=(1+2\delta)^k-(1+\delta)^k
\le
k\delta(1+2\delta)^{k-1}.
\]

Hence if one could prove

\[
(A_C^k)_{ij}\ge c\tau+\eta_k
\]

inside a shallow positive component, then \(P_{ij}>0\) and the direct shortcut would give the desired product scale.

The failed inequality is precisely:

\[
\boxed{
(A_C^k)_{ij}\ \ge\ c\tau + O(k\delta)
\quad\text{or equivalently}\quad
\Pi_C\ge c\tau-C'L\delta .
}
\]

Why it fails as an H-M step:

Given any exact signed idempotent \(P\), split an index \(r\) into \(M\) duplicate indices. With a surjection \(\pi\) from new indices to old ones and positive fiber weights \(\alpha_b\) summing to \(1\) on each fiber, define

\[
\widehat P_{ab}
=
\alpha_b P_{\pi(a),\pi(b)} .
\]

Then

\[
\widehat P\mathbf 1=\mathbf 1,\qquad
\widehat P^2=\widehat P,\qquad
\delta(\widehat P)=\delta(P).
\]

The coordinate-splitting map is an \(\ell^1\)-isometry on row differences, so row vertices, exposedness, \(W\), \(H\), \(g\), and \(\widetilde\sigma_v\) are unchanged.

But if a component \(C\) is split into \(M\) equal duplicate fibers, every edge into a clone is divided by \(M\). The cloned component \(\widehat C\) is still strongly connected, with diameter bounded in terms of the old diameter and independent of \(M\), while

\[
\Pi_{\widehat C}
\le
\frac{1+\delta}{M}.
\]

Thus for any positive right-hand side,

\[
c\tau-C'\widehat L\delta>0,
\]

choosing

\[
M>\frac{1+\delta}{c\tau-C'\widehat L\delta}
\]

violates the claimed floor, with all geometric hypotheses preserved.

Natural repairs fail in the current frame:

1. Iterating \(P^k=P\) controls positive path sums, not atom-level products.
2. Total mass in a component survives cloning, but the finisher needs entry or path-product atoms.
3. Degree or path-count bounds are impossible dimension-free; cloning changes degree without changing geometry.
4. Threshold choice cannot help because \(g\) is unchanged on duplicate fibers.
5. Quotienting exact duplicates would fix this obstruction, but that is not Conjecture 2 as stated and would require a new quotient/near-duplicate finisher.

So the H-M surrogate identifies the right recurrent-carrier idea, but the path-product floor in its current index-level form is not a viable non-vacuous target.

Updated [progress.md](/tmp/codex-sigma-wall/w15_prover/progress.md).

Calibrated probabilities:

\[
P(\text{index-level floor as written is true})\approx 0.30
\]

mostly via possible vacuity of the high-hidden antecedent.

\[
P(\text{this H-M path-product route closes without redefining the floor})\approx 0.18.
\]

A quotient or aggregate-mass version looks more plausible, but it is a different theorem.