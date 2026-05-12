.PHONY: up down build logs ps health clean

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

clean:
	docker compose down -v --remove-orphans