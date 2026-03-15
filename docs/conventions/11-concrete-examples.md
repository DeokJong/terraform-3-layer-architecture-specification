---
title: 구체 예시
doc_section: conventions
nav_parent: conventions-index
nav_order: 12
---

# Concrete Examples

## DB Example

| Item | Recommended Placement |
| --- | --- |
| DB cluster | `user-db` |
| SG allowlist | `user-db` or `user-db-binding` |
| stable host publication | `user-db-publication` |
| app consumer | service runtime consumes contract only |

## S3 Example

| Item | Recommended Placement |
| --- | --- |
| shared bucket | `shared-storage` |
| bucket policy binding | `shared-storage` or `shared-storage-binding` |
| public outputs or shared publication | `shared-storage-publication` |

## Redis Example

| Item | Recommended Placement |
| --- | --- |
| Redis core | `shared-cache` |
| ingress allowlist | `shared-cache` or `shared-cache-binding` |
| stable endpoint publication | `shared-cache-publication` |

## Ingress Example

| Item | Recommended Placement |
| --- | --- |
| shared ingress core | `shared-ingress` |
| listener rule binding or allowlist | `shared-ingress` or `shared-ingress-binding` |
| stable hostname | publication workspace or DNS publication set |

## Fast Classification Examples

| Question | Example Answer | Outcome |
| --- | --- | --- |
| Is it consumed by many services | yes | Platform candidate |
| Does it move with one service lifecycle | yes | Service candidate |
| Is it part of global network foundation | yes | Foundation candidate |
| Is it a stable consumer-facing value | yes | Contract candidate |
| Is it a physical endpoint or internal ID | yes | Implementation Value candidate |

