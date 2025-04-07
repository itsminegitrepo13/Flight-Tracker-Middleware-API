from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_flight():
    response = client.get("/flight", params={
        "airline_code": "AA",
        "flight_number": "100",
        "departure_date": "2025-04-01T00:00:00"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["airline_code"] == "AA"
    assert "status" in data
