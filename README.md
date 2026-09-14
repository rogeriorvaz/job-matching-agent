# Local Job Matching Agent

A local-first job discovery and CV matching agent for Ubuntu. It discovers recent jobs, extracts and normalises listings, deduplicates them, scores them against a structured candidate profile using a local LLM, and presents ranked results through Streamlit.

## Goals

- Discover relevant jobs within a configurable time window.
- Replace Apify with local browser automation where practical.
- Keep CV, job history and scoring data local.
- Produce conservative, explainable fit scores.
- Track applications and outcomes.
- Export results to CSV or Excel.
- Keep collectors, matching and presentation loosely coupled.

## Architecture

```text
Search / Job Sources
        |
        v
  Playwright Collectors
        |
        v
 Normalisation + Date Filter
        |
        v
     Deduplication
        |
        v
       SQLite
        |
        v
     Local LLM
        |
        v
     Scoring
        |
        v
       SQLite
        |
        +------> Streamlit Dashboard
        |
        +------> CSV / Excel Export
```

Python owns deterministic operations such as dates, filtering, deduplication, persistence and score arithmetic. The LLM performs semantic comparison between the candidate profile and job descriptions.

## Requirements

- Ubuntu 24.04 or compatible Linux
- Python 3.12+
- Chromium supported by Playwright
- A local LLM runtime exposing an OpenAI-compatible endpoint
- Git

## Installation

```bash
git clone <YOUR_REPOSITORY_URL>
cd job-matching-agent

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
playwright install chromium
```

If Linux browser dependencies are required:

```bash
playwright install-deps chromium
```

Copy the environment template:

```bash
cp .env.example .env
```

Edit `.env` with your local LLM endpoint and model.

## Running

Initialise the database and run the CLI:

```bash
python main.py
```

Example:

```bash
python main.py --location London --hours 24 --minimum-score 7 --limit 10
```

Start the dashboard:

```bash
streamlit run app/dashboard.py
```

## Configuration

- `config/profile.yaml` contains the structured candidate profile.
- `config/searches.yaml` contains target roles and sources.
- `config/settings.yaml` contains runtime settings.

Do not put secrets in configuration files.

## Scoring

| Dimension | Maximum |
|---|---:|
| Role alignment | 2 |
| Responsibility alignment | 2 |
| Technical skills | 2 |
| Agile / delivery | 1 |
| Leadership / seniority | 1 |
| Domain relevance | 1 |
| Location fit | 1 |
| **Total** | **10** |

Mandatory requirements are evaluated separately and can produce penalties of up to 3 points.

Interpretation:

- 9 to 10: exceptionally strong match
- 8 to 8.9: strong candidate
- 7 to 7.9: credible application
- Below 7: normally exclude

The LLM must never invent experience, certifications, clearance, technology knowledge or domain experience.

## Database

SQLite is the system of record.

Core tables:

- `jobs`
- `job_sources`
- `job_scores`
- `applications`
- `searches`
- `job_searches`
- `cv_profiles`

Database:

```text
data/jobs.db
```

## Repository hygiene

The repository deliberately ignores:

- `.env`
- local SQLite databases
- raw scraped data
- personal CV files
- logs
- generated exports
- browser profiles

## Responsible collection

Use automation only where the target website permits it. Respect terms of service, rate limits, authentication controls and access restrictions. Do not bypass CAPTCHAs or anti-bot controls.

LinkedIn is optional and must not become a dependency of the application.

## Development principles

1. Prefer deterministic Python logic over LLM decisions.
2. Keep source-specific selectors inside collectors.
3. Preserve source URLs.
4. Make scoring explainable.
5. Preserve historical scores.
6. Never silently overwrite application history.
7. Test date handling and deduplication.
8. Keep personal data out of Git.
9. Build one reliable collector before adding more.

## Roadmap

### Phase 1
SQLite, configuration, CV profile, first collector, normalisation, date filtering and deduplication.

### Phase 2
Local LLM integration, structured scoring and shortlisting.

### Phase 3
Streamlit dashboard, application tracking and exports.

### Phase 4
Additional sources, semantic deduplication, analytics, career-fit scoring and application priority.

### Phase 5
Daily scheduling, notifications, market analysis and CV tailoring.
