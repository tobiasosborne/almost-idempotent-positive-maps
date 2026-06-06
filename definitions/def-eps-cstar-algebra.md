---
id: def-eps-cstar-algebra
term: ε-C* algebra
aliases: epsilon-C*-algebra; eps-C*; extended ε-C*-algebra; extended epsilon-C*-algebra
kind: cited
status: locked
source: kitaev-2405.02434
locus: approximate_algebras.tex:407-440 (Def. ε-Banach/ε-C*); 1477-1479 (extended)
sha256: e7eb512a2ec2438d
consensus: transcribed in report sec:exponent (the Kitaev CP target structure); used by lem-cstar-sa-to-epsjb
---

**Statement.** Let $\varepsilon\ge 0$. An *$\varepsilon$-$C^*$ algebra* is a complex Banach space $\mathcal A$
with a bilinear product, a conjugate-linear involution $X\mapsto X^\dagger$, and a unit $I$, satisfying:

- **(ax\_prodnorm)** $\lVert XY\rVert \le (1+\varepsilon)\lVert X\rVert\,\lVert Y\rVert$ — approximate submultiplicativity;
- **(ax\_assoc)** $\lVert (XY)Z-X(YZ)\rVert \le \varepsilon\,\lVert X\rVert\,\lVert Y\rVert\,\lVert Z\rVert$ — **$\varepsilon$-associativity**;
- **(ax\_\*)** $\lVert X^\dagger\rVert=\lVert X\rVert$ and $(XY)^\dagger=Y^\dagger X^\dagger$ — involution (**exact**);
- **(ax\_C\*)** $\lVert X^\dagger X\rVert \ge (1-\varepsilon)\lVert X\rVert^2$ — the $C^*$-identity (lower bound; the
  upper bound $\lVert X^\dagger X\rVert\le(1+\varepsilon)\lVert X\rVert^2$ follows from ax\_prodnorm + ax\_\*);

with the unit satisfying the exact conditions $XI=X$, $IX=X$, $\lVert I\rVert=1$, $I^\dagger=I$ (if specified;
otherwise their $\varepsilon$-approximate forms). An *extended $\varepsilon$-$C^*$ algebra* is a complete
self-adjoint operator space $\mathcal A$ with a multiplication and unit making each $M_n\otimes\mathcal A$ an
$\varepsilon$-$C^*$ algebra.

**Key contrast.** Unlike [[def-eps-jb-algebra]] (where the order, unit, and norm are *exact* and only the
product carries the defect), here even the **norm is only approximately multiplicative** (ax\_prodnorm) and
ax\_C\* is a *norm* lower bound — **not** an order inequality $X^\dagger X\ge -\varepsilon\lVert X\rVert^2 I$.
This is exactly why passing to a JB algebra (`lem-cstar-sa-to-epsjb`) needs the **positivity of squares**
(JB3) supplied separately — from the concrete UCP realisation $\mathcal A=\operatorname{Im}\widetilde F$, not
from these axioms alone.

**Notes / provenance.** Byte-matched to Kitaev
`refs/kitaev-2405.02434/approximate_algebras.tex:407-440` (the $\varepsilon$-Banach / $*\varepsilon$-Banach /
$\varepsilon$-$C^*$ definition) and `:1477-1479` (extended). The conclusion of Kitaev's almost-idempotent
theorem (`th_almost_idemp`, `:2192-2194`) is an extended $O(\eta)$-$C^*$ algebra; the **$O(\eta)$-associativity**
that this carries is the byte-grounded statement at `:2228-2231`. The registry lemma `lem-cstar-sa-to-epsjb`
passes from this structure to an ε-JB algebra ([[def-eps-jb-algebra]]).
