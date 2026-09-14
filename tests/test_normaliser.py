from processing.normaliser import clean_text, job_hash


def test_clean_text():
    assert clean_text("  hello   world ") == "hello world"


def test_job_hash_is_stable():
    first = job_hash("Role", "Company", "London", "https://example.com/job")
    second = job_hash("Role", "Company", "London", "https://example.com/job")
    assert first == second
