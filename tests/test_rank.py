from rank import rank_candidates


results = rank_candidates(10)

print("=" * 80)

print("FINAL RANKING")

print("=" * 80)

for rank, candidate in enumerate(results, start=1):

    print()

    print(f"Rank #{rank}")

    print(candidate["candidate_id"])

    print()

    print(
        "Final Score :",
        candidate["final_score"]
    )

    print()

    print(
        "Semantic :",
        candidate["semantic_score"]
    )

    print(
        "Career :",
        candidate["career_score"]
    )

    print(
        "Consistency :",
        candidate["consistency_score"]
    )

    print(
        "Behavior :",
        candidate["behavior_score"]
    )

    print(
        "Domain :",
        candidate["domain_score"]
    )

    print("-" * 80)