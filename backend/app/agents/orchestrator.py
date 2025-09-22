import asyncio
from app.models.trip import TripRequest, TripPlan
from app.agents.flight_agent import FlightAgent
from app.agents.hotel_agent import HotelAgent
from app.agents.summary_agent import SummaryAgent
from app.mcp_gateway.gateway import MCPGateway

class OrchestratorAgent:
    """
    The orchestrator agent that manages the trip planning process.
    """
    def __init__(self):
        # The orchestrator is responsible for creating the gateway
        self.mcp_gateway = MCPGateway()
        # It injects the gateway into the agents that need it
        self.flight_agent = FlightAgent(self.mcp_gateway)
        self.hotel_agent = HotelAgent() # Hotel agent is mock, doesn't need MCP yet
        self.summary_agent = SummaryAgent(self.mcp_gateway)

    async def plan_trip(self, request: TripRequest) -> TripPlan:
        """
        Coordinates the specialized agents to create a trip plan.
        """
        flight_task = self.flight_agent.search(request.destination)
        hotel_task = self.hotel_agent.search(request.destination)

        live_flights, hotels = await asyncio.gather(flight_task, hotel_task)

        summary = await self.summary_agent.generate_summary(
            origin=request.origin,
            destination=request.destination,
            flights=live_flights,
            hotels=hotels
        )

        return TripPlan(
            summary=summary,
            live_flights_nearby=live_flights,
            hotels=hotels
        )
