---
title: Service Dependencies
doc_section: architecture
nav_parent: architecture-index
nav_order: 9
---

# Service Dependencies

## Basic rule

A Service must not depend directly on another Service's implementation.

Allowed:

- stable API hostname published by another service
- official authentication or authorization interface
- intentionally documented consumer-facing Contract

Disallowed:

- direct use of another service's physical ALB DNS
- direct reference to another service's private resource IDs
- coupling to another service's internal database or cache topology

## Access dependencies

Auth, allowlist, Security Group grants, and IAM relationships should be modeled as access dependencies, not as permission to consume arbitrary implementation details.

## Review question

If one service changes its internal implementation, can the consumer keep working without immediate code changes? If not, the dependency is probably too deep.

## Next

- [Operations](./08-operations.md)
