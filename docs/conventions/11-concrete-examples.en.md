---
title: Concrete Examples
doc_section: conventions
nav_parent: conventions-index
nav_order: 12
---

# Concrete Examples

## DB example

| Item | Recommended placement |
| --- | --- |
| DB cluster | `user-db` |
| SG allowlist | `user-db` or `user-db-binding` |
| stable host publication | `user-db-publication` |
| app consumer | service runtime consumes Contract only |

## S3 example

| Item | Recommended placement |
| --- | --- |
| shared bucket | `shared-storage` |
| bucket policy binding | `shared-storage` or `shared-storage-binding` |
| public outputs or shared publication | `shared-storage-publication` |

## Redis example

| Item | Recommended placement |
| --- | --- |
| Redis core | `shared-cache` |
| ingress allowlist | `shared-cache` or `shared-cache-binding` |
| stable endpoint publication | `shared-cache-publication` |

## Ingress example

| Item | Recommended placement |
| --- | --- |
| shared ingress core | `shared-ingress` |
| listener rule binding or allowlist | `shared-ingress` or `shared-ingress-binding` |
| stable hostname | publication Workspace or DNS publication set |

## Fast classification examples

| Question | Example answer | Outcome |
| --- | --- | --- |
| Is it consumed by many services? | yes | Platform candidate |
| Does it move with one service lifecycle? | yes | Service candidate |
| Is it part of global network foundation? | yes | Foundation candidate |
| Is it a stable consumer-facing value? | yes | Contract candidate |
| Is it a physical endpoint or internal ID? | yes | Implementation Value candidate |
