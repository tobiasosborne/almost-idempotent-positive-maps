# Wave-14: the REAL Hognas-Mukherjea proof autopsy (the delta=0 anchor, at last)
You are a codex (gpt-5.5) analyst. The campaign's kernel (read
agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex — the complete
self-contained statement, Conjectures 1 and 2) needs a quantitative delta>0 version of the
classification of idempotent stochastic matrices. The actual proof is NOW AVAILABLE:
refs/hognas-mukherjea-2011/hognas-mukherjea-2011.txt (pdftotext of the book; ~22k lines).
PROGRESS PROTOCOL: short message per stage. Repo root:
/home/tobias/Projects/almost-idempotent-positive-maps.
## TASK
1. LOCATE the precise statements + proofs: the structure theorem for idempotent probability
   measures (around §2.2 "Invariant and Idempotent Probability Measures", grep the txt);
   specialize to FINITE semigroups / stochastic matrices (the completely-simple kernel,
   Rees product structure, equal-input/recurrent-block form). Quote loci (line numbers in
   the txt) for every step you use.
2. AUTOPSY the actual proof for the finite stochastic-matrix case: decompose into atomic
   steps; per step attempt the delta-perturbed analogue (entries >= -delta rowwise,
   ||P^2-P|| = 0 here! — note OUR P is EXACTLY idempotent, only POSITIVITY is perturbed:
   the right question is which steps use nonnegativity essentially vs only row-sums +
   idempotence) — this differs crucially from the generic almost-idempotent perturbation:
   exactness is free, signs are the perturbation. Verdict per step: SIGN-ROBUST (survives
   entries >= -delta with modulus you derive) / SIGN-RIGID (uses nonnegativity essentially
   — exhibit the failing step + the minimal repair hypothesis).
3. SYNTHESIS: does the H-M mechanism suggest the delta>0 surrogate for the Kernel
   Conjecture (kernel-conjecture.tex Conjecture 1)? Specifically: their kernel/minimal-
   ideal construction — what is its signed analogue, and does it attach to the proved
   component finisher (Conjecture 2's machinery)?
## Deliverable: VERDICT first (the step table: step | locus | sign-robust/sign-rigid |
modulus or repair), then the synthesis paragraph, then P(the H-M mechanism yields the
conjecture), P(your reading survives audit).
