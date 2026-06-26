import os
import json
import numpy as np

from sentence_transformers import SentenceTransformer

from src.parser.candidate_loader import load_candidates
from src.parser.jd_parser import parse_jd
from src.features.document_builder import (
    build_general_document,
    build_career_document
)

ARTIFACT_DIR = "artifact"

MODEL_NAME = "all-MiniLM-L6-v2"


def save_domain_labels(domains):

    with open(
        os.path.join(ARTIFACT_DIR, "domain_labels.json"),
        "w"
    ) as f:

        json.dump(domains, f, indent=4)


def main():

    os.makedirs(ARTIFACT_DIR, exist_ok=True)

    print("Loading embedding model...")

    model = SentenceTransformer(MODEL_NAME)

    print("Parsing JD...")

    jd = parse_jd()

    # ----------------------------------------------------
    # JD Embedding
    # ----------------------------------------------------

    # print("Generating JD embedding...")

    # jd_embedding = model.encode(
    #     " ".join(jd["clean_jd"]),
    #     convert_to_numpy=True,
    #     normalize_embeddings=True
    # )

    # np.save(
    #     os.path.join(ARTIFACT_DIR, "jd_embedding.npy"),
    #     jd_embedding
    # )

    # ----------------------------------------------------
    # Domain Embeddings
    # ----------------------------------------------------

    print("Generating domain embeddings...")

    domain_labels = []
    domain_texts = []

    for label, keywords in jd["target_domains"].items():

        domain_labels.append(label)

        domain_description = (
            f"This domain focuses on {label}. "
            f"It includes concepts such as: {', '.join(keywords)}."
        )

        domain_texts.append(domain_description)

    domain_embeddings = model.encode(
        domain_texts,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    np.save(
        os.path.join(
            ARTIFACT_DIR,
            "domain_embeddings.npy"
        ),
        domain_embeddings
    )

    save_domain_labels(domain_labels)

    # ----------------------------------------------------
    # Candidate Embeddings
    # ----------------------------------------------------

    # print("Loading candidates...")

    # candidates = load_candidates(
    #     "data/raw/candidates.jsonl"
    # )

    # candidate_ids = []

    # general_documents = []

    # career_documents = []

    # print("Building documents...")

    # for candidate in candidates:

    #     candidate_ids.append(
    #         candidate["candidate_id"]
    #     )

    #     general_documents.append(
    #         build_general_document(candidate)
    #     )

    #     career_documents.append(
    #         build_career_document(candidate)
    #     )

    # print("Generating General Embeddings...")
    # general_embeddings = model.encode(
    #     general_documents,
    #     batch_size=64,
    #     show_progress_bar=True,
    #     convert_to_numpy=True,
    #     normalize_embeddings=True
    # )
    # print("General Embeddings Shape:", general_embeddings.shape)

    
    # print("Generating Career Embeddings...")

    # career_embeddings = model.encode(
    #     career_documents,
    #     batch_size=64,
    #     show_progress_bar=True,
    #     convert_to_numpy=True,
    #     normalize_embeddings=True
    # )
    # print("Career Embeddings Shape:", career_embeddings.shape)

    # np.save(
    #     os.path.join(
    #         ARTIFACT_DIR,
    #         "candidate_general_embeddings.npy"
    #     ),
    #     general_embeddings
    # )

    # np.save(
    #     os.path.join(
    #         ARTIFACT_DIR,
    #         "candidate_career_embeddings.npy"
    #     ),
    #     career_embeddings
    # )

    # np.save(
    #     os.path.join(
    #         ARTIFACT_DIR,
    #         "candidate_ids.npy"
    #     ),
    #     np.array(candidate_ids)
    # )

    # print()

    # print("=" * 60)
    # print("Embedding Generation Completed")
    # print("=" * 60)

    # print(f"Candidates : {len(candidate_ids)}")
    # print(f"Domains    : {len(domain_labels)}")



    # print("Current Working Directory:")
    # print(os.getcwd())
if __name__ == "__main__":
    main()
