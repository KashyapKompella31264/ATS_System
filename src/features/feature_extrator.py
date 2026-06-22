def feature_extrator(candidate):
    profile=candidate["profile"]
    signals=candidate["redrob_signals"]

    return{
        "candidate_id":
            candidate["candidate_id"],
        "years_of_experience":
            profile["years_of_experience"],
        "current_title":
            profile["current_title"],
        "open_to_work":
            signals["open_to_work_flag"],
        "notice_period":
            signals["notice_period_days"],
        "response_rate":
            signals["recruiter_response_rate"],
        "saved_by_recruiters":
            signals["saved_by_recruiters_30d"],
        "github_score":
            signals["github_activity_score"]
    }