<!--
ROLE: crash-safe handoff for the argument-architecture build (now on branch main; the feature branch was retired).
UPDATE POLICY: rewritten (not appended) at each checkpoint; keep <=500 lines; git history holds old versions.
TRIGGER: end of a work session / before a push / when phase status changes.
NOTE: this tracks the REORG/ARCHITECTURE + af-proof build. For the MATH status see PRD.md §math + agent-A/HANDOFF.md.
-->

# HANDOFF — argument-architecture build

> ## START HERE (next agent)
> 1. `git checkout main` (the work lives on `main`; the `argument-architecture` feature branch was retired).
> 2. Read, in order: **`PRD.md`** → **`CLAUDE.md`**(==`AGENTS.md`) → **this file** → `definitions/INDEX.md`
>    + `argument/INDEX.md` + `argument/DAG.md` (the live state). `bd ready` = the work frontier.
> 3. **TWO THEOREMS ARE NOW MACHINE-VALIDATED (af, A+B consensus):**
>    - **The algebraic bridge `thm-bridge`** (the √η general result) — its 9-lemma DAG (`lem-P-properties`,
>      `lem-bridge-orderunit`, `lem-first-insertion`, `lem-square-hole-almost-positive`, `lem-bridge-easy`,
>      `lem-bridge-polar`, `lem-bridge-onehole`, `prop-bridge-jordan`, `thm-bridge`).
>    - **The dilation-compatible `thm-dilation-compatible`** (the conditional **O(η)** Kitaev-strength result)
>      — NEW this session: 3 factored sub-lemmas + the capstone, all `af: validated`:
>      `lem-idempotence-inheritance`, `lem-intertwine-spectral-idempotent`,
>      `lem-cstar-sa-to-epsjb` (the **O(η) crux** — C\*→JB symmetrisation), `thm-dilation-compatible`.
>    **13 results are `af: validated` total.** `grep -c validated argument/INDEX.md`.
> 4. Sanity-check: `sh scripts/check-all.sh` must print `[check-all] OK` (check-defs + **check-refs** +
>    linker + **check-provenance** (report↔registry sync + latexmk build) + tests). Now GREEN here (20/50 refs
>    present). On a fresh clone with absent `refs/` payloads, REBUILD reproducibly: `python3 scripts/fetch-refs.py`
>    fetches the **17/50 authoritative-origin-pinned** sources (kitaev, vlw, effros-størmer, baak-moslehian,
>    blecher-read) hash-verified; `AIPM_REFS_CACHE=<dir> python3 scripts/fetch-refs.py` restores the bespoke
>    residue from a content-addressed cache (seed once with `--populate-cache <dir>`, mirror durably). See the
>    genuineness audit + SUSPECT list (`kaup`, `chu-russo`) in DONE/gotchas. Beads is still empty here (no dolt
>    remote, `issue_prefix` unset) — an environment-provisioning gap, not a code regression.
> 5. **What to do next is in beads (`bd ready`).** Top of the queue: the **classical layer** (`aipm-9mw` split
>    the `lem-leakage` contract → then af `lem-leakage`/`lem-classical-equiv`; `aipm-18d` acquire the scouted
>    sources); **`aipm-iel`** (P1, harden check-refs skip_noquote); **`aipm-17f`** (`cited`→`grounded` audit);
>    **`aipm-qpa`** (factor `lem-P-properties`). Open-math frontier: `aipm-245`/`aipm-08u`/`aipm-36d`.
> 6. Live recipes below: **Recipe B** (af per-lemma), **Recipe D** (capstone = assembly of validated lemmas),
>    **Recipe C** (gate/commit), **Recipe A** (add a registry shard).

**Branch:** `main` (single branch; `argument-architecture` retired). **Date:** 2026-06-07. **Approved design:**
`docs/plans/2026-06-05-argument-architecture-plan.md`. Mental model: definitions = types · each lemma (af
workspace) = a module whose *contract* is its one-line statement · a linker enforces the DAG.

## Two governing rules (user, 2026-06-06) — non-negotiable
1. **No "standard facts"/"citations".** The ONLY ground truth is a **byte/string match to a LOCAL `refs/`
   source** (enforced by `scripts/check-refs.py`). If a fact is not in `refs/`, **STOP** — do not paraphrase
   from memory. You MAY dispatch researcher subagents to FIND an authoritative byte-extractable source and
   propose adding it to `refs/` (manifest + sha256), but the binding step is still a local byte-match.
2. **"A derivation = lemma = af".** Every non-leaf fact is an af-validated claim (a node; if reusable/
   substantial, its own registry lemma). Pure-algebra/definition-unfolding steps are DERIVED af nodes
   (bottoming at refs leaves or imported validated lemmas), not asserted "elementary".

