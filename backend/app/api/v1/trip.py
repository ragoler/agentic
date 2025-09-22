from fastapi import APIRouter
from app.models.trip import TripRequest, TripPlan, FlightOption, HotelOption

router = APIRouter()

@router.post("/plan", response_model=TripPlan, tags=["Planning"])
async def get_trip_plan(request: TripRequest):
    """
    Accepts user's trip request and returns a mock trip plan.
    """
    # Mock data for now
    mock_flights = [
        FlightOption(airline="Airline A", price=500.0, departure_time="10:00"),
        FlightOption(airline="Airline B", price=550.0, departure_time="12:00"),
    ]
    mock_hotels = [
        HotelOption(name="Hotel X", price_per_night=150.0, rating=4.5),
        HotelOption(name="Hotel Y", price_per_night=200.0, rating=4.8),
    ]

    return TripPlan(flights=mock_flights, hotels=mock_hotels)
