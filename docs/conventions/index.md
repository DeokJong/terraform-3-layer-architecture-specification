---
title: Conventions
description: 3계층 아키텍처를 실제 Terraform 코드와 운영 구조에 적용할 때 반복적으로 사용하는 naming, ownership, contract, workspace 규칙입니다.
hero_kicker: Section Overview
doc_section: conventions
nav_key: conventions-index
nav_title: Overview
nav_order: 1
---

# Conventions

이 섹션은 3계층 아키텍처를 실제 Terraform 코드와 운영 구조에 적용할 때 따라야 하는 규칙을 정리합니다.

## 이 섹션의 목적

- 아키텍처 문서를 실제 구현 규칙으로 번역한다.
- naming, ownership, contract, workspace 설계 기준을 일관되게 만든다.
- 리뷰와 운영 시 반복적으로 확인할 기준을 제공한다.

## 챕터

1. [Layer Classification](./01-layer-classification.md)
2. [Ownership](./02-ownership.md)
3. [Contracts](./03-contracts.md)
4. [Workspaces](./04-workspaces.md)
5. [Network and IAM](./05-network-and-iam.md)
6. [Shared Resources](./06-shared-resources.md)
7. [Service-to-Service](./07-service-to-service.md)
8. [Legacy](./08-legacy.md)
9. [Safety](./09-safety.md)
10. [Review Checklist](./10-review-checklist.md)
11. [Concrete Examples](./11-concrete-examples.md)

## 어떻게 읽으면 좋은가

- 새 workspace나 shared capability를 만들 때는 [Layer Classification](./01-layer-classification.md), [Ownership](./02-ownership.md), [Workspaces](./04-workspaces.md)를 먼저 봅니다.
- contract naming과 publication이 고민되면 [Contracts](./03-contracts.md), [Service-to-Service](./07-service-to-service.md)를 함께 봅니다.
- 네트워크와 IAM 경계는 [Network and IAM](./05-network-and-iam.md), 레거시 전환은 [Legacy](./08-legacy.md)를 기준으로 판단합니다.
- 리뷰 전에는 [Review Checklist](./10-review-checklist.md)와 [Concrete Examples](./11-concrete-examples.md)로 최종 점검합니다.
