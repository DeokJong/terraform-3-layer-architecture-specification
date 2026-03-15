# Terraform 3-Layer Architecture Conventions

## 1. 목적

이 문서는 3-Layer 아키텍처를 실제 Terraform 코드와 운영 구조에 적용할 때 따라야 하는 naming, ownership, contract, workspace Convention을 정의합니다.

## 2. 문서 사용 원칙

- 구조와 책임은 [terraform-3-layer-architecture-specification.md](./terraform-3-layer-architecture-specification.md)를 따른다.
- 본 문서는 구현 시 반복 적용할 규칙과 판단 기준을 제공한다.
- ADR은 예외 없는 상위 규칙이 아니라 의사결정 배경 기록으로 취급한다.

## 3. Convention 적용 방식

이 문서는 다음 상황에서 사용합니다.

- 새 workspace를 만들 때
- shared resource ownership을 판단할 때
- 계약 naming과 게시 방식을 정할 때
- legacy 자산을 새 기준에 맞춰 재해석할 때

적용 순서:

1. Layer를 결정한다.
2. owner를 결정한다.
3. 계약 여부를 결정한다.
4. 워크스페이스를 분리할지 결정한다.
5. Safety 기준으로 검토한다.

## 4. Layer 분류 Convention

### 4.1 Foundation으로 분류하는 기준

다음 특성이 강하면 Foundation으로 분류합니다.

- 전역 또는 환경 기반 자원이다.
- 여러 상위 영역이 공통으로 사용한다.
- 변경 빈도가 낮다.
- 특정 서비스 lifecycle에 종속되지 않는다.

예:

- VPC
- Subnet
- Hosted Zone
- shared KMS key

### 4.2 Platform으로 분류하는 기준

다음 특성이 강하면 Platform으로 분류합니다.

- 여러 서비스가 공통으로 소비한다.
- shared capability를 제공한다.
- provider로서 stable 계약를 게시한다.
- 서비스별 runtime과 분리된 shared lifecycle을 가진다.

예:

- shared cluster
- shared database
- shared cache
- shared ingress
- shared bucket

### 4.3 Service로 분류하는 기준

다음 특성이 강하면 Service로 분류합니다.

- 특정 서비스와 함께 배포된다.
- 특정 서비스 장애/롤백 단위에 속한다.
- 특정 서비스만을 위한 설정 또는 엔드포인트다.

예:

- service ECS service
- service IAM role
- service ALB
- service DNS

## 5. Ownership Convention

### 5.1 ownership 판단 규칙

다음 질문에 가장 강하게 연결되는 레이어가 owner입니다.

1. 누가 lifecycle을 관리하는가
2. 누가 변경 책임을 지는가
3. 누가 인터페이스 안정성을 보장하는가
4. 누가 삭제와 마이그레이션 책임을 지는가

### 5.2 ownership 판단 시 쓰지 않는 기준

다음은 ownership 기준이 아닙니다.

- 누가 값을 읽는가
- 값이 어디 저장되는가
- 어떤 도구로 전달되는가
- 현재 코드가 어느 workspace에 들어 있는가

## 6. 계약 Convention

### 6.1 계약 설계 원칙

- 하위 레이어는 계약만 소비한다.
- 구현값는 직접 노출하지 않는다.
- 계약는 의미가 안정적이어야 한다.
- 계약 owner는 provider다.

### 6.2 계약 게시 수단

다음은 모두 계약 게시 수단으로 사용할 수 있습니다.

- Terraform output
- SSM Parameter
- Route53 Record
- Secrets Manager reference

게시 수단은 ownership을 바꾸지 않습니다.

### 6.3 계약 naming Convention

원칙:

- 의미 중심 이름을 사용한다.
- 구현 세부사항보다 소비 목적이 드러나야 한다.
- 변경에 강한 stable name을 우선한다.

권장 예:

- `db-main.internal.example.com`
- `/platform/orders/db/host`
- `orders-api.internal.example.com`
- `platform_db_primary_endpoint`

지양 예:

- 물리 리소스명에 과도하게 결합된 이름
- 임시 마이그레이션 의미가 영구 이름에 박힌 이름
- consumer 이름이 뒤섞여 provider 의미가 흐려지는 이름

### 6.4 계약 문서화 Convention

각 계약는 가능하면 아래를 남깁니다.

- 계약 이름
- 타입
- provider
- 주요 consumer
- 게시 방식
- source of truth
- breaking change 절차

### 6.5 계약 lifecycle Convention

