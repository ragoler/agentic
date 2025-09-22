import asyncio
from app.models.trip import TripRequest, TripPlan
from app.agents.flight_agent import FlightAgent
from app.agents.hotel_agent import HotelAgent

class OrchestratorAgent:
    """
    The orchestrator agent that manages the trip planning process.
    """
    def __init__(self):
        self.flight_agent = FlightAgent()
        self.hotel_agent = HotelAgent()

    async def plan_trip(self, request: TripRequest) -> TripPlan:
        """
        Coordinates the specialized agents to create a trip plan.
        """
        # Run the agent searches concurrently
        flight_task = self.flight_agent.search(request.destination)
        hotel_task = self.hotel_agent.search(request.destination)

        live_flights, hotels = await asyncio.gather(flight_task, hotel_task)

        return TripPlan(live_flights_nearby=live_flights, hotels=hotels)
