---
title: Shared Resources
doc_section: architecture
nav_parent: architecture-index
nav_order: 8
---

# Shared Resources

## Resource Set first

Treat a shared resource as one Resource Set that provides one shared capability.

Examples:

- `user-db`
- `shared-cache`
- `shared-storage`
- `shared-ingress`

## Internal partitioning

A Resource Set can be split internally when needed:

- primary resource set
- binding or access set
- publication set

This split is optional. The goal is not maximal fragmentation but safe operation.

## Split signals

Consider splitting when:

- access-control churn is high
- consumer onboarding changes frequently
- publication migration needs to happen independently
- the primary resource should stay stable even while bindings change

## Ownership rule

Even when split, ownership should remain clear. Publication and binding design do not automatically change the lifecycle owner of the capability.

## Next

- [Service Dependencies](./07-service-dependencies.md)
