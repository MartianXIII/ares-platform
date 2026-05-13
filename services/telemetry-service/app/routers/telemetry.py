import logging
from datetime import UTC, datetime

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.metrics import last_reported_battery, telemetry_messages_total

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/telemetry", tags=["telemetry"])


class TelemetryEvent(BaseModel):
    node_id: str = Field(..., examples=["edge-node-alpha"])
    latitude: float = Field(..., examples=[30.2672])
    longitude: float = Field(..., examples=[-97.7431])
    battery_percent: float = Field(..., ge=0, le=100, examples=[87.5])
    status: str = Field(..., examples=["nominal"])
    timestamp: str | None = None


TELEMETRY_EVENTS: dict[str, list[TelemetryEvent]] = {}


@router.post("")
def ingest_telemetry(payload: TelemetryEvent) -> dict:
    if payload.timestamp is None:
        payload.timestamp = datetime.now(UTC).isoformat()

    TELEMETRY_EVENTS.setdefault(payload.node_id, []).append(payload)

    telemetry_messages_total.inc()
    last_reported_battery.labels(node_id=payload.node_id).set(payload.battery_percent)

    logger.info(
        "telemetry_received",
        extra={
            "node_id": payload.node_id,
            "battery_percent": payload.battery_percent,
            "status": payload.status,
        },
    )

    return {
        "accepted": True,
        "node_id": payload.node_id,
        "timestamp": payload.timestamp,
    }


@router.get("/{node_id}")
def get_node_telemetry(node_id: str) -> list[TelemetryEvent]:
    return TELEMETRY_EVENTS.get(node_id, [])