---
title: Review Checklist
doc_section: conventions
nav_parent: conventions-index
nav_order: 11
---

# Review Checklist

Check the following when adding a resource or Contract:

- Which Layer owns this resource?
- Is this value a Contract or an Implementation Value?
- Is the provider, not the consumer, represented as the owner?
- Does a Workspace split reduce blast radius?
- Are shared core and access-control bindings mixed unnecessarily?
- Can the provider evolve implementation without breaking consumers?
- Is there a migration path for any breaking change?
