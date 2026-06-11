<!--
ROLE: crash-safe handoff for the argument-architecture build (branch main; feature branch retired).
UPDATE POLICY: rewritten (not appended) at each checkpoint; keep <=500 lines; git history holds old versions.
TRIGGER: end of a work session / before a push / when phase status changes.
NOTE: this tracks the REORG/ARCHITECTURE + af-proof build. For the MATH status see PRD.md §math + agent-A/HANDOFF.md.
-->

# HANDOFF — argument-architecture build

> ## START HERE (next agent)
> 0. **Which lane?** If you are **Agent B (exploration / scoping)**, read
>    **`docs/plans/2026-06-07-agent-b-rules-of-engagement.md`** (mirrored in `agent-B/README.md`) FIRST — your
>    sandbox lane (`agent-B/**`, `docs/plans/`, `docs/worklog.md`) + do-not-touch list (validated `proofs/<id>/`,
>    generated files, locked defs, `status:`/`af:` upgrades). Reach the canonical layers ONLY via Recipe A→B.
> 1. `git checkout main` (all work lives on `main`).
> 2. Read, in order: **`PRD.md`** → **`CLAUDE.md`**(==`AGENTS.md`) → **this file** → `definitions/INDEX.md`
>    + `argument/INDEX.md` + `argument/DAG.md`. `python3 scripts/argument.py` prints the ready/blocked frontier;
>    **beads WORKS here** (`bd ready`, `bd show <id>`) — use it.
> 3. **16 results are `af: validated`** (`grep -c validated argument/INDEX.md`). The bridge (9), dilation (4:
>    `thm-dilation-compatible`+3), `thm-faithful-approx`, `lem-classical-equiv`, and **NEW `prop-direct-sum`**
>    (first feeder of the Layer-1 `cor-adjoint-benchmark` cluster — see below).
> 4. **ACTIVE CAMPAIGN: af-validate the `cor-adjoint-benchmark` cluster** (epic **`aipm-brd`**) — the master
>    exact-adjoint Jordan-coboundary inversion, the most advanced prose-proved result on the critical path to
>    Layer-1 (`op-jordan-structure`/`op-layer1-gap`). Five pieces, status:
>    - `prop-direct-sum` (`aipm-bb4`) — ✅ **DONE** (validated, committed, pushed this session).
>    - `prop-spin-splitting` (`aipm-8zc`) — kit ready (`proofs/prop-spin-splitting/orchestration/PROOF-KIT.md`,
>      verdict G, 11-node plan). **Build ATTEMPT 1 FAILED** (af `--dry-run` friction + stall); workspace scrapped,
>      **REBUILD next** (see NEXT §1 + the `--dry-run` gotcha).
>    - `prop-comm-scalar` (`aipm-0r4`) — kit ready but **OVER BUDGET** (14 nodes/depth 6); must **factor into ~4
>      sub-lemmas first** (`aipm-0wn`, Recipe A) before building.
>    - `thm-matrix-splitting` (`aipm-l3y`) — soundness audit DONE → **`NEEDS-REFORMULATION`** (`aipm-q85`): sound,
>      `C` genuinely n-independent, log-Schur stress test is NOT a counterexample (the `obs-matrix-audit`/`aipm-36d`
>      re-audit is resolved: no cb-gap), BUT the **quaternionic mixed-sector twirl is asserted-not-derived** (must
>      be expanded), `C` should read "universal" not 60/84/124, and it must factor into ~8 sub-lemmas.
>    - `cor-adjoint-benchmark` (`aipm-i4g`) — capstone (Recipe D), blocked on the four.
>    **OPEN USER DECISION (matrix):** A = honest maximal progress (reformulate + build R/C/leakage/detection
>    sub-lemmas, attempt quaternionic last); B = quaternionic-first; C = feeders-only, defer matrix. Default **A**.
> 5. **The report is the human-readable front door** (`report/main.pdf`): green `✓ af-validated` badges per result.
>    **Report upkeep for newly-validated results is BATCHED** (`aipm-6ct`) — `prop-direct-sum` does NOT yet have its
>    `\afbadge`/`tab:status` tick (check-all passes regardless: `status drift OK` = underclaim-safe). Do the batch
>    (badges + counts + `gen-dag-figure.py` + tracked `main.pdf`) when the clean feeders land.
> 6. Sanity-check: `sh scripts/check-all.sh` must print `[check-all] OK`. **There IS an active pre-commit hook**
>    that runs `check-all` on every `git commit` (so commits are auto-gated; latexmk build included). Fresh clone
>    with absent `refs/`: `python3 scripts/fetch-refs.py` (18/51 arXiv-pinned + hash-verified, now incl.
>    `baake-sumner-2007.11433`); `AIPM_REFS_CACHE=<dir> python3 scripts/fetch-refs.py` restores the bespoke residue.

