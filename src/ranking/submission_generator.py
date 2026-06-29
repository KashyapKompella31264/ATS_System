import pandas as pd
import os
from rank import rank_candidates


def generate_submission():

    print("Ranking Candidates...")

    ranked = rank_candidates(100)

    submission = []

    for rank, candidate in enumerate(
        ranked,
        start=1
    ):

        submission.append({

            "rank": rank,

            "candidate_id":
                candidate["candidate_id"],

            "score":
                candidate["final_score"],

            "reason":
                candidate["reason"]

        })

    df = pd.DataFrame(submission)

    

    os.makedirs("output", exist_ok=True)

    df.to_csv(
        os.path.join("output", "submission.csv"),
        index=False
    )

    print()

    print("=" * 60)

    print("Submission Generated")

    print("=" * 60)

    print(df.head())


if __name__ == "__main__":

    generate_submission()