def profile_score(candidate):

    return candidate["redrob_signals"].get(
        "profile_completeness_score",
        0
    )


def recruiter_response_score(candidate):

    return (
        candidate["redrob_signals"].get(
            "recruiter_response_rate",
            0
        ) * 100
    )


def interview_score(candidate):

    return (
        candidate["redrob_signals"].get(
            "interview_completion_rate",
            0
        ) * 100
    )


def github_score(candidate):

    github_score= candidate["redrob_signals"].get(
        "github_activity_score",
        0
    )
    return min(max(github_score,0),100)


def saved_by_recruiters_score(candidate):

    saved = candidate["redrob_signals"].get(
        "saved_by_recruiters_30d",
        0
    )

    return min(saved, 100)


def search_appearance_score(candidate):

    appearances = candidate["redrob_signals"].get(
        "search_appearance_30d",
        0
    )

    return min(appearances / 10, 100)


def open_to_work_score(candidate):

    return (
        100
        if candidate["redrob_signals"].get(
            "open_to_work_flag",
            False
        )
        else 0
    )


def calculate_behavior_score(candidate):

    profile = profile_score(candidate)

    recruiter = recruiter_response_score(candidate)

    interview = interview_score(candidate)

    github = github_score(candidate)

    saved = saved_by_recruiters_score(candidate)

    search = search_appearance_score(candidate)

    open_to_work = open_to_work_score(candidate)

    behavior = (

        0.15 * profile +

        0.20 * recruiter +

        0.20 * interview +

        0.15 * github +

        0.10 * saved +

        0.10 * search +

        0.10 * open_to_work

    )

    return {

        "behavior_score": round(float(behavior), 2),

        "profile_score": round(float(profile), 2),

        "recruiter_response_score": round(float(recruiter), 2),

        "interview_score": round(float(interview), 2),

        "github_score": round(float(github), 2),

        "saved_by_recruiters_score": round(float(saved), 2),

        "search_appearance_score": round(float(search), 2),

        "open_to_work_score": round(float(open_to_work), 2)

    }
