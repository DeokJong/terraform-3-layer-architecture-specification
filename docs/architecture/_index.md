---
title: 아키텍처
description: 3계층 Terraform 모델의 구조, 책임, 참조 규칙, workspace 분리 기준을 설명하는 기술 명세 섹션입니다.
hero_kicker: Section Overview
doc_section: architecture
nav_key: architecture-index
nav_title: 개요
nav_order: 1
---

# 아키텍처

이 섹션은 3계층 Terraform 구조의 아키텍처 기술 명세입니다.

## 이 섹션의 목적

- 구조를 설명한다.
- 책임 경계를 정의한다.
- 계약와 워크스페이스를 어떻게 다뤄야 하는지 명확히 한다.
- 안전성과 운영 관점까지 포함해 설계 판단 기준을 제공한다.

## 권장 읽기 순서

1. [개요](./01-overview.md)
2. [계층](./02-layers.md)
3. [계약](./03-contracts.md)
4. [소유권과 참조](./04-ownership-and-references.md)
5. [워크스페이스 모델](./05-workspace-model.md)
6. [공유 리소스](./06-shared-resources.md)
7. [서비스 의존성](./07-service-dependencies.md)
8. [운영](./08-operations.md)
9. [안전성과 복원력](./09-safety-and-resilience.md)
10. [의사결정 체크리스트](./10-decision-checklist.md)
11. [용어 참고](./01a-glossary-and-views.md)
12. [공유 리소스 설계 템플릿](./11-shared-resource-design-template.md)
13. [마이그레이션과 롤아웃 시나리오](./12-마이그레이션-and-rollout-scenarios.md)

## 어떻게 읽으면 좋은가

- 처음 읽는다면 [개요](./01-overview.md)에서 그림과 핵심 원칙을 먼저 잡고, [계층](./02-layers.md)과 [계약](./03-contracts.md)으로 넘어가는 흐름이 가장 자연스럽습니다.
- 설계 경계 판단이 목적이면 [소유권과 참조](./04-ownership-and-references.md)와 [워크스페이스 모델](./05-workspace-model.md)까지 연달아 읽습니다.
- 공유 capability 설계가 목적이면 [공유 리소스](./06-shared-resources.md), [서비스 의존성](./07-service-dependencies.md), [공유 리소스 설계 템플릿](./11-shared-resource-design-template.md)을 같이 봅니다.
- 운영 안정성이 목적이면 [운영](./08-operations.md), [안전성과 복원력](./09-safety-and-resilience.md), [의사결정 체크리스트](./10-decision-checklist.md)를 우선 읽습니다.
- [용어 참고](./01a-glossary-and-views.md)는 본 흐름의 필수 선행 장이 아니라, 읽다가 개념이 헷갈릴 때 찾아보는 참고 문서입니다.

## 관련 문서

- [규약](../conventions/index.md)
- [ADR](../adr/adr-0001-3layer-architecture-contract-workspace.md)

