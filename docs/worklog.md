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

## 2026-06-06 — Theorem B (the algebraic bridge) fully machine-validated via af + a provenance gate

**Headline.** Drove the entire bridge to machine-checked completion: **8/8 lemmas af-validated** (only
`lem-P-properties` predated this session) — `lem-bridge-orderunit`, `lem-first-insertion`,
`lem-square-hole-almost-positive`, `lem-bridge-easy`, `lem-bridge-polar`, `lem-bridge-onehole`,
`prop-bridge-jordan` (crux: the approximate Jordan identity by exact-ambient-cancellation), `thm-bridge`
(capstone). Commits `7021740..b7110ba`, all pushed. Per lemma: sonnet prep (grounded kit) → opus prover
build → fresh-opus-verifier adversarial pass (sequential, per node, reviewer≠author) → prover resolve →
re-verify → `af: validated` → linker `--check --generate` → commit + push.

**Orchestration.** Multi-agent (~40 background workflows/agents): prep/search = sonnet; prover / verifier /
coding = opus; main loop = conductor — monitored, raised beads, committed in dependency order, never blind.

**Linker fix (50305fc, TDD, reviewer≠author).** `argument.py:133` wrongly required *every* dep
`af:validated`, blocking ground-truth-leaf (cited) deps (`prop-kadison-js`) → the bridge stalled. Fixed: a
dep is available iff `af:validated` OR `status==cited` (the design's "internal-lemma dep" intent).

**Governing rules locked (user, 2026-06-06).** (1) *No "standard facts"/"citations" — the ONLY ground
truth is a byte/string match to a LOCAL `refs/` source.* (2) *"A derivation = lemma = af"* (small ⇒
in-workspace node; reusable/substantial ⇒ own lemma). The recurring `‖Φ‖=1` was *avoided* (δ-bound +
triangle), never asserted — so no `lem-positive-unital-contraction` was needed for the bridge.

**The adversarial loop caught three real defects (the project's whole point):**
- **R5 fabrication (e5b21c8).** `GT-bhsa-jc` seeded with a *fabricated* "verbatim" quote (a true-fact
  paraphrase) that reached pushed commit `73b240b`; `lem-bridge-polar`'s verifier caught it (its peers
  had grep-confirmed only a substring). Built `scripts/check-refs.py` (TDD, 17 tests, reviewer-approved) —
  byte-matches every af-external quote vs `refs/`, wired into `check-all.sh`; full audit = exactly 2
  fabrications, both corrected (+`GT-jc-is-jb` added for the JC→JB step). The class is now pre-commit-gated.
- **R6 boundary error.** `thm-bridge` asserted `η₀=1/4`, but `lem-P-properties` needs `η₀<1/4` *strictly*
  (the binomial for `P` diverges at `4η₀=1`, constants → ∞); verifier caught it, fixed to `η₀<1/4`.
- `lem-square-hole` node-1.2 asserted `‖Φ‖=1` as a leaf → replaced by the in-scope triangle bound.

**Process directive (user): each discovered failure mode → a red→green test/gate.** `test_check_refs.py`
(fixture-based matcher red→green + the live `fail_count==0` invariant), `test_argument.py` (grounded-leaf).
LEARNINGS R5/R6.

**Beads.** Closed `aipm-dkn` (linker), `aipm-0ze` (bridge). Filed `aipm-17f` (registry cited-audit),
`aipm-6ao` (gate — core shipped), `aipm-iel` (gate hardening: skip-no-quote evasion + retrofit
`lem-P-properties`' 7 quote-less externals, P1), `aipm-1pd` (af `depend` post-hoc-dep PR).

**af frictions noted.** No post-hoc dependency-edge command (`aipm-1pd`); externals are workspace-level
(node scope shows "(none found)"); a child-fix also requires resolving the *root's* cascaded dependency
challenge. The af workspace is not safe under concurrent mutation → per-workspace af ops were serialized.

**Known gaps / next (highest first).** `aipm-iel` (harden check-refs — 8 quote-less externals still
unverified); `aipm-17f` (audit cited registry results, downgrade ungrounded e.g. whitehead/aut-compact,
rename cited→grounded); `aipm-qpa` (factor `‖Φ‖=1` / operator-Banach-algebra into own lemmas/defs);
`aipm-dqz` (`af replay --verify` of `proofs/*` in check-all); `aipm-oql`/`aipm-chn` (Phase-4 reorg);
open-math frontier `aipm-245`/`aipm-08u`/`aipm-36d` (Layer-1).

---

## 2026-06-07 — Dilation-compatible theorem (the conditional O(η) result) COMPLETE; branch → `main`

**Built `thm-dilation-compatible` + 3 factored sub-lemmas + 1 def, all `af: validated` (A+B consensus).**
Restructured the brittle 1-theorem scaffold (per L3) into: `lem-idempotence-inheritance`
(`‖Φ²−Φ‖≤‖F²−F‖`, constant exactly 1), `lem-intertwine-spectral-idempotent` (`θ(2F−1)j=jθ(2Φ−1)`),
`lem-cstar-sa-to-epsjb` (**the O(η) crux** — sa-part of Kitaev's extended O(η)-C\*-algebra is O(η)-ε-JB; JB4
from `ax_assoc=O(η)` via an n=4 pentagon reassociation, K₄≤32, dimension-free; JB3 via concrete UCP), and
the `thm-dilation-compatible` capstone (7-node assembly importing the 3 + `lem-P-properties`). New def
`def-eps-cstar-algebra` (byte-matched Kitaev :407-440). Each: scout → prover(agent-B) → fresh-verifier
(agent-A) → resolve → confirm → flip; every crux independently re-derived.

**Scope decision (user): dilation space restricted to `D=B(K)`** (a full matrix algebra — the natural
Stinespring dilation target) so `lem-cstar` (UCP on B(H)) applies verbatim. The general finite-dim C\*
`D=⊕Mₙ` case is **deferred** (`aipm-us3`): a careful proof-read confirmed Kitaev's almost-idempotent
construction is C\*-generic in everything except the two-hole estimate's Stinespring *stack*, which Kitaev
instantiates only over full `B(Hₙ)`; widening needs a bridge lemma re-deriving that tower at finite-dim-C\*
generality. (`⊕B(Lⱼ)` is a *proper* subalgebra of `B(K)` for ≥2 summands — no free `D≅B(K)`.)

**Adversarial wins (the loop cuts both ways).**
- **R7:** a fresh *verifier* produced a confident, plausible, WRONG "critical false premise" counterexample
  on `lem-idempotence-inheritance`; refuted by an independent **7,008,000-sample** sweep + a one-line proof
  (`‖Φ²−Φ‖=‖(Φ−I)Cj‖≤‖(Φ−I)C‖=‖F²−F‖`, `j` order-isometric). New standing lesson: *a refutation is itself a
  claim — reproduce it before acting.*
- A **Wedderburn shortcut** the orchestrator tried for the capstone (`D≅B(K)` for general finite-dim C\*) was
  FALSE (proper-subalgebra dimension count); a fresh verifier caught it; the false claim was removed from the
  repo and replaced by the honest `D=B(K)` restriction + a flagged deferral.
- `GT-bhsa-jc` (the R5 fabrication site) independently re-grepped byte-clean in `lem-cstar`.

**Branch consolidated.** `argument-architecture` (30 commits ahead, clean fast-forward) promoted to `main`;
feature branch deleted local+remote; default stays `main`; HANDOFF + auto-memory updated. Single branch now.

**Classical-layer prep.** Reframed `aipm-9mw`: the elementary finite-dim facts are inline-derivable from
Kitaev's general operator-norm def (`:638-642`) + `def-stochastic` (the validated-bridge standard) — only
`lem-leakage`'s contract needs splitting (the "no O(η) closure" sharpness should depend on the existing
`ex-hume`). Scouted byte-extractable OPEN sources for first-class provenance (`aipm-18d`): MIT OCW 6.241J
Ch.4 (matrix norms), Boyd & Vandenberghe (convexity/simplex/stochastic).

**Beads.** Closed `aipm-ynq`/`aipm-vp5`/`aipm-q8i` (dilation theorem done). Filed `aipm-9mw` (leakage split),
`aipm-18d` (classical sources), `aipm-us3` (general-D backlog), `aipm-on1` (af friction PRs). **13 results are
`af: validated` total** (the 9-lemma bridge + 3 dilation sub-lemmas + the dilation capstone). LEARNINGS R7.

---

## 2026-06-07 (side-quest) — `check-provenance.py`: report↔registry sync gate (was `aipm-oql`)

**What.** Built the Phase-2b "CI for the paper" and wired it into `check-all.sh`: a new
`scripts/check-provenance.py` plus the `latexmk` build, so the human-readable report can no longer silently
drift from the machine-checked argument. **Join key** = each registry shard's `provenance:` line `report
<label>` token (the ids are NOT a string transform — `lem-square-hole-almost-positive` ↔ `lem:bridge-squarehole`),
with a first-hyphen→colon id fallback. 55/59 shards already carried the token; the gate exploits it.

**Checks.** ERRORS (block commit): forward labels (every `report <label>` resolves to a `\label{}`); per-claim
labels resolve; per-claim Source keys are defined in the source registry; in-repo source `sha256[:16]` fresh;
**status OVERCLAIM** (a `status:open` result framed proved/benchmark in `tab:status` — the project's #1 guarded
failure mode); `latexmk` build with no undefined references. WARNINGS: reverse-labels, anchor (a result mapping
to zero report labels), coverage, status underclaim, parse-integrity (unparseable/duplicate rows), absent
gitignored payloads, stale absolute source paths. Build compiles into gitignored `report/.build/` via
`-output-directory`, so the tracked `report/main.pdf` is never mutated (verified by a test).

**Process.** TDD: 52 red→green tests (`scripts/tests/test_check_provenance.py`), incl. live port-and-verify
(perturb a real shard/table → RED → restore) and a guarded `run_build` isolation test. **Reviewer≠author**: a
3-agent adversarial review (correctness/false-greens · parsing-robustness · build-integration) found real
issues, all reproduced; fixes applied: overclaim WARN→ERROR; hash EVERY source row (caught a silent `B-ROUND`
duplicate-key that had been un-checking `factorization-positivity-rounding.md`); strip `%`-comments before
harvesting labels/status; split status rows on unescaped `&`; BOM-tolerant frontmatter; broadened claim-source
separators; latexmk-timeout handling. Fixed a genuine `A-ER` 15→16-hex sha typo the gate surfaced.

**Honest limits (in the gate docstring).** STATEMENT/contract TEXT is not compared (label↔label only) — the
registry `contract` stays the single source of truth; status drift is seen only for `tab:status`-listed
results; ~⅓ of sources are hash-unverifiable (gitignored payloads). Follow-ups noted in HANDOFF.

**Environment gaps (pre-existing, not regressions).** This clone lacks the gitignored `refs/` payloads, so
`test_check_refs.py` fails its byte-match assertions (the check-refs GATE itself passes — 0 fabrications); and
beads is unprovisioned (empty DB, `issue_prefix` unset, no dolt remote) so `aipm-*` ids can't be reconciled.
The new gate + its tests + the other three gates all pass.

---

## 2026-06-07 (side-quest cont.) — reproducible refs/ reconstruction (`fetch-refs.py` + `sources.lock.json`)

**Problem.** `refs/` ground truth (the gitignored payloads the byte-match gates need) lived only on the
original authoring machine — brittle. Recovered 17/50 locally + by arXiv fetch (HOS/Idel/Kitaev from
sibling repos; Kitaev PDF + all 6 VLW files fetched byte-exact from arXiv), which already turned
`check-all` GREEN for the first time in this clone (all 4 af-cited sources — HOS, Kitaev, Idel, VLW —
present; `test_check_refs` 6 failing → 0).

**Robust fix.** A reproducible, machine-independent reconstruction:
- `refs/manifest/sources.lock.json` (tracked) — per refs file: sha256 + a *verified* fetch spec
  (arXiv e-print/PDF by pinned id) for the 14 reproducible ones (kitaev 8 + vlw 6), else `cache-only`
  (36 bespoke). Hash-driven, honest: a source is `fetch` ONLY because the fetch was proven to byte-match.
- `scripts/fetch-refs.py` — rebuilds `refs/` on any clone, verifying every byte vs the recorded sha256:
  (1) FETCH the arXiv-pinned sources (e-print tarball members selected BY HASH, + per-version PDF —
  proven byte-stable: deleted all 14 and reconstructed them clean from ids alone); (2) restore the
  bespoke residue from a CONTENT-ADDRESSED cache `$AIPM_REFS_CACHE/<sha256>` (a dir/URL the user
  controls — seed once with `--populate-cache`, mirror anywhere durable). `--status` (no network),
  `--require-all` (CI). Never installs a blob whose bytes ≠ recorded hash (tested).
- 16 offline red→green tests (`test_fetch_refs.py`, incl. tampered-blob refusal), wired into check-all.

**Why this removes the brittleness.** The 14 public sources reproduce from arXiv with zero local
dependency; the 36 copyrighted/bespoke ones reproduce from a content-addressed cache the user mirrors
durably — no dependence on any specific live machine. The lock + script are committed (no copyright), so
the reconstruction recipe travels with the repo. `refs/` payloads stay gitignored.

---

## 2026-06-07 (side-quest cont.) — web recovery of refs + genuineness audit (high-skepticism)

**Web recovery.** Located + fetched the byte-exact source files (no specific machine needed):
- From authoritative origins, hash-matched ⇒ GENUINE: Kitaev `2405.02434` (e-print+pdf), VLW
  `2604.08380` (e-print+pdf), Effros–Størmer source PDF (official *Math. Scand.* galley 11830/9846),
  Baak–Moslehian (arXiv `math/0501158`), Blecher–Read `.tex` (arXiv `1905.05836` gunzipped source).
  Now **17/50 are fetch-reproducible** via `fetch-refs.py` (added `url` + single-file-gz arXiv handling).
- Still 20/50 present locally (gate GREEN; all 4 af-cited sources HOS/Kitaev/Idel/VLW present).

**Genuineness audit (user flagged: prior agents may have fetched wrong PDFs / hallucinated).**
- Fetching from authoritative origins IS a genuineness proof: a hallucinated/wrong file cannot byte-match
  official arXiv/journal bytes. So the 6 web-recovered sources are certified genuine, not just hash-consistent.
- HOS: scan title page = the real Hanche-Olsen–Størmer book; the 21 passages the proofs byte-quote
  (Jordan product 2.17, Jordan identity 2.18, JB axioms 3.1.3/3.1.4 incl. the exact M₂ counterexample,
  state Cauchy–Schwarz) are correct standard mathematics with correct equation numbering — not a
  hallucination signature. **User attests `joa-m.md` is their own file originally stored in `../af-tests`**
  (the copy used here, hash `28740e73`). ⇒ genuine.
- Idel: verifiably Martin Idel's 2013 TUM/LMU thesis (advisor Wolf); abstract states the project's
  foundational fact (fixed points of unital positive maps are Jordan algebras). ⇒ genuine.
- SUSPECT / unverifiable (the candidates for the prior-agent-error worry): `kaup-1984` and
  `chu-russo-1512.03347` PDFs — recorded bytes match NO current authoritative source (mscand re-encoded;
  arXiv+Wayback don't carry the recorded chu-russo bytes). Neither is cited by an af proof; chu-russo only
  backs the already-flagged `thm-whitehead`. Recommend re-deriving from the authoritative source and
  re-pinning the manifest hash, or dropping them — flagged honestly, not trusted.
- The ~28 Effros–Størmer OCR page-scans/text + `blecher-neal`/`itoh` text extractions are locally-derived
  (OCR/pdftotext of source PDFs), not byte-reproducible by fetch; cache-only.

## 2026-06-07 (cont.) — report UX upgrade + thm-faithful-approx (14th af-validated)

Two pieces of work after the refs side-quest, both pushed to `main`.

**Report as a status-transparent, provenance-linked front door** (commits `bfedb28`, `d30ef45`,
`2b21ec7`). First fixed a stale tracked `main.pdf` (gate builds to `report/.build/`, never refreshes the
committed PDF → it lagged the 2026-06-07 dilation work; regenerated). Then, reusing existing infra (no new
gates), four upgrades + a DAG figure: (1) clickable bibliography links — `references.bib` now carries
`note=\href{...}` to arXiv/Math.Scand. for Kitaev/VLW/Effros–Størmer/Chu–Russo (URLs from
`sources.lock.json`); HOS/Idel have no public URL (honest ceiling). (2) `\afbadge`/`\aflink`/`\afyes` macros
(`main.tex`) → a green "✓ af-validated" badge on each validated result linking to its GitHub `proofs/<id>/`.
(3) `tab:status` gained an `af` column (Status kept as col 2 so `check-provenance`'s parser is unaffected) +
legend. (4) a reading guide in §01. Plus `scripts/gen-dag-figure.py` (reuses `argument.py`'s parser) →
`report/figures/dag.{dot,pdf}` via GraphViz (colour=status), embedded as `fig:dag`; NOT gate-wired (committed
artifact like `main.pdf`, re-run by hand). User steer recorded: balance utility vs CI ceremony — don't turn
report niceties into a software-engineering programme.

**thm-faithful-approx COMPLETE — af: validated** (commits `71f277a`, `4a282f0`). The 14th machine-validated
result: the conditioned faithful-invariant ambient-product bound `||h_{a,b}|| <= C(η/λ)||a||||b||` (§06b),
the corrected statement of the retracted "faithful invariant ⇒ O(η)" overclaim (honest η/λ, no smuggled
floor on λ). 10-node af workspace (depth 3): spectral split + square-hole import (`lem-square-hole`) →
expectation bound (imports `lem-P-properties` for `||P-Φ||≤Cη`) → faithfulness upgrade
`ω(x)=Tr(ρx)≥λTr(x)≥λ||x||` (grounded in VLW trace self-duality `paper.tex:453` + Idel density `:333` +
`Tr≥norm`) → diagonal → polarisation. Recipe B with a **fresh single-node verifier per node** (user rule,
2026-06-07): one challenge (node 1.4 omitted the direct `1.1` dependency edge) resolved via amend + the
transitive `1.4→1.3→1.1` recording (af v0.1.3 has no post-hoc edge command; re-refining would archive
validated children), re-verified clean. Registry: `af none→validated`, deps corrected to add
`lem-P-properties` (genuinely imported, previously undeclared); INDEX/DAG regenerated; report badge + status
+ counts (13→14) updated in lockstep. Next af frontier (`argument.py`): `lem-classical-equiv` (unblocks the
classical chain), `prop-rank-gap` (the √rank honesty caveat), the §10 obstructions.

## 2026-06-07 (cont.) — Agent B exploration lane + `lem-classical-equiv` (15th af-validated, Workflow-orchestrated)

**Agent B rules of engagement** (commit `5eff235` on `main`; first written as `222ced5`). A second agent (Agent
B) was admitted for exploratory scoping of how to land the full proof. To protect the validated results from
generative/optimistic exploration, codified a lane discipline in four surfaces:
`docs/plans/2026-06-07-agent-b-rules-of-engagement.md` (canonical full version — sandbox-vs-front-door,
never-touch list, status-honesty/no-overclaim, ground-truth byte-match, shared-repo coordination, "best output =
a map not a half-proof"), `agent-B/README.md` (condensed front-door), the `CLAUDE.md`==`AGENTS.md` "Two agents,
two lanes" callout, and the HANDOFF START-HERE step 0. Core principle: explore freely in `agent-B/**` /
`docs/plans/`; reach canonical layers ONLY by *proposing* via Recipe A→B + a non-self reviewer.

**`lem-classical-equiv` COMPLETE — af: validated** (15th machine-validated result; §08 signed↔stochastic
equivalence with explicit universal constants). First **end-to-end multi-agent Workflow orchestration** of an af
result (orchestration in `proofs/lem-classical-equiv/orchestration/`):
- **Groundability gate** (workflow: parallel scope-per-direction → one grounding probe per foundational fact →
  synthesize). Verdict **A** (build may proceed, no acquisition). Key finding that de-risked the whole task: the
  forward direction's hand-waved "standard spectral separation estimate" is NOT a (fragile) holomorphic calculus
  but Kitaev's **elementary binomial/Taylor Banach-algebra calculus** (`refs/kitaev:503-533`, present) — Kitaev
  uses it precisely because the holomorphic calculus is "fragile in the approximate setting". Three residual gaps
  (explicit constant `C`, calculus multiplicativity, the `Mₙ(ℝ)` norm arena) are all derivable as proof nodes.
- **Build** (single prover): 11-node workspace (root + 1.1–1.10, depth 2). Forward N1–N7 instantiates Kitaev's
  *general* Banach-algebra Prop_P **directly at `Mₙ(ℝ)`** — deliberately did NOT import the validated
  `lem-P-properties` (its arena is `B(H)ₛₐ`, an arena/hypothesis mismatch a verifier would rightly challenge);
  registry `deps` stays empty. Converse N8–N10: the exact ring identity `Q²−Q=PD+DP+D²−D` + disjoint-support ℓ¹.
  5 externals (4 Kitaev byte-quoted incl. `GT-operator-norm-banach`; `GT-hyp` skip_noquote); `check-refs` 0-failed.
- **Verify** (workflow: 11 FRESH per-node verifiers, sequential, leaves→root — user rule 3). **All accept, 0
  challenges**, taint 11 clean. Real adversarial work: numeric cross-checks (op-norm = max-row-ℓ¹ to 1e-16,
  `S²−I=4(Q²−Q)` swept n=2..120), full refs byte-matching, and independent re-derivation of the linchpin N4
  multiplicativity via Cauchy product (resolving a flagged tension vs the `lem-P-properties` `GT-funcalc`
  citation). Confirmed `C=6C₁(η₀)` is **dimension-free in n** (no √rank leak). Honest flag carried through: the
  `Mₙ(ℝ)` max-row-ℓ¹ closed form is **extraction-level** (not byte-stated in any present ref; derived inline,
  the `lem-P-properties` 1.1.2 pattern).
- **Finalize:** `af export`; shard `af none→validated` (deps empty); INDEX/DAG regenerated (linker 0/0);
  unblocks `thm-rank-one`/`thm-simplex`/`prop-approx-simplex` (now ready). Report upkeep in lockstep: `\afbadge`,
  the `tab:status` row **split** (only `lem-classical-equiv` gets `\afyes`, not the un-validated Hume example),
  counts 14→15 (§01, §11), `dag.pdf` regenerated, tracked `main.pdf` rebuilt. `check-all` OK.
- **Coordination note:** Agent B (since frozen — "done, will not edit again") had switched the shared working
  tree onto branch `agent-b/op-exposed-hull-orchestration` and its index swept 2 exploration notes into the
  `222ced5` docs commit. Consolidated canonical work onto `main` (per user): restored only the 4 intended docs
  files, rewrote HANDOFF; Agent B's exploration stays on its own pushed branch.
