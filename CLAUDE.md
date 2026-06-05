<!--
ROLE: how-to-work / process rules for any AI agent on this repo. (WHAT/scope lives in PRD.md.)
UPDATE POLICY: this file is IDENTICAL to AGENTS.md — edit both in the same commit (or `cp -f CLAUDE.md AGENTS.md`); never let them drift. Keep the BEADS INTEGRATION block (bd-managed) intact.
TRIGGER: a process/convention/tooling change, or a new standing rule from the user.
-->

# CLAUDE.md — how to work on this project

> **This file is identical to `AGENTS.md`.** Edit both together; never let them drift (`cp -f CLAUDE.md AGENTS.md`).
>
> **Router.** *What is this project / what may I change?* → **`PRD.md`** (the entry point, read it first).
> *How do I work?* → this file. *Current build state / next task?* → **`HANDOFF.md`** then `bd ready`.
> *The approved design?* → `docs/plans/2026-06-05-argument-architecture-plan.md`. *Math status?* → `PRD.md` §math.

**The single failure mode this project guards against: a confident, plausible, WRONG claim.** Everything
below exists to make that hard — ground truth before claims, one canonical definition, an enforced proof
DAG, reviewer ≠ author, and honest "(open)" tags. The repo is canonical; conversation, memory, and
prior-session summaries are **not**.

---

## 0. Read-order gate (by file name, not by number)

