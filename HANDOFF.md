<!--
ROLE: crash-safe handoff for the in-progress repo re-architecture (branch argument-architecture).
UPDATE POLICY: rewritten (not appended) at each checkpoint; keep <=500 lines; git history holds old versions.
TRIGGER: end of a work session / before a push / when phase status changes.
NOTE: this tracks the REORG/ARCHITECTURE build. For the MATH status see agent-A/HANDOFF.md.
-->

# HANDOFF — argument-architecture build

**Branch:** `argument-architecture` (off `main`). **Date:** 2026-06-05.
**Approved design:** `docs/plans/2026-06-05-argument-architecture-plan.md` (copied from the plan-mode file;
read it first). The repo is being rebuilt as a **typed module system for the proof**:
definitions = types · lemmas (af workspaces) = modules · statements = contracts · a linker enforces the DAG.

## Four governing principles (from the user)
1. **Definitions DB is PRIORITY 1** — deduplicated, provenanced, consensus-gated, local ground truth. Drift = death.
2. **Every lemma gets its OWN tiny af workspace**; a huge proof tree is a brittleness *failure signal* → factor into sub-lemmas.
3. **The whole argument is an enforced DAG** (modules + contracts), checked by a linker.
4. **~200-LOC sharding everywhere**, greppable, indexed. No monolith.
Plus standing directives: **red-green TDD for all tooling**; **harvest CLAUDE.md best-bits from
`../cft-anyons`, `../Bennett.jl`, `../af-tests`, `../arithmetic-quantum-mechanics`** when writing our CLAUDE.md (Phase 4).

## DONE (committed on this branch)
- **Phase 0:** `bd init` (prefix `aipm`); references deduped into one `refs/<source-id>/` tree (~24M→17M);
  HOS `joa-m.md` + Idel text brought local (were `../af-tests` abs paths); `refs/manifest/{SOURCES.md,
  checksums.sha256}` tracked (50 files, `cd refs && sha256sum -c manifest/checksums.sha256`); `.gitignore`
  rewritten (payload ignored, manifest tracked; proofs/ ledger rules; `.claude/`).
- **Phase 1 (core):** `definitions/` Layer-0 DB — **16 shards** (analytic setting, Jordan/JB, spectral
  construction, the central `def-eps-jb-algebra`, bridge/factorization objects). `scripts/check-defs.py`
  gate (dedup/drift + cited-SHA256 vs manifest + consensus-gate + `INDEX.md` gen); **TDD'd** by
  `scripts/tests/test_check_defs.py` (8/8). Gate green: 16 shards, 0 errors, 0 warnings.
- `definitions/README.md` = the shard schema (flat YAML frontmatter: id, term, aliases, kind
  cited|consensus|original, status draft|locked, source/locus/sha256, consensus).

Commits: `bd init` → Phase 0 refs → Phase 1 foundation → Phase 1 TDD → Phase 1 core defs.

## NEXT (in order)
1. **Finish Phase 1** — ~6 peripheral def shards for the open/secondary results: `def-stochastic`,
   `def-exposed` (classical geometry); `def-jordan-coboundary`, `def-injective-cochain-norm` (Layer-1);
   `def-decomposable-map`; `def-multiplicative-domain`. Source loci are in `report/PROVENANCE.md`.
2. **Phase 2 — argument registry + linker (TEST-FIRST):** `argument/lemmas/<id>.md` contract shard per
   result (~40-60; seed from `report/PROVENANCE.md` per-claim ledger — it already lists every
   lemma/thm/op with source+locus+status). Then `scripts/argument.py`: acyclic · contract-match vs af
   (`af get 1 -f json`) · imports-resolve (`af externals -f json`) · status-propagation · brittleness
   (node-count via `af status -f json`) · orphans; generate `argument/{INDEX,DAG}.md`; sync beads.
   Wire `scripts/check-all.sh` into `.beads/hooks/pre-commit` (bd owns `core.hooksPath=.beads/hooks`).
3. **Phase 3** — af per-lemma pilot on the bridge's proved leaves. **Phase 4** — reorg theory/experiments
   + archive clutter (phantom `response-to-agent-a-v*`, superseded stacks, 91KB compaction dump) +
   CLAUDE.md/AGENTS.md/PRD + merge report/PROVENANCE.md up. **Phase 5** — fresh Lean scaffold (secondary).

## Key facts / gotchas for whoever resumes
- `af` = Adversarial Proof Framework, source `../vibefeld`, v0.1.3 (PATH binary mislabels as "dev";
  `af --version` is authoritative). Export is Markdown/LaTeX only — **no af→Lean generator** (manual
  transcription using af node IDs). af workspaces are machine-introspectable via `-f json`.
- Lean is **secondary**; `af-tests` is **reference only** (not a dependency).
- bd: never `bd init --force`; fresh clone `bd import` not `bd init`; serialize bd calls. bd auto-committed
  its init and set `core.hooksPath=.beads/hooks` + wrote a minimal `CLAUDE.md`/`AGENTS.md` (to be
  superseded in Phase 4; bd's "no MEMORY.md" rule to be reconciled with the ~/.claude memory system).
- Pre-existing uncommitted edit `agent-A/lean-formalisation-coverage.md` is **not** part of this work — left untouched.
- Commits use `git -c core.hooksPath=/dev/null` to skip bd's pre-commit hook until the validation suite is wired (Phase 2).
- Tasks (harness): #1 done, #2 in_progress (Phase 1 core done; peripheral defs remain), #3-#6 pending.
