# w15_sos — chain-specialized certificate search: SCALAR SHADOW IS FALSE (codex, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w15_sos/brief.md. Artifacts archived to experiments/out/w15_sos/.

VERDICT: all \(L=2,3,4,5\) are **FORMALIZATION BLOCKED** for the actual kernel route. The notes do not define a complete polynomial reduction in only edge weights, \(\delta\), \(\widetilde\sigma\), and \(\tau\); the w13 locus explicitly says the thin-chain scale is “not an exact construction” but the obstruction.

I saved the artifacts in `/tmp/codex-sigma-wall/w15_sos`:

- [answer.md](/tmp/codex-sigma-wall/w15_sos/answer.md)
- [formalization.md](/tmp/codex-sigma-wall/w15_sos/formalization.md)
- [thin_chain_certificate_search.py](/tmp/codex-sigma-wall/w15_sos/thin_chain_certificate_search.py)
- [outputs/thin_chain_search.json](/tmp/codex-sigma-wall/w15_sos/outputs/thin_chain_search.json)
- [outputs/thin_chain_search.txt](/tmp/codex-sigma-wall/w15_sos/outputs/thin_chain_search.txt)

I also tested the strongest scalar shadow I could justify. It has exact rational small-\(\delta\) witnesses with \(\tau=1/100\), \(\delta=1/10000\), \(\widetilde\sigma=1/50\), and \(a_i=d_i=1/100\). They satisfy all scalar constraints but violate \(\Pi_L+L\delta-\tau\ge0\) for every \(L=2,3,4,5\). So no LP/SOS certificate can exist for that scalar shadow at any degree; the missing ingredient must be a genuine matrix/hiddenness row-realization constraint.
---
## Appendix: the formalization (formalization.md, verbatim)

# Reduced Thin-Chain Certificate Target

This is the exact scalar reduction I can justify from the requested notes.
It is intentionally weaker than the full signed-idempotent row problem.
The full reduction is blocked for the reasons quoted below.

## Source Statements

The target in `kernel-conjecture.tex` is the path-product floor: if a hidden
top vertex \(v\) has \(\widetilde\sigma_v>\tau=\sqrt\delta\) and \(H>B\tau\),
then for some shallow-band component \(\mathcal C\),
\[
  \Pi_{\mathcal C}\ge c\tau-C'L\delta .
\]

The wave-12 finisher leaves the survivor class
\[
  \Pi_C \le E_L(\delta,\zeta)+
  \frac{2(1+\delta)\varepsilon}{r_*-4\delta},
  \qquad r_*=0.85\tau .
\]

The wave-13 chain exclusion note gives only the following scalar obstruction:
\[
  p_i=(1-a)p_i+a p_{i+1}+\text{signed correction},
\]
where the correction only needs to absorb
\[
  a\,\|p_{i+1}-p_i\|_1 \lesssim \delta .
\]
It then records the surviving scale
\[
  a=\tau,\qquad
  \|p_{i+1}-p_i\|_1\asymp\tau,\qquad
  a\|p_{i+1}-p_i\|_1\asymp\delta ,
\]
while
\[
  \Pi_C\sim a^L=\tau^L\ll\tau .
\]
The note explicitly says: "This is not an exact construction. It is the
obstruction."

## Polynomial Scalar Model Actually Tested

For \(L\in\{2,3,4,5\}\), variables are
\[
  \tau,\delta,\widetilde\sigma,\quad
  a_1,\ldots,a_L,\quad d_1,\ldots,d_L ,
\]
where \(a_i\) is the positive thin-chain edge weight and \(d_i\) is the
\(\ell^1\)-row gap paid for by the signed correction on link \(i\).

The extracted necessary constraints are
\[
\begin{aligned}
  &\delta-\tau^2=0,\qquad 0\le \tau\le \tfrac14,\\
  &\widetilde\sigma-\tau\ge0,\qquad
    \widetilde\sigma\le 1+\delta,\\
  &0\le a_i\le 1,\qquad 0\le d_i\le \tau,\qquad
    a_i d_i\le \delta,\quad 1\le i\le L .
\end{aligned}
\]
The path product is
\[
  \Pi_L=\prod_{i=1}^L a_i .
\]

For fixed positive constants \(c,C\), the certificate target is
\[
  F_{L,c,C}:=\Pi_L+C\,L\,\delta-c\,\tau\ge0.
\]

This model is only a necessary scalar shadow of the desired matrix problem.
It does not encode:

- the full hidden/exposedness LP geometry;
- the row-coordinate realization of \(p_i=\sum_j P_{ij}p_j\);
- forced skip edges from exact entrywise idempotence;
- the frame-coordinate left-inverse tax observed by the refuters;
- a specified value of the universal constants \(c,C'\).

Those missing constraints are precisely where the refuter notes say thin
templates snap, so a certificate in the scalar shadow would be meaningful, but
a failure in the scalar shadow does not refute the kernel conjecture.

## Exact Thin Ray

For any \(N\ge4\), set
\[
  \tau=\frac1N,\quad \delta=\frac1{N^2},\quad
  \widetilde\sigma=\frac2N,\quad
  a_i=d_i=\frac1N .
\]
Then all scalar constraints above hold, every link budget is tight
\[
  a_i d_i=\delta,
\]
and
\[
  F_{L,c,C}
  = \frac1{N^L}+\frac{CL}{N^2}-\frac{c}{N}
  = \frac1N\left(N^{1-L}+\frac{CL}{N}-c\right).
\]
For any fixed \(c>0\) and finite \(C\), this is negative for all sufficiently
large \(N\). Thus no SOS/LP certificate of this scalar target can exist at any
degree unless extra matrix/geometric constraints are added.

