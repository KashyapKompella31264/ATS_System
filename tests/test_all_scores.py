from src.parser.candidate_loader import load_candidates
from src.parser.jd_parser import parse_jd
from src.scoring.semantic_score import semantic_search
from src.scoring.domain_score import calculate_domain_score
from src.scoring.consistency_score import calculate_consistency_score
from src.scoring.behaviour_score import calculate_behavior_score
from src.scoring.career_score import calculate_career_score


# -------------------------------------------------------
# Load Data
# -------------------------------------------------------

candidates = load_candidates(
    "data/raw/candidates.jsonl"
)

jd_features = parse_jd()

results = semantic_search(20)

print("=" * 80)
print("Top 10 Candidate Score Breakdown")
print("=" * 80)

for result in results:

    index = result["index"]

    candidate = candidates[index]

    semantic_score = result["semantic_score"] * 100

    domain = calculate_domain_score(index)

    consistency = calculate_consistency_score(
        candidate,
        index
    )

    behavior = calculate_behavior_score(
        candidate
    )

    career = calculate_career_score(
        candidate,
        jd_features
    )

    print()

    print("=" * 80)

    print(candidate["candidate_id"])

    print("=" * 80)

    print(
        f"Semantic Score      : {semantic_score:.2f}"
    )

    print(
        f"Domain Score        : {domain['domain_score']:.2f}"
    )

    print(
        f"Consistency Score   : {consistency['consistency_score']:.2f}"
    )

    print(
        f"Behavior Score      : {behavior['behavior_score']:.2f}"
    )

    print(
        f"Career Score        : {career['career_score']:.2f}"
    )

    print("-" * 80)

    print("Career Breakdown")

    print(
        f"Years               : {career['years_score']:.2f}"
    )

    print(
        f"Relevant Experience : {career['relevant_experience_score']:.2f}"
    )

    print(
        f"Product Company     : {career['consulting_company_score']:.2f}"
    )

    print(
        f"Career Stability    : {career['career_stability_score']:.2f}"
    )

    print(
        f"Current Role        : {career['current_role_score']:.2f}"
    )

    print("-" * 80)
