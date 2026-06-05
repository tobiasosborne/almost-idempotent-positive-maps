---
id: obs-regular-polygon
kind: obstruction
contract: A dense regular polygon makes pointwise vertex-deletion accumulate (every vertex O(sqrt delta)-redundant, none well-exposed at the sqrt(delta) scale), so a pointwise exposed/redundant dichotomy is insufficient for op-exposed-hull; but regular polygons cannot arise as a near-positive signed affine retraction's row polytope, since every dihedrally-symmetric affine coordinate system on one has vertex negative mass >= sqrt(3)/pi - 1/3 ~= 0.218, bounded away from 0.
defs: def-stochastic; def-exposed
deps:
status: proved
af: none
provenance: regular-polygon-retraction-obstruction.md; simultaneous-skeleton-reduction.md (warning); report rem:regular-polygon
owner: B
workspace: proofs/obs-regular-polygon
---

The regular polygon is a logical warning about quantifier structure (it forces the global formulation of
op-exposed-hull) but is not a genuine counterexample: it cannot occur as a small-defect retraction's row
polytope. Uses [[def-stochastic]], [[def-exposed]]. Report `rem:regular-polygon` (status proved). Theory:
agent-B/notes/regular-polygon-retraction-obstruction.md, simultaneous-skeleton-reduction.md (Warning).
