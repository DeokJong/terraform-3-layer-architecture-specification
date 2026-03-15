# Workspace Convention

## 설계 원칙

- Workspace는 Layer와 분리해서 설계한다.
- Resource Set을 먼저 정의하고 필요 시 내부 분리를 검토한다.
- 고위험 resource body와 churn이 높은 binding은 변경 특성이 다르면 분리한다.
- publication은 namespace보다 contract ownership과 migration 경계를 기준으로 둔다.
- 서비스 런타임은 가능한 한 독립 배포 가능해야 한다.
- 규모가 작고 변경 특성이 유사하면 하나의 Resource Set을 하나의 Workspace로 함께 둘 수 있다.

## naming Convention

권장 패턴:

`<layer>-<domain>-<role>`

예:

- `foundation-network-core`
- `user-db`
- `user-db-publication`
- `service-orders-runtime`

역할 suffix 권장:

- `core`
- `binding`
- `publication`
- `runtime`

## 같은 Workspace에 둘 수 있는 경우

- 항상 함께 변경됨
- ownership 동일
- apply 주체 동일
- blast radius 차이 작음
- access rule 변경이 드묾
- publication 변경이 primary resource와 사실상 같은 수명주기를 가짐

대표 예:

- `user-db` cluster + SG allowlist + SSM publication
- `shared-storage` bucket + bucket policy binding + output publication
- `shared-cache` cluster + ingress allowlist + endpoint publication

## 분리해야 하는 신호

- access rule 변경이 잦음
- consumer onboarding이 잦음
- rollback 위험이 다름
- downstream dependency가 많음
- shared primary resource와 서비스별 binding이 섞여 있음
- publication contract를 독립적으로 versioning하거나 migration해야 함

## 빠른 판단 규칙

- "함께 자주 바뀌면 함께 둘 수 있다"
- "consumer onboarding이 잦으면 binding 분리를 먼저 본다"
- "contract migration이 보이면 publication 분리를 본다"
- "rollback 단위가 다르면 workspace를 분리한다"