## DONE (this session, 2026-06-07 — all committed + pushed to `main`)
- **`thm-dilation-compatible` COMPLETE** (the conditional O(η) result). Restructured from a brittle 1-theorem
  scaffold into 3 factored sub-lemmas + capstone (per L3), each prover(agent-B)→fresh-verifier(agent-A):
  - `lem-idempotence-inheritance` — `‖Φ²−Φ‖≤‖F²−F‖` (constant **exactly 1**); the R7 fact.
  - `lem-intertwine-spectral-idempotent` — `θ(2F−1)j = jθ(2Φ−1)` (functional-calculus intertwining).
  - `lem-cstar-sa-to-epsjb` — **the O(η) crux**: the sa-part of Kitaev's extended O(η)-C\*-algebra under the
    symmetrised product is O(η)-ε-JB; JB4 at O(η) from Kitaev's `ax_assoc=O(η)` (n=4 pentagon reassociation),
    JB3 via concrete UCP.
  - `thm-dilation-compatible` (capstone) — 7-node assembly importing the 3 + `lem-P-properties`.
- **Honest scope decision (user):** the dilation space is **restricted to `D=B(K)`** (a full matrix algebra —
  the natural Stinespring dilation target), so `lem-cstar` (UCP on B(H)) applies verbatim. The general
  finite-dim C\* `D=⊕Mₙ` case is **deferred** (`aipm-us3`): `⊕B(Lⱼ)` is a *proper* subalgebra of `B(K)`, and
  Kitaev's two-hole estimate uses a Stinespring stack instantiated only over full `B(Hₙ)` — widening needs a
  bridge lemma re-deriving that stack at finite-dim-C\* generality (C\*-generic core confirmed, `aipm-q8i`).
- **Branch consolidated:** `argument-architecture` (30 commits ahead) fast-forwarded onto `main`; feature
  branch deleted local+remote; default stays `main`.
- **LEARNINGS R7** (a fresh *verifier* produced a confident, plausible, WRONG counterexample — "false premise"
  on `lem-idempotence-inheritance` — refuted by a 7M-sample sweep + a one-line proof). New standing lesson:
  *a refutation is itself a claim; reproduce it before acting.* Also caught (and corrected before commit) a
  bad **Wedderburn shortcut** I tried (`D≅B(K)` is false for ≥2 summands) — the adversarial loop works.
- **Classical-layer sources scouted** (`aipm-18d`): MIT OCW 6.241J Ch.4 (matrix norms), Boyd & Vandenberghe
  (convexity/simplex/stochastic) — open + byte-extractable; acquire when the classical lemmas come up.
- **`check-provenance.py` report-sync gate built + wired into check-all** (was `aipm-oql`; the report build +
  a sync gate). Errors (block commit): every registry `provenance: report <label>` resolves to a `\label{}`;
  every PROVENANCE per-claim label resolves; every per-claim Source key is defined; every IN-REPO source
  sha256[:16] is fresh; **status OVERCLAIM** (a `status:open` result framed proved in `tab:status`) — the #1
  guarded failure mode; `latexmk` compiles with no undefined refs (built into gitignored `report/.build/`, so
  the tracked `main.pdf` is never mutated). Warnings: reverse/anchor/coverage/underclaim/parse-integrity/absent
  payloads. Join key = the shard `provenance:`'s `report <label>` token (+ first-hyphen→colon fallback). 52
  red→green tests (`test_check_provenance.py`). 3-agent adversarial review (reviewer≠author) hardened it:
  promoted overclaim WARN→ERROR, hash ALL source rows (caught a silent `B-ROUND` dup), strip `%`-comments in
  label/status harvesting, anchor check, loud parse-integrity. Fixed a real `A-ER` 15→16-hex sha typo it
  surfaced. KNOWN LIMITS (documented in the gate docstring): statement/contract TEXT not compared; status sync
  only covers `tab:status`-listed results; ~⅓ of sources hash-unverifiable (gitignored).
- **Reproducible `refs/` reconstruction + web recovery (`fetch-refs.py` + `sources.lock.json`).** `refs/` is no
  longer machine-bound: `python3 scripts/fetch-refs.py` rebuilds it on any clone, hash-verifying every byte.
  **17/50 fetch-reproducible from authoritative origins** (kitaev+vlw arXiv e-prints/pdfs; Effros–Størmer source
  PDF from official Math. Scand.; Baak–Moslehian arXiv `math/0501158`; Blecher–Read arXiv `1905.05836` source).
  The bespoke residue restores from a content-addressed cache `$AIPM_REFS_CACHE/<sha256>` (seed once with
  `--populate-cache <dir>`, mirror durably). **20/50 present locally now → `check-all` GREEN** (was failing on
  absent refs; all 4 af-cited sources HOS/Kitaev/Idel/VLW present). 16 offline tests in check-all.
