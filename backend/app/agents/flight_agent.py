import httpx
from fastapi import HTTPException

OPENSKY_API_URL = "https://opensky-network.org/api/states/all"

GEOCODE_MOCK = {
    "paris, france": (48.8566, 2.3522),
    "tokyo, japan": (35.6895, 139.6917),
    "new york, usa": (40.7128, -74.0060),
}

class FlightAgent:
    """
    An agent specialized in finding flight information.
    """
    async def search(self, destination: str):
        """
        Searches for live flights near a given destination.
        """
        destination_lower = destination.lower()
        if destination_lower not in GEOCODE_MOCK:
            return []
        
        lat, lon = GEOCODE_MOCK[destination_lower]
        return await self._get_flights_near_coordinates(lat, lon)

    async def _get_flights_near_coordinates(self, lat: float, lon: float):
        params = {
            "lamin": lat - 2.0,
            "lamax": lat + 2.0,
            "lomin": lon - 2.0,
            "lomax": lon + 2.0,
        }
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(OPENSKY_API_URL, params=params, timeout=10.0)
                response.raise_for_status()
                data = response.json()
                
                flights = []
                if data.get("states"):
                    for state in data["states"][:10]:
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
