from prometheus_client import Counter, Gauge

telemetry_messages_total = Counter(
    "telemetry_messages_total",
    "Total number of telemetry messages received",
)

last_reported_battery = Gauge(
    "telemetry_last_reported_battery_percent",
    "Last reported battery percentage by edge node",
    ["node_id"],
)