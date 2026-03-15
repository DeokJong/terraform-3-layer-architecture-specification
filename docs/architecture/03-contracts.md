---
title: Contracts
doc_section: architecture
nav_parent: architecture-index
nav_order: 5
---

# Contracts

## Contract 정의

Contract는 레이어 간 의존성을 표현하기 위해 공식적으로 게시된 값 또는 인터페이스입니다.

예:

- Terraform output
- SSM Parameter
- Route53 Record
- Secret reference
- IAM principal reference
- Security Group client identity
- stable bucket name, cluster name, key ARN

Contract는 다음 성질을 가져야 합니다.

- consumer가 구현 세부사항을 몰라도 사용할 수 있어야 한다.
- 의미가 문서화되어 있어야 한다.
- provider가 안정성과 변경 정책을 설명할 수 있어야 한다.
- breaking change 여부를 판단할 수 있어야 한다.

즉, 외부에 노출된 값이 모두 Contract는 아닙니다. provider가 공식 surface로 관리하는 값만 Contract로 취급합니다.

## Implementation Value vs Contract Value

| 구분 | 의미 | 하위 레이어 직접 참조 여부 |
| --- | --- | --- |
| Implementation Value | 내부 구현 세부사항 | 금지 |
| Contract Value | 안정적으로 게시된 공식 값 | 허용 |

Implementation Value 예:

- RDS가 직접 생성한 endpoint
- ALB physical name
- 내부 리소스 ID

Contract Value 예:

- stable DNS name
- 표준 SSM parameter path
- 공식 output name
- stable bucket name

판단 질문:

- 이 값은 내부 구현이 바뀌어도 유지되어야 하는가
- 하위 레이어가 이 값에 의존해도 provider가 책임질 수 있는가
- 문서와 운영 절차에 따라 변경 관리가 가능한가

## Contract 유형

### Identity Contract

- VPC ID
- Hosted Zone ID
- Cluster Name
- Bucket Name
- KMS Key ARN

### Connectivity Contract

- DB stable DNS
- Redis stable DNS
- shared ingress hostname
- internal API hostname

### Access Contract

- Client SG
- IAM principal ARN
- IRSA Role ARN
- consumer principal

### Runtime Contract

- SSM parameter
- Secret reference
- queue URL
- topic name

## Publication 모델

Contract는 아래 두 요소가 합쳐져야 성립합니다.

1. 의미를 정의하는 provider
2. 값을 전달하는 publication surface

publication surface 예:

- Terraform output
- SSM parameter
- Route53 record
- Secrets Manager reference
- output aggregation

publication surface는 ownership을 결정하지 않습니다.

## Owner와 Consumer 책임

### Provider 책임

- Contract 의미 정의
- naming과 path 안정성 관리
- 변경 호환성 보장
- deprecation 및 migration 계획 제공
- consumer가 기대할 수 있는 semantics 문서화

### Consumer 책임

- Contract만 의존하고 implementation을 추측하지 않기
- deprecated signal에 맞춰 migration 수행
- 비공식 값이나 임시 output에 의존하지 않기

## Contract 최소 기술 항목

| 항목 | 설명 |
| --- | --- |
| Name | Contract 이름 |
| Type | Identity / Connectivity / Access / Runtime |
| Provider | Contract owner |
| Consumer | 예상 consumer 또는 consumer class |
| Publication | Terraform output / SSM / DNS 등 전달 수단 |
| Stability | stable / versioned / temporary |
| Breaking Change Policy | 변경 시 절차 |
| Source of Truth | 실제 값을 생성하는 시스템 또는 workspace |

## Source of Truth

publication workspace나 aggregation workspace가 있더라도 source of truth는 원 provider에 남아 있어야 합니다.

예:

- DB endpoint contract의 source of truth는 DB를 운영하는 Platform domain
- DNS publication은 contract 전달 수단일 뿐 ownership 이전이 아님
- aggregation output은 convenience layer일 수 있지만 contract 의미를 새로 정의하지는 않음

## Compatibility 원칙

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

## Lifecycle

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

### DB endpoint

- 실제 DB instance endpoint: Implementation Value
- `db-main.internal.example.com`: Connectivity Contract
- `/platform/db/main/host`: Runtime Contract

### shared bucket

- bucket physical ID: Implementation Value일 수 있음
- stable bucket name: Identity Contract
- bucket consumer principal binding: Access Contract

### service API

- internal ALB DNS: Implementation Value
- `orders-api.internal.example.com`: Service가 제공하는 Connectivity Contract

## 다음 문서

- [Ownership and References](./04-ownership-and-references.md)

