# w19_leftcone — FALSE AS STATED: exact n=4 counterexample family (codex, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w19_leftcone/brief.md. Artifacts: experiments/out/w19_leftcone/.

VERDICT: FALSE AS STATED.

I saved the full report at [verdict.md](/tmp/codex-sigma-wall/w19_leftcone/verdict.md). The decisive counterexample is an exact `n=4`, rank-3 idempotent family with `delta = eps` where `K_C` has an extreme point tending to `(1/2,1/2,0,0)`, while its distance to the row set tends to `2/3` and to the visible recurrent rows tends to `1`. So no `O(delta)` row-proximity lemma can hold.

I also proved the correct universal replacement:

\[
\operatorname{dist}_1(\ell,\operatorname{conv}\{p_i\})
\le (2+4\delta)\operatorname{neg}(\ell)
\le (2+4\delta)C\delta.
\]

That bound is clone-invariant but too weak for the intended height/hiddenness payoff.

Saved artifacts:

- [leftcone_counterexample.py](/tmp/codex-sigma-wall/w19_leftcone/leftcone_counterexample.py)
- [leftcone_counterexample_results.json](/tmp/codex-sigma-wall/w19_leftcone/leftcone_counterexample_results.json)
- [leftcone_vertex_check.py](/tmp/codex-sigma-wall/w19_leftcone/leftcone_vertex_check.py)
- [leftcone_vertex_results.json](/tmp/codex-sigma-wall/w19_leftcone/leftcone_vertex_results.json)
- [progress.md](/tmp/codex-sigma-wall/w19_leftcone/progress.md)

I ran the exact-family verifier and the `n=7` w16 vertex enumeration. The w16 check is consistent with the failure mode: many `K_C` vertices are not especially near visible rows, but the small analytic family is the actual refutation.
---
## Appendix: verdict.md (worker long-form, verbatim)

# VERDICT: FALSE AS STATED

The proposed perturbative lemma is false, even for arbitrarily small row
negative mass and even if `neg(l) = 0`.  The obstruction is not cloning or
hiddenness.  It is signed cancellation inside the left-fixed probability slice:
new extreme stationary vectors can sit over high-diameter faces of the row
polytope.

## Exact counterexample family

Fix `eps > 0` and set

\[
P_\varepsilon=
\begin{pmatrix}
1-\varepsilon/3&-\varepsilon/3&-\varepsilon/3&\varepsilon\\
\varepsilon/3&1+\varepsilon/3&\varepsilon/3&-\varepsilon\\
0&0&1&0\\
1/3&1/3&1/3&0
\end{pmatrix}.
\]

This is exactly idempotent and row-stochastic.  One factorization is

\[
\Lambda=\begin{pmatrix}
1&0&0\\0&1&0\\0&0&1\\1/3&1/3&1/3
\end{pmatrix},\qquad
B=\begin{pmatrix}
1-\varepsilon/3&-\varepsilon/3&-\varepsilon/3&\varepsilon\\
\varepsilon/3&1+\varepsilon/3&\varepsilon/3&-\varepsilon\\
0&0&1&0
\end{pmatrix},
\]

with \(B\Lambda=I_3\), so \(P=\Lambda B\) and \(P^2=P\).  The row negative
mass is

\[
\delta(P_\varepsilon)=\varepsilon .
\]

For any fixed \(C\ge 0\), let \(r=C\varepsilon\) and

\[
\ell_{\varepsilon,C}=\left({1+r\over2},{1+r\over2},-r,0\right).
\]

Then \(\ell_{\varepsilon,C}P_\varepsilon=\ell_{\varepsilon,C}\),
\(\ell_{\varepsilon,C}{\bf 1}=1\), and
\(\operatorname{neg}(\ell_{\varepsilon,C})=C\delta\), hence
\(\ell_{\varepsilon,C}\in K_C\).  For \(C=0\) this is already a nonnegative
left-fixed probability vector.

It is an extreme point of \(K_C\).  Parametrize the left-fixed affine slice by
\(\beta=(x,y,z)\), \(x+y+z=1\), via \(\ell=\beta B\).  Then

\[
\ell_3=1-x-y-{\varepsilon\over3}(x-y),\qquad
\ell_4=\varepsilon(x-y).
\]

At \(\ell_{\varepsilon,C}\), the two valid subset-sum inequalities

\[
\ell_3\ge -r,\qquad \ell_3+\ell_4\ge-r
\]

are active.  Their gradients in \((x,y)\) have determinant \(2\varepsilon\),
so in the two-dimensional slice their intersection is a vertex.

As \(\varepsilon\to0\),

\[
\ell_{\varepsilon,C}\to(1/2,1/2,0,0),
\]

while the row set tends to
\[
\{e_1,e_2,e_3,(1/3,1/3,1/3,0)\}.
\]

Therefore

\[
\operatorname{dist}_1(\ell_{\varepsilon,C},\{p_i\})
\to {2\over3},
\]

and the distance to the visible recurrent rows tends to \(1\).  No estimate
\(O(\delta)\) to the row set, let alone to visible rows, can hold.

## Delta-zero anchor

For a nonnegative stochastic idempotent \(P\), each row \(p_i\) is stationary:
\(p_iP=p_i\).  A stationary distribution gives zero mass to transient states,
so all transient columns of \(P\) vanish.  On each closed communicating class
\(C_s\), the restriction has a unique stationary probability row \(\pi_s\);
because all rows in \(C_s\) are stationary and supported on \(C_s\), they all
equal \(\pi_s\).  A transient row is stationary after one step, hence has the
form

\[
p_i=\sum_s \alpha_{is}\pi_s,\qquad \alpha_{is}\ge0,\quad \sum_s\alpha_{is}=1.
\]

