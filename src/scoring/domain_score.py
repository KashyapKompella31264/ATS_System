import os
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


_ARTIFACT_CACHE = {}

def load_domain_artifacts(artifact_dir="artifact"):

    if artifact_dir in _ARTIFACT_CACHE:
        return _ARTIFACT_CACHE[artifact_dir]

    candidate_embeddings = np.load(
        os.path.join(
            artifact_dir,
            "candidate_career_embeddings.npy"
        )
    )

    domain_embeddings = np.load(
        os.path.join(
            artifact_dir,
            "domain_embeddings.npy"
        )
    )

    with open(
        os.path.join(
            artifact_dir,
            "domain_labels.json"
        ),
        "r"
    ) as f:

        domain_labels = json.load(f)

    _ARTIFACT_CACHE[artifact_dir] = (
        candidate_embeddings,
        domain_embeddings,
        domain_labels
    )

    return _ARTIFACT_CACHE[artifact_dir]


# --------------------------------------------------------
# Domain Importance Weights
# --------------------------------------------------------

DOMAIN_WEIGHTS = {

    "recommendation": 0.25,

    "retrieval": 0.20,

    "search": 0.20,

    "ranking": 0.15,

    "embeddings": 0.10,

    "llm": 0.10
}


# --------------------------------------------------------
# Calculate Domain Score
# --------------------------------------------------------

def calculate_domain_score(candidate_index, artifact_dir="artifact"):

    (
    candidate_embeddings,
    domain_embeddings,
    domain_labels
) = load_domain_artifacts(
    artifact_dir
)
    
    candidate_embedding = candidate_embeddings[
        candidate_index
    ].reshape(1, -1)

    similarities = cosine_similarity(
        candidate_embedding,
        domain_embeddings
    ).flatten()

    weighted_score = 0

    matched_domains = []

    similarity_scores = {}

    for label, similarity in zip(
            domain_labels,
            similarities):

        similarity_scores[label] = round(
            float(similarity), 3
        )

        weighted_score += (
            similarity *
            DOMAIN_WEIGHTS[label]
        )

        if similarity >= 0.30:

            matched_domains.append(
                (
                    label,
                    round(float(similarity), 3)
                )
            )

    return {

        "domain_score": round(
            weighted_score * 100,
            2
        ),

        "matched_domains": matched_domains,

        "similarity_scores": similarity_scores
    }
