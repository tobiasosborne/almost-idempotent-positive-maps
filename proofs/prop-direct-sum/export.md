# Proof Export

## Node 1

**Statement:** If B=⊕_r B_r (order-unit norm = max_r) and each factor has an exact-adjoint coboundary splitting with constant K_r, then B has one with constant max_r K_r + 1, independent of the number of summands (off-block components recovered by P_r f(e_r,·), with no sum over r); valid for adjoint/block-respecting modules.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.1

**Statement:** SETUP / FRAME. By GT-hyp, B = direct-sum over r=1..m of unital JB-algebras B_r (def-jb-algebra), with coordinatewise Jordan product and order-unit norm ||x|| = max_r ||x_r||. Each B_r is the ideal summand U_{e_r}B for a central idempotent e_r of B: by GT-central-idempotent-summand a central idempotent e in a unital Jordan algebra makes U_e B a direct summand and an ideal, so the e_r are the central units of the summands; e_r acts as the identity on its own block B_r (e_r circ y = y for y in B_r) and the coordinatewise product makes B_r an ideal annihilating the other blocks (y in B_s, s != r => e_r circ y = 0). Let P_r: B -> B_r be the coordinate projection. The cochain module is the ADJOINT module (def-jordan-coboundary): the action is left Jordan multiplication a.m := a circ m, and the Jordan coboundary is (d^1 h)(a,b) = a circ h(b) + h(a) circ b - h(a circ b). By GT-hyp (module restriction) all modules are adjoint/block-respecting, so no Peirce-1/2 mixing occurs; arbitrary modules are excluded. By GT-jb-is-order-unit-space each unital JB-algebra (B_r and B) is a complete order unit space with order unit the identity and order norm equal to the given norm, so by GT-orderunit-norm-formula the norm is ||a|| = inf{lambda>0: -lambda*1 <= a <= lambda*1}; by GT-jb-unit-norm-one the identity has norm 1, hence ||e_r|| = 1. By GT-hyp (E6) each factor carries an exact-adjoint coboundary splitting S_r: im(d^1_{B_r}) -> C^1(B_r,B_r) with d^1_{B_r} S_r g = g and ||S_r g|| <= K_r ||g|| in the injective order-unit cochain norm (def-injective-cochain-norm); set K := max_r K_r. This node fixes notation and the standing hypotheses used by all later nodes.

**Type:** claim

**Inference:** assumption

**Status:** validated

**Taint:** clean

### Node 1.2

**Statement:** BLOCK RESTRICTION IS A COBOUNDARY. Fix an exact-adjoint coboundary f = d^1 h on B (so f in im(d^1), with primitive 1-cochain h: B -> B; this f is the input we must split). For each r define the same-factor restriction f^r: B_r x B_r -> B_r by f^r(a,b) := P_r f(a,b) for a,b in B_r, and define the restricted 1-cochain h_r: B_r -> B_r by h_r(a) := P_r h(a). CLAIM: f^r = d^1_{B_r} h_r, i.e. f^r is an exact-adjoint coboundary on B_r. PROOF: for a,b in B_r, unfold the B-coboundary (def-jordan-coboundary, node 1.1) and apply P_r: P_r f(a,b) = P_r[ a circ h(b) + h(a) circ b - h(a circ b) ]. Since B_r is an ideal of B and a,b in B_r (node 1.1), a circ b in B_r, and for any z in B the product a circ (P_r z) and the projection commute on the B_r block: P_r(a circ h(b)) = a circ P_r h(b) = a circ h_r(b), because a in B_r and the coordinatewise product has no cross-block contribution to the B_r component (node 1.1: B_r is a block-ideal, e_r acts as identity on B_r and annihilates other blocks, so P_r(a circ w) = a circ P_r w for a in B_r). Likewise P_r(h(a) circ b) = (P_r h(a)) circ b = h_r(a) circ b, and P_r h(a circ b) = h_r(a circ b). Hence f^r(a,b) = a circ h_r(b) + h_r(a) circ b - h_r(a circ b) = (d^1_{B_r} h_r)(a,b). Therefore f^r in im(d^1_{B_r}), so S_r f^r is defined (node 1.1, E6) and d^1_{B_r}(S_r f^r) = f^r.

**Type:** claim

**Inference:** by_definition

**Status:** validated

