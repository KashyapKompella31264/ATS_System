from src.parser.candidate_loader import load_candidates
from src.parser.jd_parser import parse_jd

from src.scoring.semantic_score import semantic_search

from src.scoring.career_score import (
    calculate_career_score
)


# ------------------------------------------
# Load Data
# ------------------------------------------

candidates = load_candidates(
    "data/raw/candidates.jsonl"
)

jd_features = parse_jd()

results = semantic_search(10)

print("=" * 60)

for result in results:

    candidate = candidates[
        result["index"]
    ]

    output = calculate_career_score(
        candidate,
        jd_features
    )

    print(candidate["candidate_id"])
    print()

    print(
        "Career Score :",
        output["career_score"]
    )

    print()

    print(
        "Years Score :",
        output["years_score"]
    )

    print(
        "Relevant Experience :",
        output["relevant_experience_score"]
    )

    print(
        "Career Progression :",
        output["career_progression_score"]
    )

    print(
        "Consulting Company :",
        output["consulting_company_score"]
    )
    
    print(
        "Career Stability :",
        output["career_stability_score"]
    )

    print(
        "Current Role :",
        output["current_role_score"]
    )

    print("-" * 60)
