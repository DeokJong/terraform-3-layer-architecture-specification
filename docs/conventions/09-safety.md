---
title: 안전성 규약
doc_section: conventions
nav_parent: conventions-index
nav_order: 10
---

# Safety Convention

## 변경 안전성

- implementation change와 contract change를 구분한다.
- Active 계약은 마이그레이션 없이 직접 교체하지 않는다.
- breaking change는 병행 게시 후 전환한다.

## 영향 범위 제어

- core stability와 access churn이 다르면 분리 검토한다.
- service onboarding 때문에 shared core workspace를 반복 수정하지 않는다.
- 게시 convenience 때문에 source of truth ownership을 흐리지 않는다.

## rollback 가능성

- workspace는 rollback 단위로 설명 가능해야 한다.
- access 변경 실패가 core resource 변경으로 이어지지 않아야 한다.
- Consumer 마이그레이션 실패 시 기존 계약을 유지할 수 있어야 한다.

## 안전성 anti-pattern

- active 계약을 마이그레이션 없이 in-place 변경
- 공유 리소스 allowlist 변경 때문에 core 전체 apply 필요
- 서비스 하나의 실패가 shared platform core 변경으로 전파
- aggregation output만 남고 실제 provider contract가 흐려지는 구조


