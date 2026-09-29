from recommendation.engine import recommend


def test_recommendation_is_ranked_and_explained():
    profile = {
        "genres": ["地下アイドル", "ポップ"],
        "liked_artists": ["idol-a"],
        "areas": ["新宿", "渋谷"],
        "prefers_free": True,
    }
    idols = [
        {"artist_id": "idol-b", "genres": ["地下アイドル"], "similar_to": ["idol-a"], "area": "渋谷", "free": True, "days_since_activity": 7},
        {"artist_id": "idol-c", "genres": ["ロック"], "similar_to": [], "area": "池袋", "free": False, "days_since_activity": 90},
    ]
    result = recommend(profile, idols, top_k=2)
    assert len(result) == 2
    assert result[0]["artist_id"] == "idol-b"
    assert result[0]["reasons"]
    assert result[0]["score"] >= result[1]["score"]
