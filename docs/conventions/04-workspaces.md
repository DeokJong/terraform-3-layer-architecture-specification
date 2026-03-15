---
title: 워크스페이스 규약
doc_section: conventions
nav_parent: conventions-index
nav_order: 5
---

# 워크스페이스 규약

## 설계 원칙

- 워크스페이스는 Layer와 분리해서 설계한다.
- 리소스 세트를 먼저 정의하고 필요 시 내부 분리를 검토한다.
- 고위험 resource body와 churn이 높은 바인딩은 변경 특성이 다르면 분리한다.
- 게시는 namespace보다 계약 ownership과 마이그레이션 경계를 기준으로 둔다.
- 서비스 런타임은 가능한 한 독립 배포 가능해야 한다.
- 규모가 작고 변경 특성이 유사하면 하나의 리소스 세트를 하나의 워크스페이스로 함께 둘 수 있다.

## 이름 규약

권장 패턴:

`<layer>-<domain>-<role>`

예:

- `foundation-network-core`
- `user-db`
- `user-db-게시`
- `service-orders-runtime`

역할 suffix 권장:

- `core`
- `바인딩`
- `게시`
- `runtime`

## 같은 워크스페이스에 둘 수 있는 경우

- 항상 함께 변경됨
- ownership 동일
- apply 주체 동일
- 영향 범위 차이 작음
- access rule 변경이 드묾
- 게시 변경이 primary resource와 사실상 같은 수명주기를 가짐

대표 예:

- `user-db` cluster + SG allowlist + SSM 게시
- `shared-storage` bucket + bucket policy 바인딩 + output 게시
- `shared-cache` cluster + ingress allowlist + endpoint 게시

## 분리해야 하는 신호

- access rule 변경이 잦음
- consumer onboarding이 잦음
- rollback 위험이 다름
- downstream dependency가 많음
- shared primary resource와 서비스별 바인딩이 섞여 있음
- 게시 contract를 독립적으로 versioning하거나 마이그레이션해야 함

## 빠른 판단 규칙

- "함께 자주 바뀌면 함께 둘 수 있다"
- "consumer onboarding이 잦으면 바인딩 분리를 먼저 본다"
- "contract 마이그레이션이 보이면 게시 분리를 본다"
- "rollback 단위가 다르면 워크스페이스를 분리한다"


