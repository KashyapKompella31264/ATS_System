import os
import json
import numpy as np
import argparse
from sentence_transformers import SentenceTransformer

from src.parser.candidate_loader import load_candidates
from src.parser.jd_parser import parse_jd
from src.features.document_builder import (
    build_general_document,
    build_career_document,
    build_skill_document
)



MODEL_NAME = "all-MiniLM-L6-v2"


def save_domain_labels(domains,artifact_dir):

        with open(
            os.path.join(artifact_dir, "domain_labels.json"),
            "w"
        ) as f:

            json.dump(domains, f, indent=4)


def generate_embeddings(candidates_path,artifact_dir="artifact"):
    print("Loading embedding model...")
    os.makedirs(artifact_dir, exist_ok=True)
    model = SentenceTransformer(MODEL_NAME)


    

    print("Parsing JD...")

    jd = parse_jd()

    # ----------------------------------------------------
    # JD Embedding
    # ----------------------------------------------------

    print("Generating JD embedding...")

    jd_embedding = model.encode(
        " ".join(jd["clean_jd"]),
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    np.save(
        os.path.join(artifact_dir, "jd_embedding.npy"),
        jd_embedding
    )



    

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
            artifact_dir,
            "domain_embeddings.npy"
        ),
        domain_embeddings
    )

    save_domain_labels(domain_labels,artifact_dir)

    # ----------------------------------------------------
    # Candidate Embeddings
    # ----------------------------------------------------

    print("Loading candidates...")

    candidates = load_candidates(
        candidates_path
    )

    candidate_ids = []

    general_documents = []
    skill_documents = []
    career_documents = []
    print("Building documents...")
    for candidate in candidates:

        candidate_ids.append(
            candidate["candidate_id"]
        )

        general_documents.append(
            build_general_document(candidate)
        )

        career_documents.append(
            build_career_document(candidate)
        )
        skill_documents.append(
            build_skill_document(candidate)
        )

    print("Generating General Embeddings...")
    general_embeddings = model.encode(
        general_documents,
        batch_size=64,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True
    )
    print("General Embeddings Shape:", general_embeddings.shape)



    print("Generating Skill Embeddings...")

    skill_embeddings = model.encode(
        skill_documents,
        batch_size=64,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True
    )
    np.save(
    os.path.join(
        artifact_dir,
        "candidate_skill_embeddings.npy"
    ),
    skill_embeddings
    )

    print("Skill Embeddings Shape:", skill_embeddings.shape)
    print("Generating Career Embeddings...")

    career_embeddings = model.encode(
        career_documents,
        batch_size=64,
        show_progress_bar=True,
        convert_to_numpy=True,
        normalize_embeddings=True
    )
    print("Career Embeddings Shape:", career_embeddings.shape)

    np.save(
        os.path.join(
            artifact_dir,
            "candidate_general_embeddings.npy"
        ),
        general_embeddings
    )

    np.save(
        os.path.join(
            artifact_dir,
            "candidate_career_embeddings.npy"
        ),
        career_embeddings
    )

    np.save(
        os.path.join(
            artifact_dir,
            "candidate_ids.npy"
        ),
        np.array(candidate_ids)
    )

    print()

    print("=" * 60)
    print("Embedding Generation Completed")
    print("=" * 60)

    print(f"Candidates : {len(candidate_ids)}")
    print(f"Domains    : {len(domain_labels)}")
    return artifact_dir

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(

        "--candidates",
        required=True,
        # default="data/raw/candidates.jsonl",

        help="Path to candidates.jsonl"

    )

    args = parser.parse_args()
    generate_embeddings(
        args.candidates
    )



if __name__ == "__main__":
    main()