- 신규는 `Draft` 또는 `Active`로 시작한다.
- breaking change 시 새 계약를 병행 게시한다.
- 기존 계약는 `Deprecated` 단계를 거친다.
- consumer 전환 후 제거한다.

## 7. 워크스페이스 Convention

### 7.1 워크스페이스 설계 원칙

- 워크스페이스는 Layer와 분리해서 설계한다.
- Resource Set을 먼저 정의하고 필요 시 내부 분리를 검토한다.
- 고위험 resource body와 churn이 높은 바인딩은 변경 특성이 다르면 분리한다.
- 게시은 namespace보다 contract ownership과 마이그레이션 경계를 기준으로 둔다.
- 서비스 런타임은 가능한 한 독립 배포 가능해야 한다.
- 규모가 작고 변경 특성이 유사하면 하나의 Resource Set을 하나의 워크스페이스로 함께 둘 수 있다.

### 7.2 워크스페이스 naming Convention

권장 패턴:

`<layer>-<domain>-<role>`

예:

- `foundation-network-core`
- `foundation-dns-core`
- `user-db`
- `user-db-게시`
- `service-orders-runtime`
- `service-orders-contract`

역할 suffix 권장:

- `core`
- `바인딩`
- `게시`
- `runtime`

### 7.3 같은 워크스페이스에 둘 수 있는 경우

- 항상 함께 변경됨
- ownership 동일
- apply 주체 동일
- 영향 범위 차이 작음
- access rule 변경이 드물음
- 게시 변경이 primary resource와 사실상 같은 수명주기를 가짐

예:

- 단일 shared resource를 한 팀이 관리
- consumer 수가 적음
- access rule 변경이 드묾
- 게시이 단순 stable contract 게시 역할만 함

대표 예:

- `user-db` cluster + SG allowlist + SSM 게시
- `shared-storage` bucket + bucket policy 바인딩 + output 게시
- `shared-cache` cluster + ingress allowlist + endpoint 게시

### 7.4 분리해야 하는 신호

- access rule 변경이 잦음
- consumer onboarding이 잦음
- rollback 위험이 다름
- downstream dependency가 많음
- shared primary resource와 서비스별 바인딩이 섞여 있음
- 게시 contract를 독립적으로 versioning하거나 마이그레이션해야 함

### 7.5 빠른 판단 규칙

- "함께 자주 바뀌면 함께 둘 수 있다"
- "consumer onboarding이 잦으면 바인딩 분리를 먼저 본다"
- "contract 마이그레이션이 보이면 게시 분리를 본다"
- "rollback 단위가 다르면 workspace를 분리한다"

## 8. Network / IAM Convention

### 8.1 Security Group Convention

- ingress rule은 받는 쪽 owner가 관리한다.
- shared producer SG는 Platform이 소유한다.
- 서비스 식별은 가능하면 고정 Client SG로 표현한다.

권장 예:

- `orders-client-sg`
- `billing-client-sg`

### 8.2 IAM Convention

- workload role은 원칙적으로 해당 workload와 함께 선언한다.
- shared platform component role만 Platform ownership을 가질 수 있다.
- 서비스별 role 목록을 Platform이 일반 리소스 관리 목적으로 직접 관리하지 않는다.

## 9. Shared Resource Convention

### 9.1 Resource Set 우선 규칙

shared resource는 먼저 하나의 Resource Set으로 정의합니다. Resource Set은 하나의 명확한 shared capability를 제공하는 리소스 묶음입니다.

권장 예:

- `user-db`
- `book-db`
- `finance-db`
- `shared-cache`
- `shared-ingress`

문서와 설계 검토에서는 가능하면 shared resource를 먼저 Resource Set으로 설명합니다.

### 9.2 내부 분리 판단 기준

Resource Set 내부는 다음 기준이 있을 때 분리를 검토합니다.

- 영향 범위 차이가 큰가
- 변경 빈도가 크게 다른가
- ownership 또는 승인 절차가 다른가
- rollback 경계가 다른가
- 게시 churn이 core 안정성에 영향을 주는가

위 조건이 약하면 하나의 Resource Set 또는 하나의 workspace로 유지할 수 있습니다.

### 9.3 Core / Access / Publication은 선택 패턴

`Core / Access / Publication`은 Resource Set 내부를 설명하는 대표 패턴으로 사용합니다.

- Core: 본체 리소스
- Access: allowlist, attachment, grant, policy 바인딩
- Publication: consumer-facing contract

모든 shared resource에 이 3분할을 강제하지는 않습니다.

