from pydantic import BaseModel, Field
from datetime import date

class TripRequest(BaseModel):
    destination: str = Field(..., example="Paris, France", description="The desired travel destination.")
    start_date: date = Field(..., example="2025-12-19", description="The start date of the trip.")
    end_date: date = Field(..., example="2025-12-26", description="The end date of the trip.")

class FlightOption(BaseModel):
    airline: str
    price: float
    departure_time: str

class HotelOption(BaseModel):
    name: str
    price_per_night: float
    rating: float

class TripPlan(BaseModel):
    flights: list[FlightOption]
    hotels: list[HotelOption]
