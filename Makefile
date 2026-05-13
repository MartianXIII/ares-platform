.PHONY: up down build logs ps health clean lint format test security ci smoke

up:
	docker compose up --build

down:
	docker compose down

build:
	docker compose build

logs:
	docker compose logs -f

ps:
	docker compose ps

health:
	curl -s http://localhost:8001/health | jq .
	curl -s http://localhost:8002/health | jq .
	curl -s http://localhost:8003/health | jq .

lint:
	ruff check services edge-agent

format:
	ruff format services edge-agent

test:
	PYTHONPATH=services/fleet-manager pytest services/fleet-manager/tests
	PYTHONPATH=services/telemetry-service pytest services/telemetry-service/tests
	PYTHONPATH=services/mission-service pytest services/mission-service/tests

security:
	bandit -r services edge-agent

ci:
	./scripts/ci-local.sh

smoke:
	./scripts/docker-smoke-test.sh

clean:
	docker compose down -v --remove-orphans