<!--
ROLE: append-only narrative log of work sessions on the argument-architecture rebuild.
UPDATE POLICY: append a dated section per session; never rewrite past entries. Task backlog lives in beads (bd ready); orientation in HANDOFF.md.
TRIGGER: end of a work session.
-->

# Worklog — argument-architecture rebuild

## 2026-06-05 — Phases 0–2(core): definitions DB, linker, validation suite

Rebuilt the repo as a typed module system for the proof (per the 4 user principles +
`docs/plans/2026-06-05-argument-architecture-plan.md`). Branch `argument-architecture`, pushed.

**Done**
- **Phase 0:** `bd init` (prefix `aipm`); deduped all references into one `refs/<source-id>/` tree
  (~24M→17M; Kitaev/VLW/PDFs were byte-identical dupes across agent-A/agent-B); HOS `joa-m.md` + Idel
  text copied local (were `../af-tests` abs paths); `refs/manifest/{SOURCES.md,checksums.sha256}` tracked
  (50 files, `sha256sum -c`-verifiable); rewrote `.gitignore` (payload ignored, manifest tracked).
- **Phase 1 (Definitions DB, Priority 1):** 22 shards under `definitions/`; `scripts/check-defs.py` gate
  (dedup/drift, cited-SHA256 vs manifest, consensus-gate, INDEX gen); TDD'd (`tests/test_check_defs.py`,
  8/8). 2 VLW-cited defs left `draft` (byte-check pending → `aipm-9ho`).
- **Phase 2 (core):** `argument/` registry schema + `scripts/argument.py` linker (acyclic · imports ·
  contract-match-vs-af · status-propagation w/ ready/blocked · brittleness · orphans), built **test-first**
  (`tests/test_argument.py`, 19/19 — went red then green; one red was a test-data bug, fixed). Seeded the
  bridge's proved 5-node DAG; generates `argument/{INDEX,DAG}.md`. `scripts/check-all.sh` wired into
  `.beads/hooks/pre-commit` and proven to run on commit.
- Seeded **14 beads issues** (the remaining backlog + open-math frontier); `bd ready` is the next-agent queue.

**Key decisions**
- af = canonical NL-proof record (source `../vibefeld` v0.1.3); Lean is **secondary**, fresh, af-tests
  **reference only** (no dependency); no af→Lean generator (manual transcription via node IDs).
- CI = local pre-commit validation suite (no GitHub Actions), per house style + user intent.
- Definition shard kinds cited|consensus|original; status draft|locked; contracts are single-source-of-truth
  strings the af workspace root + dependents must both match (anti-drift).

**Open threads / gotchas**
- `bd` ids are random suffixes (`aipm-0sg`), not sequential. Never `bd init --force`; serialize bd calls.
- bd wrote a minimal `CLAUDE.md`/`AGENTS.md` and asserts "no MEMORY.md" — reconcile in Phase 4 (`aipm-ond`)
  with the ~/.claude memory system (memory currently holds project notes + the TDD/harvest feedback).
- Pre-existing uncommitted `agent-A/lean-formalisation-coverage.md` left untouched (not this work).
- Registry currently has only the 5 bridge shards; ~35–55 results remain (`aipm-w2b`, harvest from
  `report/PROVENANCE.md`).
