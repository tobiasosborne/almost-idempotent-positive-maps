VERDICT: CONFIRMED-WITH-CORRECTIONS

Independent argument: in rank 3 the four rows have one affine dependence, so affine values `y_i=h(p_i)` are feasible exactly when `a y0+b y1=c y2+d y3`. For `p0`, choose values `(0,1,b,b)`. They satisfy the circuit, lie in `[0,1]`, and give margin at least `b`; similarly `(1,0,a,a)`, `(d,d,0,1)`, `(c,c,1,0)` give margins at least `a,d,c`. These are lower bounds only.

For collapse, let `q=c p2+d p3=a p0+b p1 ∈ conv{p2,p3}`. Then
`dist1(p0,conv{p2,p3}) ≤ ||p0-q||1 = b||p0-p1||1 ≤ bD`, if `D` is row diameter. This is sharper than the recorded `(b/a)D`; since `a<1`, the claimed `(b/a)D` also follows. Equivalently, the recorded derivation gives `||p0-q||=(b/a)||q-p1||≤(b/a)D`.

Reconciliation: the recorded proof uses the same affine-value certificates and correctly flags the margins as lower bounds. The re-verification’s warning is important: large coefficient implies exposed by this certificate; non-exposedness in an absolute sense does not imply the coefficient is small without extra argument. No refutation. Corrected constant: normalized circuit gives `bD` for `p0`, cyclically `aD,dD,cD`; `(b/a)D` etc. are valid weaker collapse bounds.