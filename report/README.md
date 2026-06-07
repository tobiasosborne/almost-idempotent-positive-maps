# Report: Almost-idempotent positive maps and approximate Jordan algebras

A self-contained, fully provenanced mathematical report on the positive-map /
Jordan-algebra generalisation of Kitaev's almost-idempotent-channels theorem.

## Build
```
cd report && make                         # -> main.pdf  (needs pdflatex + latexmk)
python3 ../scripts/gen-dag-figure.py      # regenerate figures/dag.pdf when the registry changes (needs graphviz)
```

## Structure
- `main.tex` — preamble (fixed macros + theorem environments) and `\input` of each section.
- `sections/NN-*.tex` — one file per section. Notation is fixed by `main.tex`; sections never redefine macros.
- `references.bib` — bibliography (cited sources link out to arXiv / journal open access where a verified public URL exists).
- `figures/dag.{dot,pdf}` — the argument dependency graph (`fig:dag`), generated from `argument/lemmas/` by `scripts/gen-dag-figure.py`; node colour = status (green = af-validated). Committed artifact, like `main.pdf`.
- `PROVENANCE.md` — **audit ledger**. Every Definition/Theorem and every labelled status-carrying Lemma/Proposition/Remark has a row: report label, source key, source location, internal proof or source locus, harmonisation note. Source files are registered with SHA256 at top.

## Provenance rules (non-negotiable)
1. No named claim or definition without a `PROVENANCE.md` row.
2. External-source rows must be byte-checkable against a local ground-truth file; internal rows must point to a hashed proof, consensus, or experiment file.
3. Ground truth: Hanche-Olsen–Størmer (`HOS`, Jordan/JB definitions), Kitaev TeX (`KIT`), van Luijk–Wilming TeX (`VLW`), Effros–Størmer OCR page files (`ES-Pxx`), Chu–Russo (`CHU`), Idel (`IDEL`), and hashed internal project files. Extraction-level rows are explicitly flagged.
4. Status tags in named statements: `(cited)`, `(proved)`, `(consensus)`, `(open)`.

## Status of contents
- §1–§5: definitions and the spectral idempotent (cited / consensus).
- §6: the bridge theorem — **complete proof** (Agent B; verified line-by-line by Agent A).
- §7: the structure-theory programme — **open**, with strategy and the current dimension-free obstruction.
- §8: status ledger and open problems.

## Verification workflow
Authored by section subagents (provenanced), then **adversarially verified with Agent B**: B checks every source-locus match and every derivation step. Disagreements are resolved in the findings files before a statement is marked `(proved)`.
