# Duration must be a minimum of 10 minutes and maximun of 120 minutes.
# Duration should also only be multiples of 5
def validate_request(name, age, skill, focus_area, session_duration_minutes):
    allowed_skills = ["beginner", "intermediate", "advanced"]
    allowed_focus_areas = ["shooting", "ball handling", "defense", "footwork", "layups",
                           "passing", "conditioning"]

    errors = []
    # validate name
    if name == "":
        errors.append("name cannot be empty")
    # validate age
    if age < 0 or age > 100:
        errors.append(f"invalid age: {age}")
    # Validate skill
    if skill not in allowed_skills:
        errors.append(f"invalid skill: {skill}")
    # validate focus area
    if focus_area not in allowed_focus_areas:
        errors.append(f"invalid focus area: {focus_area}")
    # validate duration
    if session_duration_minutes % 5 != 0 or session_duration_minutes < 10 or session_duration_minutes > 120:
        errors.append("duration must be a multiple of 5, between 10 and 120 minutes")

    if errors:
        return {"valid": False, "errors": errors}
    return {"valid": True, "errors": []}