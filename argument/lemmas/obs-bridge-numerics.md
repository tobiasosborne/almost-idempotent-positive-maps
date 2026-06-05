---
id: obs-bridge-numerics
kind: obstruction
contract: Numerically the classical R^3 absorbing/transient family gives ||P(h_{r,s}^2)||/eta -> 32/27 = 1.1852 (and ||P(h_{r,s}^2)||/sqrt eta -> 0), so the square-hole null bound is Theta(eta), not O(eta^2): the bridge exponent cannot be improved by this route (qubit Bloch-form holes vanish identically).
defs: def-square-hole
deps: lem-square-hole-almost-positive
status: proved
af: none
provenance: B-NULL (null-ideal-probe/REPORT.md); report rem:bridge-numerics
owner: B
workspace: proofs/obs-bridge-numerics
---

Numerical evidence pinning the square-hole rate at Theta(eta) with sharp asymptotic constant 32/27, ruling
out an O(eta^2) improvement; the qubit case is trivial (h_{r,s}=0). Uses [[def-square-hole]]. Report
`rem:bridge-numerics`; source agent-B/experiments/null-ideal-probe/REPORT.md.
