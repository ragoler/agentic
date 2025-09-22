import asyncio
from fastapi import APIRouter
from app.models.trip import TripRequest, TripPlan
from app.services.flight_service import get_flights_for_destination
from app.services.hotel_service import get_hotels_for_destination

router = APIRouter()

@router.post("/plan", response_model=TripPlan, tags=["Planning"])
async def get_trip_plan(request: TripRequest):
    """
    Accepts user's trip request and returns a trip plan by calling external services.
    """
    # Run the service calls concurrently
    flight_task = get_flights_for_destination(request.destination)
    hotel_task = get_hotels_for_destination(request.destination)

    live_flights, hotels = await asyncio.gather(flight_task, hotel_task)

    return TripPlan(live_flights_nearby=live_flights, hotels=hotels)
