---
title: 계약 규약
doc_section: conventions
nav_parent: conventions-index
nav_order: 4
---

# 계약 규약

## 설계 원칙

- 하위 레이어는 Contract만 소비한다.
- Implementation Value는 직접 노출하지 않는다.
- Contract는 의미가 안정적이어야 한다.
- Contract owner는 provider다.

## 게시 수단

- Terraform output
- SSM Parameter
- Route53 Record
- Secrets Manager reference

게시 수단은 ownership을 바꾸지 않습니다.

## 이름 규약

원칙:

- 의미 중심 이름을 사용한다.
- 구현 세부사항보다 소비 목적이 드러나야 한다.
- 변경에 강한 stable name을 우선한다.

권장 예:

- `db-main.internal.example.com`
- `/platform/orders/db/host`
- `orders-api.internal.example.com`
- `platform_db_primary_endpoint`

## 생명주기 규약

- 신규는 `Draft` 또는 `Active`로 시작한다.
- breaking change 시 새 Contract를 병행 게시한다.
- 기존 Contract는 `Deprecated` 단계를 거친다.
- consumer 전환 후 제거한다.

## 문서화 규약

각 Contract는 가능하면 아래를 남깁니다.

- Contract 이름
- 타입
- provider
- 주요 consumer
- publication 방식
- source of truth
- breaking change 절차

