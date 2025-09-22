import pytest
from unittest.mock import patch, AsyncMock

from app.services.flight_service import get_flights_for_destination
from app.services.hotel_service import get_hotels_for_destination

# Mark all tests in this file as async
pytestmark = pytest.mark.asyncio

async def test_hotel_service_mock():
    """
    Tests the mock hotel service to ensure it returns expected data.
    """
    # Test a known destination
    hotels = await get_hotels_for_destination("Paris, France")
    assert len(hotels) == 2
    assert hotels[0]["name"] == "Hotel Le Grand"

    # Test an unknown destination
    hotels = await get_hotels_for_destination("Unknown City")
    assert len(hotels) == 2
    assert hotels[0]["name"] == "City Center Hotel"

@patch('httpx.AsyncClient.get', new_callable=AsyncMock)
async def test_flight_service_success(mock_get):
    """
    Tests the flight service with a successful, mocked API call.
    """
    # Sample data from the OpenSky Network API
    mock_api_response = {
        "time": 1715377200,
        "states": [
            ["a8a8a8", "KLM123  ", "Netherlands", 1715377200, 1715377200, 4.88, 52.3, 7600, False, 250, 0, 0, None, 7800, None, False, 0]
        ]
    }
    mock_get.return_value.json.return_value = mock_api_response
    mock_get.return_value.raise_for_status = lambda: None

    flights = await get_flights_for_destination("Paris, France")
    
    assert len(flights) == 1
    assert flights[0]["callsign"] == "KLM123"
    assert flights[0]["origin_country"] == "Netherlands"

async def test_flight_service_unknown_destination():
    """
    Tests the flight service with a destination not in our geocode mock.
    """
    flights = await get_flights_for_destination("Unknown City")
    assert len(flights) == 0
