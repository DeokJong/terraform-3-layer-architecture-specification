---
title: Ownership Convention
doc_section: conventions
nav_parent: conventions-index
nav_order: 3
---

# Ownership Convention

## ownership 판단 규칙

다음 질문에 가장 강하게 연결되는 레이어가 owner입니다.

1. 누가 lifecycle을 관리하는가
2. 누가 변경 책임을 지는가
3. 누가 인터페이스 안정성을 보장하는가
4. 누가 삭제와 마이그레이션 책임을 지는가

## ownership 판단 시 쓰지 않는 기준

- 누가 값을 읽는가
- 값이 어디 저장되는가
- 어떤 도구로 전달되는가
- 현재 코드가 어느 workspace에 들어 있는가

