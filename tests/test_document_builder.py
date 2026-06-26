from src.parser.candidate_loader import load_candidates
from src.features.document_builder import (
    build_general_document,
    build_career_document
)

candidates = load_candidates("data/raw/candidates.jsonl")

candidate = candidates[0]

print("=" * 70)
print("GENERAL DOCUMENT")
print("=" * 70)

print(build_general_document(candidate))

print("\n")

print("=" * 70)
print("CAREER DOCUMENT")
print("=" * 70)

print(build_career_document(candidate))