<!--
ROLE: crash-safe handoff for the classical-portfolio sidequest (Agent A exploration lane).
Branch: agent-a/classical-portfolio. Rewritten at session close (2026-06-11, day-2 end).
-->

# HANDOFF — classical-portfolio sidequest (op-classical / op-exposed-hull)

> ## START HERE (next agent)
> 1. Branch **`agent-a/classical-portfolio`** (exploration lane; canonical layers via
>    Recipe A→B + reviewer ≠ author only — repo CLAUDE.md).
> 2. Read order: repo gate files → this file → **`notes/wave5-sigma-wall-parallel.md`**
>    (THE day-2 dossier: waves 5–13, read the FINAL sections first — they supersede
>    earlier ones) → `notes/swarm-answers/` (45+ archived worker verdicts, every died-at
>    in display math) → `report/` (the 49pp self-contained LaTeX report, v3, delivered).
> 3. Day-1 material: `ORCHESTRATION.md` + `notes/wave4/audit-summary.md` (audited
>    constants) + `notes/fable-hlc-attack.md`. Numerics: d1–d14 in `experiments/`.
> 4. Beads: `bd show aipm-3u6` (carries THE KERNEL) → `aipm-e71` (HLC) → the
>    Högnäs–Mukherjea acquisition bead → epic `aipm-and`. Report bead `aipm-sjw` done.

## THE KERNEL (the single remaining open, after 13 waves / 10 strategy kinds / ~60 workers)
**Path-product floor:** for the band component C of any hidden top vertex with σ̃ > τ,
  Π_C ≳ τ − O(Lδ)  (thin-chain exclusion).
- TRUE ⇒ component finisher (PROVED, w12) + s8 branch (PROVED) ⇒ **LINEAR LAW δ ≥ cH**
  ⇒ HLC ⇒ op-exposed-hull ⇒ op-classical. Every other link proved or proved-mod-audit.
- FALSE ⇒ first-ever H ≫ δ instance (two refuters failed to build one; quantified
  failure maps archived).
- Empirics: the ENTIRE record (67k+ instances, d8–d14) fits δ ≥ ~H/2; the √δ "flat
  floor" was a corner extrapolation (d13, high strength).

## Landmark results of day 2 (all in the dossier, statuses per its tags)
- **Corner theorem** (2-family): τ* = 2−√3, wall H/τ = 2(2−√3) = 0.53590, floor
  δ/H² = (7+4√3)/4 = 3.48205 — finite-δ corner, NOT asymptotic.
- **σ̃-height-collapse** (proved): σ̃ ≤ s ⇒ H ≤ δΩ/(1−s); contrapositive σ̃ ≥ 1 − δΩ/H.
- **s8 branch** (proved): σ̃ ≤ τ ⇒ H ≤ 3τ ⇒ δ ≥ H²/9 (HLC direct there).
- **t10 Birkhoff finisher** (proved): bounded projective diameter + ε-idempotence ⇒
  row collapse (no spectral gap); **w12 component finisher** (proved): fat components
  collapse-and-expose; survivor = thin chains.
- **d14**: positive kernel closes exactly (λ⁺ = 0); only v's δ-budget negatives cross.
- **Refuted/downgraded:** literal ψ-gap (×2, conditioned variant proved instead);
  literal T_far = ∅; NG′; the linear financier law's scale claim; d12's broad verdict.
- **s5**: exact all-shallow optimal face EXISTS (low height only — σ̃ < τ).
- **Wave-10 meta-theorem:** "hiddenness IS the LP frame" (5 strategy kinds collapsed);
  canonical W-free statement = B–S normal-form distance (audited: target, not route).
- **Source discovery:** Baake–Sumner cite Högnäs–Mukherjea WITHOUT proof — the δ=0
  anchor needs its own byte-pin (bead filed; TIB).

## NEXT (priority order)
1. **Acquire + byte-pin Högnäs–Mukherjea** (bead), then re-run the proof autopsy
   (notes/swarm-answers/w105_bsautopsy.md) on the REAL δ=0 proof — the only unwalked
   analytic path; its mechanism may dictate the δ > 0 surrogate for the kernel.
2. **Chain-specialized SOS/certificate search** (small n, the REDUCED thin-chain
   inequality — distinct from wave-10's collapsed full-problem SOS).
3. If both stall: **the honest-stall write-up is PRD-sanctioned and 90% done** —
   report v3 (delivered) + the dossier's FINAL STATE section = the obstruction map;
   then Recipe A→B banking of the proved belt on main (large: batch as registry
   shards + af workspaces; the af follow-on phase per the done-bar).
4. Periodic-component patch for the w12 finisher (its declared primitivity gap —
   refuter #2's dichotomy suggests it's benign; prove it).

## Protocol (hard-won; LLM-LEARNINGS.md + memory)
- Codex swarms liberal (user standing order); opus serial; fable per-approval with
  the file-protocol MANDATORY. Briefs: progress-protocol, verdict-first, died-at in
  display math, calibrated P's, anti-collapse rule for strategy diversity.
- Watchdogs on every detached fleet; archive every answer into notes/swarm-answers/
  IMMEDIATELY (tmp is volatile); harvest file updated per landing, committed per wave.
- All numerics: presolve OFF, multiplicity-correct vertices (d3_vertexfix), honest
  τ = √δ from the instance's own δ. Violations fabricate structure.

## Hygiene
- `agent-A/lean-formalisation-coverage.md` working-tree mod predates the sidequest — leave.
- `CODEX_DELEGATION.md` (repo root) untracked, user-owned — leave.
- Report PDF is gitignored; rebuild via `cd report && latexmk -pdf main.tex`.
- `bd export -o .beads/issues.jsonl` before committing issue changes; full check-all
  (incl. latexmk) runs on every commit — let it.
