# Day 1 Local Platform Architecture

## Goal

Establish a local platform engineering environment that simulates cloud services, edge nodes, and observability for autonomous systems infrastructure.

## Components

### Fleet Manager

Responsible for registering and tracking edge nodes.

### Telemetry Service

Receives telemetry events from simulated autonomous edge devices.

### Mission Service

Creates and manages simulated mission assignments.

### Edge Agent

Represents a deployable node running on an edge device such as a Raspberry Pi, Jetson, or tactical computer.

### Prometheus

Scrapes metrics from platform services.

### Grafana

Provides dashboarding for platform metrics.

## Local Network

All services run on a shared Docker bridge network named `ares-net`.

## Why Docker Compose

Docker Compose is used for local development and simulation. It allows engineers to run a complete platform environment locally before introducing AWS, Terraform, ECS, or Kubernetes.

## Future Evolution

- Add persistent database models
- Add GitHub Actions CI/CD
- Add Terraform AWS infrastructure
- Add deployment artifacts
- Add offline edge telemetry buffering
- Add security scanning
- Add audit logging