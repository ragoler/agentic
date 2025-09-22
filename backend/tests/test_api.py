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

def test_plan_trip_mock():
    """
    Tests the /api/v1/plan endpoint with mock data.
    """
    payload = {
        "destination": "Tokyo, Japan",
        "start_date": "2026-01-15",
        "end_date": "2026-01-22"
    }
    response = client.post("/api/v1/plan", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "flights" in data
    assert "hotels" in data
    assert len(data["flights"]) > 0
    assert len(data["hotels"]) > 0
    assert data["flights"][0]["airline"] == "Airline A"
    assert data["hotels"][0]["name"] == "Hotel X"
