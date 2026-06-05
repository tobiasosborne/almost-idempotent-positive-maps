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

## 2026-06-05 (session 2) — Phase 2b: registry seeded (5 → 56 results)

Seeded the rest of the argument registry (`aipm-w2b`, closed). Method: I designed the full acyclic DAG up
front (a master inventory fixing every id/kind/status/defs/deps so the linker resolves by construction),
then fan-out via a background **workflow** — a defs track + 6 per-cluster `author → adversarial-verify`
pipelines (15 agents, ~864k tok). Authoring agents wrote each `argument/lemmas/<id>.md` and refined the
one-line `contract` against its cited source (report sections + `agent-A|B/theory|notes` + `refs/`);
verifiers re-checked every contract for faithfulness/overclaim and the frontmatter against the inventory.

**Done**
- **51 new registry shards** (total 56): B0 bridge sub-lemmas (orderunit/easy/polar/onehole) + C1 cited
  preliminaries (power-assoc, Kadison–Jordan-Schwarz, JNW classification, Effros–Størmer, Whitehead,
  Aut(J)-compact, VLW minimal-J*) + C2 faithful-invariant (4) + C3 exact factorization (op-npps,
  thm-factorization, rounding-fails, P-not-positive) + C4 classical stability (14) + C5 Layer-1 structure
  programme (11) + C6 exponent (7). Obstructions and open-problems are first-class `kind`s.
- **2 new defs:** `def-peirce-decomposition` (locked, byte-matched HOS 2.6.2/2.6.4-5 incl. mult. table),
  `def-jordan-frame` (draft — HOS lacks the literal term; Faraut–Korányi vocabulary, lock criterion noted).
- Wired the finer bridge lemmas into the existing DAG (thm-bridge ← easy/orderunit; prop-bridge-jordan ←
  polar/onehole; lem-square-hole ← prop-kadison-js, the Kadison crux).
- Gates green: `argument.py --check` 0 errors/0 warnings (56 results, 17 ready, 29 blocked);
  `check-defs` 0 errors; `scripts/check-all.sh` = `[check-all] OK`. INDEX.md + DAG.md regenerated.

**Key modeling decisions**
- `def:*` ledger rows map to Layer-0 defs (not registry); pure framing `rem:*` excluded; substantive
  `rem:*`/`ex:*`/counterexample `prop:*` carried as `kind: obstruction`. Cited literature → `status: cited`
  (taken as axioms, not in the af ready-frontier). Conditional theorems modeled as `proved` with the open
  hypothesis as a `dep` → they show as **blocked** until the hypothesis is af-validated (semantically right).

**Open threads**
- Phase 2b **beads-sync** (`aipm-wfp`) still pending: `argument.py --sync-beads` is a dry-run stub.
- `def-jordan-frame` is draft (term not in HOS); fold into the draft-def lock pass (`aipm-9ho`) or
  A+B-sign-off as consensus vocabulary.
- Recommended next: Phase 3 af pilot on `lem-P-properties` (`aipm-0sg`, the ready frontier).

## 2026-06-05 (session 3) — Phase 4 context-hygiene docs (CLAUDE/AGENTS/PRD/LEARNINGS)

Authored the project's context docs (`aipm-ond`, closed). Method: a **harvest workflow** (5 agents —
one per neighbour repo `../cft-anyons` / `../arithmetic-quantum-mechanics` / `../Bennett.jl` / `../af-tests`,
plus a self-inventory of this repo) returned structured best-practices + the accurate current state; I
synthesized the docs; a 2-agent **adversarial review** (math-overclaim + process/consistency) found and
I fixed 9 defects.

**Done**
- **`CLAUDE.md` (== `AGENTS.md`, byte-identical, bd block preserved):** HOW/process — read-order gate by
  file name; the Laws (ground-truth-before-claims, one-canonical-def, atomic/validated/accretive,
  reviewer≠author); numbered Rules (no-overclaim, "runs-without-errors-is-never-a-test", get-feedback-fast,
  ~200-LOC sharding, no-remote-CI, cross-session→beads, def-never-(proved), non-interactive shell, …);
  hallucination callouts; verified build/test commands; the 4-layer architecture; af+linker usage; M/D/C/R/I
  validation gates; commit discipline; stop conditions; file map; land-the-plane.
