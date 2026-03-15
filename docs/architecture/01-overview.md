---
title: Overview
doc_section: architecture
nav_parent: architecture-index
nav_order: 2
---

# Overview

## 목적

이 문서는 Terraform 기반 인프라를 `Foundation`, `Platform`, `Service`의 3개 레이어로 설계하고 운영하기 위한 아키텍처 기준을 정의합니다.

주요 목표는 다음과 같습니다.

- 레이어별 책임과 ownership 명확화
- 레이어 간 의존 방향 통제
- Contract 중심 연결 방식 표준화
- Workspace 분리 원칙 정의
- shared resource 운영 모델 정리

## 범위

포함 대상:

- Terraform으로 관리되는 AWS 인프라
- shared infrastructure와 service-specific infrastructure
- 레이어 간 전달값과 참조 모델
- Terraform Workspace 설계 원칙

비포함 대상:

- 애플리케이션 내부 구현
- 배포 파이프라인 상세 절차
- 모듈 내부 세부 구현

## 비목표

- 기존 운영 자산의 이름과 경로를 즉시 전면 변경하는 일
- 모든 shared resource를 무조건 Platform으로 승격하는 일
- Layer와 Workspace를 1:1로 강제하는 일
- 구현 편의를 위해 레이어 간 직접 참조를 폭넓게 허용하는 일

## 대상 독자

- Terraform workspace를 설계하는 엔지니어
- shared infrastructure를 운영하는 플랫폼 엔지니어
- 서비스 인프라를 설계하거나 소비하는 서비스 개발팀

## 설계 원칙

- Layer는 ownership 모델이다.
- Dependency는 단방향이어야 한다.
- 하위 레이어는 Contract만 소비한다.
- Contract ownership은 provider에게 있다.
- Workspace는 운영 단위다.
- shared resource는 필요 시 분리할 수 있는 구조여야 한다.

작은 규모에서는 core, access, publication을 하나의 workspace에서 함께 운영할 수 있습니다. 다만 변경 churn과 blast radius가 커질 때 분리할 수 있어야 합니다.

## 다음 문서

- [Glossary and Views](./01a-glossary-and-views.md)

