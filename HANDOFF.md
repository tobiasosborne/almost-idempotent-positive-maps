<!--
ROLE: crash-safe handoff for the argument-architecture build (branch main; feature branch retired).
UPDATE POLICY: rewritten (not appended) at each checkpoint; keep <=500 lines; git history holds old versions.
TRIGGER: end of a work session / before a push / when phase status changes.
NOTE: this tracks the REORG/ARCHITECTURE + af-proof build. For the MATH status see PRD.md §math + agent-A/HANDOFF.md.
-->

# HANDOFF — argument-architecture build

> ## START HERE (next agent)
> 1. `git checkout main` (all work lives on `main`; the `argument-architecture` feature branch was retired).
> 2. Read, in order: **`PRD.md`** → **`CLAUDE.md`**(==`AGENTS.md`) → **this file** → `definitions/INDEX.md`
>    + `argument/INDEX.md` + `argument/DAG.md` (the live state). `python3 scripts/argument.py` prints the
>    ready/blocked frontier. (Beads is non-functional in this clone — see gotchas; use the linker, not `bd`.)
> 3. **14 results are `af: validated`** (`grep -c validated argument/INDEX.md`). Three clusters:
>    - **Algebraic bridge `thm-bridge`** (the unconditional **√η** result) + its 9-lemma DAG (`lem-P-properties`,
>      `lem-bridge-orderunit`, `lem-first-insertion`, `lem-square-hole-almost-positive`, `lem-bridge-easy`,
>      `lem-bridge-polar`, `lem-bridge-onehole`, `prop-bridge-jordan`, `thm-bridge`).
>    - **Dilation-compatible `thm-dilation-compatible`** (the conditional **O(η)** Kitaev-strength result) +
>      `lem-idempotence-inheritance`, `lem-intertwine-spectral-idempotent`, `lem-cstar-sa-to-epsjb` (O(η) crux).
>    - **`thm-faithful-approx`** (the conditioned faithful-invariant **O(η/λ)** bound, §06b) — the corrected
>      statement of the retracted "faithful invariant ⇒ O(η)" overclaim (honest η/λ, no floor on λ).
> 4. **The report is now the human-readable front door** (`report/main.pdf`, 39pp): every validated result
>    carries a green **`✓ af-validated`** badge linking to its `proofs/<id>/` on GitHub; definitions cite
>    sources with clickable arXiv/journal links; `tab:status` has an `af` column; §01 has a reading guide; the
>    argument DAG is embedded as `\Cref{fig:dag}` (`report/figures/dag.pdf`). See "Report upkeep" below.
> 5. Sanity-check: `sh scripts/check-all.sh` must print `[check-all] OK` (check-defs + check-refs + linker +
>    check-provenance `--build` + TDD). GREEN here (20/50 refs present). Fresh clone with absent `refs/`:
>    `python3 scripts/fetch-refs.py` (17/50 authoritative-origin-pinned, hash-verified);
>    `AIPM_REFS_CACHE=<dir> python3 scripts/fetch-refs.py` restores the bespoke residue.
> 6. **What to do next:** the af frontier (`python3 scripts/argument.py`). Strongest picks: **`lem-classical-equiv`**
>    (highest leverage — unblocks 4 classical results: `thm-rank-one`/`thm-simplex`/`prop-approx-simplex`/
>    `thm-well-exposed`), **`prop-rank-gap`** (small, 0 deps, formalises the √rank "Frobenius ⇏ order-unit"
>    honesty caveat), or the §10 obstructions (`prop-doubling`/`prop-sartre`/`prop-decomposable-norm`, leaf
>    counterexamples defending the conditional η exponent). Recipes below.

**Branch:** `main`. **Date:** 2026-06-07. **Approved design:** `docs/plans/2026-06-05-argument-architecture-plan.md`.
Mental model: definitions = types · each lemma (af workspace) = a module whose *contract* is its one-line
statement · a linker enforces the DAG.

## Governing rules (user) — non-negotiable
1. **No "standard facts"/"citations".** The ONLY ground truth is a **byte/string match to a LOCAL `refs/`
   source** (enforced by `scripts/check-refs.py`). If a fact is not in `refs/`, **STOP** — do not paraphrase
   from memory. You MAY dispatch researcher subagents to FIND an authoritative byte-extractable source and
   propose adding it to `refs/` (manifest + sha256), but the binding step is still a local byte-match.
2. **"A derivation = lemma = af".** Every non-leaf fact is an af-validated claim. Pure-algebra/definition-
   unfolding steps are DERIVED af nodes (bottoming at refs leaves or imported validated lemmas), not asserted
   "elementary".
