---
title: Glossary and Views
doc_section: architecture
nav_parent: architecture-index
nav_order: 3
---

# Glossary and Views

## Glossary

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

## Layer view

```mermaid
---
config:
  layout: elk
  theme: redux
  look: neo
---
flowchart TB
    Foundation[Foundation]
    Platform[Platform]
    Service[Service]

    Foundation --> Platform
    Foundation --> Service
    Platform --> Service
```

This view shows the allowed dependency direction. Higher-level capabilities may be consumed downward, but lower layers must not reach back into implementation details of upper layers.

## Workspace view

```mermaid
---
config:
  layout: elk
  theme: redux
  look: neo
---
flowchart TB
    subgraph Foundation
        FN[foundation-network-core]
        FD[foundation-dns-core]
    end

    subgraph Platform
        PDB[user-db]
        PDBP[user-db-publication]
        PCACHE[shared-cache]
    end

    subgraph Service
        SRT[service-orders-runtime]
        SCT[service-orders-contract]
    end

    FN --> PDB
    FD --> PDBP
    PDB --> PDBP
    PDBP --> SRT
    PCACHE --> SRT
    SCT --> SRT
```

This view illustrates that Layer and Workspace are related but not identical concepts. A shared capability may publish Contracts from a dedicated publication Workspace without changing ownership.

## Next

- [Layers](./02-layers.md)
