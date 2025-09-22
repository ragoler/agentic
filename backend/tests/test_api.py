import pytest
from unittest.mock import patch, AsyncMock
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    """
    Tests the /health endpoint.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@pytest.mark.asyncio
@patch('app.api.v1.trip.get_hotels_for_destination', new_callable=AsyncMock)
@patch('app.api.v1.trip.get_flights_for_destination', new_callable=AsyncMock)
async def test_plan_trip_integration(mock_get_flights, mock_get_hotels):
    """
    Tests the /api/v1/plan endpoint, mocking the service layer.
    """
    # Setup mock return values for the services
    mock_get_flights.return_value = [
        {"callsign": "TEST1", "origin_country": "Testland", "longitude": 0, "latitude": 0, "on_ground": False}
    ]
    mock_get_hotels.return_value = [
        {"name": "Test Hotel", "price_per_night": 100.0, "rating": 5.0}
    ]

    payload = {
        "destination": "Tokyo, Japan",
        "start_date": "2026-01-15",
        "end_date": "2026-01-22"
    }
    
    # Use the TestClient to make the request
    response = client.post("/api/v1/plan", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    
    # Verify that our mock data was returned
    assert "live_flights_nearby" in data
    assert "hotels" in data
    assert len(data["live_flights_nearby"]) == 1
    assert data["live_flights_nearby"][0]["callsign"] == "TEST1"
    assert len(data["hotels"]) == 1
    assert data["hotels"][0]["name"] == "Test Hotel"

    # Verify that the services were called with the correct destination
    mock_get_flights.assert_called_once_with("Tokyo, Japan")
    mock_get_hotels.assert_called_once_with("Tokyo, Japan")
