# Terraform 3계층 아키텍처 기술 명세서

Terraform 3-Layer 아키텍처 기술 명세서를 정리한 문서 저장소입니다.

이 저장소는 다음 세 축으로 문서를 구성합니다.

- Architecture Specification
- Conventions
- ADR

## 문서 시작점

- [GitHub Pages 문서 포털](./docs/_index.md)
- [Architecture Specification](./terraform-3-layer-architecture-specification.md)
- [Architecture Conventions](./terraform-3-layer-architecture-conventions.md)
- [아키텍처 개요](./docs/architecture/_index.md)
- [규약 개요](./docs/conventions/_index.md)
- [ADR Index](./docs/adr/_index.md)

## 문서 구조

```text
docs/
  index.md
  architecture/
  conventions/
  adr/
```

## 읽는 순서

처음 읽는 경우 아래 순서를 권장합니다.

1. [개요](./docs/architecture/01-overview.md)
2. [계층](./docs/architecture/02-layers.md)
3. [계약](./docs/architecture/03-contracts.md)
4. [워크스페이스 모델](./docs/architecture/05-workspace-model.md)
5. [안전성과 복원력](./docs/architecture/09-safety-and-resilience.md)
6. [규약 개요](./docs/conventions/_index.md)

## 문서 성격

- Architecture 문서는 구조와 책임을 설명합니다.
- Convention 문서는 구현과 운영 시 지켜야 할 규칙을 설명합니다.
- ADR은 설계 결정을 채택한 이유를 기록합니다.
