from datastores import athletes
from models.models import Athlete
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
    is_eligible = monthly_duration >= 6 # eligible after 6 months

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