Before you ADD or CHANGE any mathematical content, you must have read: **`PRD.md`**, **this file**,
**`HANDOFF.md`**, **`definitions/INDEX.md`**, **`argument/INDEX.md`**. To add/edit a definition or a
registry result, also read the relevant schema: `definitions/README.md` / `argument/README.md`. (The
gate names files, not "items 1–5", so it can't drift as the list grows.) If you have not read them,
**STOP**: file a `bd` issue blocked on the pre-read, and stop — do not improvise.

---

## 1. The Laws (non-negotiable)

- **L1 — Ground truth before claims.** Every named Definition/Theorem must string-match **byte-verbatim**
  to a LOCAL source under `refs/` (recompute the SHA256, `grep -F` the quote). No claim without a
  provenance row. If the source isn't in `refs/`, **STOP and ask** — never paraphrase from memory.
  Extraction-level / PDF-only provenance is **flagged honestly**, never passed off as byte-verified.
- **L2 — One canonical definition (Definitions DB = Priority 1).** Each term is defined **exactly once**
  in `definitions/`; `report/`, `proofs/` (af), and `theory/` *reference* `def-<slug>` and never restate
  it. Two shards sharing a term/alias = drift = build failure. **Drift is death.**
- **L3 — Atomic / validated / accretive.** Every result gets its **own tiny af workspace**, proven down to
  trivial steps; a tree `>12` nodes or depth `>3` is a **brittleness FAILURE** → factor into sub-lemmas.
  The whole argument is an **enforced acyclic DAG** of one-line contracts (the linker checks it). One
  atomic, validated step per commit.
- **L4 — Reviewer ≠ author; consensus is the bar.** The af *verifier* must differ from the *prover* per
  node; a result is done only at **A+B consensus** on formulation, statement, AND proof. Be
  constructively skeptical — demand excellence on constants and rigor; never accept blindly.

---

## 2. The Rules (numbered)

0. **Don't overclaim — tag `(open)` honestly.** The load-bearing honest facts (see also §3): the bridge
   exponent is **√η in general** (η only under complete positivity / a compatible dilation; decomposable
   is conjectural); the **Layer-1 structure theorem and exact UP factorization are OPEN**; the Layer-1
   dimension-free constant is **Frobenius-bounded but order-unit-norm OPEN** (keep that distinction).
1. **"Runs without errors" is never a passing test.** Every test asserts an invariant against a
   known-correct value (for proofs: the goal closes). Write the failing check first (red→green); for a
   load-bearing test, perturb to confirm it goes RED, then restore (port-and-verify).
2. **Get feedback fast.** Don't work blind. After any non-trivial change run the relevant gate:
   `python3 scripts/check-defs.py --check` (defs), `python3 scripts/argument.py --check` (linker),
   `sh scripts/check-all.sh` (everything), `cd report && make` (paper). Numerics carry a SHA256 + a
   re-run command.
3. **Reviewer ≠ author** for every substantive change (a different agent reviews; verdict in the commit
   under a `Review:` line). Pure-mechanical ops (`git mv`, regenerating an INDEX, a verbatim
   user-specified edit) are exempt — but say so.
4. **~200-LOC sharding everywhere.** One def per file, one result per registry shard, theory notes
   `≤~200` lines; stable greppable ids (`def-`/`lem-`/`thm-`/`prop-`/`op-`/`obs-<slug>`); the generated
   `INDEX`/`DAG` files are the lookup tables (never hand-edit them). No monolith.
5. **No remote CI.** The only gate is the **local** pre-commit suite `scripts/check-all.sh` (wired into
   `.beads/hooks/pre-commit`). Let it run — do **not** use `core.hooksPath=/dev/null`.
6. **A definition is never `(proved)`.** Tag adopted-and-agreed defs `consensus`, literature defs
   `cited` (byte-matched), project-introduced defs `original`. `consensus`/`original` lock only on
   recorded A+B sign-off.
7. **Cross-session state → beads, never markdown TODO.** `bd` for ALL task tracking (no TodoWrite /
   markdown TODO lists). Persistent project knowledge → `bd remember`. (The harness's own `~/.claude`
   memory is the *agent's* private cross-session memory and is orthogonal — do not create in-repo
   `MEMORY.md` files.)
8. **Docs move in lockstep with content.** A change that leaves `HANDOFF.md`, a README, or a provenance
   row stale is **incomplete work**, not a follow-up.
9. **Re-read these rules after every context compaction.** Then re-orient from the repo, not from the
   conversation summary.
10. **Non-interactive shell.** Use `cp -f` / `mv -f` / `rm -f` (`-i` aliases hang the agent).
11. **Provenance is byte-verbatim.** `refs/manifest/checksums.sha256` is authoritative
    (`cd refs && sha256sum -c manifest/checksums.sha256`). Cited shards record `source` (a SOURCES.md id)
    + `locus` + 16-hex `sha256`; the gate fails on hash mismatch, warns if the gitignored payload is absent.

---

## 3. Hallucination-risk callouts (claims that LOOK right but are WRONG here)

*(The retracted claims are logged in full, with dates and who-conceded, in `docs/LEARNINGS.md`.)*

- ❌ "Frobenius-bounded ⇒ the Layer-1 splitting is done." → Frobenius-boundedness does **not** give
  order-unit-boundedness (the conversion can lose `√rank` — `prop-rank-gap`, `obs-cochain-caveats`). Honest
  status: the order-unit splitting **is** now proved for **exact cocycles in the adjoint module**
  (`cor-adjoint-benchmark`, *modulo* the `obs-matrix-audit` re-audit); the **full Layer-1 structure theorem
  stays OPEN** (`op-layer1-gap`: next-arrow for arbitrary modules, pre-cohomological construction, …).
- ❌ "A **faithful invariant state ⇒ O(η)**." → FALSE. The bound is `O(η/λ)` and needs a dimension-free
  spectral floor `λ`; A overclaimed YES, B refuted, A withdrew (`prop-faithful-counterexample`).
- ❌ "The square-hole rate is `O(η²)`." → It is `O(η)` and **sharp** (`‖P(q_r²)‖/η → 32/27`,
  `obs-bridge-numerics`).
- ❌ "Use `η` (Kitaev strength) in general." → Only **`√η`** is unconditional; `η` is CP-only /
  decomposable-conjectural (`obs-exponent`, `op-decomposable`).
- ❌ "`P = θ(2Φ−1)` is a positive map." → Not in general (`obs-P-not-positive`); that's exactly why
  `op-npps` is open.
- ❌ Trusting `agent-B/notes/response-to-agent-a-v0.*` as A's positions. → Those are **phantom** subagent
  extrapolations; `agent-a-findings` is the single source of truth for A.
- ❌ Following `/home/tobiasosborne/...` paths from `agent-A/HANDOFF.md`. → Stale; the repo is
  `/home/tobias/...` and refs are deduped into `refs/`. That file's MATH is current; its FILE MAP is stale.
- ❌ Treating `thm-whitehead` / `prop-aut-compact` as byte-verified. → They are **extraction/PDF-level**
  (Chu–Russo PDF; Faraut–Korányi not local) — flagged, not discharged.

---

## 4. Build & test (verified commands)

```bash
sh scripts/check-all.sh                       # THE gate → prints "[check-all] OK"; non-zero fails commit
                                              #   = check-defs.py --check + argument.py --check + unit tests
python3 scripts/check-defs.py --check         # definitions: drift/dedup + cited SHA256 vs manifest + consensus-gate
python3 scripts/check-defs.py --generate-index# regenerate definitions/INDEX.md  (generated — don't hand-edit)
python3 scripts/argument.py --check           # the LINKER (acyclic · imports · contract-match · status · brittleness · orphans)
python3 scripts/argument.py --generate        # regenerate argument/INDEX.md + DAG.md  (generated)
python3 scripts/argument.py                   # default: check + generate + print the ready frontier
python3 scripts/tests/test_check_defs.py      # TDD unit tests for the gates (run without af present)
python3 scripts/tests/test_argument.py
cd report && make                             # latexmk -pdf; report/main.pdf (13 section files: 00–11 + 06b). NOT yet in check-all (aipm-oql)
cd refs && sha256sum -c manifest/checksums.sha256   # ground-truth integrity (50 files; payload gitignored)
af --version                                  # 0.1.3 — authoritative (the binary self-label may say "dev")
```

---

## 5. Architecture — the typed module system for the proof

Mental model: **definitions = types/vocabulary · each result = a module whose *contract* is its one-line
statement and whose *imports* are the defs/lemmas it uses · each af workspace = that module's tiny
implementation · a linker enforces the contracts.** Four layers:

- **Layer 0 — `definitions/`** (Priority 1): one `def-<slug>.md` shard per term. Gate: `check-defs.py`.
- **Layer 1 — `argument/lemmas/<id>.md`**: one shard per result; `contract` (one line) is the anti-drift
  single source of truth; `defs`/`deps` are the imports/DAG edges; `status`/`af`/`owner`. Generated
  `INDEX.md` + `DAG.md`.
- **Layer 2 — `proofs/<id>/`**: one tiny af workspace per result; root conjecture **==** the registry
  `contract`. *(Does not exist yet — Phase 3.)*
- **Layer 3 — `scripts/`**: `argument.py` (linker) + `check-defs.py` + `check-all.sh`; `.beads/` mirrors
  the DAG as tasks.

Ground truth: `refs/<source-id>/` (local copies, payload gitignored) + `refs/manifest/SOURCES.md` +
`checksums.sha256` (tracked). Full design: `docs/plans/2026-06-05-argument-architecture-plan.md`.

---

## 6. af + the linker (Layer 2)

`af` = Adversarial Proof Framework (`../vibefeld`, v0.1.3; export Markdown/LaTeX only — **no af→Lean**;
Lean is secondary, `af-tests` reference-only). Per-lemma workflow is **Recipe B** in `HANDOFF.md`:
`af init -c "<contract VERBATIM from the registry shard>"` (root must match the contract — the linker
enforces it) → seed `af def-add` / `af add-external` imports → prove to trivial steps with
**prover runs `af claim`/`af refine`, the OTHER agent runs `af challenge`/`af accept`** (`af reap`
between) → balloon past ~12 nodes ⇒ STOP and factor a sub-lemma → on `validated`+`clean` set the shard
`af: validated`, run `argument.py --check`, `af export`, commit.

The linker enforces 6 invariants: acyclic deps · imports resolve · **contract-match** (registry `contract`
≡ af root) · status propagation (`af: validated` needs all deps validated; computes ready/blocked) ·
brittleness (`>12`/depth `>3` ⇒ REFACTOR) · orphans (registry ↔ `proofs/` correspondence).

> **First-time af.** The Phase 3 pilot is this project's *first* use of `af` — get a hint or two from the
> user before starting that first workspace. After the first one, `af` is ordinary autonomous work.

---

## 7. Validation gates (declare which you exercised, per commit)

Adapted from the neighbour repos' **M/D/C/R/I**:
- **M**echanical — `check-all.sh` (and `report/make` if the paper changed) passes.
- **D**efinitional — every term used resolves to a `definitions/` shard; no restating.
- **C**ross-reference — a cited claim byte-matches its `refs/` source at the recorded locus.
- **R**eviewer — an independent agent (≠ author) signed off.
- **I**dempotent — re-running the generators/gate yields the same state.

Risk tiers: trivial/mechanical = `M I`; a new proved result = `M D C R I`.

---

## 8. Commit discipline

One atomic step per commit; split if two landed together. Message = imperative subject + a body that
states **what** and **why** and (for math) cites the source locus + which gates passed. Never amend a
pushed commit. End every commit message with:
`Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`.

---

## 9. Stop conditions (escalate to the user, don't improvise)

- The **first** af workspace (the Phase 3 pilot, §6) — get a hint or two from the user (just the first; not every af thereafter).
- A claim's ground truth is **not in `refs/`** (don't paraphrase from memory).
- You'd add something **out of scope** per `PRD.md` (out-of-scope additions are a stop condition).
- A **contract drift / cycle / orphan** the linker reports that you can't resolve cleanly.
- A definition would need to **change** (it ripples through everything that references it).
- You're about to **overclaim** (turn an `(open)` into a theorem) — stop and get consensus.

