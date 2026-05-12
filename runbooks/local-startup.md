# Local Startup Runbook

## Purpose

This runbook explains how to start the ARES Platform local development environment.

## Prerequisites

- Docker Desktop
- Docker Compose
- Make
- curl
- jq

## Start Platform

```bash
make up
```


## Validate API's Manually
Register
```bash
curl -X POST http://localhost:8001/nodes/register \
  -H "Content-Type: application/json" \
  -d '{
    "node_id": "manual-node-1",
    "site": "LOCAL-LAB",
    "platform": "macbook-sim",
    "capabilities": ["telemetry", "mission-receive"]
  }' | jq .
```

List 
```bash
curl -s http://localhost:8001/nodes | jq .
```

Send telemetry:
```bash
curl -X POST http://localhost:8002/telemetry \
  -H "Content-Type: application/json" \
  -d '{
    "node_id": "manual-node-1",
    "latitude": 30.2672,
    "longitude": -97.7431,
    "battery_percent": 91.4,
    "status": "nominal"
  }' | jq .
```

Create a mission:
```bash
curl -X POST http://localhost:8003/missions \
  -H "Content-Type: application/json" \
  -d '{
    "name": "perimeter-survey",
    "assigned_node_id": "manual-node-1",
    "objective": "Survey perimeter and report telemetry."
  }' | jq .
```

Prometheus:
```html
http://localhost:9090
```