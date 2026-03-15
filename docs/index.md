# Terraform 3계층 아키텍처 문서 포털

이 문서는 3계층 Terraform 아키텍처를 빠르게 이해하고, 실제 설계와 운영에 바로 적용할 수 있도록 구성한 문서 포털입니다.

## 이 문서에서 찾을 수 있는 것

- 3계층 구조의 설계 원칙과 책임 분리 기준
- Layer와 Workspace를 어떻게 다르게 봐야 하는지에 대한 설명
- Contract, ownership, blast radius, 안전성 구조에 대한 기준
- 실제 구현 시 적용할 Convention과 리뷰 체크리스트
- 이 구조를 왜 채택했는지에 대한 ADR

## 핵심 챕터

처음 보는 경우 아래 챕터 순서대로 읽으면 됩니다.

1. [Overview](./architecture/01-overview.md)
2. [Glossary and Views](./architecture/01a-glossary-and-views.md)
3. [Layers](./architecture/02-layers.md)
4. [Contracts](./architecture/03-contracts.md)
5. [Workspace Model](./architecture/05-workspace-model.md)
6. [Safety and Resilience](./architecture/09-safety-and-resilience.md)
7. [Conventions Overview](./conventions/index.md)

## 문서 구역

### 1. Architecture

구조와 책임을 설명하는 기술 명세 섹션입니다.

- [Architecture Overview](./architecture/index.md)
- [Overview](./architecture/01-overview.md)
- [Glossary and Views](./architecture/01a-glossary-and-views.md)
- [Layers](./architecture/02-layers.md)
- [Contracts](./architecture/03-contracts.md)
- [Ownership and References](./architecture/04-ownership-and-references.md)
- [Workspace Model](./architecture/05-workspace-model.md)
- [Shared Resources](./architecture/06-shared-resources.md)
- [Service Dependencies](./architecture/07-service-dependencies.md)
- [Operations](./architecture/08-operations.md)
- [Safety and Resilience](./architecture/09-safety-and-resilience.md)
- [Decision Checklist](./architecture/10-decision-checklist.md)

### 2. Conventions

실제 Terraform 코드와 운영 구조에 적용할 규칙 섹션입니다.

- [Conventions Overview](./conventions/index.md)
- [Layer Classification](./conventions/01-layer-classification.md)
- [Ownership](./conventions/02-ownership.md)
- [Contracts](./conventions/03-contracts.md)
- [Workspaces](./conventions/04-workspaces.md)
- [Network and IAM](./conventions/05-network-and-iam.md)
- [Shared Resources](./conventions/06-shared-resources.md)
- [Service-to-Service](./conventions/07-service-to-service.md)
- [Legacy](./conventions/08-legacy.md)
- [Safety](./conventions/09-safety.md)
- [Review Checklist](./conventions/10-review-checklist.md)

### 3. ADR

구조를 채택한 배경과 결정 기록입니다.

- [ADR Index](./adr/index.md)
- [ADR-0001: 3-Layer Architecture and Contract / Workspace Model](./adr/adr-0001-3layer-architecture-contract-workspace.md)

### 4. Documentation System

Codex 기반 유지보수와 문서 진행 상태 추적을 위한 메타 섹션입니다.

- [Documentation System](./meta/index.md)
- [Document Registry](./meta/document-registry.json)
- [Work Index](./meta/work-index.md)

## 상황별 바로가기

### 아키텍처를 처음 이해하려는 경우

- [Overview](./architecture/01-overview.md)
- [Glossary and Views](./architecture/01a-glossary-and-views.md)
- [Layers](./architecture/02-layers.md)

### shared resource를 어디에 둘지 고민하는 경우

- [Contracts](./architecture/03-contracts.md)
- [Workspace Model](./architecture/05-workspace-model.md)
- [Shared Resources](./architecture/06-shared-resources.md)
- [Workspaces](./conventions/04-workspaces.md)

### 운영 안전성과 blast radius를 점검하려는 경우

- [Operations](./architecture/08-operations.md)
- [Safety and Resilience](./architecture/09-safety-and-resilience.md)
- [Safety](./conventions/09-safety.md)
- [Review Checklist](./conventions/10-review-checklist.md)

### 왜 이런 구조를 채택했는지 확인하려는 경우

- [ADR Index](./adr/index.md)
- [ADR-0001](./adr/adr-0001-3layer-architecture-contract-workspace.md)
