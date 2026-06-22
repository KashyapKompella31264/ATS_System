CONSULTING_COMPANIES={
    "tcs",
    "infosys",
    "capgemini",
    "wipro",
    "accenture",
    "cognizant",
    "tech mahindra"
    "mindtree"
    "globex frim"
}

def consulting_ratio(candidate):

    history = candidate.get(
        "career_history",
        []
    )

    total = len(history)

    consulting = 0

    for job in history:

        company = job["company"].lower()

        if company in CONSULTING_COMPANIES:
            consulting += 1

    if total == 0:
        return 0

    return consulting / total
