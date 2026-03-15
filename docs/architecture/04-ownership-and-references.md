---
title: 소유권과 참조
doc_section: architecture
nav_parent: architecture-index
nav_order: 6
---

# 소유권과 참조

이 장은 "누가 무엇의 owner인가"와 "누가 누구를 어떤 방식으로 참조할 수 있는가"를 결정합니다. 리소스가 어디에 저장되어 있는지보다 누가 lifecycle과 호환성을 책임지는지가 더 중요하다는 점을 분명히 합니다.

## 이 장이 답하는 질문

- ownership은 배치 위치가 아니라 어떤 기준으로 결정되는가
- Contract owner와 consumer는 각각 무엇을 책임지는가
- 어떤 cross-layer reference는 허용되고 어떤 것은 금지되는가
- access control 예외는 어디까지 허용되는가

## 리소스 소유권 판단 기준

리소스 ownership은 배치 편의가 아니라 lifecycle과 운영 책임을 기준으로 판단합니다.

owner의 책임:

- 생성
- 변경
- 삭제
- 정책 관리
- 인터페이스 안정성 관리
- 호환성 관리

## 계약 소유권

Contract ownership은 다음으로 결정하지 않습니다.

- 누가 읽는가
- 어디에 저장되는가
- 어떤 도구로 전달되는가

Contract ownership은 아래 기준으로 결정합니다.

- 누가 해당 리소스 또는 인터페이스를 제공하는가
- 누가 그 의미를 정의하는가
- 누가 안정성과 호환성을 보장하는가

예:

- `db-main.internal.example.com`을 backend가 읽더라도 owner는 backend가 아니라 DB provider다.
- SSM parameter에 저장된 secret reference를 서비스가 소비하더라도, secret 의미와 rotation을 Platform이 관리하면 owner는 Platform이다.
- Hosted Zone이 Foundation에 있어도 개별 record contract의 owner는 Platform 또는 Service일 수 있다.

## 허용되는 참조

- Service → Platform Contract
- Service → Foundation Contract
- Platform → Foundation Contract
- producer-side access control을 위한 최소 식별자 참조

## 금지되는 참조

- Foundation → Platform 또는 Service 참조
- Platform → Service 내부 구현 참조
- Service A → Service B 내부 구현 참조
- 순환 참조

## 예외: 접근 제어

다음은 제한적으로 허용합니다.

- SG ingress allowlist
- bucket policy binding
- KMS grant / key policy binding
- role trust policy consumer binding

단, core lifecycle과 access lifecycle은 가능하면 분리합니다.

## 금지되는 설계 습관

- 하위 레이어가 상위 레이어의 물리 리소스명을 직접 조합해 쓰는 것
- consumer가 provider contract를 우회해 내부 output을 직접 읽는 것
- temporary migration output을 영구 인터페이스처럼 사용하는 것
- shared resource onboarding 때문에 core workspace를 계속 수정하는 것

## 다음 문서

- [워크스페이스 모델](./05-workspace-model.md)

