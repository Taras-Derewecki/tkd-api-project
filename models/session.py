from pydantic import BaseModel
from datetime import date
from enum import Enum

class SessionType(Enum):
    SPARRING = "Sparring"
    FORMS = "Forms"
    BREAKING = "Breaking"
    TECHNIQUE = "Technique"

class SessionLength(Enum):
    SPARRING = 45
    FORMS = 60
    BREAKING = 45
    TECHNIQUE = 90

class Session(BaseModel):
    session_id: int                # Identification of the session
    athlete_id: int                # Identification of the athelete
    session_type: SessionType      # Type of session: "sparring", "forms", "breaking", "technique", etc.
    session_date: date             # Date of the session
    session_length: SessionLength  # Length of each session
    instructor_notes: str          # Instructor notes 
