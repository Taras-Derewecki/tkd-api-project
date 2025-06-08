from pydantic import BaseModel
from datetime import date
from enum import Enum

class Athlete(BaseModel):
    athlete_id: int               # Identification of the athlete
    athlete_name: str             # Name of athlete
    athlete_age: int              # Age of athlete
    athlete_belt_rank: Enum       # The belt rank of the athlete
    athlete_start_date: date      # Date when athlete joined
    num_of_athlete_teachings: int # How many times did the athlete teach

class Session(BaseModel):
    session_id: int       # Identification of the session
    athlete_id: int       # Identification of the athelete
    session_type: Enum    # Type of session: "sparring", "forms", "breaking", "technique", etc.
    session_date: date    # Date of the session
    instructor_notes: str # Instructor notes 

class BeltColor(Enum):
    WHITE = 1
    YELLOW = 2
    ORANGE = 3
    GREEN = 4
    BLUE = 5
    PURPLE = 6
    BROWN = 7
    RED = 8
    CHO_DAN_BO = 9
    FIRST_DEGREE_BLACK = 10
    SECOND_DEGREE_BLACK = 11
    THIRD_DEGREE_BLACK = 12
    FOURTH_DEGREE_BLACK = 13
    FIFTH_DEGREE_BLACK = 14
    SIXTH_DEGREE_BLACK = 15
    SEVENTH_DEGREE_BLACK = 16
    EIGHTH_DEGREE_BLACK = 17
    NINETH_DEGREE_BLACK = 18

class SessionType(Enum):
    SPARRING = 1
    FORMS = 2
    BREAKING = 3
    TECHNIQUE = 4