**Taint:** clean

### Node 1.3

**Statement:** CONSTRUCTION OF THE SPLITTING Sf. Given the exact-adjoint coboundary f = d^1 h on B (node 1.2), define a 1-cochain Sf: B -> B coordinatewise by its blocks: for x in B and each r, (Sf)_r(x) := P_r (Sf)(x) is given by (Sf)_r(x) = (S_r f^r)(x_r) + P_r f(e_r, x_{!=r}), where x_r := P_r x is the B_r-component, x_{!=r} := x - x_r is the off-block part, S_r is the per-factor splitting and f^r = d^1_{B_r} h_r the same-factor restriction (node 1.2). Then Sf(x) := sum_r (Sf)_r(x) assembling the blocks. The FIRST summand (S_r f^r)(x_r) is the diagonal term (well-defined since f^r in im(d^1_{B_r}) by node 1.2); the SECOND summand P_r f(e_r, x_{!=r}) is the off-block recovery term, evaluated at the central unit e_r (node 1.1) on the FIRST slot and the off-block part on the second, with NO sum over r (each output block B_r uses only its own e_r). Sf is linear in f (both summands are linear in f: S_r is linear and f |-> f^r, f |-> f(e_r,.) are linear) and linear in x. This defines the candidate map S: im(d^1) -> C^1(B,B), f |-> Sf.

**Type:** claim

**Inference:** by_definition

**Status:** validated

**Taint:** clean

### Node 1.4

**Statement:** COORDINATE MAPS ARE NORM-NONINCREASING (max-norm). Working in the order-unit norm of B and the injective order-unit cochain norm (def-injective-cochain-norm, node 1.1). From ||x|| = max_r ||x_r|| (GT-hyp E5, node 1.1): (i) for each r, ||x_r|| <= max_s ||x_s|| = ||x||, so the coordinate projection P_r is norm-nonincreasing, ||P_r y|| <= ||y|| for all y in B. (ii) ||x_{!=r}|| = ||x - x_r|| = ||sum_{s != r} x_s|| = max_{s != r} ||x_s|| <= max_s ||x_s|| = ||x|| (the max-norm of the off-block part is the max over s != r, dominated by the full max). (iii) ||e_r|| = 1 (node 1.1, via GT-jb-unit-norm-one). CONSEQUENCE for cochain restrictions: for the same-factor restriction f^r(a,b) = P_r f(a,b) with a,b in B_r (node 1.2), ||f^r||_inj = sup_{||a||,||b|| <= 1, a,b in B_r} ||P_r f(a,b)|| <= sup_{||a||,||b|| <= 1 in B} ||f(a,b)|| = ||f||_inj, using (i) (P_r norm-1) and that the sup over the B_r-unit-ball is over a subset of the B-unit-ball (||a|| <= 1, a in B_r implies ||a|| <= 1 in B since the norm is inherited, node 1.1). Hence ||f^r|| <= ||f|| for every r.

**Type:** claim

**Inference:** by_definition

**Status:** validated

**Taint:** clean

### Node 1.5

**Statement:** NORM BOUND ||Sf|| <= (max_r K_r + 1)||f||. Take x in B with ||x|| <= 1; bound each output block (Sf)_r(x) = (S_r f^r)(x_r) + P_r f(e_r, x_{!=r}) (node 1.3). DIAGONAL term: ||(S_r f^r)(x_r)|| <= ||S_r f^r||_inj * ||x_r|| <= K_r ||f^r|| * ||x_r|| <= K_r ||f|| * 1 <= K ||f||, using ||S_r g|| <= K_r ||g|| (node 1.1, E6), ||f^r|| <= ||f|| (node 1.4), ||x_r|| <= ||x|| <= 1 (node 1.4(i)), and K = max_r K_r (node 1.1) so K_r <= K. OFF-BLOCK term: ||P_r f(e_r, x_{!=r})|| <= ||P_r|| * ||f(e_r, x_{!=r})|| <= ||f||_inj * ||e_r|| * ||x_{!=r}|| <= ||f|| * 1 * 1 = ||f||, using ||P_r y|| <= ||y|| (node 1.4(i)), the definition of the injective cochain norm ||f(u,v)|| <= ||f||_inj ||u|| ||v|| (def-injective-cochain-norm, node 1.1), ||e_r|| = 1 (node 1.4(iii)), and ||x_{!=r}|| <= ||x|| <= 1 (node 1.4(ii)). SUM per block: ||(Sf)_r(x)|| <= K||f|| + ||f|| = (K+1)||f|| for EVERY r, where the +1 is the single flat cost of the one application of f in the off-block term, INDEPENDENT of the factor constants K_r. AGGREGATE: ||Sf(x)|| = max_r ||(Sf)_r(x)|| <= (K+1)||f|| (the aggregation across blocks is a MAX, by ||y|| = max_r ||y_r||, node 1.1/1.4 — NOT a sum). Taking sup over ||x|| <= 1: ||Sf||_inj <= (K+1)||f|| = (max_r K_r + 1)||f||. The bound is INDEPENDENT OF THE NUMBER OF SUMMANDS m: the only cross-summand aggregations (||x|| = max_r ||x_r|| and ||Sf|| = max_r ||(Sf)_r||) are maxima of per-r quantities each bounded by the same (K+1), so no term scales with m.

