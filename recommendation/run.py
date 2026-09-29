#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .engine import recommend


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", default="recommendation/seed/user_profiles.jsonl")
    parser.add_argument("--idols", default="recommendation/seed/idol_features.jsonl")
    parser.add_argument("--output", default="recommendation/output/recommendations.jsonl")
    parser.add_argument("--top-k", type=int, default=5)
    args = parser.parse_args()

    result = recommend(read_jsonl(Path(args.profile))[0], read_jsonl(Path(args.idols)), args.top_k)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in result) + "\n", encoding="utf-8")
    print(f"wrote {len(result)} recommendations -> {output}")


if __name__ == "__main__":
    main()
