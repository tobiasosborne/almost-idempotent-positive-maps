#!/usr/bin/env sh
# Pre-commit / session-close validation suite (the local "CI"). Non-zero exit fails the commit.
# Wired into .beads/hooks/pre-commit (bd owns core.hooksPath=.beads/hooks).
ROOT="$(git rev-parse --show-toplevel)" || exit 1
cd "$ROOT" || exit 1
fail() { echo "[check-all] FAILED: $1"; exit 1; }

echo "[check-all] definitions gate (drift/dedup, cited SHA256, consensus-gate)"
python3 scripts/check-defs.py --check || fail "check-defs"

echo "[check-all] argument linker (acyclic, imports, contracts, status, brittleness, orphans)"
python3 scripts/argument.py --check || fail "argument"

echo "[check-all] tooling tests (TDD)"
for t in scripts/tests/test_check_defs.py scripts/tests/test_argument.py; do
  out=$(python3 "$t" 2>&1) || { echo "$out"; fail "$t"; }
done

# TODO (Phase 2b+): scripts/check-provenance.py ; (cd report && latexmk -pdf -halt-on-error main.tex) ;
#                    af replay --verify in each proofs/* workspace ; lean build (Phase 5).
echo "[check-all] OK"
