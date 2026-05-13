from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_create_mission_returns_mission_record():
    payload = {
        "name": "perimeter-survey",
        "assigned_node_id": "edge-node-test",
        "objective": "Survey the simulated perimeter.",
    }

    response = client.post("/missions", json=payload)

    assert response.status_code == 200

    body = response.json()
    assert body["name"] == "perimeter-survey"
    assert body["assigned_node_id"] == "edge-node-test"
    assert body["status"] == "created"
    assert "mission_id" in body
    assert "created_at" in body


def test_start_mission_sets_status_active():
    payload = {
        "name": "start-test",
        "assigned_node_id": "edge-node-test",
        "objective": "Validate mission start transition.",
    }

    create_response = client.post("/missions", json=payload)
    mission_id = create_response.json()["mission_id"]

    start_response = client.post(f"/missions/{mission_id}/start")

    assert start_response.status_code == 200
    assert start_response.json()["status"] == "active"