- **Genuineness audit (user: prior agents may have fetched wrong/hallucinated files — high bar).** Fetching from
  an authoritative origin + hash-match IS a genuineness proof. Verdict: GENUINE = HOS (user-stored canonical in
  `../af-tests`, hash `28740e73`; scan title = real H-O–Størmer book; the 21 proof-cited passages are correct
  standard math), Idel (real 2013 TUM thesis), and the 6 web-recovered sources. **SUSPECT** (could NOT verify vs
  any authoritative origin) = `kaup-1984` + `chu-russo-1512.03347` PDFs — NOT cited by any af proof (chu-russo
  only backs the already-flagged `thm-whitehead`); flagged, not trusted. The ~28 Effros–Størmer OCR pages /
  text extractions are locally-derived, not byte-reproducible by fetch.

## NEXT (priority order — see `bd ready`)
1. **Classical layer** — `aipm-9mw` (split `lem-leakage`'s contract: the leakage bound is groundable; the
   "no O(η) closure" sharpness should depend on the existing `ex-hume`), then af `lem-leakage` +
   `lem-classical-equiv`. Ground elementary finite-dim facts by inline derivation from Kitaev's general
   operator-norm def (`approximate_algebras.tex:638-642`) + `def-stochastic`, OR acquire the `aipm-18d`
   sources first (matrix norms = MIT OCW; convexity/stochastic = Boyd & Vandenberghe). This unblocks the
   classical-stability chain (`thm-simplex`/`thm-cluster`/`thm-classical-factorization`).
2. **`aipm-iel` (P1).** Harden `check-refs`: 8 externals cite a `refs/` locus but embed NO verbatim quote
   (→ `skip_noquote`, unchecked); retrofit `lem-P-properties`' quote-less externals; require quotes.
3. **`aipm-17f`.** Audit every `cited` result vs `refs/`; downgrade the ungrounded (`thm-whitehead`,
   `prop-aut-compact` are PDF-only); rename `cited`→`grounded`.
4. **`aipm-qpa`** (factor `lem-P-properties`) · **`aipm-9ho`** (byte-verify draft defs) · ~~`aipm-oql`
   (report `latexmk` + check-provenance into check-all)~~ **DONE** · **`aipm-chn`** (reorg theory/experiments).
   Follow-ups surfaced this session (file as beads when the tracker is restored): **(refs)** seed the durable
   content-addressed cache so the bespoke residue reproduces anywhere (`fetch-refs.py --populate-cache`); decide
   on the 2 SUSPECT PDFs — re-derive `kaup-1984` (mscand `12043`) + `chu-russo-1512.03347` (arXiv source) from
   the authoritative origin and **re-pin** their manifest hashes (a ground-truth change → user sign-off), or drop
   them; relativise the 2 stale `/home/tobias/...` source paths in `report/PROVENANCE.md` to `refs/` (now that
   those payloads are present they'd hash-verify). **(report-sync review)** a `tab:status` coverage warn for
   un-listed results; cross-check absent source hashes vs `refs/manifest/checksums.sha256`.
5. **Open-math frontier** (hard, may need the user): `aipm-245` (Layer-1 coboundary splitting), `aipm-08u`
   (NPPS/exposed-hull), `aipm-36d` (matrix benchmark re-audit). **`aipm-3ox`** = Phase-5 fresh Lean scaffold.
6. **Backlog:** `aipm-us3` (general-D dilation via the Stinespring-stack bridge lemma) · `aipm-on1`/`aipm-1pd`
   (af friction PRs upstream `../vibefeld`, user-authorized).

## Recipes (do exactly this)

**Recipe B — af per-lemma (PROVEN over the bridge + 3 dilation sub-lemmas).** Drive the ready frontier
(`python3 scripts/argument.py` prints it). Per lemma:
1. **Prep (sonnet):** read the lemma shard + its prose (`provenance` line range) + the cited def shards; for
   every external fact, locate the verbatim `refs/` string. Output a "proof kit" (outline · externals with
   loci + verbatim strings · node plan ≤12, depth ≤3 · ungrounded flags · GROUNDABILITY VERDICT G/A/R).
2. **Build (opus prover):** `af init -c "<contract VERBATIM>" -a <agent> -d proofs/<id>` (root must byte-match
   the registry contract). Seed defs (`af def-add`) + externals: **COPY actual `refs/` bytes** into the
   `VERBATIM:` quote — NEVER from memory. Import a validated lemma as a black-box external (no refs quote).
   Build (`af refine`, `--depends` AT REFINE TIME). **Self-check** `check-refs.py --check | grep <id>` PASSES.
   Do NOT self-validate.
3. **Verify (opus, FRESH verifier ≠ prover, per node, sequential — af not concurrency-safe in a workspace):**
   re-grep every refs leaf (FULL quote, not substring — R5); check imports satisfy their lemma contracts;
   demand universal/dimension-free constants; **reproduce any counterexample before believing it (R7)**.
   `af claim <n> -o v<r>-<n> -r <verifier>` → `af challenge`/`af accept --confirm`. Leaves → parents → root.
4. **Resolve (prover):** address challenges (`af amend` pending / `af resolve-challenge <full-id> -r "…"` for
   validated). Re-verify fresh (≠ resolver).
5. When all nodes validated+clean: set shard `af: validated`, `argument.py --check --generate`, commit (C).
   >12 nodes or depth >3 ⇒ STOP and factor a sub-lemma.

**Recipe D — capstone (assembly of validated lemmas, PROVEN on `thm-dilation-compatible`).** When a theorem
reduces to already-validated lemmas: `af init` with the contract; `af add-external` each dep lemma's contract
**byte-verbatim** (→ `skip_import`, no refs quote); declare `--depends` to the registry deps; build a thin
assembly (~6–7 nodes) + a `GT-hyp` external for the theorem's own hypotheses (`skip_noquote`). The verifier's
#1 job: confirm each import's **hypotheses are satisfied** by the parent's setup (this is where the dilation
capstone hit — and the verifier caught — the `B(H)` vs general-`D` and the false-Wedderburn gaps).

