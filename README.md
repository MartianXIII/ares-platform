# ARES Platform

ARES Platform is a miniature autonomous systems deployment platform designed to demonstrate senior platform engineering skills across cloud, on-prem, and edge environments.

## Purpose

This project simulates infrastructure patterns used for autonomous vehicle orchestration:

- Containerized microservices
- Edge device agents
- Fleet registration
- Telemetry ingestion
- Mission orchestration
- Local observability
- Deployment automation foundations
- Future AWS/Terraform/CI/CD integration

## Why This Exists

The goal is to move beyond theoretical DevOps talking points and demonstrate production-style platform engineering decisions in working code.

## Core Components

| Component | Purpose |
|---|---|
| Fleet Manager | Tracks edge nodes and fleet registration |
| Telemetry Service | Receives telemetry from simulated edge devices |
| Mission Service | Creates and manages simulated missions |
| Edge Agent | Simulates an autonomous vehicle edge node |
| PostgreSQL | Persistent platform data |
| Redis | Lightweight coordination/cache layer |
| Prometheus | Metrics scraping |
| Grafana | Dashboarding |

## Local Startup

```bash
make up


## Local Shutdown
```bash
make down



