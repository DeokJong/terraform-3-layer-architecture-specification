---
title: Migration and Rollout Scenarios
doc_section: architecture
nav_parent: architecture-index
nav_order: 14
---

# Migration and Rollout Scenarios

## Contract migration

1. Identify the current active Contract.
2. Define and publish the new Contract in parallel.
3. Identify consumers and migration order.
4. Run both Contracts during migration.
5. Move the old Contract to `Deprecated` after migration.
6. Remove it only after all consumers have switched.

## Shared resource split

1. Start from one Resource Set.
2. Measure change churn and blast radius.
3. Split `binding` or `publication` only when risk or ownership differs.
4. Keep ownership explicit after the split.

## Legacy rollout

1. Reinterpret legacy assets with the new ownership rules.
2. Avoid forced renames unless they create operational value.
3. Prefer parallel publication over immediate cutover.
4. Move consumers gradually.

## Rollback expectation

Rollback should be possible without deleting the provider's ability to continue publishing the old Contract. If rollback is impossible, the rollout plan is too aggressive.
