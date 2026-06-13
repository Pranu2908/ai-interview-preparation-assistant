def calculate_readiness_score(
    match_score,
    missing_skills_count
):

    score = match_score

    deduction = missing_skills_count * 5

    score = score - deduction

    if score < 0:
        score = 0

    if score > 100:
        score = 100

    return round(score, 2)