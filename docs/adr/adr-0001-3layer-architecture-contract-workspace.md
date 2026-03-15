# ADR-0001: 3-Layer Architecture and Contract / Workspace Model

원문 ADR:

- [Root ADR](../../adr-3layer-architecture-contract-workspace.md)

## 제목

3-Layer Architecture에서 Layer, Contract, Workspace 역할과 ownership 규칙 정의

## 상태

Proposed

## 요약

이 ADR은 다음 결정을 기록합니다.

- Layer의 ownership과 dependency direction을 정의한다.
- Workspace를 Layer와 별개의 운영 단위로 본다.
- 모든 레이어 전달값을 Contract로 간주한다.
- Contract ownership은 provider가 가진다.
- Implementation Value와 Contract Value를 구분한다.
- Shared Resource는 Resource Set 단위로 우선 설명하고, 내부 분리는 blast radius 기준으로 선택한다.
- 기존 자산은 legacy로 허용한다.

## 영향 받은 참고 자료

이 ADR은 HashiCorp 자료인 [Happy Terraforming! Real-world experience and proven best practices](https://www.hashicorp.com/en/resources/terraforming-real-world-experience-best-practices)를 중요한 참고 자료로 사용합니다.

이 저장소의 ADR은 이를 그대로 복제하지 않고 `Foundation / Platform / Service`, `Contract`, `Workspace`, `Resource Set` 개념으로 확장해 재정의합니다.

## 상세 기록

상세한 배경과 예시는 아래 원문 ADR을 참조합니다.

- [adr-3layer-architecture-contract-workspace.md](../../adr-3layer-architecture-contract-workspace.md)
