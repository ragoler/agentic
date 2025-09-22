from pydantic import BaseModel, Field
from datetime import date
from typing import List, Optional

class TripRequest(BaseModel):
    destination: str = Field(..., example="Paris, France", description="The desired travel destination.")
    start_date: date = Field(..., example="2025-12-19", description="The start date of the trip.")
    end_date: date = Field(..., example="2025-12-26", description="The end date of the trip.")

class LiveFlightState(BaseModel):
    callsign: str
    origin_country: str
    longitude: Optional[float]
    latitude: Optional[float]
    on_ground: bool

class HotelOption(BaseModel):
    name: str
    price_per_night: float
    rating: float

class TripPlan(BaseModel):
    live_flights_nearby: List[LiveFlightState]
    hotels: List[HotelOption]
