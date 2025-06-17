from fastapi import FastAPI, HTTPException, APIRouter
from pydantic import BaseModel
# from typing import Optional, List
from datetime import date
from contextlib import asynccontextmanager
from datastores import athletes, sessions
from models.athlete import Athlete, BeltColor
from models.session import Session, SessionType, SessionLength
from routes import athlete_routes, session_routes

# lifespan event handler to initialize data
@asynccontextmanager
async def lifespan(app: FastAPI):
    default_athlete = Athlete(
        athlete_id = 0,
        athlete_name = "Taras",
        athlete_age = 30,
        athlete_belt_rank = BeltColor.FIRST_DEGREE_BLACK,
        athlete_start_date = date(2008, 1, 1),
        tournaments_at_current_rank = 2,
        num_of_instructed_classes = 10
    )
    athletes[default_athlete.athlete_id] = default_athlete

    default_session = Session(
        session_id = 0,
        athlete_id = 0,
        session_type = SessionType.SPARRING,
        session_date = date(2025, 5, 18),
        session_length = SessionLength.SPARRING,
        instructor_notes = "string"
    )
    sessions[default_session.session_id] = default_session
    yield # startup complete, app runs
    # no shutdown cleanup needed

app = FastAPI(lifespan=lifespan)

"""
- The app.include_router() function adds the router object 
  to the main application.

- The router object encapsulates all the path operations 
  defined within the respective route file.

- This approach allows you to modularize your API logic and 
  organize your routes into separate files, making your project 
  more maintainable and scalable
"""
app.include_router(athlete_routes.router)
app.include_router(session_routes.router)

@app.get("/")
def homepage():
    return {"Hello" : athletes[0].athlete_name}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
