---
title: 의사결정 체크리스트
doc_section: architecture
nav_parent: architecture-index
nav_order: 12
---

# 의사결정 체크리스트

새 리소스 또는 Contract 추가 시 아래 순서로 판단합니다.

1. 누구 lifecycle과 함께 움직이는가
2. Foundation / Platform / Service 중 어디에 속하는가
3. 어떤 Resource Set capability에 속하는가
4. Implementation Value인가, Contract Value인가
5. Contract라면 provider는 누구인가
6. 변경 빈도와 blast radius가 달라 Workspace 분리가 필요한가

## 관련 문서

- [안전성과 복원력](./09-safety-and-resilience.md)
- [규약 개요](../conventions/)
- [ADR-0001](../adr/adr-0001-3layer-architecture-contract-workspace.md)

