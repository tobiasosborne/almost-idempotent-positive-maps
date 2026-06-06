<!--
ROLE: append-only log of retracted/corrected claims and hard-won lessons, so the project does not
re-make a mistake it already paid for. The single failure mode is a confident plausible WRONG claim;
this file is its graveyard.
UPDATE POLICY: append a dated entry when a claim is retracted or a lesson is learned; never delete.
TRIGGER: a claim is withdrawn, a constant/exponent is corrected, or a process mistake recurs.
-->

# LEARNINGS — retracted claims & hard-won lessons

Cross-referenced from `CLAUDE.md` §3 (hallucination callouts). The repo (registry + report + refs) is
canonical; conversation, memory, and prior-session summaries are not.

## Retracted / corrected claims

**R1 — "A faithful invariant state ⇒ `O(η)` defect / approximate ordinary-∘ closure." → WITHDRAWN.**
Agent A asserted YES (findings v0.10); Agent B refuted with the `T_a` family (faithful for all `a>0`,
`η_a→0`, yet ambient hole `→2/9` with floor `λ=a/3=Θ(η)`); A conceded (v0.11). Correct statement: the
defect is `O(η/λ)` and needs a **dimension-free spectral floor `λ`**, which faithfulness alone does not
provide. Registry: `thm-faithful-approx` (the `O(η/λ)` bound), `prop-faithful-counterexample`,
`ex-no-faithful`. Memory: [[project-faithful-invariant-transfer]].

**R2 — "Layer-1 is resolved because the coboundary splitting is Frobenius-bounded." → CORRECTED.**
An earlier "resolved in principle" was retracted: **Frobenius-boundedness does not imply order-unit
boundedness** — the conversion can lose `√rank` (`prop-rank-gap`, `obs-cochain-caveats`). Current honest
status: the order-unit splitting is proved for **exact cocycles in the adjoint module**
(`cor-adjoint-benchmark`, *modulo* the `obs-matrix-audit` re-audit, `aipm-36d`); the **full Layer-1
structure theorem stays OPEN** (`op-layer1-gap`). The 2026-06-04 numerical smoke test gave only
*encouraging evidence*, not a proof.

**R3 — Phantom "Agent-A positions." → IGNORE.** Agent B's subagent pipeline once generated
`agent-B/notes/response-to-agent-a-v0.6 … v0.18.md` replying to A-positions that were never written
(subagent extrapolation). **`agent-a-findings` is the single source of truth for A's positions**; ignore
phantom "A versions". Memory: [[project-collaboration]].

**R4 — "rank-balance" intermediate claim. → retracted (see findings).** A rank-balancing step in the
spin/matrix exact-adjoint splitting line was withdrawn during the order-vs-Frobenius re-audit. Precise
details live in `agent-a-findings` / `agent-b-findings` (the Layer-1 / spin-splitting threads) and the
caveat is captured in `obs-cochain-caveats` / `rem:cochain-caveats`. *Expand this entry when the exact
statement is re-extracted from the findings.*

**R5 — Fabricated "verbatim" external quote (`GT-bhsa-jc`). → corrected + machine-gated.** During the
Phase-3 af bridge proofs, two build provers seeded the af external `GT-bhsa-jc` with a *plausible but
fabricated* "VERBATIM" quote — *"If A is a C\* algebra then A_sa with the Jordan product a∘b=½(ab+ba) is a
JB algebra"* — attributed to `refs/hos/joa-m.md:2300` (HOS 3.1.2). **That string is not in the source.** The
real 3.1.2 only defines `B(H)_sa` as a *JC* algebra ("any norm-closed Jordan subalgebra of `B(H)_sa`"); the
JC→JB step is the separate HOS line 2320 ("each JC algebra is a JB algebra", now `GT-jc-is-jb`). The *fact*
is true; the *quote* was a paraphrase from memory — exactly the L1 failure mode. It reached a **pushed
commit** (`lem-square-hole`, `73b240b`) because that workspace's verifiers grep-confirmed a *substring*, not
the full quote; `lem-bridge-polar`'s verifier caught it (target=context). **Fix:** both quotes corrected from
the actual bytes, `GT-jc-is-jb` added, the JB-using nodes re-grounded JC→JB, both lemmas re-validated.
**Prevention:** `scripts/check-refs.py` (gate, `aipm-6ao`) byte-matches *every* af-external verbatim quote
against its cited `refs/` locus, wired into `check-all.sh` so the pre-commit hook blocks the whole class;
17 red→green tests (`scripts/tests/test_check_refs.py`). Known gate blind spots (skip-no-quote evasion;
single-run false-negative) tracked in `aipm-iel`.

## Standing lessons

- **No-overclaim is the prime directive.** `√η` general (not `η`); Layer-1 structure theorem and exact
  UP factorization OPEN; `obs-matrix-audit` is a real consensus-pending caveat, not a footnote.
- **Ground truth before claims.** Stale paths (`/home/tobiasosborne/...` in `agent-A/HANDOFF.md`) and
  extraction-level provenance (`thm-whitehead`, `prop-aut-compact`) must be flagged, not trusted.
- **Re-derive status from the registry, not from a handoff.** `agent-A/HANDOFF.md`'s math is mostly
  current but its file map is stale and its Layer-1 framing predates `cor-adjoint-benchmark`.
- **"Verbatim" means byte-match the WHOLE quote, not a substring.** A prover can paraphrase a true fact
  into a false "verbatim" string (`R5`); verifiers must `grep -F` the *full* quoted text, and
  `scripts/check-refs.py` enforces it mechanically in the pre-commit hook. Every discovered failure mode
  earns a red→green test/gate (`aipm-6ao`, `aipm-iel`).
