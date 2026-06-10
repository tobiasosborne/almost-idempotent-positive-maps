<!--
ROLE: living orchestration log for the classical-portfolio sidequest (Agent A, exploration lane).
Branch: agent-a/classical-portfolio. Canonical promotions go through Recipe A→B on main ONLY.
UPDATE POLICY: rewritten sections as state changes; delegation ledger is append-only.
-->

# Classical portfolio — orchestration

**Goal.** A fully rigorous, dimension-free proof of `op-classical` (every row-stochastic Q with
‖Q²−Q‖_{∞→∞} ≤ η ≤ η₀ is within C√η of a stochastic idempotent, C universal) **or** an explicit
counterexample. Equivalent exact form (`lem-classical-equiv`, validated): P signed affine retraction
(P1=1, P²=P, neg(p_i) ≤ δ) ⇒ stochastic idempotent within C√δ.

**Done criteria (user-approved 2026-06-10).**
- PROOF-DONE: complete prose proof, every lemma verified by **two independent model families**
  (Claude-family + gpt-5.5/codex) with ≥1 adversarial pass; every external fact byte-grounded in
  `refs/`. af-validation = follow-on phase (beads filed).
- COUNTEREXAMPLE-DONE: explicit exact-rational family + verification script (P1=1, P²=P, neg ≤ δ,
  dist to EVERY stochastic idempotent ≥ K_n√δ, K_n → ∞), reproduced by two model families.
- HONEST-STALL: all lanes blocked on named precise obstructions → obstruction map to user.

**Mode.** Serial delegation (one subagent at a time, economy + continuous learning). I (Agent A,
orchestrator) write briefs, review every hand-back, log learnings, raise beads, switch lanes.

**Switching rules.** Switch lane when (a) a kill criterion fires; (b) a blocker survives two
independent attacks by different model families; (c) another lane's finding opens a cheaper door.
Every switch logged here + worklog.

**Tooling on this machine.** mosek, gurobi (`gurobi_cl`), wolframscript, numpy/scipy/HiGHS,
`codex exec` (gpt-5.5, xhigh default; see CODEX_DELEGATION.md). TIB network: paywalled papers
accessible — refs acquisition is unblocked.

**Observability protocol (user directive 2026-06-10): verbosity + eager flush in ALL activities.**
- Every long-running delegated process streams a live trace to a file: codex → `--json` events
  (never `--ephemeral`); python → `python3 -u` (+ per-iteration prints); shell pipelines →
  `stdbuf -oL -eL`; solvers → native log files (gurobi LogFile, mosek log).
- Heartbeat rule: any run expected >2 min must emit progress at least every ~60s; silence beyond
  ~3× the expected cadence ⇒ byte-flow check (`/proc/<pid>/io` rchar delta over 15s) ⇒ kill+resume.
  Watchdog timeouts on all launches.
- Process-hygiene: never `pkill -f`/`pgrep -f` with a pattern contained in your own command line
  (self-match kills your own shell); use bracket-grep `[c]odex` or kill by recorded PID.

**Delegation matrix (initial; evolves via LLM-LEARNINGS.md).**
| Step type | Worker |
|---|---|
| Ideation / reformulation | gpt-5.5 codex (read-only) |
| Lemma proving / derivation | Opus 4.8 high |
| Cross-check of load-bearing derivation | codex xhigh (second family) |
| Numerics write+run | codex workspace-write (gurobi/mosek) or sonnet |
| Lit scouting / refs byte-pinning | sonnet |
| Adversarial verify (suspect, load-bearing) | Opus xhigh; fable only if survives opus and still suspect |

---

## Lanes

