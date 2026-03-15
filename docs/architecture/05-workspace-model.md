---
title: 워크스페이스 모델
doc_section: architecture
nav_parent: architecture-index
nav_order: 7
---

# 워크스페이스 모델

이 장은 "같은 capability를 왜 여러 워크스페이스로 나눌 수 있는가"를 설명합니다. Layer가 ownership 모델이라면, 워크스페이스는 state, apply, 권한, blast radius를 조절하는 운영 모델입니다.

## 이 장이 답하는 질문

- 어떤 경우에 하나의 capability를 하나의 워크스페이스로 유지할 수 있는가
- 어떤 경우에 core, 바인딩, 게시를 분리해야 하는가
- 워크스페이스를 나누더라도 ownership은 왜 그대로일 수 있는가
- 공유 리소스 모델과 워크스페이스 모델은 무엇이 다른가

## 공유 리소스 모델과의 차이

`공유 리소스`는 "무엇을 제공하는가"를 기준으로 capability boundary를 설명합니다. 반면 `워크스페이스 모델`은 "어떻게 운영 위험을 나누는가"를 기준으로 apply 경계를 설명합니다.

정리하면:

- 공유 리소스 = 기능 단위 모델
- 워크스페이스 = 운영 경계 모델

그래서 `user-db`는 하나의 공유 리소스일 수 있지만, 운영상 필요하면 `user-db`, `user-db-access`, `user-db-publication`처럼 여러 워크스페이스로 나눌 수 있습니다.

## 워크스페이스 정의

워크스페이스는 Terraform state, apply, 권한 경계, 영향 범위를 가지는 운영 단위입니다.

정리:

- Layer = ownership / dependency 모델
- 워크스페이스 = state / apply / 영향 범위 모델

## 워크스페이스 유형

### 본체 리소스 워크스페이스

- VPC
- Cluster
- RDS
- Shared S3
- KMS Key

특성:

- 변경 빈도 낮음
- 영향 범위 큼
- 안정성 우선

### 바인딩 워크스페이스

- SG ingress allowlist
- bucket policy attachment
- KMS grants
- consumer binding

특성:

- 변경 빈도 높을 수 있음
- onboarding / offboarding 잦을 수 있음
- primary resource와 분리 가치가 큼

### 게시 워크스페이스

- SSM parameter 게시
- Route53 stable endpoint 게시
- output aggregation

특성:

- consumer-facing surface를 담당
- source of truth와 분리될 수 있음
- ownership 자체를 가져가지는 않음

### 서비스 런타임 워크스페이스

- ECS Service
- Lambda stack
- service IAM / SG
- service-specific DNS

## 같은 워크스페이스에 둘 수 있는 경우

- 항상 함께 변경됨
- lifecycle이 동일함
- ownership이 동일함
- 영향 범위 차이가 작음
- 운영 주체와 리뷰 주체가 같다

예:

- 하나의 `user-db` Resource Set을 한 팀이 함께 관리
- 하나의 `user-db`에 대해 DB cluster, SG allowlist, SSM publication을 함께 관리
- 하나의 `shared-storage`에 대해 bucket, policy binding, output publication을 함께 관리

## 분리를 우선 검토해야 하는 경우

- 변경 빈도가 다름
- apply 주체가 다름
- rollback 위험이 다름
- downstream dependency가 많음
- 고위험 resource body와 binding이 섞여 있음
- 서비스 온보딩이나 access rule 변경이 잦음
- 게시 계약을 별도 마이그레이션해야 할 가능성이 큼

## 워크스페이스와 계약의 관계

Workspace는 Contract를 게시할 수 있지만 Contract owner와 항상 동일하지는 않습니다.

예:

- `user-db` Resource Set이 DB를 생성하고 lifecycle을 관리한다.
- `user-db-publication`이 stable endpoint를 SSM이나 DNS에 게시한다.
- Contract owner는 여전히 `user-db` Platform domain이며, publication workspace는 게시 책임만 수행한다.

즉 publication workspace는 source of truth를 대체하지 않습니다.

## 안티패턴

- 변경 특성이 뚜렷이 다른데도 하나의 workspace가 primary resource, binding, publication을 모두 관리
- 서비스 온보딩마다 primary resource workspace를 수정
- shared resource의 policy churn이 primary resource 안정성을 침범
- aggregation workspace가 사실상 source of truth가 되는 구조

## 권장 구조 예시

Foundation:

- `foundation-network-core`
- `foundation-dns-core`
- `foundation-kms-core`

Platform:

- `platform-cluster-core`
- `user-db`
- `user-db-publication`
- `shared-storage`
- `shared-storage-publication`

Service:

- `service-orders-runtime`
- `service-orders-access`
- `service-orders-contract`

## 워크스페이스 분리 판단 매트릭스

| 질문 | 예 | 답이 "예"면 |
| --- | --- | --- |
| 항상 함께 변경되는가 | `user-db` 본체와 publication이 항상 같이 수정됨 | 같은 workspace 가능 |
| ownership이 동일한가 | 동일 팀이 lifecycle 전체 관리 | 같은 workspace 가능 |
| binding churn이 잦은가 | consumer onboarding이 자주 발생 | binding 분리 우선 검토 |
| rollback 위험이 다른가 | DB 교체와 policy 수정의 위험도 차이 큼 | 분리 검토 |
| consumer contract migration이 필요한가 | DNS/SSM path 이행 중 | publication 분리 검토 |
| blast radius가 크게 다른가 | 버킷 본체와 policy binding 영향 범위 차이 큼 | 분리 검토 |

## 다음 문서

- [공유 리소스](./06-shared-resources.md)

