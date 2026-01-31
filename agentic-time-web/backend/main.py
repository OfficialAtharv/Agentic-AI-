from fastapi import FastAPI
from pydantic import BaseModel
from agent import get_time_for_location
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class TimeRequest(BaseModel):
    location: str

@app.post("/time")
def fetch_time(request: TimeRequest):
    result = get_time_for_location(request.location)
    return {
        "location": request.location,
        "current_time": result
    }


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
