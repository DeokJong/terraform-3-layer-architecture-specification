---
title: Reference Terms
doc_section: architecture
nav_parent: architecture-index
nav_title: Reference Terms
nav_order: 15
---

# Reference Terms

This page is a lookup reference, not the main narrative entry point. Use it when a term becomes ambiguous while reading the architecture chapters.

## Core terms

| Term | Meaning |
| --- | --- |
| Layer | Logical model that defines ownership and dependency direction |
| Workspace | Operational unit that controls Terraform state, apply scope, permissions, and blast radius |
| Resource Set | Group of resources that provides one shared capability |
| Provider | Owner that publishes a Contract and guarantees its meaning |
| Consumer | Component that reads or uses a Contract |
| Contract | Officially published value or interface allowed for cross-layer consumption |
| Implementation Value | Internal detail that should not be consumed directly |
| Contract Value | Stable value that consumers are allowed to depend on |
| Primary Resource | Main resource body of a shared capability |
| Binding | Allowlist, grant, policy, or other access-control attachment |
| Publication | Surface that publishes a consumer-facing Contract |
| Source of Truth | System or owner responsible for the meaning and lifecycle of a value |
| Blast Radius | Scope affected by a change or failure |

## Common distinctions

- Layer vs Workspace:
  A Layer explains ownership and dependency rules, while a Workspace is the operational boundary for state and apply.
- Contract vs Implementation Value:
  A Contract is safe for consumers to depend on; an Implementation Value is an internal detail that may change.
- Provider vs Consumer:
  The provider owns contract meaning and compatibility. The consumer should rely only on that published contract.

## When to use this page

- when a term becomes ambiguous while reading Overview or Layers
- when checking the exact distinction between Contract and ownership rules
- when reviewing a design and needing a quick definition refresh
