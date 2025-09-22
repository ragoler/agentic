import pytest
from unittest.mock import patch, AsyncMock
from fastapi.testclient import TestClient
from app.main import app
from app.models.trip import TripPlan # Import TripPlan for type hinting

client = TestClient(app)

def test_health_check():
    """
    Tests the /health endpoint.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@pytest.mark.asyncio
@patch('app.api.v1.trip.orchestrator.plan_trip', new_callable=AsyncMock)
async def test_plan_trip_integration(mock_plan_trip):
    """
    Tests the /api/v1/plan endpoint by mocking the orchestrator.
    """
    # Setup a mock return value from the orchestrator
    mock_plan = TripPlan(
        summary="Orchestrated Summary",
        live_flights_nearby=[
            {"callsign": "ORCHESTRA1", "origin_country": "Orchestraland", "longitude": 1, "latitude": 1, "on_ground": False}
        ],
        hotels=[
            {"name": "Orchestra Hotel", "price_per_night": 150.0, "rating": 4.9}
        ]
    )
    mock_plan_trip.return_value = mock_plan

    payload = {
        "destination": "Orchestra City",
        "start_date": "2026-02-01",
        "end_date": "2026-02-08"
    }
    
    response = client.post("/api/v1/plan", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    
    # Verify that the data from the mocked orchestrator was returned
    assert data["summary"] == "Orchestrated Summary"
    assert data["live_flights_nearby"][0]["callsign"] == "ORCHESTRA1"
    assert data["hotels"][0]["name"] == "Orchestra Hotel"

    # Verify the orchestrator was called
    mock_plan_trip.assert_called_once()
