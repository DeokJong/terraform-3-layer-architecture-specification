---
title: Service Dependencies
doc_section: architecture
nav_parent: architecture-index
nav_order: 9
---

# Service Dependencies

This chapter is not about banning all service-to-service dependency. It explains what a service may depend on when such a dependency is necessary. Implementation references stay prohibited; only published Contracts are allowed.

## Questions this chapter answers

- What may Service A reference when it needs something from Service B?
- What is allowed in cases such as an SSR frontend that needs a backend endpoint?
- How does service-to-service dependency differ from a shared Platform capability?

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
