---
title: Architecture
description: 3계층 Terraform 모델의 구조, 책임, 참조 규칙, workspace 분리 기준을 설명하는 기술 명세 섹션입니다.
hero_kicker: Section Overview
doc_section: architecture
nav_key: architecture-index
nav_title: Overview
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

1. [Overview](./01-overview.md)
2. [Glossary and Views](./01a-glossary-and-views.md)
3. [Layers](./02-layers.md)
4. [Contracts](./03-contracts.md)
5. [Ownership and References](./04-ownership-and-references.md)
6. [Workspace Model](./05-workspace-model.md)
7. [Shared Resources](./06-shared-resources.md)
8. [Service Dependencies](./07-service-dependencies.md)
9. [Operations](./08-operations.md)
10. [Safety and Resilience](./09-safety-and-resilience.md)
11. [Decision Checklist](./10-decision-checklist.md)
12. [Shared Resource Design Template](./11-shared-resource-design-template.md)
13. [Migration and Rollout Scenarios](./12-migration-and-rollout-scenarios.md)

## 어떻게 읽으면 좋은가

- 구조 개요부터 보려면 [Overview](./01-overview.md)와 [Glossary and Views](./01a-glossary-and-views.md)부터 읽습니다.
- 설계 경계 판단이 목적이면 [Contracts](./03-contracts.md), [Ownership and References](./04-ownership-and-references.md), [Workspace Model](./05-workspace-model.md)을 먼저 봅니다.
- 운영 안정성이 목적이면 [Operations](./08-operations.md)와 [Safety and Resilience](./09-safety-and-resilience.md)를 우선 읽습니다.
- 새 shared capability를 설계하려면 [Shared Resource Design Template](./11-shared-resource-design-template.md)와 [Migration and Rollout Scenarios](./12-migration-and-rollout-scenarios.md)를 같이 봅니다.

## 관련 문서

- [Conventions](../conventions/index.md)
- [ADR](../adr/adr-0001-3layer-architecture-contract-workspace.md)
