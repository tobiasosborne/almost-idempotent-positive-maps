# Subagent Matrix Obstruction Audit v0.1

Date: 2026-06-05.

Source: sidecar agent Poincare, read-only audit.

This memo records an independent search for lower-bound obstructions to a
dimension-free exact-adjoint splitting for

```text
J=H_n(F),        F in {R,C,H},
```

in order-unit/operator cochain norm.

## Bottom Line

No genuine obstruction was found.

The correct obstruction criterion is not merely

```text
||d^1h|| << ||h||.
```

Since derivations are the kernel of `d^1`, a real obstruction must satisfy

```text
dist(h, Der(J)) >> ||d^1h||.
```

Several families have a small literal ratio only because they are close to the
derivation gauge.

## Fake Small-Coboundary Families

For any derivation `D` and any normalized non-derivation `k`, for instance

```text
k=P_0,        P_0(x)=x-tr(x)1/n,
```

the family

```text
h_epsilon = D + epsilon k
```

satisfies

```text
h_epsilon(1)=0,
d^1h_epsilon=epsilon d^1k,
||d^1h_epsilon||/||h_epsilon||=O(epsilon).
```

This is pure gauge: subtracting `D` leaves only the small primitive
`epsilon k`.

Similarly, if `alpha_t=exp(tD)` is a one-parameter Jordan automorphism group,
then

```text
h_t=alpha_t-id
```

satisfies the exact identity

```text
d^1h_t(a,b)=-h_t(a) o h_t(b).
```

Thus `||d^1h_t||<=||h_t||^2`, but `h_t/||h_t||` tends to the derivation
`D/||D||` as `t->0`. This is again not an obstruction after quotienting by
derivations.

## Natural Candidates That Fail

The existing notes already rule out unit-value, multiplication, central-valued,
and trace-zero rank-one components as high-rank obstructions.

Two additional elementary candidates also fail.

For

```text
h=P_0,        P_0(x)=x-tr(x)1/n,
```

evaluating at `a=b=e_11` gives

```text
||d^1P_0(a,a)|| >= 1-1/n,
```

while `||P_0||<=2`.

For the off-diagonal projection relative to a fixed frame,

```text
h=E_off,
```

taking `s=E_12+E_21` gives

```text
d^1h(s,s)=2(e_1+e_2),
```

so the coboundary is again large.

## Schur-Multiplier Stress Test

The strongest obstruction candidate found was Schur-multiplier based.

For `H_n(C)`, take

```text
h_m(x)_ij=m_ij x_ij,
m_ij=i sign(i-j),        m_ii=0.
```

This is normalized and not a derivation. Its Schur-multiplier norm grows like
`log n`; testing on the Hermitian Hilbert matrix

```text
X_ij=i/(i-j),        i != j,        X_ii=0,
```

gives bounded `||X||` but `||h_m(X)||` of logarithmic size.

However, sampled tests showed `||d^1h_m||` growing on the same scale. For
`n=8,16,32,48`, structured sampled lower bounds were approximately

```text
1.32, 1.89, 2.51, 2.90.
```

This is consistent with logarithmic growth, not with bounded coboundary and
growing primitive.

For `H_n(R)`, the analogous symmetric Hankel sign multiplier

```text
m_ij=sign(i+j-n-1),        m_ii=0,
```

also has logarithmically growing multiplier norm on a Hankel-Hilbert test
matrix, but its coboundary again grew logarithmically in structured tests.

## Conclusion

No family was found with

```text
dist(h_n, Der(H_n(F))) ~ 1        or growing,
||d^1h_n|| -> 0
```

after normalization.

The Schur-multiplier family remains a serious stress test for any proposed
proof: it shows why pointwise edge control is insufficient. But current
evidence suggests that the full Jordan coboundary detects the same logarithmic
coherence that makes the multiplier large.
