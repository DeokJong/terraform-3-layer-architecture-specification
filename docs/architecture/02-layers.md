---
title: 계층
doc_section: architecture
nav_parent: architecture-index
nav_order: 4
---

# 계층

이 장은 "이 리소스는 어느 Layer에 속하는가"를 판단하기 위한 기준을 설명합니다. 배포 위치보다 ownership과 dependency 방향을 먼저 결정하는 장입니다.

## 이 장이 답하는 질문

- 이 리소스는 Foundation, Platform, Service 중 어디에 두어야 하는가
- 어떤 Layer가 어떤 Layer의 Contract를 참조할 수 있는가
- shared capability와 service-specific implementation을 어디서 갈라야 하는가

## 계층 개요

| Layer | 역할 | 주된 책임 | 참조 가능 대상 |
| --- | --- | --- | --- |
| Foundation | 기반 인프라 제공 | 네트워크, 전역 기반 자원, 공통 토대 | 없음 |
| Platform | shared capability 제공 | 공유 런타임, 공유 데이터, 공용 인터페이스 | Foundation |
| Service | 서비스 제공 | 서비스별 배포, 설정, 권한, 엔드포인트 | Foundation, Platform |

## 의존 방향

논리적 의존 방향:

`Foundation <- Platform <- Service`

참조 허용 방향:

- Platform은 Foundation을 참조할 수 있다.
- Service는 Foundation과 Platform을 참조할 수 있다.
- Foundation은 Platform 또는 Service를 참조하지 않는다.
- Platform은 Service의 내부 구현값을 참조하지 않는다.

## Foundation 계층

주요 책임:

- 네트워크와 전역 공통 기반 제공
- 환경 초기 구성
- 변경 빈도가 낮고 다수 consumer가 의존하는 기반 자원 관리

대표 리소스:

- VPC / Subnet
- Route Table / NAT / IGW
- Route53 Hosted Zone
- 공용 KMS Key
- 공용 NACL

판단 기준:

- 여러 상위 레이어가 넓게 참조한다.
- 자주 변경되지 않는다.
- 특정 서비스 lifecycle에 종속되지 않는다.

## Platform 계층

주요 책임:

- shared runtime 제공
- shared data service 제공
- shared ingress, DNS, storage, cluster 같은 공용 인터페이스 제공

대표 리소스:

- ECS / EKS Cluster
- Shared ALB / NLB
- RDS / ElastiCache / Kafka
- Shared S3 / ECR / Log Group
- internal shared DNS endpoint

판단 기준:

- 여러 서비스가 공통으로 소비한다.
- provider로서 안정된 Contract를 게시한다.
- 서비스 개별 구현 세부사항을 일반 리소스 관리 목적으로 알지 않아야 한다.

예외:

- producer-side access control을 위한 최소 식별자(Client SG, Role ARN, principal)는 참조할 수 있다.

## Service 계층

주요 책임:

- 서비스 배포와 운영
- 서비스 전용 설정과 권한 관리
- 서비스 전용 endpoint와 runtime dependency 연결

대표 리소스:

- ECS Service / Lambda / application stack
- service-specific S3
- service-specific Route53 Record
- service-specific Secret / Parameter
- service IAM Role / Security Group / ALB

판단 기준:

- 특정 서비스 lifecycle과 함께 변경된다.
- 다른 서비스에 대한 일반 shared capability가 아니다.
- 독립 배포와 독립 롤백이 중요하다.

## 다음 문서

- [계약](./03-contracts.md)

