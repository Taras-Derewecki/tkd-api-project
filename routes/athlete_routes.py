from datastores import athletes
from models.athlete import Athlete, BeltColor
from fastapi import HTTPException
from datetime import date
from fastapi import APIRouter

router = APIRouter()

@router.get("/athletes/")
async def get_all_athletes():
    return list(athletes.values())

@router.post("/athletes/")
async def add_athlete_info(athlete: Athlete):
    if athlete.athlete_id not in athletes:
        athletes[athlete.athlete_id] = athlete   
        return {"message": "Athlete added successfully!"}
    
    raise HTTPException(status_code=400, detail="Athlete already exists")
    

@router.get("/athletes/{athlete_id}")
async def get_athlete_info(athlete_id: int):
    if athlete_id not in athletes:
        raise HTTPException(status_code=404, detail="Athlete not found")
    
    athlete = athletes[athlete_id]
    today = date.today()
    monthly_duration = (today - athlete.athlete_start_date).days // 30
    is_eligible = False

    if athlete.athlete_belt_rank == BeltColor.WHITE:
        # Promote in 3 months
        if monthly_duration >= 3:
            is_eligible = True

    elif athlete.athlete_belt_rank == BeltColor.YELLOW:
        # Promote in 6 months
        if monthly_duration >= 6:
            is_eligible = True

    elif athlete.athlete_belt_rank == BeltColor.ORANGE:
        # Promote in 6 months
        if monthly_duration >= 12:
            is_eligible = True

    elif athlete.athlete_belt_rank == BeltColor.GREEN:
        # Promote in 6 months
        if monthly_duration >= 18:
            is_eligible = True

    elif athlete.athlete_belt_rank == BeltColor.BLUE:
        # Promote in 6 months
        if monthly_duration >= 24:
            is_eligible = True

    elif athlete.athlete_belt_rank == BeltColor.PURPLE:
        # Promote in 8 months
        if monthly_duration >= 32:
            is_eligible = True

    elif athlete.athlete_belt_rank == BeltColor.BROWN:
        # Promote in 8 months
        if monthly_duration >= 40:
            is_eligible = True

    elif athlete.athlete_belt_rank == BeltColor.RED:
        # Promote in 8 months
        if monthly_duration >= 48:
            is_eligible = True

    elif athlete.athlete_belt_rank == BeltColor.CHO_DAN_BO:
        # Promote in 1 year
        if monthly_duration >= 60:
            is_eligible = True
    
    elif athlete.athlete_belt_rank == BeltColor.FIRST_DEGREE_BLACK:
        # Promote in 2 years
        if monthly_duration >= 84:
            is_eligible = True

    elif athlete.athlete_belt_rank == BeltColor.SECOND_DEGREE_BLACK:
        # Promote in 3 years
        if monthly_duration >= 120:
            is_eligible = True
    
    elif athlete.athlete_belt_rank == BeltColor.THIRD_DEGREE_BLACK:
        # Promote in 4 years
        if monthly_duration >= 168:
            is_eligible = True

    elif athlete.athlete_belt_rank == BeltColor.FOURTH_DEGREE_BLACK:
        # Promote in 5 years
        if monthly_duration >= 228:
            is_eligible = True

    elif athlete.athlete_belt_rank == BeltColor.FIFTH_DEGREE_BLACK:
        # Promote in 6 years - MASTER RANK
        if monthly_duration >= 300:
            is_eligible = True
        
    elif athlete.athlete_belt_rank == BeltColor.SIXTH_DEGREE_BLACK:
        # Promote in 7 years - MASTER RANK
        if monthly_duration >= 384:
            is_eligible = True

    elif athlete.athlete_belt_rank == BeltColor.SEVENTH_DEGREE_BLACK:
        # Promote in 8 years - MASTER RANK
        if monthly_duration >= 480:
            is_eligible = True   

    elif athlete.athlete_belt_rank == BeltColor.EIGHTH_DEGREE_BLACK:
        # Promote in 9 years - GRANDMASTER RANK
        if monthly_duration >= 588:
            is_eligible = True

    return {
        "athlete_name" : athlete.athlete_name,
        "athlete_belt_rank" : athlete.athlete_belt_rank,
        "athlete_age" : athlete.athlete_age,
        "practicing_months" : monthly_duration,
        "eligible_for_promotion" : is_eligible,
        "num_of_athlete_teachings" : athlete.num_of_athlete_teachings
    }

# implement code for the actual patch later... changing to put
@router.put("/athletes/{athlete_id}")
async def update_athlete_info(athlete_id: int, updated: Athlete):
    if athlete_id not in athletes:
        raise HTTPException(status_code=404, detail="Athlete not found")
    athletes[athlete_id] = updated
    return {"message" : "Athlete updated successfully!"}

@router.delete("/athletes/{athlete_id}")
async def delete_athlete_info(athlete_id: int):
    if athlete_id not in athletes:
        raise HTTPException(status_code=404, detail="Athlete not found")
    del athletes[athlete_id]
    return {"message" : "Athlete deleted successfully!"}
