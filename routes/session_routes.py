from datastores import sessions, athletes
from models.models import Session
from fastapi import HTTPException
from fastapi import APIRouter

router = APIRouter()

@router.get("/sessions/")
async def get_all_sessions():
    return list(sessions.values())

@router.post("/sessions/")
async def add_session_info(session: Session):
    if session.session_id in sessions:
        raise HTTPException(status_code=400, detail="Session already exists")
    if session.athlete_id not in athletes:
        raise HTTPException(status_code=404, detail="Athlete not found")
    sessions[session.session_id] = session
    return {"message": "Session added"}

@router.get("/sessions/{athlete_id}")
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
            if session.session_type == "sparring":
                sparring += 1
            elif session.session_type == "forms":
                forms += 1
            elif session.session_type == "breaking":
                breaking += 1
            elif session.session_type == "technique":
                technique += 1

    return {
        "total_sessions": len(all_sessions),
        "sparring_sessions": sparring,
        "form_sessions": forms,
        "breaking_sessions": breaking,
        "technique_sessions": technique
    }

@router.patch("/sessions/{session_id}")
async def update_session_info(session_id: int, updated: Session):
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    sessions[session_id] = updated
    return {"message": "Session updated"}

@router.delete("/sessions/{session_id}")
async def delete_session_info(session_id: int):
    if session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    del sessions[session_id]
    return {"message": "Session deleted"}
