#!/usr/bin/env python3
"""
argument.py — the LINKER for the argument registry (Layer 1, the module graph / DAG).

Enforces the contracts between proof modules and generates the index + dependency graph:
  * acyclic dependency DAG
  * imports resolve (deps -> registry ids; defs -> definitions/ ids)
  * contract match (registry contract == af workspace root conjecture)
  * status propagation (af=validated requires deps validated) + ready-frontier / blocked
  * brittleness (oversized af tree => REFACTOR signal)
  * orphans (registry<->proofs/ workspace correspondence)

Pure check functions (unit-tested in scripts/tests/test_argument.py) take a parsed registry
plus injected "workspace facts"; main() builds those facts from `af ... -f json` + the filesystem.

Usage:
  python3 scripts/argument.py --check       # validate (exit 1 on ERROR)
  python3 scripts/argument.py --generate     # (re)write argument/{INDEX,DAG}.md
  python3 scripts/argument.py --show <id>     # local map of one result: contract, defs,
                                              #   direct deps/dependents, full ancestor/descendant closures
  python3 scripts/argument.py --sync-beads    # (dry-run stub) mirror registry into beads

The whole-DAG map is argument/DAG.md (Mermaid, generated) + argument/INDEX.md (table, generated).
"""
import sys
import json
import shutil
import subprocess
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
ARG_DIR = ROOT / "argument"
DEFS_DIR = ROOT / "definitions"
PROOFS_DIR = ROOT / "proofs"
KINDS = {"lemma", "proposition", "theorem", "corollary", "open-problem", "obstruction"}
MATH_STATUS = {"proved", "cited", "consensus", "open", "obstruction", "disproved"}
AF_STATES = {"none", "seeded", "validated"}
LIST_FIELDS = ("defs", "deps")
NODE_THRESHOLD = 12


def normalize(s):
    return " ".join((s or "").split())


def _parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    fm = {}
    for line in text[3:end].strip("\n").splitlines():
        line = line.rstrip()
        if not line or line.lstrip().startswith("#") or ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip()
    for f in LIST_FIELDS:
        fm[f] = [x.strip() for x in fm.get(f, "").split(";") if x.strip()]
    return fm


def parse_registry(arg_dir):
    """Read <arg_dir>/lemmas/*.md -> (lemmas, errors)."""
    arg_dir = pathlib.Path(arg_dir)
    lemmas, errors = [], []
    lemdir = arg_dir / "lemmas"
    for path in sorted(lemdir.glob("*.md")) if lemdir.exists() else []:
        if path.name in ("README.md", "INDEX.md"):
            continue
        fm = _parse_frontmatter(path)
        if fm is None:
            errors.append(f"{path.name}: missing/unterminated frontmatter")
            continue
        if fm.get("id") and fm["id"] != path.stem:
            errors.append(f"{path.name}: id '{fm.get('id')}' != filename stem '{path.stem}'")
        if fm.get("kind") and fm["kind"] not in KINDS:
            errors.append(f"{path.name}: kind '{fm['kind']}' not in {sorted(KINDS)}")
        if fm.get("status") and fm["status"] not in MATH_STATUS:
            errors.append(f"{path.name}: status '{fm['status']}' not in {sorted(MATH_STATUS)}")
        if fm.get("af", "none") not in AF_STATES:
            errors.append(f"{path.name}: af '{fm.get('af')}' not in {sorted(AF_STATES)}")
        lemmas.append(fm)
    return lemmas, errors


# ---------- pure checks ----------

def check_acyclic(lemmas):
    ids = {l["id"] for l in lemmas}
    adj = {l["id"]: [d for d in l.get("deps", []) if d in ids] for l in lemmas}
    errors, state = [], {}  # 0=unvisited 1=in-stack 2=done

    def dfs(u, stack):
        state[u] = 1
        for v in adj.get(u, []):
            if state.get(v, 0) == 1:
                cyc = stack[stack.index(v):] + [v]
                errors.append("cycle detected: " + " -> ".join(cyc))
                return True
            if state.get(v, 0) == 0 and dfs(v, stack + [v]):
                return True
        state[u] = 2
        return False

    for l in lemmas:
        if state.get(l["id"], 0) == 0:
            if dfs(l["id"], [l["id"]]):
                break
    return errors


def check_imports(lemmas, def_ids):
    ids = {l["id"] for l in lemmas}
    errors = []
    for l in lemmas:
        for d in l.get("deps", []):
            if d not in ids:
                errors.append(f"{l['id']}: unknown dep '{d}' (not a registry id)")
        for df in l.get("defs", []):
            if df not in def_ids:
                errors.append(f"{l['id']}: unknown def '{df}' (not in definitions/)")
    return errors


