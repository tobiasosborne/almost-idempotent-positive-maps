VERDICT: GAP

Independent sketch: (i) is PROVED for `H>0`: distance to `conv W` is convex, so a row written as a convex combination of vertices has some vertex at distance `>=H`; such a vertex is not in `W`. (ii) is PROVED only with a small-delta/diameter normalization: if `dist_1(v,conv(rows\{v})) >= rho`, Hahn-Banach gives an affine separator with margin `rho`; normalizing by `diam_1(K)` gives exposure margin at least `rho/diam_1(K)`. This is `>=kappa` under e.g. `delta<=1` as in the note, but it is not stated in the claim.

The recorded proof matches (i) and (ii), adding the needed small-`delta` assumption.

The failure is in (iii): from `||v-q||_1<rho`, Lipschitzness gives `dist(q,conv W)>=H-rho`. Expanding `q` into vertices and using convexity gives some vertex at distance `>=H-rho`, but it may be `v` again. Since `q in conv(rows\{v})` does not imply `q in conv(vertices\{v})` (a nonvertex row can lie on an edge from `v`), the proof does not produce “another” non-`W` vertex. Need an extra lemma excluding re-use of `v`, or weaken the recursion statement.