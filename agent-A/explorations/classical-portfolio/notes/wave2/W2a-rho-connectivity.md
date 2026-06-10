**Verdict:** the full metric statement is still **OPEN**. I cannot honestly prove:

> hidden high vertex `v` ⇒ a pairwise-`ρ` row chain from `v` down to `Nρ(conv low rows)`.

The current audited facts prove a weaker but useful structure theorem.

**PROVED Structure Theorem**

Fix an affine height `g` with `g≤0` on `conv W`, `g(v)=H_v≥H`, and `‖g‖Lip,ℓ1≤1`. Let

```text
Low = {rows p_i : g(p_i) ≤ H/2}
High = {rows p_i : g(p_i) > H/2}.
```

If a row vertex `u∉W` has `g(u)>H/2` and fails `(ρ,κ)`-exposedness, then one of the following holds:

1. **Downward shadow:**  
   `u` is within `ρ` of `conv Low`.

2. **High carrier:**  
   some failed-exposedness/shadow certificate for `u` uses a row of height `>H/2` outside the low hull. If that carrier is a row vertex and not in `W`, it is another hidden high vertex and the recursion continues.

3. **Reuse/localization obstruction:**  
   the carrier is a non-vertex row whose vertex expansion reuses `u` with large coefficient. After collecting the `u`-coefficient, the height loss is amplified by roughly `diam(K)/ρ`; this is exactly the Audit-A2 stall / dual-localization gap, not a proved descent step.

**Proof Status By Step**

- **PROVED:** hidden vertex has a `ρ`-shadow: otherwise L1 exposes it with margin at least `ρ/(2+4δ) ≥ κ`.
- **PROVED:** applying the height functional to a shadow/certificate: if all certificate mass were at height `≤H/2`, then `u` would be within `ρ` of `conv Low`; otherwise there is high carrier mass.
- **PROVED:** exposed high carriers cannot be ignored: if a high carrier is a row vertex in `W`, then it already lies in the reference hull and collapses the measured height.
- **SKETCH/OPEN:** converting every high carrier into a new hidden vertex without height loss. Non-vertex carriers may expand using the old vertex `u`; collecting that coefficient is precisely where the current proof loses control.

**Cost Accounting Enabled**

Take any acyclic stretch of hidden high vertices produced before reaching `Nρ(conv Low)`. Let `S` be the rows in the stretch with height `≥H/2`. N1 applies:

```text
if P⁺_{S,S} is acyclic / strictly triangular,
then max_j P⁺_{v_j, High \ S} g  ≥  cρ - O(δ).
```

So an acyclic high chain cannot reproduce height internally. It must push positive mass to **off-chain high carriers**. Those carriers are exactly the objects produced by the connectivity recursion above.

Thus the unified picture is:

```text
downward shadow
or high cycle / skinny pair
or off-chain high carrier forced by nilpotence.
```

What is still missing is the localization theorem saying those off-chain high carriers either join `W`/collapse height or themselves continue a controlled `ρ`-connected descent. Claiming the full metric chain now would overclaim.