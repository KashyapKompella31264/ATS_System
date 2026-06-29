def generate_reason(candidate_scores):

    reasons = []

    # ---------------------------------------------
    # Semantic
    # ---------------------------------------------

    if candidate_scores["semantic_score"] >= 65:

        reasons.append(
            "Excellent semantic match with the job description"
        )

    elif candidate_scores["semantic_score"] >= 55:

        reasons.append(
            "Strong semantic relevance to the job description"
        )

    # ---------------------------------------------
    # Career
    # ---------------------------------------------

    if candidate_scores["career_score"] >= 85:

        reasons.append(
            "Strong and relevant career trajectory"
        )

    elif candidate_scores["career_score"] >= 70:

        reasons.append(
            "Relevant professional experience"
        )

    # ---------------------------------------------
    # Consistency
    # ---------------------------------------------

    if candidate_scores["consistency_score"] >= 65:

        reasons.append(
            "Skills are highly consistent with work experience"
        )

    elif candidate_scores["consistency_score"] >= 55:

        reasons.append(
            "Skills align well with career history"
        )

    # ---------------------------------------------
    # Behavior
    # ---------------------------------------------

    if candidate_scores["behavior_score"] >= 75:

        reasons.append(
            "Highly active and recruiter-friendly profile"
        )

    elif candidate_scores["behavior_score"] >= 60:

        reasons.append(
            "Positive recruiter engagement signals"
        )

    # ---------------------------------------------
    # Domain
    # ---------------------------------------------

    if candidate_scores["domain_score"] >= 35:

        reasons.append(
            "Strong exposure to relevant AI domains"
        )

    elif candidate_scores["domain_score"] >= 30:

        reasons.append(
            "Experience in key target domains"
        )

    if len(reasons) == 0:

        reasons.append(
            "Overall good match for the role"
        )

    return "; ".join(reasons)