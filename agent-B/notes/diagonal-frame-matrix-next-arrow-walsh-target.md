# Diagonal Frame Matrix Next-Arrow Walsh Theorem

Date: 2026-06-05.

This note follows
`agent-B/notes/diagonal-frame-matrix-module-splitting.md` and
`agent-B/notes/commutative-scalar-cocycle-projection-theorem.md`.

It proves the approximate-cocycle projection estimate for the diagonal frame
action

```text
B=R^n,        M=H_n(F),        F in {R,C,H},
x.A=(D_xA+AD_x)/2.
```

The exact Rademacher splitting gives a bounded projection

```text
Pi_n=d^1S_n,        ||Pi_n||<=33,
```

onto exact coboundaries. The next-arrow target is stronger:

```text
||theta-Pi_n theta|| <= C ||Jtheta||
```

with `C` independent of `n` and `F`, where `Jtheta` is the two-variable
linearized Jordan defect.

The scalar half-sum theorem controls each Peirce entry, but entrywise control
alone does not control the operator norm of the coherent off-diagonal matrix.
The proof below replaces entrywise recovery by global diagonal
Walsh/Rademacher averages. The endpoint modes, one-tail modes, and tail-tail
modes all lift in operator norm.

## Theorem

There is a universal constant `C` such that every symmetric 2-cochain
`theta:B x B -> H_n(F)` satisfies

```text
dist(theta,im d^1) <= C||Jtheta||.
```

Consequently, for the bounded Rademacher projection `Pi_n=d^1S_n` from
`agent-B/notes/diagonal-frame-matrix-module-splitting.md`,

```text
||theta-Pi_n theta|| <= 34 C ||Jtheta||.
```

The constants are independent of `n` and of `F in {R,C,H}`.

## Projection Reduction

Because `Pi_n` is a bounded projection onto `im d^1`, any dimension-free
distance estimate

```text
dist(theta,im d^1) <= C ||Jtheta||
```

would imply the displayed projection estimate:

```text
theta-Pi_n theta
  = (I-Pi_n)(theta-c),        c in im d^1,
```

so

```text
||theta-Pi_n theta|| <= (1+||Pi_n||) dist(theta,im d^1)
                      <= 34 C ||Jtheta||.
```

Thus the diagonal-frame next-arrow problem can be attacked with any convenient
exact coboundary representative; it need not use the Rademacher projection
directly.

## Off-Diagonal Scalar Residual Form

Fix an oriented off-diagonal entry `ij`. Write

```text
alpha_x=(x_i+x_j)/2,        delta_x=x_i-x_j,
x^{ij}=x with the i,j coordinates deleted.
```

After subtracting the support-unit exact coboundary in the scalar half-sum
module, the entry residual has the form

```text
r_ij(x,y)
 = A_ij delta_x delta_y
   + B_ij(alpha_x delta_y+alpha_y delta_x)
   + delta_x U_ij(y^{ij})
   + delta_y U_ij(x^{ij})
   + W_ij(x^{ij},y^{ij}).
```

Equivalently,

```text
alpha_x delta_y+alpha_y delta_x = x_i y_i - x_j y_j.
```

The scalar theorem controls `A_ij`, `B_ij`, `U_ij`, and `W_ij` from
edge-dependent defect tests. The matrix problem is to control the matrices and
matrix-valued maps assembled from these coefficients in operator norm, without
summing over edges.

The coefficient arrays have alternating adjoint parity. With oriented entries,
`A` and `W(x,y)` are Hermitian arrays, while `B` and `U(y)` are skew-Hermitian
arrays:

```text
A_ji=conj(A_ij),        B_ji=-conj(B_ij),
U_ji(y)=-conj(U_ij(y)), W_ji(x,y)=conj(W_ij(x,y)).
```

Thus the commutator formulas below still produce Hermitian residual matrices,
as required for values in `H_n(F)`.

If the coefficient matrices/maps are controlled in operator norm, the residual
itself is controlled by diagonal left/right multiplications. For example,
with `D_z=diag(z)`,

```text
R_A(x,y)
 = D_{xy}A-D_xAD_y-D_yAD_x+AD_{xy},
||R_A(x,y)|| <= 4||A||,
```

