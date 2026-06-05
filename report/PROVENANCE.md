# PROVENANCE — report audit ledger

**Policy.** Every Definition and Theorem in the report (`sections/*.tex`), and every labelled Lemma/Proposition/Remark that carries a status flag, must have an entry here. An entry records: (1) the report label; (2) the ground-truth source file (path + SHA256, truncated to 16 hex); (3) the source locus or internal proof locus that the report statement is matched to; (4) any harmonisation (notation change) applied. "Provenanced" = the statement is a faithful transcription/derivation of registered source material, with notation harmonised per the table below, or an internal project statement tied to a hashed proof/consensus file. Results that are *original to this project* (no external source) are marked `ORIGINAL` and point to the internal working file that proves or motivates them.

Verify a hash with: `sha256sum "<path>" | cut -c1-16`.

## Ground-truth source registry

| Key | Path | SHA256 (16) | What it is |
|-----|------|-------------|------------|
| `HOS` | `/home/tobias/Projects/af-tests/examples3/Jordan Operator Algebras/joa-m/joa-m.md` | `28740e73d547dd46` | Hanche-Olsen & Størmer, *Jordan Operator Algebras* (Pitman 1984), OCR→markdown. Ground truth for Jordan/JB-algebra definitions. |
| `IDEL` | `/home/tobias/Projects/af-tests/examples3/Idel - 2013 - On the structure of positive maps/Idel - 2013 - On the structure of positive maps.md` | `737cd6d3d82ae588` | Idel, *On the structure of positive maps* (2013), OCR→markdown. Positive maps, fixed points, conditional expectations. |
| `KIT` | `agent-A/refs/kitaev-src/approximate_algebras.tex` | `e7eb512a2ec2438d` | Kitaev, *Almost-idempotent quantum channels and approximate C\*-algebras* (arXiv:2405.02434), TeX source. The result we generalise. |
| `VLW` | `agent-A/refs/vlw-src/paper.tex` | `3395946df12f6606` | van Luijk & Wilming, *Sufficiency and Petz recovery for positive maps* (arXiv:2604.08380), TeX source. The positive-map/Jordan setting. |
| `ES-P01` | `agent-B/references/effros-stormer-1979/ocr-pages/page-01.txt` | `b5594fe97fdafae1` | Effros & Størmer OCR page 127. Introduction and fixed-point consequence preview. |
| `ES-P02` | `agent-B/references/effros-stormer-1979/ocr-pages/page-02.txt` | `5d8290904cbbef07` | Effros & Størmer OCR page 128. Lemma 1.1 locus. |
| `ES-P05` | `agent-B/references/effros-stormer-1979/ocr-pages/page-05.txt` | `80ae5aacf9ce018c` | Effros & Størmer OCR page 131. Theorem 1.4 locus. |
| `ES-P06` | `agent-B/references/effros-stormer-1979/ocr-pages/page-06.txt` | `687a8024feb5ceac` | Effros & Størmer OCR page 132. Corollaries 1.5--1.6 locus. |
| `CHU` | `agent-A/refs/lit/chu-russo-1512.03347.pdf` | `8597dc5556996e83` | Chu & Russo, *Cohomology of Jordan triples and Lie algebras* (arXiv:1512.03347). Whitehead lemmas / Jordan cohomology. |
| `BRIDGE` | `agent-B/theory/theorem-B-algebraic-bridge.md` | `e2f6d7dc1f85ea50` | INTERNAL. Agent B's proof of the Layer-2 bridge theorem; verified line-by-line by Agent A (agent-a-findings v0.5 §10). Source for §6 derivation. |
| `A-FIND` | `agent-a-findings` | `22c97155f2622acb` | INTERNAL. Agent A consensus/status file (through v0.13; §16–§18 cover the faithful-invariant-state sidequest and Layer-1 re-audit). |
| `A-INGEST` | `agent-A/notes/ingestion-results-2026-06-01.json` | `972bba533931fd3d` | INTERNAL EXTRACTION. Agent A local extraction of Kitaev/VLW and Jordan-background literature. |
| `A-ER` | `agent-A/theory/01-error-reduction.md` | `72f1492a724f21a` | INTERNAL. Agent A error-reduction programme note. |
| `A-JCOB` | `agent-A/experiments/jordan-coboundary/REPORT.md` | `7c456f26a8787be0` | INTERNAL. Agent A numerical Jordan-coboundary report. |
| `B-ROUND` | `agent-B/notes/factorization-positivity-rounding.md` | `42c922ebef1d7516` | INTERNAL. Agent B positivity-rounding obstruction note. |
| `A-FIT` | `agent-A/experiments/faithful-invariant-transfer/REPORT.md` | `d1fedfe04ee973f6` | INTERNAL. Agent A faithful-invariant-state transfer report: exact statement, $O(\eta/\lambda)$ bound, numerics (`hole_scaling.py`, `crossover.py`). Source for §\ref{sec:faithful}. |
| `B-FIT` | `agent-B/notes/faithful-invariant-ambient-product-sidequest.md` | `1fc34fa7d72f8100` | INTERNAL. Agent B faithful-invariant-state sidequest note: the $T_a$ counterexample and the conditional $O(\eta/\mu)$ bound (B's $\mu$ = $\lambda$). |
| `TS3` | `agent-B/notes/theorem-stack-v0.3.md` | `639a9182e2617423` | INTERNAL. Agent B canonical theorem-stack v0.3: Layer-1/2A/2B/decomposable formulations and status taxonomy. |
| `TH-C` | `agent-B/theory/theorem-C-conditional-factorization.md` | `ebdd0c1190a10824` | INTERNAL. Agent B conditional exact UP factorization (Theorem~C): proof from near-positive projection stability, real$\to$complex Effros--Størmer, cone compatibility. Source for §\ref{sec:factorization}. |
| `B-NPPS` | `agent-B/notes/near-positive-projection-stability-program.md` | `ea285ccae975124d` | INTERNAL. Agent B near-positive projection-stability program: sharp target, Markov reduction, proved special cases. Source for §\ref{sec:factorization},§\ref{sec:classical}. |
| `B-ROUND` (spin CE) | `agent-B/notes/subagent-positivity-rounding.md` | `45d7f0afddcd6701` | INTERNAL. Agent B positivity-rounding spin-factor counterexample (companion to `B-ROUND`). |
| `CL-FAC` | `agent-B/theory/classical-cluster-factorization-theorem.md` | `44d43c1237aaf07c` | INTERNAL. Agent B exact commutative factorization under cluster geometry. Source for §\ref{sec:classical}. |
| `B-SIMP` | `agent-B/notes/simplex-classical-stability.md` | `3f84774a0f8c712a` | INTERNAL. Agent B simplex (and line-segment) classical stability, vertex-count-free constant. |
| `B-CLUS` | `agent-B/notes/cluster-representative-classical-stability.md` | `6bdb540fbb37e2cb` | INTERNAL. Agent B cluster-representative classical stability. |
| `B-EXC` | `agent-B/notes/exposed-circuit-cancellation.md` | `5b7969b9dcb7bd97` | INTERNAL. Agent B exposed-vertex concentration and circuit-cancellation lemma. |
| `B-ADJ` | `agent-B/notes/finite-dimensional-adjoint-jb-splitting-corollary.md` | `0e8e9e261a6635a8` | INTERNAL. Agent B master exact-adjoint splitting corollary (universal constant for all finite-dim JB). Source for §\ref{sec:programme}. |
| `B-MATADJ` | `agent-B/notes/matrix-factor-exact-adjoint-splitting-theorem.md` | `46420354400b16d5` | INTERNAL. Agent B high-rank matrix-factor exact-adjoint splitting (diagonal gauge, leakage globalization, sector reconstruction). |
| `B-SPINADJ` | `agent-B/notes/adjoint-spin-splitting-theorem.md` | `442194d9d0100a8a` | INTERNAL. Agent B spin-factor exact-adjoint splitting (order-unit constant $4\sqrt2$). |
| `A-SPIN` | `agent-A/theory/02-spin-splitting.md` | `57f23abbbe80cb74` | INTERNAL. Agent A rank-obstruction ($\sqrt{\mathrm{rank}}$) analysis and spin reduction (independent confirmation of `B-SPINADJ`). |
| `B-DNEXT` | `agent-B/notes/diagonal-frame-matrix-next-arrow-walsh-target.md` | `f592f7011d354f38` | INTERNAL. Agent B fixed diagonal-frame matrix next-arrow theorem. |
| `B-FMNEXT` | `agent-B/notes/full-matrix-next-arrow-source-decomposition-target.md` | `b8d1842a16590dc0` | INTERNAL. Agent B full matrix next-arrow source-decomposition target and remaining mixed-sector obligations. |
| `B-NEWTON` | `agent-B/notes/next-arrow-to-newton-error-reduction.md` | `b725a5cec7c49916` | INTERNAL. Agent B next-arrow/Newton framework and linearized Jordan defect conventions. |
| `B-DEC` | `agent-B/notes/decomposable-alpha1-route.md` | `d7b2ae0dfebc3355` | INTERNAL. Agent B decomposable $O(\eta)$ route, norm correction, doubling/Sartre obstructions. |
| `B-DECDIL` | `agent-B/notes/decomposable-dilation-compatible-theorem.md` | `c39ae649be1e9b0a` | INTERNAL. Agent B dilation-compatible $O(\eta)$ bridge (conditional, by reduction to Kitaev). |
| `B-NULL` | `agent-B/experiments/null-ideal-probe/REPORT.md` | `0d10b458a5424d52` | INTERNAL. Agent B null-ideal numerical probe: $32/27$ asymptotics, qubit triviality. |

## Notation harmonisation (source → report)

| Concept | report | HOS | KIT | VLW |
|---|---|---|---|---|
| Jordan product | `a∘b` | `a∘b = ½(ab+ba)` | `½(XY+YX)` | `{a,b}=½(ab+ba)` |
| Jordan identity | `(a∘a)∘(b∘a)=((a∘a)∘b)∘a` | `a∘(b∘a²)=(a∘b)∘a²` (eq. 2.30) | — | — |
| unit | `𝟏` | `1` | `I` | `𝟙` |
| spectral idempotent | `P=θ(2Φ−𝟏)` | — | `Φ̃=θ(2Φ−1)` (KIT eq. tilde_Phi) | `θ(2Φ−I)` |

## Per-claim ledger

Status column: **V** = statement byte-verified against the registered local source by fixed-string search or direct line inspection; **I** = inline-provenanced (source+location recorded in the section's `% PROV:` comment), awaiting independent byte-check; **O** = ORIGINAL/internal project result tied to a hashed internal file; **OPEN** = project target/conjectural programme statement, not a proved theorem; **EXTRACT** = supported by a hashed local extraction file but not yet independently byte-matched against primary text; **PDF** = source is a PDF not yet text-verified. Each section file also carries the full `% PROV:` comment above the statement where practical.

| Report label | Source | Loc. | Status | Note |
|---|---|---|---|---|
| def:operators | IDEL / HOS | IDEL 333; HOS 374 | **V** | IDEL L333 self-adjoint positive semidefinite order; HOS L374 positive functionals with $\rho(e)=1$ form the state space |
| def:positive-map | IDEL | 347–348 | **V** | IDEL L347--348 define positive and unital maps; order-unit norm contraction is proved inline |
| def:order-unit | HOS | 366–372 (§1.2.1) | **V** | HOS L366–372 order unit + Archimedean + order-unit norm; specialised to $e=\Id$ on $\Bsa$ |
| rem:order-unit-justification | HOS / elementary | HOS 366–372; spectral theorem | O | elementary verification that $\Bsa$ with unit $\Id$ satisfies the order-unit definition and that the order-unit norm is the operator norm |
| prop:kadison-js | Kadison1952 / VLW | VLW 555–560 (lem:JS-inequality) | **V** | VLW L555--560 record Jordan-Schwarz; Kadison $\Phi(a)^2\le\Phi(a^2)$ is the self-adjoint case |
| rem:cb-norm | ORIGINAL | agent-a-findings:20,191; Agent B correction in §2 | O | framing: positivity is not stable under amplification; in finite dimension the issue is not lack of cb-boundedness |
| def:jordan-algebra | HOS | 812 (eq 2.17); 963–967 (2.4.1) | **V** | HOS L963--967 define Jordan algebra by commutativity and the Jordan identity |
| rem:jordan-identity-form | HOS | 965–967 (eq 2.30) | **V** | (2.30) $a\jp(b\jp a^2)=(a\jp b)\jp a^2$ = JB4 form via commutativity |
| prop:power-associative | HOS | 1013–1025 (2.4.4–2.4.5) | **V** | HOS L1013 one-generator subalgebra associative; L1015–1017 Lemma 2.4.5 with $a^{m+n}=a^m\jp a^n$ |
| def:jb-algebra | HOS | 2308–2316 (3.1.3–3.1.4) | **V** | HOS L2308--2316 define Jordan Banach algebra and the two JB norm axioms |
| thm:jnw-classification | HOS / JvNW1934 | 2254 (2.9.6), 2264, 2270, 2293 | **V** | HOS L2254 gives direct-sum decomposition plus the $n=1$ and $n\ge3$ cases; L2264 gives spin factors |
| rem:exceptional | HOS | 2254, 1856 (2.8.5), 2306 | **V** | spin factors (2.9.7); $H_3(\mathbb O)$ exceptional (2.8.5), not a JC algebra (L2306) |
| def:spectral-idempotent | KIT | 2171–2182 (tilde_Phi); 524–533 | **V** | KIT L2171–2182 gives $\widetilde\Phi=\theta(2\Phi-1)$, idempotence, unit, closeness, and dagger preservation in the complex setting; report restricts to $\Bsa$ |
| lem:P-properties | BRIDGE (cites KIT) | bridge md:63–119 | O | worked bounds ($\lVert R-\Id\rVert\le C\eta$, $\delta$-positivity); construction cited Kitaev2024 |
| rem:kitaev-spectral-comparison | KIT / BRIDGE | KIT 2171–2182; BRIDGE md:63–119 | O | comparison between Kitaev's cb/UCP spectral idempotent and the report's order-norm positive-map adaptation |
| def:eps-jb | ORIGINAL (consensus) | A-FIND §5; BRIDGE md:36–50 | O | order-unit $\eps$-JB axioms JB1–JB4; A & B agree |
| rem:eps-jb-degeneration | ORIGINAL | A-FIND §5; KIT 407–438 | O | $\eps=0$ degeneration; contrast with Kitaev's approximate-norm $\eps$-C* |
| def:eps-jb-iso | ORIGINAL (consensus) | A-FIND §5; KIT 443–456; Agent B correction in §5 | O | $\delta$-Jordan-hom / $\delta$-iso; algebraic/normed Jordan transcription of Kitaev's notion, not an order-isomorphism unless order preservation is added |
| thm:bridge | BRIDGE | bridge md:7–50 | O | the bridge theorem; A-verified line-by-line (agent-a-findings v0.5 §10) |
| lem:bridge-orderunit | BRIDGE | bridge md:121–152 | O | exact order-unit structure of $A=\Img P$ |
| lem:bridge-easy | BRIDGE | bridge md:188–218 | O | unit/comm. exact; product bound; square positivity & norm lower bound |
| lem:bridge-fi | BRIDGE | bridge md:220–299 | O | first insertion (FI): almost-contraction + almost-orthogonality |
| lem:bridge-squarehole | BRIDGE | bridge md:301–372 | O | square holes almost null: (3.1)–(3.3) |
| lem:bridge-polar | BRIDGE | bridge md:374–451 | O | polarized holes: (HH) two-hole $O(\eta)$, (HZ) one-hole $O(\sqrt\eta)$ |
| lem:bridge-onehole | BRIDGE | bridge md:453–487 | O | one-hole contexts (5.1),(5.2) |
| prop:bridge-jordan | BRIDGE | bridge md:489–597 | O | Jordan-identity assembly (L),(R), exact ambient identity, $O(\sqrt\eta)$ bound |
| op:jordan-structure | KIT (model) / ORIGINAL | KIT 460–462; A-FIND §11; B-NEWTON | OPEN | open Jordan analogue; KIT L461 is the verified model statement, harmonized in report prose; cochain/linearized-defect notation follows B-NEWTON |
| thm:whitehead | CHU / A-INGEST | A-INGEST "jordan-stability-cohomology" | EXTRACT / PDF | $H^1{=}H^2{=}0$ (Whitehead lemmas); CHU primary is local PDF, but report statement currently comes through hashed extraction |
| prop:aut-compact | A-INGEST | "Aut(J) is compact" extraction block | EXTRACT | $\Aut(J)$ compact for Euclidean $J$; Faraut--Koranyi primary text not locally extracted in this repo |
| op:layer1-gap | TS3 / A-ER / B-FMNEXT | TS3 (status taxonomy); A-ER §3; `agent-B/notes/layer1-after-adjoint-benchmark-obligations.md`; B-FMNEXT | OPEN | what separates the exact-adjoint benchmark from \Cref{op:jordan-structure}: pre-cohomological frame/Peirce/coordinatization construction, arbitrary modules, approximate cocycles, approximate-module errors, incremental assembly, and positivity-capable output |
| rem:exponent | ORIGINAL / KIT | A-FIND §9–10; KIT 2643–2673; Agent B exponent correction note | O | $\sqrt\eta$ general; $\eta$ in UCP/cb or compatible dilation settings; decomposable case open |
| prop:faithful-exact | VLW / A-FIT | VLW 600–610 (`prop:fixpoint`); A-FIT §1 | I | **not original**: consequence of the VLW faithful fixed-point / multiplicative-domain theory (`prop:fixpoint`); the range lies in the multiplicative domain and is closed under ambient $\jp$. Report supplies a self-contained self-adjoint Kadison proof inline. (Flag I per Agent B review 2026-06-04.) |
| ex:no-faithful | A-FIT | A-FIT §1 (8/9 witness) | O | exact positive idempotent $P_0$ without faithful invariant state; ambient hole $8/9$; hand- and numerically verified. Invariant set is the whole face $(t,1-t,0)$, $0\le t\le1$ (none faithful: state 3 transient) — report corrects A-FIT's stale "unique invariant state $(1,0,0)$" wording, per Agent B review 2026-06-04. |
| thm:faithful-approx | A-FIT / BRIDGE | A-FIT §2; reuses lem:bridge-squarehole | O | $\norm{h_{a,b}}\le C(\eta/\lambda)\norm a\norm b$; quantifies prop:faithful-exact via square-hole positivity + faithfulness operator-norm upgrade. **Scope split (Agent B review 2026-06-04):** the *exact*-invariance subcase ($\omega\circ\Phimap=\omega$) is Agent B's (B-FIT); the report/A-FIT theorem is the *approximate*-invariance extension ($\norm{\omega\circ\Phimap-\omega}\le\eta$), independently re-derived to the identical bound by both authors. |
| prop:faithful-counterexample | B-FIT / A-FIT | B-FIT ($T_a$ family); A-FIT §3 (independent verification) | O | faithful $\forall a>0$, $\eta_a\to0$, ambient hole $\to2/9$; $\lambda=a/3=\Theta(\eta)$; projector $P_a$ matches Riesz projector to machine precision |
| rem:faithful-scope | A-FIT / A-FIND | A-FIT §4; A-FIND §16–§17 (overclaim/withdrawal) | O | conditional $\lambda=\Omega(1)\Rightarrow O(\eta)$ defect; narrow, dimension-dependent; A overclaimed (v0.10), withdrew after B's counterexample (v0.11) |
| thm:effros-stormer | ES-P05 / ES-P06 / ES-P02 | P05 L9–16; P06 L42–44; P02 L33–38 | **V** | positive unital projection $\Rightarrow$ $P(A)$ a JC-algebra under $P(r\jp s)$; fixed-point JW corollary; Lemma 1.1 proof input |
| rem:bridge-exact | ES-P05 / ES-P06 | P05 L9–16; P06 L42–44 | **V** | exact $\eta=0$ positive-projection endpoint underlying the bridge theorem |
| prop:rounding-fails | B-ROUND | B-ROUND §§2–4; `agent-B/notes/subagent-positivity-rounding.md` | O | generic $O(\eps)$ positivity-rounding FALSE; spin-factor target, $\eps$-positive map at distance $\ge\sqrt\eps$ from all positive unital maps; Rademacher lower bound |
%% --- rows added 2026-06-05: exact factorization (sec:factorization) ---
| rem:P-not-positive | TS3 | `agent-B/notes/compaction-checkpoint.md` (Counterexample Boundary) | O | classical $\R^4$ family with $\Phimap$ positive unital almost-idempotent but $\theta(2\Phimap-\Id)$ not positive |
| def:spin-cone | HOS | HOS 2264 (2.9.7) | I | spin-factor cone $\{s\ge\norm v_2\}$ and order-unit norm $\lvert s\rvert+\norm v_2$; computed inline |
| op:npps | TS3 / B-NPPS | TS3 (Theorem 3 hypothesis); B-NPPS | OPEN | near-positive projection stability at sharp scale $\sqrt\delta$; dimension-free; open |
| thm:factorization | TH-C | TH-C (full proof) | O | conditional exact UP factorization; $\Delta=$ incl, $\Upsilon=E$; $\norm{\Delta\Upsilon-\Phimap}\le C\sqrt\eta$; proved \emph{conditional} on \Cref{op:npps} |
| rem:layer1-route | TS3 | TS3; `agent-B/notes/layer1-output-requirements.md` | OPEN | alternative route via a positivity-capable Layer-1 output; not yet formalised |
%% --- rows added 2026-06-05: commutative stability (sec:classical) ---
| def:stochastic | B-NPPS | `agent-B/notes/markov-affine-retraction-formulation.md` | O/consensus | row-stochastic map, stochastic idempotent, signed affine retraction, negative mass, row polytope |
| op:classical | TS3 / B-NPPS | TS3 (Theorem 3 commutative reduction); `agent-B/notes/stochastic-stoquastic-special-cases.md` | OPEN | classical projection stability $\le C\sqrt\eta$; open; sharp exponent |
| lem:classical-equiv | B-NPPS | `agent-B/notes/subagent-classical-sqrt-stability-proof.md`; `agent-B/notes/classical-affine-face-lemmas.md` (Lemma 3) | O | equivalence of signed-idempotent and stochastic formulations with explicit constants |
| ex:hume | B-NPPS | `agent-B/notes/rank-one-classical-stability.md`; experiment `agent-B/experiments/classical-projection-stability/explicit_sqrt_family` | O | explicit $3\times3$ family, distance $2\sqrt\delta+O(\delta)$; $\sqrt{}$ exponent sharp |
| lem:leakage | B-EXC | `agent-B/notes/classical-affine-face-lemmas.md` (Lemma 1, Cor 2) | O | affine-face leakage at $\sqrt{}$ scale |
| def:exposed | B-EXC | `agent-B/notes/exposed-redundant-dichotomy-target.md` | O/consensus | exposed vertex; exposedness modulus $e_v(\rho)$ |
| lem:exposed-circuit | B-EXC | B-EXC (concentration + circuit cancellation) | O | exposed-vertex concentration and $\ell^1$ circuit cancellation, dimension-free |
| thm:rank-one | B-NPPS | `agent-B/notes/rank-one-classical-stability.md` | O | rank-one signed retractions $O(\sqrt\delta)$-stable (contains Hume) |
| thm:simplex | B-SIMP | B-SIMP; `agent-B/notes/line-segment-classical-stability.md` | O | line-segment and simplex stability, constant independent of vertex count |
| thm:well-exposed | B-EXC | `agent-B/notes/well-exposed-classical-stability.md` | O | well-exposed separated vertices $\Rightarrow$ simplex $\Rightarrow$ stable |
| thm:cluster | B-CLUS | B-CLUS | O | cluster-representative stability, no accumulation over representatives |
| thm:classical-factorization | CL-FAC | CL-FAC (incl.\ global exposed-hull corollary) | O | exact commutative UP factorization under cluster geometry hypothesis |
| prop:approx-simplex | B-NPPS | `agent-B/notes/approximate-simplexity-reduction.md`; `agent-B/notes/robust-approximate-simplexity-reduction.md` | O | reduces \Cref{op:classical} to $O(\sqrt\delta)$ approximate simplex coordinates with $O(\delta)$ coeff.\ negative mass |
| prop:parallelogram | B-NPPS | `agent-B/notes/parallelogram-classical-stability.md` | O | bounded binary-coordinate dependencies impossible at small $\delta$ ($m\sqrt\delta$ bound) |
| op:exposed-hull | B-NPPS | `agent-B/notes/simultaneous-skeleton-reduction.md`; `agent-B/notes/exposed-redundant-dichotomy-target.md` | OPEN | global exposed-hull lemma; the remaining classical obstruction |
| rem:regular-polygon | B-NPPS | `agent-B/notes/simultaneous-skeleton-reduction.md` (warning); `agent-B/notes/regular-polygon-retraction-obstruction.md` | O | dense regular polygons not realisable as small-defect retractions (vertex neg.\ mass $\ge\sqrt3/\pi-1/3$); pointwise dichotomy insufficient |
%% --- rows added 2026-06-05: abstract structure theorem (sec:programme) ---
| prop:rank-gap | A-SPIN / TS3 | A-SPIN §1; `agent-B/notes/cochain-norm-conversion-caveat.md` | O | order-vs-Frobenius gap on a rank-$r$ simple factor is exactly $\sqrt r$ (sharp at $\Id$) |
| rem:cochain-caveats | TS3 | `agent-B/notes/cochain-norm-conversion-caveat.md`; `agent-B/notes/nuclear-rank-one-route-caveat.md` | O | order-bounded coboundary can force $\sqrt n$ Frobenius primitive; nuclear route loses dimension |
| prop:spin-splitting | B-SPINADJ / A-SPIN | B-SPINADJ; `agent-B/notes/spin-normalized-cocycle-projection-reduction.md`; A-SPIN §2 | O | spin exact-adjoint splitting, order-unit constant $4\sqrt2$, dimension-free; next-arrow estimate |
| prop:direct-sum | B-ADJ | `agent-B/notes/adjoint-direct-sum-reduction.md`; `agent-B/notes/spin-direct-sum-adjoint-corollary.md` | O | direct-sum reduction, constant $\max_r K_r+1$, summand-count-free (adjoint/block-respecting) |
| rem:directsum-scope | TS3 | `agent-B/notes/response-to-agent-a-v0.12-layer1-caveat.md` | O | summand-count independence only for block-respecting modules; mixed Peirce-$\tfrac12$ caveat |
| prop:comm-scalar | B-ADJ | `agent-B/notes/commutative-scalar-module-splitting.md`; `agent-B/notes/commutative-scalar-cocycle-projection-theorem.md` | O | commutative scalar modules: norm-one splitting, projection $\le3$, next-arrow $\le12$ |
| thm:matrix-splitting | B-MATADJ | B-MATADJ; `fixed-frame-peirce-matrix-reduction.md`; `off-sector-leakage-globalization-theorem.md`; sector reconstruction notes | O | high-rank matrix exact-adjoint splitting benchmark; Agent B proof claim, independent re-audit pending |
| rem:matrix-audit | B-MATADJ | `agent-B/notes/subagent-schur-residual-audit-v0.1.md`; `subagent-matching-curvature-audit-v0.1.md`; `pointwise-schur-curvature-caveat.md` | O | audit caveat: earlier Haagerup route had ordinary-vs-cb gap; matching route claims closure, re-audit pending |
| cor:adjoint-benchmark | B-ADJ | B-ADJ | O | master exact-adjoint coboundary inversion, universal constant, all finite-dim JB; benchmark only, modulo \Cref{rem:matrix-audit} |
| prop:diag-next-arrow | B-DNEXT / B-NEWTON | B-DNEXT; B-NEWTON | O | fixed diagonal-frame $D\times D$ matrix next-arrow theorem with a bounded Walsh projection; does not close the full matrix next-arrow |
%% --- rows added 2026-06-05: exponent (sec:exponent) ---
| def:decomposable | VLW | VLW (decomposable = CP+coCP); `agent-B/notes/subagent-decomposable-norm.md` | I | decomposable map $\Phimap=\Phimap_0+\Psi_0\circ\tau$ |
| prop:decomposable-norm | B-DEC | `agent-B/notes/subagent-decomposable-norm.md` | O | standard decomposable norm of $\tau_n$ is $n$; correct hypothesis is CP+coCP component bound |
| thm:dilation-compatible | B-DECDIL | B-DECDIL | O | conditional $O(\eta)$ bridge by reduction to Kitaev, under lifted-UCP hypothesis |
| prop:doubling | B-DEC | `agent-B/notes/decomposable-doubling-obstruction.md` | O | exact commutative counterexample: $\Phimap=Cj$ idempotent but $jC$ defect $1$ |
| prop:sartre | B-DEC | `agent-B/notes/subagent-decomposable-alpha1-stress.md` | O | bad CP+coCP decomposition of depolarising $M_2$ projection; $\eta=0$ but lift defect $\eps/2$ |
| op:decomposable | TS3 / B-DEC | TS3 (Theorem 5); B-DEC | OPEN | general decomposable $O(\eta)$ conjecture |
%% --- row added 2026-06-05: bridge numerics (sec:bridge) ---
| rem:bridge-numerics | B-NULL | B-NULL | O | $\norm{P(q_r^2)}/\eta\to32/27$ (so $O(\eta^2)$ false); qubit triviality |
| rem:vlw | VLW | 1517–1524 (thm:luczak); 235–247 | **V** | VLW L1521–1524 minimal PTP-sufficient operator system is the fixed-point intersection; L236–245 Neyman--Pearson tests generate the minimal sufficient J*-algebra |

**Verification log.** The **V**-marked statements were confirmed against the registered local sources by direct line inspection or fixed-string search. Agent B's 2026-06-02 review corrected the ES registry to point to the OCR page files actually used, added HOS state-functional provenance, removed a misleading VLW contraction source, and downgraded Whitehead/compactness to extraction-level provenance until primary text extraction is independently checked.
