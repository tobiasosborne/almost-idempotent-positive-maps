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
- 2026-06-10 [sonnet Explore x4, parallel summarization, async] — branch-corpus summarization:
  all four faithful and precise on first pass; the registry agent (37 tool uses) correctly
  distinguished proved/conjectured/numerical throughout. Lesson: sonnet Explore is the right
  tool for corpus distillation; give it explicit "keep proved/conjectured/numerical distinct"
  instructions and it complies.
