---
title: ADR-0001
description: 3계층 Terraform 구조와 contract/workspace 모델을 채택한 배경, 기대효과, trade-off를 기록한 ADR입니다.
hero_kicker: Architecture Decision Record
doc_section: adr
nav_parent: adr-index
nav_order: 2
nav_title: ADR-0001
---

# ADR-0001: 3-Layer Architecture and 계약 / 워크스페이스 Model

원문 ADR:

- [Root ADR](../../adr-3layer-architecture-contract-workspace.md)

## 제목

3-Layer Architecture에서 Layer, 계약, 워크스페이스 역할과 ownership 규칙 정의

## 상태

Accepted

## 요약

이 ADR은 다음 결정을 기록합니다.

- Layer의 ownership과 dependency direction을 정의한다.
- 워크스페이스를 Layer와 별개의 운영 단위로 본다.
- 모든 레이어 전달값을 계약로 간주한다.
- 계약 ownership은 provider가 가진다.
- 구현값와 계약 Value를 구분한다.
- Shared Resource는 Resource Set 단위로 우선 설명하고, 내부 분리는 영향 범위 기준으로 선택한다.
- 기존 자산은 legacy로 허용한다.

이 결정은 다음 운영 문제를 해결하기 위한 배경에서 출발합니다.

- 모놀로식 Terraform 워크스페이스에 리소스가 과도하게 집약되어 lock 경합이 심하다.
- 한 환경에서 PR 하나가 lock을 잡으면 다른 PR은 Plan조차 수행하지 못한다.
- SSM Parameter처럼 리소스 수가 많은 영역은 Plan만으로도 약 5분이 걸릴 수 있다.
- Lambda는 SLS Stack으로 별도 관리되고 있어 Terraform 구조와 관리 주제가 이미 분리되어 있다.

## 영향 받은 참고 자료

이 ADR은 HashiCorp 자료인 [Happy Terraforming! Real-world experience and proven best practices](https://www.hashicorp.com/en/resources/terraforming-real-world-experience-best-practices)를 중요한 참고 자료로 사용합니다.

이 저장소의 ADR은 이를 그대로 복제하지 않고 현재 운영 문제를 설명할 수 있도록 `Foundation / Platform / Service`, `계약`, `워크스페이스`, `Resource Set` 개념으로 확장해 재정의합니다.

## 상세 기록

상세한 배경과 예시는 아래 원문 ADR을 참조합니다.

- [adr-3layer-architecture-contract-workspace.md](../../adr-3layer-architecture-contract-workspace.md)


