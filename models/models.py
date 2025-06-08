from pydantic import BaseModel
from datetime import date

class Athlete(BaseModel):
    athlete_id: int          # Identification of the athlete
    athlete_name: str        # Name of athlete
    athlete_age: int         # Age of athlete
    athlete_belt_rank: str   # The belt rank of the athlete
    athlete_start_date: date # Date when athlete joined

class Session(BaseModel):
    session_id: int       # Identification of the session
    athlete_id: int       # Identification of the athelete
    session_type: str     # Type of session: "sparring", "forms", "breaking", "technique", etc.
    session_date: date    # Date of the session
    instructor_notes: str # Instructor notes 