"""
canary_smoke.py -- dimension canary for the Jordan error-reduction splitting.

SMOKE TEST (prototype, not a certified computation). Extends the existing
jordan-coboundary experiment to large vector-space dimension N to see whether
the splitting constant of the Jordan 2-coboundary d^1 is dimension-free (the
Layer-1 structure-theorem conjecture survives) or grows with N (canary fires).

Background (report sec. 7, REPORT.md). The coboundary is
    (d^1 h)(a,b) = a o h(b) + h(a) o b - h(a o b),   C^1=Lin(J,J) -> C^2=Sym^2(J)->J,
for the adjoint module M=J. Since H^2(J,J)=0 for semisimple J, d^1 has a right
inverse (splitting) s with d^1 s = id on B^2=Z^2. Its norm is the constant K in
Kitaev's error-reduction Newton step  delta -> O(delta^2 + K eps); a
dimension-free K is exactly what the Jordan structure theorem needs.

  s := Frobenius-minimal right inverse (the pseudoinverse).
  Frobenius:   ||s||_F  = 1 / sigma_min(d^1)              (EXACT; cheap)
               -- the BOUNDED result (averaging over U(M(J)), Frobenius isometries).
  Order-unit:  ||s||_op = sup_g ||s g||_op / ||g||_op     (THE norm the theorem
               controls) -- the UNRESOLVED one.

Two honest caveats on ||s||_op:
  (1) It is the op-norm of THIS (Frobenius-minimal) splitting; the theorem needs
      only SOME bounded splitting, so ||s_F||_op bounded is good news, ||s_F||_op
      growing is suggestive-not-fatal (an op-norm-optimal splitting might be
      smaller).
  (2) We compute it by maximizing a ratio over test cochains, so it is a LOWER
      bound on ||s_F||_op. A clear GROWTH is therefore the decisive (canary-fires)
      signal; a plateau is consistent with dimension-free but not a proof.

Why spin factors are the canary family: V_n = R (+) R^n has dim N=n+1 (linear in
n vs n^2 for H_n(C)), so N reaches ~40 cheaply; and its order-unit norm
||(t,v)|| = |t|+||v||_2 makes ||.||_op a tractable extreme-point computation
(poles +-e_0 and the equator sphere {(0,u)}), so the spin numbers are trustworthy.
H_n(C)/H_n(R) are cross-checks against the existing REPORT.md numbers (looser,
random-direction op-norm search).

Run:  python3 canary_smoke.py            # default sweep, writes results_canary.json
      python3 canary_smoke.py --quick    # smaller budget / faster
      python3 canary_smoke.py --families=spin
"""
import sys
import time
import json
import numpy as np

import jordan_common as jc
from jordan_fast import build_d1_fast


# ======================================================================
# Build algebra + coboundary + Frobenius-minimal splitting.
# ======================================================================

def build_family(family, n):
    if family == "spin":
        N, ip, jordan, B = jc.make_spin_factor(n)
        ker_expected = n * (n - 1) // 2            # dim so(n)
    elif family == "HnC":
        B = jc.basis_Hn_C(n)
        N, ip, jordan, B = jc.make_matrix_algebra(B)
        ker_expected = n * n - 1                   # dim su(n)
    elif family == "HnR":
        B = jc.basis_Hn_R(n)
        N, ip, jordan, B = jc.make_matrix_algebra(B)
        ker_expected = n * (n - 1) // 2            # dim so(n)
    else:
        raise ValueError(family)
    D, info = build_d1_fast(N, ip, jordan, B)
    return N, B, D, info, ker_expected


def frobenius_part(D):
    """smin/smax (nonzero) of d^1 via the small Gram G=D^T D, plus the
    row-space projector P=G^+ G onto (ker d^1)^perp in the HS inner product."""
    G = D.T @ D
    w, V = np.linalg.eigh(G)
    w = np.clip(w, 0.0, None)
    tol = max(G.shape) * np.finfo(float).eps * (w[-1] if w[-1] > 0 else 1.0)
    pos = w > tol
    smin = float(np.sqrt(w[pos].min())) if pos.any() else 0.0
    smax = float(np.sqrt(w[-1]))
    Vp = V[:, pos]
    return smin, smax, int(pos.sum()), Vp @ Vp.T


def f_tensor(fvec, N, pairs):
    F = np.zeros((N, N, N))
    for k, (a, b) in enumerate(pairs):
        w = 1.0 if a == b else np.sqrt(2.0)
        blk = fvec[k * N:(k + 1) * N] / w
        F[a, b, :] = blk
        F[b, a, :] = blk
    return F


