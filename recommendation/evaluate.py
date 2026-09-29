"""Small offline ranking metrics for recommendation experiments."""
from __future__ import annotations


def precision_at_k(recommended: list[str], relevant: set[str], k: int) -> float:
    items = recommended[:k]
    return sum(x in relevant for x in items) / max(len(items), 1)


def recall_at_k(recommended: list[str], relevant: set[str], k: int) -> float:
    if not relevant:
        return 0.0
    return sum(x in relevant for x in recommended[:k]) / len(relevant)


def dcg(recommended: list[str], relevant: set[str], k: int) -> float:
    import math
    return sum((1.0 / math.log2(i + 2)) for i, x in enumerate(recommended[:k]) if x in relevant)


def ndcg_at_k(recommended: list[str], relevant: set[str], k: int) -> float:
    import math
    ideal_n = min(len(relevant), k)
    if ideal_n == 0:
        return 0.0
    ideal = sum(1.0 / math.log2(i + 2) for i in range(ideal_n))
    return dcg(recommended, relevant, k) / ideal


def coverage(recommended_lists: list[list[str]], catalog_size: int) -> float:
    if catalog_size <= 0:
        return 0.0
    return len({x for row in recommended_lists for x in row}) / catalog_size