- **`PRD.md` (the entry point):** WHAT/scope — mission, in/out scope, the two-layer theorem + ε-JB axioms +
  a Kitaev analogy table with "what does NOT transfer", honest current state, success criteria, open
  obstructions (each → registry id + bead), milestones.
- **`docs/LEARNINGS.md`:** seeded with the retracted claims (faithful "YES" → O(η/λ); Frobenius-"resolved";
  phantom response-to-agent-a-v*; rank-balance stub) + standing no-overclaim lessons.

**Review fixes worth recording**
- The math reviewer caught that the docs **understated** Layer-1: the report/registry now carry
  `cor-adjoint-benchmark` (order-unit splitting **proved** for exact-adjoint cocycles, *modulo* the
  `obs-matrix-audit` re-audit); only `op-layer1-gap` remains open. PRD/CLAUDE/LEARNINGS corrected (the
  pre-2026-06-04 "order-unit OPEN" framing was stale). Also fixed the η<1/4-vs-η≤η₀ threshold, the
  "η is CP-only" category error, the 12-vs-13 section count, and "gate green"→"0 errors, 3 draft warns".
- The process reviewer ran every command (all pass) and flagged the af stop-condition.

**Key decision (user clarification)**
- The af escalation was initially written as a hard "ask before ANY af use" gate; the user clarified it
  should be **light — only the FIRST af workspace needs a hint or two**. Softened everywhere (CLAUDE §6/§9,
  HANDOFF START-HERE + Recipe B, PRD escalation; ~/.claude memory `feedback-first-af-needs-hint`).

**Remaining Phase 4:** reorg/archive (`aipm-chn`) + check-provenance/report-build in check-all (`aipm-oql`).

## 2026-06-05 (session 4) — Phase 3: first af proof (lem-P-properties validated)

Drove the first machine-checkable proof end-to-end in `af` (`aipm-0sg`, closed). `proofs/lem-P-properties/`
is **fully validated** (10/10 nodes validated + clean, root composition verified). User-set conventions:
**verifier = a FRESH subagent every node** (gaps/errors are high-value wins; strictest rigour); **prover =
the main loop**; **no "standard facts"** — every fact provenanced to `refs/` ground truth or derived from
cited facts / named nodes.

**Process (4 adversarial rounds).** Built an 8→10-node tree (added foundational sub-nodes 1.1.1 `‖Φ‖=1`
order-unit contraction, 1.1.2 `End(B(H)_sa)` is a unital Banach algebra). Each round: fresh verifier per
node (via Workflow, 7/7/7/3 + 1 root) → I resolved challenges as prover (`amend`/`resolve-challenge`) →
re-verify fresh. The adversarial loop caught **real defects**: a wrong `‖U‖≤1/2` gate (bug), a `3/2·C=C`
arithmetic slip, multiple provenance mis-citations (Idel cited for facts it doesn't contain; `‖Φ‖=1` and
Φ's positivity/unitality are definitional hypotheses → `def positive-unital-map`), and a deep
**multiplicativity gap** for `R²=(S²)⁻¹` — resolved by going to ground truth: Kitaev's general-Banach-algebra
`prop_P` (refs/kitaev:524-532) states `θ(2P−I)²=θ(2P−I)` directly, and `sgn(X)²=I` at :518. Completeness
pinned to HOS 3.1.2/3.3.10 + Kitaev:638-642.

**Result.** Shard `af: validated`; `argument.py --check` 0 errors, contract-match OK, status propagation
unblocked `lem-first-insertion`+`lem-bridge-orderunit`. Export `proofs/lem-P-properties/export.{tex,md}`.
`check-all` OK. The committed canonical record is the append-only `ledger/` + `externals/` + `meta.json`
(nodes/ caches gitignored).

**Conventions / gotchas learned.** af has **no post-hoc dependency-edge command** (deps named in-text).
`resolve-challenge` takes `<challenge-id> -r "..."` (no `-o`). `accept` without a prior challenge needs
`--confirm`. Recipe B in HANDOFF updated with the prover/fresh-verifier convention.

**Follow-ups filed:** factor the reusable foundational facts (`‖Φ‖=1` contraction, operator Banach algebra)
into their own registry lemmas/defs (+ re-cite node 1.7's Φ(x)≥0 to the def); add `af replay --verify` of
`proofs/*` to `check-all.sh`.
