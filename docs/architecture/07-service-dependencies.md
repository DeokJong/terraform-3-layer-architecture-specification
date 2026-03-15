---
title: 서비스 의존성
doc_section: architecture
nav_parent: architecture-index
nav_order: 9
---

# 서비스 의존성

이 장은 "서비스끼리 완전히 단절해야 하는가"가 아니라 "서비스 간 의존이 필요할 때 무엇만 의존할 수 있는가"를 설명합니다. Service 간 연결이 필요해도 implementation reference는 금지하고, published Contract만 허용합니다.

## 이 장이 답하는 질문

- Service A가 Service B를 필요로 할 때 무엇을 참조할 수 있는가
- SSR frontend처럼 backend endpoint가 필요한 경우 어떤 형태가 허용되는가
- service-to-service dependency가 shared Platform capability와 어떻게 다른가

## 기본 원칙

Service는 다른 Service의 implementation을 직접 참조하지 않습니다.

허용:

- 상대 서비스가 게시한 stable API hostname
- 상대 서비스가 게시한 공식 Contract

금지:

- 상대 서비스 ALB physical DNS 직접 사용
- 상대 서비스 Secret path 직접 참조
- 상대 서비스 내부 queue, topic, bucket path 직접 의존

## 서비스 간 의존 방식

provider 역할을 가진 서비스가 Contract를 게시하고, consumer는 그 Contract만 참조합니다.

## 중개 레이어 사용 원칙

Platform이 service-to-service 호출을 중개할 수는 있지만, 그 사실만으로 endpoint ownership이 Platform으로 이동하지는 않습니다.

구분:

- transport 또는 routing을 제공하는 shared platform
- business capability를 제공하는 service contract

예:

- shared ingress 아래에 있어도 `orders-api.internal.example.com`의 의미와 lifecycle이 Orders에 귀속되면 owner는 Orders Service입니다.

## 흔한 오해

- shared infra 위에 올라가 있으면 무조건 Platform ownership이다.
- SSM에 있으므로 SSM 값을 만든 consumer가 owner다.
- 다른 서비스가 많이 쓰면 무조건 Platform으로 승격해야 한다.
- shared resource는 처음부터 무조건 Core / Access / Publication을 나눠야 한다.

## 다음 문서

- [운영](./08-operations.md)