# ======================================================================
# Spin factors: trustworthy order-unit norms via extreme-point structure.
#   element coords x = (t, v): ou(x) = |t| + ||v||_2.
#   unit-ball extreme points: poles +-e_0  and  equator (0,u), ||u||=1.
# ======================================================================

def spin_ou(x):
    x = np.asarray(x, float)
    return abs(x[0]) + float(np.linalg.norm(x[1:]))


def max_ou_over_sphere(L, rng, restarts=6, steps=40):
    """sup_{||z||=1} ou(L z),  L shape (N_out, m). ou(y)=|y0|+||y[1:]||.
    Projected-gradient ascent with restarts (a slight under-estimate of the sup)."""
    Nout, m = L.shape
    if m == 0:
        return 0.0
    best = 0.0
    # seeds: right singular vectors of L (good directions) + random
    try:
        _, _, Vt = np.linalg.svd(L, full_matrices=False)
        seeds = [Vt[i] for i in range(min(m, 3))]
    except np.linalg.LinAlgError:
        seeds = []
    seeds += [rng.standard_normal(m) for _ in range(restarts)]
    for z in seeds:
        z = np.asarray(z, float)
        nz = np.linalg.norm(z)
        if nz == 0:
            continue
        z = z / nz
        for _ in range(steps):
            y = L @ z
            tail = y[1:]
            nt = np.linalg.norm(tail)
            g = np.sign(y[0]) * L[0]
            if nt > 1e-14:
                g = g + L[1:].T @ (tail / nt)
            ng = np.linalg.norm(g)
            if ng < 1e-14:
                break
            z = z + 0.5 * g / ng
            z = z / np.linalg.norm(z)
        best = max(best, spin_ou(L @ z))
    return best


def op_norm_1cochain_spin(H, rng):
    """||h||_op for h(e_j)=sum_i H[i,j] e_j-image, H shape (N,N)."""
    pole = spin_ou(H[:, 0])                       # x = +-e_0
    equator = max_ou_over_sphere(H[:, 1:], rng)   # x = (0,u)
    return max(pole, equator)


def op_norm_2cochain_spin(F, rng):
    """||g||_op for symmetric bilinear g, tensor F[i,j,p]. sup over extreme x,y."""
    N = F.shape[0]
    # pole-pole: g(e0,e0)
    pp = spin_ou(F[0, 0, :])
    # pole-equator: g(e0,(0,w)) linear in w; L[p,j]=F[0,1+j,p]
    pe = max_ou_over_sphere(F[0, 1:, :].T, rng)
    # equator-equator: g((0,u),(0,w)) bilinear; alternate u<->w
    Fee = F[1:, 1:, :]                            # (i, j, p), i,j in equator
    n = N - 1
    ee = 0.0
    if n > 0:
        for _ in range(4):
            u = rng.standard_normal(n); u /= np.linalg.norm(u)
            for _ in range(5):
                Lw = np.tensordot(u, Fee, axes=(0, 0)).T   # sum_i u_i Fee[i,j,p] -> (p, j)
                w = _best_sphere_vec(Lw, rng)
                Lu = np.tensordot(w, Fee, axes=(0, 1)).T   # sum_j w_j Fee[i,j,p] -> (p, i)
                u = _best_sphere_vec(Lu, rng)
            ee = max(ee, spin_ou(np.einsum('i,j,ijp->p', u, w, Fee)))
    return max(pp, pe, ee)


def _best_sphere_vec(L, rng, steps=30):
    """argmax-ish unit z of ou(L z); returns the unit vector (not the value)."""
    Nout, m = L.shape
    if m == 0:
        return np.zeros(0)
    try:
        _, _, Vt = np.linalg.svd(L, full_matrices=False)
        z = Vt[0].copy()
    except np.linalg.LinAlgError:
        z = rng.standard_normal(m)
    z = z / (np.linalg.norm(z) + 1e-30)
    for _ in range(steps):
        y = L @ z
        tail = y[1:]; nt = np.linalg.norm(tail)
        g = np.sign(y[0]) * L[0]
        if nt > 1e-14:
            g = g + L[1:].T @ (tail / nt)
        ng = np.linalg.norm(g)
        if ng < 1e-14:
            break
        z = z + 0.5 * g / ng
        z = z / np.linalg.norm(z)
    return z


# ======================================================================
# Matrix families H_n(C/R): random-extreme-direction search (matches the
# existing opnorm_trend.py method; looser, used for cross-validation).
# ======================================================================

def make_mat_ou(B):
    def ou(x):
        M = np.zeros_like(B[0], dtype=complex)
        for c, e in zip(x, B):
            M = M + c * e
        M = (M + M.conj().T) / 2
        return float(np.max(np.abs(np.linalg.eigvalsh(M))))
    return ou


