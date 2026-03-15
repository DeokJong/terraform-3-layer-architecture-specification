---
title: Architecture
description: English overview of the 3-layer Terraform architecture section.
hero_kicker: Section Overview
doc_section: architecture
nav_key: architecture-index
nav_title: Overview
nav_order: 1
---

# Architecture

This section explains how the 3-layer Terraform model is structured and how the detailed chapter set should be read.

## What this section covers

- Layer responsibilities and dependency direction
- Contract boundaries and ownership rules
- Workspace split criteria
- Shared resource and operational safety considerations

## Canonical English source

Use the root specification for the full English architecture text:

- [Terraform 3-Layer Architecture Specification](../../terraform-3-layer-architecture-specification.md)

## Suggested order

1. [Overview](./01-overview.md)
2. [Layers](./02-layers.md)
3. [Contracts](./03-contracts.md)
4. [Ownership and References](./04-ownership-and-references.md)
5. [Workspace Model](./05-workspace-model.md)
6. [Shared Resources](./06-shared-resources.md)
7. [Service Dependencies](./07-service-dependencies.md)
8. [Operations](./08-operations.md)
9. [Safety and Resilience](./09-safety-and-resilience.md)
10. [Decision Checklist](./10-decision-checklist.md)
11. [Reference Terms](./01a-glossary-and-views.md)
12. [Shared Resource Design Template](./11-shared-resource-design-template.md)
13. [Migration and Rollout Scenarios](./12-migration-and-rollout-scenarios.md)

## How to read it

- For a first read, start with [Overview](./01-overview.md), then continue directly to [Layers](./02-layers.md) and [Contracts](./03-contracts.md).
- If the goal is boundary design, continue with [Ownership and References](./04-ownership-and-references.md) and [Workspace Model](./05-workspace-model.md).
- If the goal is shared capability design, read [Shared Resources](./06-shared-resources.md), [Service Dependencies](./07-service-dependencies.md), and the [Shared Resource Design Template](./11-shared-resource-design-template.md) together.
- If the goal is operational safety, prioritize [Operations](./08-operations.md), [Safety and Resilience](./09-safety-and-resilience.md), and the [Decision Checklist](./10-decision-checklist.md).
- [Reference Terms](./01a-glossary-and-views.md) is intentionally a lookup page, not the main narrative start.

## Related sections

- [Conventions](../conventions/)
- [ADR](../adr/)
