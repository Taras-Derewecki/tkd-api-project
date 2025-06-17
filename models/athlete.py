from pydantic import BaseModel
from datetime import date
from enum import Enum
from typing import Optional

class BeltColor(str, Enum):
    WHITE =                "White Belt"
    YELLOW =               "Yellow Belt"
    ORANGE =               "Orange Belt"
    GREEN =                "Green Belt"
    BLUE =                 "Blue Belt"
    PURPLE =               "Purple Belt"
    BROWN =                "Brown Belt"
    RED =                  "Red Belt"
    CHO_DAN_BO =           "Cho Dan Bo"
    FIRST_DEGREE_BLACK =   "First Degree Black Belt"
    SECOND_DEGREE_BLACK =  "Second Degree Black Belt"
    THIRD_DEGREE_BLACK =   "Third Degree Black Belt"
    FOURTH_DEGREE_BLACK =  "Fourth Degree Black Belt"
    FIFTH_DEGREE_BLACK =   "Fifth Degree Black Belt"
    SIXTH_DEGREE_BLACK =   "Sixth Degree Black Belt"
    SEVENTH_DEGREE_BLACK = "Seventh Degree Black Belt"
    EIGHTH_DEGREE_BLACK =  "Eighth Degree Black Belt"
    NINETH_DEGREE_BLACK =  "Nineth Degree Black Belt"

# Maps each belt to its promotion requirement in months
PROMOTION_REQUIREMENTS = {
    BeltColor.WHITE:                {"months": 3,   "tournaments": 0, "instructed": 0},
    BeltColor.YELLOW:               {"months": 6,   "tournaments": 0, "instructed": 0},
    BeltColor.ORANGE:               {"months": 12,  "tournaments": 1, "instructed": 0},
    BeltColor.GREEN:                {"months": 18,  "tournaments": 1, "instructed": 0},
    BeltColor.BLUE:                 {"months": 24,  "tournaments": 1, "instructed": 0},
    BeltColor.PURPLE:               {"months": 32,  "tournaments": 2, "instructed": 0},
    BeltColor.BROWN:                {"months": 40,  "tournaments": 2, "instructed": 0},
    BeltColor.RED:                  {"months": 48,  "tournaments": 2, "instructed": 0},
    BeltColor.CHO_DAN_BO:           {"months": 60,  "tournaments": 2, "instructed": 1},
    BeltColor.FIRST_DEGREE_BLACK:   {"months": 84,  "tournaments": 3, "instructed": 3},
    BeltColor.SECOND_DEGREE_BLACK:  {"months": 120, "tournaments": 5, "instructed": 5},
    BeltColor.THIRD_DEGREE_BLACK:   {"months": 168, "tournaments": 7, "instructed": 25},
    BeltColor.FOURTH_DEGREE_BLACK:  {"months": 228, "tournaments": 6, "instructed": 50},
    BeltColor.FIFTH_DEGREE_BLACK:   {"months": 300, "tournaments": 4, "instructed": 150},
    BeltColor.SIXTH_DEGREE_BLACK:   {"months": 384, "tournaments": 3, "instructed": 500},
    BeltColor.SEVENTH_DEGREE_BLACK: {"months": 480, "tournaments": 2, "instructed": 1000},
    BeltColor.EIGHTH_DEGREE_BLACK:  {"months": 588, "tournaments": 1, "instructed": 2500}
}

class Athlete(BaseModel):
    athlete_id: int                  # Identification of the athlete
    athlete_name: str                # Name of athlete
    athlete_age: int                 # Age of athlete
    athlete_belt_rank: BeltColor     # The belt rank of the athlete
    athlete_start_date: date         # Date when athlete joined
    tournaments_at_current_rank: int # How many tournaments the athlete attended at their current rank
    num_of_instructed_classes: int   # How many times did the athlete teach

class AthleteUpdate(BaseModel):
    athlete_name: Optional[str]
    athlete_age: Optional[int]
    athlete_belt_rank: Optional[BeltColor]
    athlete_start_date: Optional[date]
    tournaments_at_current_rank: Optional[int]
    num_of_athlete_teachings: Optional[int]
