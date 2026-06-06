# Proof Export

## Node 1

**Statement:** For r in A the square hole q_r = P(r^2)-r^2 in Ker P satisfies q_r >= -C eta ||r||^2 1, ||P(q_r^2)|| <= C eta ||r||^4, and ||q_r||_omega <= C sqrt(eta) ||r||^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** q_r in Ker P. Let r in A=Im P (def-near-fixed-algebra), and let q_r=P(r^2)-r^2 be its square hole (def-square-hole), where r^2=r o r is the ambient Jordan square in V=B(H)_sa. By GT-Pprops, P is real-linear and P^2=P. Since r in Im P, r=P(s) for some s, so P(r)=P^2(s)=P(s)=r, i.e. P(r)=r. Then by linearity P(q_r)=P(P(r^2)-r^2)=P^2(r^2)-P(r^2)=P(r^2)-P(r^2)=0 (using P^2=P on the first term). Hence q_r in Ker P.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** LOWER BOUND: q_r >= -C eta ||r||^2 1. Write delta=||P-Phi|| (GT-Pprops), with delta<=C eta. STEP A (r is Phi-near-fixed): since r in A=Im P, P(r)=r (node 1.1), so ||Phi(r)-r||=||Phi(r)-P(r)||=||(Phi-P)(r)||<=delta||r|| (GT-Pprops, delta=||P-Phi||<=C eta). STEP B (Jordan-Schwarz): Phi is unital positive on B(H)_sa, so by GT-jordan-schwarz with self-adjoint a=r (so a o a=r^2 and (Phi r) o (Phi r)=Phi(r)^2), Phi(r)^2 <= Phi(r^2), i.e. Phi(r^2) >= Phi(r)^2. STEP C (perturb the square): put x:=Phi(r) in V=B(H)_sa. The Jordan product is commutative, so x o x - r o r = (x-r) o (x+r) (expand: (x-r) o (x+r)=x o x + x o r - r o x - r o r = x^2 - r^2, using commutativity x o r=r o x). Bounds: ||x-r||=||Phi(r)-r||<=delta||r|| (Step A). For ||x+r|| we use only the in-scope norm triangle inequality and the grounded delta bound (NO ||Phi||=1): since r=P(r) in A, ||Phi(r)-r||=||(Phi-P)(r)||<=delta||r|| (Step A, GT-Pprops), so by the norm triangle inequality ||Phi(r)||=||(Phi(r)-r)+r||<=||Phi(r)-r||+||r||<=delta||r||+||r||=(1+delta)||r||; hence max(||Phi(r)||,||r||)<=(1+delta)||r|| and ||x+r||<=||x||+||r||=||Phi(r)||+||r||<=(1+delta)||r||+||r||=(2+delta)||r||. By GT-jb-submult (||a o b||<=||a|| ||b|| for the Jordan product), ||Phi(r)^2-r^2||=||(x-r) o (x+r)||<=||x-r|| ||x+r||<=delta||r||*(2+delta)||r||=(2+delta) delta||r||^2=:C delta||r||^2 (C=2+delta<=2+delta_0 universal & dimension-free, delta<=delta_0=C eta_0). By GT-orderunit-def, ||z||<=c (z=z^*) gives -c1<=z<=c1, so with z=Phi(r)^2-r^2: Phi(r)^2 >= r^2 - C delta||r||^2 1. Combining with Step B: Phi(r^2) >= Phi(r)^2 >= r^2 - C delta||r||^2 1. STEP D (replace Phi by P): ||(P-Phi)(r^2)||<=delta||r^2||=delta||r||^2 (GT-bh-cstar ||r^2||=||r||^2 for r=r^*), so by GT-orderunit-def P(r^2) >= Phi(r^2) - delta||r||^2 1 >= r^2 - (C delta+delta)||r||^2 1 = r^2 - C delta||r||^2 1 (absorb constants). Hence q_r=P(r^2)-r^2 >= -C delta||r||^2 1 >= -C eta||r||^2 1 (delta<=C eta). Uses node 1.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** BOUND ||Phi(q_r^2)|| and ||P(q_r^2)|| <= C eta ||r||^4. Write delta=||P-Phi||<=C eta (GT-Pprops). STEP A (crude norm bound on q_r): q_r=P(r^2)-r^2, so ||q_r||<=||P(r^2)||+||r^2||<=||P|| ||r^2||+||r||^2<=(1+C eta)||r||^2+||r||^2<=C||r||^2 (GT-Pprops ||P||<=1+C eta; GT-bh-cstar ||r^2||=||r||^2). STEP B (shift to a positive element): set gamma=C delta||r||^2 the constant from node 1.2, so q_r >= -gamma 1 (node 1.2), hence y:=q_r+gamma 1 >= 0 (GT-orderunit-def). Also ||y||<=||q_r||+gamma<=C||r||^2+C delta||r||^2<=C||r||^2 (Step A; gamma=O(delta||r||^2)). Thus 0 <= y <= ||y|| 1 <= M 1 with M:=C||r||^2 (GT-jb-orderunit-3310 / GT-orderunit-def: ||y||<=M and y>=0 give 0<=y<=M1). STEP C (Phi(y) is small and positive): P(q_r)=0 (node 1.1), so Phi(q_r)=(Phi-P)(q_r), ||Phi(q_r)||<=delta||q_r||<=C delta||r||^2 (Step A). Phi(gamma 1)=gamma 1 (Phi unital), so Phi(y)=Phi(q_r)+gamma 1 with ||Phi(y)||<=||Phi(q_r)||+gamma<=C delta||r||^2. Also y>=0 => Phi(y)>=0 (GT-positive-monotone). STEP D (key: y^2<=M y): by node 1.3.1, 0<=y<=M1 gives 0<=y^2<=M y. STEP E (apply Phi, monotone): from Step D, 0<=y^2 and M y - y^2>=0; by GT-positive-monotone Phi(M y - y^2)>=0 i.e. Phi(y^2)<=M Phi(y), and Phi(y^2)>=0. Hence 0<=Phi(y^2)<=M Phi(y), so by norm-monotonicity (GT-sup-states: 0<=u<=v => ||u||<=||v|| in the order unit space B(H)_sa) ||Phi(y^2)||<=||M Phi(y)||=M||Phi(y)||<=C||r||^2 * C delta||r||^2=C delta||r||^4. STEP F (back to q_r^2): q_r=y-gamma 1, so q_r^2=(y-gamma1) o (y-gamma1)=y^2-2gamma y+gamma^2 1, and the Jordan identity gives 2y^2+2gamma^2 1 - q_r^2=(y+gamma1)^2>=0 (a square is positive, GT-jb-positive-spectrum), i.e. q_r^2<=2y^2+2gamma^2 1. Apply Phi (GT-positive-monotone) and triangle/norm-monotonicity: ||Phi(q_r^2)||<=||Phi(2y^2+2gamma^2 1)||<=2||Phi(y^2)||+2gamma^2||Phi(1)||=2||Phi(y^2)||+2gamma^2 (Phi(1)=1). With ||Phi(y^2)||<=C delta||r||^4 (Step E) and gamma^2=C delta^2||r||^4=O(delta^2||r||^4)<=C delta||r||^4 (delta<=delta_0=C eta_0, eta_0<1/4 fixed): ||Phi(q_r^2)||<=C delta||r||^4. STEP G (replace Phi by P): ||(P-Phi)(q_r^2)||<=delta||q_r^2||=delta||q_r||^2<=delta(C||r||^2)^2=C delta||r||^4 (Step A; GT-bh-cstar ||q_r^2||=||q_r||^2 for q_r=q_r^*). Hence ||P(q_r^2)||<=||Phi(q_r^2)||+C delta||r||^4<=C delta||r||^4<=C eta||r||^4 (delta<=C eta). Uses node 1.1, node 1.2, node 1.3.1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** FUNCTIONAL CALCULUS: for self-adjoint y in V=B(H)_sa with 0<=y<=M 1 (M>=0), one has 0<=y^2<=M y. PROOF via the JB spectral theorem. V=B(H)_sa is a unital JB algebra (GT-bhsa-jc + GT-jc-is-jb). By GT-jb-spectral (HOS 3.2.4), C(y) (smallest norm-closed Jordan subalgebra of V containing y and 1) is isometrically and Jordan-isomorphically mapped by phi onto C(Sp y), the continuous real functions on the compact spectrum Sp y subset R, with phi(1)=1 (constant function 1) and phi(y)=iota (the identity function t |-> t). (i) SPECTRUM IN [0,M]: y, M1-y, and y^2, M y - y^2 all lie in C(y) (Jordan subalgebra generated by y,1; y^2=y o y, M y=scalar mult, M1=scalar mult of 1). By GT-jb-positive-spectrum positivity is intrinsic (c>=0 iff Sp c subset [0,infty), spectrum computed in C(c) subset C(y)), so the hypotheses y>=0 and M1-y>=0 (from 0<=y<=M1 in V; M1-y>=0 is M1-y in V_+, and M1-y in C(y)) transfer to C(y): under phi, phi(y)=t>=0 and phi(M1-y)=M-t>=0 pointwise on Sp y, hence Sp y subset [0,M]. (ii) POINTWISE INEQUALITIES: phi is a unital Jordan isomorphism, so phi(y^2)=phi(y)^2=t^2 and phi(M y)=M*phi(y)=M t (real-linear, multiplicative on the associative C(y)). On Sp y subset [0,M]: t^2>=0 and M t - t^2 = t(M-t)>=0 pointwise (product of two nonnegatives, t>=0 and M-t>=0). So phi(y^2)>=0 and phi(M y - y^2)=M t - t^2>=0 pointwise in C(Sp y). (iii) PULL BACK: the cone of C(Sp y) is the pointwise-nonnegative functions (an order unit space, GT-jb-positive-spectrum/HOS:474), and phi is an order isomorphism (positivity intrinsic, preserved by the Jordan isomorphism), so y^2=phi^{-1}(t^2)>=0 and M y - y^2=phi^{-1}(M t - t^2)>=0 in C(y), hence in V (positivity intrinsic, GT-jb-positive-spectrum). Therefore 0<=y^2<=M y in V. Uses GT-jb-spectral, GT-jb-positive-spectrum, GT-bhsa-jc, GT-jc-is-jb.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** SEMINORM BOUND: ||q_r||_omega <= C sqrt(eta) ||r||^2 for every state seminorm omega=rho o Phi. By def-state-seminorm, ||q_r||_omega^2=omega(q_r^2)=rho(Phi(q_r^2)). rho is a state on B(H), so its restriction to B(H)_sa is a state on the order-unit space B(H)_sa (order unit 1), hence |rho(a)|<=||a|| for self-adjoint a (GT-state-bounded). Phi(q_r^2) is self-adjoint (Phi maps B(H)_sa to B(H)_sa, q_r^2 in B(H)_sa). Therefore ||q_r||_omega^2=rho(Phi(q_r^2))<=|rho(Phi(q_r^2))|<=||Phi(q_r^2)||. By node 1.3 (Step F), ||Phi(q_r^2)||<=C delta||r||^4<=C eta||r||^4 (delta<=C eta, GT-Pprops). Hence ||q_r||_omega^2<=C eta||r||^4, and taking square roots ||q_r||_omega<=sqrt(C eta)||r||^2=C' sqrt(eta)||r||^2 with C'=sqrt(C) a universal constant. Uses node 1.3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

