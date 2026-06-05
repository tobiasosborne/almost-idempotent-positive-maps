---
id: def-jordan-frame
term: Jordan frame
aliases: complete orthogonal idempotents; frame of idempotents; complete system of orthogonal idempotents
kind: cited
status: draft
source: hos
locus: joa-m.md:1522-1523 (2.6.4-2.6.5); 2224 (2.9.4(iii))
sha256: 28740e73d547dd46
consensus: transcribed report sec:programme (Layer-1 vocabulary)
---

**Statement.** A *Jordan frame* in a unital [[def-jordan-algebra]] (typically a [[def-jb-algebra]]) is a
complete system $p_1,\dots,p_k$ of pairwise *orthogonal* idempotents summing to the unit:
$$p_i^2=p_i,\qquad p_i\circ p_j=0\ (i\neq j),\qquad \sum_{i=1}^{k}p_i=1,$$
where $\circ$ is the [[def-jordan-product]] and $p\circ q=0$ is the Jordan orthogonality of idempotents.
The $p_i$ are the Jordan analogue of a resolution of the identity: they induce the
[[def-peirce-decomposition]] $A=\bigoplus_{1\le i\le j\le k}A_{ij}$, $A_{ij}=\{p_i A p_j\}$. A frame is
called *minimal* (or a *complete frame of minimal/primitive idempotents*) when each $p_i$ is a minimal
idempotent; in a finite-dimensional [[def-formally-real]] Jordan algebra every element lies in a maximal
associative subalgebra $\mathbb{R}p_1\oplus\dots\oplus\mathbb{R}p_n$ spanned by such a minimal frame.

**Notes / provenance.** The concept byte-matches HOS: the pairwise-orthogonal-idempotents-with-sum-$1$
data and the orthogonality convention $p\circ q=0$ are 2.6.4-2.6.5 `refs/hos/joa-m.md:1522-1523`, and the
minimal-idempotent (maximal associative subalgebra) refinement is 2.9.4(iii) `joa-m.md:2224`. Status is
**draft**: HOS does not use the *term* "Jordan frame" (it writes "pairwise orthogonal idempotents with
sum 1"); the name "Jordan frame" / "frame of idempotents" is the standard Euclidean-Jordan-algebra
(Faraut-Koranyi) vocabulary adopted here for the Layer-1 structure programme. Lock once A+B sign off on
the term, or re-key to a byte-exact HOS phrasing. Used by the structure-theorem track (registry ids
`op-jordan-structure`, `op-layer1-gap`).
