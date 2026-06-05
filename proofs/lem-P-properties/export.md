# Proof Export

## Node 1

**Statement:** For eta <= eta_0 < 1/4 there are universal constants so that P=theta(2Phi-1) satisfies P^2=P, P(1)=1, P real-linear on B(H)_sa, ||R-1||<=C eta, delta:=||P-Phi||<=C eta, ||P||<=1+C eta, and delta-positivity (a>=0 => P(a) >= -delta||a|| 1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Setup and spectral bounds. Phi is unital positive on B(H)_sa. By node 1.1.1, ||Phi||=1 in the order-unit norm; Phi(I)=I by hypothesis (def positive-unital-map). Work in the unital Banach algebra End(B(H)_sa) (node 1.1.2). Put S:=2Phi-I; then ||S||<=2||Phi||+||I||=3 by the triangle inequality, homogeneity and ||Id||=1 (node 1.1.2). Since S^2-I=(2Phi-I)^2-I=4Phi^2-4Phi=4(Phi^2-Phi), by def almost-idempotent ||S^2-I||=4||Phi^2-Phi||<=4 eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** ||Phi||=1 in the order-unit norm. Phi is positive (monotone) and unital (Phi(I)=I, hence Phi(-I)=-I) by hypothesis (def positive-unital-map). By GT-order-unit-norm, for a in B(H)_sa, ||a||<=1 iff -I<=a<=I. If ||a||<=1 then -I<=a<=I; monotonicity + unitality give -I=Phi(-I)<=Phi(a)<=Phi(I)=I, so ||Phi(a)||<=1 (GT-order-unit-norm). Thus ||Phi||<=1; and ||Phi||>=||Phi(I)||=||I||=1 since Phi(I)=I and ||I||=1 (GT-order-unit-norm). Hence ||Phi||=1.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** End(B(H)_sa) with ||T||:=sup{||Ta||:||a||<=1} is a unital Banach algebra. B(H)_sa is a normed space with order unit I (GT-order-unit-norm) and is COMPLETE (GT-bhsa-complete: B(H)_sa is a unital JB algebra, HOS 3.1.2, and a unital JB algebra is a complete order-unit space, HOS 3.3.10), i.e. a Banach space. From the sup-definition: ||Id||=1; ||T+U||<=||T||+||U|| (triangle); ||TUa||<=||T|| ||Ua||<=||T|| ||U|| ||a|| so ||TU||<=||T|| ||U|| (submultiplicativity). Since B(H)_sa is a Banach space, End(B(H)_sa) with the operator norm is a unital Banach algebra (GT-end-banach, Kitaev:638-642); hence the function calculus GT-funcalc applies.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** R well-defined with ||R-I||<=C eta. Work in the Banach algebra End(B(H)_sa) (node 1.1.2). Put U:=S^2-I; by node 1.1, ||U||=||S^2-I||<=4 eta, and we FIX eta_0<1/4 so that 4 eta_0<1. Apply GT-funcalc with f(x)=x^(-1/2) (Taylor coefficients a_n=C(-1/2,n), center x0=1, radius rho=1): since ||U||<=4 eta_0<1=rho, R:=(S^2)^(-1/2)=f(S^2)=sum_{n>=0} a_n U^n converges in End(B(H)_sa) and ||R-I||=||f(S^2)-f(I)|| <= sum_{n>=1}|a_n| ||U||^n. Factoring one power of ||U||: sum_{n>=1}|a_n| ||U||^n = ||U|| * sum_{n>=1}|a_n| ||U||^{n-1} <= ||U|| * sum_{n>=1}|a_n|(4 eta_0)^{n-1} = C(eta_0)*||U||, with C(eta_0):=sum_{n>=1}|a_n|(4 eta_0)^{n-1} < infinity since 4 eta_0<rho=1 (GT-funcalc). Hence ||R-I||<=C(eta_0)*||U||<=4 C(eta_0) eta =: C eta.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** P^2=P. Work in the Banach algebra End(B(H)_sa) (node 1.1.2). For S=2Phi-I, ||S^2-I||<=4 eta<1 (node 1.1). Kitaev states sgn(X)^2=I for every X with ||X^2-I||<1 (GT-kitaev-spectral, refs/kitaev:514-522, line 518), where sgn(X)=X(X^2)^(-1/2); applied to X=S, sgn(S)^2=I. Moreover Kitaev's Banach-algebra Proposition prop_P (refs/kitaev:524-532), instantiated at Phi in End(B(H)_sa) with ||Phi^2-Phi||<=eta<1/4 (def almost-idempotent, eta_0<1/4), states directly that P=theta(2Phi-I)=(1/2)(I+sgn(2Phi-I)) satisfies P^2=P. Explicitly, P=(I+sgn(S))/2 gives P^2=(I+2 sgn(S)+sgn(S)^2)/4=(I+sgn(S))/2=P. Uses nodes 1.1, 1.1.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** P(I)=I. Phi(I)=I by hypothesis (def positive-unital-map). With S=2Phi-I (node 1.1), S(I)=I, so S^2(I)=I and U(I)=(S^2-I)(I)=0. By GT-funcalc, R=f(S^2)=sum_{n>=0} a_n U^n with constant term a_0=f(x0)=f(1)=1. Since U(I)=0, U^n(I)=0 for n>=1, so R(I)=a_0 I=I; thus sgn(S)(I)=S R(I)=S(I)=I, and P=(I+sgn(S))/2 (node 1.3) gives P(I)=(I+sgn(S))(I)/2=I. Uses nodes 1.1, 1.2, 1.3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** delta:=||P-Phi||<=C eta and ||P||<=1+C eta. In End(B(H)_sa) (node 1.1.2): P=(I+sgn(S))/2=(I+SR)/2 (node 1.3, with sgn(S)=SR and R=(S^2)^(-1/2) from node 1.2) and Phi=(I+S)/2, so P-Phi=(I+SR)/2-(I+S)/2=S(R-I)/2. By submultiplicativity (node 1.1.2), delta=||P-Phi||<=||S|| ||R-I||/2<=(3/2) C_2 eta, using ||S||<=3 (node 1.1) and ||R-I||<=C_2 eta (node 1.2). Define the universal constant C:=(3/2) C_2; then delta<=C eta. (Kitaev prop_P, refs/kitaev:530, independently gives the same O(eta) closeness.) Then by the triangle inequality (node 1.1.2), ||P||<=||Phi||+delta<=1+C eta, using ||Phi||=1 (node 1.1.1). Uses nodes 1.1, 1.1.1, 1.1.2, 1.2, 1.3.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** P is real-linear on B(H)_sa. Phi is real-linear by hypothesis (def positive-unital-map); hence S=2Phi-I and U=S^2-I are real-linear, and each partial sum R_N:=sum_{n<=N} a_n U^n (a_n real) is real-linear. R is the operator-norm limit of R_N (node 1.2), and for any z, R_N z -> R z pointwise since ||R_N z - R z|| <= ||R_N - R|| ||z|| (operator-action bound from the induced-operator-norm sup-definition, node 1.1.2) and ||R_N - R|| -> 0 (node 1.2). Real-linearity passes to the limit as two separate facts: (i) additivity R(x+y)=lim_N R_N(x+y)=lim_N(R_N x+R_N y)=R x+R y (pointwise limits + continuity of addition); (ii) homogeneity R(s x)=lim_N R_N(s x)=lim_N s(R_N x)=s R x for real s (pointwise limit + continuity of scalar multiplication). Hence R is real-linear, and so are sgn(S)=S R and P=(I+sgn(S))/2. Uses nodes 1.1.2, 1.2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** delta-positivity: x>=0 => P(x) >= -delta ||x|| I. For x>=0, Phi(x)>=0 (GT-positive-unital). Let y:=P(x)-Phi(x), self-adjoint with ||y|| <= ||P-Phi|| ||x|| <= delta ||x|| (node 1.5). By GT-order-unit-norm, ||y|| <= delta||x|| gives -delta||x|| I <= y. Hence P(x)=Phi(x)+y >= 0 - delta||x|| I = -delta ||x|| I.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

