# Recommendation MVP

推しレコメンドの最小実装。

```
profile -> retrieve -> score -> rerank -> explain
```

現在はローカルJSONLと説明可能なweighted scoreだけで動く。候補取得をDB/vector searchへ、rankingをBQML等へ差し替えられるように、入出力をJSON互換に保つ。

## Run

```sh
python -m recommendation.run
```

出力: `recommendation/output/recommendations.jsonl`

## Contract

- profile: user preference signals
- idol_features: candidate features
- recommendation: score / signals / reasons

次段階で idol-db canonical dataからfeature生成し、offline evaluationを追加する。
