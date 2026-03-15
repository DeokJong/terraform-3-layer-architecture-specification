---
title: 공유 리소스 규약
doc_section: conventions
nav_parent: conventions-index
nav_order: 7
---

# Shared Resource Convention

## Resource Set 우선 규칙

shared resource는 먼저 하나의 Resource Set으로 정의합니다. Resource Set은 하나의 명확한 shared capability를 제공하는 리소스 묶음입니다.

권장 예:

- `user-db`
- `book-db`
- `finance-db`
- `shared-cache`
- `shared-ingress`

문서와 설계 검토에서는 가능하면 shared resource를 먼저 Resource Set으로 설명합니다.

## 내부 분리 판단 기준

Resource Set 내부는 다음 기준이 있을 때 분리를 검토합니다.

- blast radius 차이가 큰가
- 변경 빈도가 크게 다른가
- ownership 또는 승인 절차가 다른가
- rollback 경계가 다른가
- publication churn이 core 안정성에 영향을 주는가

위 조건이 약하면 하나의 Resource Set 또는 하나의 workspace로 유지할 수 있습니다.

## Core / Access / Publication은 선택 패턴

`Core / Access / Publication`은 Resource Set 내부를 설명하는 대표 패턴으로 사용합니다.

- Core: 본체 리소스
- Access: allowlist, attachment, grant, policy binding
- Publication: consumer-facing contract

모든 shared resource에 이 3분할을 강제하지는 않습니다.

## 대표 적용 예

DB Resource Set:

- `user-db`
- 필요 시 `user-db-core`, `user-db-access`, `user-db-publication`

Storage Resource Set:

- `shared-storage`
- 필요 시 `shared-storage-core`, `shared-storage-access`, `shared-storage-publication`

Redis Resource Set:

- `shared-cache`
- 필요 시 `shared-cache-core`, `shared-cache-access`, `shared-cache-publication`

