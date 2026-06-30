import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
_ARTIFACT_CACHE = {}

def load_semantic_artifacts(artifact_dir="artifact"):

    if artifact_dir in _ARTIFACT_CACHE:
        return _ARTIFACT_CACHE[artifact_dir]

    candidate_embeddings = np.load(
        os.path.join(
            artifact_dir,
            "candidate_general_embeddings.npy"
        )
    )

    candidate_ids = np.load(
        os.path.join(
            artifact_dir,
            "candidate_ids.npy"
        ),
        allow_pickle=True
    )

    jd_embedding = np.load(
        os.path.join(
            artifact_dir,
            "jd_embedding.npy"
        )
    )

    _ARTIFACT_CACHE[artifact_dir] = (
        candidate_embeddings,
        candidate_ids,
        jd_embedding
    )

    return _ARTIFACT_CACHE[artifact_dir]

def calculate_semantic_scores(artifact_dir="artifact"):

    (
    candidate_embeddings,
    _,
    jd_embedding
) = load_semantic_artifacts(
    artifact_dir
)

    similarities = cosine_similarity(

        jd_embedding.reshape(1, -1),

        candidate_embeddings

    ).flatten()

    return similarities


def semantic_search(
    top_k=5000,
    artifact_dir="artifact"
):

    scores = calculate_semantic_scores(
        artifact_dir
    )

    top_indices = np.argsort(scores)[::-1][:top_k]

    (
    _,
    candidate_ids,
    _
) = load_semantic_artifacts(
    artifact_dir
)

    results = []

    for idx in top_indices:

        results.append({

            "candidate_id": str(candidate_ids[idx]),

            "index": int(idx),

            "semantic_score": float(scores[idx])

        })

    return results