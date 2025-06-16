from pydantic import BaseModel
from datetime import date
from enum import Enum

class BeltColor(Enum):
    WHITE = "White Belt"
    YELLOW = "Yellow Belt"
    ORANGE = "Orange Belt"
    GREEN = "Green Belt"
    BLUE = "Blue Belt"
    PURPLE = "Purple Belt"
    BROWN = "Brown Belt"
    RED = "Red Belt"
    CHO_DAN_BO = "Cho Dan Bo"
    FIRST_DEGREE_BLACK = "First Degree Black Belt"
    SECOND_DEGREE_BLACK = "Second Degree Black Belt"
    THIRD_DEGREE_BLACK = "Third Degree Black Belt"
    FOURTH_DEGREE_BLACK = "Fourth Degree Black Belt"
    FIFTH_DEGREE_BLACK = "Fifth Degree Black Belt"
    SIXTH_DEGREE_BLACK = "Sixth Degree Black Belt"
    SEVENTH_DEGREE_BLACK = "Seventh Degree Black Belt"
    EIGHTH_DEGREE_BLACK = "Eighth Degree Black Belt"
    NINETH_DEGREE_BLACK = "Nineth Degree Black Belt"

class Athlete(BaseModel):
    athlete_id: int               # Identification of the athlete
    athlete_name: str             # Name of athlete
    athlete_age: int              # Age of athlete
    athlete_belt_rank: BeltColor  # The belt rank of the athlete
    athlete_start_date: date      # Date when athlete joined
    num_of_athlete_teachings: int # How many times did the athlete teach
