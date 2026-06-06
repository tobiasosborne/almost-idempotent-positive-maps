# Proof Export

## Node 1

**Statement:** The projected product on A=Im P satisfies the approximate Jordan identity ||((a•a)•b)•a - (a•a)•(b•a)|| <= C sqrt(eta) ||a||^3 ||b||, by exact-ambient-Jordan-identity cancellation of the leading term with O(sqrt(eta)) one-hole error terms.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** LEFT REDUCTION. Fix a,b in A=Im P (def near-fixed-algebra). Set p:=P(a^2)=a^2-h_{a,a} in A, where h_{a,a}=a^2-P(a^2) in Ker P (def square-hole; P(h_{a,a})=0 by P^2=P, GT-Pprops). Crude bound ||p||=||P(a^2)||<=||P|| ||a^2||<=(1+C eta)||a||^2<=C||a||^2 (GT-Pprops, GT-jb-submult ||a^2||<=||a||^2). CLAIM: ((a•a)•b)•a = P((a^2∘b)∘a) + E_L with ||E_L|| <= C sqrt(eta)||a||^3||b||. Hence ((a•a)•b)•a = P((a^2∘b)∘a) + O(sqrt(eta)||a||^3||b||). PROOF: a•a=P(a∘a)=P(a^2)=p, so (a•a)•b=P(p∘b). Then ((a•a)•b)•a=P(P(p∘b)∘a). Write l:=h_{p,b}=p∘b-P(p∘b) in Ker P (def square-hole). By P real-linear (GT-Pprops), P(P(p∘b)∘a)=P((p∘b)∘a)-P(l∘a). Using p=a^2-h_{a,a} and bilinearity of ∘ (def jordan-product), (p∘b)∘a=(a^2∘b)∘a-(h_{a,a}∘b)∘a, so P((p∘b)∘a)=P((a^2∘b)∘a)-P((h_{a,a}∘b)∘a). Thus E_L=-P(l∘a)-P((h_{a,a}∘b)∘a). Node 1.1.1 bounds ||P(l∘a)||<=C sqrt(eta)||a||^3||b||; node 1.1.2 bounds ||P((h_{a,a}∘b)∘a)||<=C sqrt(eta)||a||^3||b||. Sum: ||E_L||<=C sqrt(eta)||a||^3||b||. Uses node 1.1.1, node 1.1.2, GT-Pprops, GT-jb-submult, def near-fixed-algebra, def square-hole, def jordan-product.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.1

**Statement:** E1 (left, l-term). l:=h_{p,b}=p∘b-P(p∘b) where p=P(a^2) in A=Im P and b in A (def square-hole, def near-fixed-algebra). (i) l in Ker P: P(l)=P(p∘b)-P^2(p∘b)=P(p∘b)-P(p∘b)=0 since P^2=P (GT-Pprops). (ii) Norm: ||l||<=||p∘b||+||P(p∘b)||<=||p∘b||+(1+C eta)||p∘b||<=C||p∘b||<=C||p||||b||<=C||a||^2||b|| (triangle inequality; GT-Pprops ||P||<=1+C eta; GT-jb-submult ||p∘b||<=||p||||b||; node-1.1 bound ||p||<=C||a||^2). (iii) Apply GT-FI (first insertion) with n=l in Ker P and c=a in A: ||P(l∘a)||<=C sqrt(eta)||l||||a||<=C sqrt(eta)·C||a||^2||b||·||a||=C sqrt(eta)||a||^3||b||. CONCLUSION: ||P(l∘a)||<=C sqrt(eta)||a||^3||b||. Uses GT-FI, GT-Pprops, GT-jb-submult, def square-hole, def near-fixed-algebra.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.1.2

