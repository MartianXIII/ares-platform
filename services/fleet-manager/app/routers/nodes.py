import logging
from datetime import UTC, datetime

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.metrics import active_nodes, registered_nodes_total

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/nodes", tags=["nodes"])


class EdgeNodeRegistration(BaseModel):
    node_id: str = Field(..., examples=["edge-node-alpha"])
    site: str = Field(..., examples=["AUSTIN-LAB"])
    platform: str = Field(..., examples=["raspberry-pi-sim"])
    capabilities: list[str] = Field(default_factory=list)


class EdgeNodeRecord(EdgeNodeRegistration):
    registered_at: str
    status: str = "online"


NODES: dict[str, EdgeNodeRecord] = {}


@router.post("/register", response_model=EdgeNodeRecord)
def register_node(payload: EdgeNodeRegistration) -> EdgeNodeRecord:
    record = EdgeNodeRecord(
        **payload.model_dump(),
        registered_at=datetime.now(UTC).isoformat(),
        status="online",
    )

    is_new_node = payload.node_id not in NODES
    NODES[payload.node_id] = record

    if is_new_node:
        registered_nodes_total.inc()

    active_nodes.set(len(NODES))

    logger.info(
        "edge_node_registered",
        extra={
            "node_id": payload.node_id,
            "site": payload.site,
            "platform": payload.platform,
        },
    )

    return record


@router.get("", response_model=list[EdgeNodeRecord])
def list_nodes() -> list[EdgeNodeRecord]:
    return list(NODES.values())


@router.get("/{node_id}", response_model=EdgeNodeRecord)
def get_node(node_id: str) -> EdgeNodeRecord:
    return NODES[node_id]