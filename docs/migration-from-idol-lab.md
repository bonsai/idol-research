# Migration from idol-lab

## Purpose

Move empirical research assets from `bonsai/idol-lab` into `bonsai/idol-research` without mixing theory and evidence.

## Move here

- structured observations
- event / performer datasets
- crawlers and collectors used for empirical analysis
- analysis notebooks / scripts
- marketing experiments and hypothesis tests
- derived datasets and visualizations

## Keep in idol-lab

- theory
- folklore / cultural interpretation
- ontology as a conceptual framework
- essays whose primary purpose is interpretation
- theoretical hypotheses before empirical operationalization

## First migration wave

Source assets identified in `idol-lab` include:

- `data/events.json`
- `data/idolwatch.jsonl`
- `data/spark-2025-artists.jsonl`
- `crawler/idolwatch.py`
- `crawler/generate_rss.py`

Migration rule: preserve source provenance and original timestamps; do not silently rewrite facts as interpretations.

## Next

1. Copy empirical assets into this repository.
2. Add source/provenance metadata.
3. Add schemas for observation, hypothesis, evidence, and evaluation.
4. Create `cases/terasuma/` as the first case study.
5. Build reusable cross-idol comparison datasets.
