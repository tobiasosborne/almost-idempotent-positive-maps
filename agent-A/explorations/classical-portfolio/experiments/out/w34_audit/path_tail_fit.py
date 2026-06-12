#!/usr/bin/env python3
from __future__ import annotations

import json
import math

import numpy as np


rows = json.load(open("audit_compute.json"))["A3_path_tie_growth"]["path_pattern_rows"]
for cutoff in [4, 8, 10, 12, 15, 20]:
    data = [r for r in rows if r["k"] >= cutoff]
    x = np.array([r["k"] for r in data], dtype=float)
    y = np.array([r["ratio"] for r in data], dtype=float)

    X = np.column_stack([np.ones_like(x), 1 / x])
    coef = np.linalg.lstsq(X, y, rcond=None)[0]
    pred = X @ coef
    L = coef[0]
    c = -coef[1]

    Xlog = np.column_stack([np.ones_like(x), np.log(x)])
    clog = np.linalg.lstsq(Xlog, y, rcond=None)[0]
    predlog = Xlog @ clog

    cforced = np.linalg.lstsq((1 / x)[:, None], 2 - y, rcond=None)[0][0]
    predforced = 2 - cforced / x

    print(
        "cutoff",
        cutoff,
        "n",
        len(data),
        "free_L",
        L,
        "free_c",
        c,
        "rmse_free",
        float(np.sqrt(((pred - y) ** 2).mean())),
        "forced2_c",
        cforced,
        "rmse_forced2",
        float(np.sqrt(((predforced - y) ** 2).mean())),
        "log_beta0",
        clog[0],
        "log_beta1",
        clog[1],
        "rmse_log",
        float(np.sqrt(((predlog - y) ** 2).mean())),
        "pred100_free",
        L - c / 100,
        "pred100_forced2",
        2 - cforced / 100,
        "pred100_log",
        clog[0] + clog[1] * math.log(100),
    )
