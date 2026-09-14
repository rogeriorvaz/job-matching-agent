from matching.scorer import calculate_score


def test_full_score():
    result = {
        "role_alignment": 2,
        "responsibility_alignment": 2,
        "technical_skills": 2,
        "delivery_agile": 1,
        "leadership_seniority": 1,
        "domain_relevance": 1,
        "location_fit": 1,
        "missing_requirements": [],
    }

    raw, penalty, final = calculate_score(result)

    assert raw == 10
    assert penalty == 0
    assert final == 10


def test_missing_requirements_apply_penalty():
    result = {
        "role_alignment": 2,
        "responsibility_alignment": 2,
        "technical_skills": 2,
        "delivery_agile": 1,
        "leadership_seniority": 1,
        "domain_relevance": 1,
        "location_fit": 1,
        "missing_requirements": ["SC clearance"],
    }

    raw, penalty, final = calculate_score(result)

    assert raw == 10
    assert penalty == 1
    assert final == 9
