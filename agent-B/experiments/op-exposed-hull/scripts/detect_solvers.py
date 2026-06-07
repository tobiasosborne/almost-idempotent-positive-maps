#!/usr/bin/env python3
"""Record solver and CAS availability for reproducible numerical runs."""

from __future__ import annotations

import argparse
import importlib
import json
import shutil
import subprocess
import sys
from pathlib import Path


def command_output(cmd: list[str]) -> dict:
    path = shutil.which(cmd[0])
    if path is None:
        return {"available": False, "path": None, "output": None}
    try:
        result = subprocess.run(cmd, check=False, text=True, capture_output=True, timeout=15)
    except Exception as exc:  # pragma: no cover - environment detail only
        return {"available": True, "path": path, "output": None, "error": repr(exc)}
    return {
        "available": True,
        "path": path,
        "returncode": result.returncode,
        "output": (result.stdout + result.stderr).strip(),
    }


def module_info(name: str) -> dict:
    try:
        module = importlib.import_module(name)
    except Exception as exc:
        return {"available": False, "error": repr(exc)}
    version = getattr(module, "__version__", None)
    extra = {}
    if name == "cvxpy":
        extra["installed_solvers"] = module.installed_solvers()
    if name == "gurobipy":
        extra["gurobi_version"] = module.gurobi.version()
    return {"available": True, "version": version, **extra}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()

    info = {
        "python": sys.version,
        "commands": {
            "gurobi_cl": command_output(["gurobi_cl", "--version"]),
            "wolframscript": command_output(["wolframscript", "-version"]),
            "wolframscript_smoke": command_output(["wolframscript", "-code", "1+1"]),
        },
        "python_modules": {
            name: module_info(name)
            for name in ["numpy", "scipy", "cvxpy", "gurobipy", "ortools"]
        },
        "primary_lp_backend": "scipy.optimize.linprog(method='highs')",
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(info, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