> **CLASSICAL-PORTFOLIO MERGED TO MAIN (2026-06-11).** Agent A's classical campaign
> (the sidequest toward `op-classical`/`op-exposed-hull`) is now part of main per user
> direction. Entry point: **`agent-A/explorations/classical-portfolio/OVERVIEW.md`**
> (the twice-reviewed bird's-eye map: conjectures in plain terms, the full strategy
> map with statuses, the frontier). Its current state: four hostile-audited lemmas
> (the variety programme), the local-linear-law assembly broken by audit (the open
> piece), certified above-corner antecedent instances, and a fresh lead (H-M Theorem
> 1.12, the signed structure theorem — worker in flight). Kernel bead: `aipm-3u6`.

**Branch:** `main`. **Date:** 2026-06-09. **Approved design:** `docs/plans/2026-06-05-argument-architecture-plan.md`.
Mental model: definitions = types · each lemma (af workspace) = a module whose *contract* is its one-line
statement · a linker enforces the DAG.

## Governing rules (user) — non-negotiable
1. **No "standard facts"/"citations".** The ONLY ground truth is a **byte/string match to a LOCAL `refs/`
   source** (enforced by `scripts/check-refs.py`). Not in `refs/` ⇒ **STOP**; never paraphrase from memory. You
   MAY dispatch researchers to FIND an authoritative byte-extractable source + propose adding it (manifest +
   sha256 + `sources.lock.json`); the binding step is still a local byte-match. (Done this session for
   `baake-sumner-2007.11433`.)
2. **"A derivation = lemma = af".** Every non-leaf fact is an af-validated DERIVED node (bottoming at refs leaves
   or imported validated lemmas), not asserted "elementary".
3. **One fresh verifier per node.** In the af verify step, spawn a SINGLE fresh verifier subagent for EVERY node —
   one node, verify, exit. Never one verifier across multiple nodes (max reviewer independence). Serialize af ops
   per workspace (run verifiers sequentially, leaves→root). **PROVEN this session at scale on `prop-direct-sum`
   (10 nodes, background subagents).**

## DONE (latest — 2026-06-09, committed + pushed to `main`)
- **`prop-direct-sum` COMPLETE (`af: validated`)** — the 16th validated result; first feeder of the
  `cor-adjoint-benchmark` cluster. The summand-count-free exact-adjoint direct-sum coboundary splitting (constant
  `max_r K_r + 1`, no m-dependence, adjoint/block-respecting modules). **10-node af workspace** (depth 3),
  orchestrated via **background subagents**: a groundability scout (verdict G, 4 HOS externals byte-matched:
  order-unit norm 1.2.1, JB unit-norm 3.1.4, JB-is-order-unit 3.3.10, central-idempotent-summand 2.5.7) → 1 prover
  → **10 fresh per-node verifiers** (leaves→root). **One challenge** (node 1.7 under-declared its transitive use of
  node 1.5's norm bound) caught by a fresh verifier, **resolved** by a prover≠challenger (statement-only amend
  recording 1.5 + root assembly; `thm-faithful-approx` 1.4 precedent), **re-verified clean** by a third agent.
  Commit `52110bd`. LESSON: declare EVERY cross-node dependency (incl. constant-supplying nodes) at refine time.
