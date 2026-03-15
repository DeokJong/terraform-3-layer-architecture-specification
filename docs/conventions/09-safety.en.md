---
title: Safety Convention
doc_section: conventions
nav_parent: conventions-index
nav_order: 10
---

# Safety Convention

## Change safety

- Separate implementation change from Contract change.
- Do not directly replace an active Contract without a migration path.
- Publish in parallel before performing a breaking switch.

## Blast radius control

- keep shared core stable when access churn is high
- split high-risk bindings when needed
- stage consumer migration rather than forcing all consumers at once

## Rollback rule

If rollback requires immediate coordination from every consumer, the rollout plan is too risky.