**Type:** claim

**Inference:** modus_ponens

**Status:** validated

**Taint:** clean

### Node 1.6

**Statement:** OFF-BLOCK RECOVERY IDENTITY. Write the primitive's output-blocks as h_{rs}: B_s -> B_r, h_{rs}(y) := P_r h(y) for y in B_s (so the relevant unit is e_r on the OUTPUT side B_r). CLAIM: for r != s and y in B_s, P_r f(e_r, y) = h_{rs}(y). PROOF: f = d^1 h (node 1.2), so unfold (def-jordan-coboundary, node 1.1) at (e_r, y): f(e_r, y) = e_r circ h(y) + h(e_r) circ y - h(e_r circ y). Now e_r circ y = 0 since y in B_s, s != r and e_r annihilates other blocks (node 1.1), so the third term vanishes: h(e_r circ y) = h(0) = 0. Apply P_r to the remaining two terms. FIRST term: P_r(e_r circ h(y)) = e_r circ P_r h(y) = e_r circ h_{rs}(y) = h_{rs}(y), because e_r acts as the identity on its own block B_r (node 1.1: e_r circ z = z for z in B_r) and P_r h(y) = h_{rs}(y) lies in B_r; also e_r circ (anything) projected to B_r equals e_r circ (its B_r-part) since e_r is the block-r central unit (node 1.1, GT-central-idempotent-summand). SECOND term: P_r(h(e_r) circ y) = 0, because y in B_s with s != r and the coordinatewise product sends B_? circ B_s into B_s-related blocks with zero B_r-component when s != r (node 1.1: distinct blocks multiply to 0 in the coordinatewise product, so any product involving the factor y in B_s has zero component in B_r for r != s). Hence P_r f(e_r, y) = h_{rs}(y) + 0 = h_{rs}(y). This reads the off-block primitive component h_{rs} (r != s) directly off the coboundary f via one evaluation at the central unit e_r.

**Type:** claim

**Inference:** by_definition

**Status:** validated

**Taint:** clean

### Node 1.7

