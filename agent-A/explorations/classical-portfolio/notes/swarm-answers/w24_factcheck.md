# w24_factcheck — hostile fact-check of OVERVIEW.md: 15 findings, all applied (codex, 2026-06-11)

**Findings**

1. **[ERROR]** - [OVERVIEW.md:50](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/OVERVIEW.md:50): “linear functional … bounded by 1 on all rows, that attains strict maximum exactly at that row.”  
   Visibility is misstated. Formal exposedness uses affine `h` with `h(p_v)=0`, `0<=h(p_j)<=1`, and `h(p_j)>=κ` only for rows at `l1` distance at least `ρ`; nearby rows are exempt. It is not “strict maximum exactly at that row.” Source: [kernel-conjecture.tex:93](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex:93), [def-exposed.md:13](/home/tobias/Projects/almost-idempotent-positive-maps/definitions/def-exposed.md:13).

2. **[ERROR]** - [OVERVIEW.md:61](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/OVERVIEW.md:61): “positive mass … to other outsiders.”  
   `\tilde\sigma_v` includes all columns with `dist(p_j,C_W)>0`, including `j=v` when the row is outside and `P_vv>0`. The certified instances rely on this self coefficient. Source: [kernel-conjecture.tex:130](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex:130), [w9deep.md:18](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/swarm-answers/w9deep.md:18), [w17_cert_audit.md:4](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/swarm-answers/w17_cert_audit.md:4).

3. **[ERROR]** - [OVERVIEW.md:80](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/OVERVIEW.md:80): “Every such P is O(δ)-close to H-M normal form.”  
   False as a global W-free/full-distance target. The archived W-free target is `D_BS(P) <= C sqrt(ν(P))`; full-distance `O(δ)` is refuted by `ex-hume`. The observed linear law is for hidden height `H`, not full matrix distance. Source: [w105_wfree.md:26](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/swarm-answers/w105_wfree.md:26), [w11_wfree_audit.md:14](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/swarm-answers/w11_wfree_audit.md:14), [ex-hume.md:4](/home/tobias/Projects/almost-idempotent-positive-maps/argument/lemmas/ex-hume.md:4).

4. **[OVERCLAIM]** - [OVERVIEW.md:74](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/OVERVIEW.md:74): “Each link in that chain is proved; only the linear law is open.”  
   The kernel ledger says links are “proved or proved modulo recorded audits,” and `op-exposed-hull <= HLC` is explicitly `PROVED-mod-audit`. Correction: say “proved or proved-mod-audit/conditional.” Source: [kernel-conjecture.tex:46](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex:46), [STATUS-LEDGER.md:20](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/STATUS-LEDGER.md:20).

5. **[OVERCLAIM]** - [OVERVIEW.md:115](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/OVERVIEW.md:115): “Proved and independently audited … culminating in claimed assembly.”  
   The wording blurs audited pieces with the unaudited w23 assembly. `w23_loj` begins: pending audit, not proved until audited; dossier assigns only `P(J2 survives audit)=0.60`. Source: [w23_loj.md:1](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/swarm-answers/w23_loj.md:1), [wave5-sigma-wall-parallel.md:1468](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave5-sigma-wall-parallel.md:1468).

6. **[STALE]** - [OVERVIEW.md:119](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/OVERVIEW.md:119), [OVERVIEW.md:215](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/OVERVIEW.md:215): `notes/swarm-answers/w23_loj_audit.md`.  
   This file is absent. Since the text marks it pending/in flight, this is acceptable only as a forward pointer; it must be labeled “not yet archived” until created.

7. **[OVERCLAIM]** - [OVERVIEW.md:215](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/OVERVIEW.md:215): “FULL δ=0 locus … yields `H <= C_loc δ`.”  
   The archived claim is fixed-`n`, local-neighborhood, local H-M locus, audit pending; it explicitly does not prove a global small-δ law or dimension-free constant. Source: [experiments/out/w23_loj/proof.md:19](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/experiments/out/w23_loj/proof.md:19), [proof.md:405](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/experiments/out/w23_loj/proof.md:405).

