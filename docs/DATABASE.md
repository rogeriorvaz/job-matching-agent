# Database

The database is `data/jobs.db`.

## Tables

- `cv_profiles`: candidate profile versions.
- `jobs`: canonical job records.
- `job_sources`: source references for jobs.
- `job_scores`: score breakdown and model metadata.
- `applications`: application lifecycle.
- `searches`: search terms and sources.
- `job_searches`: relationship between jobs and searches.

The MVP schema is idempotent. Once the schema is stable, use numbered migrations for changes.
