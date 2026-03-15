---
title: ADR-0001
description: ADR that records the rationale, expected benefits, and trade-offs of the 3-layer Terraform contract/workspace model.
hero_kicker: Architecture Decision Record
doc_section: adr
nav_parent: adr-index
nav_order: 2
nav_title: ADR-0001
---

# ADR-0001: 3-Layer Architecture and Contract / Workspace Model

Original root ADR:

- [Root ADR](../../adr-3layer-architecture-contract-workspace.md)

## Title

Define the Layer, Contract, Workspace, and ownership rules for the 3-layer architecture.

## Status

Accepted

## Summary

This ADR records the following decisions:

- Layer defines ownership and dependency direction.
- Workspace is treated as an operational boundary, not the same thing as a Layer.
- Cross-layer published values are treated as Contracts.
- Contract ownership belongs to the provider.
- Implementation Value and Contract Value must be distinguished.
- Shared resources are explained first as Resource Sets, then split internally only when blast radius or churn requires it.
- Existing assets are treated as legacy and migrated gradually.

## Rationale

The repository needed a clearer model for:

- boundary control between shared and service-specific resources
- ownership of published values such as SSM, Route53, and Secrets Manager entries
- Workspace splitting rules
- safer service-to-service dependency handling

The target was not a forced big-bang rename. The goal was to provide a practical model for future design and migration.

## Reference material

This ADR uses HashiCorp's [Happy Terraforming! Real-world experience and proven best practices](https://www.hashicorp.com/en/resources/terraforming-real-world-experience-best-practices) as an important reference, but adapts it to this repository's `Foundation / Platform / Service`, `Contract`, `Workspace`, and `Resource Set` vocabulary.

## Detailed record

For the full background and extended reasoning, refer to:

- [adr-3layer-architecture-contract-workspace.md](../../adr-3layer-architecture-contract-workspace.md)
