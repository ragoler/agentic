from app.mcp_gateway.gateway import MCPGateway

GEOCODE_MOCK = {
    "paris, france": (48.8566, 2.3522),
    "tokyo, japan": (35.6895, 139.6917),
    "new york, usa": (40.7128, -74.0060),
}

class FlightAgent:
    """
    An agent specialized in finding and processing flight information.
    """
    def __init__(self, mcp: MCPGateway):
        self.mcp = mcp

    async def search(self, destination: str):
        """
        Searches for live flights by calling the MCPGateway.
        """
        destination_lower = destination.lower()
        if destination_lower not in GEOCODE_MOCK:
            return []
        
        lat, lon = GEOCODE_MOCK[destination_lower]
        
        # Delegate the external call to the MCP
        raw_data = await self.mcp.get_live_flights(lat, lon)
        
        # Process the data into the desired format
        return self._process_flight_data(raw_data)

    def _process_flight_data(self, data):
        flights = []
        if data and data.get("states"):
            for state in data["states"][:10]:
                flights.append({
                    "callsign": state[1].strip() or "N/A",
                    "origin_country": state[2],
                    "longitude": state[5],
                    "latitude": state[6],
                    "on_ground": state[8],
                })
        return flights
