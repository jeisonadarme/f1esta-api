from fastapi import FastAPI
import json
from f1 import get_next_race

app = FastAPI()

@app.get("/next-race/{year}")
def next_race(year: int):
    return json.loads(get_next_race(year))  # FastAPI expects dict not JSON string