"""Build recommendation features from canonical-ish event/artist records."""
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime
from typing import Any


def build_artist_features(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    artists: dict[str, dict[str, Any]] = defaultdict(lambda: {
        "genres": Counter(), "areas": Counter(), "event_count": 0,
        "free_event_count": 0, "last_activity": None,
    })
    for event in events:
        date = event.get("date") or event.get("start_at")
        area = event.get("area") or (event.get("venue") or {}).get("area")
        free = bool((event.get("admission") or {}).get("price") == 0 or event.get("free"))
        for artist in event.get("artists", []):
            if isinstance(artist, dict):
                artist_id = artist.get("artist_id") or artist.get("id") or artist.get("name")
                genres = artist.get("genres", [])
            else:
                artist_id, genres = str(artist), []
            if not artist_id:
                continue
            row = artists[artist_id]
            row["event_count"] += 1
            row["free_event_count"] += int(free)
            if area:
                row["areas"][area] += 1
            for genre in genres:
                row["genres"][genre] += 1
            if date and (row["last_activity"] is None or str(date) > str(row["last_activity"])):
                row["last_activity"] = date

    output = []
    for artist_id, row in artists.items():
        output.append({
            "artist_id": artist_id,
            "genres": [x for x, _ in row["genres"].most_common()],
            "area": row["areas"].most_common(1)[0][0] if row["areas"] else None,
            "event_count": row["event_count"],
            "free_event_ratio": round(row["free_event_count"] / max(row["event_count"], 1), 6),
            "last_activity": row["last_activity"],
        })
    return output
