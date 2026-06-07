# `agent-B/` — the exploration sandbox

**You are in the scratch lane.** This directory (`theory/`, `experiments/`, `notes/`) is where exploratory work
to *scope out how to land the full proof* lives. Nothing here is load-bearing or gated — explore freely, but
follow the rules of engagement so you don't damage the canonical, validated record.

> **READ FIRST:** [`docs/plans/2026-06-07-agent-b-rules-of-engagement.md`](../docs/plans/2026-06-07-agent-b-rules-of-engagement.md)
> — the full lane discipline. Then the read-order gate: `PRD.md` → `CLAUDE.md`(==`AGENTS.md`) → `HANDOFF.md` →
> `definitions/INDEX.md` → `argument/INDEX.md`.

## The five things that protect the 14 validated results

1. **Stay in the sandbox.** Write here, in `docs/plans/` (new dated docs), or append to `docs/worklog.md`.
   **Never edit** `definitions/`, `argument/`, `proofs/`, or `report/` directly — reach them only by *proposing*
   a registry shard through Recipe A → Recipe B → a reviewer who isn't you. Scoping ≠ committing.
2. **Never touch** a validated `proofs/<id>/` (re-refine archives validated children), a generated file
   (`*/INDEX.md`, `argument/DAG.md`, `report/figures/dag.pdf`), or a locked definition.
3. **No overclaim.** `(open)` stays `(open)` / `(conjecture)` until A+B af consensus. Never flip an `af:` or
   `status:` field. A status OVERCLAIM is the repo's #1 guarded failure. Read `docs/LEARNINGS.md` and `CLAUDE.md`
   §3 for the exact traps already fallen into.
4. **Ground truth = byte-match to local `refs/`.** Tag any from-memory fact `[UNGROUNDED — needs refs/]`.
   **Do not trust** the SUSPECT refs (`kaup-1984`, `chu-russo-1512.03347`) or the **phantom** notes
   `agent-B/notes/response-to-agent-a-v0.*` (predecessor hallucinations, not Agent A's positions).
5. **Work on a feature branch**, run `sh scripts/check-all.sh` before any commit, and let the linker
   (`scripts/argument.py`) — not optimism — arbitrate the canonical state.

**Best output:** not a half-proof in the canonical layers, but a *map* in `docs/plans/` — the lemmas needed to
land the proof, which reduce to grounded `refs/` loci, which are genuinely open and why, with proposed
one-line contracts. That feeds the pipeline without risking the validated work.
