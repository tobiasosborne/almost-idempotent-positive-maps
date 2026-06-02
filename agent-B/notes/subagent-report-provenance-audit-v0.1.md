# Subagent report provenance audit v0.1

Scope: `report/PROVENANCE.md` and `report/sections/*.tex`, current filesystem
snapshot. I did not edit `report/`, `agent-a-findings`, or `agent-A`.

Registry hash check: every hash currently listed in the ground-truth registry
matches its path. The failures below are provenance-integrity issues: wrong
source file, missing registered hash, quote not byte-matchable, or status/source
mismatch.

## Findings

1. `thm:effros-stormer`: registry source is not the quoted OCR text.

- Where: `report/PROVENANCE.md:15`, `report/PROVENANCE.md:63`,
  `report/sections/08-discussion.tex:70-76`.
- Problem: registry key `ES` points to
  `agent-B/references/effros-stormer-1979/positive-projections-jordan-structure.txt`
  with matching hash `ee3e9571f483c678`, but that file contains only form-feed
  characters, not the theorem text. The section and ledger actually quote
  `ocr-pages/page-05.txt` and `ocr-pages/page-02.txt`, which are not registered
  or hashed in `PROVENANCE.md`.
- Additional support gap: the "Equivalently, the fixed-point set..." sentence in
  `08-discussion.tex:74-76` is supported by `page-01.txt:21-23` and/or
  `page-06.txt:42-44`, not by the current page-05/page-02 locus.
- Recommended edit: replace or supplement the `ES` registry entry with the OCR
  page files actually used. Hashes I computed:
  `page-01.txt` `b5594fe97fdafae1`, `page-02.txt` `5d8290904cbbef07`,
  `page-05.txt` `80ae5aacf9ce018c`, `page-06.txt` `687a8024feb5ceac`,
  `page-07.txt` `606847efe808170a`. Expand the theorem loc to include the
  fixed-point corollary pages, or remove the equivalence sentence.

2. `def:operators`: Idel does not support "states as positive unital
   functionals."

- Where: `report/PROVENANCE.md:34`, `report/sections/02-preliminaries.tex:7`,
  `report/sections/02-preliminaries.tex:16-17`.
- Problem: the cited Idel line 333 defines a state/density matrix as a positive
  trace-one matrix. It does not define states as positive unital linear
  functionals on `B(H)`. HOS line 374 has an order-unit state-space definition
  for positive functionals, but it is not cited for this row.
- Recommended edit: either change the report definition to density matrices, or
  add a source such as HOS `joa-m.md:374` (or another registered local source)
  for positive unital functionals.

3. `def:positive-map`: VLW `cor:UP-contraction` is not the operator-norm
   contraction used here.

- Where: `report/PROVENANCE.md:35`,
  `report/sections/02-preliminaries.tex:20-32`.
- Problem: VLW lines 655-662 prove contraction for the KMS inner product under
  faithful reference states. The report claims and proves order-unit/operator
  norm contraction on the self-adjoint part. That proof is elementary from
  positivity and unitality, not the cited VLW corollary.
- Recommended edit: keep IDEL for positive/unital definitions, remove the VLW
  contraction provenance from this row/comment, and describe the contraction as
  proved in-line from the order-unit order interval. If VLW is retained, cite it
  only for its KMS-specific statement.

4. `thm:jordan-structure`: V status and "verbatim" quote are misleading.

- Where: `report/PROVENANCE.md:58`,
  `report/sections/07-structure-programme.tex:22-34`.
- Problem: the quote printed in the report is not byte-verbatim from KIT line
  461. The source uses `C^*`, `\calA`, and `\calB`; the report uses `C^{*}`,
  `\mathcal{A}`, and `\mathcal{B}`. Also, the report theorem is an open Jordan
  analogue, not a verified transcription of KIT's C*-theorem, so row status
  `**V**` overstates what is verified.
- Recommended edit: either print the exact source TeX quote or change
  "verbatim" to "notation-harmonized". Change the ledger row status for
  `thm:jordan-structure` to an open/original target, with KIT recorded only as
  the verified model quote.

5. `thm:whitehead` and `prop:aut-compact`: cited facts use an unregistered,
   partly missing extraction path.

- Where: `report/PROVENANCE.md:59-60`,
  `report/sections/07-structure-programme.tex:114-150`.
- Problem: the section comments cite `notes/ingestion-results-2026-06-01.json`,
  but that path does not exist from the project root. The actual file is
  `agent-A/notes/ingestion-results-2026-06-01.json` (hash
  `972bba533931fd3d`), and it is not in the source registry. `CHU` is registered
  only as a PDF and is explicitly not text-verified. `FarautKoranyi1994` has no
  registered local primary source at all.
- Recommended edit: add registered text/extraction sources with hashes and exact
  string-matchable quotes, or downgrade these `(cited)` statements to
  "PDF/unverified" until a local text source is registered.

6. Labeled status remarks are missing ledger/provenance coverage.

- Where: `report/sections/02-preliminaries.tex:54-63`
  (`rem:order-unit-justification`) and
  `report/sections/06-bridge-theorem.tex:538-545` (`rem:bridge-exact`).
- Problem: `rem:order-unit-justification` is marked `(cited)` but has no
  `% PROV:` comment and no ledger row. `rem:bridge-exact` is labeled and cites
  Effros-Stormer but has no status flag, no `% PROV:` comment, and no ledger row.
- Recommended edit: add ledger rows and inline provenance, or change these to
  unlabeled/explanatory text. For `rem:order-unit-justification`, `(proved)` or
  "elementary from spectral theorem/order unit definition" would be more accurate
  unless a source is added.

7. Introduction overclaims that all definitions are source-transcribed and
   byte-matched.

- Where: `report/sections/01-introduction.tex:25-28`.
- Problem: the introduction says the listed definitions, including the
  approximate Jordan algebra, are "transcribed from a named source and matched
  against a local copy." But `def:eps-jb` and `def:eps-jb-iso` are explicitly
  `ORIGINAL (consensus)` in `PROVENANCE.md:47-49`, not external
  source-transcriptions.
- Recommended edit: split the sentence: standard background definitions are
  source-matched; project definitions are marked `ORIGINAL`/consensus and tied
  to internal notes/proofs.

8. Cross-cutting: several internal cited local files have no registry hash.

- Where: examples include `report/PROVENANCE.md:47-49`,
  `report/PROVENANCE.md:61-64` and inline
  comments citing `agent-a-findings`, `agent-b-findings`,
  `agent-A/theory/01-error-reduction.md`, and
  `agent-A/experiments/jordan-coboundary/REPORT.md`.
- Problem: the ledger policy says each entry records a source path plus SHA256.
  These internal sources exist, but are not registered with hashes, so hash
  integrity cannot be checked from `PROVENANCE.md`.
- Recommended edit: add registry rows or per-claim hashes for internal sources.
  Hashes I computed for common ones: `agent-a-findings`
  `42674f8c12e0eab1`, `agent-b-findings` `3350359464d77929`,
  `agent-A/theory/01-error-reduction.md` `facf15f4bee20cc5`,
  `agent-A/experiments/jordan-coboundary/REPORT.md` `7c456f26a8787be0`.

## Non-findings

- Registered hashes for `HOS`, `IDEL`, `KIT`, `VLW`, `CHU`, and `BRIDGE` match
  the values in `PROVENANCE.md`.
- The core bridge theorem source claim is locally supported at the level of
  provenance: `agent-a-findings:173-185` says Agent A verified
  `agent-B/theory/theorem-B-algebraic-bridge.md` line by line, and the bridge
  source hash matches the registry.
