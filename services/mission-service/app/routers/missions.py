import logging
from datetime import UTC, datetime
from uuid import uuid4

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.metrics import active_missions, missions_created_total

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/missions", tags=["missions"])


class MissionCreate(BaseModel):
    name: str = Field(..., examples=["perimeter-survey"])
    assigned_node_id: str = Field(..., examples=["edge-node-alpha"])
    objective: str = Field(..., examples=["Survey perimeter and report telemetry."])


class MissionRecord(MissionCreate):
    mission_id: str
    status: str = "created"
    created_at: str


MISSIONS: dict[str, MissionRecord] = {}


@router.post("", response_model=MissionRecord)
def create_mission(payload: MissionCreate) -> MissionRecord:
    mission = MissionRecord(
        **payload.model_dump(),
        mission_id=str(uuid4()),
        status="created",
        created_at=datetime.now(UTC).isoformat(),
    )

    MISSIONS[mission.mission_id] = mission
    missions_created_total.inc()
    active_missions.set(len(MISSIONS))

    logger.info(
        "mission_created",
        extra={
            "mission_id": mission.mission_id,
            "assigned_node_id": mission.assigned_node_id,
            "objective": mission.objective,
        },
    )

    return mission


@router.get("", response_model=list[MissionRecord])
def list_missions() -> list[MissionRecord]:
    return list(MISSIONS.values())


@router.post("/{mission_id}/start")
def start_mission(mission_id: str) -> MissionRecord:
    mission = MISSIONS[mission_id]
    mission.status = "active"

    logger.info(
        "mission_started",
        extra={
            "mission_id": mission_id,
            "assigned_node_id": mission.assigned_node_id,
        },
    )

    return mission