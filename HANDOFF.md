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
- `definitions/README.md` = the shard schema. **Phase 1 COMPLETE: 22 def shards** (+classical
  stochastic/exposed, Layer-1 jordan-coboundary/injective-cochain-norm, decomposable-map +
  multiplicative-domain — last two `draft`, byte-check pending). Gate: 22 shards, 0 errors, 2 warns.
- **Phase 2 (core) DONE:** `argument/` Layer-1 registry — README schema + `scripts/argument.py` linker
  (acyclic · imports · contract-match-vs-af · status-propagation w/ ready/blocked · brittleness · orphans),
  built TEST-FIRST (`scripts/tests/test_argument.py`, 19/19). Seeded the bridge's proved 5-node DAG
  (lem-P-properties → first-insertion/square-hole → prop-bridge-jordan → thm-bridge); generates
  `argument/{INDEX,DAG}.md`. `scripts/check-all.sh` (defs+linker+tests) wired into
  `.beads/hooks/pre-commit` — **proven to run on commit** (bd hook + suite both green).

Commits: bd init → Phase0 refs → Phase1 (foundation/TDD/core/peripheral) → plan+HANDOFF → Phase2 linker.

## NEXT (in order)
1. **Phase 2b — seed the rest of the registry (~35-55 shards):** one `argument/lemmas/<id>.md` per
   remaining result, harvested from `report/PROVENANCE.md` per-claim ledger (every lemma/thm/op with
   source+locus+status) + `theory/`. Then full **beads sync** (currently a dry-run stub in argument.py;
   serialize bd calls, persist a lemma↔bd-id map). Re-run `python3 scripts/argument.py --check --generate`.
2. **Phase 3 — af per-lemma pilot** on the bridge's proved leaves (`lem-P-properties` is the current
   ready frontier): `af init proofs/<id>`, transcribe to trivial steps, A=prover/B=verifier, advance the
   shard `af: none→seeded→validated`; add `af replay --verify` per `proofs/*` to check-all.sh.
3. **Phase 4 — reorg + hygiene:** consolidate `theory/`+`experiments/`, archive clutter (phantom
   `response-to-agent-a-v*`, superseded stacks, 91KB compaction dump); author CLAUDE.md==AGENTS.md + PRD
   — **harvest best-bits from `../cft-anyons`, `../Bennett.jl`, `../af-tests`, `../arithmetic-quantum-mechanics`**
   (user directive); add `check-provenance.py` + report `latexmk` to check-all.sh; merge `report/PROVENANCE.md` up.
4. **Phase 5 — fresh Lean scaffold** (secondary; af-tests reference only).

## Key facts / gotchas for whoever resumes
- `af` = Adversarial Proof Framework, source `../vibefeld`, v0.1.3 (PATH binary mislabels as "dev";
  `af --version` is authoritative). Export is Markdown/LaTeX only — **no af→Lean generator** (manual
  transcription using af node IDs). af workspaces are machine-introspectable via `-f json`.
- Lean is **secondary**; `af-tests` is **reference only** (not a dependency).
- bd: never `bd init --force`; fresh clone `bd import` not `bd init`; serialize bd calls. bd auto-committed
  its init and set `core.hooksPath=.beads/hooks` + wrote a minimal `CLAUDE.md`/`AGENTS.md` (to be
  superseded in Phase 4; bd's "no MEMORY.md" rule to be reconciled with the ~/.claude memory system).
- Pre-existing uncommitted edit `agent-A/lean-formalisation-coverage.md` is **not** part of this work — left untouched.
- The validation suite is now LIVE in the pre-commit hook (don't use the `core.hooksPath=/dev/null`
  override anymore — let `check-all.sh` run). It currently checks defs + linker + tooling tests;
  provenance/report/af-replay checks are TODO in `scripts/check-all.sh`.
- Tasks (harness): #1,#2 done; #3 (Phase 2) core done, seeding+beads-sync remain; #4-#6 pending.
