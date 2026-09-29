#!/usr/bin/env python3
"""Generate recommendations directly from a checked-out bonsai/idol-db."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .engine import recommend
from .idol_db import build_features, load_json


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--idol-db", default="../idol-db")
    parser.add_argument("--profile", default="recommendation/seed/user_profiles.jsonl")
    parser.add_argument("--features-output", default="recommendation/output/idol_db_features.jsonl")
    parser.add_argument("--output", default="recommendation/output/recommendations.jsonl")
    parser.add_argument("--top-k", type=int, default=5)
    args = parser.parse_args()

    root = Path(args.idol_db)
    features = build_features(
        load_json(root / "data/idols.json"),
        load_json(root / "data/events.json"),
    )

    feature_path = Path(args.features_output)
    feature_path.parent.mkdir(parents=True, exist_ok=True)
    feature_path.write_text(
        "\n".join(json.dumps(x, ensure_ascii=False) for x in features) + "\n",
        encoding="utf-8",
    )

    profiles = [
        json.loads(line)
        for line in Path(args.profile).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    result = recommend(profiles[0], [x for x in features if x["active"]], args.top_k)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        "\n".join(json.dumps(x, ensure_ascii=False) for x in result) + "\n",
        encoding="utf-8",
    )
    print(f"features={len(features)} active={sum(x['active'] for x in features)} recommendations={len(result)}")


if __name__ == "__main__":
    main()