**Statement:** E2 (left, h_{a,a}-term). The product hole h_{a,a}=a∘a-P(a∘a)=a^2-P(a^2) in Ker P (def square-hole). Apply GT-onehole-51 (eq 5.1: ||P((h_{r,s}∘t)∘u)||<=C sqrt(eta)||r||||s||||t||||u||) with r=s=a, t=b, u=a, so h_{r,s}=h_{a,a}: ||P((h_{a,a}∘b)∘a)||<=C sqrt(eta)||a||·||a||·||b||·||a||=C sqrt(eta)||a||^3||b||. CONCLUSION: ||P((h_{a,a}∘b)∘a)||<=C sqrt(eta)||a||^3||b||. Uses GT-onehole-51, def square-hole.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** RIGHT REDUCTION. With a,b,p as in node 1.1, set q:=P(b∘a)=b∘a-h_{b,a} in A, h_{b,a}=b∘a-P(b∘a) in Ker P (def square-hole). Crude bounds ||q||=||P(b∘a)||<=C||a||||b|| and ||h_{b,a}||=||b∘a-P(b∘a)||<=||b∘a||+||P(b∘a)||<=C||a||||b|| (GT-Pprops, GT-jb-submult ||b∘a||<=||a||||b||). CLAIM: (a•a)•(b•a) = P(a^2∘(b∘a)) + E_R with ||E_R|| <= C sqrt(eta)||a||^3||b||. PROOF: a•a=p, b•a=P(b∘a)=q, so (a•a)•(b•a)=P(p∘q). Substitute p=a^2-h_{a,a}, q=b∘a-h_{b,a} and expand by bilinearity (def jordan-product): p∘q=a^2∘(b∘a)-h_{a,a}∘(b∘a)-a^2∘h_{b,a}+h_{a,a}∘h_{b,a}. Apply P (real-linear, GT-Pprops): P(p∘q)=P(a^2∘(b∘a))-P(h_{a,a}∘(b∘a))-P(a^2∘h_{b,a})+P(h_{a,a}∘h_{b,a}). So E_R=-P(h_{a,a}∘(b∘a))-P(a^2∘h_{b,a})+P(h_{a,a}∘h_{b,a}). Node 1.2.1 bounds ||P(h_{a,a}∘(b∘a))||<=C sqrt(eta)||a||^3||b||. For P(a^2∘h_{b,a}) decompose a^2=p+h_{a,a}: P(a^2∘h_{b,a})=P(p∘h_{b,a})+P(h_{a,a}∘h_{b,a}); node 1.2.2 bounds ||P(p∘h_{b,a})||<=C sqrt(eta)||a||^3||b||. Node 1.2.3 bounds ||P(h_{a,a}∘h_{b,a})||<=C eta||a||^3||b||<=C sqrt(eta)||a||^3||b|| (eta<=1), and this term appears twice. Summing: ||E_R||<=C sqrt(eta)||a||^3||b||. Uses node 1.2.1, node 1.2.2, node 1.2.3, GT-Pprops, GT-jb-submult, def near-fixed-algebra, def square-hole, def jordan-product.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** E3 (right, h_{a,a}∘(b∘a) term). h_{a,a}=a^2-P(a^2) in Ker P (def square-hole). Apply GT-onehole-52 (eq 5.2: ||P(h_{r,s}∘(t∘u))||<=C sqrt(eta)||r||||s||||t||||u||) with r=s=a, t=b, u=a, so h_{r,s}=h_{a,a}: ||P(h_{a,a}∘(b∘a))||<=C sqrt(eta)||a||·||a||·||b||·||a||=C sqrt(eta)||a||^3||b||. CONCLUSION: ||P(h_{a,a}∘(b∘a))||<=C sqrt(eta)||a||^3||b||. Uses GT-onehole-52, def square-hole.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.2

**Statement:** E4 (right, p∘h_{b,a} term). p=P(a^2) in A=Im P with ||p||<=C||a||^2 (node 1.1); h_{b,a}=b∘a-P(b∘a) in Ker P with ||h_{b,a}||<=C||a||||b|| (node 1.2, def square-hole). Since ∘ is commutative (def jordan-product), p∘h_{b,a}=h_{b,a}∘p. Apply GT-FI (first insertion) with n=h_{b,a} in Ker P and c=p in A: ||P(h_{b,a}∘p)||<=C sqrt(eta)||h_{b,a}||||p||<=C sqrt(eta)·C||a||||b||·C||a||^2=C sqrt(eta)||a||^3||b||. Hence ||P(p∘h_{b,a})||<=C sqrt(eta)||a||^3||b||. Uses GT-FI, def square-hole, def near-fixed-algebra, def jordan-product.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.3

