---
title: Workspace Convention
doc_section: conventions
nav_parent: conventions-index
nav_order: 5
---

# Workspace Convention

## Design principles

- Design Workspaces separately from Layers.
- Define the Resource Set first, then split internally only when needed.
- Separate high-risk resource bodies from high-churn bindings when their change patterns differ.
- Treat publication boundaries based on Contract ownership and migration, not only namespace convenience.
- Service runtime should remain independently deployable whenever practical.

## Split signals

Split a Workspace when:

- blast radius becomes too large
- different operators own different parts
- binding churn is much higher than core lifecycle
- publication migration needs a separate rollout

## Anti-pattern

Do not create one Workspace per Layer by default. That hides the real lifecycle model and often creates unnecessary coordination.
