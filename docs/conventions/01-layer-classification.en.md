---
title: Layer Classification Convention
doc_section: conventions
nav_parent: conventions-index
nav_order: 2
---

# Layer Classification Convention

## Foundation

Classify something as `Foundation` when these traits are strong:

- environment-wide or global base infrastructure
- used commonly by multiple upper areas
- relatively low change frequency
- not tied to one service lifecycle

Examples:

- VPC
- subnets
- Hosted Zone
- shared KMS key

## Platform

Classify something as `Platform` when it:

- is consumed by multiple services
- provides a shared capability
- publishes stable Contracts as a provider
- has a lifecycle independent of one service runtime

Examples:

- shared cluster
- shared database
- shared cache
- shared ingress

## Service

Classify something as `Service` when it:

- is deployed with one service
- belongs to that service's rollback and failure boundary
- exists mainly for that service

Examples:

- service runtime
- service IAM role
- service ALB
- service DNS
