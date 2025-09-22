import asyncio
from app.models.trip import TripRequest, TripPlan
from app.agents.flight_agent import FlightAgent
from app.agents.hotel_agent import HotelAgent
from app.agents.summary_agent import SummaryAgent

class OrchestratorAgent:
    """
    The orchestrator agent that manages the trip planning process.
    """
    def __init__(self):
        self.flight_agent = FlightAgent()
        self.hotel_agent = HotelAgent()
        self.summary_agent = SummaryAgent()

    async def plan_trip(self, request: TripRequest) -> TripPlan:
        """
        Coordinates the specialized agents to create a trip plan.
        """
        # Run the data-gathering agents concurrently
        flight_task = self.flight_agent.search(request.destination)
        hotel_task = self.hotel_agent.search(request.destination)

        live_flights, hotels = await asyncio.gather(flight_task, hotel_task)

        # After gathering data, generate the summary
        summary = await self.summary_agent.generate_summary(
            destination=request.destination,
            flights=live_flights,
            hotels=hotels
        )

        return TripPlan(
            summary=summary,
            live_flights_nearby=live_flights,
            hotels=hotels
        )
