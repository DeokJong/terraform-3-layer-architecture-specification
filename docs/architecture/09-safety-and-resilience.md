# Safety and Resilience

## 목표

이 아키텍처에서 안전성은 다음을 의미합니다.

- 상위 레이어 변경이 하위 레이어 전체 장애로 번지지 않을 것
- shared resource 변경이 불필요하게 넓은 blast radius를 만들지 않을 것
- consumer가 provider 내부 구현 변화에 직접 노출되지 않을 것
- 실패 시 rollback, isolate, migration이 가능할 것

## 안전성 축

### 변경 안전성

- implementation change는 contract change와 분리한다.
- Active Contract는 조용히 의미를 바꾸지 않는다.
- breaking change는 병행 게시와 migration을 통해 수행한다.

### 장애 격리

- shared resource core와 access churn을 필요 시 분리한다.
- 서비스별 rollout 실패가 foundation 또는 shared platform 전체 재적용으로 번지지 않게 한다.
- access 변경이 core stability를 침범하지 않게 한다.

### 참조 안전성

- consumer는 implementation value를 직접 참조하지 않는다.
- service-to-service는 공식 Contract만 사용한다.
- publication surface는 source of truth를 숨기거나 왜곡하지 않는다.

### 복구 가능성

- workspace는 rollback 단위로도 의미가 있어야 한다.
- contract migration은 병행 운영이 가능해야 한다.
- legacy 자산은 즉시 rename보다 안전한 전환을 우선한다.

## 안전성 설계 규칙

- blast radius가 다른 리소스를 무조건 같은 workspace에 넣지 않는다.
- access rule 변경이 잦은 shared resource는 core와 분리 검토한다.
- publication은 consumer 안정성을 높이는 방향으로 설계한다.
- provider는 contract compatibility를 명시적으로 책임진다.
- migration 없는 in-place breaking change를 금지한다.

## 실패 시나리오별 기대 동작

### shared resource access 변경 실패

예:

- DB SG allowlist 변경 실패
- bucket policy binding 오류

기대 동작:

- core resource 자체는 유지된다.
- 실패 범위는 access 정책 변경으로 제한된다.
- 이전 정책으로 rollback 가능해야 한다.

### service rollout 실패

예:

- Service runtime apply 실패
- 신규 consumer onboarding 실패

기대 동작:

- shared platform core는 재생성되거나 흔들리지 않는다.
- 기존 consumer contract는 유지된다.
- 실패한 서비스 단위에서만 복구 작업이 가능해야 한다.

### contract migration 실패

예:

- 새 SSM path 도입 후 일부 consumer 미전환
- 새 DNS contract 전환 중 consumer 혼재

기대 동작:

- 기존 Active Contract는 유지된다.
- 새 Contract는 병행 제공된다.
- consumer별 전환 상태를 추적할 수 있어야 한다.

## 안전성 리뷰 질문

- 이 변경은 어느 레이어까지 blast radius를 가지는가
- 이 값은 implementation인가 contract인가
- 실패 시 기존 consumer를 유지한 채 rollback 가능한가
- access churn이 core stability를 침범하는가
- migration 없이 직접 교체되는 Active Contract가 있는가
- source of truth와 publication이 혼동되고 있지 않은가

## 다음 문서

- [Decision Checklist](./10-decision-checklist.md)