- **Matrix soundness audit DONE → `NEEDS-REFORMULATION`** (`thm-matrix-splitting`, `aipm-l3y`/`aipm-q85`). A
  read-only adversarial audit + numerics (front-loaded to de-risk the suspect node BEFORE building). Verdict:
  **sound** — `C` genuinely n-independent; the matching-curvature DETECTION identity verified to machine precision
  (arbitrary matrix → full Schur multiplier, so NO ordinary-vs-cb amplification gap); the **log-Schur stress test
  is NOT a counterexample** (`dist/‖f‖` ratio flat ~1.3) ⇒ **`obs-matrix-audit`/`aipm-36d` re-audit RESOLVED**. But
  NOT build-ready: (1) quaternionic mixed-sector twirl + scalar-amplification lemma are **asserted-not-derived**
  (expand before any checkmark); (2) state `C` as "universal", drop per-sector numerals 60/84/124 from the
  contract; (3) factor into ~8 sub-lemmas. Full plan in `aipm-q85`.
- **refs: added `baake-sumner-2007.11433`** (Baake–Sumner, *On equal-input and monotone Markov matrices*,
  J. Appl. Probab. 2022) as byte-greppable `.tex` (arXiv e-print source, hash `f358c71c…`, fetch-reproducible).
  Idempotent Markov-matrix structure (min poly `x(x−1)`, extremal idempotents `E_1..E_d`, equal-input idempotents)
  for the **commutative case** (`op-classical`/`def-stochastic`/`thm-simplex`). Manifest + `test_fetch_refs.py`
  counts updated (50→51 files, 17→18 fetch-reproducible); check-all green.
- **Stale-HANDOFF facts CORRECTED:** beads is **fully functional** here (embedded-dolt + git-backed `origin`
  remote; `bd create`/`close`/`dep`/`export` all work) — *use it*; there **IS an active pre-commit hook** running
  `check-all` on every commit. (Both were wrongly listed as broken in the prior HANDOFF.)

## DONE (earlier — context; full narrative in docs/worklog.md)
- `lem-classical-equiv` (15th), `thm-faithful-approx` (14th), `thm-dilation-compatible` (cond. O(η)) + 3 sub-lemmas,
  the 9-lemma algebraic bridge. `check-provenance.py` report-sync gate. Reproducible `refs/` (`fetch-refs.py`).
  SUSPECT refs (`kaup-1984`, `chu-russo-1512.03347`) flagged, not af-cited.

## NEXT (priority order)
1. **Finish the `cor-adjoint-benchmark` cluster** (epic `aipm-brd`):
   - **REBUILD `prop-spin-splitting`** (`aipm-8zc`) — kit is ready & verdict G (11 nodes, two sub-trees:
     right-inverse + next-arrow). Clean `af init`; follow the kit; **do NOT pass `--dry-run` to `af refine`** (it
     mutates state — `aipm-rdx`); declare ALL cross-node deps at refine. Then 11 fresh per-node verifiers.
   - **FACTOR + build `prop-comm-scalar`** (`aipm-0r4`/`aipm-0wn`) — register ~4 sub-lemma shards (Recipe A,
     reviewer≠author): `-classification` (load-bearing module decomposition), `-rightinv` (norm-one S, ‖Π‖≤3),
     `-coord-nextarrow` (≤2), `-halfsum-nextarrow` (≤12); make `prop-comm-scalar` a thin assembly; build each.
     HOS has NO module theory — derive the classification, never cite HOS for it (arena-gap risk).
   - **`thm-matrix-splitting`** (`aipm-l3y`/`aipm-q85`) — once the user picks A/B/C: reformulate the contract
     (Recipe A), factor into ~8 sub-lemmas, expand the quaternionic twirl (the hardest node), build. The new
     `baake-sumner` ref may help the commutative pieces.
   - **`cor-adjoint-benchmark`** (`aipm-i4g`) — capstone (Recipe D) once the four feeders validate.
2. **Batch report upkeep** (`aipm-6ct`): `\afbadge` + `tab:status` `af` ticks + count bumps for the newly-validated
   feeders, `python3 scripts/gen-dag-figure.py`, rebuild tracked `report/main.pdf`. Do before declaring the cluster done.
3. **Gate-hardening / hygiene** (`aipm-iel`/`aipm-17f`/`aipm-qpa`): quotes on the 8 `skip_noquote` externals;
   audit `cited` results vs `refs/`, downgrade ungrounded (`thm-whitehead`, `prop-aut-compact` PDF-only).
