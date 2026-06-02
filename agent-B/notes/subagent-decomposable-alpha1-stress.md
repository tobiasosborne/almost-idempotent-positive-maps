# Sidecar: stress test of the decomposable `O(eta)` bridge

Question: does an explicit decomposition

```text
Phi = Phi_0 + Psi_0 o tau
```

with `Phi_0,Psi_0` completely positive, together with
`||Phi^2-Phi|| <= eta`, plausibly force the projected Jordan product on
`Im theta(2Phi-I)` to have `O(eta)` Jordan defect?

## Conditional mechanism that would work

Let `A=M_d`, let `tau` be a fixed transpose, and use the universal doubled
C*-algebra

```text
U(A) = A direct_sum A^op
```

with Jordan embedding

```text
j(x) = (x, x^op),        x in A_sa.
```

Given `Phi=Phi_0+Psi_0 o tau`, define the CP extension

```text
F: U(A) -> A,
F(x, y^op) = Phi_0(x) + Psi_0(tau(y)).
```

Then `F(j(x))=Phi(x)`.

If one had a UCP endomorphism

```text
widehat Phi: U(A) -> U(A)
```

such that

```text
widehat Phi(j(x)) = j(Phi(x)),
j(x) o j(y) = j(x o y).
```

Therefore, if one could prove the stronger estimate

```text
||widehat Phi^2 - widehat Phi|| <= C eta,        (UL)
```

then Kitaev's CP two-hole theorem would transfer directly to the original
projected Jordan product. The spectral projection of `widehat Phi` restricts
on `j(A_sa)` to `j theta(2Phi-I)`, so the `O(eta)` Jordan defect upstairs
would imply the desired `O(eta)` defect downstairs.

Thus the doubled/universal-envelope route is viable under the extra
component-compatibility condition `(UL)`.

The problem is that the obvious diagonal return `z -> j(F(z))` is only a
Jordan-positive/formal return map in general; the embedding `j:A_sa->U(A)` is
not a CP map of C*-algebras. Thus the CP extension `F` alone is not yet a
Kitaev-ready CP endomorphism.

## Why the current hypotheses do not imply `(UL)`

Even if one ignores this CP-return problem and tests the formal diagonal
return `jF`, its idempotence defect is

```text
(jF)^2(z)-jF(z) = j(Phi(F(z))-F(z)).
```

The original defect `Phi^2-Phi` controls this only on the Jordan diagonal
`z=j(a)`, because then `F(j(a))=Phi(a)`. It gives no control on the separate
CP and coCP legs.

This is not just a proof gap; the implication is false for arbitrary supplied
decompositions.

### Exact example with nonzero lift defect

Work in `M_2`. Let

```text
D(x) = Tr(x) I/2,
p = |0><0|,
R(x) = <0|x|0> p.
```

For `0 < eps <= 1/2`, set

```text
Phi_0 = eps R,
Psi_0 = D - eps R.
```

Both maps are CP. They are also compatible with transpose, since `D tau=D` and
`R tau=R`. The Choi matrix of `Psi_0` is

```text
(1/2) I_4 - eps (p tensor p),
```

so `Psi_0` is CP for `eps <= 1/2`; the same diagonal form makes it coCP.

The decomposable map is exactly the depolarizing projection:

```text
Phi = Phi_0 + Psi_0 o tau
    = eps R + (D-eps R) o tau
    = D.
```

Hence

```text
Phi^2=Phi,        eta=0.
```

But the CP extension has nonzero off-diagonal invariance defect. Taking
`z=(p,0) in M_2 direct_sum M_2^op`,

```text
F(z)=eps p,
Phi(F(z))-F(z)
 = D(eps p)-eps p
 = eps(I/2-p),
```

and therefore

```text
||Phi F-F||_{U(A)->A} >= eps/2.
```

So no estimate controlling the natural universal-envelope off-diagonal terms
can follow from `||Phi^2-Phi||` and the mere existence of a bounded CP+coCP
decomposition. The supplied decomposition can carry large off-diagonal
universal-envelope defect even when the original map is an exact positive
projection.

This does not disprove the actual `O(eta)` bridge: for this example the
projected product is just the scalar algebra and has zero defect. It only
disproves the naive doubled proof using the arbitrary supplied decomposition.

## Low-dimensional obstruction checks

Two easy sources do not produce counterexamples.

1. In `M_2`, every unital idempotent `P` on the self-adjoint part has, in
   Bloch coordinates,

   ```text
   P(a,r) = (a + alpha.r, B r),     B^2=B,     alpha B=0.
   ```

   Thus `Im P = R 1 direct_sum Im B`, and the projected product is an exact
   spin-factor product. The Jordan defect is identically zero. A genuine
   failure of the algebraic bridge must start in matrix size at least `3`.

2. Hume's classical `3 x 3` sharp projection-stability family also has zero
   projected Jordan defect numerically. This is consistent with the fact that
   its range is two-dimensional and unital, where the Jordan identity is
   automatic.

## Verdict

The decomposable `O(eta)` bridge remains plausible, but the current hypothesis
does not justify the advertised doubled CP proof. A proof needs one of the
following stronger ingredients:

```text
||Phi F - F||_{U(A)->A} <= C eta
```

for a chosen universal CP extension `F`, equivalently componentwise
almost-invariance of the supplied CP and coCP legs; or an intrinsic two-hole
calculation that uses only the diagonal defect `Phi^2-Phi` and proves the
off-diagonal universal terms cancel.

I found no concrete family disproving the actual `O(eta)` Jordan-defect
statement.
