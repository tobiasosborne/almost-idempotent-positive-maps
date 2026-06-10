# LLM-delegation learnings (classical-portfolio sidequest)

Meta-experiment: large-scale math research with LLM subagents. One entry per delegation
(or notable orchestrator observation). Durable lessons also go to `bd remember`.

Format: `- [date] [worker@effort] [task type] — what happened; lesson.`

## Entries

- 2026-06-10 [opus-4.8@default, one-shot strategist, distilled brief] — strategy generation:
  produced 5 genuinely distinct routes + sharp architectural critique of the stuck campaign
  (maximality = no optimality slack; C9 = measure-controls-rows category error). HIGH value.
  BUT two of its concrete constructions contain errors a careful reader catches: (i) Strategy 1's
  E = lim q^{k!} kills the near-1 modes it must keep (2-state counterexample: Q=[[1,0],[ε,1−ε]]);
  (ii) Strategy 3's killer test (Lip of optimal dual potential) is trivially green — the ℓ¹-dist
  dual is ‖φ‖_∞ ≤ 1 BY CONSTRAINT. Lesson: opus one-shot ideation = excellent breadth + critique;
  every concrete construction needs an independent derivation pass before resources are committed.
- 2026-06-10 [codex/gpt-5.5@xhigh, infra] — WEDGED-SOCKET failure mode: a wifi blip mid-run left
  codex retrying ("Reconnecting 2/5..4/5"), then it hung indefinitely on an ESTAB-but-dead TLS
  socket — no output, no exit, for ~25 min. Undetectable without event streaming. FIXES (now
  standard for all codex runs): (1) never `--ephemeral` on long runs (it kills `codex exec resume`);
  (2) always `--json` events to a file — "thinking" vs "stuck" must be observable; (3) a 10-second
  low-effort smoke test cleanly separates pipeline-health from run-health before relaunching.
  Also: kill+relaunch cost ≈ nothing (the wedged run generated almost no tokens).
- 2026-06-10 [codex/gpt-5.5, infra #2] — ROOT CAUSE of the wedges: "idle timeout waiting for
  websocket" — long silent xhigh reasoning ⇒ idle websocket ⇒ flaky network path drops it ⇒
  reconnect attempts can exhaust/hang. MITIGATIONS THAT WORK: (1) PROGRESS PROTOCOL — instruct the
  model to emit a short message after each deliverable; keeps the stream warm, makes stalls
  observable, AND checkpoints partial results server-side (the resumed thread retained the finished
  audit). (2) `codex exec resume <thread-id>` genuinely continues with full context — but exec-level
  flags (-C/-s/--json/-o) must come BEFORE the `resume` subcommand token, only --skip-git-repo-check
  etc. after. (3) Monitor + bounded watchdog + kill/resume loop = robust against arbitrary flakes.
- 2026-06-10 [codex/gpt-5.5@xhigh, D0 math] — second-family adversarial audit WORKS: codex verified
  the orchestrator's vacuity analysis step-by-step (ℓ¹-dual identification, truncation sign,
  bookkeeping orders) rather than deferring to it — exactly the independent-check value we wanted
  from a non-Claude family. Quality of partial output: high, precise, no hedging.
- 2026-06-10 [sonnet Explore x4, parallel summarization, async] — branch-corpus summarization:
  all four faithful and precise on first pass; the registry agent (37 tool uses) correctly
  distinguished proved/conjectured/numerical throughout. Lesson: sonnet Explore is the right
  tool for corpus distillation; give it explicit "keep proved/conjectured/numerical distinct"
  instructions and it complies.
- 2026-06-10 [day-1 meta, serial multi-model] — the alternating prover/verifier pattern ACROSS model
  families (opus proves → codex verifies → codex proposes → opus refutes → ...) caught an inverted
  inequality, an overclaim, two numerics artifacts, and one vacuous proof route in a single day —
  each catch by a DIFFERENT party than the author. Thread-resume on codex is the efficiency key
  (420k cached tokens by D6; each continuation costs only the new reasoning). Opus tool-workers
  self-debugged honestly (both red→green pins were their own initiative). Calibrated-probability
  asks ("P(true)? P(provable)?") produced usefully honest numbers from codex, not flattery.
- 2026-06-10 [process] — "progress message after each deliverable" doubles as wedge-detection AND
  server-side checkpointing for codex resume; now standard in every brief. Monitor harness with
  answer-file/process-death/stall detection made 6 long runs babysittable at near-zero attention.
