# w15_hmloci: byte-pin the Hognas-Mukherjea loci for the delta=0 anchor

You are a codex (gpt-5.5) provenance worker. The campaign's distilled document
(kernel-conjecture.tex) carries an anchor caveat in §5: the delta=0 classification
of idempotent stochastic matrices was cited from Baake-Sumner, who cite
Hognas-Mukherjea WITHOUT proof. The H-M book is now ingested. Pin the loci.
Repo root: /home/tobias/Projects/almost-idempotent-positive-maps (read-only task).

## SOURCE
refs/hognas-mukherjea-2011/hognas-mukherjea-2011.txt (pdftotext extraction, ~22k
lines). Provenance tier: extraction-level (quote against the .txt, noting it is not
the PDF bytes). A prior worker located: Theorem 2.2 (idempotent probability measure
structure) around lines 3969-3979 with proof 3982-4117; Theorem 1.11 (nonnegative
idempotent matrix basis) lines 2225-2244 with proof 3079-3210; Theorem 1.16
(stochastic specialization, recurrent blocks equal-input) lines 2767-2777; Rees
product lines 1021-1060. VERIFY these independently; do not trust them.

## TASK
1. Read agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex §5
   (the evidence/constraints ledger) and find the exact anchor item (the delta=0
   classification caveat — what statement the document says it needs pinned).
2. For EACH delta=0 anchor claim the document uses (the structure theorem for
   idempotent stochastic matrices: block/equal-input form, extremal idempotents,
   transient rows as mixtures of recurrent rows): produce
   - the claim as the document states it;
   - the EXACT verbatim quote from the .txt (copy the actual bytes — full
     sentences, enough to be uniquely greppable; verify your quote with grep -F
     against the file before reporting it);
   - the line range;
   - a one-line note on any mismatch between the document's phrasing and the
     source's actual statement (hypothesis drift = report it, do not paper over).
3. Check: does H-M's statement cover EXACTLY the finite stochastic-matrix case the
   campaign uses, or only via specialization from compact semigroups? If
   specialization is needed, identify the specialization steps and their loci too.
4. Draft the replacement text for the kernel-conjecture.tex §5 anchor item
   (LaTeX, ready to paste): citing H-M with the pinned loci, honest about the
   extraction-level tier.

## DELIVERABLE (verdict-first)
VERDICT: PINNED (all claims) / PARTIAL (which claim lacks a clean locus and why).
Then the claim->quote->lines table (quotes verbatim, grep-verified), the
specialization-gap note, and the §5 replacement LaTeX. Calibrated
P(every quote byte-matches under grep -F).