### 9.4 대표 적용 예

DB Resource Set:

- `user-db`
- 필요 시 `user-db-core`, `user-db-access`, `user-db-게시`

Storage Resource Set:

- `shared-storage`
- 필요 시 `shared-storage-core`, `shared-storage-access`, `shared-storage-게시`

Redis Resource Set:

- `shared-cache`
- 필요 시 `shared-cache-core`, `shared-cache-access`, `shared-cache-게시`

## 10. Service-to-Service Convention

- Service는 다른 Service implementation을 직접 참조하지 않는다.
- 상대 서비스가 게시한 API hostname 또는 공식 계약만 사용한다.
- auth, allowlist, 바인딩은 access dependency로 분리한다.

금지 예:

- 다른 서비스 ALB physical DNS 직접 사용
- 다른 서비스 Secret path 직접 참조
- 다른 서비스 내부 bucket path 직접 의존

## 11. Legacy Convention

- 기존 naming은 즉시 바꾸지 않는다.
- 기존 자산도 ownership은 새 기준으로 재해석한다.
- 신규 리소스와 신규 계약는 Convention을 우선 적용한다.
- rename보다 병행 게시와 점진 마이그레이션을 우선한다.

## 12. Safety Convention

### 12.1 변경 안전성

- implementation change와 contract change를 구분한다.
- Active 계약는 마이그레이션 없이 직접 교체하지 않는다.
- breaking change는 병행 게시 후 전환한다.

### 12.2 영향 범위 제어

- core stability와 access churn이 다르면 분리 검토한다.
- service onboarding 때문에 shared core workspace를 반복 수정하지 않는다.
- 게시 convenience 때문에 source of truth ownership을 흐리지 않는다.

### 12.3 rollback 가능성

- workspace는 rollback 단위로 설명 가능해야 한다.
- access 변경 실패가 core resource 변경으로 이어지지 않아야 한다.
- consumer 마이그레이션 실패 시 기존 contract를 유지할 수 있어야 한다.

### 12.4 안전성 anti-pattern

- active contract를 마이그레이션 없이 in-place 변경
- shared resource allowlist 변경 때문에 core 전체 apply 필요
- 서비스 하나의 실패가 shared platform core 변경으로 전파
- aggregation output만 남고 실제 provider contract가 흐려지는 구조

## 13. 리뷰 체크리스트

리소스나 계약 추가 시 아래를 확인합니다.

- 이 리소스는 어느 Layer owner인가
- 이 값은 계약인가 구현값인가
- consumer가 아니라 provider가 owner로 표현되었는가
- 워크스페이스 분리가 영향 범위를 줄이는가
- shared resource의 primary resource와 바인딩이 불필요하게 섞여 있지 않은가
- legacy naming이 필요하더라도 의미 해석은 새 기준을 따르는가
- 실패 시 rollback과 병행 마이그레이션이 가능한가

## 14. Concrete Examples

### 14.1 DB Example

| Item | Recommended Placement |
| --- | --- |
| DB cluster | `user-db` |
| SG allowlist | `user-db` or `user-db-바인딩` |
| stable host 게시 | `user-db-게시` |
| app consumer | service runtime consumes contract only |

In a small-scale environment these can still live in one workspace, but frequent onboarding or access churn is the signal to split them.

### 14.2 S3 Example

| Item | Recommended Placement |
| --- | --- |
| shared bucket | `shared-storage` |
| bucket policy 바인딩 | `shared-storage` or `shared-storage-바인딩` |
| public outputs or shared 게시 | `shared-storage-게시` |

### 14.3 Redis Example

| Item | Recommended Placement |
| --- | --- |
| Redis core | `shared-cache` |
| ingress allowlist | `shared-cache` or `shared-cache-바인딩` |
| stable endpoint 게시 | `shared-cache-게시` |

### 14.4 Ingress Example

| Item | Recommended Placement |
| --- | --- |
| shared ingress core | `platform-ingress-core` |
| listener rule 바인딩 or allowlist | `platform-ingress-access` or related access workspace |
| stable hostname | contract or DNS 게시 workspace |

### 14.5 Fast Classification Examples

| Question | Example Answer | Outcome |
| --- | --- | --- |
| Is it consumed by many services | yes | Platform candidate |
| Does it move with one service lifecycle | yes | Service candidate |
| Is it part of global network foundation | yes | Foundation candidate |
| Is it a stable consumer-facing value | yes | 계약 candidate |
| Is it a physical endpoint or internal ID | yes | 구현값 candidate |


