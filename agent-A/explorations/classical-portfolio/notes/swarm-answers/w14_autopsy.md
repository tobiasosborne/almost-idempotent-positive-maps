# w14_autopsy — the REAL Hognas-Mukherjea proof autopsy (codex, 2026-06-11)
# Brief: /tmp/codex-sigma-wall/w14_autopsy/brief.md (volatile; pattern in worklog 2026-06-11 cont.)

**VERDICT**

I read `delta` as row negative mass, matching [kernel-conjecture.tex](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/report/kernel-conjecture.tex:55). If it only means entrywise `P_ij >= -delta`, the dimension-free moduli below do not follow.

| step | locus | verdict | modulus / repair |
|---|---:|---|---|
| Idempotent probability measure structure: support is completely simple, `mu=mu1*Haar*mu3` | H-M `Theorem 2.2`, lines 3969-3979; proof 3982-4117 | SIGN-RIGID | Uses positivity of a probability measure. Signed analogue is not a signed Rees product; replace support by positive carrier components. |
| Rees product / finite kernel | Rees theorem lines 1021-1060; finite kernel lines 1089-1109 | SIGN-RIGID as perturbative tool | Algebra survives, but signed coefficients do not give a semigroup support. Repair: positive carrier graph plus path-product lower bound. |
| Exact row reproduction `p_i=sum_j P_ij p_j` | `P^2=P`; kernel setup lines 55-65, 81-82 | SIGN-ROBUST | `dist(p_i, conv{p_j:P_ij>0}) <= (2+4δ)ν_i <= (2+4δ)δ`. |
| Nonnegative idempotent matrix basis | H-M `Theorem 1.11`, lines 2225-2244; proof deferred to 3079-3210 | SIGN-RIGID | Exact basis uses zero/positive pattern. Signed replacement is visible vertices `W` and clusters. |
| Prove positive diagonal | lines 3104-3135 | SIGN-RIGID | Fails even for rank-one signed `P=1π` with `π_i<0`. Only trivial repair is exact nonnegativity or a new geometric vertex selection. |
| Zero-sum closure: `0=sum nonnegative terms => each term 0` | lines 3112-3114, 3141-3148, 2731-2742 | SIGN-RIGID | This is the main failure. Repair: a positive path product beating signed error, `Π_C > O(Lδ)+collapse threshold`. |
| Zero-pattern symmetry and block partition | lines 3136-3155, 3186-3188 | SIGN-RIGID | Cancellations destroy exact zero pattern. Repair by thresholded positive carrier SCCs. |
| Strictly positive idempotent block has rank 1 | lines 3157-3185 | SIGN-RIGID but quantitatively repairable | If component path-products give entry floor `θ_C`, w12 finisher gives row diameter `<= 2(1+δ)ε/θ_C+4δ`, `ε<=7δ+6δ²`. For `θ_C~√δ`, this is `O(√δ)`. |
| Stochastic specialization: recurrent blocks equal-input | H-M `Theorem 1.16`, lines 2767-2777 | SIGN-ROBUST after collapse | Exact proportional + row sum gives equal rows. Perturbed version attaches to near-equal-input cluster theorem. |
| Transient rows are proportional mixtures of recurrent rows | lines 2770-2777 plus ratio lines 2233-2240 | PARTLY RIGID | Small invisible mass branch is proved: height `<=2(1+2δ)max(σ̃_v,ν_v)`, hence `<=3√δ` when `σ̃_v<=√δ`. Large invisible mass is exactly Conjecture 1. |
| Component finisher | kernel-conjecture lines 242-259; w12 note | SIGN-ROBUST conditional | If positive SCC path products beat signed/idempotence error, Birkhoff-Hilbert collapse gives a near equal-input cluster, then exposure, contradiction to hiddenness. |
| Remaining missing step | kernel-conjecture lines 253-264; w13 note | OPEN | Need thin-chain exclusion / path-product floor `Π_C >= c√δ - C'Lδ`. H-M does not supply this; it identifies it. |

**Synthesis**

The H-M proof does not perturb directly. Its literal kernel/minimal-ideal/Rees support mechanism is positivity-rigid. The right signed analogue is: visible exposed vertices play the recurrent classes, hidden top vertices generate a shallow positive carrier graph, and a strongly connected positive component with enough path-product mass is the “approximate minimal ideal.” Once such a component has `Π_C` above signed error, the proved component finisher attaches cleanly and produces a near equal-input cluster, which then joins `W` and contradicts hiddenness. So H-M points to Conjecture 2 as the correct quantitative surrogate for Conjecture 1, but the new content is exactly the path-product floor / thin-chain exclusion.

`P(the H-M mechanism yields the conjecture) = 0.63`.

`P(this reading survives audit) = 0.86`.

No files changed. `bd ready` was blocked because the read-only filesystem prevented opening the embedded beads lock.