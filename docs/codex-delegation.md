# Delegating to GPT‑5.5 via Codex — Claude Code Cheatsheet

How to hand a self-contained sub-task to OpenAI's `codex` CLI (running `gpt-5.5`) from
inside a Claude Code session, and get a clean result back. Verified on this machine
2026‑06‑10 with codex `v0.139.0`.

## TL;DR

```bash
echo "<self-contained task>" | codex exec \
  --skip-git-repo-check \
  -C /abs/path/to/workdir \
  -s workspace-write \
  -o /abs/path/to/answer.txt -
# then: Read answer.txt  → the final message only
```

`codex exec` is the non-interactive entrypoint. Pipe the prompt on stdin, terminate the
arg list with `-`, and capture the final answer with `-o`.

## Environment (this machine)

| Thing | Value |
|---|---|
| Binary | `codex` (`@openai/codex` v0.139.0, nvm node 24) |
| Auth | ChatGPT login token in `~/.codex/auth.json` — **no API key, counts against the 5h/weekly ChatGPT limits** |
| Model | `gpt-5.5`, `model_reasoning_effort = "xhigh"` (`~/.codex/config.toml`) |
| Entry | `codex exec` (alias `codex e`) |

## Flags that matter for delegation

| Flag | Use |
|---|---|
| `-` (trailing) | read prompt from stdin; required when piping |
| `-o FILE` / `--output-last-message` | write **only** the final message to FILE — the clean capture path |
| `--json` | stream every event (tool calls, reasoning, commands) as JSONL — use when you need the trace, not just the answer |
| `--output-schema FILE` | force the final response to match a JSON Schema → machine-readable hand-back |
| `-s MODE` | sandbox: `read-only` \| `workspace-write` \| `danger-full-access` |
| `-C DIR` | working root |
| `--add-dir DIR` | extra writable dir |
| `--skip-git-repo-check` | allow running outside a git repo |
| `--ephemeral` | don't persist session files to `~/.codex/sessions` |
| `-m MODEL` | override model for one call |
| `-c key=value` | override any config value (TOML dotted path), e.g. `-c model_reasoning_effort=\"high\"` |

### Sandbox levels — pick the least powerful that works
- `read-only` — pure reasoning / reading files. Safest. Use for "prove / derive / check this".
- `workspace-write` — can run code and write files **in the workdir only**. Default for
  "write and run a test program". No network.
- `danger-full-access` — network + full FS. Only when the task genuinely needs e.g.
  `pip install` or external fetches. Avoid unless required.

## Recipes

### 1. Pure reasoning, answer to stdout
```bash
echo "Derive the first-order correction to the energy for H = p^2/2 + x^2/2 + λx^4. Show steps." \
  | codex exec --skip-git-repo-check -s read-only -
```

### 2. Write + run code, capture clean answer
```bash
mkdir -p /tmp/codex-task
echo "Write a Python script that diagonalizes the QHO Hamiltonian on a grid and prints the
ground-state energy and its error vs the exact 0.5. Run it and report the numbers." \
  | codex exec --skip-git-repo-check -C /tmp/codex-task -s workspace-write \
      -o /tmp/codex-task/answer.txt -
# Read /tmp/codex-task/answer.txt and the produced .py
```

### 3. Structured hand-back (best for programmatic integration)
```bash
cat > /tmp/codex-task/schema.json <<'JSON'
{
  "type": "object",
  "required": ["value", "abs_error", "method"],
  "properties": {
    "value":     {"type": "number"},
    "abs_error": {"type": "number"},
    "method":    {"type": "string"}
  },
  "additionalProperties": false
}
JSON
echo "Compute the QHO ground-state energy numerically. Return value, abs_error vs 0.5, and method." \
  | codex exec --skip-git-repo-check -C /tmp/codex-task -s workspace-write \
      --output-schema /tmp/codex-task/schema.json \
      -o /tmp/codex-task/answer.json -
# answer.json is valid against schema → parse with jq / json.load
```

### 4. Full trace for debugging what it did
```bash
echo "<task>" | codex exec --skip-git-repo-check -s workspace-write --json - \
  > /tmp/codex-task/events.jsonl 2> /tmp/codex-task/err.log
```

## Writing good delegated prompts

- **Self-contained.** Codex starts fresh — no Claude Code context. Inline all needed
  facts, file paths, and the exact success criterion ("the exact answer is 0.5; report the
  error").
- **Ask it to run, not just write.** "Write **and run** … and report the output" — otherwise
  you may get untested code.
- **State the return shape.** Either a schema (recipe 3) or an explicit "report X, Y, Z".
- **Scope to one workdir.** Put scratch in a temp dir and pass `-C`; keeps the sandbox tight
  and output easy to collect.

## Gotchas

- **stderr noise:** every run currently logs `failed to stat skills path .../cloudflare/...
  configuration.md` — a broken codex plugin reference. Harmless; ignore it, or run
  `codex doctor` to clean up. Always read the answer from `-o`, not from mixed stdout/stderr.
- **cwd resets** after `codex exec` returns; use absolute paths.
- **Usage limits:** delegated work burns the ChatGPT subscription quota, not a metered key.
- **No shared state:** each `exec` is independent. To continue a thread use
  `codex exec resume --last` (or `resume <session-id>`).

## When to delegate to codex vs. do it yourself

Good fits: an independent second-model cross-check of a derivation or numeric result;
a self-contained "write a test program and run it"; offloading a bounded reasoning task to
run in parallel while you continue. Two independent model families agreeing on a
mathematical-physics result is a real signal. Keep orchestration, integration, and final
judgment in Claude Code.
