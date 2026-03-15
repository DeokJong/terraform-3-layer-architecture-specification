---
title: 규약
description: 3계층 아키텍처를 실제 Terraform 코드와 운영 구조에 적용할 때 반복적으로 사용하는 naming, ownership, contract, workspace 규칙입니다.
hero_kicker: Section Overview
doc_section: conventions
nav_key: conventions-index
nav_title: 개요
nav_order: 1
---

# 규약

이 섹션은 3계층 아키텍처를 실제 Terraform 코드와 운영 구조에 적용할 때 따라야 하는 규칙을 정리합니다.

## 이 섹션의 목적

- 아키텍처 문서를 실제 구현 규칙으로 번역한다.
- naming, ownership, contract, workspace 설계 기준을 일관되게 만든다.
- 리뷰와 운영 시 반복적으로 확인할 기준을 제공한다.

## 챕터

1. [레이어 분류](./01-layer-classification.md)
2. [소유권](./02-ownership.md)
3. [계약](./03-contracts.md)
4. [워크스페이스](./04-workspaces.md)
5. [네트워크와 IAM](./05-network-and-iam.md)
6. [공유 리소스](./06-shared-resources.md)
7. [서비스 간 통신](./07-service-to-service.md)
8. [레거시](./08-legacy.md)
9. [안전성](./09-safety.md)
10. [리뷰 체크리스트](./10-review-checklist.md)
11. [구체 예시](./11-concrete-examples.md)

## 어떻게 읽으면 좋은가

- 새 워크스페이스나 공유 capability를 만들 때는 [계층 분류](./01-layer-classification.md), [소유권](./02-ownership.md), [워크스페이스](./04-workspaces.md)를 먼저 봅니다.
- 계약 이름과 게시 방식이 고민되면 [계약](./03-contracts.md), [서비스 간 의존](./07-service-to-service.md)를 함께 봅니다.
- 네트워크와 IAM 경계는 [네트워크와 IAM](./05-network-and-iam.md), 레거시 전환은 [레거시](./08-legacy.md)를 기준으로 판단합니다.
- 리뷰 전에는 [검토 체크리스트](./10-review-checklist.md)와 [구체적 예시](./11-concrete-examples.md)로 최종 점검합니다.

