def generate_reason(candidate, candidate_scores):

    reasons = []

    # -------------------------------------------------
    # Current Role
    # -------------------------------------------------

    current_role = (
    candidate.get("profile", {})
    .get("current_title", "")
    )

    if current_role:

        reasons.append(
            f"Current role: {current_role}"
        )

    # -------------------------------------------------
    # Experience
    # -------------------------------------------------

    years = candidate.get(
    "profile",
    {}
    ).get(
        "years_of_experience",
        None
    )

    if years is not None:

        reasons.append(
            f"{years} years of professional experience"
        )

    # -------------------------------------------------
    # Top Skills
    # -------------------------------------------------

    skills = candidate.get("skills", [])

    if skills:

        top_skills = [
            skill["name"]
            for skill in skills[:4]
            if "name" in skill
        ]

        if top_skills:

            reasons.append(
                "Key skills: " +
                ", ".join(top_skills)
            )

    # -------------------------------------------------
    # Strengths
    # -------------------------------------------------

    strengths = []

    if candidate_scores["semantic_score"] >= 65:

        strengths.append("high semantic relevance")

    if candidate_scores["career_score"] >= 80:

        strengths.append("strong career progression")

    if candidate_scores["consistency_score"] >= 65:

        strengths.append("good skill consistency")

    if candidate_scores["behavior_score"] >= 70:

        strengths.append("positive recruiter signals")

    if candidate_scores["domain_score"] >= 35:

        strengths.append("relevant AI domain experience")

    if strengths:

        reasons.append(
            "Strengths: " +
            ", ".join(strengths)
        )

    # -------------------------------------------------
    # Concerns
    # -------------------------------------------------

    concerns = []

    notice = candidate.get(
        "redrob_signals",
        {}
    ).get(
        "notice_period_days",
        0
    )

    if notice >= 60:

        concerns.append(
            f"{notice}-day notice period"
        )

    if candidate_scores["behavior_score"] < 50:

        concerns.append(
            "limited recruiter engagement"
        )

    if candidate_scores["consistency_score"] < 50:

        concerns.append(
            "skills need stronger career evidence"
        )

    if concerns:

        reasons.append(
            "Concern: " +
            ", ".join(concerns)
        )

    return ". ".join(reasons) + "."