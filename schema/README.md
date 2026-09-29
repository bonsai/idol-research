# Schema

## Authority

**Schema is decided and evolved here in `bonsai/idol-research`.**

Research observes real data, proposes fields, tests meanings, and versions the
contract. Once a schema is ready, it is published to `idol-db` as a generated
mirror so crawlers/validators can inspect the contract locally.

```
Go crawl
  -> raw observations
  -> idol-research / Python
  -> schema proposal
  -> validation / evaluation
  -> schema contract
  -> CP + push to idol-db
  -> Go/Python can inspect it
```

The copy in `idol-db/schema/models.py` is **not** authoritative.

## Reference mode

Consumers that do not need a local copy may reference the canonical files in
this repository directly:

- `schema/models.py`
- `schema/README.md`
- versioned contracts under `schema/contract/`

The reference should pin a commit SHA when reproducibility matters.

## Lang 三兄弟

| layer | role |
|---|---|
| LangChain | structured extraction against the current research schema |
| LangGraph | observe -> normalize -> resolve -> validate -> persist |
| LangSmith | trace / dataset / evaluation / schema drift |

## Growth

```
crawl
  -> observe
  -> discover fields
  -> research schema
  -> validate
  -> publish contract
  -> canonicalize
  -> use
  -> observe again
  -> evolve schema
```

Fact / Inference / Hypothesis remain separate.
