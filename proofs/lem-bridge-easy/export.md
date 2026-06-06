# Proof Export

## Node 1

**Statement:** The projected product a•b=P(a∘b) on A satisfies the easy axioms with O(eta): unit 1•a=a and commutativity a•b=b•a are exact, ||a•b|| <= (1+C eta)||a||||b||, a•a >= -C eta ||a||^2 1, and ||a•a|| >= (1-C eta)||a||^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** EXACT axioms: unit law and commutativity. For a in A: 1•a=P(1 o a). By def-jordan-product 1 o a = (1/2)(1*a+a*1)=a (unit is the algebra identity), so 1•a=P(a)=a since a=P(a) for a in A (def-near-fixed-algebra, A=Im P=Ker(1-P)). Hence 1•a=a EXACTLY. Commutativity: a•b=P(a o b) and b•a=P(b o a); the Jordan product is commutative a o b=b o a (def-jordan-product, (ab+ba)/2 symmetric), so a•b=P(a o b)=P(b o a)=b•a EXACTLY. No eta error in either.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Upper product bound: ||a•b|| <= (1+C eta)||a|| ||b||. For a,b in A: a•b=P(a o b), so ||a•b||=||P(a o b)|| <= ||P|| * ||a o b|| (definition of operator norm of P, valid since a o b in B(H)_sa). By GT-Pprops ||P||<=1+C eta. By GT-jb-submult (HOS 3.1.3, V=B(H)_sa a JB algebra by GT-bhsa-jc) ||a o b|| <= ||a|| ||b||. Combining: ||a•b|| <= (1+C eta) ||a|| ||b||. (C is the universal constant from GT-Pprops, dimension-free.)

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Approx positivity of squares: a•a >= -C eta ||a||^2 1. For a in A (self-adjoint, A subset B(H)_sa), a•a=P(a o a)=P(a^2) where a^2=a o a. By GT-bh-cstar, a self-adjoint => a^2=a^*a is positive in B(H), a^2>=0. By GT-Pprops delta-positivity (x>=0 => P(x) >= -delta||x|| 1), applied to x=a^2>=0: P(a^2) >= -delta ||a^2|| 1. By GT-jb-axiom-sq (HOS 3.1.4, V=B(H)_sa JB algebra) ||a^2||=||a||^2. By GT-Pprops delta<=C eta. Hence a•a=P(a^2) >= -delta ||a||^2 1 >= -C eta ||a||^2 1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** Square-norm lower bound: ||a•a|| >= (1-C eta)||a||^2. For a in A, a•a=P(a^2), a^2=a o a. STEP A (Jordan-Schwarz): by GT-jordan-schwarz at T=Phi (unital positive on B(H)_sa), a=a^* self-adjoint: Phi(a)^2 = Phi(a) o Phi(a) <= Phi(a o a)=Phi(a^2). STEP B (norm-monotone in cone): both Phi(a)^2>=0 and Phi(a^2)>=0 (squares positive, GT-bh-cstar; Phi positive); since 0 <= Phi(a)^2 <= Phi(a^2), GT-sup-states norm-monotonicity gives ||Phi(a^2)|| >= ||Phi(a)^2|| = ||Phi(a)||^2 (last equality by GT-jb-axiom-sq, ||r^2||=||r||^2 for r=Phi(a) self-adjoint). STEP C (node 1.4.1): ||Phi(a)|| >= (1-delta)||a||, so ||Phi(a^2)|| >= (1-delta)^2 ||a||^2 >= (1-2 delta)||a||^2. STEP D (transfer P<-Phi): ||(P-Phi)(a^2)|| <= delta ||a^2|| = delta ||a||^2 (GT-Pprops operator-norm bound + GT-jb-axiom-sq); by the order-unit norm triangle inequality (GT-orderunit-def), ||P(a^2)|| >= ||Phi(a^2)|| - ||(P-Phi)(a^2)|| >= (1-2 delta)||a||^2 - delta||a||^2 = (1-3 delta)||a||^2 >= (1-C eta)||a||^2, using delta<=C eta (GT-Pprops). Hence ||a•a||=||P(a^2)|| >= (1-C eta)||a||^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Reverse-triangle bound (NO ||Phi||=1): ||Phi(a)|| >= (1-delta)||a|| for a in A. Since a in A=Im P, a=P(a) (def-near-fixed-algebra). Then Phi(a)-a = Phi(a)-P(a) = (Phi-P)(a), so ||Phi(a)-a|| = ||(Phi-P)(a)|| <= delta ||a|| where delta:=||P-Phi|| (GT-Pprops: operator-norm bound ||(P-Phi)(z)||<=delta||z||, here z=a; delta<=C eta). By the reverse triangle inequality for the order-unit norm (GT-orderunit-def, the order norm is a genuine norm): ||Phi(a)|| >= ||a|| - ||Phi(a)-a|| >= ||a|| - delta||a|| = (1-delta)||a||. No appeal to ||Phi||=1 or any Phi-contraction.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

