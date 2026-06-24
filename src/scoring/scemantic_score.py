from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def calculate_similarity(
        jd_embeddings,
        candidate_embedding
):
    similarity=cosine_similarity(
        np.array(jd_embeddings).reshape(1,-1),
        np.array(candidate_embedding).reshape(1,-1)
    )
    return float(similarity[0][0])
