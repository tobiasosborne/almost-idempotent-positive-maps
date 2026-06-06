# Proof Export

## Node 1

**Statement:** With omega=rho∘Phi a state and ||x||_omega^2=omega(x^2), P is an almost-contraction (||Px||_omega^2 <= ||x||_omega^2 + C eta ||x||^2) and Im P is almost-orthogonal to Ker P (|omega(u∘n)| <= C sqrt(eta) ||u|| ||n|| for u in Im P, n in Ker P); hence ||P(Px ∘ b) - P(x∘b)|| <= C sqrt(eta) ||x|| ||b|| for b in A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** Setup. Fix a state rho on B(H) and set omega:=rho∘Phi, ||x||_omega^2:=omega(x^2) on V=B(H)_sa. CLAIMS: (a) omega is a state on the JB algebra V=B(H)_sa (positive functional with omega(1)=1); (b) ||.||_omega is a seminorm with ||x||_omega^2=omega(x^2) <= ||x||^2 for x in V. PROOF: V=B(H)_sa is a unital JB algebra (GT-bhsa-jc, GT-jb-orderunit-3310) with operator norm = order-unit norm (GT-jb-orderunit-3310). Phi is positive unital (def positive-unital-map): for x>=0, Phi(x)>=0 (GT-positive-monotone), and rho is a state on B(H) (positive, rho(1)=1), so omega(x)=rho(Phi(x))>=0 for x>=0, i.e. omega is positive; omega(1)=rho(Phi(1))=rho(1)=1 (def positive-unital-map Phi(1)=1). Hence omega is a state on V. By GT-cauchy-schwarz (HOS 3.6.2) applied to the state omega on the JB algebra V, a->omega(a^2)^{1/2} is a seminorm; so ||.||_omega is a seminorm. Finally for x in V, x^2=x∘x with ||x^2||=||x||^2 (GT-jb-axiom-sq) and -||x^2||1 <= x^2 <= ||x^2||1 in V (order-unit norm, GT-jb-orderunit-3310); applying the state omega (positive, omega(1)=1, monotone) gives omega(x^2) <= ||x^2||=||x||^2. Uses GT-bhsa-jc, GT-jb-orderunit-3310, GT-positive-monotone, GT-cauchy-schwarz, GT-jb-axiom-sq, def positive-unital-map.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** Almost-contraction: ||Px||_omega^2 <= ||x||_omega^2 + C eta ||x||^2 for all x in V, i.e. omega((Px)^2) <= omega(x^2) + C eta ||x||^2. PROOF chains three inequalities (omega=rho∘Phi). STEP A: omega((Px)^2)=rho Phi((Px)^2) <= rho Phi((Phi x)^2) + C eta ||x||^2. By node 1.2.1, ||(Px)^2-(Phi x)^2|| <= 2 max(||Px||,||Phi x||) ||Px-Phi x||; ||Px-Phi x|| <= delta ||x|| with delta<=C eta (GT-Pprops), ||Px|| <= ||P|| ||x|| <= (1+C eta)||x|| and ||Phi x|| <= ||Phi|| ||x||=||x|| (GT-Pprops ||P||<=1+C eta, ||Phi||=1), so max(...)<=C||x|| and ||(Px)^2-(Phi x)^2|| <= C eta ||x||^2. The state rho∘Phi applied to the self-adjoint difference (Px)^2-(Phi x)^2 is bounded by its order-unit norm: |rho Phi((Px)^2-(Phi x)^2)| <= ||(Px)^2-(Phi x)^2|| (omega is a state, |omega(y)| <= ||y|| for self-adjoint y in V, since -||y||1<=y<=||y||1 (GT-jb-orderunit-3310) and omega monotone, omega(1)=1, node 1.1). Hence rho Phi((Px)^2) <= rho Phi((Phi x)^2) + C eta ||x||^2. STEP B: rho Phi((Phi x)^2) <= rho Phi(Phi(x^2)) = rho Phi^2(x^2). Jordan-Schwarz (GT-jordan-schwarz) for the unital positive map Phi at element x in V gives Phi(x)^2 <= Phi(x^2) in V; apply the positive map Phi (monotone, GT-positive-monotone) then the state rho (monotone) to get rho Phi((Phi x)^2) <= rho Phi(Phi(x^2)). STEP C: rho Phi^2(x^2) <= rho Phi(x^2) + C eta ||x||^2. Since ||Phi^2-Phi|| <= eta (def almost-idempotent, GT-Pprops) and ||x^2||=||x||^2 (GT-jb-axiom-sq), the self-adjoint y:=Phi^2(x^2)-Phi(x^2) has ||y|| <= eta ||x^2|| = eta ||x||^2; the state rho gives rho(Phi^2(x^2)) <= rho(Phi(x^2)) + |rho(y)| <= rho Phi(x^2) + eta ||x||^2. Chaining A,B,C: omega((Px)^2) <= omega(x^2) + C eta ||x||^2 (absorb constants into C). Uses node 1.1, node 1.2.1, GT-Pprops, GT-jordan-schwarz, GT-positive-monotone, GT-jb-axiom-sq, GT-jb-orderunit-3310, def almost-idempotent.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** Sq-diff bound: for y,z in V=B(H)_sa, ||y^2-z^2|| <= 2 max(||y||,||z||) ||y-z||, where y^2=y∘y and ||.|| is the operator norm. PROOF: B(H) is a C*-algebra in the operator norm with associative product (GT-bh-cstar); y,z in B(H)_sa ⊆ B(H) and on self-adjoint elements y∘y=(1/2)(yy+yy)=yy, the associative square (def jordan-product), and the JB/order-unit norm on B(H)_sa equals the B(H) operator norm (GT-bhsa-jc, GT-jb-orderunit-3310). In the associative algebra B(H): y^2-z^2 = y(y-z) + (y-z)z (expand: y y - y z + y z - z z = y y - z z). By the triangle inequality and submultiplicativity ||uv|| <= ||u|| ||v|| (GT-banach-submult, valid in the C*-algebra B(H) per GT-bh-cstar): ||y^2-z^2|| <= ||y(y-z)|| + ||(y-z)z|| <= ||y|| ||y-z|| + ||y-z|| ||z|| = (||y||+||z||) ||y-z|| <= 2 max(||y||,||z||) ||y-z||. (Here y^2-z^2 is self-adjoint so its B(H)-norm equals its order-unit norm in V, GT-jb-orderunit-3310.) Uses GT-bh-cstar, GT-banach-submult, GT-bhsa-jc, GT-jb-orderunit-3310, def jordan-product.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** Almost-orthogonality: |omega(u∘n)| <= C sqrt(eta) ||u|| ||n|| for u in Im P, n in Ker P (def near-fixed-algebra). PROOF: Put c=omega(u∘n) and a=||n||_omega^2=omega(n^2). Since P is an exact idempotent (P^2=P, GT-Pprops) and u in Im P (so Pu=u), n in Ker P (so Pn=0), we have P(u+tn)=Pu+tPn=u for every real t (P real-linear, GT-Pprops). Apply the almost-contraction (node 1.2) to x=u+tn: ||P(u+tn)||_omega^2 <= ||u+tn||_omega^2 + K eta ||u+tn||^2, i.e. ||u||_omega^2 <= ||u+tn||_omega^2 + K eta||u+tn||^2. Expand ||u+tn||_omega^2=omega((u+tn)^2)=omega(u^2)+2t omega(u∘n)+t^2 omega(n^2)=||u||_omega^2+2tc+t^2 a (omega linear, (u+tn)^2=u^2+2t(u∘n)+t^2 n^2 using bilinearity/symmetry of ∘, def jordan-product). So 0 <= 2tc + t^2 a + K eta ||u+tn||^2 for all real t. Choose sign of t opposite to c and set s=|t|>0: 2tc=-2s|c|, giving 2s|c| <= s^2 a + K eta ||u+tn||^2. Bound ||u+tn||^2 <= (||u||+s||n||)^2 <= 2||u||^2+2s^2||n||^2 (triangle ineq in V + (p+q)^2<=2p^2+2q^2). Thus 2s|c| <= s^2(a+2K eta||n||^2) + 2K eta||u||^2 for all s>0. Let alpha:=a+2K eta||n||^2 >= 0 and beta:=2K eta||u||^2 >= 0; then 2s|c| <= s^2 alpha + beta for all s>0. By node 1.3.1 (the optimisation), |c| <= sqrt(alpha beta). Hence |c| <= sqrt((a+2K eta||n||^2)(2K eta||u||^2)) = sqrt(2K eta) ||u|| sqrt(a+2K eta||n||^2). Using a=omega(n^2) <= ||n||^2 (node 1.1) and (for eta<1/4) 2K eta||n||^2 <= C||n||^2: a+2K eta||n||^2 <= C||n||^2, so |c| <= C sqrt(eta) ||u|| ||n||. Uses node 1.1, node 1.2, node 1.3.1, GT-Pprops, def near-fixed-algebra, def jordan-product.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** Optimisation lemma: let alpha,beta >= 0 and c real with 2s|c| <= s^2 alpha + beta for all s>0. Then |c| <= sqrt(alpha beta). PROOF: This is a statement about real numbers. Define f(s):=s^2 alpha + beta - 2s|c| for s>0; the hypothesis is f(s) >= 0 for all s>0. CASE alpha>0: f is a quadratic in s minimised at s*=|c|/alpha>0 (if |c|>0; if c=0 the claim |0|<=sqrt(alpha beta) is trivial since alpha,beta>=0). At s=s*: f(s*)=alpha (|c|/alpha)^2 + beta - 2(|c|/alpha)|c| = |c|^2/alpha + beta - 2|c|^2/alpha = beta - |c|^2/alpha. Since f(s*)>=0, beta >= |c|^2/alpha, i.e. |c|^2 <= alpha beta, so |c| <= sqrt(alpha beta). CASE alpha=0: hypothesis becomes 2s|c| <= beta for all s>0; letting s->infinity forces |c|=0 (else LHS unbounded), so |c|=0=sqrt(0·beta)=sqrt(alpha beta). In both cases |c| <= sqrt(alpha beta). (Pure real-analysis identity; no external needed beyond the ordered-field axioms of R.)

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** First insertion (FI): ||P(Px∘b)-P(x∘b)|| <= C sqrt(eta) ||x|| ||b|| for all x in V and b in A=Im P (def near-fixed-algebra). PROOF: Set n:=x-Px. Then Pn=Px-P^2 x=Px-Px=0 (P^2=P, P real-linear, GT-Pprops), so n in Ker P; and ||n||=||x-Px|| <= ||x||+||Px|| <= ||x||+||P|| ||x|| <= (2+C eta)||x|| <= C||x|| (GT-Pprops ||P||<=1+C eta; triangle ineq in V). By P real-linear (GT-Pprops), P(x∘b)-P(Px∘b)=P((x-Px)∘b)=P(n∘b). Fix any state rho on B(H), omega=rho∘Phi. Then |rho(P(n∘b))| <= |rho(Phi(n∘b))| + |rho((P-Phi)(n∘b))|. SECOND term: ||(P-Phi)(n∘b)|| <= ||P-Phi|| ||n∘b|| = delta ||n∘b|| <= delta ||n|| ||b|| (delta=||P-Phi||<=C eta GT-Pprops; ||n∘b|| <= ||n|| ||b|| by the JB-product norm axiom GT-jb-prod-submult, V=B(H)_sa a JB algebra GT-bhsa-jc/GT-jb-orderunit-3310); since rho is a state on B(H), |rho(y)| <= ||y|| for self-adjoint y (analogue of node 1.1's bound, GT-jb-orderunit-3310), so |rho((P-Phi)(n∘b))| <= C eta ||n|| ||b||. FIRST term equals |omega(n∘b)| (omega=rho∘Phi). Now n in Ker P and b in Im P (b in A=Im P), so by almost-orthogonality (node 1.3) with u=b: |omega(n∘b)|=|omega(b∘n)| <= C sqrt(eta) ||b|| ||n|| (n∘b=b∘n, def jordan-product symmetric). Combining: |rho(P(n∘b))| <= C sqrt(eta)||n||||b|| + C eta||n||||b|| <= C sqrt(eta)||n||||b|| <= C sqrt(eta)||x||||b|| (||n||<=C||x||; eta<=sqrt(eta) for eta<1). Since P(n∘b) is self-adjoint (P:V->V, n∘b in V), take the supremum over all states rho on V=B(H)_sa: ||P(n∘b)||=sup_{rho in S(V)}|rho(P(n∘b))| (GT-sup-states, HOS 1.2.5(ii)) <= C sqrt(eta)||x||||b||. Hence ||P(Px∘b)-P(x∘b)||=||P(n∘b)|| <= C sqrt(eta)||x||||b||. Uses node 1.3, GT-Pprops, GT-sup-states, GT-jb-prod-submult, GT-bhsa-jc, GT-jb-orderunit-3310, def near-fixed-algebra, def jordan-product.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

