# Development

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

## Tests

```bash
pytest
```

## Adding a collector

1. Create the collector module.
2. Implement `JobCollector`.
3. Keep selectors inside the module.
4. Add tests.
5. Add the source to configuration.
6. Make source failures non-fatal.

## Adding a scoring dimension

1. Update the prompt.
2. Update the schema if required.
3. Update Python score calculation.
4. Add tests.
5. Update scoring documentation.

Do not silently change scoring for historical results.
