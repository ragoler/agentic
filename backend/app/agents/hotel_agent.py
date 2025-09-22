import asyncio

class HotelAgent:
    """
    An agent specialized in finding hotel information.
    This is a mock agent that simulates calling a real hotel API.
    """
    async def search(self, destination: str):
        """
        Simulates fetching hotel data for a given destination.
        """
        print(f"HotelAgent searching for hotels in {destination}...")
        
        # Simulate a network delay
        await asyncio.sleep(1) 
        
        destination_lower = destination.lower()
        
        if "paris" in destination_lower:
            return [
                {"name": "Hotel Le Grand", "price_per_night": 250.0, "rating": 4.7},
                {"name": "Chic Parisian Flat", "price_per_night": 180.0, "rating": 4.9},
            ]
        elif "tokyo" in destination_lower:
            return [
                {"name": "Park Hyatt Tokyo", "price_per_night": 450.0, "rating": 4.9},
                {"name": "Shinjuku Gyoen Hotel", "price_per_night": 120.0, "rating": 4.4},
            ]
        else:
            return [
                {"name": "City Center Hotel", "price_per_night": 160.0, "rating": 4.2},
                {"name": "The Grand Plaza", "price_per_night": 220.0, "rating": 4.6},
            ]
