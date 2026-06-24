from src.features.generate_jd_embeddings import generate_jd_embedding
from src.features.embedding_generator import generate_embedding
from src.scoring.scemantic_score import calculate_similarity
from src.parser.candidate_loader import load_candidates
from src.features.document_builder import build_candidate_document
from src.features.embedding_generator import generate_embedding

candidates=load_candidates("data/raw/candidates.jsonl")
candidate=candidates[36]
document=build_candidate_document(candidate)
candidate_embedding=generate_embedding(document)

jd_embedding=generate_jd_embedding()
score=calculate_similarity(jd_embedding,candidate_embedding)
print(candidate["candidate_id"])
print(score)