4. **refs follow-ups** (`aipm-18d`): more classical-layer sources if needed (matrix norms/convexity); seed the
   content-addressed cache (`fetch-refs.py --populate-cache`); decide the 2 SUSPECT PDFs. report-sync warns
   (`lem-cstar-sa-to-epsjb` coverage, `B-ROUND` dup key) still open.
5. **Open-math frontier** (hard): Layer-1 (`op-jordan-structure`/`op-layer1-gap`), NPPS/exposed-hull
   (`op-npps`/`op-exposed-hull`). The classical chain (`thm-rank-one`/`thm-simplex`/`prop-approx-simplex`) is also
   ready (depends on validated `lem-classical-equiv`) — a separate, high-throughput continuation off the critical path.
6. **Backlog:** general-`D` dilation (`aipm-us3`); af-friction PRs upstream `../vibefeld` (user-authorized — the
   `--dry-run` bug `aipm-rdx` is a candidate); Phase-5 Lean scaffold.

## Recipes (do exactly this)

**Recipe B — af per-lemma (PROVEN: bridge, dilation, faithful-approx, classical-equiv, prop-direct-sum).**
1. **Prep (scout):** read the lemma shard + report prose + def shards. For every external, locate the verbatim
   `refs/` string (re-harvest reusable `GT-*` strings byte-exact, e.g. `proofs/prop-direct-sum/externals/`).
   Output a proof kit (outline · externals w/ loci+verbatim · node plan ≤12, depth ≤3 · verdict G/A/R).
