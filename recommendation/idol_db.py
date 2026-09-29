"""Adapt bonsai/idol-db canonical JSON into recommendation features."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _event_performers(event: dict[str, Any]) -> list[str]:
    values = event.get("performers") or event.get("artists") or []
    result: list[str] = []
    for value in values:
        if isinstance(value, dict):
            for key in ("id", "artist_id", "name", "label"):
                if value.get(key):
                    result.append(str(value[key]))
                    break
        elif value:
            result.append(str(value))
    return result


def build_features(idols_doc: dict[str, Any], events_doc: dict[str, Any]) -> list[dict[str, Any]]:
    events = events_doc.get("events", []) if isinstance(events_doc, dict) else []
    rows: list[dict[str, Any]] = []

    for idol in idols_doc.get("entries", []):
        if idol.get("type") not in {"idol", "person"}:
            continue

        idol_id = idol.get("id")
        label = idol.get("label")
        if not idol_id or not label:
            continue

        aliases = {str(x) for x in idol.get("aliases", [])}
        names = aliases | {str(label), str(idol_id)}
        tags = [str(x) for x in idol.get("tags", [])]

        matched_events = []
        for event in events:
            performers = set(_event_performers(event))
            if performers & names:
                matched_events.append(event)

        areas = Counter()
        genres = Counter(tags)
        for event in matched_events:
            region = event.get("region") or event.get("area")
            if region:
                areas[str(region)] += 1
            category = event.get("category")
            if category:
                genres[str(category)] += 1

        region = idol.get("region")
        if region:
            areas[str(region)] += 1

        activities = idol.get("activities", [])
        active = any(
            isinstance(a, dict) and a.get("status") == "active"
            for a in activities
        ) or idol.get("active_period", {}).get("end") in {None, ""}

        rows.append({
            "artist_id": idol_id,
            "name": label,
            "aliases": sorted(aliases),
            "genres": [x for x, _ in genres.most_common()],
            "area": areas.most_common(1)[0][0] if areas else None,
            "event_count": len(matched_events),
            "free_event_ratio": round(
                sum(
                    1 for event in matched_events
                    if event.get("free") is True
                    or (event.get("admission") or {}).get("price") == 0
                ) / max(len(matched_events), 1),
                6,
            ),
            "last_activity": max(
                [str(event.get("date", "")) for event in matched_events] or
                [str(idol.get("active_period", {}).get("end") or "")]
            ),
            "active": active,
            "source": "bonsai/idol-db",
        })

    return rows
