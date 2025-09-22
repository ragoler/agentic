import asyncio

# This is a mock service that simulates calling a real hotel API.
# In a real application, this would use httpx to call an external service.

async def get_hotels_for_destination(destination: str):
    """
    Simulates fetching hotel data for a given destination.
    """
    print(f"Searching for hotels in {destination}...")
    
    # Simulate a network delay
    await asyncio.sleep(1) 
    
    # Return mock data based on the destination
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
        # Return a generic list for other destinations
        return [
            {"name": "City Center Hotel", "price_per_night": 160.0, "rating": 4.2},
            {"name": "The Grand Plaza", "price_per_night": 220.0, "rating": 4.6},
        ]
