<!--
ROLE: catalogue of all ground-truth reference sources, with citation, local path, role, and integrity hash.
UPDATE POLICY: append a row when a source is added; never rewrite a hash without re-deriving it. Hashes live in checksums.sha256.
TRIGGER: a new reference is brought into refs/, or a definition/lemma needs a source not yet catalogued.
-->

# Reference sources (ground truth)

Single deduplicated reference store. **Payload (PDF/TeX/txt/png/md) is gitignored**; only this
`manifest/` directory is tracked, so the ledger is auditable from a clean checkout (the
`check-provenance` gate *warns*, not fails, when a payload is absent locally).

**Integrity.** Authoritative hashes are in `refs/manifest/checksums.sha256` (51 files).
Verify the whole store:

```bash
cd refs && sha256sum -c manifest/checksums.sha256
```

**Reproducible reconstruction (no specific machine needed).** `refs/manifest/sources.lock.json` +
`scripts/fetch-refs.py` rebuild the gitignored payload on any clone, hash-verifying every byte:

```bash
python3 scripts/fetch-refs.py --status     # what's present / fetchable / cache-only / missing
python3 scripts/fetch-refs.py              # fetch the arXiv-pinned sources (kitaev, vlw) + verify
AIPM_REFS_CACHE=<dir> python3 scripts/fetch-refs.py   # restore bespoke sources from a CAS you control
```

- **Fetch-reproducible (18 files), and thereby GENUINENESS-VERIFIED:** `kitaev-2405.02434` (8),
  `vlw-2604.08380` (6) from arXiv e-prints/PDFs; `baake-sumner-2007.11433/equal-fin.tex` from the arXiv `2007.11433` source; `effros-stormer-1979/positive-projections-jordan-structure.pdf`
  from the official *Mathematica Scandinavica* open-access galley; `baak-moslehian` from arXiv `math/0501158`;
  `blecher-read-2019/...tex` from the arXiv `1905.05836` source. Each was fetched from its AUTHORITATIVE
  origin and byte-matched the recorded hash — a prior agent's wrong/hallucinated file could not match the
  official source, so the hash-match here independently certifies these refs are genuine. `fetch-refs.py`
  reproduces them on any clone; no local copy required.
