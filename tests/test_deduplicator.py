from processing.deduplicator import deduplicate_jobs


def test_duplicate_jobs_are_removed():
    jobs = [
        {"title": "Technical Delivery Manager", "company": "Example Ltd", "location": "London"},
        {"title": "Technical Delivery Manager", "company": "Example Ltd", "location": "London"},
    ]

    assert len(deduplicate_jobs(jobs)) == 1
