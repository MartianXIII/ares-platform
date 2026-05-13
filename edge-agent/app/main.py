import logging
import os
import random
import time

import requests
from logging_config import configure_logging

configure_logging()
logger = logging.getLogger(__name__)

NODE_ID = os.getenv("EDGE_NODE_ID", "edge-node-alpha")
EDGE_SITE = os.getenv("EDGE_SITE", "AUSTIN-LAB")

FLEET_MANAGER_URL = os.getenv(
    "FLEET_MANAGER_URL",
    "http://fleet-manager:8000",
)

TELEMETRY_SERVICE_URL = os.getenv(
    "TELEMETRY_SERVICE_URL",
    "http://telemetry-service:8000",
)


def register_node() -> None:
    payload = {
        "node_id": NODE_ID,
        "site": EDGE_SITE,
        "platform": "docker-edge-sim",
        "capabilities": [
            "telemetry",
            "mission-receive",
            "offline-buffering-planned",
        ],
    }

    response = requests.post(
        f"{FLEET_MANAGER_URL}/nodes/register",
        json=payload,
        timeout=5,
    )
    response.raise_for_status()

    logger.info(
        "registered_with_fleet_manager",
        extra={"node_id": NODE_ID, "site": EDGE_SITE},
    )


def generate_telemetry() -> dict:
    return {
        "node_id": NODE_ID,
        "latitude": 30.2672 + random.uniform(-0.01, 0.01),
        "longitude": -97.7431 + random.uniform(-0.01, 0.01),
        "battery_percent": round(random.uniform(40, 100), 2),
        "status": random.choice(["nominal", "nominal", "nominal", "degraded"]),
    }


def send_telemetry() -> None:
    payload = generate_telemetry()

    response = requests.post(
        f"{TELEMETRY_SERVICE_URL}/telemetry",
        json=payload,
        timeout=5,
    )
    response.raise_for_status()

    logger.info(
        "telemetry_sent",
        extra={
            "node_id": NODE_ID,
            "battery_percent": payload["battery_percent"],
            "status": payload["status"],
        },
    )


def main() -> None:
    while True:
        try:
            register_node()
            break
        except Exception as exc:
            logger.warning(
                "fleet_registration_failed_retrying",
                extra={"error": str(exc)},
            )
            time.sleep(5)

    while True:
        try:
            send_telemetry()
        except Exception as exc:
            logger.error(
                "telemetry_send_failed",
                extra={"error": str(exc)},
            )

        time.sleep(10)


if __name__ == "__main__":
    main()