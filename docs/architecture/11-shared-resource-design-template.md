---
title: 공유 리소스 설계 템플릿
doc_section: architecture
nav_parent: architecture-index
nav_order: 13
---

# Shared Resource Design Template

새 shared resource를 설계할 때 사용하는 표준 템플릿입니다.

## Basic Record

| Field | Description |
| --- | --- |
| Resource Name | Example: `user-db` |
| Resource Type | DB / Cache / Bucket / KMS / Ingress |
| Layer | Foundation / Platform / Service |
| Owner | Lifecycle owner |
| Primary Consumer | Main consumer or consumer class |
| Criticality | low / medium / high |

## Design Decisions

| Question | Example Answer |
| --- | --- |
| Why is this shared | Multiple services consume it |
| Why does it belong to this layer | It is not tied to a single service lifecycle |
| What is hidden as implementation | Physical endpoint or internal IDs |
| What is published as contract | Stable DNS, SSM path, standard output |
| How often does binding change | Monthly / weekly / frequent |
| Is publication separate from the primary resource set | Yes or no with reason |

## Resource Set Partition Plan

| Partition | Included Resources | Owner | Change Frequency | Split Decision |
| --- | --- | --- | --- | --- |
| Primary Set | Primary resource body and closely coupled configuration | provider | low | keep together if lifecycle is aligned |
| Binding Set | allowlist, bindings, grants, policy attachments | provider or access owner | medium or high | split if churn is high |
| Publication Set | DNS, SSM, output publication | provider | low or medium | split if migration is likely |

## Contract Record

| Contract Name | Type | Consumer | Publication | Source of Truth | Stability |
| --- | --- | --- | --- | --- | --- |
| `db-main.internal.example.com` | Connectivity | backend services | Route53 | `user-db` | stable |
| `/backends/prod/db/primary` | Runtime | app runtime | SSM | `user-db-publication` | stable |

## Review Questions

- Does this shared resource really have a shared lifecycle
- Can the primary resource set stay stable as consumer count grows
- Will binding churn force repeated primary resource applies
- Can contract migration run in parallel without breaking consumers

## Next

- [Migration and Rollout Scenarios](./12-migration-and-rollout-scenarios.md)

