I audited [equal-fin.tex](/home/tobias/Projects/almost-idempotent-positive-maps/refs/baake-sumner-2007.11433/equal-fin.tex:1044) and the final campaign state in [wave5-sigma-wall-parallel.md](/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/notes/wave5-sigma-wall-parallel.md:445). Important source fact: Baake–Sumner state the idempotent classification as a reformulation of Högnäs–Mukherjea; the proof is not written out there, so this is an autopsy of the reconstructed exact proof.

Norm convention: `||·||` below is max row `l1`, and I write `δ_- = max_i sum_j max(-B_ij,0)`. If the only assumption is entrywise `B_ij >= -δ` on an `m`-column block, substitute `δ_- <= mδ`, which loses dimension-free control.

**Step Table**

| step | δ=0 content | verdict | modulus or obstruction |
|---|---|---|---|
| 1 | Idempotence gives row stationarity: each row `r_i M = r_i`. | PERTURBABLE | Let `L=1+η+2δ_-`. Normalizing the positive part of row `i` to a probability `p_i`, `||p_iB-p_i||_1 <= α := ε + (L+1)(η+2δ_-)`. |
| 2 | Support closure: if stationary `p` has `p_j>0`, row `j` cannot leave `supp p`. | PERTURBABLE, thresholded | If `p_j >= a` and `p(C) <= τ`, then positive leakage `B_{jC}` is `<= (τ+α+δ_-)/a`. Needs the mass floor `a`; no floor, no useful closure. |
| 3 | Finite descent to recurrent communicating classes `K_s`. | RIGID literal; CONDITIONAL surrogate | Classes are discontinuous. `[[1-t,t],[0,1]]` has defect `2t(1-t)` but changes the closed-class picture for every `t>0`. Stable surrogate must be leakage/spectral clusters, not graph communication. |
| 4 | Zero-column set `Z` records transient coordinates. | RIGID literal | A formerly zero column can receive mass `t` at cost `O(t)` in defect. Replace `Z` by columns/sets below a chosen mass/leakage threshold. |
| 5 | Exact closed block restriction is again Markov idempotent. | PERTURBABLE after a block is chosen | If `K` has row leakage `λ`, the restricted block has row-sum error `η+λ` and idempotence defect `<= ε+O(Lλ)`. |
| 6 | Positive closed idempotent block has equal rows. | CONDITIONAL, key jewel | With all entries `>= β>0`, column-max proof gives row diameter `<= (ε'+Lη')/β^2`, where `ε'=ε+O(Lλ+δ_-)`, `η'=η+λ`. Better: with Hilbert diameter `Δ`, `q=tanh(Δ/4)`, Birkhoff gives diameter `<= 2ε'/(1-q)`. |
| 7 | Rank `r` equals number of recurrent blocks. | RIGID unless spectral input supplied | Almost-idempotence allows eigenvalues near both `0` and `1`. Need a resolvent/spectral-cluster rule or a leakage-selected band cut. |
| 8 | Transient rows are proportional to recurrent block rows. | PERTURBABLE after steps 3/6 | If class rows in `K_s` are `γ`-close to representatives `π^s`, and row `i` has transient-column mass `ζ_i`, then `dist(row_i, sum_s a_{is}π^s) <= ε + Lγ + Lζ_i`. |
| 9 | Converse: a matrix with the B–S normal form is idempotent. | PERTURBABLE | Approximate normal form with closure `λ`, equal-input error `γ`, transient mass `ζ`, row-sum error `η` gives `||B²-B|| <= O(λ+γ+ζ+η+δ_-)`. |
| 10 | Exact theorem excludes shallow hidden webs at `δ=0`. | RIGID as an absolute statement | The campaign’s s5 certificate shows low-height all-shallow webs exist for `δ>0`; the stable theorem must be height-conditioned, not “no shallow webs”. |

**True Core**

The rigid core is minimal but real:

1. Stable class detection: replace communicating classes by a leakage/spectral/resolvent cluster decomposition.
2. Stable transient set: replace zero columns by thresholded low-return/low-column-mass coordinates.
3. Equal-input collapse without a global entry floor: needs either projective contraction, a support-graph alternative, or the band-cut closure lemma.
4. Height-conditioned web exclusion: low-height s5 webs must survive; only high shallow top-band webs should be ruled out.

**Sub-Lemmas Derived**

Row-normalization stationarity: `α = ε + (L+1)(η+2δ_-)`.

Threshold support closure: leakage `<= (τ+α+δ_-)/a`.

Interior equal-input forcing: row diameter `<= (ε'+Lη')/β²`.

Conditional projective finisher: diameter `<= 2ε'/(1-q)` with `q=tanh(Δ/4)`.

Transient proportionality stability: error `<= ε + Lγ + Lζ`.

Approximate-normal-form converse: defect linear in `λ+γ+ζ+η+δ_-`.

Probabilities: `P(quantitative B–S with polynomial modulus true) = 0.62` for the height-conditioned, cluster-surrogate version; lower if “literal communicating classes” is required. `P(audit survives review) = 0.78`, main risk being the reconstructed HM proof rather than a proof printed in Baake–Sumner.