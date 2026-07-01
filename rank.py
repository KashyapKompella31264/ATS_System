import os
import argparse
import pandas as pd

from src.ranking.rank_candidates import rank_candidates


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(

        "--candidates",

        required=True,

        help="Path to candidates.jsonl"

    )

    parser.add_argument(

        "--out",

        default="output/submission.csv",

        help="Output CSV"

    )

    parser.add_argument(

        "--artifact-dir",

        default="artifact",

        help="Directory containing precomputed embeddings"

    )

    args = parser.parse_args()

    results = rank_candidates(

        candidates_path=args.candidates,

        top_k=100,

        artifact_dir=args.artifact_dir

    )
    rows = []

    for rank, candidate in enumerate(results, start=1):

        rows.append({

            "candidate_id": candidate["candidate_id"],

            "rank": rank,

            "score": round(candidate["final_score"], 2),

            "reasoning": candidate["reason"]

        })

    df = pd.DataFrame(rows)

    os.makedirs(

        os.path.dirname(args.out),

        exist_ok=True

    )

    df.to_csv(

        args.out,

        index=False

    )

    print()

    print("=" * 60)

    print("Submission file created successfully!")

    print("=" * 60)

    print(args.out)


if __name__ == "__main__":

    main()
