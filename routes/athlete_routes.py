from datastores import athletes
from models.athlete import Athlete, AthleteUpdate, BeltColor, PROMOTION_REQUIREMENTS
from fastapi import HTTPException
from datetime import date
from fastapi import APIRouter

athletes_router = APIRouter(
    prefix="/athletes",
    tags=["athletes"]
)

@athletes_router.get("/")
async def get_all_athletes():
    return list(athletes.values())
    

def is_eligible_for_promotion(rank: BeltColor, months_practiced: int, tournaments: int, teachings: int):
    requirements = PROMOTION_REQUIREMENTS[BeltColor(rank)]
    return (
        months_practiced >= requirements["months"] 
        and tournaments >= requirements["tournaments"] 
        and teachings >= requirements["teachings"]
    )
