---
id: thm-matrix-splitting
kind: theorem
contract: (benchmark; re-audit pending) There is a universal C so that for every n and F in {R,C,H}, an exact-adjoint coboundary f=d^1h on J=H_n(F) admits a derivation delta in Der(J) with ||h-delta||<=C||f||_inj, i.e. d^1 has an order-unit right inverse of norm <=C uniformly in n, via fixed diagonal-frame Peirce gauge (||h|_D||<=11||f||), coherent off-sector leakage globalization, and sector-preserving edge-map reconstruction (real-symmetric 60, complex 84/124, quaternionic) by random-triple matching-curvature averaging.
defs: def-jordan-coboundary; def-injective-cochain-norm
deps: prop-direct-sum
status: proved
af: none
provenance: B-MATADJ (matrix-factor-exact-adjoint-splitting-theorem.md); agent-B/notes/fixed-frame-peirce-matrix-reduction.md; agent-B/notes/off-sector-leakage-globalization-theorem.md; report thm:matrix-splitting
owner: B
workspace: proofs/thm-matrix-splitting
---

The hard high-rank case of the exact-adjoint benchmark: a dimension-free order-unit splitting of the
[[def-jordan-coboundary]] on H_n(F), where the rank gap (prop-rank-gap) is real. Three controlled
pieces -- diagonal-frame gauge, off-sector leakage globalization (averaged squared diagonal-sign
commutator, spectral gaps {0,1/2,1,3/2}), and sector reconstruction -- bound the
[[def-injective-cochain-norm]] uniformly in n. Independent re-audit of the matching-reconstruction step
is pending (obs-matrix-audit). Report `thm:matrix-splitting`; theory:
agent-B/notes/fixed-frame-peirce-matrix-reduction.md, agent-B/notes/off-sector-leakage-globalization-theorem.md.
