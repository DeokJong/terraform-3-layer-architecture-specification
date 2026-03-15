---
title: Shared Resource Design Template
doc_section: architecture
nav_parent: architecture-index
nav_order: 13
---

# Shared Resource Design Template

Use this template when introducing a new shared capability.

## Basic record

| Field | Description |
| --- | --- |
| Resource Name | Example: `user-db` |
| Resource Type | DB / Cache / Bucket / KMS / Ingress |
| Layer | Foundation / Platform / Service |
| Owner | Lifecycle owner |
| Primary Consumer | Main consumer or consumer class |
| Criticality | low / medium / high |

## Design decisions

| Question | Example answer |
| --- | --- |
| Why is this shared | Multiple services consume it |
| Why does it belong to this layer | It is not tied to a single service lifecycle |
| What stays hidden as implementation | Physical endpoint or internal IDs |
| What is published as Contract | Stable DNS, SSM path, standard output |
| How often does binding change | monthly / weekly / frequent |
| Is publication separate from the primary resource set | yes or no, with reason |

## Resource Set partition plan

| Partition | Included resources | Owner | Change frequency | Split decision |
| --- | --- | --- | --- | --- |
| Primary Set | Primary resource body and tightly coupled configuration | provider | low | keep together if lifecycle is aligned |
| Binding Set | allowlists, bindings, grants, policy attachments | provider or access owner | medium or high | split if churn is high |
| Publication Set | DNS, SSM, or output publication | provider | low or medium | split if migration is likely |

## Contract record

| Contract Name | Type | Consumer | Publication | Source of Truth | Stability |
| --- | --- | --- | --- | --- | --- |
| `db-main.internal.example.com` | Connectivity | backend services | Route53 | `user-db` | stable |
| `/backends/prod/db/primary` | Runtime config | app runtime | SSM | `user-db-publication` | stable |

## Review questions

- Does this capability really have a shared lifecycle?
- Can the primary resource set remain stable as consumer count grows?
- Will binding churn force repeated applies on the primary resource?
- Can Contract migration happen in parallel without breaking consumers?

## Next

- [Migration and Rollout Scenarios](./12-migration-and-rollout-scenarios.md)
