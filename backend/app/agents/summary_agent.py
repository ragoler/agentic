import google.generativeai as genai
from app.core.config import settings
from app.models.trip import LiveFlightState, HotelOption
from typing import List

class SummaryAgent:
    """
    An agent that uses the Gemini LLM to generate trip summaries.
    """
    def __init__(self):
        if settings.GEMINI_API_KEY == "YOUR_API_KEY_HERE":
            print("Warning: GEMINI_API_KEY is not set. SummaryAgent will return a mock summary.")
            self.model = None
        else:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-pro')

    async def generate_summary(self, destination: str, flights: List[LiveFlightState], hotels: List[HotelOption]) -> str:
        """
        Generates a natural language summary of the trip plan.
        """
        if not self.model:
            return "This is a mock summary because the Gemini API key is not configured."

        prompt = self._create_prompt(destination, flights, hotels)
        
        try:
            response = await self.model.generate_content_async(prompt)
            return response.text
        except Exception as e:
            print(f"Error generating summary with Gemini: {e}")
            return "There was an error generating the trip summary."

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

