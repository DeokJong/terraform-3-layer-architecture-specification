---
title: Terraform 3계층 아키텍처 문서 포털
description: 3-layer Terraform architecture의 구조, 운영 규칙, ADR, 유지보수 체계를 한 흐름으로 읽기 위한 문서 포털입니다.
hero_kicker: Documentation Portal
page_kind: portal-home
nav_title: 홈
nav_order: 1
---

이 포털은 `Foundation`, `Platform`, `Service` 3계층 모델을 문서 중심으로 설명합니다. 설계 원칙, 운영 규칙, 예시, ADR, 문서 유지보수 체계를 같은 source of truth 위에서 읽을 수 있도록 구성했습니다.

## 시작 경로

처음 읽는 경우 아래 순서로 보면 전체 맥락이 빠르게 잡힙니다.

1. [개요](./architecture/01-overview.md)
2. [계층](./architecture/02-layers.md)
3. [계약](./architecture/03-contracts.md)
4. [워크스페이스 모델](./architecture/05-workspace-model.md)
5. [안전성과 복원력](./architecture/09-safety-and-resilience.md)
6. [규약](./conventions/_index.md)

## 주요 섹션

<div class="home-grid">
  <section class="home-card">
    <h3><a href="./architecture/">아키텍처</a></h3>
    <p>Layer, Contract, ownership, workspace, shared resource, 안전성 구조를 정의하는 기술 명세 섹션입니다.</p>
    <ul>
      <li><a href="./architecture/03-contracts/">계약</a></li>
      <li><a href="./architecture/05-workspace-model/">워크스페이스 모델</a></li>
      <li><a href="./architecture/09-safety-and-resilience/">안전성과 복원력</a></li>
    </ul>
  </section>
  <section class="home-card">
    <h3><a href="./conventions/">규약</a></h3>
    <p>실제 Terraform 구조와 리뷰에서 반복 적용할 naming, ownership, workspace 규칙을 정리합니다.</p>
    <ul>
      <li><a href="./conventions/04-workspaces/">워크스페이스 규약</a></li>
      <li><a href="./conventions/06-shared-resources/">공유 리소스 규약</a></li>
      <li><a href="./conventions/10-review-checklist/">리뷰 체크리스트</a></li>
    </ul>
  </section>
  <section class="home-card">
    <h3><a href="./adr/">ADR</a></h3>
    <p>왜 이 구조를 채택했는지, 어떤 문제를 줄이려는지에 대한 의사결정 배경을 기록합니다.</p>
    <ul>
      <li><a href="./adr/adr-0001-3layer-architecture-contract-workspace/">ADR-0001</a></li>
    </ul>
  </section>
  <section class="home-card">
    <h3><a href="./meta/">문서 시스템</a></h3>
    <p>문서 레지스트리, work index, agent guidance처럼 문서 유지보수 체계를 관리하는 메타 영역입니다.</p>
    <ul>
      <li><a href="./meta/work-index/">작업 인덱스</a></li>
      <li><a href="./meta/agent-instructions/">에이전트 지침 원본</a></li>
      <li><a href="./meta/document-registry.json">문서 레지스트리</a></li>
    </ul>
  </section>
</div>

## 상황별 진입점

### 아키텍처 구조를 먼저 이해하려는 경우

- [개요](./architecture/01-overview.md)
- [계층](./architecture/02-layers.md)
- [용어 참고](./architecture/01a-glossary-and-views.md)

### shared resource와 contract 경계를 판단하려는 경우

- [계약](./architecture/03-contracts.md)
- [공유 리소스](./architecture/06-shared-resources.md)
- [워크스페이스 규약](./conventions/04-workspaces.md)

### 운영 안전성과 blast radius를 점검하려는 경우

- [운영](./architecture/08-operations.md)
- [안전성과 복원력](./architecture/09-safety-and-resilience.md)
- [안전성 규약](./conventions/09-safety.md)

### 문서 체계 자체를 유지보수하려는 경우

- [문서 시스템](./meta/_index.md)
- [작업 인덱스](./meta/work-index.md)
- [에이전트 지침 원본](./meta/agent-instructions.md)