def rand_unit_op(n_mat, B, ou, rng):
    t = rng.integers(0, 4)
    if t == 0:
        Mc = rng.standard_normal((n_mat, n_mat)) + 1j * rng.standard_normal((n_mat, n_mat))
        H = (Mc + Mc.conj().T) / 2
    elif t == 1:
        Q, _ = np.linalg.qr(rng.standard_normal((n_mat, n_mat)) + 1j * rng.standard_normal((n_mat, n_mat)))
        H = Q @ np.diag(rng.choice([-1.0, 1.0], n_mat)) @ Q.conj().T
    elif t == 2:
        v = rng.standard_normal(n_mat) + 1j * rng.standard_normal(n_mat); v /= np.linalg.norm(v)
        H = np.outer(v, v.conj())
    else:
        v = rng.standard_normal(n_mat) + 1j * rng.standard_normal(n_mat); v /= np.linalg.norm(v)
        u = rng.standard_normal(n_mat) + 1j * rng.standard_normal(n_mat); u /= np.linalg.norm(u)
        H = np.outer(v, v.conj()) - np.outer(u, u.conj())
    vec = np.array([float(np.real(np.trace(e @ H))) for e in B])
    nn = ou(vec)
    return vec / nn if nn > 0 else vec


def op_norm_2cochain_mat(F, B, ou, rng, n_dir):
    best = 0.0; n_mat = B[0].shape[0]
    for _ in range(n_dir):
        a = rand_unit_op(n_mat, B, ou, rng); b = rand_unit_op(n_mat, B, ou, rng)
        best = max(best, ou(np.einsum('i,j,ijp->p', a, b, F)))
    return best


def op_norm_1cochain_mat(H, B, ou, rng, n_dir):
    best = 0.0; n_mat = B[0].shape[0]
    for _ in range(n_dir):
        a = rand_unit_op(n_mat, B, ou, rng)
        best = max(best, ou(H @ a))
    return best


# ======================================================================
# Operator-norm lower bound on ||s_F||_op (s_F = Frobenius-minimal r.inv).
# For 1-cochain h0:  f = d h0 in B^2,  h = s_F f = P h0.
# ======================================================================

def op_lower_bound(family, N, B, D, P, info, n_restart, n_dir, seed=11):
    pairs = [(a, b) for a in range(N) for b in range(a, N)]
    rng = np.random.default_rng(seed)
    if family == "spin":
        op2 = lambda F: op_norm_2cochain_spin(F, rng)
        op1 = lambda H: op_norm_1cochain_spin(H, rng)
    else:
        ou = make_mat_ou(B)
        op2 = lambda F: op_norm_2cochain_mat(F, B, ou, rng, n_dir)
        op1 = lambda H: op_norm_1cochain_mat(H, B, ou, rng, n_dir)
    best = 0.0
    for r in range(n_restart):
        kind = rng.integers(0, 3)
        if kind == 0:
            H0 = rng.standard_normal((N, N))
        elif kind == 1:
            H0 = np.zeros((N, N))
            for _ in range(int(rng.integers(1, 3))):
                H0 += np.outer(rng.standard_normal(N), rng.standard_normal(N))
        else:
            H0 = rng.standard_normal((N, N)); H0[np.abs(H0) < 0.8] = 0.0
        h0 = H0.reshape(-1)
        fvec = D @ h0
        if np.linalg.norm(fvec) < 1e-10:
            continue
        hvec = P @ h0
        fop = op2(f_tensor(fvec, N, pairs))
        if fop < 1e-12:
            continue
        hop = op1(hvec.reshape(N, N))
        best = max(best, hop / fop)
    return best


# ======================================================================
# Sweep + trend + verdict.
# ======================================================================

SWEEPS = {
    "spin": [2, 3, 4, 6, 8, 10, 13, 16, 20, 25, 30, 35, 40],   # N = n+1
    "HnC":  [2, 3, 4, 5, 6],
    "HnR":  [2, 3, 4, 5, 6, 7, 8],
}


def budget(family, N, quick):
    if family == "spin":                       # spin op-norm is cheap & accurate
        nr = (40 if quick else 80)
        return nr, 0
    nr = (int(700 / np.sqrt(N)) if quick else int(1500 / np.sqrt(N)))
    nd = (max(24, int(180 / np.sqrt(N))) if quick else max(36, int(280 / np.sqrt(N))))
    return max(40, nr), nd


def loglog_slope(xs, ys):
    xs = np.asarray(xs, float); ys = np.asarray(ys, float)
    m = (xs > 0) & (ys > 0)
    if m.sum() < 2:
        return float("nan")
    return float(np.polyfit(np.log(xs[m]), np.log(ys[m]), 1)[0])