and

```text
R_B(x,y)
 = D_{xy}B-BD_{xy},
||R_B(x,y)|| <= 2||B||.
```

The `U` terms have the analogous commutator form
`D_x U(y)-U(y)D_x` plus the symmetric term. The real difficulty is therefore
not the final insertion of diagonal factors; it is proving operator-norm
control of the assembled coefficient maps from `Jr`.

## Coherent Modes Already Controlled

Two coherent coefficient modes do lift cleanly from scalar tests to matrix
operator norm.

### The `A` Mode

Assume only

```text
r_ij(x,y)=A_ij(x_i-x_j)(y_i-y_j).
```

For diagonal sign vectors `epsilon in {+-1}^n`,

```text
Jr(epsilon,epsilon)
 = 2(A-D_epsilon A D_epsilon)
```

on the off-diagonal entries. Since
`E_epsilon D_epsilon A D_epsilon=0` off diagonal,

```text
A = (1/2) E_epsilon Jr(epsilon,epsilon).
```

The averaging uses only diagonal sign conjugations and is contractive in the
operator norm. Hence

```text
||A|| <= (1/2)||Jr||,
||R_A|| <= 2||Jr||.
```

### The `B` Mode

Assume only

```text
r_ij(x,y)=B_ij(x_i y_i-x_j y_j).
```

Then

```text
Jr(epsilon,1)=D_epsilon B-BD_epsilon.
```

Multiplying on the left by `D_epsilon` and averaging gives

```text
B=E_epsilon D_epsilon Jr(epsilon,1),
```

again with no rank-dependent loss. Consequently

```text
||B|| <= ||Jr||,
||R_B|| <= 2||Jr||.
```

These two computations show that the coherent off-diagonal accumulation
itself is not automatically fatal. Cut averages detect and reconstruct the
same Schur-type matrices that appear in the residual.

## The `U` Mode Also Lifts

The one-tail mode needs sparse signs rather than ordinary signs. Let
`xi_1,...,xi_n` be independent with

```text
P(xi_i=0)=1-p,        P(xi_i=1)=P(xi_i=-1)=p/2,
```

where `0<p<1` is fixed, say `p=2/3`. Put

```text
Q_xi=diag(xi_i^2),        N_xi=I-Q_xi,
C_xi(A)=D_xi A-AD_xi.
```

For the pure `U` residual

```text
r_ij(x,y)=(x_i-x_j)U_ij(y^{ij})+(y_i-y_j)U_ij(x^{ij}).
```

For fixed `y`, evaluate the defect at

```text
a=xi,        b=N_xi y.
```

Entrywise, if `xi_i` and `xi_j` are not both nonzero and opposite, then the
outer commutator/projection below kills the `ij` entry. If they are opposite,
then `l_ij(a)=0`, `l_ij(a^2)=1`, `b_i=b_j=0`, and the scalar defect formula
gives

```text
J_U(xi,N_xi y)_ij=(xi_i-xi_j)U_ij(N_xi y).
```

The possible `W` contamination in the same test has an odd unused tail sign
and averages to zero; if the two tail indices coincide, the factor
`xi_k(1-xi_k^2)` is zero. The `A` and `B` endpoint modes vanish for these
endpoint values. Therefore, for the assembled off-diagonal matrix `U(y)`,
the same averaged functional extracts the `U` component from a general
residual `R`:

```text
E_xi C_xi(Q_xi J_R(xi,N_xi y) Q_xi)
  = 2p^2(1-p) U(y)
```

Hence

```text
U(y)
 = [2p^2(1-p)]^{-1} E_xi C_xi(Q_xi J_R(xi,N_xi y) Q_xi).
```

The maps `Q_xi`, `N_xi`, and diagonal multiplication by `D_xi` are
contractions and `||C_xi||<=2`. Hence

```text
||U|| <= [p^2(1-p)]^{-1}||J_R||.
```

For `p=2/3`, this is `||U||<=27/4||J_R||`. The residual contribution

```text
R_U(x,y)=D_xU(y)-U(y)D_x+D_yU(x)-U(x)D_y
```

then has a universal operator-norm bound.

Thus the following off-diagonal modes admit dimension-free matrix lifts:

```text
A,        B,        U.
```

