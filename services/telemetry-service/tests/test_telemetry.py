from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_ingest_telemetry_accepts_valid_payload():
    payload = {
        "node_id": "edge-node-test",
        "latitude": 30.2672,
        "longitude": -97.7431,
        "battery_percent": 87.5,
        "status": "nominal",
    }

    response = client.post("/telemetry", json=payload)

    assert response.status_code == 200

    body = response.json()
    assert body["accepted"] is True
    assert body["node_id"] == "edge-node-test"
    assert "timestamp" in body


def test_get_node_telemetry_returns_events():
    payload = {
        "node_id": "edge-node-history-test",
        "latitude": 30.2672,
        "longitude": -97.7431,
        "battery_percent": 75.0,
        "status": "nominal",
    }

    client.post("/telemetry", json=payload)

    response = client.get("/telemetry/edge-node-history-test")

    assert response.status_code == 200
    assert len(response.json()) >= 1
    assert response.json()[-1]["node_id"] == "edge-node-history-test"