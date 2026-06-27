import numpy as np

from sklearn.metrics.pairwise import cosine_similarity


# ----------------------------------------------------
# Load embeddings once
# ----------------------------------------------------

CAREER_EMBEDDINGS = np.load(
    "artifact/candidate_career_embeddings.npy"
)

SKILL_EMBEDDINGS = np.load(
    "artifact/candidate_skill_embeddings.npy"
)


# ----------------------------------------------------
# Duration Score
# ----------------------------------------------------

def duration_score(candidate):

    skills = candidate.get("skills", [])

    if len(skills) == 0:
        return 0

    durations = [
        skill.get("duration_months", 0)
        for skill in skills
    ]

    avg_duration = sum(durations) / len(durations)

    return min((avg_duration / 60) * 100, 100)


# ----------------------------------------------------
# Proficiency Score
# ----------------------------------------------------

PROFICIENCY = {

    "beginner": 25,

    "intermediate": 60,

    "advanced": 85,

    "expert": 100
}


def proficiency_score(candidate):

    skills = candidate.get("skills", [])

    if len(skills) == 0:
        return 0

    scores = []

    for skill in skills:

        level = skill.get(
            "proficiency",
            "beginner"
        ).lower()

        scores.append(
            PROFICIENCY.get(level, 25)
        )

    return sum(scores) / len(scores)


# ----------------------------------------------------
# Assessment Score
# ----------------------------------------------------

def assessment_score(candidate):

    assessments = candidate["redrob_signals"].get(
        "skill_assessment_scores",
        {}
    )

    if len(assessments) == 0:
        return 0

    return sum(
        assessments.values()
    ) / len(assessments)


# ----------------------------------------------------
# Embedding Similarity
# ----------------------------------------------------

def embedding_consistency(candidate_index):

    career = CAREER_EMBEDDINGS[
        candidate_index
    ].reshape(1, -1)

    skills = SKILL_EMBEDDINGS[
        candidate_index
    ].reshape(1, -1)

    similarity = cosine_similarity(
        career,
        skills
    )[0][0]

    return similarity * 100


# ----------------------------------------------------
# Final Consistency Score
# ----------------------------------------------------

def calculate_consistency_score(
        candidate,
        candidate_index):

    embedding = embedding_consistency(
        candidate_index
    )

    duration = duration_score(candidate)

    proficiency = proficiency_score(candidate)

    assessment = assessment_score(candidate)
    similarity= embedding_consistency(candidate_index)
    if assessment>0:

        consistency = (
         0.50 * similarity +
            0.20 * duration +
            0.15 * proficiency +
            0.15 * assessment
        )

    else:

        consistency = (
            0.65 * similarity +
            0.20 * duration +
            0.15 * proficiency
        )
    return {

        "consistency_score": round(float(consistency), 2),

        "skill_career_similarity": round(float(embedding), 2),

        "duration_score": round(duration, 2),

        "proficiency_score": round(proficiency, 2),

        "assessment_score": round(assessment, 2)

    }