**Recipe C — gate / commit.** `python3 scripts/argument.py --check --generate`; commit (the pre-commit hook
re-runs `check-all` = check-defs + **check-refs** + linker + tests). One atomic validated result per commit;
push. `git pull --rebase --autostash` before `git push`; `bd dolt push` syncs beads.

**Recipe A — add a registry shard.** Edit frontmatter (`id`==filename stem; `contract` one line; `defs`/`deps`
`;`-lists; `status`; `af: none`; `provenance`; `owner`; `workspace`). Every `def`/`dep` must resolve.
`argument.py --check --generate` → 0 errors. Commit.

## Key facts / gotchas
- **check-refs is law.** Every af-external citing a `refs/` locus embeds a verbatim quote that byte-matches.
  Imports of validated lemmas are `skip_import`; the theorem's own hypotheses are `skip_noquote` (legitimate).
  8 quote-less externals still slip through as `skip_noquote` (→ `aipm-iel`).
- **af frictions** (PRs `aipm-on1`/`aipm-1pd`): no post-hoc `af depend` (use `--depends` at refine); `af
  challenges` truncates IDs but `resolve-challenge` needs the FULL id (via `-f json`); `af challenge` takes no
  `--owner` (ownership from the prior `af claim`); `af refine` rejects `--depends` with multiple statements;
  validated nodes can't be amended (`resolve-challenge` instead). Serialize af ops per workspace; different
  workspaces parallelize fine.
- **Templates:** `proofs/lem-cstar-sa-to-epsjb` (a real multi-axiom proof with the O(η) reassociation crux),
  `proofs/lem-bridge-orderunit` (smallest/exact), `proofs/thm-dilation-compatible` (capstone assembly).
- **Reviewer ≠ author cuts both ways (R7).** Verifiers catch fabrications AND can produce false claims;
  independently reproduce counterexamples. Numerics + a one-line proof are the cheap cross-check.
- **Task tracking is beads only** (`bd ready`/`bd show`/`bd close`). `agent-A/HANDOFF.md` MATH is current; its
  FILE MAP is stale (repo is `/home/tobias/...`, refs deduped into `refs/`).
- **`refs/` is reproducible, not machine-bound (this session).** `refs/manifest/sources.lock.json` + `fetch-refs.py`
  rebuild `refs/` hash-verified; `refs/` payload stays gitignored. 17/50 fetch from authoritative origins; the rest
  need `$AIPM_REFS_CACHE`. **Trust tiers** (the `(open)`-honesty rule applies to ground truth too): GENUINE =
  HOS/Idel (user-stored in `../af-tests` + content-verified) and the 6 web-recovered (authoritative origin + hash);
  **SUSPECT = `kaup-1984`, `chu-russo-1512.03347`** (recorded bytes match no authoritative source — do NOT trust
  without re-deriving). All 4 af-cited sources (HOS, Kitaev, Idel, VLW) are GENUINE.
- **Beads is non-functional in this clone** (empty DB, `issue_prefix` config missing → `bd create` errors, no dolt
  remote → `bd dolt pull/push` fail). So the `aipm-*` ids above can't be reconciled/claimed here and `bd dolt push`
  must be skipped; this side-quest's commits went directly to `git` on `main`. Restore with `bd init --prefix aipm`
  + re-add the dolt remote. No active git pre-commit hook here either (`core.hooksPath` unset) — run `check-all` by
  hand. The side-quest added: `scripts/{check-provenance,fetch-refs}.py` + their tests, `refs/manifest/sources.lock.json`.
