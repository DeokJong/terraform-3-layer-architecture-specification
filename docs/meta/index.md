# Documentation System

이 섹션은 이 저장소의 문서 시스템 자체를 유지하기 위한 메타 문서입니다.

## 핵심 파일

- [Document Registry](./document-registry.json)
- [Work Index](./work-index.md)

## 역할

- 어떤 문서가 canonical source인지 추적합니다.
- 현재 어떤 문서가 안정 상태인지, 보강이 필요한지 표시합니다.
- 다음에 어떤 문서를 강화해야 하는지 작업 순서를 보여줍니다.
- Codex가 문서를 강화할 때 어디부터 읽고 어디를 수정해야 하는지 기준을 제공합니다.

## 유지보수 원칙

1. 문서 구조나 상태를 바꿀 때는 먼저 `document-registry.json`을 갱신합니다.
2. 그 다음 `work-index.md`를 다시 생성합니다.
3. 마지막으로 실제 문서 본문과 portal navigation을 맞춥니다.
