# Architecture

The application follows a local-first pipeline.

```text
Discovery
  -> Collection
  -> Normalisation
  -> Date validation
  -> Deduplication
  -> SQLite
  -> Local LLM
  -> Score calculation
  -> Shortlist
  -> Streamlit
```

Python owns deterministic processing. The LLM owns semantic comparison.

Collectors implement a common interface. Source-specific selectors remain inside individual collector modules.

SQLite is the system of record. CSV and Excel are output formats, not primary storage.

The LLM interface is OpenAI-compatible so the local runtime can be changed without rewriting the matching engine.