### Lane D — plateau analysis / global potential (REFORMULATED 2026-06-10)
Original form (opus strategist): global transport-duality contradiction (m-average of dual potential
= O(δ) vs √δ plateau). **Orchestrator analysis (UNVERIFIED — delegation D0 cross-checks):** the
m-average potential argument appears VACUOUS at the relevant scale. Sketch: the ℓ¹-dist dual
potential φ automatically has ‖φ‖_∞ ≤ 1 (so the "Lip blowup" killer test is trivially green =
ill-posed); the repair identity makes the capped-convex potential φ̌ = max(φ−cap,0) a 4δ-submartingale
along the q-chain; quasi-stationary slop ‖mq−m‖₁ ~ 2/L times max φ̌ ~ τ is O(δ) — same order as the
hoped-for gain. The argument only re-derives the C1/C2 lifetime dichotomy. A τ-plateau (quasi-closed
bad block at φ-height ~τ, internal circulation, O(τ) exit) is NOT excluded by averages; only vertex/
exposedness geometry can kill it. Reframe: bad configuration ⟺ a 4δ-submartingale plateau with
Ω(1/τ) lifetime and no new (ρ,κ)-exposed vertex. Question: can an exact retraction support one?
- D0: codex xhigh cross-check of the vacuity analysis + ideation on what kills a plateau. KILL the
  original lane if vacuity confirmed; keep the plateau reformulation as the sharpened C14.
- D1 (numerics): adversarial search maximizing [bad-lifetime × plateau height] over exact retractions
  (the un-pursued C9e regret item). Counterexample-hunting and structure-revealing at once.
- Status: ACTIVE (D0 next). Kill criterion: vacuity confirmed AND plateau search finds nothing
  structurally new → fold remains into Lane E.

### Lane B — Baake–Sumner probabilistic (quantitative stability of the idempotent classification)
B–S/Högnäs–Mukherjea (refs/baake-sumner-2007.11433, byte-pinned): exact stochastic idempotents =
equal-input absorbing blocks + proportional transient rows. Equal-input = one-step-mixing; Q²≈Q =
"two steps ≈ one step". Plan:
- B1: within-class lemma — strong q-communication ⇒ ‖q_i−q_j‖₁ = O(√δ) (coupling/Dobrushin). Opus.
- B2: class detection at scale √δ (the hard core — approximate recurrent classes well-defined?).
- B3: transient-row proportionality. B4: assembly into B–S normal form (uses thm-cluster's m-free
  assembly). Kill criterion: B1 already needs a spectral floor.
- Status: QUEUED.

### Lane E — variational skeleton (repair of agent-B's stuck campaign)
Replace maximal 4ρ-separated skeleton by minimizer of Φ(R) = Σ_i dist₁(p_i, conv R) + λ·Σ_{v∈R}
(κ−e_v(ρ))₊. KKT multipliers at the minimizer should bound the C12 α-mass by construction; improving
swaps replace the maximality contradiction. Reuses banked C0–C10 machinery.
- E0 (numerics): KKT α-multipliers under variational selection on sampled bad instances (codex +
  gurobi). Kill: multipliers ~1/√δ on clean small-δ samples.
- E1: variational anchoring lemma. E2: splice into C0–C10 chain.
- Status: QUEUED.

### Lane G — ultraproduct hedge (qualitative-first)
One opus pass: draft the limit argument (counterexample sequence → exact positive affine retraction
on limit algebra → B–S rigidity) + name the idempotent-lifting lemma precisely. Then PARKED.
- Status: QUEUED (one-shot).

### Lane C — cohomological (commutative Layer-1)
Advances through the main-branch `prop-comm-scalar`/`cor-adjoint-benchmark` campaign anyway.
Slow-rolled here; escalate only if D/B/E all stall. Risks: error-reduction iteration unbuilt;
positivity-capable output (`op-layer1-gap`).
- Status: PARKED (dual-use with main campaign).

### Cross-cutting
- X1: byte-pin Priority-0 refs via TIB (Blackwell 1942, Schwarz 1964, Hoffman 1952,
  Choquet–Corson–Klee 1966, Straszewicz 1935) — sonnet, when a lane first needs one (lazy, L1).
- X2: bank agent-B C0–C10 contracts into canonical registry LAZILY via Recipe A→B on main.
- X3: two-scale conjecture (exposedness at √δ, hull-distance at O(δ)) — primary numerical target in D1.

---

## Delegation ledger (append-only)
| # | Date | Lane | Worker (model/effort) | Task | Verdict |
|---|---|---|---|---|---|

## Lane-switch log
- 2026-06-10: start. Lane D first (D0 cross-check of orchestrator's vacuity analysis).
