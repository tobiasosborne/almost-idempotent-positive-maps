---
id: def-positive-unital-map
term: positive unital map
aliases: positive map; unital map; UP map; Φ
kind: cited
status: locked
source: idel-2013
locus: idel-2013.md:347-348
sha256: 737cd6d3d82ae588
consensus: transcribed report sec:prelim (def:positive-map); contraction proved inline
---

**Statement.** A linear map $\Phi:B(\mathcal H)\to B(\mathcal H)$ is *positive* if $\Phi(a)\ge0$
whenever $a\ge0$; a positive map is automatically self-adjointness-preserving
($\Phi(a^*)=\Phi(a)^*$), so it restricts to a real-linear $\Phi:B(\mathcal H)_{\mathrm{sa}}\to
B(\mathcal H)_{\mathrm{sa}}$. It is *unital* if $\Phi(\mathbf 1)=\mathbf 1$. A *positive unital map* is a
contraction on the self-adjoint part: $-\lVert a\rVert\mathbf 1\le a\le\lVert a\rVert\mathbf 1$ gives
$-\lVert a\rVert\mathbf 1\le\Phi(a)\le\lVert a\rVert\mathbf 1$, so $\lVert\Phi\rVert=1$ on
$B(\mathcal H)_{\mathrm{sa}}$.

**Notes / provenance.** Idel `refs/idel-2013/idel-2013.md:347-348` ("positive if $\forall A\ge0$,
$T(A)\ge0$"; "unital if $T(\mathbf 1)=\mathbf 1$"); order-unit-norm contraction proved inline in report
sec:prelim. **Merely positive** (not 2-positive / CP) is the whole point: it gives Kadison but not
Schwarz, forcing Jordan structure. Subject of [[def-almost-idempotent]], [[def-spectral-idempotent]].
