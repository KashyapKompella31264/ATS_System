import tempfile
import os
import pandas as pd
import gradio as gr

from src.features.embedding_generator import generate_embeddings
from src.ranking.rank_candidates import rank_candidates
def run_ranking(uploaded_file):

    if uploaded_file is None:
        raise gr.Error("Please upload a candidates.jsonl file.")

    try:

        artifact_dir = tempfile.mkdtemp()

        generate_embeddings(
            candidates_path=uploaded_file.name,
            artifact_dir=artifact_dir
        )

        results = rank_candidates(
            candidates_path=uploaded_file.name,
            top_k=100,
            artifact_dir=artifact_dir
        )

        rows = []

        for rank, candidate in enumerate(results, start=1):

            rows.append({

                "rank": rank,

                "candidate_id": candidate["candidate_id"],

                "score": candidate["final_score"],

                "reason": candidate["reason"]

            })

        df = pd.DataFrame(rows)

        csv_path = os.path.join(
            artifact_dir,
            "submission.csv"
        )

        df.to_csv(
            csv_path,
            index=False
        )

        return df.head(10), csv_path

    except Exception as e:

        raise gr.Error(str(e))

demo = gr.Interface(
    fn=run_ranking,
    inputs=gr.File(
    label="Upload candidates.jsonl",
    file_types=[".jsonl"]
),
    outputs=[
        gr.Dataframe(
            label="Top 10 Candidates"
        ),
        gr.File(
            label="Download submission.csv"
        )
    ],
    title="AI Candidate Ranking System",
    description="Upload a JSONL file containing up to 100 candidates. The system generates embeddings, ranks candidates, and returns a submission CSV."
)




if __name__ == "__main__":
    demo.queue().launch(
        server_name="0.0.0.0",
        server_port=7860
    )