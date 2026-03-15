---
title: Contract Convention
doc_section: conventions
nav_parent: conventions-index
nav_order: 4
---

# Contract Convention

## Design principles

- Lower layers consume Contracts only.
- Implementation Values are not exposed directly.
- Contracts must carry stable meaning.
- The Contract owner is the provider.

## Publication media

- Terraform output
- SSM Parameter
- Route53 record
- Secrets Manager reference

The publication medium does not change ownership.

## Naming convention

Principles:

- choose names that express consumer meaning
- prefer purpose over implementation detail
- prefer stable names that survive implementation change

Recommended examples:

- `db-main.internal.example.com`
- `/platform/orders/db/host`
- `orders-api.internal.example.com`
- `platform_db_primary_endpoint`

## Lifecycle convention

- Start a new Contract as `Draft` or `Active`.
- For breaking changes, publish a new Contract in parallel.
- Move the old Contract through `Deprecated`.
- Remove it only after consumer migration completes.

## Contract record

Each Contract should document:

- name
- type
- provider
- main consumer class
- publication method
- source of truth
- breaking-change procedure
