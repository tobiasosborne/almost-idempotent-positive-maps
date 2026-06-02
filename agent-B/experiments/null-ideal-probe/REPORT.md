# Null-Ideal Probe Report

Scope: low-dimensional numerical/symbolic probes for
`||P(h_{r,s}^2)||`, with `r,s in Im P` normalized, where
`P=theta(2 Phi-I)` and `h_{r,s}=r o s-P(r o s)`.

## Classical `R^3` Finding

Norms: `R^n` has the sup norm, positive unital maps are row-stochastic
matrices, and

```text
eta = ||T^2-T||_{infty -> infinity}
    = max_i sum_j |(T^2-T)_{ij}|.
```

The clearest nontrivial family is

```text
P0 = [ 1    0    0
       0    1    0
       1/3  2/3  0 ],

S  = [ 1    0    0
       0    0    1
       0    0    1 ],

T_a = (1-a) P0 + a S
    = [ 1        0          0
        0        1-a        a
        (1-a)/3  2(1-a)/3  a ].
```

Here `T_a` is row-stochastic for `0 <= a <= 1`. The spectral projection
`P=theta(2T_a-I)` is the near-rank-2 projection. For small `a`,

```text
eta = (2/3) a (1-a),
max_{||r||_inf,||s||_inf <= 1, r,s in Im P} ||P(h_{r,s}^2)|| = (64/81) a + O(a^2),
```

so

```text
||P(h_{r,s}^2)|| / eta -> 32/27 = 1.185185...
||P(h_{r,s}^2)|| / sqrt(eta) -> 0.
```

Full finite-`a` optimization gave:

| a | eta | defect | defect/eta | defect/sqrt(eta) |
|---:|---:|---:|---:|---:|
| 0.1 | 0.06 | 0.0745689 | 1.24282 | 0.304426 |
| 0.03 | 0.0194 | 0.0234204 | 1.20724 | 0.168149 |
| 0.01 | 0.0066 | 0.00787319 | 1.19291 | 0.0969122 |
| 0.003 | 0.001994 | 0.00236795 | 1.18754 | 0.0530287 |
| 0.001 | 0.000666 | 0.000789858 | 1.18597 | 0.0306064 |
| 0.0003 | 0.00019994 | 0.000237013 | 1.18542 | 0.0167619 |
| 0.0001 | 0.00006666 | 0.0000790097 | 1.18526 | 0.00967716 |

This is not a counterexample to smallness. It is evidence for an `O(eta)`
null-ideal estimate in this low-dimensional classical regime. It also shows
that a generally better order such as `O(eta^2)` is false.

## Random Classical Searches

The search harness sampled exact absorbing/transient stochastic projections
and perturbations `T=(1-a)P0+aS` in dimensions `3,4,5`, then optimized over
`r,s in Im P`. The strongest random `R^3` scan before first-order refinement
found `defect/eta ~= 0.927` at `a=0.003`. A leading-order optimizer for the
`R^3` absorbing/transient model found the sharper asymptotic constant
`32/27`, attained by the simple family above.

No sampled family showed growth of `defect/eta` as `eta -> 0`; the observed
behavior was linear in `eta`.

## Qubit Probe

For `H=C^2`, write self-adjoint matrices as `x0 I + v.sigma`. A unital
self-adjoint map has Bloch form

```text
Phi(x0,v) = (x0 + t.v, Mv).
```

The spectral projection has the same triangular form

```text
P = [ 1  q
      0  R ],
```

with `R^2=R` and idempotence forcing `qR=0`. Thus

```text
Im P = R I + {u.sigma : u in Im R}.
```

For `r,s in Im P`, the vector part of `r o s` remains in `Im R`, and `q`
annihilates it. Hence `h_{r,s}=0` in this qubit Bloch-form setting. The
numerical qubit run, using convex perturbations of positive projections,
accordingly found defects only at floating-point noise level (`~1e-31`).

## Bottom Line

I found no low-dimensional counterexample to smallness. The most informative
classical example gives a nonzero linear term:

```text
||P(h_{r,s}^2)|| = Theta(eta),
```

with asymptotic ratio `32/27` under the stated normalizations. Thus the probe
supports the plausibility of an `O(eta)` approximate null-ideal estimate, and
strongly supports at least `O(sqrt eta)` in these examples.
