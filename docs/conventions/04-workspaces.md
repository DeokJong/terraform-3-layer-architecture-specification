# Workspace Convention

## 설계 원칙

- Workspace는 Layer와 분리해서 설계한다.
- core와 access는 churn이 다르면 분리한다.
- publication은 ownership보다 consumer-facing surface 기준으로 둔다.
- 서비스 런타임은 가능한 한 독립 배포 가능해야 한다.
- 규모가 작고 변경 특성이 유사하면 core, access, publication을 하나의 Workspace로 함께 둘 수 있다.

## naming Convention

권장 패턴:

`<layer>-<domain>-<role>`

예:

- `foundation-network-core`
- `platform-db-core`
- `platform-db-access`
- `platform-db-contract`
- `service-orders-runtime`

## 같은 Workspace에 둘 수 있는 경우

- 항상 함께 변경됨
- ownership 동일
- apply 주체 동일
- blast radius 차이 작음
- access rule 변경이 드묾
- publication 변경이 core와 사실상 같은 수명주기를 가짐

대표 예:

- DB core + SG allowlist + SSM publication
- bucket core + bucket policy binding + output publication
- Redis core + ingress allowlist + endpoint publication

## 분리해야 하는 신호

- access rule 변경이 잦음
- consumer onboarding이 잦음
- rollback 위험이 다름
- downstream dependency가 많음
- shared core와 서비스별 binding이 섞여 있음
- publication contract를 독립적으로 versioning하거나 migration해야 함

## 빠른 판단 규칙

- 함께 자주 바뀌면 함께 둘 수 있다
- consumer onboarding이 잦으면 access 분리를 먼저 본다
- contract migration이 보이면 publication 분리를 본다
- rollback 단위가 다르면 workspace를 분리한다