**Statement:** RIGHT-INVERSE: d^1 Sf = f. We show the constructed Sf (node 1.3) satisfies (d^1 Sf)(a,b) = f(a,b) for all a,b in B, where d^1 is the B-coboundary (def-jordan-coboundary, node 1.1) and f = d^1 h is the given coboundary (node 1.2). Both d^1 Sf and f are SYMMETRIC bilinear in (a,b), and B = direct-sum_r B_r, so by bilinearity it suffices to verify the identity on homogeneous pairs (a,b) with a in B_r and b in B_s for all r,s. Two cases exhaust these homogeneous pairs: (CASE A) the same-factor pairs r = s, established in child node 1.7.1; (CASE B) the cross-factor pairs r != s, established in child node 1.7.2. Since every (a,b) in B x B expands by bilinearity into a finite sum of such homogeneous pairs and both sides are bilinear, child nodes 1.7.1 and 1.7.2 together give (d^1 Sf)(a,b) = f(a,b) on all of B x B; hence d^1 Sf = f, i.e. Sf is an exact right inverse on im(d^1). SCOPE OF THIS NODE vs THE TRANSITIVE 1.5 DEPENDENCY. The right-inverse property d^1 Sf = f established above uses ONLY this node's declared dependencies -- nodes 1.2 (block restriction is a coboundary), 1.3 (construction of Sf), 1.6 (off-block recovery identity) and the case children 1.7.1, 1.7.2 -- and asserts NO norm constant. The full conclusion the contract headlines -- that the linear map S: f |-> Sf (node 1.3) is an exact-adjoint coboundary splitting on B WITH CONSTANT max_r K_r + 1 -- is NOT discharged by this node alone: it is obtained by COMBINING this right-inverse (d^1 Sf = f) with the norm bound ||Sf|| <= (max_r K_r + 1)||f|| proved in node 1.5. Node 1.5 is therefore a TRANSITIVE DEPENDENCY of that combined, constant-bearing conclusion; we RECORD it here in-statement because af provides no post-hoc dependency-edge command to add 1.5 to this node's edges without re-refining (which would archive the already-validated case children 1.7.1, 1.7.2) -- the same in-prose transitive-dependency recording precedent established at thm-faithful-approx node 1.4. The final assembly -- construction S: f |-> Sf (node 1.3) + norm bound ||Sf|| <= (max_r K_r + 1)||f|| (node 1.5) + exact right inverse d^1 Sf = f (this node 1.7) => S is an exact-adjoint coboundary splitting on B with constant max_r K_r + 1, in the adjoint/block-respecting module -- is discharged at the root node 1.

**Type:** claim

**Inference:** universal_generalization

**Status:** validated

**Taint:** clean

#### Node 1.7.1

**Statement:** CASE A (same-factor, r = s): a, b in B_r. Compute (d^1 Sf)(a,b) = a circ Sf(b) + Sf(a) circ b - Sf(a circ b) (def-jordan-coboundary, node 1.1) and compare to f(a,b) block by block on the output. INPUTS: a,b in B_r so a circ b in B_r (block-ideal, node 1.1); the relevant components of Sf at the inputs a,b,a circ b in B_r are, for each output block j, (Sf)_j(a) = (S_j f^j)(a_j) + P_j f(e_j, a_{!=j}) with a_j = a if j=r else 0 (node 1.3, since a in B_r). OUTPUT BLOCK j = r: only the B_r-components of a circ Sf(b), Sf(a) circ b, Sf(a circ b) contribute, and since a,b in B_r and B_r is a block-ideal (node 1.1), P_r(a circ Sf(b)) = a circ (Sf)_r(b), P_r(Sf(a) circ b) = (Sf)_r(a) circ b, P_r Sf(a circ b) = (Sf)_r(a circ b). For inputs in B_r the off-block term of (Sf)_r vanishes (P_r f(e_r, a_{!=r}) with a_{!=r} = 0), so (Sf)_r restricted to B_r equals (S_r f^r) restricted to B_r = S_r f^r composed with identity, i.e. (Sf)_r|_{B_r} = S_r f^r (a 1-cochain on B_r). Hence P_r (d^1 Sf)(a,b) = a circ (S_r f^r)(b) + (S_r f^r)(a) circ b - (S_r f^r)(a circ b) = (d^1_{B_r}(S_r f^r))(a,b) = f^r(a,b) = P_r f(a,b), using d^1_{B_r}(S_r f^r) = f^r (node 1.2) and f^r = P_r f|_{B_r x B_r} (node 1.2). OUTPUT BLOCK j != r: a circ (Sf)_j(b) has zero B_j-component (a in B_r, the product a circ z lands in B_r-related blocks, zero in B_j for j != r; node 1.1) and likewise (Sf)_j(a) circ b = 0 in B_j; so P_j(a circ Sf(b)) = 0 = P_j(Sf(a) circ b). Thus P_j (d^1 Sf)(a,b) = - P_j Sf(a circ b) = - (Sf)_j(a circ b). Now a circ b in B_r and j != r, so (Sf)_j(a circ b) = (S_j f^j)((a circ b)_j) + P_j f(e_j, (a circ b)_{!=j}); here (a circ b)_j = 0 (since a circ b in B_r, j != r), and (a circ b)_{!=j} = a circ b, giving (Sf)_j(a circ b) = P_j f(e_j, a circ b). By the off-block recovery identity (node 1.6) with output-block j, source-block r, and a circ b in B_r (r != j): P_j f(e_j, a circ b) = h_{jr}(a circ b) = P_j h(a circ b). On the other side, P_j f(a,b) = P_j(d^1 h)(a,b) = P_j[a circ h(b) + h(a) circ b - h(a circ b)] = -P_j h(a circ b) (the first two terms vanish in B_j: a,b in B_r, j != r, so a circ h(b) and h(a) circ b have zero B_j-component by the block-product rule, node 1.1). Hence P_j (d^1 Sf)(a,b) = -(Sf)_j(a circ b) = -P_j h(a circ b) = P_j f(a,b). Both output blocks agree, so (d^1 Sf)(a,b) = f(a,b) for a,b in B_r.

