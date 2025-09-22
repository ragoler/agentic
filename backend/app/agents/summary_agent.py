from app.mcp_gateway.gateway import MCPGateway
from app.models.trip import LiveFlightState, HotelOption
from typing import List

class SummaryAgent:
    """
    An agent that uses the MCPGateway to generate trip summaries.
    """
    def __init__(self, mcp: MCPGateway):
        self.mcp = mcp

    async def generate_summary(self, destination: str, flights: List[LiveFlightState], hotels: List[HotelOption]) -> str:
        """
        Generates a natural language summary by creating a prompt and calling the MCP.
        """
        prompt = self._create_prompt(destination, flights, hotels)
        
        # Delegate the external call to the MCP
        return await self.mcp.generate_text_summary(prompt)

    def _create_prompt(self, destination: str, flights: List[LiveFlightState], hotels: List[HotelOption]) -> str:
        flight_details = "\n".join([f"- Flight {f.callsign} from {f.origin_country}" for f in flights]) if flights else "No live flights found nearby."
        hotel_details = "\n".join([f"- {h.name} (${h.price_per_night}/night, {h.rating} stars)" for h in hotels]) if hotels else "No hotels found."

        return f"""
        You are a helpful travel assistant.
        Generate a brief, friendly, and inviting summary for a trip to {destination}.
        The summary should be a single paragraph.
        
        Here is the data you have to work with:
        
        Live Flights Currently Near Destination:
        {flight_details}
        
        Hotel Options:
        {hotel_details}
        
        Based on this, write a short, engaging summary for the user's upcoming trip.
        """