- **Cache-only (33 files):** the user-stored canonical OCR `hos/*` + `idel-2013/*` (verified genuine: the
  HOS scan's title page is the real Hanche-Olsen–Størmer book and the cited passages are correct standard
  Jordan-algebra mathematics; Idel is verifiably Martin Idel's 2013 TUM/LMU thesis); the locally-generated
  Effros–Størmer OCR page-scans/text + `blecher-neal-*`/`itoh-1991` text extractions (derived from source
  PDFs, not byte-reproducible by fetch); and two source PDFs whose recorded bytes no longer match any
  authoritative origin — `kaup-1984` (mscand re-encoded since) and `chu-russo-1512.03347` (gone from current
  arXiv + Wayback). The last two are NOT byte-verified against an authoritative source and are NOT cited by
  any af proof (chu-russo backs the already-flagged `thm-whitehead`). Seed a content-addressed cache ONCE
  from a populated tree (`fetch-refs.py --populate-cache <dir>`), mirror `<dir>` durably, and any clone
  restores them via `$AIPM_REFS_CACHE`. The cache is just `<sha256>`-named blobs — trivially mirrorable and
  self-verifying.

Definitions/lemmas cite a source by `<source-id>` + locus (e.g. line number); the
`definitions/` and `argument/` shards record the 16-hex prefix of the file's SHA256.

| source-id | citation | local path | role | key byte-match file (sha256, 16hex) |
|---|---|---|---|---|
| `kitaev-2405.02434` | Kitaev, *Almost-idempotent quantum channels and approximate C\*-algebras*, arXiv:2405.02434 | `refs/kitaev-2405.02434/` | the theorem we generalise (model for Layer-1/exponent) | `approximate_algebras.tex` `e7eb512a2ec2438d` |
| `vlw-2604.08380` | van Luijk, Wilming, *Sufficiency and Petz recovery for positive maps*, arXiv:2604.08380 | `refs/vlw-2604.08380/` | the setting (Jordan J\*-algebra invariant for positive maps) | `paper.tex` `3395946df12f6606` |
| `hos` | Hanche-Olsen, Størmer, *Jordan Operator Algebras*, Pitman 1984 | `refs/hos/joa-m.md` (text), `hos-book.pdf` (scan) | **primary ground truth** for JB/Jordan defs + JNW classification | `joa-m.md` `28740e73d547dd46` |
| `effros-stormer-1979` | Effros, Størmer, *Positive projections and Jordan structure in operator algebras*, Math. Scand. 45 (1979) | `refs/effros-stormer-1979/` (pdf + `ocr-pages/`) | exact bridge (positive projection ⇒ JC-algebra) | `ocr-pages/page-05.txt` `80ae5aacf9ce018c` |
| `chu-russo-1512.03347` | Chu, Russo, Jordan cohomology / Whitehead lemmas, arXiv:1512.03347 | `refs/chu-russo-1512.03347/` | H¹=H²=0 for f.d. semisimple Jordan (Layer-1 input) | `chu-russo-1512.03347.pdf` `8597dc5556996e83` |
| `idel-2013` | Idel, *On the structure of positive maps*, 2013 (TUM) | `refs/idel-2013/idel-2013.md` | positive-map structure background | `idel-2013.md` `737cd6d3d82ae588` |
| `blecher-read-2019` | Blecher, Read, *Contractive projections and real positivity* (2019) | `refs/blecher-read-2019/` | contractive-projection theory (factorization) | `contractive-projections-real-positive.tex` `767b69596363d005` |
| `blecher-neal-1905.05836` | Blecher, Neal, arXiv:1905.05836 | `refs/blecher-neal-1905.05836/` | real-positivity projections | `blecher-neal-1905.05836.txt` `e7b34b75aa6578be` |
| `blecher-neal-1508.01530` | Blecher, Neal, *Completely contractive projections on operator algebras*, arXiv:1508.01530 | `refs/blecher-neal-1508.01530/` | contractive-projection theory | `blecher-neal-1508.01530.txt` `06ca238eebee9ba7` |
| `kaup-1984` | Kaup, *Contractive projections on Jordan C\*-algebras* (1984) | `refs/kaup-1984/` | Jordan contractive projections | `contractive-projections-jordan-cstar.pdf` `16c72dafd7e16a86` |
| `baak-moslehian` | Baak, Moslehian, J\*-homomorphism stability | `refs/baak-moslehian/` | local J\*-stability (Layer-1 literature check) | `baak-moslehian-J-star-stability.pdf` `027cffddd2735fbe` |
| `itoh-1991` | Itoh, positive projections, Tokyo 1991 | `refs/itoh-1991/` | positive-projection range structure | `itoh-positive-projections-tokyo1991.txt` `03bd2d3d6ebb2821` |
| `baake-sumner-2007.11433` | Baake, Sumner, *On equal-input and monotone Markov matrices*, arXiv:2007.11433 (J. Appl. Probab. 2022, DOI 10.1017/apr.2021.39) | `refs/baake-sumner-2007.11433/equal-fin.tex` | idempotent Markov-matrix structure — commutative case (`op-classical` / `def-stochastic` / `thm-simplex`) | `equal-fin.tex` `f358c71c066293f8` |

**Provenance fixed (vs prior state):** previously the Kitaev/VLW/PDF payloads were byte-identical
duplicates split across `agent-A/refs` and `agent-B/references`, and HOS/Idel ground truth pointed
at absolute paths under `../af-tests`. Both are resolved: one deduplicated copy per source lives
here, and HOS `joa-m.md` + Idel `idel-2013.md` were copied local from `af-tests/examples3`.
