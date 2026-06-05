---
id: obs-matrix-audit
kind: obstruction
contract: The sector-reconstruction step of thm-matrix-splitting needs independent re-audit: an earlier Haagerup/base-vertex route had a genuine ordinary-vs-completely-bounded gap (a fixed middle slice is an amplification), and the final random-triple matching-curvature route -- designed to avoid that gap -- has not been re-verified; the sharpest stress test (a logarithmic Schur-multiplier family) appears to have logarithmically-growing coboundary too, so it is not a counterexample, but the closure is recorded as an Agent-B claim only.
defs: def-injective-cochain-norm
deps: thm-matrix-splitting
status: obstruction
af: none
provenance: agent-B/notes/subagent-schur-residual-audit-v0.1.md; agent-B/notes/pointwise-schur-curvature-caveat.md; report rem:matrix-audit (beads aipm-36d)
owner: B
workspace: proofs/obs-matrix-audit
---

The verification caveat on thm-matrix-splitting: the matching-curvature closure of the
sector-reconstruction step is not yet independently re-audited. The earlier Haagerup factorization
route gives only a cb-bilinear target (ordinary-vs-cb gap); pointwise edge/triangle-curvature bounds
cannot control the residual Schur-multiplier [[def-injective-cochain-norm]] (the Kwapien-Pelczynski
triangular projection grows logarithmically). No counterexample found; the full Jordan defect appears
to grow logarithmically as well. Report `rem:matrix-audit`; theory:
agent-B/notes/subagent-schur-residual-audit-v0.1.md, agent-B/notes/pointwise-schur-curvature-caveat.md.
