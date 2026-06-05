---
id: def-peirce-decomposition
term: Peirce decomposition
aliases: Peirce spaces; Peirce projection; Peirce components; Peirce eigenspaces
kind: cited
status: locked
source: hos
locus: joa-m.md:1479-1525 (2.6.2, 2.6.4-2.6.5)
sha256: 28740e73d547dd46
consensus: transcribed report sec:programme (Layer-1 vocabulary)
---

**Statement.** Let $A$ be a unital [[def-jordan-algebra]] and $p$ an idempotent ($p^2=p$), with
$p^{\perp}=1-p$. Let $T_p$ denote the multiplication operator $T_p\colon a\mapsto p\circ a$ (the
[[def-jordan-product]] by $p$) and $U_p$ the quadratic representation. Since
$T_p=U_p+\tfrac12(\iota-U_p-U_{p^{\perp}})+0\cdot U_{p^{\perp}}$ writes $T_p$ as a combination of three
mutually orthogonal idempotent maps summing to $1$, $T_p$ has eigenvalues $1,\tfrac12,0$, giving the
vector-space decomposition
$$A=A_1\oplus A_{1/2}\oplus A_0,$$
where $A_i$ is the eigenspace of $T_p$ for eigenvalue $i$ ($i=0,\tfrac12,1$). This is the *Peirce
decomposition* of $A$ with respect to $p$; the projections onto $A_1,A_{1/2},A_0$ are
$U_p,\;2U_{p,p^{\perp}},\;U_{p^{\perp}}$ respectively. More generally, for pairwise *orthogonal*
idempotents $p_1,\dots,p_n$ (i.e. $p_i\circ p_j=0$ for $i\neq j$) with sum $1$, setting
$A_{ij}=\{p_i A p_j\}=p_i A p_j+p_j A p_i$ gives the *Peirce decomposition with respect to*
$p_1,\dots,p_n$,
$$A=\bigoplus_{1\le i\le j\le n}A_{ij},$$
with the multiplication table $A_{ij}\circ A_{kl}=0$ if $\{i,j\}\cap\{k,l\}=\emptyset$,
$A_{ij}\circ A_{kj}\subseteq A_{ik}$ ($i,j,k$ distinct), $A_{ij}\circ A_{ij}\subseteq A_{ii}+A_{jj}$,
and $A_{ii}\circ A_{ii}\subseteq A_{ii}$.

**Notes / provenance.** Byte-matched to HOS 2.6.2, 2.6.4 and 2.6.5 (the named "Peirce decomposition")
`refs/hos/joa-m.md:1479-1525`. The single-idempotent eigenspace decomposition is 2.6.2 (the term
"Peirce decomposition" is introduced at line 1491); the several-orthogonal-idempotent generalization and
its multiplication table is the Theorem 2.6.5, with the orthogonality convention $p\circ q=0$ fixed in
2.6.4. The orthogonal idempotents $p_1,\dots,p_n$ with sum $1$ are a [[def-jordan-frame]]; the
multiplication operator $T_p$ uses the [[def-jordan-product]] $\circ$. This is Layer-1 coordinatization
vocabulary used by the structure-theorem track (registry ids `op-jordan-structure`, `op-layer1-gap`).
