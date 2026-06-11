# w24_freshread: fresh-agent readability test of OVERVIEW.md

You are a codex (gpt-5.5) worker simulating a FRESH AGENT with NO prior
knowledge of this project. Your job: read ONE document and report whether it
actually works as a self-contained onboarding map.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps (read-only).

## PROTOCOL (strict, two phases)
PHASE 1 — read ONLY agent-A/explorations/classical-portfolio/OVERVIEW.md.
Do not open any other file yet. Then answer, from the document alone:
 a. State the central conjecture precisely enough that you could explain it to
    a mathematician at a whiteboard (objects, quantifiers, the constant).
 b. What is already proved (with what caveats), what is pending, what is open?
 c. You are asked to attack the problem tomorrow: which 3 things would you do
    first, and which 5 things must you NOT do?
 d. List every term you could not fully resolve from the document alone
    (jargon leakage), every sentence you had to read twice (clarity debt),
    and every place you wanted a definition/number/pointer that was missing.
 e. Estimate: how many tokens of further reading does the document direct you
    to for (i) precise statements, (ii) the full record — and is the layering
    (this doc -> kernel-conjecture.tex -> dossier) clear?
PHASE 2 — now spot-check your Phase-1 answers against
report/kernel-conjecture.tex (same directory) ONLY. Report where the
document's plain-language rendering misled you (even slightly) about the
formal statement.

## DELIVERABLE (verdict-first)
VERDICT: WORKS AS ONBOARDING / WORKS WITH FIXES / FAILS (why). Then your
Phase-1 answers (a-e) verbatim, the Phase-2 mislead list, and a ranked list of
concrete edits (quote the sentence -> proposed replacement) that would most
improve a fresh agent's time-to-competence. Calibrated
P(a fresh agent relying on this document makes a wrong first move).
