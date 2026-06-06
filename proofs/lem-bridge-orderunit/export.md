# Proof Export

## Node 1

**Statement:** The near-fixed algebra A=Im P, with unit 1 and inherited cone A_+ = A cap B(H)_+, is an order-unit space, and its order-unit norm ||a||_ou = inf{t>0: -t1<=a<=t1} coincides exactly with the operator norm on A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** 1 in A and A is a real linear subspace of V=B(H)_sa. By GT-Pprops, P(1)=1, so 1=P(1) in Im P=A (def-near-fixed-algebra), giving 1 in A. By GT-Pprops, P is real-linear on B(H)_sa, so its range A=Im P is a real linear subspace of V=B(H)_sa (image of a real-linear map is a real subspace). Thus A is a real linear subspace of V containing the unit 1. Uses GT-Pprops, def-near-fixed-algebra.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** 1 is an order unit for (A,A_+): (i) cone-membership 1 in A_+ holds by node 1.2.1; (ii) dominance — for every a in A, -||a||1 <= a <= ||a||1 in V, since V=B(H)_sa is a unital JB algebra (GT-bhsa-jc + GT-jc-is-jb) whose operator norm equals its order-unit norm (GT-jb-orderunit-3310), and the order on A is inherited from V (def-near-fixed-algebra, node 1.1). Both clauses give: 1 is an order unit for A.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

#### Node 1.2.1

**Statement:** 1 in A_+: 1 in A since P(1)=1 (GT-Pprops) and A=Im P (def-near-fixed-algebra). 1 in V_+ since V=B(H)_sa is a complete order-unit space with order unit 1 (GT-jb-orderunit-3310) and an order unit lies in the cone (GT-orderunit-def: e in A^+). Hence 1 in A cap V_+ = A_+ (def-near-fixed-algebra, cone inherited exactly).

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** A_+=A cap V_+ is Archimedean. We show (A,A_+,1) satisfies the Archimedean axiom of GT-orderunit-def: if na<=_A 1 for all n in N then a<=_A 0. Since the order on A is inherited (def-near-fixed-algebra; A subseteq V by node 1.1), na<=_A 1 is equivalent to na<=_V 1 in V. By GT-jb-orderunit-3310 V is a complete order-unit space, hence (GT-orderunit-def) V is itself Archimedean: na<=_V 1 for all n in N implies a<=_V 0, i.e. a in V_+ with -a in V_+... more precisely a<=_V 0 means -a in V_+. Since a in A, a<=_V 0 gives -a in A cap V_+=A_+, i.e. a<=_A 0. (Equivalently, the same conclusion follows because V_+ is norm-closed: GT-jb-cone-closed-335 gives (tilde-V)_+ closed in tilde-V, and V_+=V cap (tilde-V)_+ is closed in V; if a+eps 1 in V_+ for all eps>0 then letting eps->0, a=lim(a+eps 1) in V_+. Both routes use only inherited order.) Hence A is Archimedean. Uses node 1.1, node 1.2, GT-jb-orderunit-3310, GT-orderunit-def, GT-jb-cone-closed-335, def-near-fixed-algebra.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** (A,A_+,1) is an order-unit space. By GT-orderunit-def, a real vector space with a proper convex cone and a distinguished element is an order-unit space iff that element is an order unit AND the space is Archimedean. We verify the hypotheses: (i) A is a real vector space with the inherited cone A_+=A cap V_+, which is a proper convex cone: convex and closed under R_+ scaling since V_+ is (intersection of the subspace A with the convex cone V_+), and proper (A_+ cap (-A_+) = A cap V_+ cap (-V_+) = A cap {0} = {0}) because V_+ is proper in V (V an order-unit space, GT-jb-orderunit-3310 + GT-orderunit-def); (ii) 1 in A_+ and 1 is an order unit for A by node 1.2; (iii) A is Archimedean by node 1.3. By GT-orderunit-def these are exactly the defining conditions, so (A,A_+,1) is an order-unit space (def-order-unit-space). Uses node 1.1, node 1.2, node 1.3, GT-orderunit-def, GT-jb-orderunit-3310, def-order-unit-space, def-near-fixed-algebra.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** ||a||_{ou,A} = ||a||_{B(H)} for all a in A. By node 1.4, (A,A_+,1) is an order-unit space, so by GT-orderunit-def its order-unit norm is ||a||_{ou,A}=inf{t>0: -t1<=_A a<=_A t1}. By node 1.1 A subseteq V and the order is inherited (def-near-fixed-algebra), so for a in A and t>0, -t1<=_A a<=_A t1 iff -t1<=_V a<=_V t1; hence the two infima are over the SAME set of t, giving ||a||_{ou,A}=inf{t>0:-t1<=_V a<=_V t1}=||a||_{ou,V}. By GT-jb-orderunit-3310, V=B(H)_sa is a unital JB algebra whose order norm equals the given operator norm, i.e. ||b||_{ou,V}=||b||_{B(H)} for all b in V. Therefore ||a||_{ou,A}=||a||_{ou,V}=||a||_{B(H)} for all a in A. Uses node 1.1, node 1.4, GT-jb-orderunit-3310, GT-orderunit-def, def-order-unit-space, def-near-fixed-algebra.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

