from src.scoring.semantic_score import semantic_search

from src.parser.candidate_loader import load_candidates

from src.scoring.consistency_score import (
    calculate_consistency_score
)


candidates = load_candidates(
    "data/raw/candidates.jsonl"
)

results = semantic_search(10)

print("=" * 60)

for candidate in results:

    profile = candidates[
        candidate["index"]
    ]

    output = calculate_consistency_score(
        profile,
        candidate["index"]
    )

    print(profile["candidate_id"])

    print(output)

    print("-" * 60)
