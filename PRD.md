<!--
ROLE: the entry point. WHAT this project is, what is in/out of scope, the math goal + honest status,
canonical artifacts, success criteria, open obstructions, milestones. (HOW to work lives in CLAUDE.md.)
UPDATE POLICY: refreshed at phase boundaries / when proved↔open status changes; substantive edits are
review-gated. Date every status claim. Keep ≤ ~250 lines.
TRIGGER: a result moves proved↔open, a milestone completes, or scope changes.
-->

# PRD — almost-idempotent positive maps / approximate Jordan algebras

> **Router.** *Scope / what may I change?* — this file (canonical). *How to work / process?* — `CLAUDE.md`
> (== `AGENTS.md`). *Current build state / next task?* — `HANDOFF.md` then `bd ready`. *Approved design?* —
> `docs/plans/2026-06-05-argument-architecture-plan.md`.

**Status of this document:** living charter, last refreshed **2026-06-05** (Phase 2b complete).

---

## Mission

Generalise **Kitaev's theorem on almost-idempotent quantum channels** (arXiv:2405.02434) from
**completely positive** maps to merely **positive** maps, and prove the result rigorously to **A+B
consensus**. Kitaev: an `η`-idempotent unital CP map on `B(H)` has near-fixed-points forming an
approximate **C\*-algebra**, and every finite-dimensional approximate C\*-algebra is `O(η)`-close to a
genuine one (dimension-free). **Our thesis:** for merely positive maps the right invariant is a
**Jordan (JB) algebra**, not an associative one — because positive maps obey **Kadison's** inequality
`Φ(a)² ≤ Φ(a²)` but **not Schwarz** `Φ(a)*Φ(a) ≤ Φ(a*a)` (which needs 2-positivity). The setting paper is
**van Luijk–Wilming** (arXiv:2604.08380): the sufficient invariant for positive trace-preserving maps is
a **Jordan `J*`-algebra**.

The dominant work-mode is **mathematical proof** recorded as a typed module system (see `CLAUDE.md` §5):
definitions → contracts → per-lemma adversarial (`af`) proofs → a paper.

## Read order (any agent, by file name)

`PRD.md` (this) → `CLAUDE.md` → `HANDOFF.md` → `definitions/INDEX.md` → `argument/INDEX.md` (+ `DAG.md`).
You may not add mathematical content until you have read these (`CLAUDE.md` §0).

## Scope

**In scope.**
- The two target theorems below (Layer 2 bridge — proved; Layer 1 structure — open) and their honest
  status, constants, and exponents.
- The Definitions DB, the argument registry/DAG, per-lemma `af` proofs, and the LaTeX report — all kept
  in lockstep and provenanced to local ground truth.
- Supporting mathematics already underway: exact UP factorization (`op-npps` route), classical/commutative
  stability, the Layer-1 cohomological error-reduction programme, the exponent (`√η` vs `η`).

**Out of scope (anti-goals — adding these is a stop condition).**
- Remote CI (GitHub Actions). The only gate is the **local** `scripts/check-all.sh`.
- A Lean formalization as a dependency. Lean is **secondary/deferred** (Phase 5); `af-tests` is
  reference-only; there is **no af→Lean generator**.
- Any claim from memory or a paper not present in `refs/` (acquire + register first — `CLAUDE.md` L1).
- Turning an `(open)` statement into a theorem without A+B consensus.

---

## The mathematics

### Two-layer theorem

- **Layer 2 — the BRIDGE — PROVED (`α = 1/2`).** For unital positive `Φ : B(H)_sa → B(H)_sa` with
  `‖Φ²−Φ‖ ≤ η` (operator norm of the map; constructing `P` needs `η < 1/4`, the bridge conclusion holds
  for `η ≤ η₀` with `η₀` a universal constant), let `P = θ(2Φ−1)` (spectral idempotent),
  `A = Im P`, product `a•b = P(a∘b)` with `a∘b = ½(ab+ba)`. Then `A` is an **ε-JB algebra** with
  **`ε = O(√η)`** — **unconditional, dimension-free, CP-free** (no dilation/Stinespring). Registry
  `thm-bridge`; prose proof `agent-B/theory/theorem-B-algebraic-bridge.md` (transcribed to
  `report/sections/06-bridge-theorem.tex`, A-verified) and **now MACHINE-VALIDATED via `af`** — all 9
  results of the bridge DAG are `af: validated` in `proofs/`, every leaf byte-grounded in `refs/`.
