---
id: op-jordan-structure
kind: open-problem
contract: (OPEN) Jordan structure theorem: there are dimension-free C,eps_0>0 so that every finite-dimensional eps-JB algebra A (eps<eps_0) admits a genuine finite-dimensional JB-algebra B and a linear bijection v:B->A with ||v(1_B)-1_A||<=C eps, ||v(b•b')-v(b)•v(b')||<=C eps||b||||b'||, and (1-C eps)||b||<=||v(b)||<=(1+C eps)||b|| (the Jordan analogue of Kitaev's main theorem).
defs: def-eps-jb-algebra; def-jb-algebra; def-delta-jordan-homomorphism; def-jordan-frame
deps: thm-jnw-classification; thm-whitehead; prop-aut-compact; cor-adjoint-benchmark
status: open
af: none
provenance: KIT 460-462 (model); A-FIND §11; A-ER (agent-A/theory/01-error-reduction.md); report op:jordan-structure
owner: A
workspace: proofs/op-jordan-structure
---

The standalone abstract structure theorem (Layer 1): an [[def-eps-jb-algebra]] is a controlled
deformation of a genuine [[def-jb-algebra]] via a [[def-delta-jordan-homomorphism]], with a
dimension-free constant. The cohomological strategy (frame/[[def-jordan-frame]], Peirce,
coordinatization, Newton error reduction) is set; the JNW classification (thm-jnw-classification),
Whitehead lemmas (thm-whitehead), Aut(J)-compactness (prop-aut-compact), and the exact-adjoint
benchmark (cor-adjoint-benchmark) are the inputs. Open. Report `op:jordan-structure`; theory:
agent-A/theory/01-error-reduction.md, report/sections/09-structure-programme.tex.
