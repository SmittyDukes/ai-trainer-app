# AI Trainer API 
## An API that generates structured, explainable basketball training sessions from a player profile and focus area.

# What It Does?
-Uses information provided by player or coach, it creates a custom workout session. The API uses name, age, skill level, focus area and duration. 
Skill levels are "beginner", "intermediate", and "advanced". Length of sessions can be between 60-120 minutes. Individual drills can also be selected, if a player/coach wants that option.

# How to run it?
- clone
- create venv
- activate
- In terminal: pip install -r requirements.txt, uvicorn main:app --reload
- Open: http://127.0.0.1:8000/docs


# Request and Response
-Request: {
  "name": "Smitty",
  "age": 16,
  "skill_level": "advanced",
  "focus_area": "shooting",
  "session_duration_minutes": 60
}
-Response: [
  {
    "name": "Warm-up",
    "duration": 10,
    "reason": null
  },
  {
    "name": "Form Shooting",
    "duration": 5,
    "reason": "Warm up shooting form"
  },
  {
    "name": "Spot Shooting Adv",
    "duration": 10,
    "reason": "Get familiar with the angle and distance from long distance"
  },
  {
    "name": "Catch and Shoot Adv",
    "duration": 10,
    "reason": "Get comfortable with catching on the move to shot at long distance"
  },
  {
    "name": "Skill Reinforcement",
    "duration": 20,
    "reason": null
  },
  {
    "name": "Cool-down",
    "duration": 5,
    "reason": null
  }
]

# How it Works?
- Request for API to generate session
- The model parses and validates the request to make sure it is valid before inference.
- Based on input the decision engine filters through all the drills to fill session with appropriate drills that fill the duration requested
- The response model shapes a clean output and sends back to the user.
