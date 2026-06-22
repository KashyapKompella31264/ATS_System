def build_candidate_document(candidate):

    profile = candidate["profile"]

    document = []

    document.append(
        f"HEADLINE:\n{profile.get('headline','')}\n"
    )

    document.append(
        f"SUMMARY:\n{profile.get('summary','')}\n"
    )

    document.append("CAREER HISTORY:")

    for job in candidate.get("career_history", []):

        document.append(
            f"""
                TITLE: {job.get('title','')}
                COMPANY: {job.get('company','')}
                DESCRIPTION:
                {job.get('description','')}
            """
        )

    document.append("\nSKILLS:")

    for skill in candidate.get("skills", []):

        document.append(skill["name"])

    return "\n".join(document)