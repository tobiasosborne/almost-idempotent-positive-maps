# Subagent Matching Curvature Audit v0.1

Date: 2026-06-05.

Source: sidecar agent Averroes, read-only audit.

This memo records an independent audit of
`agent-B/notes/matching-curvature-reconstruction-target.md`.

## Formulation

For a Hermitian Schur symbol

```text
mu_ba=conj(mu_ab),
```

the sharp pure skew target is

```text
dist_gamma2(mu, {i(alpha_a-alpha_b)})
  <= C sup_{I,J,K,pi} ||M_{kappa_pi}||,
```

where

```text
kappa_pi(i,j)=mu_ij+mu_{j,pi(j)}-mu_{i,pi(j)}.
```

For the full sector-preserving residual, one must add the square-detected real
edge term, for example `sup |Re mu_ab|`, or the corresponding edge-weight
control.

The zero-curvature kernel check is correct: vanishing triangle curvature
forces diagonal derivation gauge.

## Dual Proof Route

Since the Schur multiplier norm is the `gamma_2` norm, quotienting by gauges
dualizes to testing only divergence-free edge witnesses.

The desired reconstruction estimate would follow from a dimension-free filling
lemma:

```text
every divergence-free Schur-dual edge witness
= controlled sum or average of matched triangle layers.
```

Pairing a matched triangle layer with `mu` gives exactly a pairing with a
matching curvature slice `kappa_pi`. Thus such a filling theorem would prove
the matching-curvature reconstruction estimate.

## Obstruction Search

No concrete counterexample was found.

The triangular sign and Hankel/logarithmic Schur families are not
counterexamples: matching slices detect them at logarithmic scale. Gauge
perturbations are fake obstructions because the quotient removes them.

The plausible obstruction is failure of the dual filling lemma: there may be
divergence-free witnesses whose cheapest decomposition into matched triangle
layers has norm growing with dimension. Equivalently, one would need symbols
`mu_n` with large quotient `gamma_2` norm but uniformly bounded matching-slice
`gamma_2` norms.

No such family was found among random signs, block-constant symbols,
triangular signs, or low-rank/gauge constructions.

## Verdict

The matching-curvature reconstruction estimate is plausible and sharper than
the earlier cb/base-vertex route, but it remains open.

The next decisive task is:

```text
prove or disprove a dimension-free Schur-dual matched-triangle filling lemma.
```
