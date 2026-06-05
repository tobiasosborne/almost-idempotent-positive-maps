# Subagent Schur Residual Audit v0.1

Date: 2026-06-05.

Source: sidecar agent Ramanujan, read-only audit.

This memo records an independent audit of the residual Schur multiplier target
from `agent-B/notes/sector-preserving-schur-residual.md` and
`agent-B/notes/pointwise-schur-curvature-caveat.md`.

## Exact Real Formulation

For

```text
J=H_n(R)
```

and symmetric edge weights `m_ij=m_ji`, `m_ii=0`, define

```text
M_m(x)_ij=m_ij x_ij        (i != j),
M_m(x)_ii=0.
```

The desired residual estimate is

```text
||M_m||_{S_infty^sa -> S_infty^sa} <= C ||D_m||_inj,
```

where

```text
D_m(x,y)=x o M_m(y)+M_m(x) o y-M_m(x o y).
```

Coordinate formulas:

```text
(D_m(x,y))_ik
 = (1/2) sum_j (m_ij+m_jk-m_ik)(x_ij y_jk+y_ij x_jk)
        for i != k,
```

and

```text
(D_m(x,y))_ii = 2 sum_{j != i} m_ij x_ij y_ij.
```

Thus the off-diagonal part is a symmetrized bilinear Schur multiplier with
three-index symbol

```text
kappa(i,j,k)=m_ij+m_jk-m_ik,
```

plus the diagonal square-detection terms.

## Haagerup Route And Its Gap

The linear Schur multiplier theorem identifies the Schur multiplier norm with
the Haagerup/Grothendieck factorization norm:

```text
||M_m|| = gamma_2(m),
```

the infimum of

```text
sup_i ||xi_i|| sup_j ||eta_j||
```

over factorizations `m_ij=<xi_i,eta_j>`.

A plausible completely bounded route is:

1. fix a base vertex `p`;
2. write

```text
m_ik=m_ip+m_pk-kappa(i,p,k);
```

3. control the row/column terms by `sup |m_ij|`, hence by the square part of
   `D_m`;
4. control the slice `kappa(i,p,k)` by the completely bounded bilinear Schur
   norm, using extended Haagerup tensor products.

This suggests a cb-version:

```text
||M_m|| <= C ||D_m||_{cb-bilin}.
```

But it does not prove Agent B's target, which uses the ordinary bilinear
injective norm. Extracting one middle slice `j=p` as a full Schur multiplier
is precisely an amplification step; scalar inputs through a fixed middle
vertex only see rank-one products.

Therefore the current Haagerup route leaves a real ordinary-vs-cb gap.

## Stress Tests

No counterexample was found to

```text
||M_m|| <= C ||D_m||_inj.
```

The serious stress families remain logarithmic Schur multipliers:

```text
m_ij=i sign(i-j)           complex skew connection,
m_ij=sign(i+j-n-1)         real symmetric Hankel analogue.
```

Their Schur multiplier norms grow like the triangular projection, hence like
`log n`; see Kwapien--Pelczynski, "The main triangle projection in matrix
spaces and its applications", Studia Mathematica 34 (1970), 43-67:

```text
https://eudml.org/doc/217431
```

These examples rule out pointwise curvature arguments. They are not currently
counterexamples to the full residual estimate: local tests suggest
`||D_m||` grows logarithmically too.

## Verdict

The residual Schur estimate remains plausible but open. A proof via standard
Haagerup factorization currently gives only a cb-bilinear target unless one
adds a new argument converting ordinary bilinear defect norm into the Schur
slice control needed for `gamma_2(m)`.
