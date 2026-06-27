def build_general_document(candidate):

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

        document.append(skill.get("name", ""))

    document.append("\nEDUCATION:")

    for edu in candidate.get("education", []):

        document.append(
            f"""
DEGREE: {edu.get('degree','')}
FIELD: {edu.get('field_of_study','')}
"""
        )

    return "\n".join(document)

def build_career_document(candidate):

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

    return "\n".join(document)



def build_skill_document(candidate):

    document = []

    document.append("SKILLS:")

    for skill in candidate.get("skills", []):

        document.append(
            f"""
SKILL:
{skill.get("name","")}

PROFICIENCY:
{skill.get("proficiency","")}

EXPERIENCE:
{skill.get("duration_months",0)} months

ENDORSEMENTS:
{skill.get("endorsements",0)}
"""
        )

    assessments = (
        candidate.get("redrob_signals", {})
                 .get("skill_assessment_scores", {})
    )

    if assessments:

        document.append("SKILL ASSESSMENTS:")

        for skill, score in assessments.items():

            document.append(
                f"""
SKILL:
{skill}

ASSESSMENT SCORE:
{score}
"""
            )

    return "\n".join(document)