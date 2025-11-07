from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from f1 import get_next_race

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/next-race/{year}")
def next_race(year: int):
    return json.loads(get_next_race(year))  # FastAPI expects dict not JSON string