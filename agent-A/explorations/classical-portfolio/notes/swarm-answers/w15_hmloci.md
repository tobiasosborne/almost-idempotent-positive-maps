# w15_hmloci — H-M loci byte-pin for the delta=0 anchor (codex, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w15_hmloci/brief.md. Orchestrator spot-check: both excerpts grep -F verified.

VERDICT: PINNED for the `kernel-conjecture.tex` delta=0 anchor as used. Caveat: H-M does not literally state the row-vertex/“visible” conclusion or a separate “extremal idempotents” claim; those are derived from Theorem 1.16’s block form.

I kept H-M verbatim excerpts short because the source is copyrighted; the excerpts below were `grep -F` verified against the local `.txt`.

| Anchor claim | H-M locus and grep-verified excerpt | Mismatch note |
|---|---|---|
| Finite stochastic idempotents have recurrent equal-input blocks | [hognas-mukherjea-2011.txt](/home/tobias/Projects/almost-idempotent-positive-maps/refs/hognas-mukherjea-2011/hognas-mukherjea-2011.txt:2767), lines 2767-2777. Excerpt: “identical positive rows” | This exactly covers finite `d x d` row-stochastic idempotents. |
| Transient rows are proportional blockwise, hence mixtures of recurrent rows | Same theorem, lines 2770-2777. Excerpts/formula: `Pij/Pjj = Pih/Pjh` for `i in Tc`, `j,h in Cs`; “Tr is empty” | H-M states ratio/proportionality, not the convex-mixture sentence. Mixture follows because columns in `Tc` vanish and rows sum to 1. |
| Visible/extreme row points are the recurrent block row distributions | Same theorem, lines 2768-2777. Excerpt: “proportional with row sum 1, hence equal” | H-M does not mention `visible vertices`. This is a convex-geometric consequence: recurrent block row distributions have disjoint supports; transient rows lie in their convex hull. |
| Proof backing for the finite nonnegative basis theorem | Theorem 1.11 statement: lines 2225-2244; proof pointer: lines 2967-2972; proof via Theorem 1.18: lines 3079-3210. Excerpt: “rank 1 idempotent matrix” | Theorem 1.11 is stated in finite form, then proved later through the countable nonnegative case. |

**Specialization Gap**

H-M covers the exact finite stochastic-matrix case directly by Theorem 1.16. No specialization from the compact-semigroup/idempotent-probability-measure theorem is needed.

The specialization actually used inside H-M is: stochastic matrix definition at lines 2745-2749; use Theorem 1.11’s nonnegative idempotent basis, lines 2225-2244; then Theorem 1.16 proves `Tr` is empty and recurrent proportional rows become equal because row sums are 1, lines 2776-2777. The broader idempotent probability measure/Rees product result is Theorem 2.2, lines 3965-3979 with proof lines 3982-4117, but it is not the clean source for this finite Markov anchor.

**Replacement LaTeX**

```latex
\item \textbf{The $\delta=0$ anchor.} At $\delta=0$ both conjectures hold by the
finite stochastic-idempotent normal form of H\"ogn\"as--Mukherjea,
\emph{Probability Measures on Semigroups}, Thm.~1.16; local extraction
\texttt{refs/hognas-mukherjea-2011/hognas-mukherjea-2011.txt:2767--2777}
(extraction-level provenance: byte-checked against the \texttt{pdftotext}
output, not against PDF bytes). In H--M notation a stochastic idempotent
has a basis $\{T_c,C_1,\ldots,C_k\}$; each $C_s\times C_s$ block has one
positive probability row, off-diagonal recurrent blocks vanish, and the
ratio identity for $i\in T_c$ gives $P_{i,C_s}=\alpha_{is}\pi_s$. Since
columns in $T_c$ are zero and rows sum to one, $\alpha_{is}\ge0$ and
$\sum_s\alpha_{is}=1$. Hence the geometrically distinct row vertices are
exactly the recurrent equal-input block rows $\pi_s$, and every transient
row lies in their convex hull. The proof source is H--M Theorem~1.11
(statement \texttt{:2225--2244}; proof via Theorem~1.18,
\texttt{:3079--3210}), not merely the Baake--Sumner reformulation.
```

Calibrated `P(every quoted excerpt byte-matches under grep -F)`: `0.995`. Remaining risk is only extraction-tier provenance versus PDF bytes, not the `.txt` matches.