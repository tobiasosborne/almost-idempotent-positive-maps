<!--
ROLE: crash-safe handoff for the argument-architecture build (now on branch main; the feature branch was retired).
UPDATE POLICY: rewritten (not appended) at each checkpoint; keep <=500 lines; git history holds old versions.
TRIGGER: end of a work session / before a push / when phase status changes.
NOTE: this tracks the REORG/ARCHITECTURE + af-proof build. For the MATH status see PRD.md §math + agent-A/HANDOFF.md.
-->

# HANDOFF — argument-architecture build

> ## START HERE (next agent)
> 1. `git checkout main` (the work lives on `main` now; the `argument-architecture` feature branch was fast-forwarded onto `main` and retired).
> 2. Read, in order: **`PRD.md`** → **`CLAUDE.md`**(==`AGENTS.md`) → **this file** → `definitions/INDEX.md`
>    + `argument/INDEX.md` + `argument/DAG.md` (the live state).
> 3. **THE ALGEBRAIC BRIDGE (Theorem B) IS COMPLETE** — all 9 results of its DAG are machine-validated via
>    `af` (`lem-P-properties` predated this session; the other 8 are commits `7021740..b7110ba`):
>    `lem-P-properties`, `lem-bridge-orderunit`,
>    `lem-first-insertion`, `lem-square-hole-almost-positive`, `lem-bridge-easy`, `lem-bridge-polar`,
>    `lem-bridge-onehole`, `prop-bridge-jordan` (crux), `thm-bridge` (capstone). **What to do next is in
>    beads (`bd ready`).** Highest-value follow-ups, in order: **`aipm-iel`** (P1 — harden `check-refs`:
>    8 quote-less externals, 7 of them in `lem-P-properties`, are SKIPPED by the gate and NOT byte-verified;
>    retrofit them to embed verbatim quotes + re-verify, close the skip-no-quote evasion); **`aipm-17f`**
>    (audit the `cited` registry results vs `refs/` string-matches, honestly downgrade the ungrounded —
>    `thm-whitehead`/`prop-aut-compact` are PDF-only — and rename `cited`→`grounded`); **`aipm-qpa`** (factor
>    `‖Φ‖=1`/operator-Banach-algebra into own lemmas/defs); **`aipm-dqz`** (`af replay --verify` in
>    check-all); **`aipm-oql`/`aipm-chn`** (Phase-4 reorg). Open-math frontier (hard): `aipm-245`/`aipm-08u`/
>    `aipm-36d` (Layer-1). Claim with `bd update <id> --status in_progress`; close with `bd close <id>`.
> 4. Sanity-check: `sh scripts/check-all.sh` must print `[check-all] OK`. The gate now includes
>    **`check-refs`** (byte-matches every af-external verbatim quote vs its `refs/` locus) — it is LIVE in
>    the pre-commit hook. Commit normally; do **not** use `core.hooksPath=/dev/null`.
> 5. Live recipes below: **Recipe B** (af per-lemma — proven over 8 bridge lemmas), **Recipe C**
>    (gate/commit), **Recipe A** (add a registry shard).

**Branch:** `main` (the `argument-architecture` feature branch was fast-forwarded onto `main` and retired). **Date:** 2026-06-06. **Approved design:**
`docs/plans/2026-06-05-argument-architecture-plan.md`. Mental model: definitions = types · each lemma (af
workspace) = a module whose *contract* is its one-line statement · a linker enforces the DAG.

## Two governing rules (user, 2026-06-06) — non-negotiable
1. **No "standard facts"/"citations".** The ONLY ground truth is a **byte/string match to a LOCAL `refs/`
   source**. Every leaf of every proof is an af external whose verbatim quote byte-matches `refs/`
   (enforced by `scripts/check-refs.py`). If a fact is not in `refs/`, STOP — do not paraphrase from memory.
2. **"A derivation = lemma = af".** Every non-leaf fact is an af-validated claim (a node; if reusable/
   substantial, its own registry lemma). Small derivations stay in-workspace nodes; don't over-factor.
Corollary actually used in the bridge: **`‖Φ‖=1` is AVOIDABLE** — bound `‖Φ(a)‖ ≤ (1±δ)‖a‖` via the norm
triangle inequality + the grounded `δ=‖P−Φ‖` bound (lem-P-properties); never assert `‖Φ‖=1` as a leaf.

## DONE (this session — all committed + pushed)
- **Theorem B fully machine-validated.** 8 af workspaces, each: build (opus) → fresh-opus-verifier
  adversarial pass per node (reviewer≠author) → resolve → re-verify → `af: validated`. Every leaf
  byte-grounded in `refs/`; `argument.py --check` 0 errors; contract-match + status-propagation clean.
- **Linker fix (`50305fc`).** Grounded-leaf (cited) deps no longer block readiness (TDD, reviewer≠author).
- **`check-refs` provenance gate (`e5b21c8`).** Byte-matches every af-external quote vs `refs/`; wired into
  `check-all.sh`. It exists because a **fabricated "verbatim" quote** (`GT-bhsa-jc`, a true-fact paraphrase)
  reached pushed commit `73b240b` and was caught by a fresh verifier (LEARNINGS **R5**). Audit: exactly 2
  fabrications, both corrected.
- **LEARNINGS R5** (fabrication) + **R6** (`thm-bridge` asserted `η₀=1/4` where `lem-P-properties` needs
  `η₀<1/4` strictly — binomial diverges at the boundary; verifier caught it). Each failure mode earned a
  red→green test (`test_check_refs.py`, `test_argument.py`).

