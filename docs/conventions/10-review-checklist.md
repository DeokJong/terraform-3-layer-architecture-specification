---
title: 리뷰 체크리스트
doc_section: conventions
nav_parent: conventions-index
nav_order: 11
---

# 검토 체크리스트

리소스나 계약 추가 시 아래를 확인합니다.

- 이 리소스는 어느 Layer owner인가
- 이 값은 계약인가 구현값인가
- consumer가 아니라 provider가 owner로 표현되었는가
- 워크스페이스 분리가 영향 범위를 줄이는가
- 공유 리소스의 core와 access가 불필요하게 섞여 있지 않은가
- legacy naming이 필요하더라도 의미 해석은 새 기준을 따르는가
- 실패 시 rollback과 병행 마이그레이션이 가능한가


