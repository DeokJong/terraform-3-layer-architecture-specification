---
title: Overview
doc_section: architecture
nav_parent: architecture-index
nav_order: 2
---

# Overview

## Purpose

This document defines the architecture rules for operating Terraform-based infrastructure with three layers: `Foundation`, `Platform`, and `Service`.

Its main goals are:

- clarify ownership and responsibility for each layer
- keep dependency direction explicit and predictable
- connect layers through Contracts rather than direct implementation references
- define when a Workspace should be split
- organize a stable operating model for shared resources

## Scope

Included in scope:

- AWS infrastructure managed by Terraform
- shared infrastructure and service-specific infrastructure
- value publication and reference rules between layers
- Workspace design principles

Out of scope:

- application-internal implementation details
- deployment pipeline details
- low-level module implementation per resource

## Non-goals

This document does not aim to:

- rename all existing assets immediately
- promote every shared resource to `Platform` by default
- force a 1:1 mapping between Layer and Workspace
- broadly allow direct cross-layer references for implementation convenience

## Audience

- engineers designing Terraform Workspaces
- platform engineers operating shared infrastructure
- service teams designing or consuming service infrastructure

## Design principles

- A Layer is an ownership model.
- Dependency direction must remain explicit.
- Lower layers consume Contracts, not implementation details.
- Contract ownership belongs to the provider.
- A Workspace is an operating boundary, not the same thing as a Layer.
- Shared resources should stay stable even when consumer count grows.

In smaller environments, `core`, `binding`, and `publication` can remain in one Workspace. Split them only when change churn, risk, or operational ownership diverges.

## Next

- [Glossary and Views](./01a-glossary-and-views.md)
