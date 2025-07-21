from fastapi import HTTPException, APIRouter, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from models.athlete import Athlete, AthleteUpdate
from models.session import Session, SessionUpdate, SessionType
from datastores import athletes, sessions
import json
import secrets
from datetime import date
from routes.athlete_routes import is_eligible_for_promotion

security = HTTPBasic()

def load_users():
    with open("users.json") as f:
        return json.load(f)

def require_admin(credentials: HTTPBasicCredentials = Depends(security)):
    users = load_users()
    username = credentials.username
    password = credentials.password

    user = users.get(username)
    if not user or not secrets.compare_digest(user["password"], password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    if user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    
    return username

admin_router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(require_admin)] # apply to all routes
)

@admin_router.get("/athletes")
async def get_all_athletes():
    return list(athletes.values())

@admin_router.post("/athletes")
async def add_athlete_info(athlete: Athlete):
    if athlete.athlete_id not in athletes:
        athletes[athlete.athlete_id] = athlete   
        return {"message": "Athlete added successfully!"}
    
    raise HTTPException(status_code=400, detail="Athlete already exists")

@admin_router.get("/athletes/{athlete_id}")
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

@admin_router.patch("/athletes/{athlete_id}")
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

@admin_router.delete("/athletes/{athlete_id}")
async def delete_athlete_info(athlete_id: int):
    if athlete_id not in athletes:
        raise HTTPException(status_code=404, detail="Athlete not found")
    del athletes[athlete_id]
    return {"message" : "Athlete deleted successfully!"}


# ----------------------------------------------------------------------------------


@admin_router.post("/sessions/")
async def add_session_info(session: Session):
    if session.session_id in sessions:
        raise HTTPException(status_code=400, detail="Session already exists")
    if session.athlete_id not in athletes:
        raise HTTPException(status_code=404, detail="Athlete not found")
    sessions[session.session_id] = session
    return {"message": "Session added"}

@admin_router.get("/sessions/{athlete_id}")
async def get_session_info(athlete_id: int):
    if athlete_id not in athletes:
        raise HTTPException(status_code=404, detail="Athlete not found")

    all_sessions = []
    sparring = 0
    forms = 0
    breaking = 0
    technique = 0

    for session in sessions.values():
        if session.athlete_id == athlete_id:
            all_sessions.append(session)
            if session.session_type == SessionType.SPARRING:
                sparring += 1
            elif session.session_type == SessionType.FORMS:
                forms += 1
            elif session.session_type == SessionType.BREAKING:
                breaking += 1
            elif session.session_type == SessionType.TECHNIQUE:
                technique += 1

    return {
        "total_sessions": len(all_sessions),
        "sparring_sessions": sparring,
        "form_sessions": forms,
        "breaking_sessions": breaking,
        "technique_sessions": technique
    }

@admin_router.patch("/sessions/{session_id}")
async def update_session_info(session_id: int, updated: SessionUpdate):
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    
    existing_session = sessions[session_id]

    # Convert existing session to a dict
    existing_data = existing_session.model_dump()

    # Merge updated fields into existing data
    updated_data = updated.model_dump(exclude_unset=True)

    for key, value in updated_data.items():
        existing_data[key] = value

    # Re-validate and create a new Session object
    sessions[session_id] = Session(**existing_data)

    return {"message": "Session updated"}

@admin_router.delete("/sessions/{session_id}")
async def delete_session_info(session_id: int):
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    del sessions[session_id]
    return {"message": "Session deleted"}
