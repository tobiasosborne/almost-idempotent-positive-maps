<!--
ROLE: crash-safe handoff for the classical-portfolio sidequest (Agent A exploration lane).
Branch: agent-a/classical-portfolio. Rewritten at session close. Read AFTER the repo gate files.
-->

# HANDOFF — classical-portfolio sidequest (op-classical / op-exposed-hull)

> ## START HERE (next agent)
> 1. You are on branch **`agent-a/classical-portfolio`** (exploration lane; canonical layers on
>    `main` are reached ONLY via Recipe A→B with reviewer ≠ author — see repo CLAUDE.md).
> 2. Read order: repo gate files (`PRD.md` → `CLAUDE.md` → root `HANDOFF.md` for the main build) →
>    **this file** → `ORCHESTRATION.md` (same dir; the full campaign log + EOD snapshot) →
>    `notes/wave4/audit-summary.md` (audited constants) → `notes/endgame-sigma-wall-residual.md`
>    (the terminal residual). Math deep-dives as needed (map below).
> 3. **A read-only git worktree of agent-B's original exploration branch is kept at
>    `/tmp/aipm-agentb-branch`** (branch `agent-b/op-exposed-hull-orchestration`: their session
>    report, ~30 subagent notes, experiments). Recreate if the machine rebooted:
>    `git worktree add /tmp/aipm-agentb-branch origin/agent-b/op-exposed-hull-orchestration`.
> 4. Work queue lives in beads: `bd show aipm-3u6` (σ_v-wall, the terminal open) → `aipm-e71`
>    (HLC) → `aipm-nhj`/`aipm-mox` (absorbed faces) under epic `aipm-and`.
> 5. Codex (gpt-5.5) delegation cheatsheet: `CODEX_DELEGATION.md` at repo root (untracked, user's
>    file). User quota was ample as of 2026-06-10 (~few % used); confirm before heavy waves.

## Mission & done bar (user-approved)
Prove **op-classical** dimension-free (row-stochastic Q, ‖Q²−Q‖ ≤ η ⇒ stochastic idempotent within
C√η, C universal) **or** refute it. PROOF-DONE = rigorous prose + every lemma verified by **two
model families** (Claude + gpt-5.5/codex) with ≥1 adversarial pass + refs byte-grounding;
af-validation is a follow-on phase. COUNTEREXAMPLE-DONE = exact-rational family + verifier script,
2-family reproduced. HONEST-STALL = precise obstruction map (PRD-legitimate outcome).

## Where the mathematics stands (2026-06-10 EOD)

```
op-classical ⟸ thm-cluster (proved, main) + op-exposed-hull
op-exposed-hull ⟸ HLC               [2-family-VERIFIED assembly, C′ = max(4A, 1/√a)]
                                     notes/wave2/W2d-grand-assembly.md (+ assembly-verification-opus.md)
HLC ⟸ σ_v-wall lemma                [conditional glue, a = min(4/B_A², 1/B_B²)]
                                     notes/endgame-sigma-wall-residual.md
σ_v-wall: MEASURED, UNPROVED — THE terminal open (bead aipm-3u6):
  (A) hidden vertex v with external mass σ_v ≤ 1/2  ⇒  H ≤ B_A·σ_v·τ        [measured law]
  (B) σ_v ≥ 1/2 and H > B_B·τ  ⇒  v is (ρ,κ)-exposed (margin pins at κ)     [measured B_B = 0.536]
  Sub-residual on one route: ψ-gap lemma ("ρ-far non-S-full rows have ψ-gap ≥ κZ").
```
Setting/notation: P n×n real, P1=1, P²=P exact, row neg mass ≤ δ, τ=√δ, ρ=4τ, κ=τ/4, ℓ¹ geometry,
W = (ρ,κ)-well-exposed row vertices (row-set-intrinsic), H = max_i dist₁(p_i, conv W).

**Numerics (validated pipeline):** NO counterexample in 67k+ verified exact instances over 4
independent campaigns; universal floor δ/H² = 3.484 at the hard wall H/τ = 0.536 (d3, d7, d8
concur); σ_v-wall law H/τ ≈ min(σ_v, 0.536); the MRP middle regime is the SAFEST region (fable's
borderline worry dissolved — d8). Verdict probabilities (codex-calibrated): P(HLC true) ≈ 0.75–0.8.

**Literature (TIB sweep, notes/literature-sweep-hlc.md):** HLC is VIRGIN ground — it is the first
quantitative stability version of Douglas(1965)/Ando(1966) "contractive unital projections are
conditional expectations" (here: ‖P‖_{∞→∞} ≤ 1+2δ unital projection on ℓ∞ⁿ near a contractive one).
Kitaev 2405.02434 is the closest relative (CP-only). Standalone publishable either way.

