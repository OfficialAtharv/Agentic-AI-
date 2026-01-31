import re
import requests
from datetime import datetime
from timezonefinder import TimezoneFinder
from city_timezone import CITY_TIMEZONE

tf = TimezoneFinder()


def extract_city(user_input: str):
    user_input = user_input.lower()

    patterns = [
        r"time of ([a-zA-Z\s]+)",
        r"time in ([a-zA-Z\s]+)",
        r"tell me time of ([a-zA-Z\s]+)",
        r"what is the time in ([a-zA-Z\s]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, user_input)
        if match:
            return match.group(1).strip()

    return None


def get_timezone_from_city(city: str):
    """
    City → lat/lon → timezone (NO external timezone API)
    """
    geo_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": city,
        "format": "json",
        "limit": 1
    }

    res = requests.get(
        geo_url,
        params=params,
        headers={"User-Agent": "time-agent"}
    ).json()

    if not res:
        return None

    lat = float(res[0]["lat"])
    lon = float(res[0]["lon"])

    return tf.timezone_at(lat=lat, lng=lon)


def get_city_time(city: str):
    """
    Get current time for ANY city safely.
    """

    city_key = city.lower().strip()
    timezone = CITY_TIMEZONE.get(city_key)

    if not timezone:
        timezone = get_timezone_from_city(city)

    if not timezone:
        return None

    try:
        url = f"https://worldtimeapi.org/api/timezone/{timezone}"
        res = requests.get(url, timeout=5)
        res.raise_for_status()

        data = res.json()
        dt = datetime.fromisoformat(data["datetime"])
        return dt.strftime("%I:%M %p")

    except Exception:
        return None



def get_time_for_location(user_input: str):
    """
    Entry point for FastAPI.
    Accepts raw user input (city / sentence) and returns time.
    """

    # Try extracting city from sentence
    city = extract_city(user_input)

    # If no pattern matched, assume input itself is city
    if not city:
        city = user_input.strip()

    time = get_city_time(city)

    if not time:
        return f"Sorry, I couldn't find the time for {city}."

    return f"The current time in {city.title()} is {time}."
