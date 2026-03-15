---
title: 계약
doc_section: architecture
nav_parent: architecture-index
nav_order: 5
---

# 계약

이 장은 "왜 계약이 필요한가"와 "어떤 값만 하위 레이어가 의존해도 되는가"를 설명합니다. Layer를 나누는 것만으로는 충분하지 않고, 실제 연결 surface를 계약으로 제한해야 구조가 오래 유지됩니다.

## 이 장이 답하는 질문

- 왜 소비자가 제공자의 구현 세부사항을 직접 보면 안 되는가
- 어떤 값이 계약이고 어떤 값이 구현값인가
- 계약 소유자는 누가 되며, 게시 위치와 왜 다른가
- 호환성 깨짐 변경을 어떻게 판단해야 하는가

## 왜 계약이 필요한가

- 구현 세부사항에 직접 의존하면 제공자 내부 교체가 소비자 장애로 이어집니다.
- ownership과 게시 위치를 분리해도 meaning을 안정적으로 유지하려면 공식 surface가 필요합니다.
- Layer 간 연결을 리뷰하고 migration하기 위해서는 "의존 가능한 값 목록"이 문서화되어야 합니다.

## 계약 정의

계약은 레이어 간 의존성을 표현하기 위해 공식적으로 게시된 값 또는 인터페이스입니다.

예:

- Terraform output
- SSM Parameter
- Route53 Record
- Secret reference
- IAM principal reference
- Security Group client identity
- stable bucket name, cluster name, key ARN

계약은 다음 성질을 가져야 합니다.

- 소비자가 구현 세부사항을 몰라도 사용할 수 있어야 한다.
- 의미가 문서화되어 있어야 한다.
- 제공자가 안정성과 변경 정책을 설명할 수 있어야 한다.
- 호환성 깨짐 변경 여부를 판단할 수 있어야 한다.

즉, 외부에 노출된 값이 모두 계약은 아닙니다. 제공자가 공식 surface로 관리하는 값만 계약으로 취급합니다.

## 구현값과 계약값

| 구분 | 의미 | 하위 레이어 직접 참조 여부 |
| --- | --- | --- |
| 구현값 | 내부 구현 세부사항 | 금지 |
| 계약값 | 안정적으로 게시된 공식 값 | 허용 |

구현값 예:

- RDS가 직접 생성한 endpoint
- ALB physical name
- 내부 리소스 ID

계약값 예:

- stable DNS name
- 표준 SSM parameter path
- 공식 output name
- stable bucket name

판단 질문:

- 이 값은 내부 구현이 바뀌어도 유지되어야 하는가
- 하위 레이어가 이 값에 의존해도 제공자가 책임질 수 있는가
- 문서와 운영 절차에 따라 변경 관리가 가능한가

## 계약 유형

### 식별 계약

- VPC ID
- Hosted Zone ID
- Cluster Name
- Bucket Name
- KMS Key ARN

### 연결 계약

- DB stable DNS
- Redis stable DNS
- shared ingress hostname
- internal API hostname

### 접근 계약

- Client SG
- IAM principal ARN
- IRSA Role ARN
- consumer principal

### 런타임 계약

- SSM parameter
- Secret reference
- queue URL
- topic name

## 게시 모델

Contract는 아래 두 요소가 합쳐져야 성립합니다.

1. 의미를 정의하는 provider
2. 값을 전달하는 게시 surface

게시 surface 예:

- Terraform output
- SSM parameter
- Route53 record
- Secrets Manager reference
- output aggregation

게시 surface는 ownership을 결정하지 않습니다.

## 제공자와 소비자 책임

### 제공자 책임

- Contract 의미 정의
- naming과 path 안정성 관리
- 변경 호환성 보장
- deprecation 및 migration 계획 제공
- consumer가 기대할 수 있는 semantics 문서화

### 소비자 책임

- Contract만 의존하고 implementation을 추측하지 않기
- deprecated signal에 맞춰 migration 수행
- 비공식 값이나 임시 output에 의존하지 않기

## 계약 최소 기술 항목

| 항목 | 설명 |
| --- | --- |
| 이름 | 계약 이름 |
| Type | Identity / Connectivity / Access / Runtime |
| Provider | 계약 소유자 |
| Consumer | 예상 consumer 또는 consumer class |
| 게시 방식 | Terraform output / SSM / DNS 등 전달 수단 |
| Stability | stable / versioned / temporary |
| Breaking Change Policy | 변경 시 절차 |
| Source of Truth | 실제 값을 생성하는 시스템 또는 workspace |

## 원천 시스템

publication workspace나 aggregation workspace가 있더라도 source of truth는 원 provider에 남아 있어야 합니다.

예:

- DB endpoint contract의 source of truth는 DB를 운영하는 Platform domain
- DNS publication은 contract 전달 수단일 뿐 ownership 이전이 아님
- aggregation output은 convenience layer일 수 있지만 contract 의미를 새로 정의하지는 않음

## 호환성 원칙

breaking change 예:

- contract name 변경
- parameter path 변경
- DNS name 변경
- 값의 의미 변경
- consumer가 기대하는 format 변경
- access contract의 scope 축소

non-breaking change 예:

- implementation 교체 후 contract value 유지
- publication backend의 내부 구조 변경
- consumer에게 투명한 내부 리소스 교체

breaking 여부는 `consumer 수정이 필요한가`와 `기존 의미가 유지되는가`를 기준으로 판단합니다.

## 생명주기

상태:

- Draft
- Active
- Deprecated
- Removed

권장 상태 전이:

`Draft -> Active -> Deprecated -> Removed`

운영 원칙:

- Active Contract는 in-place rename 하지 않는다.
- Active Contract의 의미를 조용히 바꾸지 않는다.
- breaking change가 필요하면 새 Contract를 추가하고 migration을 수행한다.
- Deprecated 없이 바로 제거하지 않는다.

## 사례

### DB 엔드포인트

- 실제 DB instance endpoint: 구현값
- `db-main.internal.example.com`: 연결 계약
- `/platform/db/main/host`: 런타임 계약

### 공유 버킷

- bucket physical ID: Implementation Value일 수 있음
- stable bucket name: 식별 계약
- bucket consumer principal binding: 접근 계약

### 서비스 API

- internal ALB DNS: 구현값
- `orders-api.internal.example.com`: Service가 제공하는 연결 계약

## 다음 문서

- [소유권과 참조](./04-ownership-and-references.md)

