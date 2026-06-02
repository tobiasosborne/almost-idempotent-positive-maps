# Subagent Report Exposition/Build Audit v0.1

Scope: read-only audit of `report/` for self-contained exposition, visible
status, theorem/proof/conjecture distinctions, correction markers, stale
generated files, and LaTeX build hygiene.

I did not edit `report/`, `agent-a-findings`, or `agent-A`. During the audit,
`report/README.md`, `report/PROVENANCE.md`, and sections
`02-preliminaries.tex`, `03-jordan-algebras.tex`, `04-spectral-idempotent.tex`,
`05-epsilon-jb.tex`, `06-bridge-theorem.tex`, `07-structure-programme.tex`, and
`08-discussion.tex` changed externally. The findings below use the current
source after those changes.

Reference practices checked:

- `../cft-anyons/PROVENANCE.md`
- `../cft-anyons/CONVENTIONS.md`
- `../arithmetic-quantum-mechanics/report/README.md`
- `../arithmetic-quantum-mechanics/docs/report_mega_review/README.md`

Non-destructive checks run:

- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` in a fresh
  `/tmp/aipm-report-final-clean` copy after deleting generated products in the
  copy only.
- `rg`, `sed`, `nl`, `find`, `stat`, `sha256sum`, and `pdftotext` on report
  sources and generated artifacts.
- `chktex -q -n1 -n8 -n24 -n36 main.tex` and `lacheck main.tex` in the clean
  `/tmp` copy.

## Findings

### 1. Current generated report artifacts are stale

Severity: high for build hygiene.

Current source files have mtimes later than `report/main.pdf`,
`report/main.aux`, `report/main.toc`, `report/main.log`, and
`report/main.fls`. A clean rebuild of the current source in
`/tmp/aipm-report-final-clean` succeeds, but generated outputs differ:

- `report/main.pdf` hash:
  `2176f7046994d0ababc44e879a42544a9160623342a7ff09ce14d2b91b323eb9`
- clean rebuilt `main.pdf` hash:
  `5446fa5fd22f89b0c33362b6bf10d75f1ef72856c184df5665867b781c6bb23b`
- `report/main.pdf` text hash:
  `16a60a53f12a3b79ab3f9702124e9dc4b920ffab114ea082bae7d5db549f24ee`
- clean rebuilt PDF text hash:
  `a1db621609710c63537771b1a9be8b1eea996794d85765af3b791005c0c2a393`
- `report/main.aux` differs from clean rebuilt `main.aux`.
- `report/main.toc` differs from clean rebuilt `main.toc`.
- `report/main.bbl` matches the clean regenerated `main.bbl`.

Action: rebuild `report/main.pdf` after the current source changes, or remove
generated temporary products from `report/` and keep only the intended PDF
artifact. The present PDF does not represent the current source.

### 2. Several rendered `(cited)` claims are not final by the report's own provenance ledger

Severity: high for scientific-practice/status clarity.

`report/README.md:18-21` says every claim or definition needs provenance and
that statements carry `(cited)`, `(proved)`, or `(open)`. `report/README.md:30`
and `report/PROVENANCE.md:67` add that Agent B should independently byte-check
external-source claims before a statement is final.

Several statements are rendered as plain `(cited)` while
`report/PROVENANCE.md` says they are still `I` or `PDF`:

- `report/sections/02-preliminaries.tex:8-17` renders `def:operators` as
  `(cited)`, while `report/PROVENANCE.md:34` is `I`.
- `report/sections/03-jordan-algebras.tex:54-63` renders
  `prop:power-associative` as `(cited)`, while `report/PROVENANCE.md:41` is `I`.
- `report/sections/04-spectral-idempotent.tex:22-35` renders
  `def:spectral-idempotent` as `(cited)`, while `report/PROVENANCE.md:45` is
  `I`.
- `report/sections/07-structure-programme.tex:115-126` renders
  `thm:whitehead` as `(cited)`, while `report/PROVENANCE.md:59` is `PDF`.
- `report/sections/07-structure-programme.tex:144-151` renders
  `prop:aut-compact` as `(cited)`, while `report/PROVENANCE.md:60` is `I`.
- `report/sections/08-discussion.tex:71-77` renders `thm:effros-stormer` as
  `(cited)`, while `report/PROVENANCE.md:63` is `I`.
- `report/sections/08-discussion.tex:117-134` renders `rem:vlw` as `(cited)`,
  while `report/PROVENANCE.md:65` is `I`.

Section 7 now adds a useful explicit provenance flag for `thm:whitehead` and
`prop:aut-compact` at `report/sections/07-structure-programme.tex:159-165`, but
the theorem/proposition headings still display the stronger `(cited)` status.

Action: either complete the Agent B byte-check and promote these rows to `V`, or
render them visibly as `(cited, pending byte-check)` / `(source-extracted,
pending verification)` until the ledger status is final.

### 3. Status taxonomy is inconsistent between README, introduction, and section bodies

Severity: medium.

`report/README.md:21` lists only `(cited)`, `(proved)`, and `(open)`. The
introduction adds `(consensus)` at `report/sections/01-introduction.tex:53-60`,
and section 5 uses it in definitions at
`report/sections/05-epsilon-jb.tex:13-43` and
`report/sections/05-epsilon-jb.tex:67-98`.

This is not just cosmetic: `report/README.md:24` says sections 1-5 are
"cited / consensus", so the README knows about consensus informally but omits it
from the non-negotiable rule.

Action: make the status vocabulary single-source and explicit. Either add
`(consensus)` to README rule 4 and explain that consensus definitions still need
provenance rows, or stop rendering it as a status tag.

### 4. Some claim-bearing remarks still lack visible status or full ledger coverage

Severity: medium.

The report states a strong policy: "Status tags in every statement"
(`report/README.md:21`). Several claim-bearing environments have inline
provenance comments or ledger rows, but no rendered status in the environment
title or first line:

- `report/sections/03-jordan-algebras.tex:37-47`
  (`rem:jordan-identity-form`; ledger row at `report/PROVENANCE.md:40`)
- `report/sections/03-jordan-algebras.tex:139-145`
  (`rem:exceptional`; ledger row at `report/PROVENANCE.md:44`)
- `report/sections/04-spectral-idempotent.tex:112-121`
  (claim-bearing remark on Kitaev's operator and norm independence; no label)
- `report/sections/05-epsilon-jb.tex:46-64`
  (`rem:eps-jb-degeneration`; ledger row at `report/PROVENANCE.md:48`)

The exact bridge remark now has a visible `(cited)` tag at
`report/sections/06-bridge-theorem.tex:539-548`, but it has only an inline
`% PROV:` comment and no `PROVENANCE.md` row. That is acceptable only if the
policy is narrowed to named Definition/Theorem/Proposition/Lemma statements;
it conflicts with the broader README sentence "No claim or definition without a
`PROVENANCE.md` row."

Correction markers are now visible in the source at:

- `report/sections/02-preliminaries.tex:108-112`
- `report/sections/03-jordan-algebras.tex:132-135`
- `report/sections/04-spectral-idempotent.tex:132-136`
- `report/sections/05-epsilon-jb.tex:94-97`
- `report/sections/07-structure-programme.tex:74-77`
- `report/sections/08-discussion.tex:56-59`

Most current correction markers are mirrored in `PROVENANCE.md`, but the
one-dimensional summand correction for `thm:jnw-classification` is not explicit
in the ledger row at `report/PROVENANCE.md:43`; the fuller inline `% PROV:`
comment is present at `report/sections/03-jordan-algebras.tex:137`.

Action: either relax the policy to "named Definition/Theorem/Proposition/Lemma
statements carry status and ledger rows", or add visible status tags and ledger
rows to all claim-bearing remarks. Mirror the JvNW one-dimensional correction in
the ledger row.

### 5. Open targets are still typeset as theorem/proposition environments

Severity: medium for theorem/proof/conjecture clarity.

The report is candid that section 7 is open
(`report/sections/07-structure-programme.tex:9-13`), but the open targets are
still in theorem/proposition environments:

- `report/sections/07-structure-programme.tex:34-46` states the "Jordan
  structure theorem" in a `theorem` environment while marking it `(open)`.
- `report/sections/07-structure-programme.tex:246-254` states
  "Dimension-free error reduction" in a `proposition` environment, then begins
  with "Programme, not a proved theorem".

The tag helps, but the environment still tells the reader to process these as
formal mathematical results. This is weaker than the comparison repositories'
practice of separating established artifacts from active-programme targets.

Action: introduce `conjecture`, `openproblem`, or `programmetarget`
environments and reserve `theorem`/`proposition` for proved or cited results.
At minimum, rename Proposition 7.4 to an Open Problem/Programme Target.

### 6. Section 7 is still not self-contained enough for a no-jargon report

Severity: medium for exposition.

Section 7 introduces a dense chain of specialist terms without local definitions
or a glossary-style paragraph:

- "Jordan frame", "Peirce decomposition", and "coordinatization theorem" at
  `report/sections/07-structure-programme.tex:60-107`.
- "multiplication algebra", "module", "Whitehead lemma", "cocycle", and
  "coboundary" at `report/sections/07-structure-programme.tex:109-141`.
- "cochain", "approximate Jordan 2-cocycle", "coboundary", "contracting
  homotopy", and "splitting operator" at
  `report/sections/07-structure-programme.tex:175-190`.
- "diagonal (Casimir) tensor", "projective tensor norm", "separability
  idempotent", "multiplication algebra", and "Haar-average representation" at
  `report/sections/07-structure-programme.tex:192-243`.

The section is status-honest, and it now flags extraction-level provenance for
two cited inputs, but it is not self-contained for readers who do not already
know Jordan cohomology and Banach tensor-norm jargon.

Action: add a short "Vocabulary for the programme" subsection before
`7.2 The dimension-free obstruction...`, defining these terms at the level
needed for the report. Where a term is only heuristic strategy rather than a
proved construct, say so explicitly.

### 7. Numerical evidence is reported without a visible reproducibility status

Severity: medium.

`report/sections/07-structure-programme.tex:263-299` reports computations of
smallest singular values and exact kernel dimensions, ending with a pointer to
`agent-A/experiments/jordan-coboundary/REPORT.md`. The prose is useful, but the
report's status system does not say whether this evidence is reproduced,
original-unverified, independently checked, or just a lab note.

Action: add a status marker such as `(computational evidence; not theorem)` and
record the experiment artifact in `PROVENANCE.md` or a small reproducibility
ledger. This would match the comparison docs' practice of keeping source maps
and review outputs explicit.

### 8. LaTeX build succeeds but has hyperlink-destination warnings that matter

Severity: medium for PDF navigability.

A clean current-source build succeeds. The final log has no unresolved citation
or reference warnings, but it does retain duplicate PDF destinations:

- `equation.6.26` at `report/sections/06-bridge-theorem.tex:268-275`
- repeated `equation.6.31` around
  `report/sections/06-bridge-theorem.tex:506-510` and after section 7 starts

The likely cause is mixed use of numbered equation environments and manual
`\tag{...}` labels in section 6:

- `report/sections/06-bridge-theorem.tex:197-201`
- `report/sections/06-bridge-theorem.tex:327-330`
- `report/sections/06-bridge-theorem.tex:456-470`
- `report/sections/06-bridge-theorem.tex:506-510`

Action: replace manual equation tags with ordinary numbered labels plus textual
names, or use `\tag*{...}` / hyperref-safe custom tagging so every labeled
display has a unique PDF destination. This matters because cross-reference
clicks may jump to the wrong display.

### 9. LaTeX build has visible overfull boxes

Severity: low to medium.

Persistent overfull boxes in the clean current build:

- `report/sections/07-structure-programme.tex:159-166`: 2.85 pt too wide in
  the new provenance-flag paragraph.
- `report/sections/07-structure-programme.tex:210-214`: 55.75 pt too wide,
  caused by the long monospace path
  `agent-A/theory/01-error-reduction.md`.
- `report/sections/08-discussion.tex:143-164`: 33.75 pt too wide in the status
  table.
- Smaller overfull boxes at `report/sections/04-spectral-idempotent.tex:82-85`,
  `report/sections/07-structure-programme.tex:247-254`, and
  `report/sections/08-discussion.tex:97-101`.

Action: break long paths with `\path{}` / `\url{}` or manual line breaks, and
make the status table use `tabularx` / `p{...}` columns or shorter status text.
The build also reports `LaTeX Warning: 'h' float specifier changed to 'ht'` for
the status table; that is secondary but will go away if the table is made more
flexible.

### 10. Repeated status tags in theorem titles trigger font warnings

Severity: low.

The clean build repeatedly reports:

`LaTeX Font Warning: Font shape 'T1/cmr/m/scit' undefined ... using 'T1/cmr/m/scsl'`

This is caused by `\textsc{...}` status tags inside theorem-like headings, where
`amsthm` sets title text in an italic context.

Action: define a status macro that forces an upright text font, e.g. a
`\status{...}` macro using `\textnormal{\textsc{...}}`, and use it consistently
in theorem titles and first lines.

### 11. LaTeX lints are noisy but mostly secondary

Severity: low.

`chktex` and `lacheck` find many style warnings, mostly expected math style
issues (`x^2`, missing `~` before refs/cites, and quote punctuation). The
warnings that are most worth addressing after the build issues above are:

- `chktex` warning 17 at `report/main.tex:80`, apparently caused by unmatched
  optional-argument parsing earlier in the document; the PDF build succeeds, but
  it is a signal that theorem titles with nested punctuation/macros are hard for
  tooling to parse.
- `lacheck` reports whitespace before punctuation at
  `report/sections/06-bridge-theorem.tex:17`,
  `report/sections/06-bridge-theorem.tex:34`, and
  `report/sections/07-structure-programme.tex:222`.

Action: do not treat these as blockers, but a final typesetting pass should
clean the easy `~`/spacing warnings and check whether the status-tag macro in
finding 10 also reduces the `chktex` false positives.

## Positive notes

- The current source compiles successfully from a clean `/tmp` copy with
  `latexmk`.
- `report/main.bbl` matches the clean regenerated bibliography output.
- The report now has visible "Agent B review correction" markers for the
  cb-norm framing, JvNW one-dimensional summand, spectral idempotent domain,
  `\delta`-isomorphism/order distinction, approximate-frame construction, and
  decomposable-map exponent qualification.
- Section 8's status ledger is useful and should be retained, but it should be
  synchronized with the stronger provenance statuses in `PROVENANCE.md`.
