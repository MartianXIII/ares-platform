from fastapi import FastAPI, Response
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

from app.logging_config import configure_logging
from app.routers import missions

configure_logging()

app = FastAPI(
    title="ARES Mission Service",
    version="0.1.0",
    description="Creates and manages simulated autonomous missions.",
)

app.include_router(missions.router)


@app.get("/health")
def health() -> dict:
    return {
        "service": "mission-service",
        "status": "healthy",
    }


@app.get("/metrics")
def metrics() -> Response:
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)