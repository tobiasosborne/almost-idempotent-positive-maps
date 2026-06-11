# w15_audit: hostile derive-first audit of the w14 H-M autopsy

You are a codex (gpt-5.5) HOSTILE AUDITOR. A previous worker autopsied the
Hognas-Mukherjea proof of the idempotent-stochastic-matrix structure theorem and
produced a SIGN-ROBUST/SIGN-RIGID step table. Your job: try to BREAK its reading.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps (read-only).

## READ
1. agent-A/explorations/classical-portfolio/notes/swarm-answers/w14_autopsy.md
   (the autopsy under audit — its step table cites line loci).
2. refs/hognas-mukherjea-2011/hognas-mukherjea-2011.txt (the source; ~22k lines,
   pdftotext extraction).
3. agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex
   (the campaign's self-contained problem statement: all definitions, Conjectures 1+2,
   the conditional chain, the evidence/constraints ledger).

## TASK (derive-first: re-derive before you trust; check loci before you accept)
1. For EVERY row of the autopsy's step table: (a) open the cited line range in the
   .txt and confirm the cited statement/proof step is actually there and actually says
   what the autopsy claims; (b) re-derive the claimed modulus or failure independently.
   In particular re-derive: the SIGN-ROBUST exact-row-reproduction modulus
   dist(p_i, conv{p_j : P_ij > 0}) <= (2+4*delta)*nu_i <= (2+4*delta)*delta,
   the rank-one-block repair modulus (row diameter <= 2(1+delta)*eps/theta_C + 4*delta
   with eps <= 7*delta + 6*delta^2), and the transient-row small-invisible-mass branch
   (height <= 2(1+2*delta)*max(sigma_tilde_v, nu_v)).
2. Attack the SYNTHESIS: "visible exposed vertices = recurrent classes, positive
   carrier SCC with path-product mass = approximate minimal ideal, component finisher
   attaches once Pi_C beats signed error". Is this attachment actually licensed by the
   proved component finisher's hypotheses (read
   notes/swarm-answers/w12_comp_finisher.md)? Name any hypothesis mismatch precisely.
3. The autopsy read delta as ROW negative mass and warned the moduli fail for the
   entrywise reading. Check kernel-conjecture.tex: which reading is the campaign's
   actual convention? Is the autopsy's caveat live or moot?

## DELIVERABLE (verdict-first)
Per step-table row: CONFIRMED / CORRECTED (state the fix in display math) /
REFUTED (exhibit the failure). Then an overall verdict paragraph, then calibrated
P(autopsy reading survives) and P(the signed-surrogate frame is the right next attack).
Any inequality you derive or refute: display math. Do not soften; finding errors is success.
