#!/usr/bin/env python3
"""
Red-green tests for scripts/argument.py — the argument-DAG linker. Written test-FIRST.
Drives the pure check functions with synthetic registries + injected af "workspace facts";
no real af workspaces needed. Run: python3 scripts/tests/test_argument.py
"""
import importlib.util
import pathlib
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
_spec = importlib.util.spec_from_file_location("argument", ROOT / "scripts" / "argument.py")
ag = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ag)

passed = failed = 0
def check(name, cond):
    global passed, failed
    if cond: passed += 1; print(f"PASS  {name}")
    else:    failed += 1; print(f"FAIL  {name}")
def has(msgs, sub): return any(sub in m for m in msgs)

def L(id, deps=(), defs=(), af="none", status="proved", contract="C", workspace=None):
    return {"id": id, "deps": list(deps), "defs": list(defs), "af": af,
            "status": status, "contract": contract,
            "workspace": workspace or f"proofs/{id}"}

# --- check_acyclic ---
chain = [L("a", deps=[]), L("b", deps=["a"]), L("c", deps=["b"])]
check("acyclic chain -> no error", ag.check_acyclic(chain) == [])
cyc = [L("a", deps=["b"]), L("b", deps=["a"])]
check("cycle is caught", has(ag.check_acyclic(cyc), "cycle"))

# --- check_imports ---
ids_ok = [L("a"), L("b", deps=["a"], defs=["def-x"])]
check("resolvable imports -> no error", ag.check_imports(ids_ok, {"def-x"}) == [])
bad_dep = [L("b", deps=["nope"])]
check("dangling dep is caught", has(ag.check_imports(bad_dep, set()), "nope"))
bad_def = [L("b", defs=["def-nope"])]
check("dangling def is caught", has(ag.check_imports(bad_def, {"def-x"}), "def-nope"))

# --- check_status: validated cannot rest on unvalidated; frontier/blocked ---
inconsistent = [L("a", af="none"), L("b", deps=["a"], af="validated")]
errs, ready, blocked = ag.check_status(inconsistent)
check("validated-on-unvalidated is caught", has(errs, "validated"))
prop = [L("a", af="validated", status="proved"),
        L("b", deps=["a"], af="none", status="proved"),
        L("c", deps=["b"], af="none", status="proved")]
errs, ready, blocked = ag.check_status(prop)
check("frontier: b ready (deps validated)", "b" in ready)
check("frontier: c blocked (dep b not validated)", "c" in blocked)
check("frontier: c not ready", "c" not in ready)

# --- check_contracts: drift between registry and af root ---
lemmas = [L("a", contract="For r in A,  q_r >= 0.")]   # note: double space after comma
ws_match = {"a": "For r in A, q_r >= 0."}              # whitespace differs only (single space)
ws_drift = {"a": "For r in A, q_r >= 1."}
check("contract match (whitespace) -> no error", ag.check_contracts(lemmas, ws_match) == [])
check("contract drift is caught", has(ag.check_contracts(lemmas, ws_drift), "drift"))

# --- check_brittleness: oversized af tree warns REFACTOR ---
lemmas = [L("a"), L("b")]
warns = ag.check_brittleness(lemmas, {"a": 5, "b": 99}, threshold=12)
check("small tree no warn", not has(warns, "proofs/a"))
check("oversized tree warns REFACTOR", has(warns, "REFACTOR") and has(warns, "b"))

# --- check_orphans ---
lemmas = [L("a", af="validated", workspace="proofs/a"), L("b", af="none", workspace="proofs/b")]
errs = ag.check_orphans(lemmas, {"proofs/a"})            # b has af=none so missing dir is OK
check("af!=none with missing workspace dir is caught", errs == [])
errs = ag.check_orphans([L("a", af="seeded", workspace="proofs/a")], set())
check("seeded lemma missing workspace dir is caught", has(errs, "proofs/a"))
errs = ag.check_orphans([L("a", af="validated", workspace="proofs/a")], {"proofs/a", "proofs/ghost"})
check("workspace dir with no registry entry is caught", has(errs, "ghost"))

# --- parse_registry round-trip ---
with tempfile.TemporaryDirectory() as d:
    d = pathlib.Path(d); (d / "lemmas").mkdir()
    (d / "lemmas" / "lem-x.md").write_text(
        "---\nid: lem-x\nkind: lemma\ncontract: Foo.\ndefs: def-a; def-b\ndeps: lem-y\n"
        "status: proved\naf: none\nowner: A\nworkspace: proofs/lem-x\n---\nbody\n", encoding="utf-8")
    lemmas, errs = ag.parse_registry(d)
    check("parse_registry reads one lemma", len(lemmas) == 1)
    check("parse_registry splits defs", lemmas[0]["defs"] == ["def-a", "def-b"])
    check("parse_registry splits deps", lemmas[0]["deps"] == ["lem-y"])

print(f"\n{passed} passed, {failed} failed")
raise SystemExit(1 if failed else 0)
