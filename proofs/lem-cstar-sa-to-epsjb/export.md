# Proof Export

## Node 1

**Statement:** If F is a unital eta-idempotent UCP map on B(H) (||F^2-F||_cb <= eta < 1/4), Ftilde=theta(2F-1), and B=Im Ftilde carries the Choi-Effros product X*Y=Ftilde(XY) (Kitaev's extended O(eta)-C*-algebra), then B_sa with the symmetrized product X∘Y=(1/2)(X*Y+Y*X) is an O(eta)-eps-JB order-unit algebra with universal dimension-free constants.

**Type:** claim

**Inference:** assumption

**Status:** pending

**Taint:** unresolved

### Node 1.1

**Statement:** SETUP + EASY AXIOMS (exact order/unit/involution/commutativity). By GT-kitaev-thalmostidemp applied to F (=Kitaev Phi), B=Im Ftilde with X*Y=Ftilde(XY) is an extended O(eta)-C*-algebra (def-eps-cstar-algebra) with eps=O(eta): ax_prodnorm ||X*Y||<=(1+Ceta)||X||||Y||, ax_assoc, ax_C* ||X^dag*X||>=(1-Ceta)||X||^2, EXACT involution (X*Y)^dag=Y^dag*X^dag and ||X^dag||=||X||, EXACT unit X*1=X=1*X, ||1||=1, 1^dag=1, all with universal dimension-free constants. B_sa:={X in B: X=X^dag} is a real linear subspace of B(H)_sa (def-self-adjoint-part), since B is *-closed (Ftilde(X^dag)=Ftilde(X)^dag, GT-tildePhi-props) and the involution is conjugate-linear. CLOSURE under o: for X,Y in B_sa, XoY=(1/2)(X*Y+Y*X); (XoY)^dag=(1/2)((X*Y)^dag+(Y*X)^dag)=(1/2)(Y^dag*X^dag+X^dag*Y^dag)=(1/2)(Y*X+X*Y)=XoY (ax_* exact involution, X=X^dag, Y=Y^dag), so XoY in B_sa. UNIT (exact): 1 in B_sa (1^dag=1, 1 in B); 1oX=(1/2)(1*X+X*1)=(1/2)(X+X)=X exactly (exact unit). COMMUTATIVITY (exact): XoY=(1/2)(X*Y+Y*X)=(1/2)(Y*X+X*Y)=YoX exactly (def-jordan-product). The ORDER, UNIT, NORM on B_sa are inherited EXACTLY from B(H)_sa (operator norm, PSD cone); only the product o carries defect. Uses GT-kitaev-thalmostidemp, GT-tildePhi-props, def-eps-cstar-algebra, def-self-adjoint-part, def-jordan-product.

**Type:** claim

**Inference:** assumption

**Status:** pending

**Taint:** unresolved

### Node 1.2

**Statement:** JB1 (approximate submultiplicativity): ||XoY|| <= (1+Ceta)||X||||Y|| for X,Y in B_sa. By def-jordan-product XoY=(1/2)(X*Y+Y*X). Triangle inequality: ||XoY|| <= (1/2)(||X*Y||+||Y*X||). By ax_prodnorm (def-eps-cstar-algebra, GT-kitaev-thalmostidemp, eps=O(eta)): ||X*Y||<=(1+Ceta)||X||||Y|| and ||Y*X||<=(1+Ceta)||Y||||X||. Hence ||XoY|| <= (1/2)((1+Ceta)||X||||Y||+(1+Ceta)||X||||Y||)=(1+Ceta)||X||||Y||. C universal dimension-free (the ax_prodnorm constant). This is JB1 (def-eps-jb-algebra) with eps=Ceta. Uses GT-kitaev-thalmostidemp, def-eps-cstar-algebra, def-jordan-product, def-eps-jb-algebra.

**Type:** claim

**Inference:** assumption

**Status:** pending

**Taint:** unresolved

### Node 1.3

**Statement:** JB2 (square-norm lower bound): ||XoX|| >= (1-Ceta)||X||^2 for X in B_sa. Since X=X^dag (X in B_sa) and o symmetric: XoX=(1/2)(X*X+X*X)=X*X=X^dag*X (def-jordan-product, X=X^dag). By ax_C* (def-eps-cstar-algebra, GT-kitaev-thalmostidemp, eps=O(eta)): ||X^dag*X|| >= (1-Ceta)||X||^2. Hence ||XoX||=||X^dag*X|| >= (1-Ceta)||X||^2. C universal dimension-free (the ax_C* constant). This is JB2 (def-eps-jb-algebra) with eps=Ceta. Uses GT-kitaev-thalmostidemp, def-eps-cstar-algebra, def-jordan-product, def-eps-jb-algebra.

**Type:** claim

**Inference:** assumption

**Status:** pending

**Taint:** unresolved

### Node 1.4

**Statement:** JB3 (approximate positivity of squares, ORDER inequality): XoX >= -Ceta||X||^2 1 for X in B_sa. This needs the CONCRETE UCP realisation, NOT ax_C* (which is only a NORM bound). STEP 1: XoX=X*X=Ftilde(X X)=Ftilde(X^2) (def-jordan-product with X=X^dag, X*X=Ftilde(XX); X^2 is the ordinary operator square, self-adjoint, =X^dag X). STEP 2 (split off F): Ftilde(X^2)=F(X^2)+(Ftilde-F)(X^2). STEP 3 (F-positivity, the crux): F is UCP hence POSITIVE (order-preserving on self-adjoints); X self-adjoint => X^2=X^dag X >= 0 in B(H); so F(X^2) >= 0 (GT-ucp-positive-square: F(X^dag X)>=0 since F(X^dag)F(X)<=F(X^dag X) and more directly positivity of F). [Ftilde is NOT positive in general (Kitaev :363), so we MUST route through F.] STEP 4 (error bound): ||(Ftilde-F)(X^2)|| <= ||Ftilde-F||_cb ||X^2|| <= O(eta)||X^2|| (GT-tildePhi-props ||Ftilde-F||_cb<=O(eta); ||.||<=||.||_cb on the single argument X^2). By GT-jb-normsquare ||X^2||=||X||^2 (B(H)_sa JB algebra, X self-adjoint). So ||(Ftilde-F)(X^2)|| <= Ceta||X||^2. STEP 5 (assemble in the order): write E:=(Ftilde-F)(X^2), a self-adjoint element with ||E||<=Ceta||X||^2. By GT-orderunit-def the order-unit/operator norm satisfies E >= -||E|| 1 >= -Ceta||X||^2 1. Hence XoX=F(X^2)+E >= 0 + (-Ceta||X||^2 1)=-Ceta||X||^2 1. This is JB3 (def-eps-jb-algebra) with eps=Ceta, C universal dimension-free. Uses GT-ucp-positive-square, GT-tildePhi-props, GT-jb-normsquare, GT-orderunit-def, GT-hyp, def-jordan-product, def-eps-jb-algebra.

**Type:** claim

**Inference:** assumption

**Status:** pending

**Taint:** unresolved

### Node 1.5

**Statement:** JB4 (approximate Jordan identity --- the O(eta) crux, NOT O(sqrt eta)): for X,Y in B_sa, ||((XoX)oY)oX - (XoX)o(YoX)|| <= Ceta||X||^3||Y||, C universal dimension-free. Set a:=X (self-adjoint), so aoa=(1/2)(a*a+a*a)=a*a=:P2 (def-jordan-product, a in B_sa). Expanding every o into the symmetrized * product (XoY=(1/2)(X*Y+Y*X), def-jordan-product), the defect D:=((aoa)oY)oa-(aoa)o(Yoa) is the fixed (1/4)-integer combination of EIGHT fully-parenthesized *-monomials in the letters (a,a,Y,a) computed in node 1.5.1. By node 1.5.1 these eight monomials group into FOUR pairs (P_w - Q_w), one per 4-letter word w in {aaYa, Yaaa, aaaY, aYaa}, each pair being two DIFFERENT parenthesizations of the SAME *-word, with coefficient +1/4: D=(1/4)*sum_w (P_w - Q_w). [At eps=0 the * product is exactly associative, all parenthesizations of a word coincide, each P_w-Q_w=0, and D=0 --- this is exactly the EXACT special Jordan identity HOS (2.18), GT-jordan-identity, the eps=0 limit. So the ONLY source of nonzero D is eps-C* NON-associativity.] By node 1.5.2 (Reassociation Lemma) each ||P_w-Q_w|| <= Ceta*(product of the four letter-norms of w)=Ceta||a||^3||Y|| (each word has exactly three a's and one Y). Hence ||D|| <= (1/4)*4*Ceta||a||^3||Y||=Ceta||X||^3||Y|| (node 1.5.3 assembles). This is JB4 (def-eps-jb-algebra) with eps=Ceta. The O(eta) (not O(sqrt eta)) rate comes from ax_assoc being O(eta). Uses node 1.5.1, node 1.5.2, node 1.5.3, GT-jordan-identity, def-jordan-product, def-eps-jb-algebra.

**Type:** claim

**Inference:** assumption

**Status:** pending

**Taint:** unresolved

#### Node 1.5.1

**Statement:** EXPANSION of the Jordan defect into a (1/4)-combination of eight *-monomials, grouped as four same-word pairs. Let * be the eps-C* product on B and {U,V}:=(1/2)(U*V+V*U)=UoV the symmetrized product (def-jordan-product); * is bilinear (def-eps-cstar-algebra) so {.,.} is bilinear. For a=X in B_sa, aoa=a*a (a=a^dag, the two summands coincide). The defect D:=((aoa)oY)oa-(aoa)o(Yoa)={{a*a,Y},a}-{a*a,{Y,a}}. Expanding by bilinearity of {.,.} into fully-parenthesized *-monomials gives EXACTLY (verified by exact symbolic expansion): D = (1/4)[ ((a*a)*Y)*a + (Y*(a*a))*a - (Y*a)*(a*a) - (a*Y)*(a*a) - (a*a)*(Y*a) - (a*a)*(a*Y) + a*((a*a)*Y) + a*(Y*(a*a)) ]. These eight monomials, read by their leaves left-to-right, fall into FOUR underlying *-words, each appearing TWICE with opposite signs (so each word's coefficient-sum is 0): word aaYa: +((a*a)*Y)*a, -(a*a)*(Y*a); word Yaaa: +(Y*(a*a))*a, -(Y*a)*(a*a); word aaaY: +a*((a*a)*Y), -(a*a)*(a*Y); word aYaa: +a*(Y*(a*a)), -(a*Y)*(a*a). Hence D=(1/4)[ (P_{aaYa}-Q_{aaYa})+(P_{Yaaa}-Q_{Yaaa})+(P_{aaaY}-Q_{aaaY})+(P_{aYaa}-Q_{aYaa}) ], where for each word w, P_w and Q_w are two DIFFERENT parenthesizations of the SAME four-letter *-word w (each word: three a's, one Y). [Sanity: in any exactly-associative algebra P_w=Q_w for every w, so D=0; this is the EXACT special Jordan identity, GT-jordan-identity HOS (2.18): a o (b o a^2)=(a o b) o a^2, equivalently the symmetric form ((aoa)oY)oa=(aoa)o(Yoa), at eps=0.] Uses GT-jordan-identity, def-jordan-product, def-eps-cstar-algebra.

**Type:** claim

**Inference:** assumption

**Status:** pending

**Taint:** unresolved

#### Node 1.5.2

**Statement:** REASSOCIATION LEMMA. In an eps-C* algebra (def-eps-cstar-algebra, eps<=1) let Z_1,...,Z_n in B and let T, T' be ANY two full parenthesizations of the *-word Z_1*...*Z_n. Then ||T - T'|| <= K_n eps prod_{i=1}^n ||Z_i||, with K_n=(n-1)(n-2) a universal dimension-free constant (independent of H). PROOF by induction on n. n<=2: only one parenthesization, T=T', bound 0. Inductive step: it suffices (triangle inequality) to bound ||T - L|| where L:=L(Z_1,...,Z_n):=(...((Z_1*Z_2)*Z_3)...*Z_n) is the LEFT-NESTED form, since then ||T-T'||<=||T-L||+||L-T'||. Write T=A*B where A is a parenthesization of Z_1..Z_k and B of Z_{k+1}..Z_n (1<=k<=n-1). By ax_prodnorm (def-eps-cstar-algebra) and induction, ||A||<=(1+eps)^{k-1}prod_{i<=k}||Z_i|| and similarly ||B||; for eps<=1, (1+eps)^{m}<=2^m, absorb into K_n. STEP 1: replace A by its left-nested L_A and B by L_B: ||A*B - L_A*L_B|| <= ||(A-L_A)*B|| + ||L_A*(B-L_B)|| <= (1+eps)(||A-L_A||||B|| + ||L_A||||B-L_B||) (ax_prodnorm) <= (1+eps)(K_k eps prod_{i<=k}||Z_i|| * ||B|| + ||L_A|| * K_{n-k} eps prod_{i>k}||Z_i||) (induction on A,B) <= C' eps prod_i ||Z_i|| (all factor-norm products telescope to prod_i||Z_i|| times bounded (1+eps)-powers). STEP 2: L_A*L_B with L_A left-nested in Z_1..Z_k and L_B left-nested in Z_{k+1}..Z_n; reduce L_A*L_B to the global left-nested L by repeatedly applying ax_assoc at the ROOT: L_A*(W*Z_n)=(L_A*W)*Z_n + assoc-error, where ||assoc(U,V,Z)||<=eps||U||||V||||Z|| (ax_assoc) and each U,V,Z is a *-product of a contiguous block of Z_1..Z_n, so ||U||||V||||Z||<=(1+eps)^{n-2}prod_i||Z_i||. The number of such root-rotations to fully left-nest is <= (n-1)(n-2)/2 (associahedron diameter bound). Summing: ||L_A*L_B - L|| <= ((n-1)(n-2)/2)(1+eps)^{n-2} eps prod_i||Z_i||. STEP 1+2 give ||T-L||<=K_n eps prod_i||Z_i|| with K_n universal (absorbing the bounded (1+eps)^{<=n} factors, eps<=1). [n=4 case used in JB4: K_4 a fixed universal constant; prod=||a||^3||Y||.] Uses GT-eps-assoc, GT-kitaev-thalmostidemp, def-eps-cstar-algebra.

**Type:** claim

**Inference:** assumption

**Status:** pending

**Taint:** unresolved

#### Node 1.5.3

**Statement:** ASSEMBLY of JB4. By node 1.5.1, D=(1/4)sum_{w in {aaYa,Yaaa,aaaY,aYaa}}(P_w - Q_w), where for each word w, P_w and Q_w are two parenthesizations of the SAME *-word w (three a's, one Y). By node 1.5.2 (Reassociation Lemma with n=4, Z-letters the three a's and one Y in the order of w), ||P_w - Q_w|| <= K_4 eta prod(letter-norms of w) = K_4 eta ||a||^3||Y|| for each of the four words (the K_4 eta with eps=O(eta), GT-eps-assoc; K_4 universal dimension-free). [The eps-C* eps is O(eta) by GT-kitaev-thalmostidemp; here eta<1/4<1 by GT-hyp so eps<=1 as the lemma requires.] Therefore ||D|| <= (1/4) sum_{w}||P_w - Q_w|| <= (1/4)*4*K_4 eta||a||^3||Y|| = K_4 eta||X||^3||Y|| =: C eta||X||^3||Y||, with C=K_4 universal dimension-free. Since D=((XoX)oY)oX-(XoX)o(YoX), this is JB4 with eps=Ceta. Uses node 1.5.1, node 1.5.2, GT-eps-assoc, GT-kitaev-thalmostidemp, GT-hyp, def-eps-jb-algebra.

**Type:** claim

**Inference:** assumption

**Status:** pending

**Taint:** unresolved

### Node 1.6

**Statement:** NORM (order-unit norm = operator norm on B_sa). B_sa is a real linear subspace of B(H)_sa (node 1.1) containing 1, with the inherited PSD cone (B_sa)_+ = B_sa cap B(H)_+ and inherited order. By GT-bhsa-jc + GT-jc-is-jb, V:=B(H)_sa is a unital JB algebra; by GT-jb-orderunit-3310 V is a complete order-unit space with order unit 1 whose order norm EQUALS the given operator norm. (i) 1 is an order unit for B_sa: for X in B_sa, -||X|| 1 <= X <= ||X|| 1 in V (GT-orderunit-def applied in V, order norm=operator norm), and since the order is inherited this holds in B_sa. (ii) B_sa is Archimedean (inherited from V: if nX <= 1 for all n then X<=0 in V hence in B_sa, V an order-unit space, GT-orderunit-def). (iii) the inherited cone is proper and convex (intersection of subspace with proper convex cone V_+). So (B_sa,(B_sa)_+,1) is an order-unit space (def-self-adjoint-part). Its order-unit norm ||X||_ou=inf{t>0:-t1<=X<=t1} (GT-orderunit-def) uses the SAME inherited order as V, so ||X||_ou=||X||_{ou,V}=||X||_{B(H)} (GT-jb-orderunit-3310). Hence the eps-JB order-unit norm on B_sa is EXACTLY the operator norm; in particular JB1-JB4 (stated in operator norm) hold in the order-unit norm. Uses node 1.1, GT-bhsa-jc, GT-jc-is-jb, GT-jb-orderunit-3310, GT-orderunit-def, def-self-adjoint-part, def-eps-jb-algebra.

**Type:** claim

**Inference:** assumption

**Status:** pending

**Taint:** unresolved

### Node 1.7

**Statement:** CONCLUSION (= contract). By node 1.6, (B_sa,(B_sa)_+,1) is a finite-dimensional real order-unit space (finite-dim: H finite-dim => B(H)_sa finite-dim => B_sa a subspace) with order-unit norm=operator norm. By node 1.1 the symmetrized product o (def-jordan-product) is commutative and unital EXACTLY and maps B_sa x B_sa -> B_sa. By nodes 1.2,1.3,1.4,1.5 the four eps-JB axioms hold with a COMMON eps=Ceta (max of the four universal constants; eta<1/4 by GT-hyp keeps (1+Ceta) bounded): JB1 ||XoY||<=(1+Ceta)||X||||Y||; JB2 ||XoX||>=(1-Ceta)||X||^2; JB3 XoX>=-Ceta||X||^2 1; JB4 ||((XoX)oY)oX-(XoX)o(YoX)||<=Ceta||X||^3||Y||. All constants universal/dimension-free (GT-kitaev-thalmostidemp ax_prodnorm/ax_C*/ax_assoc are Kitaev's universal O(eta) bounds; the JB3 constant is from ||Ftilde-F||_cb<=O(eta)). Therefore B_sa with o is an O(eta)-eps-JB order-unit algebra with universal dimension-free constants (def-eps-jb-algebra) --- exactly the contract. Uses node 1.1, node 1.2, node 1.3, node 1.4, node 1.5, node 1.6, GT-hyp, GT-kitaev-thalmostidemp, def-eps-jb-algebra, def-jordan-product, def-self-adjoint-part.

**Type:** claim

**Inference:** assumption

**Status:** pending

**Taint:** unresolved

