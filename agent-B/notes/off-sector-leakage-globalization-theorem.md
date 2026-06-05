# Off-Sector Leakage Globalization Theorem

Date: 2026-06-05.

This note globalizes the single-source leakage estimate from
`agent-B/notes/fixed-frame-peirce-matrix-reduction.md`. It proves that, after
the diagonal gauge, the entire off-sector leakage operator from all
off-diagonal Peirce sectors is controlled in operator norm. This removes the
last fixed-frame high-rank matrix residual isolated in the exact-adjoint
benchmark.

It remains an exact-adjoint benchmark result, not the full Layer 1 stability
theorem for arbitrary modules and approximate cocycles.

## Setup

Let

```text
J=H_n(F),        F in {R,C,H},
```

with standard diagonal frame `e_1,...,e_n`. Let

```text
D=span{e_i},        E=direct_sum_{i<j} V_ij
```

be the diagonal and off-diagonal subspaces. For `a in D`, write `L_a` for
Jordan multiplication by `a`. On `V_ij`,

```text
L_a x = l_ij(a)x,        l_ij(a)=(a_i+a_j)/2.
```

Let `h:J->J` be a normalized adjoint primitive after the diagonal gauge from
`agent-B/notes/fixed-frame-peirce-matrix-reduction.md`, so

```text
h(1)=0,        ||h|_D|| <= C_D ||f||,        f=d^1h.
```

All norms are order/operator norms. Let

```text
H=h|_E:E->J.
```

Let `P_sec H` denote the sector-preserving part of `H`, i.e. the component
mapping each `V_ij` back into the same `V_ij`. The leakage operator is

```text
H_leak=(I-P_sec)H.
```

## Diagonal Commutator Equation

For `a in D` and `x in E`,

```text
f(a,x)=a o h(x)+h(a)o x-h(a o x).
```

Since `a o x=L_a x`, this gives

```text
[L_a,H]x := L_aH(x)-H(L_a x) = f(a,x)-h(a)o x.
```

Therefore

```text
||[L_a,H]||_{E->J} <= (1+C_D)||f|| ||a||.
```

In particular, for every diagonal sign

```text
epsilon in {+-1}^n,
```

the operator

```text
F_epsilon=[L_epsilon,H]
```

satisfies

```text
||F_epsilon|| <= C||f||.
```

## Averaged Squared Commutator

On operators `T:E->J`, define

```text
ad_epsilon(T)=L_epsilon T - T L_epsilon|_E
```

and

```text
R(T)=E_epsilon ad_epsilon^2(T).
```

Here `ad_epsilon^2` means composition:

```text
ad_epsilon^2(T)=ad_epsilon(ad_epsilon(T)).
```

Since `||L_epsilon||<=1`, both on `J` and on `E`,

```text
||ad_epsilon(T)|| <= 2||T||,        ||R(T)|| <= 4||T||.
```

Moreover,

```text
R(H)=E_epsilon ad_epsilon(F_epsilon),
```

so

```text
||R(H)|| <= 2 sup_epsilon ||F_epsilon|| <= C||f||.
```

## Spectral Gap On Off-Sector Maps

Decompose the target `J` into diagonal sectors `Re_i` and off-diagonal Peirce
sectors `V_kl`. Each source sector of `E` is some `V_ij`. If `T` maps
`V_ij` into a target sector `W`, then `R` acts on that block by the scalar

```text
rho(W,ij)=E_epsilon (lambda_W(epsilon)-l_ij(epsilon))^2,
```

where `lambda_{V_kl}=l_kl` and `lambda_{Re_k}(epsilon)=epsilon_k`.

The values are:

```text
0      if W=V_ij,
1/2    if W shares exactly one index with V_ij, including W=Re_i or Re_j,
1      if W=V_kl is disjoint from V_ij,
3/2    if W=Re_k with k notin {i,j}.
```

Thus `R` vanishes exactly on sector-preserving maps and has a uniform spectral
gap on leakage maps.

Let

```text
q(t)= (85/9)t - (40/3)t^2 + (44/9)t^3.
```

Then

```text
q(1/2)=2,        q(1)=1,        q(3/2)=2/3.
```

Here `P_sec` is the algebraic Peirce-sector projection onto the source-matched
target blocks. It is not being assumed bounded as an operator projection on
all of `B(E,J)`; the following polynomial identity proves boundedness on the
part of `H` that we need. Consequently,

```text
H_leak = q(R)R(H).
```

Since `q` is fixed and `||R||<=4`,

```text
||H_leak|| <= C||R(H)|| <= C||f||.
```

## Theorem

After the diagonal gauge, the off-sector leakage operator satisfies

```text
||(I-P_sec)h|_E|| <= C||d^1h||_inj
```

with a universal constant independent of `n` and of `F in {R,C,H}`.

## Consequence

The fixed-frame high-rank matrix exact-adjoint benchmark now has all three
pieces controlled:

1. diagonal-frame restriction;
2. coherent off-sector leakage;
3. sector-preserving edge maps for `F=R,C,H`, modulo frame-stabilizer
   derivations.

Combining this theorem with
`agent-B/notes/real-symmetric-matching-reconstruction-theorem.md`,
`agent-B/notes/hermitian-scalar-sector-reconstruction-corollary.md`,
`agent-B/notes/complex-antilinear-peirce-residual-theorem.md`, and
`agent-B/notes/quaternionic-internal-peirce-residual-theorem.md` closes the
exact-adjoint high-rank matrix simple-factor benchmark.

This still does not prove Layer 1: arbitrary Jordan modules, approximate
cocycles, approximate module errors, and positivity/concrete output remain
separate obligations.
