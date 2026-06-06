# Proof Export

## Node 1

**Statement:** For a unital order-isometric Jordan embedding j (so ||jM||=||M|| and ||j||_op=1) and a unital positive C, with Phi=Cj and F=jC, the operator-norm idempotency defects satisfy ||Phi^2-Phi|| <= ||F^2-F||; hence ||F^2-F|| <= eta < 1/4 forces ||Phi^2-Phi|| <= eta < 1/4, so P=theta(2Phi-1) is well-defined.

**Type:** claim

**Inference:** assumption

**Status:** pending

**Taint:** unresolved

### Node 1.1

**Statement:** ALGEBRA (defect of Phi). With Phi=Cj (GT-hyp H4), the operator-norm idempotency defect of Phi factors as Phi^2-Phi=(Phi-I)Cj. Derivation: Phi^2-Phi = (Cj)(Cj) - Cj = (Cj - I)(Cj) = (Phi - I)Cj, where the middle equality is the right-distributive identity (X)(Y)-Y=(X-I)Y for linear operators with X=Cj=Phi, Y=Cj, valid in the (associative) algebra of linear operators on B(H)_sa (GT-opnorm-submult: bounded linear operators form a Banach/associative operator algebra). Hence Phi^2-Phi=(Phi-I)Cj. Uses GT-hyp, GT-opnorm-submult.

**Type:** claim

**Inference:** assumption

**Status:** pending

**Taint:** unresolved

### Node 1.2

**Statement:** ALGEBRA (defect of F). With F=jC (GT-hyp H4) and Phi=Cj, the idempotency defect of F factors as F^2-F=j(Phi-I)C. Derivation: F^2-F = (jC)(jC) - jC = j(CjC) - jC = j(CjC - C) = j((Cj-I)C) = j(Phi-I)C, using associativity of composition (GT-opnorm-submult) to regroup jC jC = j(CjC), left-factoring j, then (CjC-C)=(Cj-I)C, and Cj=Phi. Hence F^2-F=j(Phi-I)C. Uses GT-hyp, GT-opnorm-submult.

**Type:** claim

**Inference:** assumption

**Status:** pending

**Taint:** unresolved

### Node 1.3

**Statement:** NORM BOUND (drop the trailing j). ||(Phi-I)Cj|| <= ||(Phi-I)C||. Derivation: by operator-norm submultiplicativity (GT-opnorm-submult: ||uw||<=||u||*||w||) applied with u=(Phi-I)C and w=j, ||(Phi-I)Cj|| = ||((Phi-I)C) j|| <= ||(Phi-I)C|| * ||j||_op; by GT-hyp (H1), ||j||_op=1, so ||(Phi-I)Cj|| <= ||(Phi-I)C|| * 1 = ||(Phi-I)C||. Uses GT-opnorm-submult, GT-hyp.

**Type:** claim

**Inference:** assumption

**Status:** pending

**Taint:** unresolved

#### Node 1.3.1

**Statement:** j ORDER-ISOMETRY: ||j(Phi-I)C|| = ||(Phi-I)C||. Derivation: by GT-hyp (H1) j is order-isometric, ||jM||=||M|| for every linear operator M (left-composition with the order-isometric embedding j preserves the operator norm). Apply with M=(Phi-I)C: ||j(Phi-I)C|| = ||(Phi-I)C||. (This is an EQUALITY, sharper than the submultiplicative bound ||j(Phi-I)C||<=||j||_op*||(Phi-I)C||=||(Phi-I)C||; order-isometry upgrades it to equality, which is what makes the defect inheritance tight with the SAME constant.) Uses GT-hyp.

**Type:** claim

**Inference:** assumption

**Status:** pending

**Taint:** unresolved

### Node 1.4

**Statement:** CONCLUSION. Chaining nodes 1.1, 1.2, 1.3 and 1.3.1: taking operator norms, ||Phi^2-Phi|| = ||(Phi-I)Cj|| by node 1.1; ||(Phi-I)Cj|| <= ||(Phi-I)C|| by node 1.3; ||(Phi-I)C|| = ||j(Phi-I)C|| by node 1.3.1 (j order-isometric); ||j(Phi-I)C|| = ||F^2-F|| by node 1.2. Composing the (in)equalities: ||Phi^2-Phi|| <= ||F^2-F||. Hence if ||F^2-F|| <= eta < 1/4 then ||Phi^2-Phi|| <= eta < 1/4; this strict threshold eta<1/4 is EXACTLY the binomial-series convergence condition for P=theta(2Phi-1) (def-spectral-idempotent: ||S^2-1||=4||Phi^2-Phi||<=4 eta<1 iff eta<1/4), so P=theta(2Phi-1) is well-defined. This is the contract. Uses node 1.1, node 1.2, node 1.3, node 1.3.1, def-spectral-idempotent.

**Type:** claim

**Inference:** assumption

**Status:** pending

**Taint:** unresolved