def run(families, quick):
    out = {}
    for fam in families:
        rows = []
        print(f"\n=== family {fam} "
              f"({'V_n: dim N=n+1' if fam == 'spin' else 'dim grows ~n^2'}) ===",
              flush=True)
        print(f"{'N':>4} {'ker':>5} {'ok':>3} {'sF=1/smin':>10} "
              f"{'smin':>7} {'smax':>7} {'kappa':>7} "
              f"{'||sF||op':>9} {'/sqrtN':>7} {'/N':>6} {'sec':>5}", flush=True)
        for n in SWEEPS[fam]:
            t0 = time.time()
            try:
                N, B, D, info, ker_exp = build_family(fam, n)
            except MemoryError:
                print(f"  n={n}: MemoryError; stopping family", flush=True)
                break
            smin, smax, rank, P = frobenius_part(D)
            ker = info["dimC1"] - rank
            sF = (1.0 / smin) if smin > 0 else float("inf")
            kappa = (smax / smin) if smin > 0 else float("inf")
            nr, nd = budget(fam, N, quick)
            sop = op_lower_bound(fam, N, B, D, P, info, nr, nd)
            dt = time.time() - t0
            rows.append(dict(family=fam, n=n, N=N, dimC1=info["dimC1"],
                             dimC2=info["dimC2"], ker=ker, ker_expected=ker_exp,
                             ker_ok=bool(ker == ker_exp), smin=smin, smax=smax,
                             kappa=kappa, sF=sF, sop_lb=sop,
                             sop_over_sqrtN=sop / np.sqrt(N), sop_over_N=sop / N,
                             n_restart=nr, n_dir=nd, sec=dt))
            print(f"{N:>4} {ker:>5} {('Y' if ker == ker_exp else 'N!'):>3} "
                  f"{sF:>10.4f} {smin:>7.3f} {smax:>7.3f} {kappa:>7.3f} "
                  f"{sop:>9.4f} {sop/np.sqrt(N):>7.4f} {sop/N:>6.4f} {dt:>5.0f}",
                  flush=True)
            del D, P
        out[fam] = rows
        if len(rows) >= 2:
            Ns = [r["N"] for r in rows]
            out[fam + "_slopes"] = dict(
                slope_sF=loglog_slope(Ns, [r["sF"] for r in rows]),
                slope_smin=loglog_slope(Ns, [r["smin"] for r in rows]),
                slope_smax=loglog_slope(Ns, [r["smax"] for r in rows]),
                slope_op=loglog_slope(Ns, [r["sop_lb"] for r in rows]))
            s = out[fam + "_slopes"]
            print(f"  log-log slopes vs N:  smin~N^{s['slope_smin']:+.3f}  "
                  f"smax~N^{s['slope_smax']:+.3f}  ||s||_F~N^{s['slope_sF']:+.3f}  "
                  f"||s||_op~N^{s['slope_op']:+.3f}", flush=True)
    return out


def verdict(out):
    print("\n" + "=" * 72)
    print("CANARY READ-OFF -- operator/order-unit norm is the one the theorem needs")
    print("=" * 72)
    for fam in ("spin", "HnC", "HnR"):
        sk = fam + "_slopes"
        if sk not in out:
            continue
        s = out[sk]["slope_op"]
        Nmax = max(r["N"] for r in out[fam])
        if s < 0.15:
            tag = "FLAT  -> canary did NOT fire (consistent with dim-free; LB)"
        elif s < 0.40:
            tag = "MILD  -> slow growth; ambiguous at this N"
        else:
            tag = "GROWS -> CANARY FIRES (K ~ N^slope, not dimension-free)"
        trust = "trustworthy" if fam == "spin" else "looser search"
        print(f"  {fam:>5} (to N={Nmax}, {trust}): "
              f"||s_F||_op ~ N^{s:+.3f}   {tag}")
    print("  ||s||_F is bounded by construction; the open question is ||s||_op.")
    print("  Reminder: ||s_F||_op is the Frobenius-minimal splitting; the theorem")
    print("  needs only SOME bounded splitting (op-norm-optimal could be smaller).")


def main():
    quick = "--quick" in sys.argv
    fams = ["spin", "HnC", "HnR"]
    for a in sys.argv[1:]:
        if a.startswith("--families="):
            fams = a.split("=", 1)[1].split(",")
    t0 = time.time()
    out = run(fams, quick)
    verdict(out)
    json.dump(out, open("results_canary.json", "w"), indent=2, default=float)
    print(f"\nWrote results_canary.json  (total {time.time()-t0:.0f}s)")


if __name__ == "__main__":
    main()
