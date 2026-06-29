from src.parser.candidate_loader import load_candidates

from src.scoring.semantic_score import semantic_search

from src.scoring.behaviour_score import (
    calculate_behavior_score
)


candidates = load_candidates(
    "data/raw/candidates.jsonl"
)

results = semantic_search(10)

print("=" * 60)

for result in results:

    candidate = candidates[
        result["index"]
    ]

    print(candidate["candidate_id"])

    output = calculate_behavior_score(
        candidate
    )

    print(output)

    print("-" * 60)