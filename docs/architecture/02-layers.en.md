---
title: Layers
doc_section: architecture
nav_parent: architecture-index
nav_order: 4
---

# Layers

## Layer summary

| Layer | Role | Main responsibility | Allowed dependencies |
| --- | --- | --- | --- |
| Foundation | Base infrastructure | Network, global primitives, common platform base | None |
| Platform | Shared capability provider | Shared runtime, shared data, common interfaces | Foundation |
| Service | Service delivery layer | Service deployment, settings, permissions, endpoints | Foundation, Platform |

## Foundation

`Foundation` owns infrastructure that is environment-wide or globally shared and is not tied to a single service lifecycle.

Examples:

- VPC
- subnet groups
- shared DNS zones
- shared KMS keys

## Platform

`Platform` owns shared capabilities consumed by multiple services and publishes stable Contracts to those consumers.

Examples:

- shared database
- shared cache
- shared ingress
- shared cluster

## Service

`Service` owns resources that move with one service lifecycle and should be deployed, rolled back, and reviewed with that service.

Examples:

- service runtime
- service IAM role
- service ALB
- service DNS

## Dependency rule

Allowed dependency direction is:

- `Foundation -> Platform -> Service`

Service code may consume published Contracts from Platform or Foundation, but it should not depend on internal implementation details.

## Next

- [Contracts](./03-contracts.md)
