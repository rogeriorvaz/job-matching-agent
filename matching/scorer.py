import json
from .prompts import SCORING_PROMPT

DIMENSIONS = [
    "role_alignment",
    "responsibility_alignment",
    "technical_skills",
    "delivery_agile",
    "leadership_seniority",
    "domain_relevance",
    "location_fit",
]


def calculate_score(result: dict) -> tuple[float, float, float]:
    raw = sum(float(result.get(key, 0)) for key in DIMENSIONS)
    missing = result.get("missing_requirements", [])
    penalty = min(float(len(missing)), 3.0)
    final = max(0.0, min(10.0, raw - penalty))
    return raw, penalty, final


def build_prompt(profile: str, job: dict) -> str:
    return SCORING_PROMPT.format(
        candidate_profile=profile,
        title=job.get("title", ""),
        company=job.get("company", ""),
        location=job.get("location", ""),
        description=job.get("description", ""),
    )


def parse_result(raw_response: str) -> dict:
    return json.loads(raw_response)
