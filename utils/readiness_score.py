def calculate_readiness_score(
    match_score,
    missing_skills_count
):

    score = (
        match_score * 0.8
    ) + (
        max(0, 20 - missing_skills_count)
    )

    if score > 100:
        score = 100

    return round(score, 2)