# 1.0 Roadmap

This document outlines the roadmap for version 1.0.

## Milestones

The project will be updated in 1 week milestones.

| Duration | Activity | Release |
| --- | --- | --- |
| 1 week | <li>SQLAlchemy</li><li>Pydantic</li><li>Docker</li> <li>Logging</li><li>Celery</li><li>Tests</li><li>Config</li>| v0.0.1 |

## Timeline

| Milestone End Date | Milestone Name |
| --- | --- |
| 12-12-2022 | Stage 1 |

## Prioritization

The following priority order is used:

- P0 = Serious issue to be dealt with ASAP.
- P1 = Normail priority issue to be dealt with according to schedule.
- P2 = Unimportant issue can be delayed.

## 1.0 Scenarios

Key deliverables for 1.0 release.

| Priority | Scenario | Description | State |
| --- | --- | --- | --- |
| P0 | Initial Framework | Initial Framework Skeleton.<br><br>Issues: #0<br> Commit: #29a303e | Done |
| P1 | Formatting & Structure | Implement correct production ready structure and formating. PEP-8 Compliance, Code documenation and Linting.<br><br>Issues: #0<br> Commit: #178c0c0 | Done |
| P1 | async, schemas, models, db, linting, env, worker, CI/CD, config | Provide async, schema, and model examples. Implement worker, env, db CI/CD, and config templates.<br><br>Issues: #0<br> Commit: #665038d | Done |
| P1 | CORS, Repo Cleanup | Provide CORS middleware.<br><br>Issues: #0<br> Commit: #8c8d603<br> PR: [#4] | Done |
| P2 | Worker Scaling | Implement celery worker scaling through docker.<br><br>Issues: #0 | On Hold |
