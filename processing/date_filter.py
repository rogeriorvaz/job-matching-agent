from datetime import datetime, timezone


def age_hours(posted_at: datetime) -> float:
    if posted_at.tzinfo is None:
        posted_at = posted_at.replace(tzinfo=timezone.utc)
    return (datetime.now(timezone.utc) - posted_at).total_seconds() / 3600


def is_recent(posted_at: datetime, hours: int = 24) -> bool:
    return age_hours(posted_at) <= hours
