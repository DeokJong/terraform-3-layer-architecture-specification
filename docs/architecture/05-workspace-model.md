# Workspace Model

## Workspace 정의

Workspace는 Terraform state, apply, 권한 경계, blast radius를 가지는 운영 단위입니다.

정리:

- Layer = ownership / dependency 모델
- Workspace = state / apply / blast radius 모델

## Workspace 유형

### Core Workspace

- VPC
- Cluster
- RDS
- Shared S3
- KMS Key

특성:

- 변경 빈도 낮음
- blast radius 큼
- 안정성 우선

### Access Workspace

- SG ingress allowlist
- bucket policy attachment
- KMS grants
- consumer binding

특성:

- 변경 빈도 높음
- onboarding / offboarding이 잦음
- core와 분리 가치가 큼

### Publication Workspace

- SSM parameter publication
- Route53 stable endpoint publication
- output aggregation

특성:

- consumer-facing surface를 담당
- source of truth와 분리될 수 있음
- ownership 자체를 가져가지는 않음

### Service Runtime Workspace

- ECS Service
- Lambda stack
- service IAM / SG
- service-specific DNS

## 같은 Workspace에 둘 수 있는 경우

- 항상 함께 변경된다.
- lifecycle이 동일하다.
- ownership이 동일하다.
- blast radius 차이가 크지 않다.
- 운영 주체와 리뷰 주체가 사실상 같다.

예:

- 하나의 shared resource에 대해 core, access, publication을 함께 관리
- 하나의 DB 클러스터에 대해 DB core, SG allowlist, SSM publication을 함께 관리
- 하나의 shared bucket에 대해 bucket, policy binding, output publication을 함께 관리

## 분리를 우선 검토해야 하는 경우

- 변경 빈도가 다르다.
- apply 주체가 다르다.
- rollback 위험이 다르다.
- downstream dependency가 많다.
- core와 access가 섞여 있다.
- 서비스 온보딩이나 access rule 변경이 잦다.
- publication contract를 별도 migration해야 할 가능성이 크다.

## Workspace와 Contract의 관계

Workspace는 Contract를 게시할 수 있지만 Contract owner와 항상 동일하지는 않습니다.

예:

- `platform-db-core`가 DB를 생성한다.
- `platform-db-contract`가 stable endpoint를 SSM이나 DNS에 게시한다.
- Contract owner는 여전히 Platform DB domain이며, publication workspace는 게시 책임만 수행한다.

즉, publication workspace는 source of truth를 대체하지 않습니다.

## Anti-pattern

- 변경 특성이 뚜렷이 다른데도 하나의 workspace가 shared resource의 core, access, publication을 모두 관리
- 서비스 온보딩마다 cluster core workspace를 수정
- shared resource의 policy churn이 core stability를 침범
- aggregation workspace가 사실상 source of truth가 되는 구조

## 권장 구조 예시

Foundation:

- `foundation-network-core`
- `foundation-dns-core`
- `foundation-kms-core`

Platform:

- `platform-cluster-core`
- `platform-db-core`
- `platform-db-access`
- `platform-db-contract`
- `platform-storage-core`
- `platform-storage-access`

Service:

- `service-orders-runtime`
- `service-orders-access`
- `service-orders-contract`

## Workspace 분리 판단 매트릭스

| 질문 | 예 | 답이 "예"면 |
| --- | --- | --- |
| 항상 함께 변경되는가 | DB core와 publication이 항상 같이 수정됨 | 같은 workspace 가능 |
| ownership이 동일한가 | 동일 팀이 lifecycle 전체 관리 | 같은 workspace 가능 |
| access churn이 잦은가 | consumer onboarding이 자주 발생 | access 분리 우선 검토 |
| rollback 위험이 다른가 | core 교체와 policy 수정의 위험도 차이 큼 | 분리 검토 |
| consumer contract migration이 필요한가 | DNS/SSM path 이행 중 | publication 분리 검토 |
| blast radius가 크게 다른가 | 버킷 본체와 policy binding 영향 범위 차이 큼 | 분리 검토 |

## 다음 문서

- [Shared Resources](./06-shared-resources.md)
