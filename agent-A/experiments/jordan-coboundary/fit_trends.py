"""
Fit the sigma_min(n) and 1/sigma_min(n) trends, and (optionally) extend
H_n(C) to n=7,8 to pin down the asymptotics. We test models:
   sigma_min ~ a + b*n        (linear)
   sigma_min ~ a + b*sqrt(n)  (sqrt)
   sigma_min^2 ~ linear in n  (i.e. smin ~ sqrt(linear))
and report which fits best, plus the implied behaviour of 1/sigma_min.
"""

import numpy as np
import json
import time
import jordan_common as jc
from jordan_fast import build_d1_fast
from run_sweep import frob_analysis, make_HnC


def smin_of(N, ip, jordan, B):
    D, info = build_d1_fast(N, ip, jordan, B)
    sv = np.linalg.svd(D, compute_uv=False)
    smax = sv[0]
    tol = max(D.shape) * np.finfo(float).eps * smax
    nz = sv[sv > tol]
    return float(nz.min()), float(smax)


def fit_models(ns, smin):
    ns = np.array(ns, float)
    smin = np.array(smin, float)
    out = {}
    # linear in n
    A = np.vstack([np.ones_like(ns), ns]).T
    coef, res, *_ = np.linalg.lstsq(A, smin, rcond=None)
    pred = A @ coef
    out['linear  smin=a+b n'] = (coef, np.max(np.abs(pred - smin)))
    # sqrt n
    A = np.vstack([np.ones_like(ns), np.sqrt(ns)]).T
    coef, *_ = np.linalg.lstsq(A, smin, rcond=None)
    pred = A @ coef
    out['sqrt    smin=a+b sqrt(n)'] = (coef, np.max(np.abs(pred - smin)))
    # smin^2 linear in n
    A = np.vstack([np.ones_like(ns), ns]).T
    coef, *_ = np.linalg.lstsq(A, smin**2, rcond=None)
    pred = np.sqrt(np.clip(A @ coef, 0, None))
    out['smin^2=a+b n -> smin'] = (coef, np.max(np.abs(pred - smin)))
    # smin^2 linear in n^2 ? (smin ~ n)
    return out


def main():
    print("Extending H_n(C) to n=7,8 (this may take a couple minutes)...")
    ns = [2, 3, 4, 5, 6, 7, 8]
    smins = []
    smaxs = []
    for n in ns:
        t0 = time.time()
        N, ip, jordan, B = make_HnC(n)
        sm, sx = smin_of(N, ip, jordan, B)
        smins.append(sm)
        smaxs.append(sx)
        print(f"  H_{n}(C): N={N:3d} smin={sm:.6f} 1/smin={1/sm:.6f} "
              f"smax={sx:.4f} ({time.time()-t0:.1f}s)")

    print("\nsmin^2 sequence (look for linear-in-n pattern):")
    for n, sm in zip(ns, smins):
        print(f"  n={n}: smin^2 = {sm*sm:.6f}   (smin^2)/(n) = {sm*sm/n:.6f}  "
              f"(smin^2)/(n+?)...")
    # differences of smin^2
    sq = np.array(smins)**2
    print("  consecutive diffs of smin^2:", np.round(np.diff(sq), 5))

    print("\nModel fits for sigma_min(n), H_n(C):")
    fits = fit_models(ns, smins)
    for name, (coef, maxerr) in fits.items():
        print(f"  {name:28s}  coef={np.round(coef,5)}  maxabs_err={maxerr:.4e}")

    # Closed-form guess test:  smin^2 = (n+2)/3 ?  smin = sqrt((n+2)/3)?
    print("\nTest candidate closed forms for smin (H_n(C)):")
    for label, f in [
        ("sqrt((n+2)/3)", lambda n: np.sqrt((n+2)/3)),
        ("sqrt(n/2)",     lambda n: np.sqrt(n/2)),
        ("sqrt((n+1)/2)", lambda n: np.sqrt((n+1)/2)),
        ("sqrt(n)/sqrt(2)*c", None),
    ]:
        if f is None:
            continue
        pred = np.array([f(n) for n in ns])
        err = np.max(np.abs(pred - np.array(smins)))
        print(f"  smin ?= {label:16s} max|pred-smin| = {err:.4e}   pred={np.round(pred,4)}")

    json.dump(dict(ns=ns, smin=smins, smax=smaxs,
                   inv=[1/s for s in smins]),
              open("results_HnC_extended.json", "w"), indent=2)
    print("\nWrote results_HnC_extended.json")


if __name__ == "__main__":
    main()