---

## 10. File map (canonical layout)

```
PRD.md                  WHAT/scope — the entry point (read first)
CLAUDE.md == AGENTS.md  HOW/process — this file
HANDOFF.md              current build state + START HERE + Recipes (rewritten each session, ≤500 lines)
docs/                   plans/ (approved design) · worklog.md (append-only) · LEARNINGS.md (retracted claims)
definitions/            Layer 0 — def-<slug>.md shards + README (schema) + INDEX (generated)
argument/               Layer 1 — lemmas/<id>.md shards + README + INDEX + DAG (generated)
proofs/<id>/            Layer 2 — af workspaces (Phase 3; not yet present)
scripts/                Layer 3 — check-all.sh · check-defs.py · argument.py · tests/
refs/                   ground truth — <source-id>/ (gitignored payload) + manifest/ (tracked)
report/                 the LaTeX paper (13 section files: 00–11 + 06b) + PROVENANCE.md
agent-A/ agent-B/       LEGACY theory/notes/experiments (to be consolidated in Phase 4) — math is real,
                        agent-A/HANDOFF.md FILE MAP is stale; agent-a-findings is A's source of truth
```

## 11. Landing the plane (session close)

The mandatory session-close checklist (file follow-up issues → run gates → update issue status →
`git pull --rebase` + `bd dolt push` + `git push` → verify → hand off) is the **Session Completion** block
below (bd-managed). Work is **not** done until `git push` succeeds — you push; never "ready to push when
you are". Rewrite `HANDOFF.md` (don't append) and append a dated `docs/worklog.md` entry.

<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:ca08a54f -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

## Session Completion

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - This is MANDATORY:
   ```bash
   git pull --rebase
   bd dolt push
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing - that leaves work stranded locally
- NEVER say "ready to push when you are" - YOU must push
- If push fails, resolve and retry until it succeeds
<!-- END BEADS INTEGRATION -->
