# Proof Export

## Node 1

**Statement:** For unital positive Phi with ||Phi^2-Phi|| <= eta <= eta_0, P=theta(2Phi-1), A=Im P, if Phi admits a faithful state omega with ||omega∘Phi-omega|| <= eta and density rho_omega >= lambda 1 (lambda>0), then for all a,b in A the ambient product hole satisfies ||a∘b-P(a∘b)|| = ||h_{a,b}|| <= C (eta/lambda) ||a|| ||b||, with universal dimension-free C.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** SPECTRAL SPLIT + q^- BOUND. q_a=P(a^2)-a^2 is self-adjoint in Ker P (GT-hyp). By functional calculus (node 1.1.1) split q_a=q^+ - q^- with q^+,q^- >= 0, q^+ o q^- = 0, and ||q_a||=max(||q^+||,||q^-||). By GT-squarehole (instantiate r:=a): q_a >= -C eta ||a||^2 1. Hence 0 <= q^- <= C eta ||a||^2 1 (GT-orderunit-def: -c1<=q_a means q^-<=c1), so ||q^-|| <= C eta ||a||^2 (GT-sup-states monotonicity, 0<=q^-<=C eta||a||^2 1).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** FUNCTIONAL CALCULUS SPLIT. V=B(H)_sa is a unital JB algebra. For self-adjoint q=q_a, by GT-jb-spectral C(q) is isometrically Jordan-isomorphic (phi) to C(Sp q), phi(q)=iota. Set q^+ = phi^{-1}(t^+), q^- = phi^{-1}(t^-) where t^+=max(t,0), t^-=max(-t,0) on Sp q. Then q^+,q^- in C(q), q^+,q^- >= 0 (GT-jb-positive-spectrum: pointwise nonneg => positive), q^+ - q^- = phi^{-1}(t)=q, and q^+ o q^- = phi^{-1}(t^+ t^-)=0 (t^+ t^- =0 pointwise). Sp q = Sp(q^+) cup (-Sp(q^-)) (disjoint supports), so by GT-norm-spectral ||q||=sup|Sp q|=max(sup Sp q^+, sup Sp q^-)=max(||q^+||,||q^-||) (q^+,q^->=0 so their norms equal their max eigenvalues).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** EXPECTATION BOUND |omega(q_a)| <= C eta ||a||^2. omega(q_a)=omega(P(a^2))-omega(a^2). Write omega(P(a^2))=omega(Phi(a^2)) + omega((P-Phi)(a^2)). By GT-Pprops delta=||P-Phi||<=C eta; omega is a state so |omega(y)|<=||y|| (GT-state-bounded); ||a^2||=||a||^2 (GT-bh-cstar). So |omega((P-Phi)(a^2))| <= ||(P-Phi)(a^2)|| <= delta||a^2|| <= C eta||a||^2. Also omega(Phi(a^2))=(omega o Phi)(a^2)=omega(a^2)+((omega o Phi)-omega)(a^2), and |((omega o Phi)-omega)(a^2)| <= ||omega o Phi - omega||*||a^2|| <= eta||a||^2 (GT-hyp). Hence omega(P(a^2))=omega(a^2)+r with |r|<=C eta||a||^2, so |omega(q_a)|=|r|<=C eta||a||^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** omega(q^+) <= C eta ||a||^2. Since q_a=q^+-q^- (1.1), omega(q^+)=omega(q_a)+omega(q^-). |omega(q_a)|<=C eta||a||^2 (1.2). q^->=0 and omega a state, so 0<=omega(q^-)<=||q^-|| (GT-state-bounded / GT-sup-states) <= C eta||a||^2 (1.1). Hence omega(q^+)<=C eta||a||^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** FAITHFULNESS UPGRADE ||q^+|| <= C (eta/lambda) ||a||^2. For any x>=0: omega(x)=Tr(rho_omega x) (GT-state-density). By node 1.4.1, Tr(rho_omega x) >= lambda Tr(x); by node 1.4.2, Tr(x) >= ||x||. So omega(x) >= lambda||x|| for x>=0. Apply to x=q^+ >= 0 (the positive part from node 1.1, a transitive dependency of this node via 1.3 whose declared deps are [1.1,1.2]; 1.1 is thus a recorded validated ancestor of 1.4): lambda||q^+|| <= omega(q^+) <= C eta||a||^2 (node 1.3), so ||q^+|| <= C (eta/lambda)||a||^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.1

**Statement:** Tr(rho_omega x) >= lambda Tr(x) for x>=0. By GT-hyp rho_omega>=lambda1, so rho_omega-lambda1>=0 (GT-orderunit-def). By GT-trace-psd (self-duality of the positive cone of L(H): a in J^+ iff tr(ab)>=0 for all b in J^+), with a:=rho_omega-lambda1>=0 and b:=x>=0, Tr((rho_omega-lambda1)x)>=0, i.e. Tr(rho_omega x) >= lambda Tr(x).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.4.2

**Statement:** Tr(x) >= ||x|| for x>=0. By GT-eigen-nonneg, x>=0 means x self-adjoint with all eigenvalues mu_i>=0. By GT-norm-spectral ||x||=sup|Sp x|=max_i mu_i (mu_i>=0). Tr(x)=sum_i mu_i >= max_i mu_i = ||x|| (all summands nonneg).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** DIAGONAL ||q_a|| <= C (eta/lambda)||a||^2. ||q_a||=max(||q^+||,||q^-||) (1.1). ||q^+||<=C(eta/lambda)||a||^2 (1.4). ||q^-||<=C eta||a||^2 (1.1) <= C(eta/lambda)||a||^2 since lambda<=1 (GT-hyp). Hence ||q_a||<=C(eta/lambda)||a||^2.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** POLARISATION => the contract. h_{a,b}=a∘b-P(a∘b)=-q_{a,b} (GT-hyp/def-square-hole) is symmetric bilinear in (a,b), with diagonal h_{a,a}=-q_a, so ||h_{a,a}||=||q_a||<=C(eta/lambda)||a||^2 (1.5). For t>0, h_{a,b}=(1/(4t))(h_{a+tb,a+tb}-h_{a-tb,a-tb}). Hence ||h_{a,b}|| <= (1/(4t))(||q_{a+tb}||+||q_{a-tb}||) <= (C eta/(4 t lambda))(||a+tb||^2+||a-tb||^2) <= (C eta/(2 t lambda))(||a||+t||b||)^2 (triangle inequality on the norm). For a,b!=0 choose t=||a||/||b||: (||a||+t||b||)^2=4||a||^2 and 1/(2t)=||b||/(2||a||), giving ||h_{a,b}|| <= C(eta/lambda)||a|| ||b|| (the zero cases are trivial). This is the contract.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