3. **One fresh verifier per node** (2026-06-07). In the af verify step, spawn a SINGLE fresh verifier subagent
   for EVERY node — it gets one node, verifies it, exits. Never one verifier across multiple nodes (max
   reviewer independence). Run them sequentially (af is not concurrency-safe in a workspace).

## DONE (latest — 2026-06-07, all committed + pushed to `main`)
- **`thm-faithful-approx` COMPLETE (`af: validated`)** — the 14th validated result; the O(η/λ) conditioned
  faithful-invariant bound (`||a∘b−P(a∘b)|| ≤ C(η/λ)||a||||b||`, §06b). 10-node af workspace, depth 3, all
  validated+clean. Chain: spectral split + square-hole import (`lem-square-hole-almost-positive`) → expectation
  bound (imports `lem-P-properties` for `||P−Φ||≤Cη`) → faithfulness upgrade `ω(x)=Tr(ρx)≥λTr(x)≥λ||x||`
  (grounded: VLW `paper.tex:453` trace self-duality + Idel `:333` density + `Tr≥norm`) → diagonal → polarisation.
  Built by a prover then a **fresh single-node verifier per node** (10 verifiers). **One challenge** (node 1.4
  cited 1.1 without a declared direct edge) **resolved** via amend + recording 1.1 as a transitive dep
  (1.4→1.3→1.1; af v0.1.3 has no post-hoc edge command and re-refining would archive validated children),
  re-verified clean. Registry: `af none→validated`; **deps corrected to add `lem-P-properties`** (genuinely
  imported, previously undeclared — declare ALL imports as deps up front next time). Commits `71f277a`,`4a282f0`.