8. **[ERROR]** - [OVERVIEW.md:167](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/OVERVIEW.md:167): “exact rational witnesses at every chain length.”  
   The recorded exact witnesses are for tested scalar-shadow lengths `L=2,3,4,5`; the scalar shadow is necessary but not an actual matrix counterexample. Source: [kernel-conjecture.tex:367](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex:367), [w15_sos.md:1](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/swarm-answers/w15_sos.md:1).

9. **[OVERCLAIM]** - [OVERVIEW.md:148](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/OVERVIEW.md:148): “component finisher. PROVED.”  
   Missing hypotheses: closed primitive positive component, positively closed shallow band, and radius threshold. Periodic closure is only for closed w12 positive components; the analytic band-closure caveat is not discharged. Source: [w12_comp_finisher.md:1](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/swarm-answers/w12_comp_finisher.md:1), [w15_audit.md:4](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/swarm-answers/w15_audit.md:4), [w15_periodic_audit.md:4](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/swarm-answers/w15_periodic_audit.md:4).

10. **[STALE]** - [OVERVIEW.md:103](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/OVERVIEW.md:103): `notes/swarm-answers/w*.md (~70 files)`.  
   Current archive count is 53 `w*.md` files, 85 markdown verdict files total. Use `notes/swarm-answers/*.md` or update the count.

11. **[NIT]** - [OVERVIEW.md:19](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/OVERVIEW.md:19): “~20 waves and ~100 delegated workers.”  
   The archive supports “~20 waves” and 85 markdown verdict files, not clearly “~100 workers.” Safer: “dozens of workers” or “85 archived verdict files.”

12. **[STALE]** - [OVERVIEW.md:106](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/OVERVIEW.md:106): `docs/codex-delegation.md`.  
   This exists at repo root, not under `agent-A/explorations/classical-portfolio/docs/`. Since nearby paths are classical-portfolio-relative, this pointer is ambiguous. Use repo-root `docs/codex-delegation.md` or `../../../docs/codex-delegation.md`.

13. **[STALE]** - [OVERVIEW.md:1](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/OVERVIEW.md:1), [OVERVIEW.md:241](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/OVERVIEW.md:241): “read this first.”  
   This conflicts with the project and sidequest read-order gates. The classical handoff says read `report/kernel-conjecture.tex` first; repo rules say start with `PRD.md`, `AGENTS.md`, `HANDOFF.md`, then indexes before math edits. Source: [HANDOFF.md:8](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/HANDOFF.md:8), [PRD.md:34](/home/tobias/Projects/almost-idempotent-positive-maps/PRD.md:34).

14. **[NIT]** - [OVERVIEW.md:36](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/OVERVIEW.md:36): H-M theorem summary.  
   H-M gives the block/proportional normal form; “visible/extreme row” is a campaign-derived consequence, not a literal H-M statement. Source: [w15_hmloci.md:4](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/swarm-answers/w15_hmloci.md:4), [kernel-conjecture.tex:415](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex:415).

15. **[NIT]** - [OVERVIEW.md:141](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/OVERVIEW.md:141): “Eight died … two produced lasting tools.”  
   The wave-10 ledger records all ten as died/collapsed, with five collapsing into the LP frame and t10 producing the Birkhoff finisher. The stated count is too clean. Source: [wave5-sigma-wall-parallel.md:703](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave5-sigma-wall-parallel.md:703).

**Checked And Matched**

The headline numeric claims I checked do match the record: `67,000+` instances, six campaigns, `(n,k)=(4,3)`, `τ*=2-sqrt(3)`, corner `δ*=(2-sqrt(3)^2`, above-corner caveat, w16/w17 certified-instance numbers, `H/δ = 2.000000000013`, `report/main.pdf` at 49 pages, `experiments/out/` present, `refs/hognas-mukherjea-2011/` present, and bead `aipm-3u6` exists.

**Verdict**

Not publishable as-is. The document is useful, but it is structurally dangerous as onboarding because it gets two formal definitions wrong, states a false global W-free `O(δ)` target, and softens pending-audit status around w23. Publishable after the fixes above.

Calibrated `P(no remaining factual errors after applying these fixes)`: **0.84**.