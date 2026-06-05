<!--
ROLE: crash-safe handoff for the in-progress repo re-architecture (branch argument-architecture).
UPDATE POLICY: rewritten (not appended) at each checkpoint; keep <=500 lines; git history holds old versions.
TRIGGER: end of a work session / before a push / when phase status changes.
NOTE: this tracks the REORG/ARCHITECTURE build. For the MATH status see agent-A/HANDOFF.md.
-->

# HANDOFF — argument-architecture build

> ## START HERE (next agent)
> 1. `git checkout argument-architecture` (this branch; pushed to origin).
> 2. Read, in order: **this file** → `docs/plans/2026-06-05-argument-architecture-plan.md` (the approved
>    design) → `definitions/INDEX.md` + `argument/INDEX.md` + `argument/DAG.md` (the current state).
> 3. **What to do next is in beads:** `bd ready` lists the unblocked tasks. Phase 2b shard-seeding
>    (`aipm-w2b`) is now **DONE** — the registry holds **56 results** (`argument/INDEX.md`). The P1 starts
>    remaining are: **Phase 3 af pilot** on `lem-P-properties` (`aipm-0sg`, the ready frontier),
>    **Phase 4 CLAUDE.md** (`aipm-ond`), and **Phase 2b beads-sync** (`aipm-wfp`, replace the dry-run stub).
>    Recommended next = Phase 3 af pilot. Claim with `bd update <id> --status in_progress`; close with
>    `bd close <id> --reason "…"`.
> 4. Sanity-check the build: `sh scripts/check-all.sh` must print `[check-all] OK`. The validation suite
>    is LIVE in the pre-commit hook — commit normally (do **not** use `core.hooksPath=/dev/null` anymore).
> 5. Exact recipes for the next two tasks are in the **"Recipes"** section below.

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

- **Phase 2b (shard-seeding) DONE:** registry grown from 5 → **56 results** (`argument/lemmas/*.md`),
  harvested from `report/PROVENANCE.md` per-claim ledger + `report/sections/*` + `agent-A|B/theory|notes`.
  Covers all 6 clusters: bridge sub-lemmas, cited preliminaries (JNW/Effros-Størmer/Whitehead/Aut/VLW/
  Kadison/power-assoc), faithful-invariant, exact factorization, classical stability (14), Layer-1
  structure programme (11), exponent (7). Plus **2 new defs** (`def-peirce-decomposition` locked,
  `def-jordan-frame` draft — HOS lacks the literal term). DAG acyclic, `argument.py --check` =
  **0 errors, 0 warnings** (56 results, 17 ready, 29 blocked); `check-defs` 0 errors. Authored + adversarially
  verified (contracts checked against cited sources) via a fan-out workflow. Conditional theorems
  (thm-factorization, thm-classical-factorization) correctly modeled as `proved` but **blocked** on their
  open hypotheses (op-npps, op-exposed-hull); obstructions/open-problems carried as first-class nodes.
  *Still open in Phase 2b:* real beads sync (`aipm-wfp`); `argument.py --sync-beads` is still a dry-run stub.

Commits: bd init → Phase0 refs → Phase1 (foundation/TDD/core/peripheral) → plan+HANDOFF → Phase2 linker
→ Phase2b registry seeded (56 results).

## NEXT (in order)
1. **Phase 2b beads-sync (`aipm-wfp`) — the only remaining 2b piece:** shard-seeding is DONE (56 results).
   Replace the dry-run stub in `scripts/argument.py --sync-beads` with a real sync: one `bd` issue per
   registry lemma, `bd dep add` edges = registry `deps`, persist a lemma↔bd-id map; serialize bd calls.
   (Goal: `bd ready` mirrors the linker's ready frontier.) Then `python3 scripts/argument.py --check --generate`.
2. **Phase 3 — af per-lemma pilot** on the bridge's proved leaves (`lem-P-properties` is the current
   ready frontier): `af init proofs/<id>`, transcribe to trivial steps, A=prover/B=verifier, advance the
   shard `af: none→seeded→validated`; add `af replay --verify` per `proofs/*` to check-all.sh.
3. **Phase 4 — reorg + hygiene:** consolidate `theory/`+`experiments/`, archive clutter (phantom
   `response-to-agent-a-v*`, superseded stacks, 91KB compaction dump); author CLAUDE.md==AGENTS.md + PRD
   — **harvest best-bits from `../cft-anyons`, `../Bennett.jl`, `../af-tests`, `../arithmetic-quantum-mechanics`**
   (user directive); add `check-provenance.py` + report `latexmk` to check-all.sh; merge `report/PROVENANCE.md` up.
4. **Phase 5 — fresh Lean scaffold** (secondary; af-tests reference only).

## Recipes (do exactly this)

**Recipe A — seed a registry shard (Phase 2b, `aipm-w2b`).** For each remaining result row in
`report/PROVENANCE.md` (per-claim ledger: label · source · locus · status):
1. `cp argument/lemmas/lem-P-properties.md argument/lemmas/<id>.md` and edit the frontmatter
   (schema: `argument/README.md`). `id`=`{lem|thm|prop|cor|op}-<slug>` == filename stem; `contract`=
   the statement as ONE line; `defs`=`;`-list of `def-*` ids; `deps`=`;`-list of registry ids it uses;
   `status`∈{proved,cited,consensus,open,obstruction,disproved}; `af: none`; `provenance`; `owner`; `workspace`.
2. Every `def` referenced MUST exist in `definitions/` — if missing, add a def shard first
   (`definitions/README.md` schema) and `python3 scripts/check-defs.py`.
3. `python3 scripts/argument.py --check --generate` → must be 0 errors; regenerates INDEX/DAG.
4. Commit (the pre-commit hook re-runs the suite). Map report status→registry: `(proved)`→proved,
   `(cited)`→cited, `(consensus)`→consensus, `OPEN`/`(open)`→open, obstruction→obstruction.

**Recipe B — af pilot on a lemma (Phase 3, `aipm-0sg`).** Drive the **ready frontier** (currently
`lem-P-properties` — `python3 scripts/argument.py` prints it):
1. `af init -c "<contract copied VERBATIM from the shard>" -a agent-A -d proofs/<id>` (root conjecture
   MUST match the registry `contract` — the linker checks this).
2. Seed: `af def-add <name> "<text>"` for each `def` (mirror `definitions/`); `af add-external --name <dep-id>
   --source "<dep contract> | proof: proofs/<dep-id>"` for each `dep`.
3. Prove to **trivial steps**: prover runs `af claim`/`af refine`; the OTHER agent (verifier ≠ prover per
   node) runs `af challenge`/`af accept`. `af reap` between agents. Challenge ids are `ch-<hex>`.
   If the tree balloons past ~12 nodes, STOP — factor a sub-lemma into its own registry shard + workspace.
4. When root is `validated`+`clean`: set the shard `af: validated`, `python3 scripts/argument.py --check`
   (verifies af root == contract, propagates status), `af export -f latex -o proofs/<id>/export.tex`, commit.

**Recipe C — run the gate / commit.** `sh scripts/check-all.sh` → `[check-all] OK`. Then `git commit`
normally (hook runs bd export + check-all). Push at checkpoints: `git push`.

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
