# Shared Resource Design Template

새 shared resource를 설계할 때 사용하는 표준 템플릿입니다.

## Basic Record

| Field | Description |
| --- | --- |
| Resource Name | Example: shared orders DB |
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
| How often does access change | Monthly / weekly / frequent |
| Is publication separate from core | Yes or no with reason |

## Core / Access / Publication Plan

| Area | Included Resources | Owner | Change Frequency | Split Decision |
| --- | --- | --- | --- | --- |
| Core | Primary resource body | provider | low | split if blast radius is large |
| Access | allowlist, bindings, grants | provider or access owner | medium or high | split if churn is high |
| Publication | DNS, SSM, output | provider | low or medium | split if migration is likely |

## Contract Record

| Contract Name | Type | Consumer | Publication | Source of Truth | Stability |
| --- | --- | --- | --- | --- | --- |
| `db-main.internal.example.com` | Connectivity | backend services | Route53 | platform-db-core | stable |
| `/platform/orders/db/host` | Runtime | app runtime | SSM | platform-db-contract | stable |

## Review Questions

- Does this shared resource really have a shared lifecycle
- Can core stability survive consumer growth
- Will access churn force repeated core applies
- Can contract migration run in parallel without breaking consumers

## Next

- [Migration and Rollout Scenarios](./12-migration-and-rollout-scenarios.md)
