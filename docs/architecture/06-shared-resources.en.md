---
title: Shared Resources
doc_section: architecture
nav_parent: architecture-index
nav_order: 8
---

# Shared Resources

This chapter explains how to identify one shared capability as a coherent resource set. The goal is not to split mechanically by role label, but to first define the capability boundary that consumers actually depend on.

## Questions this chapter answers

- Which resources should be described as one Shared Resource?
- Why is a capability boundary different from a Workspace boundary?
- When is the `core / access / publication` pattern useful, and when is it excessive?
- What must the owner of a shared capability actually guarantee?

## Difference from the Workspace model

The primary subject of this chapter is the Resource Set. It defines what one shared capability actually is before deciding how to operate it.

For example:

- `user-db` is a Shared Resource name.
- `user-db-publication` is an optional Workspace name used to operate that Shared Resource.

So the Shared Resource comes first, and Workspace splitting is a later operating decision.

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
