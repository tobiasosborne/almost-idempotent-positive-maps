**1. Obstruction #2**

**PROVED, with a corrected constant.** Let `X` be the row set, `K=conv X`, `v=p*`, and `L=conv(X\{v})`. If

```text
d = dist_1(v,L) >= rho,
```

then `v` is a vertex and is `(rho,kappa)`-well-exposed with

```text
kappa >= rho / diam_1(K).
```

Proof: by `l1/l∞` separation, choose `phi` with `||phi||_∞ <= 1` and  
`phi(v) >= sup_L phi + d`. Let `M=phi(v)`, `m=min_K phi`, and

```text
h(x) = (M - phi(x)) / (M - m).
```

Then `h:K->[0,1]`, `h(v)=0`, and every other row satisfies

```text
h(p_i) >= d / (M-m) >= d / diam_1(K) >= rho / diam_1(K).
```

Also, under `d>=rho`, there are no other rows within `<rho` of `v`, since any such row would put `dist(v,L)<rho`.

The proposed `rho/2` bound is valid only for nonnegative probability rows. With signed rows of negative mass `<= delta`, the safe bound is

```text
diam_1(K) <= 2 + 4 delta,
kappa >= rho / (2 + 4 delta).
```

So for `rho=C tau`, this gives membership in `W` whenever the chosen `c` satisfies  
`c <= C/(2+4 delta)` in the relevant small-delta regime.

**2. HCC Attempt**

**Not proved.** I can reduce it to a sharp missing inequality.

Usable lemma DAG:

- **PROVED:** isolated far vertex exposes, as above.
- **PROVED:** if a far row is hidden, some far hidden vertex exists. A convex combination of vertices cannot be farther from `conv W` than all vertices used.
- **PROVED/SKETCH:** a hidden vertex must be `O(tau)`-shadowed by other rows. Otherwise obstruction #2 exposes it.
- **KNOWN/SKETCH:** failed exposedness gives the stated LP-dual certificate with far mass `mu`, small `beta`, and uncontrolled `alpha` on the zero face.
- **OPEN KEY LEMMA:** an anchored far circuit produced by those dual certificates forces
  `max_i neg(p_i) >= a * H^2`, where `H=dist_1(v,conv W)`.

If that last lemma holds, then with `H=D tau` we get

```text
max_i neg(p_i) >= a D^2 tau^2 = a D^2 delta,
```

which is HCC with `c0=a`.

The blocker is exactly the uncontrolled `alpha` mass. A raw high circuit can be zero-negativity in an exact stochastic idempotent; cost appears only when the circuit is anchored to the lower hull or to failed exposedness constraints. I do not currently see a rigorous inequality forcing that anchor in full generality.

Simplest test case: fix a 2D affine geometry with a low exposed edge `W`, a far thin diamond/trapezoid at height `H`, and constraints that every top extreme point has exposed margin `<kappa`. Then minimize `max row neg` over all exact completions `P=Lambda R`, `R Lambda=I`, not just the min-norm `R`. Test whether `min neg / H^2` stays bounded below.

**3. Staircase Reconciliation**

**SKETCH, numerically supported.** The staircase fails because the bookkeeping used the wrong `tau`.

In `d3_scaling`, staircase height scale `s` produces real `delta ≈ s`, hence real

```text
tau_real ≈ sqrt(s),
height / tau_real ≈ sqrt(s) -> 0.
```

So the apparent high staircase becomes small at the conjecture’s actual scale. Also, exposedness is global: once mirror or upper-layer rows are added to hide one level, those rows often become well-exposed themselves and enter `W`, so `conv W` moves upward and captures the hidden rows. The staircase is not accumulating height above a fixed hull.

**4. Verdict**

`P(HCC true as stated)`: about `0.6`. The numerics and mechanisms point that way, but the universal anchored-circuit inequality is still missing.

`P(provable by this route)`: about `0.3`. The route is plausible, but the alpha/zero-face issue is a real gap.

Next numerical test: adversarially optimize over all `R` completions for fixed hidden geometries, extract the LP-dual failed-exposedness certificates, and directly measure whether the proposed anchored-circuit cost `neg/H^2` has a positive lower envelope.