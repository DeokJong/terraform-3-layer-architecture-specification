---
title: 운영
doc_section: architecture
nav_parent: architecture-index
nav_order: 10
---

# Operations

## 변경 전파

상위 레이어 변경이 하위 레이어에 영향을 줄 수 있으면 순차적으로 Plan/Apply 해야 합니다.

원칙:

- implementation change는 가능하면 contract change를 유발하지 않아야 한다.
- contract change가 발생하면 downstream consumer 검토가 필요하다.

## Breaking Change

다음은 breaking change로 간주합니다.

- output name 변경
- parameter path 변경
- DNS name 변경
- contract meaning 변경
- Active Contract 제거

처리 원칙:

1. 새 Contract 추가
2. consumer migration
3. 기존 Contract deprecate
4. 제거

## Legacy 자산 처리

기존 운영 자산은 즉시 rename하지 않습니다.

적용 원칙:

- legacy naming이어도 ownership은 새 기준으로 해석
- 신규 리소스와 신규 Contract는 새 기준을 우선 적용
- rename보다 병행 게시와 점진 migration을 우선

## Legacy 현대화 절차

1. 현재 값이 Implementation Value인지 Contract Value인지 분류한다.
2. 실제 provider와 consumer를 식별한다.
3. 공식 Contract가 없으면 새 Contract를 정의한다.
4. consumer를 새 Contract로 전환한다.
5. 기존 직접 참조를 제거한다.

## 문서화 원칙

shared resource나 service interface를 새로 만들 때는 최소한 아래를 남깁니다.

- owner
- consumer
- contract name
- publication 방식
- breaking change 절차
- workspace 배치 이유

## 다음 문서

- [Decision Checklist](./10-decision-checklist.md)

