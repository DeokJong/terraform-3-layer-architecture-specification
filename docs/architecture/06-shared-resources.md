---
title: 공유 리소스
doc_section: architecture
nav_parent: architecture-index
nav_order: 8
---

# Shared Resources

## Resource Set 우선 모델

shared resource는 우선 하나의 shared capability를 제공하는 Resource Set으로 정의합니다.

예:

- `user-db`
- `book-db`
- `finance-db`
- `shared-cache`
- `shared-ingress`

각 Resource Set은 하나의 명확한 Platform capability를 설명하는 리소스 묶음이며, 해당 capability를 제공하는 데 필요한 구성요소를 함께 포함할 수 있습니다.

예:

- RDS cluster / instance
- security group
- KMS key
- DNS record
- SSM parameter

Platform Layer는 일반적으로 Service Layer보다 구조 변화가 적고 stable capability boundary를 가지므로, shared resource를 먼저 Resource Set 관점으로 설명하는 것을 권장합니다.

## Resource Set 내부 분리 기준

하나의 Resource Set 안에 모든 구성요소를 둘 수도 있고, blast radius와 lifecycle 차이에 따라 내부를 여러 workspace나 하위 set으로 나눌 수도 있습니다.

분리 여부는 다음 기준으로 판단합니다.

- 재생성 또는 교체 위험이 큰가
- 변경 빈도가 현저히 다른가
- owner 또는 승인 절차가 다른가
- rollback 경계가 다른가
- publication 변경 실패가 core 안정성에 전파되면 안 되는가

즉 shared resource의 1차 경계는 역할명이 아니라 capability boundary이며, 내부 분리는 blast radius와 운영 경계에 따라 선택합니다.

## Core / Access / Publication은 선택적 내부 패턴

`Core / Access / Publication`은 shared resource를 항상 강제하는 기본 구조가 아니라, Resource Set 내부를 설명할 때 자주 쓰는 역할 라벨입니다.

| 역할 라벨 | 설명 | 예시 |
| --- | --- | --- |
| Core | 본체 리소스 | DB, bucket, cluster |
| Access | 허용 정책과 binding | SG rule, bucket policy, KMS grant |
| Publication | consumer-facing contract 게시 | DNS, SSM parameter, output |

예를 들어 `user-db` Resource Set은 필요 시 아래처럼 나눌 수 있습니다.

- `user-db-core`
- `user-db-access`
- `user-db-publication`

하지만 이것은 대표 패턴일 뿐이며, 모든 shared resource에 동일한 분해를 강제하지 않습니다.

## DB Resource Set 예시

`user-db` 같은 DB Resource Set은 다음 구성요소를 함께 포함할 수 있습니다.

- DB cluster / instance
- DB 관련 security group
- DB 암호화용 KMS key
- stable DNS record
- SSM parameter contract

소수 consumer만 사용하고 access churn이 낮으며 ownership이 동일하다면 하나의 workspace로 둘 수 있습니다. 반대로 consumer 수 증가, 잦은 allowlist 변경, contract migration, 별도 KMS governance 필요성이 생기면 그 시점에 내부 분리를 검토합니다.

## Owner 책임

shared resource owner는 다음을 책임집니다.

- capability lifecycle 관리
- consumer에게 제공할 contract 정의
- access control 정책의 승인 모델 정의
- migration과 compatibility 정책 제공

consumer는 shared resource를 직접 변경하는 대신 access contract와 publication contract를 통해 연결되어야 합니다.

중요한 점은 publication location이 ownership을 결정하지 않는다는 것입니다. 예를 들어 legacy 경로 아래 SSM parameter를 게시하더라도, 그 값의 의미와 lifecycle을 shared resource owner가 책임지면 owner는 여전히 Platform Resource Set입니다.

## Shared Resource 예시 매핑

| Resource Set 예시 | 포함 가능 구성요소 | 선택적 내부 분리 예시 |
| --- | --- | --- |
| `user-db` | cluster / instance, SG, KMS, DNS, SSM host | core, access, publication |
| `shared-storage` | bucket, encryption, policy binding, published output | core, access, publication |
| `shared-cache` | cluster, ingress allowlist, endpoint publication | core, access, publication |
| `shared-ingress` | ALB / NLB / gateway, listener rule, stable hostname | core, access, publication |

## 다음 문서

- [Service Dependencies](./07-service-dependencies.md)

