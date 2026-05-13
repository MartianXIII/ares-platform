#!/usr/bin/env bash
set -euo pipefail

echo "==> Building and starting platform"
docker compose up --build -d

echo "==> Waiting for services"
sleep 15

echo "==> Checking fleet-manager"
curl -fsS http://localhost:8001/health

echo
echo "==> Checking telemetry-service"
curl -fsS http://localhost:8002/health

echo
echo "==> Checking mission-service"
curl -fsS http://localhost:8003/health

echo
echo "==> Checking Prometheus"
curl -fsS http://localhost:9090/-/healthy

echo
echo "==> Docker smoke test passed"

docker compose down