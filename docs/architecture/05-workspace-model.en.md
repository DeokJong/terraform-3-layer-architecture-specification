---
title: Workspace Model
doc_section: architecture
nav_parent: architecture-index
nav_order: 7
---

# Workspace Model

This chapter explains why one capability may still be split across multiple Workspaces. A Layer is an ownership model, while a Workspace is an operating model for state, apply scope, permissions, and blast radius.

## Questions this chapter answers

- When can one capability remain in one Workspace?
- When should core, binding, and publication be split?
- Why can ownership stay the same even after Workspaces are separated?
- How is the Workspace model different from the Shared Resource model?

## Difference from the Shared Resource model

The `Shared Resource` model explains a capability boundary in terms of what is being provided. The `Workspace Model` explains an operating boundary in terms of how change risk and apply scope are separated.

In short:

- Shared Resource = capability model
- Workspace = operating-boundary model

So `user-db` may be one Shared Resource while still being operated through multiple Workspaces such as `user-db`, `user-db-access`, and `user-db-publication`.

## Workspace definition

A Workspace is an operational boundary for Terraform state, apply scope, permissions, and blast radius.

Summary:

- Layer = ownership and dependency model
- Workspace = operating boundary

These are related but not identical concepts.

## When to keep one Workspace

Keep one Workspace when:

- lifecycle is tightly coupled
- change frequency is similar
- the same team applies changes
- blast radius is acceptable

## When to split a Workspace

Split a Workspace when:

- binding or policy churn is much higher than the primary resource body
- different operators own different parts of the capability
- rollback risk differs significantly
- publication migration should move independently
- downstream dependencies need a safer blast radius boundary

## Typical pattern

One shared capability may be organized as:

- `core` for the primary resource body
- `binding` for grants, allowlists, or policy attachments
- `publication` for DNS, SSM, or consumer-facing outputs

## Anti-pattern

Do not force one Workspace per Layer. That creates artificial boundaries and often hides the actual lifecycle model.

## Next

- [Shared Resources](./06-shared-resources.md)
