EVALUATION_KEYWORDS = {

    "offline",

    "online",

    "evaluation",

    "benchmark",

    "ab test",

    "a/b",

    "relevance",

    "human relevance",

    "offline-online",

    "precision",

    "recall",

    "ndcg",

    "latency"
}


def calculate_evaluation_score(candidate):

    history = candidate.get(
        "career_history",
        []
    )

    text = ""

    for job in history:

        text += " "

        text += job.get(
            "description",
            ""
        ).lower()

    matches = 0

    for keyword in EVALUATION_KEYWORDS:

        if keyword in text:

            matches += 1

    score = min(
        matches * 15,
        100
    )

    return {

        "evaluation_score": score
    }