## NEXT (priority order — see `bd ready`)
1. **`aipm-iel` (P1).** Harden `check-refs`: 8 externals cite a `refs/` locus but embed NO verbatim quote
   (→ `skip_noquote`, unchecked); retrofit `lem-P-properties`' 7 quote-less externals to embed real quotes
   + re-verify the pilot; require quotes (skip_noquote→FAIL); consider whole-quote (not single-run) match.
2. **`aipm-17f`.** Audit every `cited` registry result vs `refs/`; downgrade the ungrounded; `cited`→`grounded`.
3. **`aipm-qpa`.** Factor `‖Φ‖=1` contraction + operator-Banach-algebra out of `lem-P-properties` into own
   registry lemmas/defs; fix the false `GT-positive-unital` Idel provenance.
4. **`aipm-dqz`** (`af replay --verify` per `proofs/*` in check-all) · **`aipm-oql`** (check-provenance +
   report `latexmk` in check-all) · **`aipm-chn`** (reorg theory/experiments, archive clutter) ·
   **`aipm-wfp`** (real beads-sync).
5. **Open-math frontier** (hard, may need the user): `aipm-245` (Layer-1 coboundary splitting), `aipm-08u`
   (NPPS/exposed-hull), `aipm-36d` (matrix benchmark re-audit). **`aipm-3ox`** = Phase-5 fresh Lean scaffold.
6. **`aipm-1pd` (P3).** af PR: post-hoc dependency-edge command (`af depend`), upstream `../vibefeld`
   (user authorized af PRs).

## Recipes (do exactly this)

**Recipe B — af per-lemma (PROVEN over 8 bridge lemmas).** Drive the ready frontier (`python3
scripts/argument.py` prints it). Per lemma:
1. **Prep (sonnet):** read the lemma shard + its prose (`agent-B/theory/theorem-B-algebraic-bridge.md` line
   range in `provenance`) + the cited def shards; for every external fact, locate the verbatim `refs/`
   string. Output a "proof kit" (proof outline · externals with loci + verbatim strings · node plan ≤12,
   depth ≤3 · ungrounded flags).
2. **Build (opus prover, owner agent-A):** `af init -c "<contract VERBATIM>" -a agent-A -d proofs/<id>`
   (root must byte-match the registry contract — the linker checks it). Seed defs (`af def-add`) and
   externals: **COPY the actual `refs/` bytes** (`sed -n '<lines>p' refs/...`) into the `VERBATIM:` quote —
   NEVER write a quote from memory. Import a validated lemma's result as a black-box external (no refs
   quote needed). Build the tree (`af refine`, declare cross-edges with `--depends` AT REFINE TIME).
   **ANTI-FABRICATION self-check:** run `python3 scripts/check-refs.py --check | grep <id>` and confirm
   every refs-external PASSES before finishing. Do NOT self-validate.
3. **Verify (opus, a FRESH verifier per node, sequential — af is NOT concurrency-safe within a workspace):**
   each told gaps/errors are high-value successes; re-grep every cited refs leaf; check imports match their
   lemma contracts; demand universal/dimension-free constants. `af claim <n> -o v<round>-<n> -r verifier`
   then `af challenge`/`af accept --confirm`. Verify leaves → parents → root.
4. **Resolve (prover):** address challenges (`af amend`/`af refine`/`af resolve-challenge`). **Also resolve
   the ROOT's cascaded dependency challenge** once children validate (easy to miss). Re-verify fresh.
5. When all nodes validated+clean: set shard `af: validated`, `python3 scripts/argument.py --check
   --generate`, `af export -f latex/-f markdown`, commit (Recipe C). >12 nodes ⇒ STOP and factor a sub-lemma.

**Recipe C — gate / commit.** `af export …`; `python3 scripts/argument.py --check --generate`; then commit
(the pre-commit hook re-runs `check-all` = check-defs + **check-refs** + linker + tests). Guard:
`grep -q '^af: validated' <shard> && sh scripts/check-all.sh && git add <proofs/id> <shard> argument/INDEX.md
argument/DAG.md && git commit … && git push`. One atomic validated result per commit, in dependency order.

**Recipe A — add a registry shard.** `cp argument/lemmas/<template>.md argument/lemmas/<id>.md`, edit
frontmatter (`id`==filename stem; `contract` one line; `defs`/`deps` `;`-lists; `status`; `af: none`;
`provenance`; `owner`; `workspace`). Every `def` must exist in `definitions/`. `python3 scripts/argument.py
--check --generate` → 0 errors. Commit.

## Key facts / gotchas
- **check-refs is law.** Every af-external citing a `refs/` locus must embed a verbatim quote that
  byte-matches (whitespace/`$`-normalised). Provers copy actual bytes + self-check; the hook blocks
  fabrications. 8 quote-less externals currently slip through as `skip_noquote` (→ `aipm-iel`).
- **af frictions.** No post-hoc dependency-edge command (deps via `--depends` at refine time, or re-ground
  a leaf from an in-scope external; PR = `aipm-1pd`). Externals are workspace-global (node scope shows
  "(none found)"). Serialize af ops per workspace (not concurrency-safe); different workspaces are
  independent and parallelize fine. `af resolve-challenge <id> -r "…"` (no `-o`); `af accept` without a
  prior challenge needs `--confirm`; amending a node requires it `pending` (validated nodes can't be amended
  — re-ground from in-scope externals instead).
- **Validated bridge workspaces are the template** for future af proofs (e.g. `aipm-qpa` factoring, the
  open-math frontier). `proofs/lem-bridge-orderunit` (smallest, exact) and `proofs/prop-bridge-jordan` (crux)
  are good worked examples.
- **Task tracking is beads only** (`bd ready`/`bd show`/`bd close`). `agent-A/HANDOFF.md` MATH is current;
  its FILE MAP is stale (repo is `/home/tobias/...`, refs deduped into `refs/`).
