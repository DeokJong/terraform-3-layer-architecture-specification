# Concrete Examples

## DB Example

| Item | Recommended Placement |
| --- | --- |
| DB cluster | `platform-db-core` |
| SG allowlist | `platform-db-access` |
| stable host publication | `platform-db-contract` |
| app consumer | service runtime consumes contract only |

## S3 Example

| Item | Recommended Placement |
| --- | --- |
| shared bucket | `platform-storage-core` |
| bucket policy binding | `platform-storage-access` |
| public outputs or shared publication | `platform-storage-contract` |

## Redis Example

| Item | Recommended Placement |
| --- | --- |
| Redis core | `platform-cache-core` |
| ingress allowlist | `platform-cache-access` |
| stable endpoint publication | `platform-cache-contract` |

## Ingress Example

| Item | Recommended Placement |
| --- | --- |
| shared ingress core | `platform-ingress-core` |
| listener rule binding or allowlist | `platform-ingress-access` or related access workspace |
| stable hostname | contract or DNS publication workspace |

## Fast Classification Examples

| Question | Example Answer | Outcome |
| --- | --- | --- |
| Is it consumed by many services | yes | Platform candidate |
| Does it move with one service lifecycle | yes | Service candidate |
| Is it part of global network foundation | yes | Foundation candidate |
| Is it a stable consumer-facing value | yes | Contract candidate |
| Is it a physical endpoint or internal ID | yes | Implementation Value candidate |
