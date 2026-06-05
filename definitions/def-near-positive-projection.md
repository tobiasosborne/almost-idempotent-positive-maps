---
id: def-near-positive-projection
term: near-positive projection
aliases: δ-positive unital idempotent; near-positive idempotent
kind: original
status: locked
source: internal
locus: report sec:factorization (op:npps); theorem-stack-v0.3.md (Theorem 3 hypothesis); near-positive-projection-stability-program.md
sha256: -
consensus: A+B; B's factorization program, formulation agreed (A-FIND §11)
---

**Statement.** A *near-positive projection* is a linear map $R\colon B(\mathcal H)_{\mathrm{sa}}\to
B(\mathcal H)_{\mathrm{sa}}$ that is an exact idempotent and unital, $R^2=R$ and $R(\mathbf 1)=\mathbf 1$,
with $\lVert R\rVert\le 1+\delta$, and *$\delta$-positive*: for $0\le x$ with $\lVert x\rVert\le1$ one has
$R(x)\ge-\delta\,\mathbf 1$, for a small parameter $\delta\in[0,\delta_0)$.

The [[def-spectral-idempotent]] $P=\theta(2\Phi-\mathbf 1)$ is the motivating example, with $\delta=O(\eta)$;
but $P$ need **not** be a genuinely positive map. *Near-positive projection stability* (the open hypothesis
`op:npps`) asks whether every near-positive projection is within $C\sqrt\delta$ (operator norm) of a genuine
*positive* unital idempotent $E$; the $\sqrt{}$ exponent is sharp (Hume's $3\times3$ family).

**Notes / provenance.** Project-original object central to the exact unital-positive factorization route
(B's program, `near-positive-projection-stability-program.md`; `theorem-stack-v0.3.md` Theorem 3 hypothesis;
report `op:npps`). Formulation agreed with A (`agent-a-findings §11`). The *stability* statement is an open
registry problem, not part of this definition. Contrast [[def-spectral-idempotent]] (which is only
$\delta$-positive) with a genuine positive idempotent (Effros–Størmer input).