**Statement:** E5 (right, two-hole term h_{a,a}∘h_{b,a}). h_{a,a}=a^2-P(a^2)=-q_{a,a} and h_{b,a}=b∘a-P(b∘a)=-q_{b,a}, where q_{r,s}=P(r∘s)-r∘s (def square-hole). So h_{a,a}∘h_{b,a}=q_{a,a}∘q_{b,a}. Apply GT-HH (two-hole) with (r,s)=(a,a) and (u,v)=(b,a): ||P(q_{a,a}∘q_{b,a})||<=C eta||a||·||a||·||b||·||a||=C eta||a||^3||b||. Since eta<=eta_0<=1 we have eta<=sqrt(eta), so ||P(h_{a,a}∘h_{b,a})||<=C eta||a||^3||b||<=C sqrt(eta)||a||^3||b||. CONCLUSION: ||P(h_{a,a}∘h_{b,a})||<=C eta||a||^3||b||<=C sqrt(eta)||a||^3||b||. Uses GT-HH, def square-hole.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** CANCELLATION + ASSEMBLY. CLAIM: P((a^2∘b)∘a)=P(a^2∘(b∘a)) EXACTLY, hence ||((a•a)•b)•a-(a•a)•(b•a)|| <= C sqrt(eta)||a||^3||b||. PROOF of cancellation: node 1.3.1 proves the symmetric ambient Jordan identity (a^2∘b)∘a=a^2∘(b∘a) as an exact identity of elements of B(H)_sa (derived from GT-jordan-identity + commutativity GT-jordan-product). Applying the well-defined real-linear map P to both sides of this exact equality of elements of B(H)_sa gives P((a^2∘b)∘a)=P(a^2∘(b∘a)). ASSEMBLY: by node 1.1, ((a•a)•b)•a=P((a^2∘b)∘a)+E_L; by node 1.2, (a•a)•(b•a)=P(a^2∘(b∘a))+E_R; with ||E_L||,||E_R||<=C sqrt(eta)||a||^3||b||. Subtracting and using the cancellation P((a^2∘b)∘a)=P(a^2∘(b∘a)): ((a•a)•b)•a-(a•a)•(b•a)=E_L-E_R, so ||((a•a)•b)•a-(a•a)•(b•a)||<=||E_L||+||E_R||<=C sqrt(eta)||a||^3||b||. This is exactly the contract (JB4, def eps-jb-algebra). Uses node 1.1, node 1.2, node 1.3.1, GT-jordan-identity, GT-jordan-product, def near-fixed-algebra, def jordan-product.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.3.1

**Statement:** SYMMETRIC AMBIENT JORDAN IDENTITY (exact). CLAIM: in B(H)_sa with the ambient Jordan product ∘ (def jordan-product), (a^2∘b)∘a=a^2∘(b∘a) for all a,b, where a^2=a∘a. PROOF: GT-jordan-identity is HOS eq (2.18): a∘(b∘a^2)=(a∘b)∘a^2 (an exact identity valid for the special Jordan product on any associative algebra, in particular B(H)). The product ∘ is commutative: a∘b=b∘a (GT-jordan-product, since (1/2)(ab+ba)=(1/2)(ba+ab)). Apply commutativity to BOTH sides of (2.18): LHS a∘(b∘a^2)=(b∘a^2)∘a=(a^2∘b)∘a (inner b∘a^2=a^2∘b by commutativity, then outer a∘X=X∘a); RHS (a∘b)∘a^2=a^2∘(a∘b)=a^2∘(b∘a) (outer commutativity, then inner a∘b=b∘a). Therefore (a^2∘b)∘a=a^2∘(b∘a), an EXACT equality of elements of B(H)_sa. (This is one commutativity-relabeling step from (2.18), no error term.) Uses GT-jordan-identity, GT-jordan-product, def jordan-product.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

