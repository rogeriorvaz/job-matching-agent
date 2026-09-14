# Collectors

Collectors discover and extract jobs.

Every collector implements:

```python
async def search(query, location)
async def extract_job(url)
```

## Rules

- Keep selectors source-specific.
- Prefer public pages.
- Use conservative request rates.
- Preserve source URLs.
- Record discovery time.
- Do not bypass CAPTCHAs or anti-bot controls.
- One source failing should not terminate the full scan.

Google is primarily a discovery source. Job pages should be used for detailed job data where possible.

LinkedIn is optional. Do not make the application dependent on authenticated or restricted scraping.
