import httpx
import google.generativeai as genai
from fastapi import HTTPException
from app.core.config import settings
from typing import List, Dict, Any

class MCPGateway:
    """
    Managed Connectivity Platform Gateway.
    A single, centralized component to manage all external API communications.
    """
    def __init__(self):
        self.opensky_api_url = "https://opensky-network.org/api/states/all"
        
        if settings.GEMINI_API_KEY == "YOUR_API_KEY_HERE":
            print("Warning: GEMINI_API_KEY is not set. MCPGateway will return mock summaries.")
            self.gemini_model = None
        else:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            self.gemini_model = genai.GenerativeModel('gemini-1.5-flash')

    async def get_live_flights(self, lat: float, lon: float) -> List[Dict[str, Any]]:
        """
        Connects to the OpenSky Network to get live flight data.
        """
        params = {"lamin": lat - 2.0, "lamax": lat + 2.0, "lomin": lon - 2.0, "lomax": lon + 2.0}
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(self.opensky_api_url, params=params, timeout=10.0)
                response.raise_for_status()
                return response.json()
            except httpx.RequestError as exc:
                raise HTTPException(status_code=503, detail=f"MCP Error: Could not connect to flight API. Details: {exc}")
            except httpx.HTTPStatusError as exc:
                raise HTTPException(status_code=exc.response.status_code, detail="MCP Error: Received error from flight API.")

    async def generate_text_summary(self, prompt: str) -> str:
        """
        Connects to the Google Gemini API to generate a text summary.
        """
        if not self.gemini_model:
            return "This is a mock summary because the Gemini API key is not configured."
        
        try:
            response = await self.gemini_model.generate_content_async(prompt)
            return response.text
        except Exception as e:
            print(f"MCP Error generating summary with Gemini: {e}")
            return "There was an error generating the trip summary via the MCP."
