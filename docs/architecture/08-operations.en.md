---
title: Operations
doc_section: architecture
nav_parent: architecture-index
nav_order: 10
---

# Operations

## Change propagation

If an upper-layer change can affect lower layers, plan and apply changes in a controlled sequence.

Principles:

- implementation changes should avoid forcing Contract changes
- breaking Contract changes require parallel publication and migration
- operational sequencing should be documented before apply

## Recommended order

1. Change provider implementation safely.
2. Publish any new Contract in parallel if needed.
3. Migrate consumers in a controlled order.
4. Observe and validate.
5. Deprecate and remove the old Contract only after migration.

## Operational goal

The provider should be able to evolve internal implementation while minimizing forced consumer coordination.

## Next

- [Safety and Resilience](./09-safety-and-resilience.md)
