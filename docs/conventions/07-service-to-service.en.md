---
title: Service-to-Service Convention
doc_section: conventions
nav_parent: conventions-index
nav_order: 8
---

# Service-to-Service Convention

- A Service must not consume another Service's implementation directly.
- Use only the API hostname or official Contract published by the provider service.
- Treat auth, allowlist, and binding as access dependencies, not permission to bypass Contracts.

Forbidden examples:

- direct use of another service's ALB physical DNS
- direct reference to another service's private database endpoint
- coupling to another service's internal Terraform outputs when no official Contract exists

Recommended approach:

- publish a stable hostname
- publish a documented authentication contract
- keep service-specific implementation private
