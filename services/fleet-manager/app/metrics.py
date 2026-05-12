from prometheus_client import Counter, Gauge

registered_nodes_total = Counter(
    "fleet_registered_nodes_total",
    "Total number of edge nodes registered with the fleet manager",
)

active_nodes = Gauge(
    "fleet_active_nodes",
    "Current number of active edge nodes known to the fleet manager",
)