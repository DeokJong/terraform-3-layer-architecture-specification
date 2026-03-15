---
title: Shared Resource Convention
doc_section: conventions
nav_parent: conventions-index
nav_order: 7
---

# Shared Resource Convention

## Resource Set first

Define a shared resource as one Resource Set before considering internal split. A Resource Set is a bundle of resources that provides one clear shared capability.

Recommended examples:

- `user-db`
- `shared-cache`
- `shared-storage`
- `shared-ingress`

## Optional partitions

Split internally only when justified:

- primary resource body
- binding or access control
- publication surface

## Split criteria

- access-control churn is high
- blast radius of binding changes is too large
- publication migration should happen independently
- operational ownership differs between primary and binding areas
