---
title: Contracts
doc_section: architecture
nav_parent: architecture-index
nav_order: 5
---

# Contracts

## Contract definition

A Contract is a formally published value or interface used to express allowed dependencies between layers.

Examples:

- Terraform output
- SSM Parameter
- Route53 record
- Secrets Manager reference
- IAM principal reference
- Security Group client identity

## Why Contracts matter

Contracts separate provider-owned implementation from consumer-facing meaning.

Consumers should depend on:

- stable DNS names
- standard SSM paths
- intentionally published outputs
- documented interface names

Consumers should not depend on:

- physical endpoints that may change frequently
- internal IDs or implementation-specific names
- private resource topology

## Contract ownership

The owner of a Contract is the provider that guarantees its meaning and lifecycle, not the tool or medium used to publish it.

Publishing through `SSM`, `Route53`, or Terraform outputs does not move ownership.

## Lifecycle model

- New Contracts start as `Draft` or `Active`.
- Breaking changes require parallel publication.
- Old Contracts move to `Deprecated` before removal.
- Consumers migrate before the old Contract is deleted.

## Next

- [Ownership and References](./04-ownership-and-references.md)
