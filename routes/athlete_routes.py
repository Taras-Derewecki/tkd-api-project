from datastores import athletes
from models.athlete import Athlete, AthleteUpdate, BeltColor, PROMOTION_REQUIREMENTS
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
    

def is_eligible_for_promotion(rank: BeltColor, months_practiced: int, tournaments: int, teachings: int):
    requirements = PROMOTION_REQUIREMENTS[BeltColor(rank)]
    return (
        months_practiced >= requirements["months"] 
        and tournaments >= requirements["tournaments"] 
        and teachings >= requirements["teachings"]
    )

@router.get("/athletes/{athlete_id}")
async def get_athlete_info(athlete_id: int):
    if athlete_id not in athletes:
        raise HTTPException(status_code=404, detail="Athlete not found")
    
    athlete = athletes[athlete_id]
    today = date.today()
    monthly_duration = (today - athlete.athlete_start_date).days // 30

    is_eligible = is_eligible_for_promotion(
        athlete.athlete_belt_rank, 
        monthly_duration, 
        athlete.tournaments_at_current_rank,
        athlete.num_of_instructed_classes
    )

    return {
        "athlete_name" : athlete.athlete_name,
        "athlete_belt_rank" : athlete.athlete_belt_rank,
        "athlete_age" : athlete.athlete_age,
        "practicing_months" : monthly_duration,
        "eligible_for_promotion" : is_eligible,
        "tournaments_participated_in_at_current_rank": athlete.tournaments_at_current_rank,
        "num_of_instructed_classes" : athlete.num_of_instructed_classes
    }

@router.patch("/athletes/{athlete_id}")
async def update_athlete_info(athlete_id: int, updated: AthleteUpdate):
    if athlete_id not in athletes:
        raise HTTPException(status_code=404, detail="Athlete not found")
    
    existing_athlete = athletes[athlete_id]

    # Convert incoming partial data to a dictionary, excluding fields that were not set
    updated_data = updated.model_dump(exclude_unset=True)

    # Create a new Athlete object with existing data and updated fields
    new_athlete_data = existing_athlete.model_dump()

    for key in updated_data:
        new_athlete_data[key] = updated_data[key]

    # Re-validate and create a new Athlete object
    athletes[athlete_id] = Athlete(**new_athlete_data)

    return {"message": "Athlete updated successfully!"}

@router.delete("/athletes/{athlete_id}")
async def delete_athlete_info(athlete_id: int):
    if athlete_id not in athletes:
        raise HTTPException(status_code=404, detail="Athlete not found")
    del athletes[athlete_id]
    return {"message" : "Athlete deleted successfully!"}
