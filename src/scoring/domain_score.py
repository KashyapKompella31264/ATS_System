import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


# --------------------------------------------------------
# Load artifacts once
# --------------------------------------------------------

CANDIDATE_EMBEDDINGS = np.load(
    "artifact/candidate_career_embeddings.npy"
)

DOMAIN_EMBEDDINGS = np.load(
    "artifact/domain_embeddings.npy"
)

with open("artifact/domain_labels.json", "r") as f:
    DOMAIN_LABELS = json.load(f)


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

def calculate_domain_score(candidate_index):

    candidate_embedding = CANDIDATE_EMBEDDINGS[
        candidate_index
    ].reshape(1, -1)

    similarities = cosine_similarity(
        candidate_embedding,
        DOMAIN_EMBEDDINGS
    ).flatten()

    weighted_score = 0

    matched_domains = []

    similarity_scores = {}

    for label, similarity in zip(
            DOMAIN_LABELS,
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