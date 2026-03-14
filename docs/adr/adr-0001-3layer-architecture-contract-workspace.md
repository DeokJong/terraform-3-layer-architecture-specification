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

## 상세 기록

상세한 배경과 예시는 아래 원본 ADR을 참조합니다.

- [adr-3layer-architecture-contract-workspace.md](../../adr-3layer-architecture-contract-workspace.md)
