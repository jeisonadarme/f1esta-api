import fastf1
import json
from datetime import datetime, timezone # Import timezone

import os
import pandas as pd

def get_next_race(year: int):
    # Enable caching to speed up subsequent API calls
    cache_dir = os.path.join(os.path.dirname(__file__), 'cache')
    fastf1.Cache.enable_cache(cache_dir)
    
    # Get the current schedule
    # Get the full event schedule
    schedule = fastf1.get_event_schedule(year, include_testing=True)
    # Get current time in UTC
    now = datetime.now(timezone.utc)
    
    # Find the next race
    next_race = None
    for _, event in schedule.iterrows():
        event_date = pd.to_datetime(event['EventDate']).tz_localize('UTC')
        if event_date > now:
            next_race = event
            break
    
    if next_race is None:
        return json.dumps({
            "error": "No upcoming races found"
        })
    
    # Format the response as JSON
    response = {
        "race_name": next_race['EventName'],
        "circuit_name": next_race['OfficialEventName'],
        "country": next_race['Country'],
        "race_date": pd.to_datetime(next_race['Session5DateUtc']).isoformat(),
        "round": next_race['RoundNumber'],
        "session1": next_race["Session1"],
        "session1DateUtc": pd.to_datetime(next_race['Session1DateUtc']).isoformat(),
        "session2": next_race["Session2"],
        "session2DateUtc": pd.to_datetime(next_race['Session2DateUtc']).isoformat(),
        "session3": next_race["Session3"],
        "session3DateUtc": pd.to_datetime(next_race['Session3DateUtc']).isoformat(),
        "session4": next_race["Session4"],
        "session4DateUtc": pd.to_datetime(next_race['Session4DateUtc']).isoformat(),
        "session5": next_race["Session5"],
        "session5DateUtc": pd.to_datetime(next_race['Session5DateUtc']).isoformat(),
    }

    return json.dumps(response)

if __name__ == "__main__":
    print(get_next_race())