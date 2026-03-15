---
title: Contracts
doc_section: architecture
nav_parent: architecture-index
nav_order: 5
---

# Contracts

This chapter explains why Contracts are necessary and which values lower layers are actually allowed to depend on. Splitting Layers is not enough on its own; the connection surface must also be constrained.

## Questions this chapter answers

- Why must consumers avoid direct dependency on provider implementation details?
- Which values count as Contracts and which are only Implementation Values?
- Who owns a Contract, and why is that different from where it is published?
- How should breaking changes be evaluated?

## Why Contracts are necessary

- Direct dependency on implementation details turns internal provider changes into consumer outages.
- A formal surface is needed to keep meaning stable even when ownership and publication location are separated.
- Layer-to-layer dependencies can only be reviewed and migrated cleanly when the allowed values are explicitly documented.

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
