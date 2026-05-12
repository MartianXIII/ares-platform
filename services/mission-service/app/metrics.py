from prometheus_client import Counter, Gauge

missions_created_total = Counter(
    "missions_created_total",
    "Total number of missions created",
)

active_missions = Gauge(
    "missions_active",
    "Current number of active missions",
)