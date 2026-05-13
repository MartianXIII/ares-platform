# Branching Strategy

## Goal

ARES Platform uses a lightweight trunk-based workflow suitable for rapid platform iteration while maintaining CI/CD safety gates.

## Branches

| Branch | Purpose |
|---|---|
| main | Production-ready branch |
| develop | Integration branch for active work |
| feature/* | Short-lived feature branches |

## Pull Request Rules

All changes should go through pull requests.

Required checks:

- Ruff lint
- Ruff format check
- Unit tests
- Docker Compose smoke test
- Bandit security scan
- Trivy filesystem scan
- Docker image build

## Release Tags

Release tags follow semantic versioning:

```text
v0.1.0
v0.2.0
v1.0.0