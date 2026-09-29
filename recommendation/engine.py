"""A small, explainable recommendation pipeline.

profile -> retrieve -> score -> rerank -> explain
The data contract is intentionally JSON-serializable so it can later be
replaced by BQML/vector retrieval without changing the public shape.
"""
from __future__ import annotations

from math import exp
from typing import Any

DEFAULT_WEIGHTS = {
    "preference": 0.35,
    "similarity": 0.25,
    "recency": 0.15,
    "locality": 0.10,
    "price_fit": 0.10,
    "novelty": 0.05,
}


def _overlap(values: list[str], preferred: list[str]) -> float:
    a, b = set(values), set(preferred)
    return len(a & b) / max(len(b), 1)


def _recency(days: float) -> float:
    return exp(-max(days, 0.0) / 30.0)


def score(profile: dict[str, Any], idol: dict[str, Any], weights: dict[str, float] | None = None) -> tuple[float, dict[str, float]]:
    w = {**DEFAULT_WEIGHTS, **(weights or {})}
    signals = {
        "preference": _overlap(idol.get("genres", []), profile.get("genres", [])),
        "similarity": _overlap(idol.get("similar_to", []), profile.get("liked_artists", [])),
        "recency": _recency(float(idol.get("days_since_activity", 365))),
        "locality": 1.0 if idol.get("area") in profile.get("areas", []) else 0.0,
        "price_fit": 1.0 if idol.get("free", False) and profile.get("prefers_free", False) else 0.5,
        "novelty": 1.0 if idol.get("artist_id") not in profile.get("liked_artists", []) else 0.0,
    }
    total = sum(signals[k] * w[k] for k in signals)
    return total, signals


def explain(profile: dict[str, Any], idol: dict[str, Any], signals: dict[str, float]) -> list[str]:
    reasons: list[str] = []
    if signals["preference"] > 0:
        reasons.append("好みのジャンルに近い")
    if signals["similarity"] > 0:
        reasons.append("よく見るアーティストと近い")
    if signals["locality"] > 0:
        reasons.append("よく行くエリアで活動")
    if signals["price_fit"] >= 1:
        reasons.append("無料イベントとの相性が高い")
    if signals["recency"] >= 0.5:
        reasons.append("最近も活動している")
    if signals["novelty"] > 0:
        reasons.append("まだ深く見ていない新しい候補")
    return reasons[:3]


def recommend(profile: dict[str, Any], idols: list[dict[str, Any]], top_k: int = 10, weights: dict[str, float] | None = None) -> list[dict[str, Any]]:
    ranked: list[dict[str, Any]] = []
    for idol in idols:
        value, signals = score(profile, idol, weights)
        ranked.append({
            "artist_id": idol["artist_id"],
            "score": round(value, 6),
            "signals": {k: round(v, 6) for k, v in signals.items()},
            "reasons": explain(profile, idol, signals),
        })
    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked[:top_k]
