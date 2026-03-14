# Safety Convention

## 변경 안전성

- implementation change와 contract change를 구분한다.
- Active Contract는 migration 없이 직접 교체하지 않는다.
- breaking change는 병행 게시 후 전환한다.

## blast radius 제어

- core stability와 access churn이 다르면 분리 검토한다.
- service onboarding 때문에 shared core workspace를 반복 수정하지 않는다.
- publication convenience 때문에 source of truth ownership을 흐리지 않는다.

## rollback 가능성

- workspace는 rollback 단위로 설명 가능해야 한다.
- access 변경 실패가 core resource 변경으로 이어지지 않아야 한다.
- consumer migration 실패 시 기존 contract를 유지할 수 있어야 한다.

## 안전성 anti-pattern

- active contract를 migration 없이 in-place 변경
- shared resource allowlist 변경 때문에 core 전체 apply 필요
- 서비스 하나의 실패가 shared platform core 변경으로 전파
- aggregation output만 남고 실제 provider contract가 흐려지는 구조
