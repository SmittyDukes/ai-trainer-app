from enum import Enum
from pydantic import BaseModel, Field, field_validator
from typing import Optional

class SkillLevel(str, Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    advanced = "advanced"

class FocusArea(str, Enum):
    shooting = "shooting"
    ball_handling = "ball handling"
    defense = "defense"
    footwork = "footwork"
    layups = "layups"
    passing = "passing"
    conditioning = "conditioning"


class TrainingRequest(BaseModel):
    name:str = Field(min_length=2, max_length=30)
    age:int = Field(ge=8, le=50)
    skill_level: SkillLevel
    focus_area: FocusArea
    session_duration_minutes:int = Field(ge=10, le=120)

    @field_validator("session_duration_minutes")
    @classmethod
    def must_be_multiple_of_five(cls, value):
        if value % 5 != 0:
            raise ValueError("duration must be multiple of 5")
        return value

class SessionBlock(BaseModel):
    name:str
    duration:int
    reason:Optional[str] = None

if __name__ == "__main__":
    # should PASS
    good = TrainingRequest(
        name="Smitty",
        age=15,
        skill_level="intermediate",
        focus_area="shooting",
        session_duration_minutes=60,
    )
    print("VALID:", good)

    try:
        bad = TrainingRequest(name="Ann", age=4, skill_level="pretty good",
                              focus_area="dunking", session_duration_minutes=23)
    except Exception as e:
        print("REJECTED:\n", e)