2. **Build (prover):** `af init -c "<contract VERBATIM>" -a <prover-id> -d proofs/<id>` (root byte-matches the
   registry contract). `af def-add` (PLAIN-TEXT content — NO leading `---`, it's parsed as a flag) + `af add-external
   --source "…VERBATIM: \"<refs bytes>\""` (COPY bytes via grep). Import a validated lemma as black-box external
   (`skip_import`); hypotheses → one `GT-hyp` (`skip_noquote`). Build with `af refine`; **`--depends` AT REFINE
   TIME — declare ALL deps incl. any node whose result/constant this node's conclusion uses** (a missing edge IS a
   challenge — happened on `prop-direct-sum` 1.7). **NEVER `af refine --dry-run`** (it creates the node anyway —
   `aipm-rdx`). Self-check `python3 scripts/check-refs.py --check` PASSES. Do NOT self-validate.
3. **Verify — ONE FRESH VERIFIER PER NODE (rule 3), sequential, leaves→root:** each verifier (distinct owner,
   `--role verifier`) claims its node, re-greps every refs leaf (FULL quote), confirms imports' hypotheses,
   demands dimension-free constants, reproduces any counterexample (R7), then `af accept <n> --agent <vid>
   --confirm` (clean node needs `--confirm`) or `af challenge <n> --owner <vid> --target <…> --reason "…"`, then
   `af release <n> --owner <vid>`. The ROOT is discharged by its refinement children (no explicit `--depends` —
   verify the SYNTHESIS, not edge syntax; precedent `prop-direct-sum`/`lem-bridge-orderunit`).
4. **Resolve (prover ≠ the verifier):** `af amend <n> --owner <prover> -s "…"` (statement only; pending nodes),
   then `af resolve-challenge <ch-id> -r "…"` (`-r` only, full `ch-…` id). No post-hoc edge command — record a
   missing transitive dep in the statement prose (precedent `prop-direct-sum` 1.7, `thm-faithful-approx` 1.4).
   Re-verify with a NEW fresh verifier (≠ author, ≠ challenger).
5. When all nodes validated+clean: `af export -d proofs/<id> > proofs/<id>/export.md` (+ `--format latex`); set the
   shard `af: validated` (+ add any newly-found import to `deps`); `python3 scripts/argument.py --check --generate`;
   commit (Recipe C); batch the report upkeep (`aipm-6ct`). >12 nodes or depth >3 ⇒ STOP and factor a sub-lemma.

**Recipe D — capstone (assembly of validated lemmas, PROVEN on `thm-dilation-compatible`).** `af init` w/ the
contract; `af add-external` each dep lemma's contract byte-verbatim (`skip_import`); `--depends` to the registry
deps; thin assembly (~6–7 nodes) + a `GT-hyp` (`skip_noquote`). Verifier's #1 job: confirm each import's
**hypotheses are satisfied** by the parent's setup.

**Recipe C — gate / commit.** `python3 scripts/argument.py --check --generate`; one atomic validated result per
commit; end the message with the `Co-Authored-By` trailer. **The pre-commit hook runs `check-all` automatically**
(let it; do NOT bypass with `core.hooksPath`). `git pull --rebase --autostash` then `git push`. Beads syncs via
git-tracked `.beads/issues.jsonl` (`bd export -o .beads/issues.jsonl` before committing if you changed issues) +
`bd dolt push` (works — git-backed `origin` remote).

**Recipe A — add a registry shard.** Edit frontmatter (`id`==filename stem; `contract` one line; `defs`/`deps`
`;`-lists; `status`; `af: none`; `provenance`; `owner`; `workspace`). Every `def`/`dep` resolves.
`argument.py --check --generate` → 0 errors. Reviewer≠author for new shards. Commit.

## Key facts / gotchas
- **check-refs is law.** Every af-external citing a `refs/` locus embeds a verbatim quote that byte-matches (modulo
  whitespace/markdown-asterisk normalization). Imports = `skip_import`; hypotheses = `skip_noquote`.
- **Beads WORKS** (embedded-dolt; git-backed `origin` remote; `.beads/issues.jsonl` git-tracked). Use `bd ready`/
  `bd show`/`bd create`/`bd dep`/`bd close`. `bd doctor`/`bd dolt status` say "unsupported in embedded mode" — that
  is EXPECTED, not breakage. Sync: `bd export -o .beads/issues.jsonl` + commit + `bd dolt push`.
- **Active pre-commit hook** runs `check-all` (incl. latexmk) on every commit — commits are auto-gated.
- **af frictions:** **`af refine --dry-run` STILL CREATES the node** (mutates state — `aipm-rdx`; never use it); no
  post-hoc dependency-edge command (declare `--depends` at refine; resolve missing-edge challenges via transitive
  prose recording, Recipe B4); `resolve-challenge` takes `-r` only, full `ch-…` id; `af accept` on a clean (un-
  challenged) node needs `--confirm`; `af amend` edits statement text only, pending nodes only; `af def-add` chokes
  on content starting with `---`; validated nodes can't be amended. Serialize af ops per workspace.
- **Report upkeep is manual + BATCHED** (`aipm-6ct`). `check-all` builds only to gitignored `report/.build/`; the
  tracked `report/main.pdf` + `report/figures/dag.pdf` are committed artifacts regenerated by hand (latexmk +
  `gen-dag-figure.py`). `status drift OK` means a validated-but-unbadged result does NOT fail the gate (underclaim-safe).
- **Templates:** `proofs/prop-direct-sum` (10-node, background-subagent-orchestrated, 1 resolved dep challenge —
  freshest worked example), `proofs/lem-classical-equiv` (11-node, cleanest 0-challenge), `proofs/thm-faithful-approx`
  (resolved dep challenge), `proofs/lem-bridge-orderunit` (smallest), `proofs/thm-dilation-compatible` (capstone).
- **Reviewer ≠ author cuts both ways (R7).** Verifiers catch fabrications AND can produce false claims (e.g. the
  `prop-direct-sum` 1.7 verifier mis-flagged a 1.7.2 "artifact" by reading a superseded ledger entry — check live
  state). Independently reproduce counterexamples; numerics + a one-line proof are the cheap cross-check.
- **`refs/` trust tiers:** GENUINE = HOS/Idel + the web-recovered arXiv-pinned (incl. new `baake-sumner`);
  **SUSPECT = `kaup-1984`, `chu-russo-1512.03347`** (do NOT trust without re-deriving). All af-cited sources GENUINE.
- `agent-A/HANDOFF.md` MATH is current; its FILE MAP/paths are stale (repo is `/home/tobias/...`).
