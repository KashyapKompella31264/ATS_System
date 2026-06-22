from src.parser.candidate_loader import load_candidates
from src.features.document_builder import build_candidate_document
from src.features.feature_extrator import feature_extrator
from src.utils.company_classifier import consulting_ratio

candidates=load_candidates("data/raw/candidates.jsonl")
print(len(candidates))
print(candidates[10]["candidate_id"])

doc=build_candidate_document(candidates[0])
print(doc)

features=feature_extrator(candidates[0])
print(features)


consulting=consulting_ratio(candidates[0])
print(consulting)