---
title: Network and IAM Convention
doc_section: conventions
nav_parent: conventions-index
nav_order: 6
---

# Network and IAM Convention

## Security Group rules

- The receiving side owner manages ingress rules.
- Shared producer Security Groups are owned by the provider layer, usually `Platform`.
- Represent service identity with stable client Security Groups whenever possible.

Recommended pattern:

- provider owns the target SG
- consumer is represented through a client SG or explicit binding
- access policy changes do not force implementation coupling

## IAM rules

- IAM roles move with the runtime lifecycle that uses them.
- Shared access should be expressed through explicit grants or assumable roles.
- Do not use IAM as a shortcut to hide unclear ownership.
