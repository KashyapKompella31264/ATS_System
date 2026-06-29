from src.parser.candidate_loader import load_candidates
from src.utils.company_classifier import consulting_ratio


candidates = load_candidates(
    "data/raw/candidates.jsonl"
)

print("=" * 80)
print("Testing Consulting Company Classifier")
print("=" * 80)

consulting_found = 0

for candidate in candidates:

    ratio = consulting_ratio(candidate)

    if ratio > 0:

        consulting_found += 1

        print(
            f"\n{candidate['candidate_id']}"
        )

        print(
            f"Consulting Ratio : {ratio:.2f}"
        )

        print("Career History:")

        for job in candidate.get(
            "career_history",
            []
        ):

            print(
                "  -",
                job.get("company", "")
            )

        print("-" * 60)

        if consulting_found == 20:
            break


print()
print("=" * 80)
print(
    "Candidates with consulting experience:",
    consulting_found
)
print("=" * 80)
