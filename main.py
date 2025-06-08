from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# from typing import Optional, List
from datetime import date
from contextlib import asynccontextmanager
from datastores import athletes, sessions
from models.models import Athlete, Session

# lifespan event handler to initialize data
@asynccontextmanager
async def lifespan(app: FastAPI):
    default_athlete = Athlete(
        athlete_id = 0,
        athlete_name = "Taras",
        athlete_age = 30,
        athlete_belt_rank = "1st Degree Black Belt",
        athlete_start_date = date(2008, 1, 1)
    )
    athletes[default_athlete.athlete_id] = default_athlete

    default_session = Session(
        session_id = 0,
        athlete_id = 0,
        session_type = "sparring",
        session_date = date(2025, 5, 18),
        instructor_notes = "string"
    )
    sessions[default_session.session_id] = default_session
    yield # startup complete, app runs
    # no shutdown cleanup needed

app = FastAPI(lifespan=lifespan)

@app.get("/")
def homepage():
    return {"Hello" : athletes[0].athlete_name}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
