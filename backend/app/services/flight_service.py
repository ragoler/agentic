import httpx
from fastapi import HTTPException

# A simple, non-authenticated API for flight data
OPENSKY_API_URL = "https://opensky-network.org/api/states/all"

async def get_flights_near_destination(lat: float, lon: float):
    """
    Fetches flights from the OpenSky Network API near a given latitude and longitude.
    Note: This is a simple implementation for demonstration. It fetches all flights
    and then filters them, which is not efficient for a real-world application.
    """
    params = {
        "lamin": lat - 2.0, # Create a bounding box 2 degrees around the destination
        "lamax": lat + 2.0,
        "lomin": lon - 2.0,
        "lomax": lon + 2.0,
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(OPENSKY_API_URL, params=params, timeout=10.0)
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
            data = response.json()
            
            # Process the data into a more friendly format
            flights = []
            if data.get("states"):
                for state in data["states"][:10]: # Limit to 10 flights for this example
                    flights.append({
                        "callsign": state[1].strip() or "N/A",
                        "origin_country": state[2],
                        "longitude": state[5],
                        "latitude": state[6],
                        "on_ground": state[8],
                    })
            return flights
        except httpx.RequestError as exc:
            print(f"An error occurred while requesting {exc.request.url!r}.")
            raise HTTPException(status_code=503, detail="Error communicating with the flight data service.")
        except httpx.HTTPStatusError as exc:
            print(f"Error response {exc.response.status_code} while requesting {exc.request.url!r}.")
            raise HTTPException(status_code=503, detail="Received an error from the flight data service.")

# To make this work, we need a way to get lat/lon from a destination name.
# For now, we'll use a simple hardcoded dictionary.
# A real implementation would use a geocoding API.
GEOCODE_MOCK = {
    "paris, france": (48.8566, 2.3522),
    "tokyo, japan": (35.6895, 139.6917),
    "new york, usa": (40.7128, -74.0060),
}

async def get_flights_for_destination(destination: str):
    """
    Gets flight data for a given destination name.
    """
    destination_lower = destination.lower()
    if destination_lower not in GEOCODE_MOCK:
        # Return empty list if we don't have coordinates for the destination
        return []
    
    lat, lon = GEOCODE_MOCK[destination_lower]
    return await get_flights_near_destination(lat, lon)
