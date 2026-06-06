# Proof Export

## Node 1

**Statement:** Polarised holes q_{r,s}=P(r∘s)-r∘s obey, in the state seminorm ||x||_omega^2=omega(x^2), ||q_{r,s}||_omega <= C sqrt(eta)||r||||s|| (4.1) and ||q_{r,s}|| <= C||r||||s||; hence ||P(q_{r,s}∘q_{u,v})|| <= C eta ||r||||s||||u||||v|| (HH) and ||P(q_{r,s}∘z)|| <= C sqrt(eta)||r||||s||||z|| for z in V (HZ).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** SETUP. Fix r,s,u,v in A=Im P (def-near-fixed-algebra) and z in V=B(H)_sa. B(H)_sa is the special Jordan algebra of self-adjoint operators and hence a JC algebra (GT-bhsa-jc, B(H) a C*-algebra GT-bh-cstar), and each JC algebra is a JB algebra (GT-jc-is-jb), so V=B(H)_sa is a unital JB algebra with Jordan product a∘b=(ab+ba)/2 and order unit 1 (GT-bhsa-jc, GT-jc-is-jb, GT-bh-cstar, GT-jb-orderunit-3310). (a) The polarised hole q_{r,s}:=P(r∘s)-r∘s lies in Ker P: P(q_{r,s})=P(P(r∘s))-P(r∘s)=P^2(r∘s)-P(r∘s)=0 since P^2=P (GT-Pprops). (b) Fix any state rho on B(H) (rho on V is a state on the order unit space V, GT-jb-orderunit-3310/GT-state-bounded) and set omega:=rho∘Phi. Then omega is a state on V: omega(1)=rho(Phi(1))=rho(1)=1 (Phi unital, GT-positive-unital) and omega(a)=rho(Phi(a))>=0 for a>=0 (Phi positive maps a>=0 to Phi(a)>=0, rho a state, GT-positive-unital). (c) The state seminorm ||x||_omega^2:=omega(x^2)=rho(Phi(x^2)) is a genuine seminorm on V: omega is a state on the JB algebra V, so a->omega(a^2)^{1/2} is a seminorm (GT-cauchy-schwarz, 3.6.2). In particular it satisfies the triangle inequality and ||lambda x||_omega=|lambda| ||x||_omega. Uses GT-Pprops, GT-positive-unital, GT-cauchy-schwarz, GT-bhsa-jc, GT-jc-is-jb, GT-bh-cstar, GT-jb-orderunit-3310, GT-state-bounded, def-near-fixed-algebra.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** (4.1): ||q_{r,s}||_omega <= C sqrt(eta) ||r|| ||s|| for r,s in A=Im P (def-near-fixed-algebra), every state seminorm omega (node 1.1). PROOF. The map (a,b)->q_{a,b}:=P(a∘b)-a∘b is symmetric (∘ symmetric, def jordan-product) and real-bilinear on A (P real-linear by GT-Pprops, ∘ bilinear; A=Im P is a real subspace so closed under linear combinations); write q_t:=q_{t,t}=P(t^2)-t^2 for the diagonal square hole (def-square-hole). Step 1 (polarisation). For a,b in A, a∘b=(1/4)((a+b)^2-(a-b)^2), so bilinearity+symmetry give q_{a,b}=(1/4)(q_{a+b}-q_{a-b}). For any lambda>0, bilinearity gives q_{r,s}=q_{lambda r, s/lambda}=(1/4)(q_{lambda r+s/lambda}-q_{lambda r-s/lambda}); the arguments lambda r ± s/lambda lie in A (real subspace). Step 2 (seminorm + diagonal bound). By the seminorm triangle inequality (node 1.1) and the DIAGONAL square-hole seminorm bound ||q_t||_omega<=C sqrt(eta)||t||^2 for t in A (GT-square-hole): ||q_{r,s}||_omega <= (1/4)(||q_{lambda r+s/lambda}||_omega+||q_{lambda r-s/lambda}||_omega) <= (1/4)C sqrt(eta)(||lambda r+s/lambda||^2+||lambda r-s/lambda||^2). Step 3 (order-unit-norm bound). For any x,y in V, ||x±y||^2<=(||x||+||y||)^2<=2||x||^2+2||y||^2 (triangle inequality in the order-unit norm + the scalar bound (p+q)^2<=2p^2+2q^2). With x=lambda r, y=s/lambda: ||lambda r+s/lambda||^2+||lambda r-s/lambda||^2 <= 4 lambda^2||r||^2+4 lambda^{-2}||s||^2. Hence ||q_{r,s}||_omega <= C sqrt(eta)(lambda^2||r||^2+lambda^{-2}||s||^2). Step 4 (optimise). If r=0 or s=0 then q_{r,s}=0 and the claim is trivial. Otherwise set lambda^2=||s||/||r||>0: then lambda^2||r||^2+lambda^{-2}||s||^2=||r||||s||+||r||||s||=2||r||||s||, giving ||q_{r,s}||_omega<=2C sqrt(eta)||r||||s||=C' sqrt(eta)||r||||s|| with C'=2C universal dimension-free. Uses node 1.1, GT-square-hole, GT-Pprops, def-near-fixed-algebra, def-square-hole, def jordan-product.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** CRUDE NORM BOUND: ||q_{r,s}|| <= C ||r|| ||s|| (operator/order-unit norm) for r,s in A. PROOF. Here V=B(H)_sa is a JC algebra (GT-bhsa-jc, B(H) a C*-algebra GT-bh-cstar) and each JC algebra is a JB algebra (GT-jc-is-jb), so V=B(H)_sa is a unital JB algebra (as set up in node 1.1); this licenses GT-jb-submult below. q_{r,s}=P(r∘s)-r∘s, so by the triangle inequality in the order-unit norm ||q_{r,s}|| <= ||P(r∘s)|| + ||r∘s|| <= ||P|| ||r∘s|| + ||r∘s|| = (||P||+1)||r∘s||. By GT-Pprops ||P||<=1+C eta<=1+1 (eta<=eta_0<1/4 small, C eta bounded), so ||P||+1<=3 (any universal bound suffices). By the JB-algebra product norm axiom ||r∘s||<=||r|| ||s|| (GT-jb-submult; V=B(H)_sa is a unital JB algebra, since B(H)_sa is a JC algebra (GT-bhsa-jc) and each JC algebra is a JB algebra (GT-jc-is-jb), GT-bh-cstar). Hence ||q_{r,s}||<=(||P||+1)||r||||s|| <= (2+C eta)||r||||s|| <= C'||r||||s|| with C'=2+C eta a universal dimension-free constant. Uses GT-Pprops, GT-jb-submult, GT-bhsa-jc, GT-jc-is-jb, GT-bh-cstar, def-near-fixed-algebra.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** SEMINORM-DOMINATED-BY-NORM: ||z||_omega <= ||z|| for every z in V=B(H)_sa and every state seminorm omega=rho∘Phi (node 1.1). NO use of ||Phi||=1. PROOF. By definition ||z||_omega^2=omega(z^2)=rho(Phi(z^2)). omega is a state on the JB algebra V (node 1.1), so applying the state bound to the self-adjoint element z^2 in V (order unit space V, order unit 1, GT-jb-orderunit-3310): |omega(z^2)|<=||z^2|| (a state on an order-unit space has |omega(a)|<=||a||, GT-state-bounded). Since z^2>=0 and omega is positive, omega(z^2)>=0, so omega(z^2)=|omega(z^2)|<=||z^2||. By the JB norm axiom ||z^2||=||z||^2 (GT-jb-axiom-sq, where V=B(H)_sa is a JC algebra (GT-bhsa-jc) and each JC algebra is a JB algebra (GT-jc-is-jb), so V is a unital JB algebra). Hence ||z||_omega^2=omega(z^2)<=||z||^2, and taking square roots ||z||_omega<=||z||. Uses node 1.1, GT-state-bounded, GT-jb-axiom-sq, GT-jb-orderunit-3310, GT-bhsa-jc, GT-jc-is-jb.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** (HH): ||P(q_{r,s}∘q_{u,v})|| <= C eta ||r||||s||||u||||v|| for r,s,u,v in A. PROOF. Set w:=q_{r,s}∘q_{u,v} in V (q_{r,s},q_{u,v} in V, ∘ closed on V). P(w) is self-adjoint (P:V->V, GT-Pprops). Take the state supremum: ||P(w)||=sup_{rho in S(V)}|rho(P(w))| (GT-sup-states, V order-unit space GT-jb-orderunit-3310). Fix a state rho on V, omega:=rho∘Phi (a state on V, node 1.1). Bridge Phi<->P: |rho(P(w))| <= |rho(Phi(w))| + |rho((P-Phi)(w))| (triangle ineq for scalars). FIRST term: |rho(Phi(w))|=|omega(w)|=|omega(q_{r,s}∘q_{u,v})|. By the Jordan Cauchy-Schwarz inequality for the state omega on the JB algebra V (GT-cauchy-schwarz, 3.6.2(i)): |omega(q_{r,s}∘q_{u,v})| <= omega(q_{r,s}^2)^{1/2} omega(q_{u,v}^2)^{1/2} = ||q_{r,s}||_omega ||q_{u,v}||_omega. By (4.1) (node 1.2): ||q_{r,s}||_omega<=C sqrt(eta)||r||||s|| and ||q_{u,v}||_omega<=C sqrt(eta)||u||||v||, so |omega(w)| <= C^2 eta ||r||||s||||u||||v||. SECOND term (replace Phi by P, the delta cost): |rho((P-Phi)(w))| <= ||(P-Phi)(w)|| (rho a state, |rho(y)|<=||y|| for self-adjoint y=(P-Phi)(w) in V, GT-state-bounded) <= ||P-Phi|| ||w|| = delta ||w|| with delta<=C eta (GT-Pprops). Now ||w||=||q_{r,s}∘q_{u,v}|| <= ||q_{r,s}|| ||q_{u,v}|| (GT-jb-submult) <= (C||r||||s||)(C||u||||v||) (crude bound, node 1.3) = C^2||r||||s||||u||||v||. So second term <= C eta · C^2 ||r||||s||||u||||v|| = C' eta ||r||||s||||u||||v||. COMBINE: |rho(P(w))| <= (C^2+C') eta ||r||||s||||u||||v|| =: C'' eta ||r||||s||||u||||v||, uniformly in rho. Taking the supremum: ||P(q_{r,s}∘q_{u,v})|| <= C'' eta ||r||||s||||u||||v|| with C'' universal dimension-free. Uses node 1.2, node 1.3, node 1.1, GT-cauchy-schwarz, GT-sup-states, GT-state-bounded, GT-jb-submult, GT-Pprops, GT-jb-orderunit-3310.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** (HZ): ||P(q_{r,s}∘z)|| <= C sqrt(eta) ||r||||s||||z|| for r,s in A and z in V=B(H)_sa. PROOF. Here V=B(H)_sa is a JC algebra (GT-bhsa-jc) and each JC algebra is a JB algebra (GT-jc-is-jb), so V is a unital JB algebra (as set up in node 1.1); this licenses the JB Cauchy-Schwarz and submultiplicativity used below. Set w:=q_{r,s}∘z in V. P(w) self-adjoint (P:V->V, GT-Pprops), so ||P(w)||=sup_{rho in S(V)}|rho(P(w))| (GT-sup-states, V order-unit space GT-jb-orderunit-3310). Fix a state rho on V, omega:=rho∘Phi (state on V, node 1.1). Bridge: |rho(P(w))| <= |rho(Phi(w))| + |rho((P-Phi)(w))|. FIRST term: |rho(Phi(w))|=|omega(q_{r,s}∘z)| <= ||q_{r,s}||_omega ||z||_omega (Jordan Cauchy-Schwarz for the state omega on the JB algebra V, GT-cauchy-schwarz 3.6.2(i)). By (4.1) (node 1.2) ||q_{r,s}||_omega<=C sqrt(eta)||r||||s||; by node 1.3.1 ||z||_omega<=||z||. So first term <= C sqrt(eta)||r||||s||·||z|| = C sqrt(eta)||r||||s||||z||. SECOND term: |rho((P-Phi)(w))| <= ||(P-Phi)(w)|| (GT-state-bounded) <= delta||w|| (delta<=C eta, GT-Pprops) and ||w||=||q_{r,s}∘z||<=||q_{r,s}|| ||z|| (GT-jb-submult, V a JB algebra) <= C||r||||s||·||z|| (crude bound node 1.3). So second term <= C eta·C||r||||s||||z|| = C'' eta ||r||||s||||z|| <= C'' sqrt(eta)||r||||s||||z|| (eta<=sqrt(eta) for 0<eta<1). COMBINE: |rho(P(w))| <= (C+C'') sqrt(eta)||r||||s||||z||, uniformly in rho; taking the supremum ||P(q_{r,s}∘z)|| <= C''' sqrt(eta)||r||||s||||z|| with C''' universal dimension-free. Uses node 1.1, node 1.2, node 1.3, node 1.3.1, GT-cauchy-schwarz, GT-sup-states, GT-state-bounded, GT-jb-submult, GT-Pprops, GT-jb-orderunit-3310, GT-bhsa-jc, GT-jc-is-jb.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

