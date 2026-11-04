import csv
import os
from collections import defaultdict


def load_rides(csv_path: str) -> list[dict[str, object]]:
    """Load ride data from a CSV file."""
    rides = []
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Could not find file: {csv_path}")
    with open(csv_path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for ride in r:
            rides.append(
                {
                    "ride_id": ride["ride_id"],
                    "start_station": ride["start_station"],
                    "end_station": ride["end_station"],
                    "duration_min": float(ride["duration_min"]),
                    "rider_type": ride["rider_type"],
                }
            )
    return rides


def average_duration(rides):
    """Return the average ride duration in minutes."""
    if len(rides) == 0:
        return 0.0
    duration = 0.0
    for ride in rides:
        duration += ride["duration_min"]
    return duration / len(rides)


def count_by_rider_type(rides):
    """Count rides for each rider type."""
    count = defaultdict(int)
    for ride in rides:
        count[ride["rider_type"]] += 1
    return dict(count)


def busiest_start_station(rides):
    """Return the start station with the most rides."""
    if rides is None:
        raise ValueError("rides must not be None")
    if len(rides) == 0:
        raise ValueError("rides must not be empty")
    count = {}
    for ride in rides:
        d = ride["start_station"]
        count[d] = count.get(d, 0) + 1
    return max(count, key=count.get)


def filter_long_rides(rides, duration=30):
    """Return all rides with duration greater than or equal to b minutes."""
    long_ride = []
    for ride in rides:
        if ride["duration_min"] >= duration:
            long_ride.append(ride)
    return long_ride
