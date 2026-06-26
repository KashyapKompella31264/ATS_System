from src.scoring.semantic_score import semantic_search
from src.scoring.domain_score import calculate_domain_score


results = semantic_search(50)

for candidate in results:

    print("=" * 60)

    print(candidate["candidate_id"])

    output = calculate_domain_score(
        candidate["index"]
    )

    print()

    print("Similarity Scores")

    for domain, score in output[
        "similarity_scores"
    ].items():

        print(f"{domain:<20} {score:.3f}")

    print()

    print(
        "Domain Score :",
        output["domain_score"]
    )

    print()

    print("Matched Domains")

    for domain, similarity in output[
        "matched_domains"
    ]:

        print(
            f"{domain:<25} {similarity:.3f}"
        )

    print()