def check_status(lemmas):
    af_of = {l["id"]: l.get("af", "none") for l in lemmas}
    status_of = {l["id"]: l.get("status") for l in lemmas}
    # A dep is AVAILABLE iff its af is validated OR it is a ground-truth leaf (status=cited:
    # cited background like Kadison's inequality is never af-proven yet is available to build on).
    # Only status=='cited' counts as a leaf — NOT consensus/open/obstruction/disproved/proved.
    def available(d):
        return af_of.get(d, "none") == "validated" or status_of.get(d) == "cited"
    errors, ready, blocked = [], [], []
    for l in lemmas:
        deps = l.get("deps", [])
        deps_available = all(available(d) for d in deps)
        if l.get("af") == "validated" and not deps_available:
            bad = [d for d in deps if not available(d)]
            errors.append(f"{l['id']}: af=validated but dep(s) not validated: {bad}")
        if l.get("af", "none") != "validated" and not deps_available:
            blocked.append(l["id"])
        if (l.get("af", "none") in ("none", "seeded")
                and l.get("status") in ("proved", "consensus")
                and deps_available):
            ready.append(l["id"])
    return errors, ready, blocked


def check_contracts(lemmas, ws_contracts):
    by_id = {l["id"]: l for l in lemmas}
    errors = []
    for lid, ws_stmt in ws_contracts.items():
        l = by_id.get(lid)
        if l is None:
            continue
        if normalize(ws_stmt) != normalize(l.get("contract", "")):
            errors.append(f"contract drift: {lid} — af root conjecture != registry contract")
    return errors


def check_brittleness(lemmas, nodecounts, threshold=NODE_THRESHOLD):
    warnings = []
    for l in lemmas:
        nc = nodecounts.get(l["id"])
        if nc is not None and nc > threshold:
            warnings.append(f"REFACTOR: {l['workspace']} has {nc} nodes (>{threshold}) "
                            f"— factor {l['id']} into sub-lemmas")
    return warnings


def check_orphans(lemmas, ws_dirs):
    errors = []
    declared = {}
    for l in lemmas:
        ws = l.get("workspace")
        declared[ws] = l["id"]
        if l.get("af", "none") != "none" and ws not in ws_dirs:
            errors.append(f"{l['id']}: af={l.get('af')} but workspace dir missing: {ws}")
    for ws in ws_dirs:
        if ws not in declared:
            errors.append(f"orphan workspace (no registry entry): {ws}")
    return errors


# ---------- node map: ancestor/descendant closures (--show) ----------

def _closure(lemmas, root, reverse):
    """Transitive set reachable from `root` along deps edges (reverse=False) or
    reverse deps edges (reverse=True). Excludes `root`; ignores dangling deps
    (check_imports reports those). Returns None if `root` is not a registry id."""
    by = {l["id"]: l for l in lemmas}
    if root not in by:
        return None
    if reverse:
        adj = {i: [] for i in by}
        for l in lemmas:
            for d in l.get("deps", []):
                if d in by:
                    adj[d].append(l["id"])
    else:
        adj = {i: [d for d in by[i].get("deps", []) if d in by] for i in by}
    seen, stack = set(), list(adj[root])
    while stack:
        n = stack.pop()
        if n in seen:
            continue
        seen.add(n)
        stack.extend(adj.get(n, []))
    seen.discard(root)  # exclude root even if a cycle through it sneaks in (--show runs pre-acyclic-check)
    return seen


def deps_closure(lemmas, root):
    """All transitive prerequisites of `root` (the ancestors it depends on)."""
    return _closure(lemmas, root, reverse=False)


def dependents_closure(lemmas, root):
    """All transitive dependents of `root` (the descendants that rely on it)."""
    return _closure(lemmas, root, reverse=True)


def format_show(lemmas, root):
    """Human-readable local map of one result: its contract, direct defs/deps,
    direct dependents, and the full ancestor/descendant closures."""
    by = {l["id"]: l for l in lemmas}
    if root not in by:
        return (f"unknown id '{root}' — not a registry result. "
                f"List them with: python3 scripts/argument.py (or see argument/INDEX.md).")
    l = by[root]

    def tag(i):
        x = by.get(i)
        return f"{i}[{x.get('status','?')}/{x.get('af','none')}]" if x else f"{i}[MISSING]"

    direct_deps = l.get("deps", [])
    direct_dependents = sorted(i for i in by if root in by[i].get("deps", []))
    anc = sorted(deps_closure(lemmas, root))
    desc = sorted(dependents_closure(lemmas, root))
    return "\n".join([
        f"# {root}  [{l.get('status','?')}/{l.get('af','none')}]  "
        f"kind={l.get('kind','?')}  owner={l.get('owner','-')}",
        f"contract: {l.get('contract','')}",
        f"defs:        {'; '.join(l.get('defs', [])) or '(none)'}",
        f"deps (direct prerequisites): {', '.join(tag(d) for d in direct_deps) or '(none)'}",
        f"dependents (direct):         {', '.join(tag(d) for d in direct_dependents) or '(none)'}",
        f"ancestors   (all {len(anc)} prerequisites): {', '.join(anc) or '(none)'}",
        f"descendants (all {len(desc)} dependents):   {', '.join(desc) or '(none)'}",
    ])


