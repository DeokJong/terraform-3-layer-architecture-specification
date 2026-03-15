---
title: Ownership and References
doc_section: architecture
nav_parent: architecture-index
nav_order: 6
---

# Ownership and References

## Ownership rules

Resource ownership is decided by lifecycle and operational responsibility, not by where code happens to be placed.

An owner is responsible for:

- creation
- change management
- deletion
- interface stability
- migration and rollback planning

## What ownership is not based on

Do not decide ownership based on:

- who currently reads the value
- where the value is stored
- which publication mechanism is used
- which Workspace happens to contain the code today

## Reference rules

Allowed references:

- consumer reads provider-owned Contract
- service consumes stable API hostname from another service
- service consumes published database endpoint or parameter path

Disallowed references:

- direct consumption of another layer's Implementation Value
- direct use of physical ALB DNS or internal endpoint when a stable Contract exists
- broad bi-directional dependencies between services

## Working rule

If a value needs to be shared repeatedly, document it as a Contract with a provider, consumer class, publication method, and source of truth.

## Next

- [Workspace Model](./05-workspace-model.md)
