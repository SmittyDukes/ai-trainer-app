from drills_data import DRILLS # pull the data in - logic reads from the data file

def filter_drills_by_skill(focus_area, skill_level):
    drills_for_focus = DRILLS[focus_area]  # list for this focus area
    matching = [] # collect the drills that suit the player
    for drill in drills_for_focus: # walk the list
        if skill_level in drill["skill_level"]:
            matching.append(drill)
    return matching



def generate_session(focus_area, skill_level, session_duration_minutes):
    warm_up = 10
    cool_down = 5
    skill_time = session_duration_minutes - warm_up - cool_down

    available_drills = filter_drills_by_skill(focus_area, skill_level)

    selected_drill = []
    remaining = skill_time

    for drill in available_drills:
        if drill["duration"] <= remaining:
            selected_drill.append(drill)
            remaining -= drill["duration"]
        else:
            break
    # ↑ loop ENDS here. Everything below is at function level (4 spaces), NOT inside the loop.

    warm_up_block = {"name": "Warm-up", "duration": warm_up}
    cool_down_block = {"name": "Cool-down", "duration": cool_down}

    session = [warm_up_block]
    session = session + selected_drill

    if remaining > 0:
        reinforcement_block = {"name": "Skill Reinforcement", "duration": remaining}
        session.append(reinforcement_block)

    session.append(cool_down_block)

    return session


if __name__ == "__main__":
    result_2 = generate_session("shooting", "beginner", 60)
    for d in result_2:
        print(d["name"], d["duration"])