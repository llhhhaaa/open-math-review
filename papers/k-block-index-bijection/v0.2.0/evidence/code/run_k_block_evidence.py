"""Build a machine-readable G2 certificate for the k-block transfer map."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import platform
import sys
from datetime import UTC, datetime
from pathlib import Path


HERE = Path(__file__).resolve().parent
BIJECTION_PATH = HERE / "k_block_bijection.py"


def _load_bijection_module():
    spec = importlib.util.spec_from_file_location("candidate02_k_block_bijection", BIJECTION_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load the k-block bijection module")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_evidence(maximum_k: int, maximum_total: int) -> dict[str, object]:
    """Run map-based and product-based checks over the requested finite range."""
    bijection = _load_bijection_module()
    finite_bijection = bijection.finite_certificate(maximum_k, maximum_total)
    independent = [
        bijection.independent_count_check(k, maximum_total)
        for k in range(2, maximum_k + 1)
    ]
    passed = bool(finite_bijection["all_checks_passed"]) and all(
        bool(item["matches"]) for item in independent
    )
    return {
        "schema_version": 2,
        "theorem_scope": "k-block-index identity for k-regular and k-strict partitions",
        "finite_bijection": finite_bijection,
        "independent_generating_functions": independent,
        "verdict": "pass" if passed else "fail",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--maximum-k", type=int, default=8)
    parser.add_argument("--maximum-total", type=int, default=40)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    evidence = build_evidence(args.maximum_k, args.maximum_total)
    evidence.update(
        {
            "run_id": args.run_id,
            "generated_at_utc": datetime.now(UTC).replace(microsecond=0).isoformat(),
            "command_line": sys.argv,
            "environment": {
                "python": sys.version,
                "platform": platform.platform(),
            },
            "source_hashes": {
                "run_k_block_evidence.py": sha256(Path(__file__)),
                "k_block_bijection.py": sha256(BIJECTION_PATH),
            },
            "claim_source": {
                "arxiv_id": "2607.16690v1",
                "url": "https://arxiv.org/abs/2607.16690v1",
                "statement_status": "The source explicitly says that the proof is left to the reader.",
            },
        }
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(evidence, indent=2))
    if evidence["verdict"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