Now let \(\ell P=\ell\), \(\ell{\bf 1}=1\), and \(\ell\ge0\).  Again \(\ell\)
has no transient mass, and on each recurrent class its restriction is a
nonnegative multiple of \(\pi_s\).  Thus

\[
K_0=\{\ell:\ell P=\ell,\ell{\bf1}=1,\ell\ge0\}
=\operatorname{conv}\{\pi_1,\ldots,\pi_k\}.
\]

The extreme points are exactly the recurrent equal-input rows \(\pi_s\), which
are the visible row vertices at \(\delta=0\).

## Correct universal replacement

The following statement is true and sharp enough to explain the data, but it is
too weak for the intended campaign payoff:

\[
\boxed{\operatorname{dist}_1(\ell,\operatorname{conv}\{p_i\})
\le (2+4\delta)\operatorname{neg}(\ell)
\le (2+4\delta)C\delta\quad(\ell\in K_C).}
\]

Proof: since \(\ell=\ell P=\sum_j\ell_jp_j\), write
\(\nu=\operatorname{neg}(\ell)\).  If \(\nu>0\),

\[
\ell=(1+\nu)q-\nu r,
\]

where \(q,r\in\operatorname{conv}\{p_i\}\) are the positive and negative
coefficient barycentres.  Hence
\[
\operatorname{dist}_1(\ell,\operatorname{conv}\{p_i\})
\le \nu\|q-r\|_1.
\]

Every row has sum \(1\) and negative mass at most \(\delta\), so every row has
\(\ell^1\)-norm at most \(1+2\delta\), giving row diameter at most \(2+4\delta\).
If \(\nu=0\), then \(\ell\in\operatorname{conv}\{p_i\}\) exactly.

The counterexample shows why this is the right replacement: the bad extreme
point is far from every row but lies in the row convex hull when \(C=0\), and
within \(O(C\delta)\) of it for \(C>0\).

## Numerical checks

Artifacts:

- `leftcone_counterexample.py`
- `leftcone_counterexample_results.json`
- `leftcone_vertex_check.py`
- `leftcone_vertex_results.json`

Counterexample family, enumerated vertices of \(K_C\), \(C=1\):

| eps = delta | dist to row set | dist to visible rows | enumerated as vertex |
|---:|---:|---:|---|
| 1e-1 | 0.8666667 | 1.1666667 | yes |
| 1e-2 | 0.6866667 | 1.0166667 | yes |
| 1e-3 | 0.6686667 | 1.0016667 | yes |
| 1e-4 | 0.6668667 | 1.0001667 | yes |

Certified w16 rational instance, exhaustive subset-halfspace vertex enumeration
at \(n=7\):

| C | vertices | max dist to rows | /delta | max dist to visible | /delta |
|---:|---:|---:|---:|---:|---:|
| 1 | 30 | 1.3550716 | 5.9329 | 1.4701079 | 6.4365 |
| 2 | 30 | 1.5940359 | 6.9791 | 1.6140812 | 7.0669 |
| 4 | 38 | 2.2867001 | 10.0118 | 2.2867001 | 10.0118 |
| 10 | 42 | 5.0275033 | 22.0118 | 5.0275033 | 22.0118 |

Random exact chart checks around H-M singleton strata also produced the same
phenomenon: with \(\delta=0.0023233\), a \(K_1\) vertex had distance
0.7841412 from the row set.  The analytic four-state family is the decisive
small-delta version.

## Implication-chain analysis

If the proposed lemma were true for \(C\ge1\) with visible rows, then every row
\(p_i\) would lie in \(K_C\), and since \(K_C\) is the convex hull of its
extreme points, every row would be \(O(\delta)\)-close to
\(\operatorname{conv}\{p_w:w\in W\}\).  This would prove the stronger linear
height bound

\[
H(P)\le A\delta
\]

directly, closing both the large-\(\widetilde\sigma\) and small-\(\widetilde\sigma\)
branches.

The counterexample kills that route.  The true convex-hull replacement only
says quasi-positive left-fixed vectors remain close to \(\operatorname{conv}\)
of all rows, which gives no control on height above the visible hull.  The
missing additional lemma would have to be a row-vertex/facial anti-cancellation
principle, for example:

> A hidden row vertex with large \(\widetilde\sigma\) cannot be supported only
> through broad cancellation faces of the left-fixed positive slice; some
> mass must pin to a bounded-diameter visible/near-visible row face.

This is essentially the recorded anti-splitting problem, not a consequence of
left-fixed extreme points alone.

## Clone invariance

Under an index split with fibre weights \(\alpha_b\) and
\(\widehat P_{ab}=\alpha_bP_{\pi(a),\pi(b)}\), fixed vectors aggregate and lift
exactly.  If \(\widehat\ell\widehat P=\widehat\ell\), then

\[
L_j=\sum_{a\in\pi^{-1}(j)}\widehat\ell_a
\]

satisfies \(LP=L\), and in fact
\[
\widehat\ell_b=\alpha_b L_{\pi(b)}.
\]

Conversely \(L\mapsto\widehat L_b=\alpha_bL_{\pi(b)}\) lifts fixed vectors.
The lift preserves \(\ell^1\) distances and negative mass:

\[
\operatorname{neg}(\widehat L)=\operatorname{neg}(L).
\]

Thus the corrected convex-hull statement and the counterexample mechanism are
clone-invariant.

## Calibration

\[
P(\text{lemma true as stated})=0.
\]

\[
P(\text{corrected convex-hull lemma true})=1
\]
because it is proved above.

\[
P(\text{this left-cone extreme-point route reaches the linear law})\approx0.03.
\]

\[
P(\text{a modified row-vertex/anti-splitting route reaches the linear law})\approx0.24.
\]