# ---------- integration (filesystem + af) ----------

def load_def_ids():
    ids = set()
    for p in DEFS_DIR.glob("*.md") if DEFS_DIR.exists() else []:
        if p.name in ("README.md", "INDEX.md"):
            continue
        fm = _parse_frontmatter(p)
        if fm and fm.get("id"):
            ids.add(fm["id"])
    return ids


def scan_workspaces():
    if not PROOFS_DIR.exists():
        return set()
    return {f"proofs/{d.name}" for d in PROOFS_DIR.iterdir()
            if d.is_dir() and (d / "ledger").exists()}


def af_introspect(workspace):
    """Return {'contract':str,'nodes':int,'epistemic':str,'clean':bool} or None."""
    ws = ROOT / workspace
    if not shutil.which("af") or not (ws / "ledger").exists():
        return None
    try:
        root = json.loads(subprocess.run(["af", "get", "1", "-d", str(ws), "-f", "json"],
                                          capture_output=True, text=True, timeout=30).stdout)
        st = json.loads(subprocess.run(["af", "status", "-d", str(ws), "-f", "json"],
                                       capture_output=True, text=True, timeout=30).stdout)
    except Exception:
        return None
    stats = st.get("statistics", {})
    epi = stats.get("epistemic_state", {})
    return {"contract": root.get("statement", ""),
            "nodes": stats.get("total_nodes", 0),
            "epistemic": root.get("epistemic_state", ""),
            "clean": stats.get("taint_state", {}).get("clean", 0) == stats.get("total_nodes", -1)}


def generate(lemmas):
    rows = ["| id | kind | status | af | owner | contract |", "|---|---|---|---|---|---|"]
    for l in sorted(lemmas, key=lambda d: d.get("id", "")):
        c = l.get("contract", "")
        c = (c[:80] + "…") if len(c) > 80 else c
        rows.append(f"| `{l.get('id','?')}` | {l.get('kind','?')} | {l.get('status','?')} | "
                    f"{l.get('af','none')} | {l.get('owner','-')} | {c} |")
    (ARG_DIR / "INDEX.md").write_text(
        "<!-- GENERATED by scripts/argument.py --generate. Do not hand-edit. -->\n"
        f"# Argument index ({len(lemmas)} results)\n\n" + "\n".join(rows) + "\n", encoding="utf-8")

    edges = []
    for l in lemmas:
        for d in l.get("deps", []):
            edges.append(f"  {d} --> {l['id']}")
    nodes = [f'  {l["id"]}["{l["id"]}<br/>{l.get("status","")}/{l.get("af","none")}"]' for l in lemmas]
    (ARG_DIR / "DAG.md").write_text(
        "<!-- GENERATED by scripts/argument.py --generate. Do not hand-edit. -->\n"
        f"# Argument DAG ({len(lemmas)} results, {len(edges)} edges)\n\n```mermaid\ngraph LR\n"
        + "\n".join(nodes) + "\n" + "\n".join(edges) + "\n```\n", encoding="utf-8")


def main(argv):
    argv = list(argv)
    if "--show" in argv:
        i = argv.index("--show")
        target = argv[i + 1] if i + 1 < len(argv) else None
        if not target or target.startswith("--"):   # missing / flag-shaped -> usage, not "unknown id"
            print("usage: python3 scripts/argument.py --show <id>")
            return 2
        lemmas, _ = parse_registry(ARG_DIR)
        print(format_show(lemmas, target))
        return 0 if any(l.get("id") == target for l in lemmas) else 1
    args = set(argv) or {"--check", "--generate"}
    lemmas, errors = parse_registry(ARG_DIR)
    def_ids = load_def_ids()
    ws_dirs = scan_workspaces()

    ws_contracts, nodecounts = {}, {}
    for l in lemmas:
        if l.get("af", "none") != "none":
            facts = af_introspect(l.get("workspace", ""))
            if facts:
                ws_contracts[l["id"]] = facts["contract"]
                nodecounts[l["id"]] = facts["nodes"]

    errors += check_acyclic(lemmas)
    errors += check_imports(lemmas, def_ids)
    serr, ready, blocked = check_status(lemmas)
    errors += serr
    errors += check_contracts(lemmas, ws_contracts)
    errors += check_orphans(lemmas, ws_dirs)
    warnings = check_brittleness(lemmas, nodecounts)

    if "--generate" in args and not errors:
        generate(lemmas)
        print(f"wrote argument/INDEX.md + DAG.md ({len(lemmas)} results)")
    if "--sync-beads" in args:
        print("[--sync-beads] dry-run stub: would ensure one bd issue per lemma with dep edges "
              "(deferred until the registry is seeded; serialize bd calls).")

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\nargument: {len(lemmas)} results, {len(ready)} ready, {len(blocked)} blocked, "
          f"{len(errors)} errors, {len(warnings)} warnings")
    if ready:
        print("  ready frontier:", ", ".join(sorted(ready)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
