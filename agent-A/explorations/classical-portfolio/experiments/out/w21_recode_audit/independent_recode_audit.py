#!/usr/bin/env python3
"""Independent hostile checks for w21 mass-removed recoding.

This does not import the claimant's recoding checker.  It rebuilds H-M
idempotents, applies boundary recoding, checks exact idempotence, removed-mass
constants, sequential compounding, and summarizes the saved w21_second records.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np


TOL = 1e-10


@dataclass
class HM:
    blocks: list[list[int]]
    transients: list[int]
    pis: list[np.ndarray]
    alphas: dict[int, np.ndarray]
    name: str

    @property
    def n(self) -> int:
        return sum(len(b) for b in self.blocks) + len(self.transients)

    @property
    def k(self) -> int:
        return len(self.blocks)


@dataclass
class Recoding:
    source: HM
    recoded: HM
    drops: list[list[int]]
    face_drops: dict[int, list[int]]
    q: list[float]
    r: dict[int, float]

    @property
    def q_total(self) -> float:
        return float(sum(self.q))

    @property
    def r_max(self) -> float:
        return max((float(x) for x in self.r.values()), default=0.0)

    @property
    def budget(self) -> float:
        return self.q_total + self.r_max


def embedded(n: int, block: list[int], pi: np.ndarray) -> np.ndarray:
    row = np.zeros(n)
    for pos, j in enumerate(block):
        row[j] = pi[pos]
    return row


def matrix(st: HM) -> np.ndarray:
    n = st.n
    rows = np.zeros((n, n))
    full = [embedded(n, b, p) for b, p in zip(st.blocks, st.pis)]
    for s, block in enumerate(st.blocks):
        for i in block:
            rows[i] = full[s]
    for i in st.transients:
        rows[i] = sum(float(st.alphas[i][s]) * full[s] for s in range(st.k))
    return rows


def hm_residual(P: np.ndarray) -> dict[str, float]:
    n = P.shape[0]
    return {
        "idempotence_inf": float(np.max(np.abs(P @ P - P))),
        "row_sum_inf": float(np.max(np.abs(P @ np.ones(n) - 1.0))),
        "negative_mass": float(max(np.maximum(-P[i], 0.0).sum() for i in range(n))),
    }


def row_l1(P: np.ndarray, Q: np.ndarray) -> float:
    return float(max(np.abs(P[i] - Q[i]).sum() for i in range(P.shape[0])))


def min_mass(st: HM) -> float:
    vals = [float(x) for pi in st.pis for x in pi if x > 0.0]
    return min(vals) if vals else math.inf


def recode(st: HM, drops: list[list[int]], face_drops: dict[int, list[int]]) -> Recoding:
    old_block_of: dict[int, int] = {}
    for s, block in enumerate(st.blocks):
        for j in block:
            old_block_of[j] = s

    new_blocks: list[list[int]] = []
    new_pis: list[np.ndarray] = []
    q: list[float] = []
    removed_rows: list[int] = []

    for s, (block, pi) in enumerate(zip(st.blocks, st.pis)):
        D = sorted(set(drops[s]))
        if any(j not in block for j in D):
            raise ValueError("drop outside its block")
        K = [j for j in block if j not in D]
        if not K:
            raise ValueError("empty survivor block")
        qs = float(sum(pi[block.index(j)] for j in D))
        if not qs < 1.0:
            raise ValueError("removed recurrent mass must be < 1")
        kept = np.array([pi[block.index(j)] for j in K], dtype=float) / (1.0 - qs)
        new_blocks.append(K)
        new_pis.append(kept)
        q.append(qs)
        removed_rows.extend(D)

    new_transients = sorted(set(st.transients).union(removed_rows))
    new_alphas: dict[int, np.ndarray] = {}
    r: dict[int, float] = {}
    for i in new_transients:
        if i in old_block_of and i not in st.transients:
            a = np.zeros(st.k)
            a[old_block_of[i]] = 1.0
            new_alphas[i] = a
            continue
        old = np.array(st.alphas[i], dtype=float)
        E = sorted(set(face_drops.get(i, [])))
        ri = float(sum(old[s] for s in E))
        if not ri < 1.0:
            raise ValueError("removed transient face mass must be < 1")
        a = old.copy()
        for s in E:
            a[s] = 0.0
        a /= 1.0 - ri
        new_alphas[i] = a
        r[i] = ri

    return Recoding(st, HM(new_blocks, new_transients, new_pis, new_alphas, st.name + "_r"), drops, face_drops, q, r)


def survivor_shift(rec: Recoding) -> float:
    worst = 0.0
    for s, K in enumerate(rec.recoded.blocks):
        old_block = rec.source.blocks[s]
        old_pi = rec.source.pis[s]
        for new_pos, j in enumerate(K):
            old = float(old_pi[old_block.index(j)])
            new = float(rec.recoded.pis[s][new_pos])
            worst = max(worst, abs(new - old) / new)
    return worst


def survivor_old_relative_shift(rec: Recoding) -> float:
    worst = 0.0
    for s, K in enumerate(rec.recoded.blocks):
        old_block = rec.source.blocks[s]
        old_pi = rec.source.pis[s]
        for new_pos, j in enumerate(K):
            old = float(old_pi[old_block.index(j)])
            new = float(rec.recoded.pis[s][new_pos])
            worst = max(worst, abs(new - old) / old)
    return worst


def face_shift(rec: Recoding, i: int) -> float:
    if i not in rec.source.transients:
        return 0.0
    return float(np.abs(rec.source.alphas[i] - rec.recoded.alphas[i]).sum())


def recurrent_compress_row(x: np.ndarray, rec: Recoding) -> np.ndarray:
    y = np.array(x, dtype=float, copy=True)
    for s, D in enumerate(rec.drops):
        if not D:
            continue
        mass = float(y[D].sum())
        y[D] = 0.0
        for pos, j in enumerate(rec.recoded.blocks[s]):
            y[j] += mass * rec.recoded.pis[s][pos]
    return y


def negative_mass_row(x: np.ndarray) -> float:
    return float(np.maximum(-x, 0.0).sum())


def summarize_case(name: str, st: HM, drops: list[list[int]], face_drops: dict[int, list[int]]) -> dict:
    rec = recode(st, drops, face_drops)
    P = matrix(st)
    Pr = matrix(rec.recoded)
    eps = row_l1(P, Pr)
    max_face = max((face_shift(rec, i) for i in st.transients), default=0.0)
    return {
        "case": name,
        "n": st.n,
        "k": st.k,
        "q": rec.q,
        "q_total": rec.q_total,
        "r_max": rec.r_max,
        "eps": eps,
        "bound_2Q": 2.0 * rec.budget,
        "eps_over_2Q": eps / (2.0 * rec.budget) if rec.budget > 0 else 0.0,
        "mu_after": min_mass(rec.recoded),
        "survivor_shift_new_relative": survivor_shift(rec),
        "survivor_shift_old_relative": survivor_old_relative_shift(rec),
        "q_max": max(rec.q) if rec.q else 0.0,
        "max_face_shift": max_face,
        "face_bound_2rmax": 2.0 * rec.r_max,
        "hm_residual": hm_residual(Pr),
        "passes": (
            eps <= 2.0 * rec.budget + 1e-10
            and survivor_shift(rec) <= (max(rec.q) if rec.q else 0.0) + 1e-10
            and max_face <= 2.0 * rec.r_max + 1e-10
            and max(hm_residual(Pr).values()) <= 1e-10
        ),
    }


def explicit_cases() -> list[dict]:
    cases: list[dict] = []

    st = HM(
        blocks=[[0, 1, 2], [3, 4]],
        transients=[5, 6],
        pis=[np.array([0.12, 0.18, 0.70]), np.array([0.07, 0.93])],
        alphas={5: np.array([0.21, 0.79]), 6: np.array([0.64, 0.36])},
        name="explicit_two_block",
    )
    cases.append(summarize_case(st.name, st, [[0], [3]], {5: [0], 6: []}))

    st = HM(
        blocks=[[0, 1, 2], [3, 4, 5], [6, 7]],
        transients=[8, 9],
        pis=[
            np.array([0.19, 0.11, 0.70]),
            np.array([0.08, 0.17, 0.75]),
            np.array([0.31, 0.69]),
        ],
        alphas={8: np.array([0.30, 0.20, 0.50]), 9: np.array([0.15, 0.70, 0.15])},
        name="multi_block_simultaneous",
    )
    cases.append(summarize_case(st.name, st, [[0, 1], [3], [6]], {8: [1], 9: [0, 2]}))

    st = HM(
        blocks=[[0, 1, 2], [3]],
        transients=[4],
        pis=[np.array([0.499999, 0.499999, 0.000002]), np.array([1.0])],
        alphas={4: np.array([0.4, 0.6])},
        name="near_total_block_removal",
    )
    cases.append(summarize_case(st.name, st, [[0, 1], []], {}))

    st = HM(
        blocks=[[0, 1], [2, 3], [4]],
        transients=[5, 6],
        pis=[np.array([0.45, 0.55]), np.array([0.25, 0.75]), np.array([1.0])],
        alphas={5: np.array([0.001, 0.899, 0.100]), 6: np.array([0.35, 0.0002, 0.6498])},
        name="transient_only_faces",
    )
    cases.append(summarize_case(st.name, st, [[], [], []], {5: [0], 6: [1]}))

    return cases


def w20_stress_cases() -> list[dict]:
    out: list[dict] = []
    for nsmall, theta in [(4, 1e-5), (8, 1e-5), (20, 1e-5), (20, 1e-4)]:
        small = 0.99 * theta
        kept = 1.01 * theta
        big = 1.0 - nsmall * small - kept
        block0 = list(range(nsmall + 2))
        singleton = nsmall + 2
        transient = nsmall + 3
        st = HM(
            blocks=[block0, [singleton]],
            transients=[transient],
            pis=[np.array([small] * nsmall + [kept, big], dtype=float), np.array([1.0])],
            alphas={transient: np.array([theta / 2.0, 1.0 - theta / 2.0])},
            name=f"w20_stress_{nsmall}_{theta:g}",
        )
        row = summarize_case(st.name, st, [block0[:nsmall], []], {transient: [0]})
        row["old_eps_over_mu_after_div8"] = row["eps"] / (row["mu_after"] / 8.0)
        out.append(row)
    return out


def claimant_mixed_rate_cases() -> list[dict]:
    rng = np.random.default_rng(20260611)
    out: list[dict] = []
    for idx in range(12):
        k = 4
        block_sizes = [5, 4, 3, 4]
        blocks: list[list[int]] = []
        pis: list[np.ndarray] = []
        drops: list[list[int]] = []
        cursor = 0
        for s, size in enumerate(block_sizes):
            block = list(range(cursor, cursor + size))
            cursor += size
            ndrop = 1 + (idx + s) % max(1, size - 2)
            tiny = np.array([10.0 ** (-(6 + ((idx + s + a) % 4))) for a in range(ndrop)])
            tiny *= 1.0 + 0.2 * rng.random(ndrop)
            kept = rng.random(size - ndrop) + 0.2
            kept = kept / kept.sum() * (1.0 - float(tiny.sum()))
            pis.append(np.concatenate([tiny, kept]))
            blocks.append(block)
            drops.append(block[:ndrop])

        transients = list(range(cursor, cursor + 5))
        alphas: dict[int, np.ndarray] = {}
        face_drops: dict[int, list[int]] = {}
        for offset, i in enumerate(transients):
            small_slots = sorted({(offset + idx) % k, (offset + 2 * idx + 1) % k})
            a = rng.random(k) + 0.1
            for s in small_slots:
                a[s] = 10.0 ** (-(5 + ((idx + offset + s) % 4)))
            a /= a.sum()
            alphas[i] = a
            face_drops[i] = [s for s in small_slots if a[s] < 5e-4]
        st = HM(blocks, transients, pis, alphas, f"claimant_mixed_{idx}")
        out.append(summarize_case(st.name, st, drops, face_drops))
    return out


def randomized_cases() -> list[dict]:
    rng = np.random.default_rng(99117)
    out: list[dict] = []
    for idx in range(40):
        k = int(rng.integers(2, 6))
        blocks: list[list[int]] = []
        pis: list[np.ndarray] = []
        drops: list[list[int]] = []
        cursor = 0
        for s in range(k):
            size = int(rng.integers(2, 7))
            block = list(range(cursor, cursor + size))
            cursor += size
            raw = rng.random(size) ** 2 + 1e-4
            if idx % 10 == 0:
                raw[0] = 10.0 ** (-rng.integers(3, 8))
            pi = raw / raw.sum()
            ndrop = int(rng.integers(0, size))
            if ndrop == size:
                ndrop = size - 1
            order = list(np.argsort(pi))
            D = sorted(block[j] for j in order[:ndrop])
            blocks.append(block)
            pis.append(pi)
            drops.append(D)
        transients = list(range(cursor, cursor + int(rng.integers(0, 5))))
        alphas: dict[int, np.ndarray] = {}
        face_drops: dict[int, list[int]] = {}
        for i in transients:
            a = rng.random(k) ** 2 + 1e-5
            if k > 2:
                a[int(rng.integers(0, k))] *= 1e-4
            a /= a.sum()
            E = [s for s in range(k) if a[s] < 1e-3 and len([u for u in range(k) if u not in [s]]) > 0]
            if len(E) == k:
                E.pop()
            alphas[i] = a
            face_drops[i] = E
        st = HM(blocks, transients, pis, alphas, f"random_{idx}")
        out.append(summarize_case(st.name, st, drops, face_drops))
    return out


def transport_checks() -> dict:
    rng = np.random.default_rng(881)
    st = HM(
        blocks=[[0, 1, 2], [3, 4], [5, 6]],
        transients=[7],
        pis=[np.array([0.10, 0.20, 0.70]), np.array([0.15, 0.85]), np.array([0.40, 0.60])],
        alphas={7: np.array([0.2, 0.3, 0.5])},
        name="transport_probe",
    )
    rec = recode(st, [[0], [3], [5]], {})
    l1_viol = 0
    neg_viol = 0
    worst_l1_ratio = 0.0
    worst_neg_increase = -math.inf
    for _ in range(2000):
        x = rng.normal(size=st.n)
        y = rng.normal(size=st.n)
        rx = recurrent_compress_row(x, rec)
        ry = recurrent_compress_row(y, rec)
        before = float(np.abs(x - y).sum())
        after = float(np.abs(rx - ry).sum())
        if after > before + 1e-10:
            l1_viol += 1
        if before > 0:
            worst_l1_ratio = max(worst_l1_ratio, after / before)
        neg_before = negative_mass_row(x)
        neg_after = negative_mass_row(rx)
        worst_neg_increase = max(worst_neg_increase, neg_after - neg_before)
        if neg_after > neg_before + 1e-10:
            neg_viol += 1
    return {
        "samples": 2000,
        "l1_nonexpansive_violations": l1_viol,
        "delta_nonincrease_violations": neg_viol,
        "worst_l1_ratio": worst_l1_ratio,
        "worst_negative_mass_increase": worst_neg_increase,
    }


def sequential_compounding() -> list[dict]:
    out: list[dict] = []
    for steps in [2, 4, 8, 12]:
        survivor = 0.1 ** steps
        masses = [0.9 * (0.1 ** j) for j in range(steps)] + [survivor]
        remaining = 1.0
        q_steps = []
        for mass in masses[:-1]:
            q_steps.append(mass / remaining)
            remaining -= mass
        direct_removed = sum(masses[:-1])
        out.append(
            {
                "removed_steps": steps,
                "direct_removed_original": direct_removed,
                "direct_distance": 2.0 * direct_removed,
                "sum_relative_step_q": sum(q_steps),
                "sequential_triangle_bound": 2.0 * sum(q_steps),
                "chain_bound_over_direct_distance": (2.0 * sum(q_steps)) / (2.0 * direct_removed),
                "q_steps_first_last": [q_steps[0], q_steps[-1]],
            }
        )
    return out


def oscillating_arc_probe() -> dict:
    # Exact H-M idempotents P(t) with a coefficient tending to zero but
    # crossing any c*t threshold infinitely often.  This is C-infinity, not
    # analytic at zero, so it attacks an unstated regularity-free formulation.
    ts = [1.0 / (2.0 * math.pi * m + phase) for m in range(20, 80) for phase in (math.pi / 2, 3 * math.pi / 2)]
    vals = []
    for t in ts:
        alpha = t * (2.0 + math.sin(1.0 / t))
        vals.append(alpha / t)
    crossings = sum(1 for a, b in zip(vals, vals[1:]) if (a - 2.0) * (b - 2.0) < 0)
    return {
        "arc": "P(t) rows e1,e2, alpha(t)e1+(1-alpha(t))e2, alpha=t*(2+sin(1/t))",
        "regularity": "C-infinity after alpha(0)=0, not real analytic",
        "ratio_alpha_over_t_min": min(vals),
        "ratio_alpha_over_t_max": max(vals),
        "crossings_of_threshold_2t_in_sample": crossings,
        "analytic_comment": "real-analytic/Puiseux profiles have finite leading-order comparisons; this oscillation is excluded only if that regularity is stated",
    }


def w21_second_summary() -> dict:
    candidates = [
        Path("/tmp/codex-sigma-wall/w21_second/second_order_full_records.json"),
        Path("/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/experiments/out/w21_second/second_order_full_records.json"),
    ]
    source = next((p for p in candidates if p.exists()), None)
    if source is None:
        summary = Path("/home/tobias/Projects/almost-idempotent-positive-maps/agent-A/explorations/classical-portfolio/experiments/out/w21_second/second_order_filtered_summary.txt")
        return {"available": False, "fallback_summary": summary.read_text(encoding="utf-8") if summary.exists() else ""}

    data = json.loads(source.read_text(encoding="utf-8"))
    records = data.get("records", [])
    local: list[tuple[float, dict, dict, float]] = []
    transition: list[tuple[float, dict, dict, float]] = []
    for rec in records:
        min_entry = float(rec.get("min_positive_entry", 0.0))
        cutoff = 0.1 * min_entry
        for sample in rec.get("samples", []):
            ratio = sample.get("H_over_delta")
            if not isinstance(ratio, (int, float)) or not math.isfinite(float(ratio)):
                continue
            item = (float(ratio), rec, sample, cutoff)
            if float(sample["t"]) < cutoff:
                local.append(item)
            else:
                transition.append(item)
    local.sort(key=lambda x: x[0], reverse=True)
    transition.sort(key=lambda x: x[0], reverse=True)
    sharp = [x for x in transition if x[0] >= 1.9]
    top = []
    for ratio, rec, sample, cutoff in sharp[:8]:
        min_entry = float(rec.get("min_positive_entry", 0.0))
        top.append(
            {
                "ratio": ratio,
                "stratum": rec.get("stratum"),
                "source": rec.get("source"),
                "t": sample.get("t"),
                "min_positive_entry": min_entry,
                "t_over_min_entry": float(sample.get("t", 0.0)) / min_entry if min_entry > 0 else math.inf,
                "visible": sample.get("visible"),
                "vertices": sample.get("vertices"),
            }
        )
    return {
        "available": True,
        "source": str(source),
        "records": len(records),
        "local_samples": len(local),
        "transition_samples": len(transition),
        "max_local_ratio": local[0][0] if local else None,
        "max_transition_ratio": transition[0][0] if transition else None,
        "sharp_transition_count_ge_1p9": len(sharp),
        "top_sharp_transition": top,
    }


def aggregate() -> dict:
    all_cases = explicit_cases()
    stress = w20_stress_cases()
    mixed = claimant_mixed_rate_cases()
    randoms = randomized_cases()
    return {
        "explicit_cases": all_cases,
        "w20_stress": stress,
        "claimant_mixed_rate_reimplementation": mixed,
        "random_cases": randoms,
        "transport_checks": transport_checks(),
        "sequential_compounding": sequential_compounding(),
        "oscillating_arc_probe": oscillating_arc_probe(),
        "w21_second": w21_second_summary(),
        "totals": {
            "case_count": len(all_cases) + len(stress) + len(mixed) + len(randoms),
            "failed_cases": [r["case"] for group in (all_cases, stress, mixed, randoms) for r in group if not r["passes"]],
            "worst_eps_over_2Q": max((r["eps_over_2Q"] for group in (all_cases, stress, mixed, randoms) for r in group), default=0.0),
            "worst_old_relative_survivor_shift": max((r["survivor_shift_old_relative"] for group in (all_cases, stress, mixed, randoms) for r in group), default=0.0),
        },
    }


def write_summary(out: dict) -> str:
    lines: list[str] = []
    totals = out["totals"]
    lines.append("independent w21 recode audit numerics")
    lines.append(f"cases checked: {totals['case_count']}")
    lines.append(f"failed removed-mass/exactness cases: {len(totals['failed_cases'])}")
    lines.append(f"worst eps/(2Q): {totals['worst_eps_over_2Q']:.12g}")
    lines.append(f"worst survivor shift relative to old mass: {totals['worst_old_relative_survivor_shift']:.12g}")
    lines.append("")
    lines.append("w20 stress family")
    for row in out["w20_stress"]:
        lines.append(
            "{case}: q={q_total:.12g} r={r_max:.12g} eps={eps:.12g} "
            "2Q={bound_2Q:.12g} eps/(2Q)={eps_over_2Q:.9g} "
            "old eps/(mu/8)={old_eps_over_mu_after_div8:.9g} passes={passes}".format(**row)
        )
    lines.append("")
    lines.append("edge cases")
    for row in out["explicit_cases"]:
        lines.append(
            "{case}: q_total={q_total:.12g} r={r_max:.12g} eps/(2Q)={eps_over_2Q:.9g} "
            "mu_after={mu_after:.12g} shift_new={survivor_shift_new_relative:.12g} "
            "shift_old={survivor_shift_old_relative:.12g} passes={passes}".format(**row)
        )
    lines.append("")
    mixed = out["claimant_mixed_rate_reimplementation"]
    lines.append(
        "claimant mixed-rate reimplementation: cases={} failures={} worst eps/(2Q)={:.9g}".format(
            len(mixed), sum(1 for r in mixed if not r["passes"]), max(r["eps_over_2Q"] for r in mixed)
        )
    )
    randoms = out["random_cases"]
    lines.append(
        "random hostile cases: cases={} failures={} worst eps/(2Q)={:.9g}".format(
            len(randoms), sum(1 for r in randoms if not r["passes"]), max(r["eps_over_2Q"] for r in randoms)
        )
    )
    t = out["transport_checks"]
    lines.append(
        "recurrent transport: l1 violations={l1_nonexpansive_violations} "
        "delta violations={delta_nonincrease_violations} worst_l1_ratio={worst_l1_ratio:.9g}".format(**t)
    )
    lines.append("")
    lines.append("sequential compounding trap")
    for row in out["sequential_compounding"]:
        lines.append(
            "steps={removed_steps}: direct_removed={direct_removed_original:.12g} "
            "sum_step_q={sum_relative_step_q:.12g} chain/direct={chain_bound_over_direct_distance:.9g}".format(**row)
        )
    osc = out["oscillating_arc_probe"]
    lines.append("")
    lines.append(
        "oscillating C-infinity profile: alpha/t in [{:.3g},{:.3g}], sampled threshold crossings={}".format(
            osc["ratio_alpha_over_t_min"], osc["ratio_alpha_over_t_max"], osc["crossings_of_threshold_2t_in_sample"]
        )
    )
    w21 = out["w21_second"]
    lines.append("")
    lines.append("w21_second boundary records")
    if w21.get("available"):
        lines.append(
            "records={records} local={local_samples} max_local={max_local_ratio} "
            "transition={transition_samples} max_transition={max_transition_ratio} "
            "sharp_ge_1p9={sharp_transition_count_ge_1p9}".format(**w21)
        )
        for row in w21["top_sharp_transition"][:5]:
            lines.append(
                "sharp ratio={ratio:.12g} stratum={stratum} t={t:.3g} "
                "min_entry={min_positive_entry:.3g} t/min={t_over_min_entry:.6g} "
                "visible={visible} vertices={vertices}".format(**row)
            )
    else:
        lines.append("raw JSON unavailable; used saved summary fallback")
    return "\n".join(lines) + "\n"


def main() -> None:
    out = aggregate()
    Path("independent_recode_results.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
    summary = write_summary(out)
    Path("independent_recode_summary.txt").write_text(summary, encoding="utf-8")
    print(summary)


if __name__ == "__main__":
    main()