No estimate above is obtained by summing scalar Peirce entries; each one is an
average of global matrix-valued defect tests and diagonal contractions.

## The `W` Mode Lifts By Two Sparse Densities

It remains to control the tail-tail residual

```text
r_{W,ij}(x,y)=W_ij(x^{ij},y^{ij}).
```

Entrywise scalar recovery uses the edge-local vector

```text
u_ij=e_i-e_j
```

and gives

```text
W_ij(z,z)
 = Jr_ij(u_ij+z,u_ij)-Jr_ij(u_ij,u_ij)-2Jr_ij(u_ij,z).
```

Using this formula separately for each edge would reassemble an operator from
edge-dependent tests. Instead use a sparse-sign identity.

Let `xi` be as in the `U` section, with density `p`, and put

```text
q_i=xi_i^2,        Q_xi=diag(q_i),        N_xi=I-Q_xi.
```

For `||y||_infty<=1`, define

```text
a_y=xi+N_xi y,        b=xi,
T_p(y)=E_xi C_xi^2(
  Q_xi ( J_W(a_y,b)-J_W(b,b) ) Q_xi
).
```

Here `C_xi(A)=D_xi A-AD_xi`, so `C_xi^2` is the double commutator and has
entry multiplier `(xi_i-xi_j)^2`.

For an output edge `ij`, only the event that `xi_i` and `xi_j` are nonzero and
opposite survives. On that event the endpoint part has

```text
l_ij(a_y)=l_ij(b)=0,        l_ij(a_y^2)=l_ij(a_y b)=1.
```

Writing `s=xi^{ij}` and `z=N_xi y^{ij}`, the pure `W` defect is

```text
J_W(a_y,b)_ij
 = W_ij((s+z)^2,(s+z)s)
   - W_ij((s+z)^2s,s+z)
   + W_ij(s+z,s)
   + W_ij(s+z,s+z).
```

Subtracting `J_W(b,b)_ij` removes the selected-selected constant terms. The
terms with one factor `s` and one factor `z` have an odd selected sign and
average to zero. The same odd-sign cancellation kills the possible `U` mode
contamination in this averaged expression; the `A` and `B` modes cancel
already in `J(a_y,b)-J(b,b)` because they depend only on the endpoints.
The remaining expectation is

```text
(2p^2)^(-1) T_p(y)
 = (1-p)^2 Q_W(y) + p(1-p) B_W(y),
```

where

```text
Q_W(y)_ij = W_ij(y^{ij},y^{ij}),
B_W(y)_ij = W_ij((y^{ij})^2,1^{ij}).
```

Use two densities, for instance

```text
p_1=1/2,        p_2=1/4.
```

Solving the two linear equations for `Q_W(y)` gives

```text
Q_W(y) = (64/3) T_{1/4}(y) - 4 T_{1/2}(y).
```

The vectors `a_y` and `b` have sup norm at most `1`; `Q_xi` and `N_xi` are
diagonal contractions; and `||C_xi^2||<=4`. Hence

```text
||T_p(y)|| <= 8||J_W||.
```

Therefore

```text
sup_{||y||_infty<=1} ||Q_W(y)|| <= (608/3)||J_W||.
```

Finally, for arbitrary `x,y` in the unit ball, real polarization gives

```text
W(x,y)=Q_W((x+y)/2)-Q_W((x-y)/2),
```

so

```text
||W|| <= (1216/3)||J_W||.
```

## Current Status

The diagonal coordinate residual is controlled by the coordinate scalar
theorem and contractivity of diagonal pinching. The off-diagonal support-unit
residual decomposes into `A`, `B`, `U`, and `W` modes, and the preceding
sections control each mode by a universal multiple of `||Jtheta||` in matrix
operator norm.

```text
dist(theta,im d^1) <= C||Jtheta||.
```

The projection reduction at the start then gives

```text
||theta-Pi_n theta|| <= C'||Jtheta||.
```

Thus the diagonal-frame matrix module is not a next-arrow obstruction. The
remaining Layer 1 matrix work is genuinely noncommutative: global matrix
cochains, compatibility across frames, internal Peirce modules not reducible
to this fixed commutative action, and robustness under approximate module
actions.
