# w24_factcheck: hostile fact-check of OVERVIEW.md against the repo record

You are a codex (gpt-5.5) HOSTILE FACT-CHECKER. A new onboarding document
claims to summarize the entire classical-portfolio campaign. Every factual
claim in it must match the archived record. Find every error, overstatement,
broken pointer, or stale status. The campaign's cardinal failure mode is a
confident, plausible, WRONG claim — in an onboarding document an error
poisons every future agent.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps (read-only).

## THE DOCUMENT UNDER AUDIT
agent-A/explorations/classical-portfolio/OVERVIEW.md

## THE RECORD (ground truth for the check)
- report/kernel-conjecture.tex (same dir) — the precise statements/ledger.
- notes/wave5-sigma-wall-parallel.md — the campaign dossier.
- notes/swarm-answers/*.md — worker verdicts (the document cites many by name:
  w12_comp_finisher, w14_autopsy, w15_audit, w15_hmloci, w15_prover,
  w15_clone_audit, w15_periodic(+_audit), w15_sos, w15_refuter, w16_quotient,
  w16_barrier, w16_cert_audit, w17_cert_audit, w18_quadlit, w18_sos_ideal,
  w18_similarity, w19_tangent(+_audit), w19_leftcone, w19_boundary, w20_curve,
  w20_t1_audit, w21_recode(+_audit), w21_second, w22_jet, w23_loj(+_audit
  possibly not yet archived — flag if absent).
- experiments/out/ — instance/certificate artifacts the document references.
- refs/hognas-mukherjea-2011/ — the cited classical theorem.

## TASKS
1. CLAIM-BY-CLAIM CHECK: every number (delta values, ratios, constants, counts
   like "67,000+", "(n,k)=(4,3)", corner constants tau* = 2-sqrt(3), the
   certified-instance numbers, "H/delta = 2.000000000013"), every status word
   (PROVED / audited / pending / FALSE / dead), and every attribution
   (which worker found what) — verify against the archived files. Quote the
   discrepancy precisely.
2. POINTER CHECK: every file path and bead id mentioned must exist (or be
   flagged as forward-looking, e.g. docs/codex-delegation.md may be created in
   the same commit — flag it as needs-creation if absent NOW).
3. DEFINITION CHECK: the plain-language definitions (delta, tau, visible/
   hidden, multiplicity-correct, H, sigma-tilde, H-M normal form, the corner
   scale) — do they match the formal definitions in kernel-conjecture.tex?
   Any subtle mismatch (e.g. H defined as max over ALL rows vs hidden rows;
   visibility's exact LP form; sigma-tilde's exact support condition) matters:
   report it even if "morally right".
4. OMISSION CHECK: is any load-bearing campaign fact MISSING that a future
   agent would be misled without? (e.g. statuses pending audit, the global
   gap, the lane discipline, the certified instances' above-corner caveat.)
5. OVERCLAIM SCAN: the document must not present the pending w23 assembly as
   proved, must not claim the global linear law, and must keep "(open)" things
   open. Flag any sentence a hostile reader could read as an overclaim.

## DELIVERABLE (verdict-first)
A numbered findings list: [SEVERITY: ERROR / OVERCLAIM / STALE / NIT] —
the OVERVIEW.md line/quote — the correction with its source pointer. Then an
overall verdict (publishable as-is / publishable after fixes / structurally
misleading) and calibrated P(no remaining factual errors after your fixes).
