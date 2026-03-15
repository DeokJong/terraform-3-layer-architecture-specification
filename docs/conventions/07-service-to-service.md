---
title: 서비스 간 통신 규약
doc_section: conventions
nav_parent: conventions-index
nav_order: 8
---

# Service-to-Service Convention

- Service는 다른 Service implementation을 직접 참조하지 않는다.
- 상대 서비스가 게시한 API hostname 또는 공식 계약만 사용한다.
- auth, allowlist, 바인딩은 access dependency로 분리한다.

금지 예:

- 다른 서비스 ALB physical DNS 직접 사용
- 다른 서비스 Secret path 직접 참조
- 다른 서비스 내부 bucket path 직접 의존


