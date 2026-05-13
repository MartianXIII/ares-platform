from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_register_node_returns_node_record():
    payload = {
        "node_id": "edge-node-test",
        "site": "TEST-LAB",
        "platform": "docker-edge-sim",
        "capabilities": ["telemetry", "mission-receive"],
    }

    response = client.post("/nodes/register", json=payload)

    assert response.status_code == 200

    body = response.json()
    assert body["node_id"] == "edge-node-test"
    assert body["site"] == "TEST-LAB"
    assert body["platform"] == "docker-edge-sim"
    assert body["status"] == "online"
    assert "registered_at" in body


def test_list_nodes_includes_registered_node():
    payload = {
        "node_id": "edge-node-list-test",
        "site": "TEST-LAB",
        "platform": "docker-edge-sim",
        "capabilities": ["telemetry"],
    }

    client.post("/nodes/register", json=payload)

    response = client.get("/nodes")

    assert response.status_code == 200
    node_ids = [node["node_id"] for node in response.json()]
    assert "edge-node-list-test" in node_ids