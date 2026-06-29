from src.utils.company_classifier import product_company_score


# --------------------------------------------------------
# Years of Experience
# --------------------------------------------------------

def years_score(candidate):

    years = candidate["profile"].get(
        "years_of_experience",
        0
    )

    return min((years / 10) * 100, 100)


# --------------------------------------------------------
# Relevant Experience
# --------------------------------------------------------

def relevant_experience_score(candidate, jd_features):

    preferred_titles = [
        title.lower()
        for title in jd_features["preferred_titles"]
    ]

    jobs = candidate.get("career_history", [])

    if len(jobs) == 0:
        return 0

    relevant_months = 0
    total_months = 0

    for job in jobs:

        months = job.get(
            "duration_months",
            0
        )

        total_months += months

        title = job.get(
            "title",
            ""
        ).lower()

        for preferred in preferred_titles:

            if preferred in title:

                relevant_months += months

                break

    if total_months == 0:
        return 0

    return (
        relevant_months /
        total_months
    ) * 100


# --------------------------------------------------------
# Career Progression
# --------------------------------------------------------

SENIORITY = {

    "intern": 1,

    "trainee": 2,

    "associate": 3,

    "junior": 4,

    "software engineer": 5,
    "backend engineer": 5,
    "data engineer": 5,

    "machine learning engineer": 6,
    "ml engineer": 6,
    "ai engineer": 6,
    "research engineer": 6,
    "applied scientist": 6,
    "data scientist": 6,

    "senior": 7,

    "lead": 8,

    "staff": 9,

    "principal": 10,

    "architect": 10,

    "manager": 11,

    "director": 12,

    "vp": 13,

    "chief": 14
}


def career_progression_score(candidate):

    history = list(
        reversed(candidate.get("career_history", []))
    )

    if len(history) <= 1:
        return 50

    levels = []

    for job in history:

        title = job.get("title", "").lower()

        level = 0

        level = 0

    for keyword, value in SENIORITY.items():

        if keyword in title:

            level = max(level, value)
    levels.append(level)
    comparisons = len(levels) - 1

    if comparisons <= 0:
        return 50
    score = 0

    comparisons = len(levels) - 1

    for i in range(comparisons):

        current = levels[i]
        nxt = levels[i + 1]

        if nxt > current:
            score += 1.0          # Promotion

        elif nxt == current:
            score += 0.5          # Same level

        else:
            score += 0.0          # Demotion

    

    return (score / comparisons) * 100


# --------------------------------------------------------
# Consulting Score
# --------------------------------------------------------

def consulting_company_score(candidate):

    ratio = product_company_score(candidate)

    if ratio <= 0.20:
        return 100

    elif ratio <= 0.40:
        return 85

    elif ratio <= 0.60:
        return 65

    elif ratio <= 0.80:
        return 40

    else:
        return 15

# --------------------------------------------------------
# Career Stability
# --------------------------------------------------------

def career_stability_score(candidate):

    jobs = candidate.get(
        "career_history",
        []
    )

    if len(jobs) <= 1:
        return 100

    total_months = sum(

        job.get(
            "duration_months",
            0
        )

        for job in jobs

    )

    average = total_months / len(jobs)

    return min(
        (average / 36) * 100,
        100
    )


# --------------------------------------------------------
# Current Role
# --------------------------------------------------------

def current_role_score(candidate, jd_features):

    title = candidate["profile"].get(
        "current_title",
        ""
    ).lower()

    preferred_titles = [

        role.lower()

        for role in jd_features[
            "preferred_titles"
        ]

    ]

    for role in preferred_titles:

        if role in title:

            return 100

    return 40


# --------------------------------------------------------
# Final Career Score
# --------------------------------------------------------

def calculate_career_score(
    candidate,
    jd_features
):

    years = years_score(candidate)

    relevant = relevant_experience_score(
        candidate,
        jd_features
    )

    progression = career_progression_score(
        candidate
    )

    consulting = consulting_company_score(
        candidate
    )

    stability = career_stability_score(
        candidate
    )

    current = current_role_score(
        candidate,
        jd_features
    )

    career = (

        0.30 * years +

        0.25 * relevant +

        0.20 * consulting +

        0.15 * stability +

        0.10 * current

    )

    return {

        "career_score": round(career, 2),

        "years_score": round(years, 2),

        "relevant_experience_score": round(
            relevant,
            2
        ),


        "consulting_company_score": round(
            consulting,
            2
        ),

        "career_stability_score": round(
            stability,
            2
        ),

        "current_role_score": round(
            current,
            2
        )

    }