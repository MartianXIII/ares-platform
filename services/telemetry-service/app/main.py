from fastapi import FastAPI, Response
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

from app.logging_config import configure_logging
from app.routers import telemetry

configure_logging()

app = FastAPI(
    title="ARES Telemetry Service",
    version="0.1.0",
    description="Receives telemetry from simulated edge devices.",
)

app.include_router(telemetry.router)


@app.get("/health")
def health() -> dict:
    return {
        "service": "telemetry-service",
        "status": "healthy",
    }


@app.get("/metrics")
def metrics() -> Response:
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)