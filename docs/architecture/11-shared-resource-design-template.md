---
title: 공유 리소스 설계 템플릿
doc_section: architecture
nav_parent: architecture-index
nav_order: 13
---

# 공유 리소스 설계 템플릿

새 공유 리소스를 설계할 때 사용하는 표준 템플릿입니다.

## 기본 기록

| 항목 | 설명 |
| --- | --- |
| 리소스 이름 | 예: `user-db` |
| 리소스 유형 | DB / Cache / Bucket / KMS / Ingress |
| 계층 | Foundation / Platform / Service |
| 소유자 | 생명주기 소유자 |
| 주요 소비자 | 주요 소비자 또는 소비자 집합 |
| 중요도 | 낮음 / 중간 / 높음 |

## 설계 결정

| 질문 | 예시 답변 |
| --- | --- |
| 왜 공유하는가 | 여러 서비스가 함께 소비하기 때문 |
| 왜 이 계층에 속하는가 | 단일 서비스 생명주기에 묶이지 않기 때문 |
| 구현으로 숨기는 것은 무엇인가 | 물리 endpoint 또는 내부 ID |
| 계약으로 게시하는 것은 무엇인가 | Stable DNS, SSM path, 표준 output |
| 바인딩은 얼마나 자주 바뀌는가 | 월간 / 주간 / 빈번 |
| 게시를 본체 리소스 세트와 분리하는가 | 예/아니오와 이유 |

## 리소스 세트 분할 계획

| 분할 단위 | 포함 리소스 | 소유자 | 변경 빈도 | 분리 판단 |
| --- | --- | --- | --- | --- |
| 본체 세트 | 본체 리소스와 밀접 결합된 구성 | 제공자 | 낮음 | 생명주기가 맞으면 함께 유지 |
| 바인딩 세트 | allowlist, 바인딩s, grants, policy attachments | 제공자 또는 접근 소유자 | 중간 또는 높음 | churn이 높으면 분리 |
| 게시 세트 | DNS, SSM, output 게시 | 제공자 | 낮음 또는 중간 | 마이그레이션 가능성이 크면 분리 |

## 계약 기록

| 계약 이름 | 유형 | 소비자 | 게시 방식 | 원천 시스템 | 안정성 |
| --- | --- | --- | --- | --- | --- |
| `db-main.internal.example.com` | Connectivity | backend services | Route53 | `user-db` | stable |
| `/backends/prod/db/primary` | Runtime | app runtime | SSM | `user-db-게시` | stable |

## 검토 질문

- 이 공유 리소스는 정말 공유 생명주기를 가지는가
- 소비자 수가 늘어나도 본체 리소스 세트는 안정적으로 유지되는가
- 바인딩 churn 때문에 본체 리소스에 반복 apply가 강제되는가
- 소비자를 깨뜨리지 않고 계약 마이그레이션을 병행할 수 있는가

## 다음

- [마이그레이션과 롤아웃 시나리오](./12-마이그레이션-and-rollout-scenarios.md)


