CONSULTING_COMPANIES = {
    "tcs",
    "infosys",
    "capgemini",
    "wipro",
    "accenture",
    "cognizant",
    "tech mahindra",
    "mindtree",
    "globex firm"
}


def product_company_score(candidate):

    history = candidate.get(
        "career_history",
        []
    )

    if len(history) == 0:
        return 0

    consulting_months = 0
    total_months = 0

    for job in history:

        company = job.get(
            "company",
            ""
        ).lower()

        months = job.get(
            "duration_months",
            0
        )

        total_months += months

        for consulting_company in CONSULTING_COMPANIES:

            if consulting_company in company:

                consulting_months += months
                break

    if total_months == 0:
        return 0

    return consulting_months / total_months