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

**R6 — `η₀=1/4` asserted where `η₀<1/4` is *strictly* required (boundary divergence). → corrected.** The
`thm-bridge` capstone build (nodes 1.7/1.8) fixed a concrete cutoff `η₀=1/4`. But `lem-P-properties`
requires `η₀<1/4` **strictly**: `P=θ(2Φ−1)` is built from the binomial series
`R=(S²)^{−1/2}=(1−4(Φ−Φ²))^{−1/2}`, which converges only for `4η₀<1`. At the boundary `4η₀=1` the constant
`C(η₀)=Σ|aₙ|(4η₀)^{n−1}` **diverges** (`∼2√(N/π)`, numerically confirmed), so `C₁,C₂,C₃→∞` and the
theorem's "universal dimension-free constants" guarantee fails. A fresh verifier caught it
(target=statement on node 1.8); fixed to `η₀<1/4` fixed (e.g. 1/8). The *fact* (bridge holds for small η)
is fine; the *admissible-range boundary* was wrong.

**R7 — A fresh VERIFIER produced a confident, plausible, WRONG counterexample. → refuted before acting.**
Reviewing the `thm-dilation-compatible` scaffold, the fresh verifier (agent-A) challenged node 1.3.3's
premise *"Φ=Cj inherits `‖Φ²−Φ‖≤η`"* as a **"critical false premise,"** backing it with a numeric
counterexample (`‖F²−F‖≈0.229<¼` while `‖Φ²−Φ‖≈0.258>¼`) and recommending the theorem's hypotheses be
amended. **The counterexample is false.** Independent recheck: **7,008,000** samples over *all* unital 0/1
order-isometric embeddings `j:ℓ∞_nin→ℓ∞_nout` (dims to 4→6) with random row-stochastic `C` gave **zero**
violations of `‖Φ²−Φ‖≤‖F²−F‖` (worst ratio exactly 1.0000). **Proof:** `Φ²−Φ=(Φ−I)Cj`, `F²−F=j(Φ−I)C`;
since `j` is order-isometric (`‖jM‖=‖M‖`, `‖j‖_op=1`), `‖Φ²−Φ‖=‖(Φ−I)Cj‖≤‖(Φ−I)C‖=‖j(Φ−I)C‖=‖F²−F‖`. The
verifier's `j` must have violated the order-isometric/injective hypothesis (or held an arithmetic slip).
So the theorem is **sound**, its hypotheses **sufficient**, and **no contract amendment** was warranted —
the premise is a clean provable inequality, which becomes a *derived* af node (the regression) inside the
new `lem-intertwine-spectral-idempotent` (`aipm-vp5`). The *same* review was simultaneously **correct** that
the two η-delivering steps (node 1.2 the C\*→ε-JB symmetrization, node 1.3 the intertwining) were
asserted-not-derived — those are genuinely factored into sub-lemmas. Net: theorem true; proof was a
scaffold; one of the verifier's two "critical" findings was itself a false claim caught only by an
independent recheck.

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
- **Respect strict-inequality thresholds inherited from imports.** A downstream node asserting a closed
  boundary value (`η₀=1/4`) where an import needs strict `<` (`η₀<1/4`) silently voids the
  universal-constant guarantee (`R6`); verifiers must check the *admissibility* of inherited cutoffs, not
  just the leading-order rate.
- **A verifier can be wrong too — a refutation is itself a claim.** Reviewer≠author cuts *both* ways. Before
  acting on a verifier's counterexample (especially before weakening a theorem's hypotheses), independently
  reproduce it. An agent's "critical false premise" (`R7`) was refuted by a 7M-sample sweep + a one-line
  proof; the premise was in fact a provable inequality. Numerics + an independent derivation are the cheap
  cross-check; never amend a statement on a single unverified counterexample.
