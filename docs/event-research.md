# Event Research

## Role

idol-research is not the crawler and not the event database.

Its core asset is **knowledge about how to discover idol events and how to select useful event records**.

## Separate the data

### Event data

Owned by idol-db.

Research reads it for analysis and evaluation.

### Discovery Intelligence

Owned by idol-research.

It accumulates:

- source/domain
- entry point
- search/query method
- keywords
- URL patterns
- crawl strategy
- observed yield
- noise
- coverage
- freshness
- reliability
- selection rules
- rejection reasons

This is the accumulated knowledge of **how to investigate idol events**.

## Python pipeline

```
raw observations
  ↓
candidate extraction
  ↓
classification
  ↓
normalization
  ↓
entity resolution
  ↓
dedupe
  ↓
quality scoring
  ↓
published events.jsonl
```

Every selection should retain, when possible:

- source
- source_url
- observed_at
- confidence
- selection_reason
- rejection_reason
- normalization decisions

The question is not only "how many events did we find?" but also:

> Which sources and search methods reliably find the events we care about?

## Learning loop

```
source -> crawl -> candidates
             ↓
       selection metrics
             ↓
       source quality
             ↓
       better crawl targets
             ↺
```

The research asset is the improving **event discovery method**.
