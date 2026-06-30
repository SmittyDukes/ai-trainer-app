from fastapi import FastAPI
from models import TrainingRequest, SessionBlock
from decision import generate_session
from typing import List


app = FastAPI()

@app.post("/generate-session", response_model=List[SessionBlock])
def create_session(request: TrainingRequest):
    session = generate_session(request.focus_area, request.skill_level, request.session_duration_minutes)
    return session