- **Layer 1 — the STRUCTURE THEOREM — OPEN.** Conjecture: every finite-dimensional ε-JB algebra is
  `C·ε`-Jordan-isomorphic to a genuine finite-dimensional JB-algebra, with **dimension-free `C`**. This is
  Kitaev's hard half, Jordan-ised. Registry `op-jordan-structure` (open). Strategy mirrors Kitaev:
  approximate Jordan frame → Peirce → coordinatization (JNW) → **error reduction** (the cohomological
  heart).

### The ε-JB algebra (central consensus definition — `def-eps-jb-algebra`)

A finite-dimensional real **order-unit space** `(A, 1, ≤)` with order-unit norm and a commutative
bilinear product `∘` for which **commutativity `a∘b=b∘a` and the unit law `1∘a=a` are EXACT**, with
`(JB1) ‖a∘b‖ ≤ (1+ε)‖a‖‖b‖`; `(JB2) ‖a∘a‖ ≥ (1−ε)‖a‖²`; `(JB3) a∘a ≥ −ε‖a‖²·1`;
`(JB4) ‖((a∘a)∘b)∘a − (a∘a)∘(b∘a)‖ ≤ ε‖a‖³‖b‖`. At `ε=0` these degenerate **exactly** to the JB-algebra
axioms (HOS 3.1.3–4). **Key design point:** order, unit, and norm are **exact** (inherited from `B(H)`);
only the product is approximate — strictly cleaner than Kitaev's approximate-norm ε-C\*-algebras.

### Analogy to Kitaev — and what does NOT transfer

| Kitaev (CP) | Here (merely positive) |
|---|---|
| Schwarz `Φ(X)*Φ(X) ≤ Φ(X*X)` (needs 2-positivity) | only **Kadison** `Φ(a)² ≤ Φ(a²)`, self-adjoint `a` |
| associative product `X⋆Y = Φ̃(XY)` → **C\*-algebra** | Jordan product `a•b = P(a∘b)` → **JB-algebra** |
| `ε = O(η)`, dimension-free | `ε = O(√η)` in general; the Kitaev-strength `O(η)` is CP/dilation-only (decomposable conjectural) |
| structure theorem via C\*-rigidity | Jordan structure theorem (**open**) |

**Does not transfer:** the "two-hole-at-once" bilinear pairing that buys Kitaev `O(η)` lives in the
Stinespring dilation, unavailable for general positive maps — a single insertion is only `O(√η)`.

---

## Current state (2026-06-06)

**Built (the typed module system).** Definitions DB (24 shards; gate 0 errors, 3 draft warns); argument registry **56
results** acyclic (`argument/INDEX.md`/`DAG.md`, linker 0 errors/0 warnings, 19 ready / 16 blocked);
local pre-commit gate `scripts/check-all.sh` = `OK` (defs + **`check-refs` provenance gate** + linker +
tests); deduped `refs/` + checksummed manifest; the LaTeX report builds clean.
**Layer 2 `af`: the algebraic bridge (Theorem B) is FULLY VALIDATED — all 9 of its workspaces are
`af: validated` in `proofs/` (machine-checked; every leaf byte-grounded in `refs/`), committed + pushed.**
Next: harden `check-refs` (`aipm-iel`), audit `cited` results (`aipm-17f`), then the Layer-1 frontier.