- **Report turned into a status-transparent, provenance-linked front door** (commits `bfedb28`,`d30ef45`,
  `2b21ec7`). Reused existing infra (no new gates, per user steer "balance utility vs CI ceremony"): clickable
  bibliography links (`note=\href` to arXiv/Math.Scand. from `sources.lock.json`); `\afbadge`/`\aflink`/`\afyes`
  macros (`main.tex`) → a green "✓ af-validated" badge per validated result linking to GitHub `proofs/<id>/`;
  `tab:status` `af` column (Status kept col 2 so `check-provenance`'s parser is unaffected) + legend + count;
  §01 reading guide; `scripts/gen-dag-figure.py` (reuses `argument.py`'s parser) → `report/figures/dag.{dot,pdf}`
  via GraphViz, embedded as `fig:dag`. Also fixed a stale tracked `main.pdf` (the gate builds to `.build/`, never
  refreshes the committed PDF).

## DONE (earlier this cycle — context, condensed; full narrative in docs/worklog.md)
- **`thm-dilation-compatible` COMPLETE** (conditional O(η)): 3 factored sub-lemmas + capstone. Honest scope:
  dilation space restricted to `D=B(K)` (general finite-dim C\* `D=⊕Mₙ` deferred, `aipm-us3`). LEARNINGS **R7**:
  a fresh verifier can produce a confident WRONG counterexample — reproduce any refutation before acting.
- **`check-provenance.py` report-sync gate** built + wired into `check-all` (forward/reverse labels, claim
  labels/sources, **status OVERCLAIM** = #1 guarded failure, hash freshness, latexmk `--build`). 52 tests.
- **Reproducible `refs/`** (`fetch-refs.py` + `sources.lock.json`): 17/50 fetch from authoritative origins,
  hash-verified; bespoke residue via `$AIPM_REFS_CACHE`. Genuineness audit: GENUINE = HOS/Idel + 6 web-recovered;
  **SUSPECT = `kaup-1984`, `chu-russo-1512.03347`** (recorded bytes match no authoritative origin; not cited by
  any af proof — flagged, not trusted). All 4 af-cited sources (HOS/Kitaev/Idel/VLW) GENUINE.

## NEXT (priority order)
1. **af frontier — pick a ready result** (`python3 scripts/argument.py`):
   - **`lem-classical-equiv`** — highest leverage; the signed↔stochastic equivalence; unblocks the whole
     classical chain. Ground from `def-stochastic` + Kitaev's operator-norm def (`approximate_algebras.tex:638-642`),
     or acquire the scouted sources first (matrix norms = MIT OCW 6.241J Ch.4; convexity/stochastic = Boyd &
     Vandenberghe — open + byte-extractable).
   - **`prop-rank-gap`** — small, 0 deps; the √rank order-vs-Frobenius gap (the load-bearing "Frobenius ⇏
     order-unit" honesty caveat, CLAUDE.md §3). Ground in HOS (present).
   - **§10 obstructions** `prop-doubling`/`prop-sartre`/`prop-decomposable-norm` — explicit finite
     counterexamples (ℓ∞ map; depolarizing M₂; transpose norm = n); tractable but leaf (unblock nothing).
   - Now also ready (depends only on the freshly-validated `thm-faithful-approx`): `prop-faithful-counterexample`.
2. **Report upkeep** (do in lockstep when the registry/refs change): after validating a result, add its
   `\afbadge{<id>}` in the report + flip its `tab:status` `af` cell to `\afyes` + bump the "N results af-validated"
   counts (§01, §11); re-run `python3 scripts/gen-dag-figure.py` (regenerates `report/figures/dag.pdf`); rebuild
   the tracked PDF `cd report && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` (the gate only
   builds to `.build/`, so the committed `main.pdf` and `dag.pdf` must be regenerated by hand). Then `check-all`.
3. **Gate-hardening / hygiene** (were beads `aipm-iel`/`aipm-17f`/`aipm-qpa`): require quotes on the 8 quote-less
   `skip_noquote` externals; audit every `cited` result vs `refs/`, downgrade ungrounded (`thm-whitehead`,
   `prop-aut-compact` are PDF-only) `cited`→`grounded`; factor `lem-P-properties` if its workspace balloons.
4. **refs follow-ups:** seed the durable content-addressed cache (`fetch-refs.py --populate-cache`); decide the
   2 SUSPECT PDFs (re-derive + re-pin from authoritative origin → user sign-off, or drop); relativise the 2 stale
   `/home/tobias/...` paths in `report/PROVENANCE.md` to `refs/`. **report-sync:** the `coverage` warn
   (`lem-cstar-sa-to-epsjb` no per-claim PROVENANCE row) and the `B-ROUND` duplicate-key warn are still open.
5. **Open-math frontier** (hard, may need the user): Layer-1 coboundary splitting (`op-jordan-structure`/
   `op-layer1-gap`), NPPS/exposed-hull (`op-npps`/`op-exposed-hull`), matrix benchmark re-audit (`obs-matrix-audit`).
6. **Backlog:** general-`D` dilation via a Stinespring-stack bridge lemma (`aipm-us3`); af-friction PRs upstream
   `../vibefeld` (user-authorized); Phase-5 fresh Lean scaffold.

## Recipes (do exactly this)

**Recipe B — af per-lemma (PROVEN: bridge, 3 dilation sub-lemmas, thm-faithful-approx).** Drive the ready
frontier (`python3 scripts/argument.py`). Per lemma:
1. **Prep:** read the lemma shard + its report prose (`provenance` line range) + cited def shards. For every
   external fact, locate the verbatim `refs/` string (re-harvest reusable `GT-*` source strings byte-exact from
   a prior workspace, e.g. `proofs/lem-square-hole-almost-positive/externals/`). Output a proof kit (outline ·
   externals with loci + verbatim strings · node plan ≤12, depth ≤3 · groundability verdict G/A/R). Two derived
   facts may NOT be quotable (build them as proven nodes, not externals).
2. **Build (prover):** `af init -c "<contract VERBATIM>" -a <prover-id> -d proofs/<id>` (root must byte-match the
   registry contract). Seed defs (`af def-add`) + externals (`af add-external --name … --source "…VERBATIM: \"<refs
   bytes>\""` — COPY actual bytes, never from memory). Import a validated lemma as a black-box external (source =
   `Prior VALIDATED registry lemma … VERBATIM contract: "…"`, → `skip_import`). Hypotheses → one `GT-hyp`
   external (→ `skip_noquote`). Build with `af refine`; **`--depends` AT REFINE TIME** (declare ALL imported
   lemmas + parent nodes as deps — a missing direct edge IS a verifier challenge). Self-check
   `python3 scripts/check-refs.py --check` PASSES. Do NOT self-validate.
3. **Verify — ONE FRESH VERIFIER PER NODE (rule 3), sequential, leaves→root:** each verifier (distinct owner,
   role verifier) claims its single node, re-greps every refs leaf (FULL quote, R5; asterisk/whitespace-only
   mismatch is OK per check-refs normalization), confirms imports' hypotheses are satisfied, demands
   dimension-free constants, reproduces any counterexample (R7), then `af accept <n> --agent <vid>` (add
   `--confirm`) or `af challenge <n> --owner <vid> --target <…> --reason "…"`. Then exits.
4. **Resolve (prover, ≠ the verifier):** `af amend <n> --owner <prover> -s "…"` (statement only; pending nodes),
   then `af resolve-challenge <ch-id> -r "…"` (note: `-r` only, NO `-o`/owner flag; full `ch-…` id). af has no
   post-hoc dependency-edge command — if a missing-edge challenge can't be fixed without re-refining (which
   archives validated children), resolve by recording the transitive dep + amending the statement (precedent:
   `thm-faithful-approx` node 1.4). Re-verify with a NEW fresh verifier.
5. When all nodes validated+clean: `af export -d proofs/<id> > proofs/<id>/export.md` (+ `--format latex` →
   `export.tex`); set the shard `af: validated` (+ add any newly-discovered import to `deps`); `python3
   scripts/argument.py --check --generate`; do the Report upkeep (NEXT §2); commit (Recipe C). >12 nodes or
   depth >3 ⇒ STOP and factor a sub-lemma.

**Recipe D — capstone (assembly of validated lemmas, PROVEN on `thm-dilation-compatible`).** When a theorem
reduces to already-validated lemmas: `af init` with the contract; `af add-external` each dep lemma's contract
byte-verbatim (→ `skip_import`); `--depends` to the registry deps; thin assembly (~6–7 nodes) + a `GT-hyp`
external (`skip_noquote`). The verifier's #1 job: confirm each import's **hypotheses are satisfied** by the
parent's setup.

**Recipe C — gate / commit.** `python3 scripts/argument.py --check --generate`; then `sh scripts/check-all.sh`
(no active pre-commit hook here — run it BY HAND). One atomic validated result per commit; end the message with
the `Co-Authored-By` trailer; `git pull --rebase --autostash` then `git push`. (`bd dolt push` is skipped — beads
non-functional here.)

**Recipe A — add a registry shard.** Edit frontmatter (`id`==filename stem; `contract` one line; `defs`/`deps`
`;`-lists; `status`; `af: none`; `provenance`; `owner`; `workspace`). Every `def`/`dep` must resolve.
`argument.py --check --generate` → 0 errors. Commit.

## Key facts / gotchas
- **check-refs is law.** Every af-external citing a `refs/` locus embeds a verbatim quote that byte-matches
  (modulo whitespace/markdown-emphasis-asterisk normalization). Imports of validated lemmas = `skip_import`;
  the theorem's own hypotheses = `skip_noquote`. 8 quote-less externals still slip through as `skip_noquote`.
- **Report upkeep is manual.** `check-all` builds the report only into gitignored `report/.build/`; the tracked
  `report/main.pdf` and `report/figures/dag.pdf` are committed artifacts you must regenerate by hand (latexmk +
  `gen-dag-figure.py`) when sources/registry change. `gen-dag-figure.py` is deliberately NOT gate-wired. New
  validated results need their `\afbadge` + `tab:status` `af` tick + count bump added in lockstep.
- **af frictions:** no post-hoc dependency-edge command (declare `--depends` at refine; resolve missing-edge
  challenges via transitive recording, see Recipe B4); `resolve-challenge` takes `-r` only (no owner flag), full
  `ch-…` id; `af amend` edits statement text only and only on pending nodes; `af refine` rejects `--depends` with
  multiple statements; validated nodes can't be amended. Serialize af ops per workspace.
- **Templates:** `proofs/thm-faithful-approx` (10-node refs-grounded + a resolved dependency challenge),
  `proofs/lem-cstar-sa-to-epsjb` (multi-axiom O(η) crux), `proofs/lem-bridge-orderunit` (smallest),
  `proofs/thm-dilation-compatible` (capstone assembly).
- **Reviewer ≠ author cuts both ways (R7).** Verifiers catch fabrications AND can produce false claims;
  independently reproduce counterexamples. Numerics + a one-line proof are the cheap cross-check.
- **`refs/` trust tiers** (the `(open)`-honesty rule applies to ground truth): GENUINE = HOS/Idel (user-stored
  `../af-tests`, content-verified) + the 6 web-recovered (authoritative origin + hash); **SUSPECT = `kaup-1984`,
  `chu-russo-1512.03347`** (do NOT trust without re-deriving). All 4 af-cited sources are GENUINE.
- **Beads is non-functional in this clone** (empty DB, `issue_prefix` unset → `bd create` errors; no dolt remote
  → `bd dolt pull/push` fail). Use the linker (`argument.py`) as the frontier, not `bd`; skip `bd dolt push`;
  commits go directly to git on `main`. No active git pre-commit hook (`core.hooksPath` unset) — run `check-all`
  by hand. `agent-A/HANDOFF.md` MATH is current; its FILE MAP is stale (repo is `/home/tobias/...`).
