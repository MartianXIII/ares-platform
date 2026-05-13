#!/usr/bin/env bash
set -euo pipefail

echo "==> Running Ruff lint"
ruff check services edge-agent

echo "==> Running Ruff format check"
ruff format --check services edge-agent

echo "==> Running Bandit security scan"
bandit -r services edge-agent

echo "==> Running fleet-manager tests"
PYTHONPATH=services/fleet-manager pytest services/fleet-manager/tests

echo "==> Running telemetry-service tests"
PYTHONPATH=services/telemetry-service pytest services/telemetry-service/tests

echo "==> Running mission-service tests"
PYTHONPATH=services/mission-service pytest services/mission-service/tests

echo "==> Local CI completed successfully"