## The proved belt (~17 lemmas, ALL independently audited — use audited constants!)
Constants/correctations: **notes/wave4/audit-summary.md** is authoritative over original statements.
- L1 lone-far-row (margin ρ/(2+4δ); ρ-ball exemption) — wave1/A1.
- L2 far row ⇒ far hidden vertex; L2′ ρ-shadow — wave1/A2 (its part (iii) recursion is GAPPED:
  can stall at v; R1's repair is correct but VACUOUS at scale — see R1 annotation).
- C10 failed-exposedness LP dual (α-mass uncontrolled — the historic crux).
- L4 frame-clipping; L5′ leakage AT GLOBAL MAXIMIZER ONLY (general-row version FALSE) — wave1/A4.
- L6 identity-frame LINEAR bound δ ≥ H/2 (R=[I|0] only; metric transfer open) — wave1/A3.
- N1 nilpotent-chain off-chain forcing; F1 skinny near-coincidence; X1 one-mode wall (diam ≥ 2);
  X2 stochastic-complement rank preservation — wave1/N1, F1; wave3/X1, X2.
- Fable belt (notes/fable-hlc-attack.md §6.1, audited wave4): F-SS sharp shadows; F-ND near-δ
  exposure (c=0.85); F-E kernel energy Γ = P(g²)−g², PΓ=0, starvation ≤ 2δ(1+δ)R²/E (R=osc(g));
  F-GB g-budget σℓ ≤ g_j + δR; F-WR wiggle rigidity (SIDE CONDITIONS: self-indexing, small δ;
  separation corollary needs R_w ≤ 2ρ) — subsumes X1 all k; F-BC blocker cap (κ+δ); F-2R private
  2-shells collapse. F-ψ is CONDITIONAL (ψ-gap missing) — do NOT cite as proved.
- Conceptual: Γ = P(g²)−g² is the classical analogue of the main project's square-hole object.

## Dead routes (proved dead — never re-walk; full map in ORCHESTRATION.md + notes/wave1-3)
Averaging/quasi-stationary potentials; projection norms via height tests (Px ∈ [0,1]); raw circuit
bounds; UNLOCALIZED dual descent (constant loss ≥ ~1/4 ≫ H); maximality contradictions sans
localization; rank induction via stochastic complement; KKT localization-energy dichotomy; pure
convex shadow composition (vacuous μ→1); log-staircase/shells (exactness is the wall — X1).

## Numerics infrastructure (validated; reuse, don't rebuild)
`experiments/d1_infra.py` (robust margin-max exposedness LP — presolve OFF mandatory; robust_linprog)
+ `d3_vertexfix.py` (multiplicity-correct vertex test — MANDATORY; coincident rows fabricate fake
counterexamples) + d7/d8 patterns (alternating exact (Λ,R) LPs, verified-entry gates, honest τ from
the instance's own δ). Regression tests: `test_lp_robustness.py`, `d3_vertexfix.py` (run directly,
not pytest). KNOWN METHODOLOGY GAP: d8 persisted only primal collapse margins — **rerun persisting
LP DUAL certificates** before the next proof push (this is NEXT step 1).

## NEXT (priority order)
1. **Rerun the d8/MRP decider persisting dual certificates** (gurobi Pi/IIS per σ_v cell) — opus
   worker, brief pattern in ORCHESTRATION ledger #12/d8. Output: certificate shapes across the
   σ_v sweep = the analytic blueprint for the σ_v-wall.
2. **Fable closer on the σ_v-wall** (aipm-3u6) with certificates in hand. MANDATORY: file-based
   incremental output protocol (see LLM-LEARNINGS — a 64k-output-cap loss already happened once);
   prove branches (A)+(B) or the precise failing inequality. Then 2-family audit (derive-first).
3. If proved: full prose write-up of the chain (σ_v-wall → HLC → op-exposed-hull → op-classical via
   thm-cluster), 2-family verification per done-bar, then Recipe A→B banking on main (the belt is
   large — batch as registry shards + af workspaces; report upkeep per aipm-6ct conventions).
   Refs to byte-pin first (lazy, L1): Douglas/Ando (PDF-only — flag), Hadwin–Li 1601.05445,
   Curgus–Jewett 0709.0309 (see literature note).
4. If stalled again: write the honest obstruction map (the material is publishable: conditional
   theorem + audited belt + dead-route map + measured wall) — PRD-sanctioned outcome.
5. Parked lanes B (Baake–Sumner coupling) / E (variational) / G (ultraproduct): only revive if the
   σ_v-wall attack suggests their tools (X3's equal-input lemma is the bridge to lane B).

## Delegation protocol (hard-won; details in LLM-LEARNINGS.md)
- codex: `cat brief | codex exec --skip-git-repo-check -C <dir> -s read-only --json -o answer.md -`
  NEVER `--ephemeral`; exec-level flags BEFORE the `resume` subcommand; thread-resume = cheap
  continuation (cached). Progress-message protocol in every brief (wedge detection + checkpoints).
  Monitor harness: tail --json events + answer-file/process-death/stall detection; byte-flow check
  (`/proc/<pid>/io` rchar over 15s) for silent wedges; never pkill with self-matching patterns.
- Long math subagents (esp. fable): deliverable = FILE, written incrementally; final message ≤300
  words. Audits: derive-first (statement only → own proof → then read recorded proof → verdict
  first line). Every consequential error this campaign was caught by a NON-author — keep that.
- Worker mix that worked: codex xhigh (proving/auditing, 2nd family), opus+tools (numerics
  campaigns, 90-min runs fine), sonnet (scout/summarize), fable (crux only; file protocol).

## File map (this directory)
ORCHESTRATION.md (campaign log + EOD snapshot + ledger) · LLM-LEARNINGS.md (meta-experiment) ·
notes/: d0–d7 arc, fable-hlc-attack.md (§6.1 facts, §6.2 MRP), wave1–4 audits + audit-summary,
mrp-decider-report.md, endgame-sigma-wall-residual.md, literature-sweep-hlc.md, agentB-n4-*.md ·
experiments/: d1/d2/d3/d7/d8 pipelines + out/*.json + regression tests.

## Hygiene notes
- `agent-A/lean-formalisation-coverage.md` is modified in the working tree from BEFORE this
  sidequest (not ours) — leave it.
- `CODEX_DELEGATION.md` (repo root) is untracked, user-owned — leave untracked.
- The pre-commit hook runs the full check-all (incl. latexmk) on every commit — let it.
- Beads sync: `bd export -o .beads/issues.jsonl` before committing issue changes.
