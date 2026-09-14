from rapidfuzz.fuzz import ratio


def duplicate_score(a: dict, b: dict) -> float:
    title = ratio(a.get("title", "").lower(), b.get("title", "").lower())
    company = ratio(a.get("company", "").lower(), b.get("company", "").lower())
    location = ratio(a.get("location", "").lower(), b.get("location", "").lower())
    return (title * 0.5) + (company * 0.35) + (location * 0.15)


def deduplicate_jobs(jobs: list[dict], threshold: float = 90) -> list[dict]:
    unique = []
    for job in jobs:
        if any(duplicate_score(job, existing) >= threshold for existing in unique):
            continue
        unique.append(job)
    return unique