**Canonical artifacts (file → invariant).**
- `definitions/` — every term defined exactly once; `check-defs.py` is the drift guard.
- `argument/lemmas/*.md` — every result's one-line **contract**; the DAG is acyclic and the linker enforces it.
- `argument/INDEX.md` / `DAG.md`, `definitions/INDEX.md` — **generated**, never hand-edited.
- `refs/manifest/{SOURCES.md,checksums.sha256}` — the ground-truth ledger (50 files; `sha256sum -c`).
- `report/` + `report/PROVENANCE.md` — the paper; every statement provenanced.
- `HANDOFF.md` — current build state; `bd ready` — the work queue / proof frontier.

## Success criteria

1. **Layer 2 bridge** stated, proved, A+B-consensus, and `af`-validated; transcribed faithfully in the report.
2. **Layer 1 structure theorem** proved with a **dimension-free** constant (the headline open goal), or its
   precise obstruction published honestly.
3. Every named definition/theorem **byte-matched** to local ground truth (no undischarged claim).
4. The argument DAG is fully `af`-validated leaf-to-root (`bd ready` → empty proof frontier).
5. No overclaim: every `(open)` is tagged; constants and exponents are exact.

## Known limitations / open obstructions (each → registry id · bead)

- **Layer-1 dimension-free constant** — `op-jordan-structure`, `op-layer1-gap` · `aipm-245`.
  Error-reduction needs a dimension-free **order-unit**-bounded right-inverse of the Jordan coboundary `d¹`
  (Frobenius-boundedness does **not** suffice — the conversion can lose `√rank`, `prop-rank-gap`). This is now
  **proved at the exact-adjoint benchmark level** (`cor-adjoint-benchmark`, assembled from spin / direct-sum /
  commutative-scalar / matrix splittings) — **modulo the `obs-matrix-audit` re-audit** of the matrix piece
  (`aipm-36d`). **Still OPEN** (`op-layer1-gap`): the gap to the full structure theorem — the next-arrow
  estimate for **arbitrary (non-adjoint) modules**, the pre-cohomological frame/Peirce/coordinatization
  construction, approximate-module tolerance, gauge stability, incremental assembly, and a positivity-capable
  output. (The 2026-06-04 numerical smoke test gave only *encouraging evidence*; the analytic benchmark supersedes it.)
- **Exact UP factorization** — `op-npps`, `op-exposed-hull` · `aipm-08u`. A generic `O(ε)` positivity-rounding
  is **provably false** (`prop-rounding-fails`). Route: near-positive-projection stability at sharp exponent
  `½`; commutative case reduced to stochastic-matrix stability with many special cases proved; the general
  "exposed-redundant dichotomy" and the non-commutative case are open.
- **The exponent** — `op-decomposable`, `obs-exponent`. `O(√η)` unconditional; `O(η)` is CP-only and
  **conjectural** for decomposable (CP+co-CP) maps.
- **Matrix exact-adjoint benchmark** — `obs-matrix-audit` · `aipm-36d`. B's high-rank splitting claim awaits
  independent re-audit (earlier Haagerup route had an ordinary-vs-cb gap).

## Validation gates & milestones

Gates (declare per commit, `CLAUDE.md` §7): **M**echanical · **D**efinitional · **C**ross-reference ·
**R**eviewer ≠ author · **I**dempotent.

Milestones (`docs/plans/2026-06-05-...`): **Phase 0** refs/bd ✓ · **1** Definitions DB ✓ · **2** registry +
linker ✓ · **2b** registry seeded (56 results) ✓ · **3** per-lemma `af` — **the whole algebraic bridge
(9 workspaces) is validated** ✓ · **4** context-hygiene docs ✓ (reorg `aipm-chn` pending) · **5** Lean
scaffold (deferred, `aipm-3ox`).

## Escalation

Stop and ask the user (see `CLAUDE.md` §9) when: ground truth is missing from `refs/` (never paraphrase —
a refs external's verbatim quote must byte-match its locus; `check-refs` blocks fabrications, LEARNINGS R5);
a change would be out of scope; the linker reports an unresolvable drift/cycle; a definition must change;
or you would turn an `(open)` into a theorem. *(af itself is established — no per-workspace user hint needed.)*
