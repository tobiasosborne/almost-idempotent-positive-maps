# Report Review v0.1

Date: 2026-06-02.

Scope: adversarial Agent B review of `report/` after Agent A produced the
provenanced LaTeX report. User requested that all corrections be in the report
and clearly flagged.

Subagent inputs:

- Math audit: `agent-B/notes/subagent-report-math-audit-v0.1.md`.
- Provenance audit: `agent-B/notes/subagent-report-provenance-audit-v0.1.md`.
- Exposition/build audit:
  `agent-B/notes/subagent-report-exposition-build-audit-v0.1.md`.

## Consensus Status

Agent A v0.5 in `agent-a-findings` says the Layer-2 bridge proof
`agent-B/theory/theorem-B-algebraic-bridge.md` is verified line by line. The
math audit found no local algebraic error in the transcribed Section 6 proof.
Agent B therefore treats the arbitrary-UP algebraic bridge as proved internally
at exponent `1/2`, while keeping Layer 1 and near-positive projection stability
open.

## Integrated Report Corrections

Patched report issues:

- Corrected the finite-dimensional cb-norm remark: positive maps are bounded in
  finite dimension; the problem is failure of positivity under amplification.
- Added the missing one-dimensional simple summand `R` in the
  Jordan-von Neumann-Wigner classification.
- Replaced an inappropriate dagger-preserving statement in the real
  self-adjoint spectral-idempotent section by preservation of `B(H)_sa`.
- Changed spectral estimates to use a small universal threshold `eta0`, not a
  uniform `O(eta)` claim up to all `eta<1/4`.
- Corrected the epsilon-JB isomorphism definition: it is algebraic/normed, not
  automatically an approximate order-isomorphism.
- Clarified that the spectral idempotent is a map-level idempotent and does not
  provide Layer-1 idempotent elements/Jordan frames.
- Downgraded the global averaging route to a candidate mechanism; the
  order-unit-norm contracting homotopy remains open.
- Tightened the exponent discussion: `O(eta)` belongs to UCP/cb or compatible
  lifted-dilation settings; decomposable `O(eta)` is still conjectural without
  compatible component control.
- Distinguished channel targets (special JC/JB) from the abstract Layer-1
  target, which may include exceptional finite-dimensional JB algebras.
- Fixed composition notation in Section 8 (`rho \circ Phi`,
  `Psi_0 \circ tau`) and removed misleading `sgn` phrasing.

All substantive corrections are visibly marked in the report by
`Agent B review correction` or `Agent B review provenance flag` paragraphs.

## Provenance Corrections

Patched provenance issues:

- Registered the actual Effros-Stormer OCR page files (`ES-P01`, `ES-P02`,
  `ES-P05`, `ES-P06`) instead of the form-feed-only aggregate OCR file.
- Added HOS line 374 for state functionals on order-unit spaces.
- Removed misleading VLW provenance for order-unit norm contraction; that
  contraction is proved inline from positivity and unitality.
- Registered hashed internal/extraction sources (`A-FIND`, `A-INGEST`, `A-ER`,
  `A-JCOB`, `B-ROUND`) and avoided using live `agent-b-findings` as a report
  ground-truth source.
- Promoted line-checked HOS/KIT/VLW/ES rows to `V`.
- Marked Whitehead and compactness facts as `EXTRACT`/`PDF` until primary text
  byte-check is completed.

## Build Status

`cd report && make` succeeds. `report/main.pdf` was rebuilt after the source
edits and is current. The duplicate PDF-destination warnings from manual
equation tags were fixed by replacing custom tags with textual labels inside
the displays. The theorem-title font warnings were fixed by introducing and
using `\status{...}`.

Remaining build issues are minor typesetting only:

- one 3.7pt overfull line in the spectral-idempotent binomial-series proof;
- one harmless underfull line in the status table.

## Remaining Review Obligations

- Independently extract/byte-match the Chu-Russo Whitehead statements from the
  local PDF or another local primary text source.
- Register a primary local source for the Faraut-Koranyi/Euclidean-Jordan
  compactness statement, or keep it explicitly extraction-level.
- Continue mathematical work on the two open engines: dimension-free Layer 1
  order-unit stability and near-positive projection stability/global
  exposed-hull lemma.
