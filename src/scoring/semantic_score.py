from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def load_candidate_embeddings():
    return np.load("artifact/candidate_general_embeddings.npy")

def load_candidate_ids(): 
    return np.load( "artifact/candidate_ids.npy", allow_pickle=True )

def load_jd_embeddings():
    return np.load("artifact/jd_embedding.npy")

def calculate_semantic_scores():
    print(np.load("artifact/jd_embedding.npy").shape)
    print(np.load("artifact/candidate_general_embeddings.npy").shape)
    candidate_embedding=load_candidate_embeddings()
    jd_embedding=load_jd_embeddings()
    similarities = cosine_similarity(
    jd_embedding.reshape(1, -1),
    candidate_embedding
).flatten()
    return similarities


def semantic_search(top_k=5000):

    scores = calculate_semantic_scores()

    top_indices = np.argsort(scores)[::-1][:top_k]

    candidate_ids = load_candidate_ids()

    results = []

    for idx in top_indices:

        results.append({
            "candidate_id": candidate_ids[idx],
            "index": int(idx),
            "semantic_score": float(scores[idx])
        })

    return results
