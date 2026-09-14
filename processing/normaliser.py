import hashlib
import re


def clean_text(value: str | None) -> str:
    if not value:
        return ""
    return re.sub(r"\s+", " ", value).strip()


def job_hash(title: str, company: str, location: str, url: str) -> str:
    raw = "|".join([
        clean_text(title).lower(),
        clean_text(company).lower(),
        clean_text(location).lower(),
        clean_text(url).lower(),
    ])
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def normalise_job(job: dict) -> dict:
    title = clean_text(job.get("title"))
    company = clean_text(job.get("company"))
    location = clean_text(job.get("location"))
    url = clean_text(job.get("url"))

    return {
        **job,
        "title": title,
        "company": company,
        "location": location,
        "description": clean_text(job.get("description")),
        "url": url,
        "job_hash": job_hash(title, company, location, url),
    }
