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

## 2026-06-09 — `cor-adjoint-benchmark` cluster launched; `prop-direct-sum` (16th af-validated); matrix audit; refs add

Multi-agent orchestration session (background subagents; opus for prover/verifier/scout/audit). Goal: af-validate
the **`cor-adjoint-benchmark` cluster** — the master exact-adjoint Jordan-coboundary inversion, the most advanced
prose-proved result on the critical path to Layer-1 (`op-jordan-structure`/`op-layer1-gap`). Tracked as beads epic
`aipm-brd` + 5 child issues mirroring the registry DAG (`prop-direct-sum`, `prop-spin-splitting`,
`prop-comm-scalar`, `thm-matrix-splitting`, `cor-adjoint-benchmark`).
- **Scoping wave (4 parallel read-only scouts):** proof-kits for the 3 ready feeders (all verdict **G**,
  byte-grounded in HOS) + a **soundness audit** of the suspect `thm-matrix-splitting` front-loaded to de-risk.
  `prop-comm-scalar` flagged OVER BUDGET (14 nodes/depth 6) → factor first (`aipm-0wn`).
- **`prop-direct-sum` COMPLETE (`af: validated`, commit `52110bd`, pushed).** 10-node workspace (depth 3): the
  summand-count-free direct-sum splitting (constant `max_r K_r+1`, no m-dependence, adjoint modules; off-block
  primitives via `P_r f(e_r,·)`, aggregation is MAX not sum). 1 prover → **10 fresh per-node verifiers**
  (leaves→root, one per node, reviewer≠author). 4 HOS externals re-grepped byte-exact. **One challenge** (node 1.7
  under-declared its transitive use of node 1.5's norm bound — an undeclared DAG edge) caught by verifier
  `ver-ds-n17`, **resolved** by `prover-direct-sum` (statement amend recording 1.5 + root assembly; no math change;
  `thm-faithful-approx` 1.4 precedent), **re-verified clean** by fresh `ver-ds-n17b`. Root validated via synthesis
  of children (1.3 construct + 1.5 bound + 1.7 right-inverse), byte-exact contract-match. LESSON: declare EVERY
  cross-node dep (incl. constant-supplying nodes) at refine. NOTE: a verifier mis-flagged a 1.7.2 "artifact" by
  reading a *superseded* ledger entry — live text was clean (check live state, not raw ledger).
- **Matrix soundness audit → `NEEDS-REFORMULATION`** (`thm-matrix-splitting`, `aipm-l3y`/`aipm-q85`). Adversarial
  read + numerics: **sound** (C genuinely n-independent; matching-curvature detection identity machine-verified —
  no ordinary-vs-cb amplification gap; **log-Schur stress test ratio flat ~1.3, NOT a counterexample**) ⇒
  `obs-matrix-audit`/`aipm-36d` re-audit **RESOLVED**. But NOT build-ready: quaternionic mixed-sector twirl
  asserted-not-derived (expand first), state C as "universal" (drop 60/84/124), factor into ~8 sub-lemmas. Open
  user decision A/B/C (default A = honest maximal progress).
- **refs: added `baake-sumner-2007.11433`** (Baake–Sumner, *On equal-input and monotone Markov matrices*, J. Appl.
  Probab. 2022) — byte-greppable arXiv `.tex` source (hash `f358c71c…`, fetch-reproducible via `sources.lock.json`,
  `arxiv-eprint-member`). Idempotent Markov-matrix structure (min poly `x(x−1)`, extremal idempotents `E_1..E_d`)
  for the commutative case. Manifest (`checksums.sha256` 50→51, `SOURCES.md`, lock `arxiv_verified`) +
  `test_fetch_refs.py` counts (17→18 fetch-reproducible) updated in lockstep; check-all green.
- **`prop-spin-splitting` build ATTEMPT 1 FAILED** (`aipm-8zc`): prover hit an **af `--dry-run` friction** — `af
  refine --dry-run` (intended as preview) actually CREATED a junk placeholder node 1.6, shifting the numbering and
  breaking the declared dependency edges (13 nodes), then the agent stalled (stream watchdog). 0 nodes validated;
  broken workspace **scrapped** (kit kept), **rebuild next session**. af bug filed (`aipm-rdx`, candidate upstream PR).
- **Stale-HANDOFF facts corrected:** beads is fully functional here (embedded-dolt + git-backed `origin` remote);
  there IS an active pre-commit hook running `check-all`. HANDOFF rewritten accordingly.

## 2026-06-10 — Agent A: classical-portfolio sidequest, day 1 (branch agent-a/classical-portfolio)
Portfolio attack on op-classical opened (epic aipm-and; ORCHESTRATION.md). Serial multi-model
delegation (opus 4.8 / codex gpt-5.5 xhigh, 2-family verification per load-bearing claim). Arc:
transport-duality route proved vacuous (2-family); codex feedback-accounting repair REFUTED by opus
(muUV = rA upper bound), confirmed by codex; counterexample hunt (7000+ exact idempotents, exact-by-
construction P=ΛR, RΛ=I) found NO plateau and three structural obstructions; lone-far-row lemma
PROVED (kappa >= rho/(2+4delta)); op-exposed-hull reduced to ONE inequality (HCC: hidden cluster at
height H forces max neg >= a*H^2) — the same alpha-mass wall as agent-B's C12, rediscovered
independently by both families. D3 envelope mining: p = 2 EXACTLY, a ≈ 2.4–3.5, sqrt(delta) rate
survives, recursion-no-base-case proof skeleton identified. Two numerics failure modes found+pinned
red→green (LP presolve on near-duplicate rows; coincident-vertex misclassification). All in
agent-A/explorations/classical-portfolio/ (notes/d0..d3*, experiments/). Infra learnings (codex
idle-websocket wedge, resume protocol, progress-message protocol) in LLM-LEARNINGS.md.

## 2026-06-10 (later) — Agent A: classical-portfolio day-1 conclusion (branch agent-a/classical-portfolio)
Full-day campaign concluded at a sharply-compressed state. HELD: op-exposed-hull <= HLC (2-family-
verified assembly, C' = max(4A, 1/sqrt(a))); HLC <= sigma_v-wall lemma (codex endgame glue,
a = min(4/B_A^2, 1/B_B^2)); sigma_v-wall measured precisely (B_B = 0.536; floor delta/H^2 = 3.484;
three independent deciders concur; the genuine MRP middle regime is the SAFEST region — fable's
borderline worry dissolved) but unproved. Proved+audited belt grew to ~17 lemmas (incl. fable's
kernel-energy Gamma = P(g^2)-g^2 [classical square-hole analogue], wiggle rigidity [X1 all-k],
near-delta exposure, g-budget, blocker cap). F-psi conditional (psi-gap lemma named). Literature:
HLC is virgin ground = first quantitative Douglas-Ando stability statement. Waves 1-4 audit sweep
caught 2 genuine gaps in earlier "proved" steps + multiple constant corrections — every catch by a
different party than the author. Meta-experiment learnings in LLM-LEARNINGS.md (idle-websocket
wedge protocol, fable 64k-output file protocol, derive-first audits, certificate-persistence gap).
Beads: aipm-e71 (HLC), aipm-nhj/mox (absorbed faces), new sigma_v-wall bead. Next session: dual-
certificate-persisting decider rerun -> fable closer on sigma_v-wall -> write-up (proof or honest
obstruction map; both PRD-legitimate).

## 2026-06-10 (session close) — Agent A: classical-portfolio handoff written
Detailed continuation handoff at agent-A/explorations/classical-portfolio/HANDOFF.md (read after
the repo gate files): result chain (op-classical <= op-exposed-hull <= HLC <= sigma_v-wall), the
~17-lemma audited belt with constants-authority pointer (wave4/audit-summary.md), dead-route map,
validated numerics pipeline + the dual-certificate-persistence gap, NEXT queue (certificate-
persisting decider rerun -> fable closer on sigma_v-wall -> write-up or honest obstruction map),
delegation protocol learnings, and beads map (aipm-3u6 -> aipm-e71 -> aipm-nhj/mox, epic aipm-and).
The agent-B reference worktree is KEPT at /tmp/aipm-agentb-branch (recreate via git worktree add if
rebooted). Session totals: ~45 delegations across 4 model families, 14 commits, all pushed.

## 2026-06-10/11 — Agent A: classical-portfolio day 2 — the spiral to the kernel (waves 5-13)

Multi-swarm campaign (user-directed: codex swarms liberal, opus serial, fable by approval;
~55 codex + 5 opus + 1 fable). Arc: 8-prover diverse-strategy wave compressed sigma_v-wall
to top-band localization; fable closer found the CORNER THEOREM (exact constants tau* =
2-sqrt3, wall 2(2-sqrt3), floor (7+4sqrt3)/4 — 2-family confirmed) + reduced to DMF; audits
caught+fixed the R-handling bug, downgraded NG'; d12/d13 deciders + the sigma-tilde
height-collapse lemma (proved) exposed the flat floor as a CORNER EXTRAPOLATION — the
empirical truth is the LINEAR LAW delta >= H/2 (entire record; d13 outcome (c), high
strength). 10-strategy-kind wave (user-requested diversity): 5/10 collapsed into the
exposedness-LP basin proving "hiddenness IS the LP frame"; t10 PROVED the Birkhoff
projective idempotent-collapse finisher (no spectral gap). d14: leakage question dissolves
(positive kernel closes exactly; v's delta-budget negatives are the only crossing); residual
= unbounded projective diameter = support-graph branch. Wave 12 PROVED the per-component
finisher (fat components collapse-and-expose); wave 13 = symmetric stalemate at the kernel:
path-product floor Pi_C >~ tau - O(L*delta) (prover died at it; two refuters could not
build against it). Literal psi-gap REFUTED twice + conditioned variant PROVED; s5 exact
all-shallow face constructed (low height only); s8 sigma-tilde<=tau branch PROVED (HLC
direct there). SOURCE DISCOVERY: Baake-Sumner cite Hognas-Mukherjea WITHOUT proof — the
delta=0 anchor needs its own byte-pin (bead filed). DELIVERABLE: 49pp self-contained
LaTeX report (13 shards, 3 hostile review rounds, overclaim bar PASSED) delivered to user;
sent as report/main.pdf (exploration lane). All ~45 worker verdicts archived in
notes/swarm-answers/; the complete spiral record in notes/wave5-sigma-wall-parallel.md.
Beads: aipm-3u6 carries the kernel; aipm-sjw (report) done; H-M acquisition bead filed.

## 2026-06-11 (cont.) — kernel-conjecture document; Hognas-Mukherjea acquired; autopsy launched

Three follow-ons after the day-2 close. (1) **report/kernel-conjecture.tex** (user
deliverable, sent): the fully self-contained statement of the minimal open input — the
KERNEL CONJECTURE (exists universal delta_0, B: for delta <= delta_0, W nonempty and every
hidden row vertex with sigma-tilde > sqrt(delta) is within B*sqrt(delta) of conv W), with
all 7 definitions from scratch, the conditional chain theorem (kernel => linear hull bound
=> HLC => op-exposed-hull => op-classical, per-link statuses), the stronger path-product-
floor working form (Conjecture 2 + the proved component-finisher bridge), and the
evidence/constraints ledger (what any proof must respect, what routes are proved dead).
(2) **refs: Hognas-Mukherjea ingested** (user-downloaded book, ISBN 978-0-387-77548-7):
refs/hognas-mukherjea-2011/ PDF + pdftotext extraction; manifest lockstep (checksums
51->53, lock cache-only entries, SOURCES.md, test_fetch_refs count red->green; 53/53
verify). Closes the wave-10.5 source-gap discovery (B-S cite the idempotent classification
without proof). (3) **w14 autopsy launched** (codex): locate the real structure-theorem
proof (section 2.2) and audit each step under the campaign's ACTUAL perturbation (exactness
free, only positivity perturbed): SIGN-ROBUST vs SIGN-RIGID per step + the signed-surrogate
synthesis question. Bead aipm-e9p in progress. All pushed through 2d090de.

## 2026-06-11 (cont. 2) — Agent A: waves 14-23, the variety programme, consolidation, MERGE TO MAIN

User-directed orchestration day (all work codex-delegated, ~30 workers, every proof
hostile-audited by a different worker). ARC: (1) H-M autopsy harvested+audited; delta=0
anchor byte-pinned, kernel-conjecture.tex §5 discharged. (2) Periodicity gap closed
(audited). (3) Chain-local SOS killed (scalar shadow false). (4) THE CLONING OBSTRUCTION:
raw-index path-product floor false-or-vacuous; quotient form 2' formulated, bridge
secured; two provers died at the same anti-splitting estimate. (5) sigma-gate crossed
(first hidden sigma>tau instance ever, certified exact rational; then the joint
antecedent realized ABOVE the corner: sigma/tau=1.55, H/tau=0.10, delta=0.233, certified
exact) — raw floor refuted outright for delta0>=0.233; ledger re-scoped (the question
lives below the corner). (6) USER-DIRECTED idempotence-exploitation research round (5
lenses): the variety programme born. (7) Waves 19-23: TANGENT-CONE LEMMA proved+audited
(dH+ <= 2*ddelta, C=2 dimension-free — the infinitesimal linear law); ambient fixed-mass
visibility lemma (audited, repaired); mass-removed boundary recoding L1+L2 (audited,
final-profile form); stratified distance-to-locus bound (audited; fixed-stratum version
refuted by support-addition arcs); the LOCAL-LAW ASSEMBLY claimed then BROKEN by audit
(visibility hypotheses fail at the chosen base 12.8-128x) — the open piece. (8)
CONSOLIDATION: OVERVIEW.md written (the bird's-eye onboarding doc), reviewed by a
hostile fact-checker (15 findings incl. the ex-hume W-free subtlety) + a fresh-agent
reader (kernel-vs-linear-law conflation caught); all fixes applied. (9) USER DISCOVERY:
H-M Theorem 1.12 = the EXACT signed structure theorem the campaign never read —
w25_hm112 in flight on the bridge to the global gap. (10) Branch MERGED TO MAIN
(fast-forward; user: "it IS the main project right now"). All in
notes/wave5-sigma-wall-parallel.md + notes/swarm-answers/ (~85 verdicts) +
experiments/out/. Beads: aipm-3u6 carries the campaign; aipm-e9p closed; acquisition
bead open (Douglas-Ando etc.).

## 2026-06-12 — Agent A: lockstep repair (waves 24-32 were undocumented) + wave-33 relaunch

Session resumed after the 2026-06-11 pause (b8da7ca; network maintenance stopped w32 at
stage 2). LOCKSTEP REPAIR: the worklog/handoffs stopped at waves 14-23 while commits ran to
w32 — this entry + the portfolio HANDOFF UPDATE block + the ORCHESTRATION 2026-06-12 snapshot
close that gap. WHAT WAVES 24-32 DID (verdicts in notes/swarm-answers/): the H-M Theorem 1.12
coordinate route was run to its core. w25: 1.12 autopsy (right global coordinates, mod a
merge/conditioning lemma; loci byte-pinned vs refs/hognas-mukherjea-2011). w26: clustered
chart L2 proved + upgraded dimension-free (A=1, max-volume actual-row basis; audited). w27:
O(delta) concentration REFUTED (rank-2 family); banked in-class concentration + cross-cluster
leakage <= 2delta/(1-eta). w28: bridge reduces to the representative displacement lemma. w29:
general-row displacement REFUTED at delta=0; max-volume representative form is THE kernel.
w30: telescope dead (no contraction from idempotence alone); maxvol route proves displacement
conditionally on the transverse coefficient tax (C_D <= 2(1+2delta_0)(2+C_mu)). w31: tax
split — scalar deficit <= 2delta PROVED; residual = THE SIGNED-FACE EXCESS (SF):
sum_j (P_{u_s j})_+ (sum_{t!=s}(-a_t(j))_+ - (1-a_s(j)))_+ <= C_sf delta. SF => tax
(C_mu = 2+C_sf) => displacement => face estimate => L4 assembly => global W-free O(sqrt(delta))
theorem. w32 banked one finding before the pause: coefficient-only LP relaxation already too
weak at delta=0 — geometry is load-bearing from round one. /tmp workspaces confirmed gone;
all 44 briefs were archived in notes/briefs/ by the pause commit (the archive worked as
designed). WAVE 33 LAUNCHED (user-directed; cap 2-3 codex parallel, opus serial, sonnet free;
TIB VPN + wolframscript unavailable, gurobi confirmed): w33_sf_geom (codex prover — geometry-
first gurobi LP loop, idempotence in from round one, + the UNDERUSED LEVER: the 1.12 CONVERSE
as an exact parametrization of all rank-k idempotents, perturbing positivity only) ||
w33_cex (codex refuter — build exact idempotents to order via the 1.12 converse, stack
transverse pairs to break SF, or name the per-pair-cost obstruction lemma) || sonnet H-M
book-mining catalog (user lead: "the book has lots of good stuff" — everything beyond 1.12,
to notes/hm-book-mining.md). Briefs archived notes/briefs/w33_*.md at launch.

## 2026-06-12 (cont.) — waves 33-34: the SF endgame takes shape; tie-quantifier = the question; outage checkpoint

Full day under the new interruption-resilience protocol (ORCHESTRATION.md; user warned of
frequent network outages). WAVE 33 (2 codex + sonnet): w33_cex DIED-AT with strong bounded
evidence (transverse stacking provably can't pump: BL=I sees only aggregate +/- mass;
split-block 1/delta mechanism dies under max-volume recomputation; dual-flow obstruction
lemma named); w33_sf_geom broke the w32 delta=0 wall (geometry-included structural LP over
P=LB, BL=I), banked tight fixed-support certificates (1+4a^2, 1+3a^2) and the exact k=7
dense-pair instance (ratio 17/8 at delta=6/17) => universal C<=2 false at moderate delta_0;
orchestrator REFUTED the worker's sec-6 convexity route via its own instance (upheld 0.98 in
w34_audit). H-M book mined (Ex 1.55 = the P=LM, ML=I factorization, byte-pinned — grounds
the campaign's frame; C-M Contemp.Math.516 is its dedicated source, acquisition blocked by
AMS Cloudflare, 7/8 other leads staged in refs-staging/). ORCHESTRATOR LOCAL PROBE
(w34_scaling, resilience fallback): dense-pair phase structure — ratio 1 for cap<=0.3,
ratio=m (linear in rank!) at cap=1/2. WAVE 34: w34_audit (hostile) CONFIRMED all of wave 33
+ THE STRUCTURAL FIND: max-volume TIE bases flip every bad instance to ratio 1 => SF's
tie-quantifier (FOR-ALL vs EXISTS basis) is the statement-level decision. w34_halfcex
(snapshotted mid-run at the outage): closed-form half-delta staircase exactly verified
m=2,3,5,8; recomputed BEST-tie ratio = m at cap=1/2 (real blow-up under FOR-ALL reading;
worst tie = 1), adversarial-tie ratios bounded ~5/3 at cap=0.3. Wave-35 questions written
into the portfolio HANDOFF. INFRA: gurobi works only OUTSIDE the codex sandbox (HostID);
wolframscript flaky-first-call. All harvests committed+pushed through the day per protocol.

## 2026-06-12 (cont. 2) — waves 35-37: the conjecture compressed to ONE display ((TREE)); theta=1/2 forced; merged to main

Resumed post-outage (the w34_halfcex worker SURVIVED the outage mid-run and delivered on
reconnect — the resilience protocol works). WAVE 35: w35_quantifier = CHAIN-COMPATIBLE
(the exists-theta-quasi-max SF form composes end-to-end; registry contract + explicit
constants C_D = 4(1+2delta_0)(C_sf+1+A); one routing caveat: w27's scalar telescope needs
the exact-max sign fact — route around); w35_charge = PARTIAL (selection U* = argmin_ties
max_s SF_s well-defined; the min-max chart collapses EVERY known bad instance to ratio
EXACTLY 1, even the staircase at delta=1/2; named open = (CHARGE)). WAVE 36: w36_audit
confirmed the whole w35 pair AND scored the decisive hit (B6): an exact PERTURBED staircase
(unique max-volume chart, ratio m-3eps at delta=1/2; good charts at volume exactly 1-eps)
refutes exists-EXACT-max-volume SF with unbounded rank => theta = 1/2 quasi-max selection is
MANDATORY (eps < 1/2 structurally forced => fixed theta = 1/2 recaptures the good charts;
constants cost A = 2). Also: (CHARGE) flagged mostly-tautological — attack Phi(U*) <= C delta
directly. w36_charge = PARTIAL: the no-center path family pins the true selected-chart
constant at ~2; the single remaining display is (TREE)/(DECAY) — multi-swap shear decay with
alpha < 1; crux = naive shear branching mass 2/generation diverges, decay must be bought by
the delta-budget. WAVE 37 launched (two-family on (TREE), theta=1/2 class): codex w37_tree
(survived a second outage mid-run, continuing) + opus independent prover (killed by the
outage at zero output; relaunched). HOUSEKEEPING: H-M book mined (Ex 1.55 = P=LM ML=I
byte-pinned; catalog notes/hm-book-mining.md); 7/8 wave-18 refs acquired to refs-staging/
(manifest lockstep pending; C-M Contemp.Math.516 needs manual TIB browser download); gurobi
broken INSIDE codex sandbox (HostID; LLM-LEARNINGS), wolframscript flaky-first-call.
MERGED TO MAIN at user direction ("this is main work"); work continues on main.

## 2026-06-13 — waves 38-43: refute-repair-prove cycle; RANK-2 THEOREM; the kernel is now (EX); consolidation

The adversarial loop earned its keep: w38 (codex) REFUTED the opus (SIG) step at theta=1/2
(overshoot rows a_s > 1; exact 1e-6 witness) => w39 (opus) repaired it exactly ((P1):
E <= sigma + 2(-lambda)_+; corrected display (SB*); overshoot provably not-free) => w40
(codex) cross-confirmed the repair AND proved the **RANK-2 THEOREM**: every theta-half
Phi-argmin chart has Phi = 0, V = 0, S* <= 2 delta — the first unconditional selected-chart
bound (max-diameter mechanism; no tie-break needed). Orchestrator spotted that the rank-2
proof FACTORIZES; w41 (codex) verified it: S*_s <= 2 Phi_s + 6 delta for ANY theta-half
chart (0 violations / 7573 charts) — so the WHOLE CAMPAIGN reduces to the existence
statement (EX): exists a theta-half actual-row chart with Phi <= C0 delta. w41 also ran
(EX) at rank 3 adversarially: HOLDS EMPIRICALLY with C0 = 1 exactly (278 exact records,
53 structured adversarial). w42 (opus, hostile) CONFIRMED the factorization 2-family
(constants (2,6) TIGHT, class-wide, no hidden delta-dependence; composition C_sf = 2C0+6
clean; 0.99). CONSOLIDATION: w43 (codex) drafting kernel-conjecture v2 (the (EX)
interface); beads filed for the rank-2 opus pass + Recipe A->B banking of the belt;
aipm-3u6 notes updated; HANDOFF frontier block rewritten (waves 33-37 narratives compacted
to the swarm-answers pointers). Chain if (EX) lands: C_sf = 2C0+6 => w35 constants
(theta=1/2, A=2) => displacement => face/L4 => global O(sqrt delta) => op-classical.
