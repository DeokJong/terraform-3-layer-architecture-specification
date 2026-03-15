---
title: Ownership Convention
doc_section: conventions
nav_parent: conventions-index
nav_order: 3
---

# Ownership Convention

## Ownership decision rules

The owner is the layer most strongly connected to these questions:

1. Who manages the lifecycle?
2. Who is responsible for change?
3. Who guarantees interface stability?
4. Who owns deletion and migration responsibility?

## What not to use as the deciding factor

Do not base ownership on:

- who currently reads the value
- where the value is stored
- which tool publishes the value
- which Workspace currently contains the code

## Working rule

Consumers may read provider-owned Contracts, but that does not make them the owner.