**Type:** case

**Inference:** by_definition

**Status:** validated

**Taint:** clean

#### Node 1.7.2

**Statement:** CASE B (cross-factor, r != s): a in B_r, b in B_s. Since distinct blocks multiply to zero in the coordinatewise product (node 1.1), a circ b = 0, so the third coboundary term vanishes: (d^1 Sf)(a,b) = a circ Sf(b) + Sf(a) circ b - Sf(a circ b) = a circ Sf(b) + Sf(a) circ b (def-jordan-coboundary, node 1.1; Sf(0) = 0 by linearity, node 1.3). Compare to f(a,b) = (d^1 h)(a,b) = a circ h(b) + h(a) circ b - h(a circ b) = a circ h(b) + h(a) circ b (node 1.2; same vanishing). Check each output block j. OUTPUT BLOCK j = r: P_r(a circ Sf(b)) = a circ (Sf)_r(b) (a in B_r, block-ideal, node 1.1), and P_r(Sf(a) circ b) = 0 because b in B_s, s != r, so any product with the factor b in B_s has zero B_r-component (node 1.1). Now b in B_s and (Sf)_r(b) = (S_r f^r)(b_r) + P_r f(e_r, b_{!=r}); since b in B_s with s != r, b_r = 0 (so the diagonal term is S_r f^r(0) = 0) and b_{!=r} = b, giving (Sf)_r(b) = P_r f(e_r, b). By the off-block recovery identity (node 1.6) with output-block r, source-block s, b in B_s (r != s): P_r f(e_r, b) = h_{rs}(b) = P_r h(b). Hence (Sf)_r(b) = P_r h(b), so a circ (Sf)_r(b) = a circ P_r h(b) = a circ h_{rs}(b), giving P_r (d^1 Sf)(a,b) = a circ h_{rs}(b). On the other side P_r f(a,b) = P_r[a circ h(b) + h(a) circ b] = a circ P_r h(b) + 0 = a circ h_{rs}(b) (the term h(a) circ b has zero B_r-component since b in B_s, s != r, node 1.1; and P_r(a circ h(b)) = a circ P_r h(b) since a in B_r, node 1.1). So P_r (d^1 Sf)(a,b) = a circ h_{rs}(b) = P_r f(a,b). OUTPUT BLOCK j = s: symmetric (swap roles of a,b and r,s using symmetry of the Jordan product and of the cochains): P_s(Sf(a) circ b) = b circ (Sf)_s(a) and (Sf)_s(a) = P_s f(e_s, a) = h_{sr}(a) = P_s h(a) (node 1.6, output-block s, source-block r, a in B_r, s != r); P_s(a circ Sf(b)) = 0 (a in B_r, r != s, node 1.1). Hence P_s (d^1 Sf)(a,b) = (Sf)_s(a) circ b = h_{sr}(a) circ b = P_s h(a) circ b = P_s f(a,b) (on the other side P_s[a circ h(b) + h(a) circ b] = 0 + P_s h(a) circ b = h_{sr}(a) circ b). OUTPUT BLOCK j with j != r and j != s: P_j(a circ Sf(b)) = 0 (the factor a in B_r forces zero B_j-component for j != r, node 1.1) and P_j(Sf(a) circ b) = 0 (factor b in B_s forces zero B_j-component for j != s, node 1.1), so P_j (d^1 Sf)(a,b) = 0; and P_j f(a,b) = P_j[a circ h(b) + h(a) circ b] = 0 likewise (node 1.1). All output blocks agree, so (d^1 Sf)(a,b) = f(a,b) for a in B_r, b in B_s, r != s.

**Type:** case

**Inference:** by_definition

**Status:** validated

**Taint:** clean

