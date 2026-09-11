# Research migration manifest

## Source

`bonsai/idol-lab`

## Split rule

Keep theory, essays, conceptual ontology and folklore interpretation in `idol-lab`.
Move empirical assets that support observation, comparison, data analysis and marketing research into `idol-research`.

## Initial split

- `data/event.json` → `data/events.json`
- `data/SPARK-fes-artists-2025.jsonl` → `data/spark-fes-artists-2025.jsonl`
- `crawler/idolwatch.py` → `collect/idolwatch.py`
- `research/00-research-design.md` → reference only; theory remains in `idol-lab`

## Provenance

All initial assets originate from `bonsai/idol-lab` and retain their original observation/source fields where available.

## Next split candidates

- `data/idolwatch.jsonl`
- `data/idols.json`
- `data/history.json`
- `data/local-idol.json`
- `data/lnan-l-group.json`
- `data/music/`

These should be moved when their analytical purpose is confirmed, rather than mechanically duplicating every theoretical dataset.
