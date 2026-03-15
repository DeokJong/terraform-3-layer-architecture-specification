---
title: Decision Checklist
doc_section: architecture
nav_parent: architecture-index
nav_order: 12
---

# Decision Checklist

When adding a new resource or Contract, decide in this order:

1. Which lifecycle does it move with?
2. Does it belong to `Foundation`, `Platform`, or `Service`?
3. Which shared capability or Resource Set does it belong to?
4. Is it an Implementation Value or a Contract Value?
5. If it is a Contract, who is the provider?
6. Does churn or blast radius require a Workspace split?

## Quick interpretation

- stable shared capability used by many services: likely `Platform`
- value tied to one service deployment: likely `Service`
- environment-wide base primitive: likely `Foundation`
- consumer-facing stable publication: likely Contract
- physical endpoint or internal ID: likely Implementation Value

## Related pages

- [Safety and Resilience](./09-safety-and-resilience.md)
- [Conventions Overview](../conventions/)
- [ADR-0001](../adr/adr-0001-3layer-architecture-contract-workspace.md)
