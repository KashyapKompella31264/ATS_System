from src.parser.candidate_loader import load_candidates
from src.parser.jd_parser import parse_jd
from src.ranking.reason_generator import generate_reason
from src.scoring.semantic_score import semantic_search
from src.scoring.domain_score import calculate_domain_score
from src.scoring.consistency_score import calculate_consistency_score
from src.scoring.behaviour_score import calculate_behavior_score
from src.scoring.career_score import calculate_career_score
from src.scoring.location_score import calculate_location_score

# -------------------------------------------------------
# Final Weights
# -------------------------------------------------------

WEIGHTS = {
    "semantic": 0.35,
    "career": 0.22,
    "consistency": 0.15,
    "behavior": 0.13,
    "domain": 0.10,
    "location":0.05
}


# -------------------------------------------------------
# Final Ranking
# -------------------------------------------------------

def rank_candidates(candidates_path,top_k=100,artifact_dir="artifact"):

    print("Loading Candidates...")

    candidates = load_candidates(
        candidates_path
    )

    print("Parsing JD...")

    jd_features = parse_jd()

    print("Running Semantic Search...")

    semantic_results = semantic_search(
        min(30000,len(candidates)),
        artifact_dir
    )

    print(
        f"Scoring {len(semantic_results)} Candidates..."
    )

    ranked_candidates = []

    for result in semantic_results:

        index = result["index"]

        candidate = candidates[index]

        semantic_score = (
            result["semantic_score"] * 100
        )

        domain_score = calculate_domain_score(
            index,
            artifact_dir
        )["domain_score"]

        consistency_score = (
            calculate_consistency_score(
                candidate,
                index,
                artifact_dir
            )["consistency_score"]
        )

        behavior_score = (
            calculate_behavior_score(
                candidate
            )["behavior_score"]
        )

        career_score = (
            calculate_career_score(
                candidate,
                jd_features
            )["career_score"]
        )
        location_score = calculate_location_score(
                        candidate
                        )["location_score"]
        candidate_scores = {

            "semantic_score": semantic_score,

            "career_score": career_score,

            "consistency_score": consistency_score,

            "behavior_score": behavior_score,

            "domain_score": domain_score,

            "location_score":location_score

        }
        reason=generate_reason(candidate_scores)
        final_score = (
            semantic_score * WEIGHTS["semantic"] +
            career_score * WEIGHTS["career"] +
            consistency_score * WEIGHTS["consistency"] +
            behavior_score * WEIGHTS["behavior"] +
            domain_score * WEIGHTS["domain"]+
            location_score*WEIGHTS["location"]
        )
        
        ranked_candidates.append(

            {

                "candidate_id":
                    candidate["candidate_id"],

                "candidate":
                    candidate,

                "semantic_score":
                    round(semantic_score, 2),

                "domain_score":
                    round(domain_score, 2),

                "consistency_score":
                    round(consistency_score, 2),

                "behavior_score":
                    round(behavior_score, 2),

                "career_score":
                    round(career_score, 2),

                "final_score":
                    round(final_score, 2),
                "reason":
                    reason

            }

        )

    ranked_candidates.sort(
        key=lambda x: (
            -x["final_score"],
            x["candidate_id"]
        )
    )

    return ranked_candidates[:top_k]
