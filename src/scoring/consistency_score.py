import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


_ARTIFACT_CACHE = {}


def load_embeddings(artifact_dir="artifact"):

    if artifact_dir in _ARTIFACT_CACHE:
        return _ARTIFACT_CACHE[artifact_dir]

    career_embeddings = np.load(
        os.path.join(
            artifact_dir,
            "candidate_career_embeddings.npy"
        )
    )

    skill_embeddings = np.load(
        os.path.join(
            artifact_dir,
            "candidate_skill_embeddings.npy"
        )
    )

    _ARTIFACT_CACHE[artifact_dir] = (
        career_embeddings,
        skill_embeddings
    )

    return _ARTIFACT_CACHE[artifact_dir]


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

def embedding_consistency(candidate_index,artifact_dir="artifact"):

    career_embeddings, skill_embeddings = load_embeddings(
    artifact_dir
)
    
    career = career_embeddings[
        candidate_index
    ].reshape(1, -1)

    skills = skill_embeddings[
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
        candidate_index,
        artifact_dir="artifact"):

    embedding = embedding_consistency(
        candidate_index,
        artifact_dir
    )

    duration = duration_score(candidate)

    proficiency = proficiency_score(candidate)

    assessment = assessment_score(candidate)
    similarity= embedding
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
