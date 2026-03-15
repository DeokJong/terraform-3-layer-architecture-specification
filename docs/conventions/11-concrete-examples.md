---
title: 구체 예시
doc_section: conventions
nav_parent: conventions-index
nav_order: 12
---

# 구체적 예시

## DB 예시

| Item | Recommended Placement |
| --- | --- |
| DB cluster | `user-db` |
| SG allowlist | `user-db` or `user-db-바인딩` |
| stable host 게시 | `user-db-게시` |
| app consumer | service runtime consumes contract only |

## S3 예시

| Item | Recommended Placement |
| --- | --- |
| shared bucket | `shared-storage` |
| bucket policy 바인딩 | `shared-storage` or `shared-storage-바인딩` |
| public outputs or shared 게시 | `shared-storage-게시` |

## Redis 예시

| Item | Recommended Placement |
| --- | --- |
| Redis core | `shared-cache` |
| ingress allowlist | `shared-cache` or `shared-cache-바인딩` |
| stable endpoint 게시 | `shared-cache-게시` |

## Ingress 예시

| Item | Recommended Placement |
| --- | --- |
| shared ingress core | `shared-ingress` |
| listener rule 바인딩 or allowlist | `shared-ingress` or `shared-ingress-바인딩` |
| stable hostname | 게시 워크스페이스 or DNS 게시 세트 |

## 빠른 분류 예시

| Question | Example Answer | Outcome |
| --- | --- | --- |
| Is it consumed by many services | yes | Platform candidate |
| Does it move with one service lifecycle | yes | Service candidate |
| Is it part of global network foundation | yes | Foundation candidate |
| 안정적인 consumer-facing value인가 | yes | 계약 후보 |
| physical endpoint 또는 internal ID인가 | yes | 구현값 후보 |


