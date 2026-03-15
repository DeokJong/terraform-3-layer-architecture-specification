---
title: 아키텍처
description: 3계층 Terraform 모델의 구조, 책임, 참조 규칙, workspace 분리 기준을 설명하는 기술 명세 섹션입니다.
hero_kicker: Section Overview
doc_section: architecture
nav_key: architecture-index
nav_title: 개요
nav_order: 1
---

# Architecture

이 섹션은 3계층 Terraform 구조의 아키텍처 기술 명세입니다.

## 이 섹션의 목적

- 구조를 설명한다.
- 책임 경계를 정의한다.
- Contract와 Workspace를 어떻게 다뤄야 하는지 명확히 한다.
- 안전성과 운영 관점까지 포함해 설계 판단 기준을 제공한다.

## 챕터

1. [개요](./01-overview.md)
2. [용어집과 뷰](./01a-glossary-and-views.md)
3. [계층](./02-layers.md)
4. [계약](./03-contracts.md)
5. [소유권과 참조](./04-ownership-and-references.md)
6. [워크스페이스 모델](./05-workspace-model.md)
7. [공유 리소스](./06-shared-resources.md)
8. [서비스 의존성](./07-service-dependencies.md)
9. [운영](./08-operations.md)
10. [안전성과 복원력](./09-safety-and-resilience.md)
11. [의사결정 체크리스트](./10-decision-checklist.md)
12. [공유 리소스 설계 템플릿](./11-shared-resource-design-template.md)
13. [마이그레이션과 롤아웃 시나리오](./12-migration-and-rollout-scenarios.md)

## 어떻게 읽으면 좋은가

- 구조 개요부터 보려면 [개요](./01-overview.md)와 [용어집과 뷰](./01a-glossary-and-views.md)부터 읽습니다.
- 설계 경계 판단이 목적이면 [계약](./03-contracts.md), [소유권과 참조](./04-ownership-and-references.md), [워크스페이스 모델](./05-workspace-model.md)을 먼저 봅니다.
- 운영 안정성이 목적이면 [운영](./08-operations.md)와 [안전성과 복원력](./09-safety-and-resilience.md)를 우선 읽습니다.
- 새 shared capability를 설계하려면 [공유 리소스 설계 템플릿](./11-shared-resource-design-template.md)와 [마이그레이션과 롤아웃 시나리오](./12-migration-and-rollout-scenarios.md)를 같이 봅니다.

## 관련 문서

- [규약](../conventions/index.md)
- [ADR](../adr/adr-0001-3layer-architecture-contract-workspace.md)
