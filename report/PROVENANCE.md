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
| `A-FIND` | `agent-a-findings` | `42674f8c12e0eab1` | INTERNAL. Agent A consensus/status file. |
| `A-INGEST` | `agent-A/notes/ingestion-results-2026-06-01.json` | `972bba533931fd3d` | INTERNAL EXTRACTION. Agent A local extraction of Kitaev/VLW and Jordan-background literature. |
| `A-ER` | `agent-A/theory/01-error-reduction.md` | `facf15f4bee20cc5` | INTERNAL. Agent A error-reduction programme note. |
| `A-JCOB` | `agent-A/experiments/jordan-coboundary/REPORT.md` | `7c456f26a8787be0` | INTERNAL. Agent A numerical Jordan-coboundary report. |
| `B-ROUND` | `agent-B/notes/factorization-positivity-rounding.md` | `42c922ebef1d7516` | INTERNAL. Agent B positivity-rounding obstruction note. |

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
| thm:jordan-structure | KIT (model) / ORIGINAL | KIT 460–462; A-FIND §11 | OPEN | open Jordan analogue; KIT L461 is the verified model statement, harmonized in report prose |
| thm:whitehead | CHU / A-INGEST | A-INGEST "jordan-stability-cohomology" | EXTRACT / PDF | $H^1{=}H^2{=}0$ (Whitehead lemmas); CHU primary is local PDF, but report statement currently comes through hashed extraction |
| prop:aut-compact | A-INGEST | "Aut(J) is compact" extraction block | EXTRACT | $\Aut(J)$ compact for Euclidean $J$; Faraut--Koranyi primary text not locally extracted in this repo |
| prop:error-reduction | ORIGINAL / OPEN | A-ER §3; Agent B correction in §7 | OPEN | candidate group-averaged separability idempotent; order-unit-norm dimension-free homotopy remains open |
| rem:exponent | ORIGINAL / KIT | A-FIND §9–10; KIT 2643–2673; Agent B correction in §8 | O | $\sqrt\eta$ general; $\eta$ in UCP/cb or compatible dilation settings; decomposable case open |
| thm:effros-stormer | ES-P05 / ES-P06 / ES-P02 | P05 L9–16; P06 L42–44; P02 L33–38 | **V** | positive unital projection $\Rightarrow$ $P(A)$ a JC-algebra under $P(r\jp s)$; fixed-point JW corollary; Lemma 1.1 proof input |
| rem:bridge-exact | ES-P05 / ES-P06 | P05 L9–16; P06 L42–44 | **V** | exact $\eta=0$ positive-projection endpoint underlying the bridge theorem |
| rem:rounding | ORIGINAL | B-ROUND §§2–4 | O | generic $O(\eps)$ positivity-rounding FALSE (spin-factor counterexample) |
| rem:vlw | VLW | 1517–1524 (thm:luczak); 235–247 | **V** | VLW L1521–1524 minimal PTP-sufficient operator system is the fixed-point intersection; L236–245 Neyman--Pearson tests generate the minimal sufficient J*-algebra |

**Verification log.** The **V**-marked statements were confirmed against the registered local sources by direct line inspection or fixed-string search. Agent B's 2026-06-02 review corrected the ES registry to point to the OCR page files actually used, added HOS state-functional provenance, removed a misleading VLW contraction source, and downgraded Whitehead/compactness to extraction-level provenance until primary text extraction is independently checked.
