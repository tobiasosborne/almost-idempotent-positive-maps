#!/usr/bin/env python3
"""
check-defs.py — Definitions DB gate (Layer 0).

Validates definitions/<id>.md shards:
  * required fields present; id == filename stem; kind/status from the allowed sets
  * DEDUP/DRIFT: no two shards claim the same term or alias  (the core guard)
  * CITED: source is a known refs/ source-id and the 16-hex sha256 prefix is in the
    refs/manifest/checksums.sha256 manifest (WARN if the gitignored payload is absent locally)
  * CONSENSUS-GATE: consensus|original shards must record `consensus:`; `status: draft` -> WARN

Usage:
  python3 scripts/check-defs.py --check            # validate (exit 1 on any ERROR)
  python3 scripts/check-defs.py --generate-index   # (re)write definitions/INDEX.md
  python3 scripts/check-defs.py                     # both
"""
import sys, re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFS = ROOT / "definitions"
MANIFEST = ROOT / "refs" / "manifest" / "checksums.sha256"

KINDS = {"cited", "consensus", "original"}
STATUSES = {"draft", "locked"}
REQUIRED = ["id", "term", "kind", "status"]
SKIP = {"README.md", "INDEX.md"}

errors, warnings = [], []
def err(m): errors.append(m)
def warn(m): warnings.append(m)


def parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    block = text[3:end].strip("\n")
    body = text[end + 4:]
    fm = {}
    for line in block.splitlines():
        line = line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            err(f"{path.name}: frontmatter line without ':' -> {line!r}")
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip()
    return fm, body


def load_manifest():
    """Return (prefix2path, source_ids, present_paths) from refs/manifest/checksums.sha256."""
    prefix2path, source_ids, present = {}, set(), set()
    if not MANIFEST.exists():
        warn(f"manifest absent: {MANIFEST.relative_to(ROOT)} (cannot verify cited hashes)")
        return prefix2path, source_ids, present
    for line in MANIFEST.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        h, _, p = line.partition("  ")
        p = p.lstrip("./")
        prefix2path[h[:16]] = p
        if "/" in p:
            source_ids.add(p.split("/", 1)[0])
        if (ROOT / "refs" / p).exists():
            present.add(p)
    return prefix2path, source_ids, present


def main():
    args = set(sys.argv[1:]) or {"--check", "--generate-index"}
    shards = sorted(p for p in DEFS.glob("*.md") if p.name not in SKIP)
    prefix2path, source_ids, present = load_manifest()

    parsed = []
    term_owner, alias_owner = {}, {}
    for path in shards:
        fm, _ = parse_frontmatter(path)
        if fm is None:
            err(f"{path.name}: missing/unterminated frontmatter")
            continue
        for field in REQUIRED:
            if not fm.get(field):
                err(f"{path.name}: missing required field '{field}'")
        if fm.get("id") and fm["id"] != path.stem:
            err(f"{path.name}: id '{fm.get('id')}' != filename stem '{path.stem}'")
        if fm.get("kind") and fm["kind"] not in KINDS:
            err(f"{path.name}: kind '{fm['kind']}' not in {sorted(KINDS)}")
        if fm.get("status") and fm["status"] not in STATUSES:
            err(f"{path.name}: status '{fm['status']}' not in {sorted(STATUSES)}")

        # dedup / drift: one term + one alias namespace across the whole DB
        term = (fm.get("term") or "").strip()
        names = [term] + [a.strip() for a in (fm.get("aliases", "") or "").split(";") if a.strip()]
        for nm in names:
            key = nm.lower()
            if not key:
                continue
            if key == term.lower():
                if key in term_owner:
                    err(f"DRIFT: term/alias '{nm}' claimed by both {term_owner[key]} and {path.name}")
                term_owner[key] = path.name
            if key in alias_owner and alias_owner[key] != path.name:
                err(f"DRIFT: name '{nm}' claimed by both {alias_owner[key]} and {path.name}")
            alias_owner[key] = path.name

        kind, status = fm.get("kind"), fm.get("status")
        if kind == "cited":
            src, sha = fm.get("source"), (fm.get("sha256") or "").strip()
            if src and source_ids and src not in source_ids:
                err(f"{path.name}: cited source '{src}' not a refs/ source-id {sorted(source_ids)}")
            if sha and sha != "-":
                if prefix2path and sha not in prefix2path:
                    err(f"{path.name}: sha256 prefix '{sha}' not in refs manifest")
                elif sha in prefix2path:
                    p = prefix2path[sha]
                    if src and not p.startswith(src + "/"):
                        warn(f"{path.name}: sha256 {sha} -> {p}, not under source '{src}'")
                    if p not in present:
                        warn(f"{path.name}: source payload absent locally ({p}); hash unverifiable in this checkout")
        elif kind in ("consensus", "original"):
            if not fm.get("consensus"):
                err(f"{path.name}: {kind} shard must record 'consensus:'")
        if status == "draft":
            warn(f"{path.name}: status=draft (not yet consensus-gated)")
        parsed.append(fm)

    if "--generate-index" in args and not errors:
        rows = ["| id | term | kind | status | source |", "|---|---|---|---|---|"]
        for fm in sorted(parsed, key=lambda d: d.get("id", "")):
            rows.append("| `{id}` | {term} | {kind} | {status} | {source} |".format(
                id=fm.get("id", "?"), term=fm.get("term", "?"),
                kind=fm.get("kind", "?"), status=fm.get("status", "?"),
                source=fm.get("source", "-")))
        idx = ("<!-- GENERATED by scripts/check-defs.py --generate-index. Do not hand-edit. -->\n"
               f"# Definitions index ({len(parsed)} terms)\n\n" + "\n".join(rows) + "\n")
        (DEFS / "INDEX.md").write_text(idx, encoding="utf-8")
        print(f"wrote definitions/INDEX.md ({len(parsed)} terms)")

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\ncheck-defs: {len(parsed)} shards, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
