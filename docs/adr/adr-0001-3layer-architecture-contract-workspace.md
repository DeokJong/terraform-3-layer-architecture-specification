# ADR-0001: 3-Layer Architecture and Contract / Workspace Model

원본 ADR:

- [Root ADR](../../adr-3layer-architecture-contract-workspace.md)

## 제목

3-Layer Architecture에서 Layer, Contract, Workspace의 역할과 ownership 규칙 정의

## 상태

Proposed

## 요약

이 ADR은 다음 결정을 기록합니다.

- Layer는 ownership과 dependency direction을 정의한다.
- Workspace는 Layer와 별개의 운영 단위다.
- 모든 레이어 간 전달값은 Contract로 간주한다.
- Contract ownership은 provider가 가진다.
- Implementation Value와 Contract Value를 구분한다.
- Shared resource는 Core / Access / Publication으로 분리 가능해야 한다.
- 기존 자산은 legacy로 허용한다.

## 영향 받은 참고 자료

이 ADR은 HashiCorp 자료인 [Happy Terraforming! Real-world experience and proven best practices](https://www.hashicorp.com/en/resources/terraforming-real-world-experience-best-practices)를 중요한 참고 자료로 삼습니다.

해당 자료에서 특히 영향을 받은 포인트는 다음과 같습니다.

- Terraform 코드를 레이어로 나누어 책임과 워크플로우를 분리해야 한다는 관점
- 리소스마다 lifecycle이 다르므로 코드와 실행 단위를 분리해야 한다는 관점
- monolithic Terraform 구성을 피하고 확장 가능한 구조를 가져가야 한다는 관점

이 저장소의 ADR은 이를 그대로 복제하지 않고 `Foundation / Platform / Service`, `Contract`, `Workspace`, `Core / Access / Publication` 개념으로 확장해 재정의합니다.

## 상세 기록

상세한 배경과 예시는 아래 원본 ADR을 참조합니다.

- [adr-3layer-architecture-contract-workspace.md](../../adr-3layer-architecture-contract-workspace.md)
