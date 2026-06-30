TARGET_LOCATIONS = {
    "noida",
    "pune"
}


def calculate_location_score(candidate):

    profile = candidate.get("profile", {})

    signals = candidate.get(
        "redrob_signals",
        {}
    )

    location = profile.get(
        "location",
        ""
    ).lower()

    willing = signals.get(
        "willing_to_relocate",
        False
    )

    for city in TARGET_LOCATIONS:

        if city in location:

            return {
                "location_score": 100
            }

    if willing:

        return {
            "location_score": 80
        }

    return {
        "location_score": 30
    }